"""
Práctica 3: los algoritmos que llevan un AFN-λ a un AFD mínimo, paso a paso.

Cada función devuelve el autómata resultante y el registro de lo que hizo
(las filas de la tabla conforme se generan, las rondas de la partición, las
transiciones añadidas...). La interfaz (app.py) solo muestra ese registro, y
las pruebas lo revisan sin abrir ninguna ventana.

    clausura_lambda      Cl(q) con la pila del recorrido            (§ 2.1)
    simular_directo      AFN-λ sin convertir: activos antes/después  (§ 2.1)
    eliminar_lambda      AFN-λ → AFN sin λ                          (§ 2.2)
    construir_subconjuntos  AFN → AFD, solo subconjuntos alcanzables (§ 2.3)
    minimizar_afd        AFD → AFD mínimo por refinamiento de particiones (§ 2.4)
    isomorfismo / equivalentes_por_minimizacion                     (§ 2.4)
    validar_lote / informe_lote                                     (§ 2.5)

Cada resultado lleva ``operaciones``: el número de consultas a δ que hizo el
algoritmo, para contrastarlo con las estimaciones de docs/ (Ejercicio 3).
Solo usa la biblioteca estándar y el núcleo de automata.py.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field
from itertools import product

from automata import LAMBDA, Automata, AutomataInvalido, mostrar_cadena, mostrar_conjunto

SUMIDERO = "∅"


def _orden(aut: Automata, conjunto) -> list[str]:
    """Los estados de ``conjunto`` en el orden en que aparecen en Q."""
    pos = {q: i for i, q in enumerate(aut.estados)}
    return sorted(conjunto, key=lambda q: (pos.get(q, len(pos)), q))


def _conj(aut: Automata, conjunto) -> str:
    """{A, B} con los estados en el orden de Q (∅ si está vacío)."""
    return "{" + ", ".join(_orden(aut, conjunto)) + "}" if conjunto else "∅"


def _bloque(aut: Automata, bloque) -> str:
    """Un bloque de la partición entre corchetes, [A, B], para no confundirlo con un estado {A, B}."""
    return "[" + ", ".join(_orden(aut, bloque)) + "]"


# ======================================================================
# 2.1 Cerradura λ
# ======================================================================

@dataclass
class Clausura:
    """Cl(estado) y cómo se obtuvo.

    ``arcos`` son las transiciones λ (q, p) que agregaron un estado nuevo, en
    el orden en que se descubrieron; ``pasos`` es la narración de la pila.
    """

    estado: str
    resultado: frozenset
    arcos: list = field(default_factory=list)
    pasos: list = field(default_factory=list)
    operaciones: int = 0


def _cerrar(aut: Automata, inicio) -> tuple[frozenset, list, list, int]:
    """Cl(S) por recorrido en profundidad con una pila explícita."""
    vistos = list(_orden(aut, inicio))
    pila = list(reversed(vistos))
    arcos, pasos, ops = [], [], 0
    pasos.append(f"Se parte de {_conj(aut, vistos)}: todo estado está en su propia cerradura (cero transiciones λ).")
    while pila:
        q = pila.pop()
        destinos = _orden(aut, aut.destinos(q, LAMBDA))
        ops += 1
        nuevos = [p for p in destinos if p not in vistos]
        if not destinos:
            pasos.append(f"Se saca {q} de la pila: δ({q}, λ) = ∅, no agrega nada.")
        elif not nuevos:
            pasos.append(f"Se saca {q} de la pila: δ({q}, λ) = {_conj(aut, destinos)}, todos ya estaban.")
        else:
            pasos.append(f"Se saca {q} de la pila: δ({q}, λ) = {_conj(aut, destinos)}; "
                         f"se agrega{'n' if len(nuevos) > 1 else ''} {', '.join(nuevos)}.")
        for p in nuevos:
            vistos.append(p)
            arcos.append((q, p))
        pila.extend(reversed(nuevos))
    resultado = frozenset(vistos)
    pasos.append(f"La pila quedó vacía: Cl = {_conj(aut, resultado)}.")
    return resultado, arcos, pasos, ops


def clausura_lambda(aut: Automata, estado) -> Clausura:
    """Cl(q): los estados alcanzables desde q con cero o más transiciones λ.

    Si ``estado`` es un conjunto, devuelve Cl(S) = ⋃ Cl(q).
    """
    inicio = {estado} if isinstance(estado, str) else set(estado)
    for q in inicio:
        if q not in aut.estados:
            raise AutomataInvalido(f"{q!r} no pertenece a Q.")
    resultado, arcos, pasos, ops = _cerrar(aut, inicio)
    nombre = estado if isinstance(estado, str) else _conj(aut, inicio)
    return Clausura(nombre, resultado, arcos, pasos, ops)


def clausuras(aut: Automata) -> dict[str, Clausura]:
    """Cl(q) para cada estado de Q, en el orden de Q."""
    return {q: clausura_lambda(aut, q) for q in aut.estados}


# ======================================================================
# 2.1 Simulación directa de un AFN-λ
# ======================================================================

@dataclass
class PasoDirecto:
    """Un paso de la simulación directa.

    Paso 0: ``antes`` = {q0} y ``despues`` = Cl({q0}). Paso i: con los
    activos ``previos`` se lee ``simbolo``; ``antes`` = δ(previos, a), el
    conjunto antes de aplicar la cerradura, y ``despues`` = Cl(antes).
    """

    indice: int
    simbolo: str
    previos: frozenset
    antes: frozenset
    despues: frozenset
    tomadas: list = field(default_factory=list)  # (q, a, p) al leer el símbolo
    por_lambda: list = field(default_factory=list)  # (q, p) λ que agregaron estados

    def describir(self, aut: Automata) -> str:
        if self.indice == 0:
            texto = (f"Paso 0 (antes de leer): activos {_conj(aut, self.antes)}; "
                     f"tras la cerradura λ: {_conj(aut, self.despues)}.")
        else:
            tomadas = "; ".join(f"δ({q}, {a}) ∋ {p}" for q, a, p in self.tomadas) or "ninguna"
            texto = (f"Paso {self.indice}: se lee {self.simbolo} desde {_conj(aut, self.previos)}. "
                     f"Transiciones: {tomadas}. Antes de la cerradura: {_conj(aut, self.antes)}; "
                     f"después de la cerradura λ: {_conj(aut, self.despues)}.")
        if self.por_lambda:
            texto += " λ seguidas: " + ", ".join(f"{q} -λ→ {p}" for q, p in self.por_lambda) + "."
        return texto


@dataclass
class SimulacionDirecta:
    cadena: str
    pasos: list
    acepta: bool
    simbolos_fuera: list = field(default_factory=list)
    operaciones: int = 0


def simular_directo(aut: Automata, w) -> SimulacionDirecta:
    """Simula el AFN-λ sin convertirlo: S₀ = Cl({q0}), Sᵢ = Cl(δ(Sᵢ₋₁, aᵢ)); acepta si Sₙ ∩ F ≠ ∅."""
    simbolos = aut.simbolos(w)
    fuera = sorted({a for a in simbolos if a not in aut.alfabeto})
    inicio = frozenset({aut.inicial})
    cerrado, arcos, _, ops = _cerrar(aut, inicio)
    pasos = [PasoDirecto(0, LAMBDA, frozenset(), inicio, cerrado, [], arcos)]
    actuales = cerrado
    for i, a in enumerate(simbolos, 1):
        tomadas = []
        for q in _orden(aut, actuales):
            ops += 1
            tomadas += [(q, a, p) for p in _orden(aut, aut.destinos(q, a))]
        movidos = frozenset(p for _, _, p in tomadas)
        cerrado, arcos, _, k = _cerrar(aut, movidos)
        ops += k
        pasos.append(PasoDirecto(i, a, actuales, movidos, cerrado, tomadas, arcos))
        actuales = cerrado
    texto = w if isinstance(w, str) else "".join(w)
    return SimulacionDirecta(texto, pasos, bool(actuales & aut.aceptacion), fuera, ops)


# ======================================================================
# 2.2 Eliminación de transiciones λ
# ======================================================================

@dataclass
class FilaSinLambda:
    """δ'(q, a) = Cl(δ(Cl(q), a)) para cada símbolo a."""

    estado: str
    clausura: frozenset
    movidos: dict  # a -> δ(Cl(q), a)
    destinos: dict  # a -> Cl(δ(Cl(q), a))
    aceptacion: bool


@dataclass
class ResultadoSinLambda:
    automata: Automata
    filas: list
    agregadas: list  # (q, a, p) de δ' que no estaban en δ
    quitadas: list  # (q, p) transiciones λ eliminadas
    nuevas_aceptacion: list  # q ∉ F con Cl(q) ∩ F ≠ ∅
    operaciones: int = 0

    def describir(self) -> list[str]:
        aut = self.automata
        lineas = []
        for f in self.filas:
            partes = [f"δ'({f.estado}, {a}) = Cl(δ({_conj(aut, f.clausura)}, {a})) = Cl({_conj(aut, f.movidos[a])}) "
                      f"= {_conj(aut, f.destinos[a])}" for a in aut.alfabeto]
            lineas.append(f"Cl({f.estado}) = {_conj(aut, f.clausura)}. " + "; ".join(partes) + ".")
        return lineas


def eliminar_lambda(aut: Automata, nombre=None) -> ResultadoSinLambda:
    """AFN-λ → AFN sin λ con los mismos estados (Hopcroft, Motwani y Ullman, 2007, § 2.5.5).

    δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q ∈ Q : Cl(q) ∩ F ≠ ∅}.
    """
    cl, ops = {}, 0
    for q in aut.estados:
        cl[q], _, _, k = _cerrar(aut, {q})
        ops += k
    filas, trans = [], []
    for q in aut.estados:
        movidos, destinos = {}, {}
        for a in aut.alfabeto:
            m = set()
            for r in cl[q]:
                ops += 1
                m |= aut.destinos(r, a)
            movidos[a] = frozenset(m)
            destinos[a] = frozenset().union(*(cl[p] for p in m)) if m else frozenset()
            trans += [(q, a, p) for p in _orden(aut, destinos[a])]
        filas.append(FilaSinLambda(q, cl[q], movidos, destinos, bool(cl[q] & aut.aceptacion)))
    finales = {f.estado for f in filas if f.aceptacion}
    nuevo = Automata(aut.alfabeto, aut.estados, aut.inicial, finales, trans,
                     f"{aut.nombre}_sin_lambda" if nombre is None else nombre)
    agregadas = [(q, a, p) for q, a, p in trans if p not in aut.destinos(q, a)]
    quitadas = [(q, p) for q in aut.estados for p in _orden(aut, aut.destinos(q, LAMBDA))]
    nuevas = [q for q in aut.estados if q in finales and q not in aut.aceptacion]
    return ResultadoSinLambda(nuevo, filas, agregadas, quitadas, nuevas, ops)


# ======================================================================
# 2.3 Construcción de subconjuntos
# ======================================================================

@dataclass
class FilaSubconjunto:
    """Un renglón de la tabla del AFD, en el orden en que se procesa."""

    conjunto: frozenset
    destinos: dict  # a -> conjunto
    nuevos: list  # conjuntos que este renglón descubrió
    aceptacion: bool
    razon: frozenset  # S ∩ F


@dataclass
class ResultadoSubconjuntos:
    automata: Automata
    original: Automata
    filas: list
    nombres: dict  # conjunto -> nombre del estado del AFD
    operaciones: int = 0

    def describir(self) -> list[str]:
        aut, lineas = self.original, []
        for k, f in enumerate(self.filas, 1):
            partes = [f"δ_D({_conj(aut, f.conjunto)}, {a}) = {_conj(aut, f.destinos[a])}" for a in aut.alfabeto]
            linea = f"Renglón {k}: " + "; ".join(partes) + "."
            if f.nuevos:
                linea += " Nuevos: " + ", ".join(_conj(aut, s) for s in f.nuevos) + "."
            if f.aceptacion:
                linea += f" Es de aceptación porque S ∩ F = {_conj(aut, f.razon)} ≠ ∅."
            lineas.append(linea)
        return lineas


def construir_subconjuntos(aut: Automata, nombre=None, completo=True) -> ResultadoSubconjuntos:
    """AFN → AFD (Rabin y Scott, 1959; Hopcroft et al., 2007, § 2.3.5), solo subconjuntos alcanzables.

    El estado inicial es {q0} (Cl({q0}) si el AFN tiene λ) y
    δ_D(S, a) = ⋃_{q ∈ S} δ(q, a) (cerrado con λ si las hay). S es de
    aceptación si S ∩ F ≠ ∅. Con ``completo`` el conjunto vacío es el estado
    sumidero ∅, para que δ_D sea total como pide la definición de AFD.
    """
    con_lambda = aut.tiene_lambda
    ops = 0

    def cerrar(s):
        nonlocal ops
        if not con_lambda:
            return frozenset(s)
        r, _, _, k = _cerrar(aut, s)
        ops += k
        return r

    inicio = cerrar({aut.inicial})
    orden, cola, filas = [inicio], deque([inicio]), []
    while cola:
        s = cola.popleft()
        destinos, nuevos = {}, []
        for a in aut.alfabeto:
            m = set()
            for q in s:
                ops += 1
                m |= aut.destinos(q, a)
            t = cerrar(m)
            destinos[a] = t
            if (t or completo) and t not in orden:
                orden.append(t)
                cola.append(t)
                nuevos.append(t)
        filas.append(FilaSubconjunto(s, destinos, nuevos, bool(s & aut.aceptacion), frozenset(s & aut.aceptacion)))
    nombres = {s: _conj(aut, s) for s in orden}
    trans = [(nombres[f.conjunto], a, nombres[t]) for f in filas for a, t in f.destinos.items() if t in nombres]
    afd = Automata(aut.alfabeto, [nombres[s] for s in orden], nombres[inicio],
                   {nombres[f.conjunto] for f in filas if f.aceptacion}, trans,
                   f"{aut.nombre}_afd" if nombre is None else nombre)
    return ResultadoSubconjuntos(afd, aut, filas, nombres, ops)


# ======================================================================
# 2.4 Minimización por refinamiento de particiones
# ======================================================================

@dataclass
class Ronda:
    """La partición Πₖ y, para cada bloque que se dividió en esta ronda, la causa."""

    numero: int
    bloques: list  # lista de frozensets
    divisiones: list = field(default_factory=list)  # (bloque viejo, [(bloque nuevo, firma)])


@dataclass
class ResultadoMinimo:
    automata: Automata
    base: Automata  # el AFD sin inaccesibles y completo sobre el que se refinó
    inaccesibles: list
    sumidero: str | None
    rondas: list
    bloque_de: dict  # estado de base -> nombre del estado mínimo
    operaciones: int = 0

    def describir(self) -> list[str]:
        b = self.base
        lineas = []
        if self.inaccesibles:
            lineas.append("Inaccesibles eliminados: " + ", ".join(self.inaccesibles) + ".")
        else:
            lineas.append("No hay estados inaccesibles.")
        if self.sumidero:
            lineas.append(f"δ era parcial: se agregó el estado sumidero {self.sumidero}.")
        for r in self.rondas:
            linea = f"Π{r.numero} = {{ " + ", ".join(_bloque(b, x) for x in r.bloques) + " }"
            if r.numero == 0:
                linea += "  (F y Q − F)"
            for viejo, partes in r.divisiones:
                linea += (f"\n   {_conj(b, viejo)} se divide: " +
                          "; ".join(f"{_conj(b, nuevo)} van a {firma}" for nuevo, firma in partes))
            lineas.append(linea)
        lineas.append(f"Π{self.rondas[-1].numero} = Π{self.rondas[-1].numero - 1}: la partición es estable."
                      if len(self.rondas) > 1 else "La partición inicial ya es estable.")
        return lineas


def minimizar_afd(aut: Automata, nombre=None) -> ResultadoMinimo:
    """AFD → AFD mínimo (Hopcroft et al., 2007, § 4.4.3 y § 4.4.4).

    1. Se eliminan los estados inaccesibles (recorrido en anchura desde q0).
    2. Si δ es parcial, se agrega un estado sumidero.
    3. Π₀ = {F, Q − F}; en la ronda k+1 dos estados de un mismo bloque siguen
       juntos solo si, para cada símbolo, van a un mismo bloque de Πₖ. Se
       termina cuando Πₖ₊₁ = Πₖ; cada bloque es un estado del AFD mínimo.
    """
    if not aut.es_determinista:
        raise AutomataInvalido("La minimización requiere un AFD: aplique antes la construcción de subconjuntos.")
    accesibles = aut.accesibles()
    inaccesibles = [q for q in aut.estados if q not in accesibles]
    base = aut.sin_inaccesibles()
    sumidero = None
    if not base.es_completo:
        base = base.completar(SUMIDERO)
        sumidero = base.estados[-1]
    ops = 0
    finales = [q for q in base.estados if q in base.aceptacion]
    resto = [q for q in base.estados if q not in base.aceptacion]
    bloques = [frozenset(x) for x in (finales, resto) if x]
    rondas = [Ronda(0, bloques)]
    while True:
        indice = {q: i for i, b in enumerate(bloques) for q in b}
        nuevos, divisiones = [], []
        for b in bloques:
            grupos: dict[tuple, list] = {}
            for q in base.estados:
                if q in b:
                    firma = []
                    for a in base.alfabeto:
                        ops += 1
                        firma.append(indice[next(iter(base.destinos(q, a)))])
                    grupos.setdefault(tuple(firma), []).append(q)
            partes = [frozenset(g) for g in grupos.values()]
            nuevos += partes
            if len(partes) > 1:
                divisiones.append((b, [(p, ", ".join(f"{a}→{_bloque(base, bloques[i])}"
                                                     for a, i in zip(base.alfabeto, f)))
                                       for p, f in zip(partes, grupos.keys())]))
        rondas.append(Ronda(len(rondas), nuevos, divisiones))
        if len(nuevos) == len(bloques):
            break
        bloques = nuevos
    # Nombres y orden de los estados del mínimo: recorrido en anchura desde el bloque inicial.
    bloque = {q: b for b in bloques for q in b}
    orden = []
    for q in base.accesibles():
        if bloque[q] not in orden:
            orden.append(bloque[q])
    nombre_de = {b: (next(iter(b)) if len(b) == 1 else _bloque(base, b)) for b in orden}
    trans = sorted({(nombre_de[bloque[q]], a, nombre_de[bloque[p]])
                    for (q, a), d in base.transiciones.items() for p in d})
    minimo = Automata(base.alfabeto, [nombre_de[b] for b in orden], nombre_de[bloque[base.inicial]],
                      {nombre_de[b] for b in orden if b & base.aceptacion}, trans,
                      f"{aut.nombre}_min" if nombre is None else nombre)
    return ResultadoMinimo(minimo, base, inaccesibles, sumidero, rondas,
                           {q: nombre_de[bloque[q]] for q in base.estados}, ops)


# ======================================================================
# 2.4 Equivalencia de dos AFD por sus autómatas mínimos
# ======================================================================

def isomorfismo(m1: Automata, m2: Automata) -> dict | None:
    """Biyección φ: Q₁ → Q₂ con φ(q0₁) = q0₂, φ(δ₁(q, a)) = δ₂(φ(q), a) y q ∈ F₁ ⇔ φ(q) ∈ F₂.

    Los dos autómatas deben ser AFD completos y sin inaccesibles (como los que
    da ``minimizar_afd``). Se recorren a la par desde los estados iniciales:
    como δ es una función, el único candidato para φ queda forzado.
    """
    if set(m1.alfabeto) != set(m2.alfabeto) or len(m1.estados) != len(m2.estados):
        return None
    phi = {m1.inicial: m2.inicial}
    cola = deque([m1.inicial])
    while cola:
        q = cola.popleft()
        if (q in m1.aceptacion) != (phi[q] in m2.aceptacion):
            return None
        for a in m1.alfabeto:
            d1, d2 = m1.destinos(q, a), m2.destinos(phi[q], a)
            if len(d1) != 1 or len(d2) != 1:
                return None
            p1, p2 = next(iter(d1)), next(iter(d2))
            if p1 in phi:
                if phi[p1] != p2:
                    return None
            else:
                phi[p1] = p2
                cola.append(p1)
    if len(phi) != len(m1.estados) or len(set(phi.values())) != len(phi):
        return None
    return phi


@dataclass
class ResultadoEquivalencia:
    equivalentes: bool
    minimo1: ResultadoMinimo
    minimo2: ResultadoMinimo
    mapa: dict | None
    motivo: str


def _a_afd(aut: Automata, alfabeto) -> Automata:
    """El AFD sobre ``alfabeto`` que se minimiza: el mismo si ya es determinista, o sus subconjuntos."""
    extendido = Automata(alfabeto, aut.estados, aut.inicial, aut.aceptacion,
                         {k: set(v) for k, v in aut.transiciones.items()}, aut.nombre)
    if extendido.es_determinista:
        return extendido
    return construir_subconjuntos(eliminar_lambda(extendido).automata).automata


def equivalentes_por_minimizacion(a1: Automata, a2: Automata) -> ResultadoEquivalencia:
    """Dos autómatas son equivalentes si y solo si sus AFD mínimos coinciden salvo el nombre de los estados.

    Es consecuencia de la unicidad del AFD mínimo (Hopcroft et al., 2007,
    § 4.4.4): todo AFD mínimo de L es isomorfo al de las clases de Myhill-Nerode.
    """
    alfabeto = list(dict.fromkeys(list(a1.alfabeto) + list(a2.alfabeto)))
    r1 = minimizar_afd(_a_afd(a1, alfabeto))
    r2 = minimizar_afd(_a_afd(a2, alfabeto))
    m1, m2 = r1.automata, r2.automata
    mapa = isomorfismo(m1, m2)
    if mapa is not None:
        motivo = ("Los AFD mínimos tienen " + str(len(m1.estados)) + " estados y coinciden salvo el nombre: "
                  + ", ".join(f"{q} ↔ {p}" for q, p in mapa.items()) + ".")
    elif len(m1.estados) != len(m2.estados):
        motivo = f"Los AFD mínimos tienen {len(m1.estados)} y {len(m2.estados)} estados: no son isomorfos."
    else:
        motivo = "Los AFD mínimos tienen el mismo número de estados, pero ninguna biyección respeta δ, q0 y F."
    return ResultadoEquivalencia(mapa is not None, r1, r2, mapa, motivo)


# ======================================================================
# 2.5 Validación de varias cadenas
# ======================================================================

@dataclass
class ResultadoCadena:
    linea: int
    cadena: str
    acepta: bool
    simbolos_fuera: list


def leer_cadenas(texto: str) -> list[str]:
    """Una cadena por línea. Una línea vacía o con «λ» es la cadena vacía.

    Se quitan los espacios de los extremos y el retorno de carro de Windows.
    Las líneas que empiezan con # son comentarios y se ignoran.
    """
    cadenas = []
    for linea in texto.splitlines():
        linea = linea.strip()
        if linea.startswith("#"):
            continue
        cadenas.append("" if linea == "λ" else linea)
    return cadenas


def validar_lote(aut: Automata, texto: str) -> list[ResultadoCadena]:
    resultados = []
    for i, w in enumerate(leer_cadenas(texto), 1):
        sim = simular_directo(aut, w)
        resultados.append(ResultadoCadena(i, w, sim.acepta, sim.simbolos_fuera))
    return resultados


def informe_lote(aut: Automata, resultados: list[ResultadoCadena], origen="") -> str:
    """Informe en texto: una línea por cadena (número, cadena, veredicto) y un resumen."""
    aceptadas = sum(r.acepta for r in resultados)
    ancho = max([len(mostrar_cadena(r.cadena)) for r in resultados] + [6])
    lineas = [
        "Informe de validación de cadenas",
        f"Autómata: {aut.nombre or 'sin nombre'} ({aut.tipo}, {len(aut.estados)} estados, Σ = {{{', '.join(aut.alfabeto)}}})",
        f"Archivo de cadenas: {origen or '(texto)'}",
        f"Método: simulación directa con cerradura λ",
        "",
        f"{'#':>4}  {'cadena':<{ancho}}  resultado",
    ]
    for r in resultados:
        veredicto = "ACEPTADA" if r.acepta else "RECHAZADA"
        if r.simbolos_fuera:
            veredicto += f" (símbolos fuera de Σ: {', '.join(r.simbolos_fuera)})"
        lineas.append(f"{r.linea:>4}  {mostrar_cadena(r.cadena):<{ancho}}  {veredicto}")
    lineas += ["", f"Total: {len(resultados)} cadenas; {aceptadas} aceptadas y {len(resultados) - aceptadas} rechazadas."]
    return "\n".join(lineas) + "\n"


# ======================================================================
# Cadena completa y comparación exhaustiva (2.6)
# ======================================================================

@dataclass
class Cadena:
    """Los cuatro autómatas de la Práctica 3 a partir de uno dado."""

    original: Automata
    sin_lambda: ResultadoSinLambda
    subconjuntos: ResultadoSubconjuntos
    minimo: ResultadoMinimo

    @property
    def automatas(self) -> list[Automata]:
        return [self.original, self.sin_lambda.automata, self.subconjuntos.automata, self.minimo.automata]


def de_afn_lambda_a_minimo(aut: Automata) -> Cadena:
    sl = eliminar_lambda(aut)
    sc = construir_subconjuntos(sl.automata)
    mn = minimizar_afd(sc.automata)
    return Cadena(aut, sl, sc, mn)


def palabras(alfabeto, n: int):
    """Σ⁰ ∪ Σ¹ ∪ … ∪ Σⁿ en orden canónico."""
    for k in range(n + 1):
        for t in product(alfabeto, repeat=k):
            yield list(t)


def profundidad_producto(automatas: list[Automata]) -> int:
    """Mayor distancia, en símbolos, desde la configuración inicial a una configuración alcanzable
    del producto de los autómatas simulados por conjuntos.

    Si todos coinciden en las cadenas de longitud ≤ esta profundidad, coinciden
    en todas: toda configuración (S₁, …, Sₖ) alcanzable se alcanza con una
    cadena de esa longitud o menor, y el veredicto de cada autómata depende
    solo de su Sᵢ.
    """
    alfabeto = list(dict.fromkeys(a for m in automatas for a in m.alfabeto))
    inicio = tuple(m.clausura({m.inicial}) for m in automatas)
    dist, cola = {inicio: 0}, deque([inicio])
    while cola:
        c = cola.popleft()
        for a in alfabeto:
            d = tuple(m.clausura(m.mover(s, a)) for m, s in zip(automatas, c))
            if d not in dist:
                dist[d] = dist[c] + 1
                cola.append(d)
    return max(dist.values())
