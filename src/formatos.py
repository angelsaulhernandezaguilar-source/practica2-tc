"""
Lectura y escritura de autómatas en .jff (JFLAP), .json y .xml.

Solo usa la biblioteca estándar; no depende de Flet. Los tres formatos
representan la misma quíntupla (Σ, Q, q0, F, δ) y las funciones de este
módulo son inversas: ``leer_X(escribir_X(M)) == M`` para X en {jff, json, xml}.

Convenciones (ver docs/03-simulador.md):

* λ se escribe como la cadena vacía: ``<read/>`` en .jff, ``"lee": ""`` en
  .json y ``lee=""`` en .xml.
* JFLAP no guarda el alfabeto: lo deduce de las transiciones. Para que la
  ida y vuelta conserve símbolos que no aparecen en δ, el .jff que escribe
  este módulo lleva, dentro de <structure>, un comentario XML
  ``<!--alfabeto: [...]-->``, que JFLAP ignora. Si el comentario no está (archivo hecho en JFLAP), Σ se deduce de
  las transiciones, como hace JFLAP.
* Las coordenadas <x>, <y> del .jff solo sirven para dibujar: se toleran al
  leer y se calculan al escribir, pero no forman parte de la quíntupla.
"""

from __future__ import annotations

import json
import pathlib
import re
import xml.etree.ElementTree as ET
from collections import deque

from automata import LAMBDA, Automata

FORMATOS = (".jff", ".json", ".xml")


class FormatoInvalido(ValueError):
    """El archivo no tiene la estructura esperada."""


# ----------------------------------------------------------------------
# Utilidades
# ----------------------------------------------------------------------

def _raiz_xml(texto: str) -> ET.Element:
    try:
        constructor = ET.TreeBuilder(insert_comments=True)
        analizador = ET.XMLParser(target=constructor)
        analizador.feed(texto)
        return analizador.close()
    except ET.ParseError as err:
        raise FormatoInvalido(f"El archivo no es XML válido: {err}") from err


def _bool(valor) -> bool:
    return str(valor).strip().lower() in ("true", "1", "si", "sí", "yes")


def _ordenar_transiciones(aut: Automata):
    """Transiciones en orden estable: estado de origen (orden de Q), símbolo (orden de Σ, λ al final), destino."""
    pos_q = {q: i for i, q in enumerate(aut.estados)}
    pos_a = {a: i for i, a in enumerate(aut.alfabeto)}
    pos_a[LAMBDA] = len(pos_a)
    claves = sorted(aut.transiciones, key=lambda k: (pos_q.get(k[0], 1e9), pos_a.get(k[1], 1e9), k))
    for q, a in claves:
        for p in sorted(aut.transiciones[q, a], key=lambda s: (pos_q.get(s, 1e9), s)):
            yield q, a, p


def posiciones(aut: Automata) -> dict[str, tuple[float, float]]:
    """Coordenadas para JFLAP: una columna por nivel del recorrido BFS desde q0."""
    nivel = {aut.inicial: 0}
    cola = deque([aut.inicial])
    while cola:
        q = cola.popleft()
        for a in aut.alfabeto + [LAMBDA]:
            for p in sorted(aut.destinos(q, a)):
                if p not in nivel:
                    nivel[p] = nivel[q] + 1
                    cola.append(p)
    ultimo = max(nivel.values(), default=0)
    for q in aut.estados:
        if q not in nivel:
            ultimo += 1
            nivel[q] = ultimo
    columnas: dict[int, list[str]] = {}
    for q in aut.estados:
        columnas.setdefault(nivel[q], []).append(q)
    alto = max(len(c) for c in columnas.values())
    pos = {}
    for n, estados in columnas.items():
        desfase = (alto - len(estados)) * 55
        for i, q in enumerate(estados):
            # Un pequeño zigzag evita que las flechas largas pasen por encima de los estados.
            pos[q] = (80.0 + 160.0 * n, 80.0 + desfase + 110.0 * i + (25.0 if n % 2 else 0.0))
    return pos


# ----------------------------------------------------------------------
# .jff (JFLAP)
# ----------------------------------------------------------------------

def leer_jff(texto: str, nombre: str = "") -> Automata:
    raiz = _raiz_xml(texto)
    if raiz.tag != "structure":
        raise FormatoInvalido("Un .jff debe tener <structure> como elemento raíz.")
    tipo = (raiz.findtext("type") or "").strip()
    if tipo != "fa":
        raise FormatoInvalido(
            f"El archivo es de tipo {tipo!r}; el simulador solo carga autómatas finitos (tipo 'fa')."
        )
    nodo = raiz.find("automaton")
    nodo = raiz if nodo is None else nodo
    nombres, estados, finales, inicial = {}, [], set(), None
    for e in nodo.iter("state"):
        ident = e.get("id")
        if ident is None:
            raise FormatoInvalido("Hay un <state> sin atributo id.")
        nombre_estado = e.get("name") or f"q{ident}"
        if nombre_estado in estados:
            nombre_estado = f"{nombre_estado}#{ident}"
        nombres[ident] = nombre_estado
        estados.append(nombre_estado)
        if e.find("initial") is not None:
            if inicial is not None:
                raise FormatoInvalido("El .jff marca más de un estado inicial.")
            inicial = nombre_estado
        if e.find("final") is not None:
            finales.add(nombre_estado)
    if inicial is None:
        raise FormatoInvalido("El .jff no marca ningún estado como inicial (<initial/>).")
    transiciones = []
    for t in nodo.iter("transition"):
        origen, destino = t.findtext("from"), t.findtext("to")
        if origen not in nombres or destino not in nombres:
            raise FormatoInvalido(f"Transición con un estado inexistente: {origen} → {destino}.")
        transiciones.append((nombres[origen], (t.findtext("read") or ""), nombres[destino]))
    alfabeto = None
    for c in raiz.iter(ET.Comment):
        m = re.match(r"\s*alfabeto:\s*(\[.*\])\s*$", c.text or "", re.S)
        if m:
            alfabeto = json.loads(m.group(1))
    if alfabeto is None:
        vistos = []
        for _, a, _ in transiciones:
            if a and a not in vistos:
                vistos.append(a)
        alfabeto = sorted(vistos)
    return Automata(alfabeto, estados, inicial, finales, transiciones, nombre).validar()


def escribir_jff(aut: Automata) -> str:
    aut.validar()
    ids = {q: str(i) for i, q in enumerate(aut.estados)}
    pos = posiciones(aut)
    lineas = [
        '<?xml version="1.0" encoding="UTF-8" standalone="no"?>',
        "<!--Creado con practica2-tc (src/formatos.py).-->",
        "<structure>",
        "\t<!--alfabeto: " + json.dumps(aut.alfabeto, ensure_ascii=False).replace("--", "-\\u002d") + "-->",
        "\t<type>fa</type>",
        "\t<automaton>",
    ]
    for q in aut.estados:
        x, y = pos[q]
        lineas.append(f'\t\t<state id="{ids[q]}" name="{_esc(q)}">')
        lineas.append(f"\t\t\t<x>{x}</x>")
        lineas.append(f"\t\t\t<y>{y}</y>")
        if q == aut.inicial:
            lineas.append("\t\t\t<initial/>")
        if q in aut.aceptacion:
            lineas.append("\t\t\t<final/>")
        lineas.append("\t\t</state>")
    for q, a, p in _ordenar_transiciones(aut):
        lectura = f"<read>{_esc(a)}</read>" if a else "<read/>"
        lineas.append(f"\t\t<transition><from>{ids[q]}</from><to>{ids[p]}</to>{lectura}</transition>")
    lineas += ["\t</automaton>", "</structure>", ""]
    return "\n".join(lineas)


def _esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


# ----------------------------------------------------------------------
# .json
# ----------------------------------------------------------------------

def leer_json(texto: str, nombre: str = "") -> Automata:
    try:
        datos = json.loads(texto)
    except json.JSONDecodeError as err:
        raise FormatoInvalido(f"El archivo no es JSON válido: {err}") from err
    faltan = [c for c in ("alfabeto", "estados", "inicial", "aceptacion", "transiciones") if c not in datos]
    if faltan:
        raise FormatoInvalido("Al .json le faltan las claves: " + ", ".join(faltan) + ".")
    transiciones = []
    for t in datos["transiciones"]:
        hacia = t["hacia"]
        for p in [hacia] if isinstance(hacia, str) else hacia:
            transiciones.append((t["desde"], t.get("lee", "") or "", p))
    return Automata(datos["alfabeto"], datos["estados"], datos["inicial"], datos["aceptacion"],
                    transiciones, datos.get("nombre", nombre)).validar()


def escribir_json(aut: Automata) -> str:
    aut.validar()
    agrupadas: dict[tuple[str, str], list[str]] = {}
    for q, a, p in _ordenar_transiciones(aut):
        agrupadas.setdefault((q, a), []).append(p)
    datos = {
        "tipo": aut.tipo,
        "alfabeto": aut.alfabeto,
        "estados": aut.estados,
        "inicial": aut.inicial,
        "aceptacion": [q for q in aut.estados if q in aut.aceptacion],
        "transiciones": [{"desde": q, "lee": a, "hacia": d} for (q, a), d in agrupadas.items()],
    }
    if aut.nombre:
        datos = {"nombre": aut.nombre, **datos}
    return json.dumps(datos, ensure_ascii=False, indent=2) + "\n"


# ----------------------------------------------------------------------
# .xml
# ----------------------------------------------------------------------

def leer_xml(texto: str, nombre: str = "") -> Automata:
    raiz = _raiz_xml(texto)
    if raiz.tag != "automata":
        raise FormatoInvalido("Un .xml del simulador debe tener <automata> como elemento raíz.")
    alfabeto = [s.text or "" for s in raiz.iterfind("alfabeto/simbolo")]
    estados, finales, inicial = [], set(), None
    for e in raiz.iterfind("estados/estado"):
        q = e.get("nombre")
        if q is None:
            raise FormatoInvalido("Hay un <estado> sin atributo nombre.")
        estados.append(q)
        if _bool(e.get("inicial", "false")):
            if inicial is not None:
                raise FormatoInvalido("El .xml marca más de un estado inicial.")
            inicial = q
        if _bool(e.get("aceptacion", "false")):
            finales.add(q)
    if inicial is None:
        raise FormatoInvalido('El .xml no marca ningún estado con inicial="true".')
    transiciones = [(t.get("desde"), t.get("lee", "") or "", t.get("hacia"))
                    for t in raiz.iterfind("transiciones/transicion")]
    return Automata(alfabeto, estados, inicial, finales, transiciones,
                    raiz.get("nombre", nombre)).validar()


def escribir_xml(aut: Automata) -> str:
    aut.validar()
    nombre = f' nombre="{_esc(aut.nombre)}"' if aut.nombre else ""
    lineas = ['<?xml version="1.0" encoding="UTF-8"?>', f'<automata tipo="{aut.tipo}"{nombre}>']
    lineas.append("\t<alfabeto>" + "".join(f"<simbolo>{_esc(a)}</simbolo>" for a in aut.alfabeto) + "</alfabeto>")
    lineas.append("\t<estados>")
    for q in aut.estados:
        atributos = f' nombre="{_esc(q)}"'
        if q == aut.inicial:
            atributos += ' inicial="true"'
        if q in aut.aceptacion:
            atributos += ' aceptacion="true"'
        lineas.append(f"\t\t<estado{atributos}/>")
    lineas.append("\t</estados>")
    lineas.append("\t<transiciones>")
    for q, a, p in _ordenar_transiciones(aut):
        lineas.append(f'\t\t<transicion desde="{_esc(q)}" lee="{_esc(a)}" hacia="{_esc(p)}"/>')
    lineas += ["\t</transiciones>", "</automata>", ""]
    return "\n".join(lineas)


# ----------------------------------------------------------------------
# Por extensión
# ----------------------------------------------------------------------

LECTORES = {".jff": leer_jff, ".json": leer_json, ".xml": leer_xml}
ESCRITORES = {".jff": escribir_jff, ".json": escribir_json, ".xml": escribir_xml}


def extension(nombre_archivo: str) -> str:
    ext = pathlib.Path(nombre_archivo).suffix.lower()
    if ext not in LECTORES:
        raise FormatoInvalido(f"Extensión {ext or '(ninguna)'} no soportada; use .jff, .json o .xml.")
    return ext


def desde_texto(texto: str, nombre_archivo: str) -> Automata:
    nombre = pathlib.Path(nombre_archivo).stem
    return LECTORES[extension(nombre_archivo)](texto, nombre)


def a_texto(aut: Automata, nombre_archivo: str) -> str:
    return ESCRITORES[extension(nombre_archivo)](aut)


def cargar(ruta) -> Automata:
    ruta = pathlib.Path(ruta)
    return desde_texto(ruta.read_text(encoding="utf-8"), ruta.name)


def guardar(aut: Automata, ruta) -> pathlib.Path:
    ruta = pathlib.Path(ruta)
    ruta.write_text(a_texto(aut, ruta.name), encoding="utf-8", newline="\n")
    return ruta


def guardar_tres(aut: Automata, ruta_sin_extension) -> list[pathlib.Path]:
    base = pathlib.Path(ruta_sin_extension)
    return [guardar(aut, base.with_suffix(ext)) for ext in FORMATOS]


def resumen_quintupla(aut: Automata) -> str:
    """Texto con los cinco componentes, para verificar una importación."""
    delta = [f"δ({q}, {a or 'λ'}) = {{{', '.join(sorted(d))}}}" for (q, a), d in
             sorted(aut.transiciones.items(), key=lambda k: (aut.estados.index(k[0][0]), k[0][1])) if d]
    return "\n".join([
        f"Tipo: {aut.tipo}",
        "Σ = {" + ", ".join(aut.alfabeto) + "}",
        "Q = {" + ", ".join(aut.estados) + "}",
        f"q0 = {aut.inicial}",
        "F = {" + ", ".join(q for q in aut.estados if q in aut.aceptacion) + "}",
        "δ:",
        *("  " + d for d in delta),
    ])

