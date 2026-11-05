"""
Práctica 4: expresiones regulares y las dos direcciones del teorema de Kleene.

    analizar             texto en la notación del curso → árbol (Expr)          (Ej. 2)
    construir_afn        Expr → AFN-λ por los casos básicos, unión, concatenación
                         y estrella, con un registro de cada autómata parcial    (Ej. 2)
    de_expresion_a_minimo  AFN-λ → AFN → AFD → AFD mínimo con algoritmos.py      (Ej. 2)
    problemas_de_determinismo  por qué un autómata no es AFD                     (Ej. 3)
    eliminar_estados     AFD → expresión regular, un autómata generalizado por
                         cada estado eliminado                                   (Ej. 3)
    comparar_expresiones dos expresiones son equivalentes si sus AFD mínimos
                         son isomorfos                                           (Ej. 3)
    a_python             notación del curso → sintaxis del módulo re             (Ej. 4)

Notación aceptada por el analizador (la del curso):

* ``+`` unión, yuxtaposición concatenación, ``*`` cerradura de Kleene;
* ``λ`` (también ``ε`` o ``!``, como JFLAP) palabra vacía, ``∅`` (también ``Ø``) lenguaje vacío;
* paréntesis para agrupar; la cerradura liga más que la concatenación y esta más que la unión;
* los espacios se ignoran. Un espacio literal se escribe ``␣``; los caracteres
  ``+ * ( ) \\`` como símbolos del alfabeto se escriben con barra: ``\\+``;
* cualquier otro carácter es un símbolo del alfabeto;
* ``clases`` declara abreviaturas de un carácter para conjuntos de símbolos,
  por ejemplo ``{"D": "0123456789"}`` hace que ``D`` signifique ``0+1+…+9``.

Solo usa la biblioteca estándar, automata.py y algoritmos.py.
"""

from __future__ import annotations

import re as _re
from dataclasses import dataclass, field

from algoritmos import Cadena, ResultadoEquivalencia, de_afn_lambda_a_minimo, equivalentes_por_minimizacion
from automata import LAMBDA, Automata, AutomataInvalido

FORMAS_LAMBDA = ("λ", "ε", "ϵ", "!")
FORMAS_VACIO = ("∅", "Ø")
ESPECIALES = "+*()\\"


# ======================================================================
# Árbol de una expresión regular
# ======================================================================

class Expr:
    """Nodo del árbol. Las subclases son inmutables y se comparan estructuralmente."""

    precedencia = 3  # átomos

    def envuelta(self, minimo: int) -> str:
        s = str(self)
        return f"({s})" if self.precedencia < minimo else s

    def simbolos(self) -> set[str]:
        return set()


@dataclass(frozen=True)
class Vacio(Expr):
    def __str__(self):
        return "∅"


@dataclass(frozen=True)
class Lambda(Expr):
    def __str__(self):
        return "λ"


@dataclass(frozen=True)
class Simbolo(Expr):
    simbolo: str

    def __str__(self):
        c = self.simbolo
        if c == " ":
            return "␣"
        return "\\" + c if c in ESPECIALES else c

    def simbolos(self):
        return {self.simbolo}


@dataclass(frozen=True)
class Clase(Expr):
    """Abreviatura declarada: ``D`` por ``0+1+…+9``."""

    nombre: str
    miembros: tuple

    def __str__(self):
        return self.nombre

    def simbolos(self):
        return set(self.miembros)


@dataclass(frozen=True)
class Union(Expr):
    partes: tuple
    precedencia = 0

    def __str__(self):
        return "+".join(p.envuelta(0) for p in self.partes)

    def simbolos(self):
        return set().union(*(p.simbolos() for p in self.partes))


@dataclass(frozen=True)
class Concat(Expr):
    partes: tuple
    precedencia = 1

    def __str__(self):
        return "".join(p.envuelta(1) for p in self.partes)

    def simbolos(self):
        return set().union(*(p.simbolos() for p in self.partes))


@dataclass(frozen=True)
class Estrella(Expr):
    base: Expr
    precedencia = 2

    def __str__(self):
        return self.base.envuelta(2) + "*"

    def simbolos(self):
        return self.base.simbolos()


VACIO = Vacio()
PALABRA_VACIA = Lambda()


# Constructores que aplican las leyes algebraicas (Hopcroft, Motwani y Ullman, 2007, § 3.4).
# Se usan en la eliminación de estados para que las etiquetas no crezcan con ∅ y λ inútiles.

def union(*partes) -> Expr:
    """r + ∅ = r (3.4.4, ∅ es la identidad de la unión); r + r = r (idempotencia, 3.4.4)."""
    planas = []
    for p in partes:
        for x in (p.partes if isinstance(p, Union) else (p,)):
            if isinstance(x, Vacio) or x in planas:
                continue
            planas.append(x)
    if not planas:
        return VACIO
    return planas[0] if len(planas) == 1 else Union(tuple(planas))


def concat(*partes) -> Expr:
    """∅r = r∅ = ∅ (3.4.4, ∅ es el aniquilador); λr = rλ = r (3.4.2, identidad)."""
    planas = []
    for p in partes:
        for x in (p.partes if isinstance(p, Concat) else (p,)):
            if isinstance(x, Vacio):
                return VACIO
            if isinstance(x, Lambda):
                continue
            planas.append(x)
    if not planas:
        return PALABRA_VACIA
    return planas[0] if len(planas) == 1 else Concat(tuple(planas))


def estrella(r: Expr) -> Expr:
    """∅* = λ, λ* = λ, (r*)* = r*, (λ + r)* = r* (3.4.5, leyes de las cerraduras)."""
    if isinstance(r, (Vacio, Lambda)):
        return PALABRA_VACIA
    if isinstance(r, Estrella):
        return r
    if isinstance(r, Union) and any(isinstance(x, Lambda) for x in r.partes):
        return estrella(union(*[x for x in r.partes if not isinstance(x, Lambda)]))
    return Estrella(r)


# ======================================================================
# Análisis sintáctico
# ======================================================================

class ErrorDeSintaxis(ValueError):
    """La expresión está mal formada; ``posicion`` es el carácter (desde 1) donde se detectó."""

    def __init__(self, mensaje: str, posicion: int, texto: str = ""):
        self.mensaje, self.posicion, self.texto = mensaje, posicion, texto
        super().__init__(f"Posición {posicion}: {mensaje}")

    def senalar(self) -> str:
        """La expresión con un acento circunflejo bajo el carácter del error."""
        return self.texto + "\n" + " " * (self.posicion - 1) + "^"


@dataclass
class _Ficha:
    tipo: str  # "simbolo", "clase", "lambda", "vacio", "+", "*", "(", ")", "fin"
    valor: str
    posicion: int


def _fichas(texto: str, clases: dict) -> list[_Ficha]:
    fichas, i = [], 0
    while i < len(texto):
        c = texto[i]
        pos = i + 1
        if c.isspace():
            i += 1
            continue
        if c == "\\":
            if i + 1 >= len(texto):
                raise ErrorDeSintaxis("la barra invertida debe ir seguida del carácter que escapa.", pos, texto)
            fichas.append(_Ficha("simbolo", texto[i + 1], pos))
            i += 2
            continue
        if c in "+*()":
            fichas.append(_Ficha(c, c, pos))
        elif c in FORMAS_LAMBDA:
            fichas.append(_Ficha("lambda", "λ", pos))
        elif c in FORMAS_VACIO:
            fichas.append(_Ficha("vacio", "∅", pos))
        elif c in clases:
            fichas.append(_Ficha("clase", c, pos))
        elif c == "␣":
            fichas.append(_Ficha("simbolo", " ", pos))
        else:
            fichas.append(_Ficha("simbolo", c, pos))
        i += 1
    fichas.append(_Ficha("fin", "", len(texto) + 1))
    return fichas


_INICIO_DE_OPERANDO = ("simbolo", "clase", "lambda", "vacio", "(")


class _Analizador:
    """Descenso recursivo con la gramática

        union    → concat ('+' concat)*
        concat   → estrella estrella*
        estrella → atomo '*'*
        atomo    → símbolo | clase | λ | ∅ | '(' union ')'
    """

    def __init__(self, texto: str, clases: dict):
        self.texto = texto
        self.clases = clases
        self.fichas = _fichas(texto, clases)
        self.i = 0

    @property
    def actual(self) -> _Ficha:
        return self.fichas[self.i]

    def _que_hay(self) -> str:
        f = self.actual
        return "el final de la expresión" if f.tipo == "fin" else f"«{f.valor}»"

    def analizar(self) -> Expr:
        if self.actual.tipo == "fin":
            raise ErrorDeSintaxis("la expresión está vacía.", 1, self.texto)
        arbol = self.union()
        if self.actual.tipo == ")":
            raise ErrorDeSintaxis("paréntesis de cierre sin su paréntesis de apertura.", self.actual.posicion, self.texto)
        if self.actual.tipo != "fin":  # no debería ocurrir: concat consume todo lo demás
            raise ErrorDeSintaxis(f"no se esperaba {self._que_hay()}.", self.actual.posicion, self.texto)
        return arbol

    def union(self) -> Expr:
        partes = [self.concat()]
        while self.actual.tipo == "+":
            self.i += 1
            partes.append(self.concat())
        return partes[0] if len(partes) == 1 else Union(tuple(partes))

    def concat(self) -> Expr:
        partes = []
        while self.actual.tipo in _INICIO_DE_OPERANDO:
            partes.append(self.estrella())
        if not partes:
            f = self.actual
            if f.tipo == "*":
                msj = "la cerradura * no tiene operando a su izquierda."
            elif f.tipo == "+":
                msj = "la unión + no tiene operando a su izquierda."
            elif f.tipo == ")":
                msj = "falta un operando antes del paréntesis de cierre."
            else:
                msj = f"se esperaba un símbolo, λ, ∅ o «(» y se encontró {self._que_hay()}."
            raise ErrorDeSintaxis(msj, f.posicion, self.texto)
        return partes[0] if len(partes) == 1 else Concat(tuple(partes))

    def estrella(self) -> Expr:
        r = self.atomo()
        while self.actual.tipo == "*":
            self.i += 1
            r = Estrella(r)
        return r

    def atomo(self) -> Expr:
        f = self.actual
        self.i += 1
        if f.tipo == "simbolo":
            return Simbolo(f.valor)
        if f.tipo == "clase":
            return Clase(f.valor, tuple(dict.fromkeys(self.clases[f.valor])))
        if f.tipo == "lambda":
            return PALABRA_VACIA
        if f.tipo == "vacio":
            return VACIO
        # f.tipo == "("
        if self.actual.tipo == ")":
            raise ErrorDeSintaxis("paréntesis vacíos: falta la expresión entre ( y ).", self.actual.posicion, self.texto)
        dentro = self.union()
        if self.actual.tipo != ")":
            raise ErrorDeSintaxis(f"falta el paréntesis de cierre del «(» de la posición {f.posicion}.",
                                  self.actual.posicion, self.texto)
        self.i += 1
        return dentro


def analizar(texto: str, clases: dict | None = None) -> Expr:
    """Árbol de la expresión; lanza ErrorDeSintaxis con la posición si está mal formada."""
    clases = clases or {}
    for nombre in clases:
        if len(nombre) != 1 or nombre in ESPECIALES or nombre in FORMAS_LAMBDA or nombre in FORMAS_VACIO:
            raise ValueError(f"El nombre de clase {nombre!r} debe ser un solo carácter que no sea operador.")
    return _Analizador(texto, clases).analizar()


def alfabeto_de(expr: Expr, alfabeto=None) -> list[str]:
    """Σ: los símbolos de la expresión (ordenados), o el alfabeto dado si los contiene a todos."""
    usados = expr.simbolos()
    if alfabeto is None:
        return sorted(usados)
    alfabeto = list(dict.fromkeys(alfabeto))
    faltan = sorted(usados - set(alfabeto))
    if faltan:
        raise AutomataInvalido("La expresión usa símbolos que no están en Σ: " + ", ".join(faltan) + ".")
    return alfabeto


# ======================================================================
# Teorema de Kleene, parte I: de la expresión al AFN-λ
# ======================================================================

@dataclass
class PasoConstruccion:
    """Un autómata parcial N(r): la regla aplicada y sus estados inicial y final."""

    numero: int
    regla: str  # "símbolo", "λ", "∅", "clase", "unión", "concatenación", "estrella"
    expresion: Expr
    automata: Automata  # solo los estados de N(r)
    inicial: str
    final: str
    operandos: list = field(default_factory=list)  # (inicial, final) de los N(·) combinados
    nuevas: list = field(default_factory=list)  # transiciones añadidas en este paso
    descripcion: str = ""


@dataclass
class ResultadoKleeneI:
    expresion: Expr
    automata: Automata
    pasos: list

    def describir(self) -> list[str]:
        return [f"Paso {p.numero}: N({p.expresion}), {p.regla}. {p.descripcion}" for p in self.pasos]


def _lista(estados) -> str:
    return ", ".join(estados)


def construir_afn(expr: Expr, alfabeto=None, nombre="", prefijo="q") -> ResultadoKleeneI:
    """AFN-λ de la expresión (Hopcroft et al., 2007, teorema 3.7; Sipser, 2013, lema 1.55).

    Cada N(r) tiene un solo estado inicial, sin transiciones de entrada, y un
    solo estado final, sin transiciones de salida:

    * N(a): i -a→ f.   N(λ): i -λ→ f.   N(∅): i y f sin transiciones.
    * N(D) para una clase D = {d₁, …, dₖ}: i -dⱼ→ f para cada dⱼ (es la unión de
      los casos básicos, sin los estados intermedios que la eliminación de λ quitaría).
    * N(r + s): nuevo i con λ hacia los iniciales de N(r) y N(s); λ desde sus
      finales hacia el nuevo f.
    * N(rs): el final de N(r) se une con λ al inicial de N(s).
    * N(r*): nuevos i y f; i -λ→ iᵣ, i -λ→ f, fᵣ -λ→ iᵣ, fᵣ -λ→ f.

    Los estados se numeran en el orden en que se crean (el de un recorrido en
    posorden del árbol), igual que en las construcciones a mano de la Lista 4.
    """
    sigma = alfabeto_de(expr, alfabeto)
    estados: list[str] = []
    transiciones: list[tuple[str, str, str]] = []
    pasos: list[PasoConstruccion] = []

    def nuevo() -> str:
        estados.append(f"{prefijo}{len(estados)}")
        return estados[-1]

    def parcial(propios: list[str], i: str, f: str) -> Automata:
        dentro = set(propios)
        return Automata(sigma, propios, i, {f}, [t for t in transiciones if t[0] in dentro and t[2] in dentro])

    def registrar(regla, nodo, propios, i, f, operandos, nuevas, descripcion):
        pasos.append(PasoConstruccion(len(pasos) + 1, regla, nodo, parcial(propios, i, f), i, f,
                                      operandos, nuevas, descripcion))
        return i, f, propios

    def construir(nodo: Expr):
        if isinstance(nodo, Simbolo):
            i, f = nuevo(), nuevo()
            t = [(i, nodo.simbolo, f)]
            transiciones.extend(t)
            return registrar("símbolo", nodo, [i, f], i, f, [], t,
                             f"caso básico: {i} -{nodo}→ {f}.")
        if isinstance(nodo, Lambda):
            i, f = nuevo(), nuevo()
            t = [(i, LAMBDA, f)]
            transiciones.extend(t)
            return registrar("λ", nodo, [i, f], i, f, [], t, f"caso básico: {i} -λ→ {f}.")
        if isinstance(nodo, Vacio):
            i, f = nuevo(), nuevo()
            return registrar("∅", nodo, [i, f], i, f, [], [],
                             f"caso básico: {i} y {f} sin transiciones; ninguna cadena llega al final.")
        if isinstance(nodo, Clase):
            i, f = nuevo(), nuevo()
            t = [(i, d, f) for d in nodo.miembros]
            transiciones.extend(t)
            miembros = ", ".join(Simbolo(d).__str__() for d in nodo.miembros)
            return registrar("clase", nodo, [i, f], i, f, [], t,
                             f"caso básico para la clase {nodo.nombre} = {{{miembros}}}: {i} -d→ {f} "
                             f"para cada símbolo d de la clase.")
        if isinstance(nodo, Union):
            hijos = [construir(p) for p in nodo.partes]
            i, f = nuevo(), nuevo()
            t = [(i, LAMBDA, hi) for hi, _, _ in hijos] + [(hf, LAMBDA, f) for _, hf, _ in hijos]
            transiciones.extend(t)
            propios = [i] + [q for _, _, pr in hijos for q in pr] + [f]
            return registrar("unión", nodo, propios, i, f, [(hi, hf) for hi, hf, _ in hijos], t,
                             f"nuevo inicial {i} con λ hacia {_lista(hi for hi, _, _ in hijos)} y nuevo final {f} "
                             f"con λ desde {_lista(hf for _, hf, _ in hijos)}.")
        if isinstance(nodo, Concat):
            hijos = [construir(p) for p in nodo.partes]
            t = [(hijos[k][1], LAMBDA, hijos[k + 1][0]) for k in range(len(hijos) - 1)]
            transiciones.extend(t)
            i, f = hijos[0][0], hijos[-1][1]
            propios = [q for _, _, pr in hijos for q in pr]
            return registrar("concatenación", nodo, propios, i, f, [(hi, hf) for hi, hf, _ in hijos], t,
                             "se une con λ el final de cada pieza con el inicial de la siguiente: "
                             + ", ".join(f"{a} -λ→ {b}" for a, _, b in t) + f"; inicial {i}, final {f}.")
        if isinstance(nodo, Estrella):
            hi, hf, pr = construir(nodo.base)
            i, f = nuevo(), nuevo()
            t = [(i, LAMBDA, hi), (i, LAMBDA, f), (hf, LAMBDA, hi), (hf, LAMBDA, f)]
            transiciones.extend(t)
            return registrar("estrella", nodo, [i] + pr + [f], i, f, [(hi, hf)], t,
                             f"nuevos {i} (inicial) y {f} (final); {i} -λ→ {hi} entra, {hf} -λ→ {hi} repite, "
                             f"{hf} -λ→ {f} sale y {i} -λ→ {f} acepta λ.")
        raise TypeError(type(nodo))

    i, f, _ = construir(expr)
    aut = Automata(sigma, estados, i, {f}, transiciones, nombre or str(expr)).validar()
    return ResultadoKleeneI(expr, aut, pasos)


@dataclass
class CadenaExpresion:
    """Todo el camino de una expresión: árbol, AFN-λ con sus pasos y los tres autómatas de la Práctica 3."""

    texto: str
    expresion: Expr
    construccion: ResultadoKleeneI
    cadena: Cadena

    @property
    def afn_lambda(self) -> Automata:
        return self.construccion.automata

    @property
    def minimo(self) -> Automata:
        return self.cadena.minimo.automata

    def acepta(self, w) -> bool:
        return self.minimo.acepta(w)

    def tamanos(self) -> dict:
        return {"AFN-λ": len(self.afn_lambda.estados), "AFN": len(self.cadena.sin_lambda.automata.estados),
                "AFD": len(self.cadena.subconjuntos.automata.estados), "AFD mínimo": len(self.minimo.estados)}


def de_expresion_a_minimo(texto: str, clases=None, alfabeto=None, nombre="") -> CadenaExpresion:
    expr = analizar(texto, clases)
    nombre = nombre or texto.replace(" ", "")
    c = construir_afn(expr, alfabeto, nombre)
    return CadenaExpresion(texto, expr, c, de_afn_lambda_a_minimo(c.automata))


# ======================================================================
# Teorema de Kleene, parte II: del autómata a la expresión por eliminación de estados
# ======================================================================

def problemas_de_determinismo(aut: Automata) -> list[str]:
    """Por qué el autómata no es un AFD: cada transición λ y cada δ(q, a) con más de un destino."""
    problemas = []
    orden = {q: k for k, q in enumerate(aut.estados)}
    for (q, a), destinos in sorted(aut.transiciones.items(), key=lambda k: (orden.get(k[0][0], 1e9), k[0][1])):
        if not destinos:
            continue
        if a == LAMBDA:
            problemas.append(f"El estado {q} tiene una transición λ hacia {', '.join(sorted(destinos))}.")
        elif len(destinos) > 1:
            problemas.append(f"δ({q}, {a}) = {{{', '.join(sorted(destinos))}}} tiene {len(destinos)} destinos.")
    return problemas


def transiciones_faltantes(aut: Automata) -> list[tuple[str, str]]:
    """Los pares (q, a) con δ(q, a) = ∅: no impiden el determinismo (sumidero implícito)."""
    return [(q, a) for q in aut.estados for a in aut.alfabeto if not aut.destinos(q, a)]


@dataclass
class PasoEliminacion:
    numero: int
    titulo: str
    eliminado: str | None
    estados: list
    etiquetas: dict  # (p, r) -> Expr, solo las distintas de ∅
    detalles: list = field(default_factory=list)

    def generalizado(self) -> Automata:
        """El autómata generalizado como Automata cuyos «símbolos» son las expresiones, para dibujarlo."""
        trans = [(p, str(e), r) for (p, r), e in self.etiquetas.items()]
        return Automata([t[1] for t in trans], self.estados, self.estados[0], {self.estados[-1]}, trans)


@dataclass
class ResultadoEliminacion:
    automata: Automata
    expresion: Expr
    pasos: list
    orden: list
    inicial: str
    final: str
    final_nuevo: bool

    def describir(self) -> list[str]:
        return [f"{p.titulo}" + ("".join("\n   " + d for d in p.detalles)) for p in self.pasos]


def eliminar_estados(aut: Automata, orden=None, nombre_final="f", requerir_afd=True) -> ResultadoEliminacion:
    """Expresión regular de L(M) por eliminación de estados (Hopcroft et al., 2007, § 3.2.2).

    1. Si hay varios estados finales, o el único final es el inicial, se agrega
       un final nuevo unido con λ desde los finales (como *Make Single Noninitial
       Final State* de JFLAP). Las transiciones paralelas se combinan en una
       unión y los pares sin transición llevan ∅.
    2. Se elimina cada estado q que no es el inicial ni el final: para cada par
       (p, r) de los demás, R(p, r) := R(p, r) + R(p, q) R(q, q)* R(q, r).
    3. Quedan el inicial i y el final f: con R = R(i, i), S = R(i, f), U = R(f, f)
       y T = R(f, i), la expresión es (R + S U* T)* S U*.
    """
    if requerir_afd:
        problemas = problemas_de_determinismo(aut)
        if problemas:
            raise AutomataInvalido("El autómata no es determinista:\n" + "\n".join(problemas))
    inicial = aut.inicial
    estados = list(aut.estados)
    final_nuevo = not (len(aut.aceptacion) == 1 and inicial not in aut.aceptacion)
    if final_nuevo:
        final = nombre_final
        while final in estados:
            final += "'"
        estados.append(final)
    else:
        final = next(iter(aut.aceptacion))
    # Etiquetas iniciales.
    etiquetas: dict[tuple[str, str], Expr] = {}
    for (q, a), destinos in aut.transiciones.items():
        for p in destinos:
            etiquetas[q, p] = union(etiquetas.get((q, p), VACIO), Simbolo(a) if a != LAMBDA else PALABRA_VACIA)
    if final_nuevo:
        for q in aut.estados:
            if q in aut.aceptacion:
                etiquetas[q, final] = PALABRA_VACIA
    orden = list(orden) if orden else [q for q in aut.estados if q not in (inicial, final)]
    intermedios = [q for q in aut.estados if q not in (inicial, final)]
    if sorted(orden) != sorted(intermedios):
        raise AutomataInvalido("El orden de eliminación debe contener exactamente los estados que no son "
                               "ni el inicial ni el final: " + ", ".join(intermedios) + ".")
    pasos: list[PasoEliminacion] = []

    def foto(titulo, eliminado, detalles):
        vivos = [inicial] + [q for q in estados if q not in (inicial, final)] + [final]
        pasos.append(PasoEliminacion(len(pasos), titulo, eliminado, vivos,
                                     {k: v for k, v in etiquetas.items() if not isinstance(v, Vacio)}, detalles))

    detalles = []
    if final_nuevo:
        detalles.append(f"Se agrega el final nuevo {final} con λ desde "
                        + ", ".join(q for q in aut.estados if q in aut.aceptacion) + ".")
    combinadas = [f"{p} -{e}→ {r}" for (p, r), e in etiquetas.items() if isinstance(e, Union)]
    if combinadas:
        detalles.append("Transiciones paralelas combinadas: " + "; ".join(combinadas) + ".")
    foto("Autómata generalizado inicial" + (" (con el final nuevo)" if final_nuevo else ""), None, detalles)

    for q in orden:
        lazo = etiquetas.get((q, q), VACIO)
        entradas = [(p, e) for (p, r), e in etiquetas.items() if r == q and p != q]
        salidas = [(r, e) for (p, r), e in etiquetas.items() if p == q and r != q]
        detalles = [f"Lazo R({q}, {q}) = {lazo}; entradas desde " + (", ".join(p for p, _ in entradas) or "nadie")
                    + "; salidas hacia " + (", ".join(r for r, _ in salidas) or "nadie") + "."]
        for p, e_in in entradas:
            for r, e_out in salidas:
                camino = concat(e_in, estrella(lazo), e_out)
                antes = etiquetas.get((p, r), VACIO)
                etiquetas[p, r] = union(antes, camino)
                detalles.append(f"R({p}, {r}) = {antes} + {e_in}({lazo})*{e_out} = {etiquetas[p, r]}")
        for k in [k for k in etiquetas if q in k]:
            del etiquetas[k]
        estados.remove(q)
        foto(f"Se elimina {q}", q, detalles)

    R, S = etiquetas.get((inicial, inicial), VACIO), etiquetas.get((inicial, final), VACIO)
    U, T = etiquetas.get((final, final), VACIO), etiquetas.get((final, inicial), VACIO)
    expresion = concat(estrella(union(R, concat(S, estrella(U), T))), S, estrella(U))
    pasos.append(PasoEliminacion(len(pasos), f"Quedan {inicial} y {final}: (R + S U* T)* S U*", None,
                                 [inicial, final], {k: v for k, v in etiquetas.items() if not isinstance(v, Vacio)},
                                 [f"R = R({inicial}, {inicial}) = {R}", f"S = R({inicial}, {final}) = {S}",
                                  f"U = R({final}, {final}) = {U}", f"T = R({final}, {inicial}) = {T}",
                                  f"Expresión: {expresion}"]))
    return ResultadoEliminacion(aut, expresion, pasos, orden, inicial, final, final_nuevo)


# ======================================================================
# Equivalencia de expresiones
# ======================================================================

@dataclass
class ComparacionExpresiones:
    primera: CadenaExpresion
    segunda: CadenaExpresion
    resultado: ResultadoEquivalencia

    @property
    def equivalentes(self) -> bool:
        return self.resultado.equivalentes


def comparar_expresiones(er1: str, er2: str, clases=None) -> ComparacionExpresiones:
    """Dos expresiones denotan el mismo lenguaje si y solo si sus AFD mínimos son isomorfos (Práctica 3, § 2.4)."""
    c1 = de_expresion_a_minimo(er1, clases, nombre="primera")
    c2 = de_expresion_a_minimo(er2, clases, nombre="segunda")
    return ComparacionExpresiones(c1, c2, equivalentes_por_minimizacion(c1.minimo, c2.minimo))


def equivalente_al_automata(er: str, aut: Automata, clases=None) -> ResultadoEquivalencia:
    """La expresión contra un autómata cualquiera, por minimización e isomorfismo."""
    c = de_expresion_a_minimo(er, clases, alfabeto=list(dict.fromkeys(list(aut.alfabeto) + sorted(analizar(er, clases).simbolos()))))
    return equivalentes_por_minimizacion(c.minimo, aut)


# ======================================================================
# Traducción a la sintaxis del módulo re
# ======================================================================

def _clase_re(miembros) -> str:
    dentro = "".join("\\" + c if c in "\\]^-" else c for c in miembros)
    return f"[{dentro}]"


def a_python(expr: Expr | str, clases=None, _contexto=0) -> str:
    """Notación del curso → patrón para re.fullmatch.

    + es |, la yuxtaposición se conserva, * se conserva, λ es el grupo vacío
    (?:) y ∅ es (?!) (una aserción que nunca se cumple). Las clases son
    clases de caracteres [...]. Los metacaracteres de re se escapan.
    ``_contexto``: 0 = libre, 1 = dentro de una concatenación, 2 = operando de *.
    """
    if isinstance(expr, str):
        expr = analizar(expr, clases)
    if isinstance(expr, Simbolo):
        return _re.escape(expr.simbolo)
    if isinstance(expr, Clase):
        return _clase_re(expr.miembros)
    if isinstance(expr, Lambda):
        return "(?:)"
    if isinstance(expr, Vacio):
        return "(?!)"
    if isinstance(expr, Union):
        dentro = "|".join(a_python(p, _contexto=0) for p in expr.partes)
        return f"(?:{dentro})" if _contexto else dentro
    if isinstance(expr, Concat):
        dentro = "".join(a_python(p, _contexto=1) for p in expr.partes)
        return f"(?:{dentro})" if _contexto == 2 else dentro
    if isinstance(expr, Estrella):
        s = a_python(expr.base, _contexto=2) + "*"
        return f"(?:{s})" if _contexto == 2 else s  # re no admite a**: se escribe (?:a*)*
    raise TypeError(type(expr))


def patron(texto: str, clases=None):
    return _re.compile(a_python(analizar(texto, clases)))


# ======================================================================
# Archivos .jff de expresiones (JFLAP: <type>re</type>, con ! por λ)
# ======================================================================

def escribir_expresion_jff(expr: Expr | str) -> str:
    texto = str(expr).replace("λ", "!").replace("␣", " ")
    texto = texto.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return ('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n'
            "<!--Creado con practica2-tc (src/expresiones.py).-->\n"
            "<structure>\n\t<type>re</type>\n\t<expression>" + texto + "</expression>\n</structure>\n")


def leer_expresion_jff(texto: str) -> str:
    import xml.etree.ElementTree as ET
    try:
        raiz = ET.fromstring(texto)
    except ET.ParseError as err:
        raise ValueError(f"El archivo no es XML válido: {err}") from err
    if raiz.tag != "structure" or (raiz.findtext("type") or "").strip() != "re":
        raise ValueError("El archivo no es una expresión regular de JFLAP (<type>re</type>).")
    return (raiz.findtext("expression") or "").strip().replace("!", "λ")
