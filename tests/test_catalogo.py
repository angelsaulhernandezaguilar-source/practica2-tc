"""Pruebas de los autómatas del Ejercicio 2 (automatas/).

Comprueban, para cada autómata del catálogo, que sus tres archivos describen
la misma quíntupla, que aceptan exactamente el lenguaje del oráculo escrito a
partir del enunciado y que el AFD de cada conversión es equivalente.
"""

import itertools
import pathlib
import random

import pytest

from catalogo import AFD_, LAMBDA_, piezas
from formatos import cargar

RAIZ = pathlib.Path(__file__).resolve().parent.parent / "automatas"
PIEZAS = list(piezas())
IDS = [p.archivo for _, p in PIEZAS]


def automata(e, p):
    return cargar(RAIZ / e.carpeta / f"{p.archivo}.jff")


def muestra(alfabeto, semilla):
    largo = 0
    while len(alfabeto) ** (largo + 1) <= 700:
        largo += 1
    for k in range(largo + 1):
        for t in itertools.product(alfabeto, repeat=k):
            yield "".join(t)
    azar = random.Random(semilla)
    for _ in range(150):
        yield "".join(azar.choice(alfabeto) for _ in range(azar.randint(0, 25)))


@pytest.mark.parametrize("e,p", PIEZAS, ids=IDS)
def test_tres_formatos_misma_quintupla(e, p):
    base = RAIZ / e.carpeta / p.archivo
    m = cargar(base.with_suffix(".jff"))
    assert cargar(base.with_suffix(".json")) == m
    assert cargar(base.with_suffix(".xml")) == m


@pytest.mark.parametrize("e,p", PIEZAS, ids=IDS)
def test_lenguaje_del_enunciado(e, p):
    m = automata(e, p)
    o = p.oraculo
    if isinstance(o, str):
        o = automata(e, next(x for _, x in PIEZAS if x.archivo == o)).acepta
    if o is None:  # transcripción de una tabla: se compara con el autómata construido en el catálogo
        o = p.automata.acepta if p.automata is not None else m.acepta
    for w in muestra(m.alfabeto, len(p.archivo)):
        assert m.acepta(w) == bool(o(w)), (p.archivo, w)


@pytest.mark.parametrize("e,p", PIEZAS, ids=IDS)
def test_clasificacion(e, p):
    m = automata(e, p)
    if e.seccion == AFD_:
        assert m.tipo == "AFD"
    if m.tiene_lambda:
        assert e.seccion == LAMBDA_


CONVERSIONES = sorted((RAIZ / "conversiones").glob("*-AFD.jff"))


@pytest.mark.parametrize("ruta", CONVERSIONES, ids=[r.stem for r in CONVERSIONES])
def test_conversion_equivalente(ruta):
    afd = cargar(ruta)
    origen = ruta.stem[: -len("-AFD")]
    assert afd.es_determinista
    if origen.startswith("familia"):
        original = cargar(ruta.with_name(origen + "-AFND.jff"))
    else:
        e, p = next((e, p) for e, p in PIEZAS if p.archivo == origen)
        original = automata(e, p)
    assert afd.equivalente(original)
