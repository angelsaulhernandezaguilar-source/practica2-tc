"""Ejercicio 5: el autómata de TCP cargado desde sus tres archivos."""

import pathlib

import pytest

from aplicacion import CASOS, tcp
from formatos import cargar

RAIZ = pathlib.Path(__file__).resolve().parent.parent / "automatas" / "aplicacion"


@pytest.mark.parametrize("ext", [".jff", ".json", ".xml"])
def test_archivos_son_la_quintupla_del_modelo(ext):
    assert cargar(RAIZ / f"tcp{ext}") == tcp()


@pytest.mark.parametrize("w,esperado,_", CASOS, ids=[c[0] or "lambda" for c in CASOS])
def test_casos_de_prueba(w, esperado, _):
    assert cargar(RAIZ / "tcp.jff").acepta(w) is esperado


def test_es_afd_completo_y_minimo():
    m = tcp()
    assert m.tipo == "AFD"
    assert len(m.minimizar().estados) == len(m.estados) == 12


def test_syn_rcvd_necesita_dos_estados():
    """Fusionar SYN-RCVD-P y SYN-RCVD-A cambiaría el lenguaje: «psr» y «osr» terminan distinto."""
    m = tcp()
    assert m.delta_gorro("CLOSED", "psr") == {"LISTEN"}
    assert m.delta_gorro("CLOSED", "osr") == {"CLOSED"}
