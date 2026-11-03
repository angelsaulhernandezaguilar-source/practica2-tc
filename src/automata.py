"""
Nucleo del simulador: autómatas finitos (AFD, AFND y AFND-λ).

Este módulo no importa Flet ni ningún formato de archivo. La interfaz
(app.py) y la lectura/escritura de archivos (formatos.py) dependen de él,
nunca al revés; por eso se prueba con pytest sin abrir ninguna ventana.

Convención para λ: la cadena vacía "" como símbolo leído en una transición.
Es la misma convención del elemento <read/> vacío de JFLAP y de los
formatos .json y .xml de este proyecto (ver docs/03-simulador.md).

El autómata es la quíntupla M = (Q, Σ, δ, q0, F):

* ``estados``      Q, lista ordenada de nombres (cadenas).
* ``alfabeto``     Σ, lista ordenada de símbolos (cadenas no vacías).
* ``transiciones`` δ, diccionario {(estado, símbolo): conjunto de destinos};
  el símbolo "" es λ.
* ``inicial``      q0.
* ``aceptacion``   F, conjunto de estados.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field
from itertools import product

LAMBDA = ""

AFD = "AFD"
AFND = "AFND"
AFND_LAMBDA = "AFND-lambda"


class AutomataInvalido(ValueError):
    """La quíntupla no está bien formada (estado o símbolo desconocido, etc.)."""


def mostrar_cadena(w) -> str:
    """Muestra una cadena (o lista de símbolos) escribiendo la vacía como λ."""
    if not isinstance(w, str):
        w = "".join(w) if all(len(s) == 1 for s in w) else " ".join(w)
    return w if w else "λ"


def mostrar_conjunto(conjunto) -> str:
    return "{" + ", ".join(sorted(conjunto)) + "}" if conjunto else "∅"


def separar(texto: str) -> list[str]:
    """Divide una lista escrita por el usuario ("q0, q1" o "{q0,q1}"); ∅, - y vacío no dan elementos."""
    texto = (texto or "").strip().strip("{}").strip()
    if texto in ("", "∅", "-", "—"):
        return []
    return [t.strip() for t in texto.split(",") if t.strip()]


def desde_tabla(alfabeto: str, estados: str, inicial: str, aceptacion, celdas: dict, nombre="") -> "Automata":
    """Construye el autómata a partir de lo que el usuario escribió en la tabla interactiva.

    ``celdas`` es {(estado, símbolo): texto}; el símbolo "" es la columna λ y
    cada texto es una lista de destinos separados por comas.
    """
    sigma, q = separar(alfabeto), separar(estados)
    trans = [(origen, a, p) for (origen, a), texto in celdas.items() for p in separar(texto)]
    return Automata(sigma, q, (inicial or "").strip(), set(aceptacion), trans, nombre).validar()


@dataclass
class Paso:
    """Un paso de la simulación: se leyó ``simbolo`` estando en ``antes``.

    ``tomadas`` son las transiciones (origen, símbolo, destino) usadas al
    leer el símbolo; ``por_lambda`` las transiciones λ que se siguieron
    después para cerrar el conjunto.
    """

    indice: int
    simbolo: str
    antes: frozenset
    despues: frozenset
    tomadas: list = field(default_factory=list)
    por_lambda: list = field(default_factory=list)


@dataclass
class Camino:
    """Un camino completo en el árbol de cómputo de una cadena."""

    movimientos: list  # [(origen, símbolo o "", destino)]
    final: str
    leidos: int  # símbolos consumidos antes de terminar o morir
    acepta: bool

    def texto(self, inicial: str) -> str:
        partes = [inicial]
        for _, a, p in self.movimientos:
            partes.append(f"-{a or 'λ'}→ {p}")
        return " ".join(partes)


class Automata:
    def __init__(self, alfabeto, estados, inicial, aceptacion, transiciones=(), nombre=""):
        self.nombre = nombre
        self.alfabeto = list(dict.fromkeys(alfabeto))
        self.estados = list(dict.fromkeys(estados))
        self.inicial = inicial
        self.aceptacion = set(aceptacion)
        self.transiciones: dict[tuple[str, str], set[str]] = {}
        if isinstance(transiciones, dict):
            transiciones = [(q, a, p) for (q, a), destinos in transiciones.items() for p in destinos]
        for q, a, p in transiciones:
            self.agregar(q, a, p)

    # ------------------------------------------------------------------
    # Construcción y validación
    # ------------------------------------------------------------------

    def agregar(self, origen, simbolo, destino):
        self.transiciones.setdefault((origen, simbolo), set()).add(destino)

    def quitar(self, origen, simbolo, destino=None):
        if destino is None:
            self.transiciones.pop((origen, simbolo), None)
            return
        destinos = self.transiciones.get((origen, simbolo), set())
        destinos.discard(destino)
        if not destinos:
            self.transiciones.pop((origen, simbolo), None)

    def errores(self) -> list[str]:
        """Lista de problemas de la quíntupla; vacía si está bien formada."""
        e = []
        if not self.estados:
            e.append("Q está vacío.")
        if any(not isinstance(a, str) or a == "" for a in self.alfabeto):
            e.append("Σ no puede contener la cadena vacía: λ no es un símbolo del alfabeto.")
        if self.inicial not in self.estados:
            e.append(f"El estado inicial {self.inicial!r} no pertenece a Q.")
        for q in sorted(self.aceptacion - set(self.estados)):
            e.append(f"El estado de aceptación {q!r} no pertenece a Q.")
        for (q, a), destinos in sorted(self.transiciones.items()):
            if q not in self.estados:
                e.append(f"δ({q}, {a or 'λ'}) parte de un estado que no está en Q.")
            if a != LAMBDA and a not in self.alfabeto:
                e.append(f"δ({q}, {a}) usa un símbolo que no está en Σ.")
            for p in sorted(destinos - set(self.estados)):
                e.append(f"δ({q}, {a or 'λ'}) llega a {p!r}, que no está en Q.")
        return e

    def validar(self):
        e = self.errores()
        if e:
            raise AutomataInvalido("\n".join(e))
        return self

    def copia(self, nombre=None) -> "Automata":
        return Automata(
            self.alfabeto, self.estados, self.inicial, self.aceptacion,
            {k: set(v) for k, v in self.transiciones.items()},
            self.nombre if nombre is None else nombre,
        )

    def __eq__(self, otro):
        """Igualdad estructural de la quíntupla (no de lenguajes)."""
        if not isinstance(otro, Automata):
            return NotImplemented
        limpia = lambda t: {k: v for k, v in t.items() if v}
        return (
            set(self.alfabeto) == set(otro.alfabeto)
            and set(self.estados) == set(otro.estados)
            and self.inicial == otro.inicial
            and self.aceptacion == otro.aceptacion
            and limpia(self.transiciones) == limpia(otro.transiciones)
        )

    def __repr__(self):
        return (f"Automata({self.tipo}, |Q|={len(self.estados)}, Σ={self.alfabeto}, "
                f"q0={self.inicial}, F={sorted(self.aceptacion)})")

    # ------------------------------------------------------------------
    # Clasificación
    # ------------------------------------------------------------------

    @property
    def tiene_lambda(self) -> bool:
        return any(a == LAMBDA and d for (_, a), d in self.transiciones.items())

    @property
    def es_determinista(self) -> bool:
        """Sin λ y con a lo sumo un destino por (estado, símbolo)."""
        return not self.tiene_lambda and all(len(d) <= 1 for d in self.transiciones.values())

    @property
    def es_completo(self) -> bool:
        return self.es_determinista and all(
            len(self.transiciones.get((q, a), ())) == 1 for q in self.estados for a in self.alfabeto
        )

    @property
    def tipo(self) -> str:
        if self.tiene_lambda:
            return AFND_LAMBDA
        return AFD if self.es_determinista else AFND

    def num_transiciones(self) -> int:
        return sum(len(d) for d in self.transiciones.values())

    # ------------------------------------------------------------------
    # Funciones de transición
    # ------------------------------------------------------------------

    def destinos(self, q, a) -> set:
        return self.transiciones.get((q, a), set())

    def clausura(self, estados) -> frozenset:
        """λ-clausura: los estados alcanzables con cero o más transiciones λ."""
        if isinstance(estados, str):
            estados = {estados}
        vistos = set(estados)
        pila = list(estados)
        while pila:
            q = pila.pop()
            for p in self.destinos(q, LAMBDA):
                if p not in vistos:
                    vistos.add(p)
                    pila.append(p)
        return frozenset(vistos)

    def mover(self, estados, a) -> frozenset:
        """δ(S, a): unión de δ(q, a) para q en S, sin cerrar."""
        return frozenset(p for q in estados for p in self.destinos(q, a))

    def delta_gorro(self, estados, w) -> frozenset:
        """δ̂(S, w) = Cl(δ(δ̂(S, w'), a)), con δ̂(S, λ) = Cl(S)."""
        if isinstance(estados, str):
            estados = {estados}
        actuales = self.clausura(estados)
        for a in self.simbolos(w):
            actuales = self.clausura(self.mover(actuales, a))
        return actuales

    def simbolos(self, w) -> list[str]:
        """Divide una cadena en símbolos de Σ.

        Si todos los símbolos tienen un carácter, cada carácter es un símbolo.
        Si hay símbolos de varios caracteres, se aceptan separados por espacios
        o comas, o se toma en cada posición el símbolo más largo que coincida.
        """
        if not isinstance(w, str):
            return list(w)
        if all(len(a) == 1 for a in self.alfabeto):
            return list(w)
        if any(s in w for s in " ,"):
            return [t for t in w.replace(",", " ").split() if t]
        resultado, i = [], 0
        por_longitud = sorted(self.alfabeto, key=len, reverse=True)
        while i < len(w):
            for a in por_longitud:
                if w.startswith(a, i):
                    resultado.append(a)
                    i += len(a)
                    break
            else:
                resultado.append(w[i])
                i += 1
        return resultado

    def acepta(self, w) -> bool:
        return bool(self.delta_gorro({self.inicial}, w) & self.aceptacion)

    # ------------------------------------------------------------------
    # Simulación documentada
    # ------------------------------------------------------------------

    def traza(self, w) -> list[Paso]:
        """Simulación por conjuntos: un Paso por símbolo, más el paso 0 (λ-clausura inicial).

        En un AFD cada conjunto tiene un solo estado y la traza es el recorrido
        clásico; en un AFND es el conjunto de estados activos (todos los
        caminos a la vez).
        """
        inicio = frozenset({self.inicial})
        cerrado = self.clausura(inicio)
        pasos = [Paso(0, LAMBDA, inicio, cerrado, [], self._lambdas_usadas(inicio, cerrado))]
        actuales = cerrado
        for i, a in enumerate(self.simbolos(w), 1):
            movidos = self.mover(actuales, a)
            tomadas = sorted((q, a, p) for q in actuales for p in self.destinos(q, a))
            cerrado = self.clausura(movidos)
            pasos.append(Paso(i, a, actuales, cerrado, tomadas, self._lambdas_usadas(movidos, cerrado)))
            actuales = cerrado
        return pasos

    def _lambdas_usadas(self, origen, cerrado):
        """Transiciones λ entre estados del conjunto cerrado (las que forman la clausura)."""
        return sorted((q, LAMBDA, p) for q in cerrado for p in self.destinos(q, LAMBDA))

    def caminos(self, w, limite=64) -> tuple[list[Camino], bool]:
        """Árbol de cómputo: todos los caminos desde q0 al leer w.

        Cada camino termina cuando consume toda la cadena (acepta o rechaza
        según el estado final) o cuando muere (no hay transición). Los ciclos
        de transiciones λ se cortan: un camino no repite un estado sin haber
        leído un símbolo. Devuelve (caminos, truncado).
        """
        simbolos = self.simbolos(w)
        resultado: list[Camino] = []
        truncado = False
        pila = [(self.inicial, 0, [], frozenset({self.inicial}))]
        while pila:
            if len(resultado) >= limite:
                truncado = True
                break
            q, i, movs, vistos_lambda = pila.pop()
            siguientes = []
            if i < len(simbolos):
                for p in sorted(self.destinos(q, simbolos[i]), reverse=True):
                    siguientes.append((p, i + 1, movs + [(q, simbolos[i], p)], frozenset({p})))
            for p in sorted(self.destinos(q, LAMBDA), reverse=True):
                if p not in vistos_lambda:
                    siguientes.append((p, i, movs + [(q, LAMBDA, p)], vistos_lambda | {p}))
            if i == len(simbolos):
                # Terminó de leer: este camino es un resultado aunque pueda seguir por λ.
                resultado.append(Camino(movs, q, i, q in self.aceptacion))
                pila.extend(s for s in siguientes if s[1] == i)
            elif not siguientes:
                resultado.append(Camino(movs, q, i, False))
            else:
                pila.extend(siguientes)
        return resultado, truncado

    # ------------------------------------------------------------------
    # Transformaciones
    # ------------------------------------------------------------------

    def renombrar(self, mapa: dict, nombre=None) -> "Automata":
        return Automata(
            self.alfabeto,
            [mapa[q] for q in self.estados],
            mapa[self.inicial],
            {mapa[q] for q in self.aceptacion},
            [(mapa[q], a, mapa[p]) for (q, a), d in self.transiciones.items() for p in d],
            self.nombre if nombre is None else nombre,
        )

    def accesibles(self) -> list[str]:
        """Estados alcanzables desde q0 (BFS, en orden de descubrimiento)."""
        vistos, cola = [self.inicial], deque([self.inicial])
        while cola:
            q = cola.popleft()
            for a in [LAMBDA] + self.alfabeto:
                for p in sorted(self.destinos(q, a)):
                    if p not in vistos:
                        vistos.append(p)
                        cola.append(p)
        return vistos

    def sin_inaccesibles(self) -> "Automata":
        utiles = set(self.accesibles())
        return Automata(
            self.alfabeto,
            [q for q in self.estados if q in utiles],
            self.inicial,
            self.aceptacion & utiles,
            [(q, a, p) for (q, a), d in self.transiciones.items() if q in utiles for p in d],
            self.nombre,
        )

    def completar(self, sumidero="∅") -> "Automata":
        """Agrega un estado de rechazo para que δ sea total (solo AFD)."""
        if not self.es_determinista:
            raise AutomataInvalido("Solo un AFD puede completarse con un estado sumidero.")
        if self.es_completo:
            return self.copia()
        nuevo = self.copia()
        while sumidero in nuevo.estados:
            sumidero += "'"
        nuevo.estados.append(sumidero)
        for q in nuevo.estados:
            for a in nuevo.alfabeto:
                if not nuevo.destinos(q, a):
                    nuevo.agregar(q, a, sumidero)
        return nuevo

    def sin_lambda(self, nombre=None) -> "Automata":
        """AFND-λ → AFND equivalente con los mismos estados.

        δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}.
        """
        trans = []
        for q in self.estados:
            cq = self.clausura({q})
            for a in self.alfabeto:
                for p in self.clausura(self.mover(cq, a)):
                    trans.append((q, a, p))
        finales = {q for q in self.estados if self.clausura({q}) & self.aceptacion}
        return Automata(self.alfabeto, self.estados, self.inicial, finales, trans,
                        self.nombre if nombre is None else nombre)

    def subconjuntos(self, completo=True, nombre=None) -> "Automata":
        """Construcción de subconjuntos (Rabin y Scott, 1959), solo estados accesibles.

        Cada estado del AFD se llama como el conjunto de estados del autómata
        original, p. ej. "{A, B}". El conjunto vacío es el estado sumidero "∅"
        y solo aparece si ``completo`` es verdadero.
        """
        inicio = self.clausura({self.inicial})
        orden, cola, trans = [inicio], deque([inicio]), []
        while cola:
            s = cola.popleft()
            for a in self.alfabeto:
                t = self.clausura(self.mover(s, a))
                if not t and not completo:
                    continue
                if t not in orden:
                    orden.append(t)
                    cola.append(t)
                trans.append((s, a, t))
        nombre_de = {s: mostrar_conjunto(s) for s in orden}
        return Automata(
            self.alfabeto,
            [nombre_de[s] for s in orden],
            nombre_de[inicio],
            {nombre_de[s] for s in orden if s & self.aceptacion},
            [(nombre_de[s], a, nombre_de[t]) for s, a, t in trans],
            self.nombre if nombre is None else nombre,
        )

    def minimizar(self, nombre=None) -> "Automata":
        """AFD mínimo por el algoritmo de Hopcroft (1971).

        Primero se quitan los inaccesibles y se completa δ; después se refina
        la partición {F, Q - F} con la estrategia "procesar el bloque menor".
        Los estados del resultado se llaman como el bloque: "{q1, q3}".
        """
        base = self if self.es_determinista else self.subconjuntos()
        base = base.sin_inaccesibles().completar()
        estados = set(base.estados)
        inversa: dict[tuple[str, str], set[str]] = {}
        for (q, a), d in base.transiciones.items():
            for p in d:
                inversa.setdefault((p, a), set()).add(q)
        finales = frozenset(base.aceptacion)
        no_finales = frozenset(estados - finales)
        particion = {b for b in (finales, no_finales) if b}
        pendientes = {min(particion, key=len)} if len(particion) == 2 else set(particion)
        while pendientes:
            divisor = pendientes.pop()
            for a in base.alfabeto:
                x = {q for p in divisor for q in inversa.get((p, a), ())}
                for y in list(particion):
                    dentro, fuera = y & x, y - x
                    if dentro and fuera:
                        particion.remove(y)
                        dentro, fuera = frozenset(dentro), frozenset(fuera)
                        particion |= {dentro, fuera}
                        if y in pendientes:
                            pendientes.remove(y)
                            pendientes |= {dentro, fuera}
                        else:
                            pendientes.add(min(dentro, fuera, key=len))
        bloque_de = {q: b for b in particion for q in b}
        # Orden de los bloques: el del recorrido BFS del AFD completo.
        orden = []
        for q in base.accesibles():
            if bloque_de[q] not in orden:
                orden.append(bloque_de[q])
        nombre_de = {b: (next(iter(b)) if len(b) == 1 else mostrar_conjunto(b)) for b in orden}
        trans = {(nombre_de[bloque_de[q]], a, nombre_de[bloque_de[p]])
                 for (q, a), d in base.transiciones.items() for p in d}
        return Automata(
            base.alfabeto, [nombre_de[b] for b in orden], nombre_de[bloque_de[base.inicial]],
            {nombre_de[b] for b in orden if b & finales}, sorted(trans),
            self.nombre if nombre is None else nombre,
        )

    def numerar(self, prefijo="q", nombre=None) -> "Automata":
        """Renombra los estados q0, q1, … en el orden del recorrido BFS desde q0."""
        orden = self.accesibles() + [q for q in self.estados if q not in self.accesibles()]
        return self.renombrar({q: f"{prefijo}{i}" for i, q in enumerate(orden)}, nombre)

    # ------------------------------------------------------------------
    # Comparación de lenguajes
    # ------------------------------------------------------------------

    def contraejemplo(self, otro: "Automata"):
        """Cadena más corta en la diferencia simétrica de L(self) y L(otro); None si son equivalentes."""
        alfabeto = sorted(set(self.alfabeto) | set(otro.alfabeto))
        inicio = (self.clausura({self.inicial}), otro.clausura({otro.inicial}))
        vistos, cola = {inicio: ""}, deque([inicio])
        while cola:
            s, t = cola.popleft()
            w = vistos[(s, t)]
            if bool(s & self.aceptacion) != bool(t & otro.aceptacion):
                return w
            for a in alfabeto:
                par = (self.clausura(self.mover(s, a)), otro.clausura(otro.mover(t, a)))
                if par not in vistos:
                    vistos[par] = w + a if len(a) == 1 else (w + " " + a).strip()
                    cola.append(par)
        return None

    def equivalente(self, otro: "Automata") -> bool:
        return self.contraejemplo(otro) is None

    def cadenas_aceptadas(self, longitud_max: int, cuantas: int | None = None):
        """Palabras aceptadas en orden canónico (longitud y luego orden de Σ)."""
        encontradas = []
        for n in range(longitud_max + 1):
            for t in product(self.alfabeto, repeat=n):
                if self.acepta(list(t)):
                    encontradas.append("".join(t))
                    if cuantas is not None and len(encontradas) >= cuantas:
                        return encontradas
        return encontradas

    def tabla(self) -> list[list[str]]:
        """Tabla de transiciones: encabezado y un renglón por estado (→ inicial, * aceptación)."""
        columnas = self.alfabeto + ([LAMBDA] if self.tiene_lambda else [])
        filas = [["Estado"] + [a or "λ" for a in columnas]]
        for q in self.estados:
            marca = ("→" if q == self.inicial else "") + ("*" if q in self.aceptacion else "")
            celdas = []
            for a in columnas:
                d = self.destinos(q, a)
                if self.es_determinista and len(d) == 1:
                    celdas.append(next(iter(d)))
                else:
                    celdas.append(mostrar_conjunto(d) if d else ("—" if self.es_determinista else "∅"))
            filas.append([marca + q] + celdas)
        return filas
