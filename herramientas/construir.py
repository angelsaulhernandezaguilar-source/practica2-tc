"""Constructores de autómatas para el catálogo de ejercicios.

* ``afd``          AFD a partir de un "estado abstracto" (lo que el autómata
                   debe recordar) y una función de transición sobre él. Los
                   estados se numeran q0, q1, … en el orden del recorrido BFS
                   y se guarda qué significa cada uno.
* ``busqueda``     AFD de búsqueda de un patrón (función de fallo, como KMP).
* ``thompson``     AFND-λ de una expresión regular (Thompson, 1968).
* ``tabla``        Transcripción de una tabla de la lista: "A: B C; B: …".
* ``er_a_python``  Traduce la sintaxis del curso (+, λ, ∅) a la del módulo re.
"""

from __future__ import annotations

import re
from collections import deque

from automata import LAMBDA, Automata

MUERTO = "muerto"


def afd(alfabeto, inicio, delta, acepta, describir=str, minimo=True, nombre=""):
    """AFD total cuyos estados son los valores abstractos alcanzables desde ``inicio``.

    ``delta(estado, símbolo)`` devuelve el estado abstracto siguiente, o None
    para el estado de rechazo absorbente. Con ``minimo`` se fusionan, con el
    algoritmo de Hopcroft, los estados abstractos que resulten equivalentes.
    Devuelve (autómata, {nombre: significado}).
    """
    orden, cola, trans = [inicio], deque([inicio]), []
    while cola:
        s = cola.popleft()
        for a in alfabeto:
            t = MUERTO if s == MUERTO else delta(s, a)
            t = MUERTO if t is None else t
            if t not in orden:
                orden.append(t)
                cola.append(t)
            trans.append((s, a, t))
    nombres = {s: f"q{i}" for i, s in enumerate(orden)}
    significado = {nombres[s]: ("rechazo absorbente" if s == MUERTO else describir(s)) for s in orden}
    m = Automata(list(alfabeto), [nombres[s] for s in orden], nombres[inicio],
                 {nombres[s] for s in orden if s != MUERTO and acepta(s)},
                 [(nombres[s], a, nombres[t]) for s, a, t in trans], nombre)
    if minimo:
        m, significado = fusionar(m, significado)
    return m, significado


def fusionar(m: Automata, significado: dict):
    """Minimiza conservando el significado de los estados fusionados y renumera q0, q1, …"""
    minimo = m.minimizar()
    if len(minimo.estados) == len(m.sin_inaccesibles().estados):
        return m, significado
    nuevo = {}
    for q in minimo.estados:
        partes = re.findall(r"q\d+|∅", q) if q.startswith("{") else [q]
        nuevo[q] = " o bien ".join(significado.get(p, p) for p in partes)
    numerado = minimo.numerar(nombre=m.nombre)
    mapa = dict(zip(minimo.accesibles() + [q for q in minimo.estados if q not in minimo.accesibles()],
                    numerado.accesibles() + [q for q in numerado.estados if q not in numerado.accesibles()]))
    return numerado, {mapa[q]: v for q, v in nuevo.items()}


def busqueda(patron: str, alfabeto, modo="contiene", nombre=""):
    """AFD de búsqueda de ``patron``: el estado j indica que los últimos j símbolos coinciden
    con el prefijo de longitud j del patrón (el más largo posible).

    modo = "contiene" (el estado final es absorbente), "termina" o "empieza".
    """
    n = len(patron)

    def siguiente(j, a):
        if modo == "empieza":
            if j == n:
                return n
            return j + 1 if patron[j] == a else None
        if j == n and modo == "contiene":
            return n
        w = patron[:j] + a
        for k in range(min(len(w), n), -1, -1):
            if w.endswith(patron[:k]):
                return k
        return 0

    def describir(j):
        return f"los últimos símbolos coinciden con «{patron[:j]}»" if j else "ningún avance en el patrón"

    if modo == "empieza":
        describir = lambda j: f"se ha leído el prefijo «{patron[:j]}»" if j < n else f"el prefijo «{patron}» ya apareció"
    elif modo == "contiene":
        _d = describir
        describir = lambda j: f"«{patron}» ya apareció" if j == n else _d(j)
    return afd(alfabeto, 0, siguiente, lambda j: j == n, describir, nombre=nombre)


# ----------------------------------------------------------------------
# Expresiones regulares
# ----------------------------------------------------------------------

def _tokens(er: str):
    er = er.replace(" ", "").replace("ε", "λ")
    for c in er:
        yield c


class _Analizador:
    """Gramática: union := concat ('+' concat)* ; concat := estrella+ ; estrella := atomo '*'*."""

    def __init__(self, er):
        self.t = list(_tokens(er))
        self.i = 0

    def ver(self):
        return self.t[self.i] if self.i < len(self.t) else None

    def tomar(self):
        c = self.ver()
        self.i += 1
        return c

    def union(self):
        partes = [self.concat()]
        while self.ver() == "+":
            self.tomar()
            partes.append(self.concat())
        return partes[0] if len(partes) == 1 else ("+", partes)

    def concat(self):
        partes = []
        while self.ver() is not None and self.ver() not in "+)":
            partes.append(self.estrella())
        if not partes:
            raise ValueError("Expresión regular con un operando vacío.")
        return partes[0] if len(partes) == 1 else (".", partes)

    def estrella(self):
        r = self.atomo()
        while self.ver() == "*":
            self.tomar()
            r = ("*", r)
        return r

    def atomo(self):
        c = self.tomar()
        if c == "(":
            r = self.union()
            if self.tomar() != ")":
                raise ValueError("Paréntesis sin cerrar.")
            return r
        if c in ("λ", "!"):
            return ("λ",)
        if c == "∅":
            return ("∅",)
        if c is None or c in "+*)":
            raise ValueError(f"Símbolo inesperado: {c!r}.")
        return ("s", c)


def analizar(er: str):
    a = _Analizador(er)
    arbol = a.union()
    if a.ver() is not None:
        raise ValueError(f"Sobra texto en la expresión: {''.join(a.t[a.i:])}")
    return arbol


def thompson(er: str, alfabeto, nombre=""):
    """Construcción de Thompson: cada subexpresión da un fragmento con un inicio y un final.

    * símbolo a:   i -a→ f
    * λ:           i -λ→ f
    * ∅:           i, f sin transiciones
    * r + s:       i -λ→ (r), i -λ→ (s), fin(r) -λ→ f, fin(s) -λ→ f
    * r s:         fin(r) -λ→ ini(s)
    * r*:          i -λ→ ini(r), i -λ→ f, fin(r) -λ→ ini(r), fin(r) -λ→ f
    """
    trans, contador = [], [0]

    def nuevo():
        contador[0] += 1
        return f"s{contador[0] - 1}"

    def construir(nodo):
        tipo = nodo[0]
        if tipo == "s":
            i, f = nuevo(), nuevo()
            trans.append((i, nodo[1], f))
            return i, f
        if tipo == "λ":
            i, f = nuevo(), nuevo()
            trans.append((i, LAMBDA, f))
            return i, f
        if tipo == "∅":
            return nuevo(), nuevo()
        if tipo == "+":
            i = nuevo()
            fines = []
            for parte in nodo[1]:
                a, b = construir(parte)
                trans.append((i, LAMBDA, a))
                fines.append(b)
            f = nuevo()
            for b in fines:
                trans.append((b, LAMBDA, f))
            return i, f
        if tipo == ".":
            i, f = construir(nodo[1][0])
            for parte in nodo[1][1:]:
                a, b = construir(parte)
                trans.append((f, LAMBDA, a))
                f = b
            return i, f
        if tipo == "*":
            i = nuevo()
            a, b = construir(nodo[1])
            f = nuevo()
            trans.extend([(i, LAMBDA, a), (i, LAMBDA, f), (b, LAMBDA, a), (b, LAMBDA, f)])
            return i, f
        raise ValueError(tipo)

    inicio, fin = construir(analizar(er))
    estados = [f"s{k}" for k in range(contador[0])]
    m = Automata(list(alfabeto), estados, inicio, {fin}, trans, nombre)
    return m.numerar(nombre=nombre)


def er_a_python(er: str) -> str:
    """Sintaxis del curso → módulo re: + es |, λ es la cadena vacía, ∅ no acepta nada."""
    return er.replace(" ", "").replace("+", "|").replace("λ", "(?:)").replace("!", "(?:)").replace("∅", "(?!)")


def regex(er: str):
    patron = re.compile(er_a_python(er))
    return lambda w: patron.fullmatch(w) is not None


# ----------------------------------------------------------------------
# Tablas de la lista
# ----------------------------------------------------------------------

def tabla(inicial, finales, simbolos, renglones, lambda_primero=False, nombre=""):
    """Transcribe una tabla: renglones 'A: B C; …' (AFD) o 'A: BC - D; …' (AFN, '-' = ∅).

    Si ``lambda_primero``, la primera columna es λ (tablas de los problemas 196-200).
    Cada estado se nombra con una letra.
    """
    columnas = ([LAMBDA] if lambda_primero else []) + list(simbolos)
    estados, trans = [], []
    for r in renglones.split(";"):
        q, resto = r.split(":")
        q = q.strip()
        estados.append(q)
        for a, destino in zip(columnas, resto.split()):
            if destino != "-":
                trans += [(q, a, p) for p in destino]
    return Automata(list(simbolos), estados, inicial, set(finales), trans, nombre).validar()
