"""Pruebas de src/formatos.py: los tres formatos y su ida y vuelta."""

import pytest

from automata import Automata
from formatos import (
    FormatoInvalido,
    a_texto,
    cargar,
    desde_texto,
    escribir_jff,
    escribir_json,
    escribir_xml,
    guardar,
    guardar_tres,
    leer_jff,
    leer_json,
    leer_xml,
)

FORMATOS = [(escribir_jff, leer_jff), (escribir_json, leer_json), (escribir_xml, leer_xml)]
IDS = ["jff", "json", "xml"]

# Los tres archivos del Anexo 3, tal como aparecen en el enunciado.
ANEXO_JFF = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<structure>
  <type>fa</type>
  <automaton>
    <state id="0" name="q0">
      <x>80.0</x><y>120.0</y>
      <initial/>
    </state>
    <state id="1" name="q1">
      <x>240.0</x><y>120.0</y>
      <final/>
    </state>
    <transition><from>0</from><to>1</to><read>a</read></transition>
    <transition><from>0</from><to>0</to><read>b</read></transition>
    <transition><from>0</from><to>1</to><read/></transition>
  </automaton>
</structure>"""

ANEXO_JSON = """{
  "tipo": "AFND-lambda",
  "alfabeto": ["a", "b"],
  "estados": ["q0", "q1"],
  "inicial": "q0",
  "aceptacion": ["q1"],
  "transiciones": [
    { "desde": "q0", "lee": "a", "hacia": ["q1"] },
    { "desde": "q0", "lee": "b", "hacia": ["q0"] },
    { "desde": "q0", "lee": "", "hacia": ["q1"] }
  ]
}"""

ANEXO_XML = """<?xml version="1.0" encoding="UTF-8"?>
<automata tipo="AFND-lambda">
  <alfabeto><simbolo>a</simbolo><simbolo>b</simbolo></alfabeto>
  <estados>
    <estado nombre="q0" inicial="true"/>
    <estado nombre="q1" aceptacion="true"/>
  </estados>
  <transiciones>
    <transicion desde="q0" lee="a" hacia="q1"/>
    <transicion desde="q0" lee="b" hacia="q0"/>
    <transicion desde="q0" lee="" hacia="q1"/>
  </transiciones>
</automata>"""


def anexo():
    return Automata("ab", ["q0", "q1"], "q0", ["q1"],
                    [("q0", "a", "q1"), ("q0", "b", "q0"), ("q0", "", "q1")])


def afnd_con_simbolo_sin_uso():
    """Σ tiene una c que no aparece en δ: JFLAP la perdería sin el comentario de alfabeto."""
    return Automata("abc", ["q0", "q1", "q2"], "q0", ["q2", "q0"],
                    [("q0", "a", "q0"), ("q0", "a", "q1"), ("q1", "b", "q2"), ("q2", "", "q0")])


def afd_completo():
    return Automata("01", ["par", "impar"], "par", ["par"],
                    [("par", "0", "impar"), ("par", "1", "par"), ("impar", "0", "par"), ("impar", "1", "impar")])


EJEMPLOS = [anexo, afnd_con_simbolo_sin_uso, afd_completo]


@pytest.mark.parametrize("escribir,leer", FORMATOS, ids=IDS)
@pytest.mark.parametrize("fabrica", EJEMPLOS)
def test_exportar_e_importar_son_inversas(escribir, leer, fabrica):
    m = fabrica()
    texto = escribir(m)
    m2 = leer(texto)
    assert m2 == m
    assert m2.alfabeto == m.alfabeto and m2.estados == m.estados
    # Y en el otro sentido: volver a escribir lo leído reproduce el mismo texto.
    assert escribir(m2) == texto


@pytest.mark.parametrize("texto,leer", [(ANEXO_JFF, leer_jff), (ANEXO_JSON, leer_json), (ANEXO_XML, leer_xml)],
                         ids=IDS)
def test_lee_los_archivos_del_anexo_3(texto, leer):
    m = leer(texto)
    assert m == anexo()
    assert m.alfabeto == ["a", "b"]
    assert m.estados == ["q0", "q1"]
    assert m.inicial == "q0"
    assert m.aceptacion == {"q1"}
    assert m.destinos("q0", "") == {"q1"}
    assert m.tipo == "AFND-lambda"


def test_los_tres_formatos_dan_la_misma_quintupla():
    assert leer_jff(ANEXO_JFF) == leer_json(ANEXO_JSON) == leer_xml(ANEXO_XML)


def test_jff_de_jflap_sin_comentario_deduce_el_alfabeto():
    sin_coordenadas = ANEXO_JFF.replace("<x>80.0</x><y>120.0</y>", "")
    assert leer_jff(sin_coordenadas).alfabeto == ["a", "b"]


def test_jff_formato_antiguo_sin_automaton():
    viejo = ANEXO_JFF.replace("<automaton>", "").replace("</automaton>", "")
    assert leer_jff(viejo) == anexo()


@pytest.mark.parametrize("ext", [".jff", ".json", ".xml"])
def test_guardar_y_cargar_en_disco(tmp_path, ext):
    m = afnd_con_simbolo_sin_uso()
    ruta = guardar(m, tmp_path / f"m{ext}")
    assert cargar(ruta) == m


def test_guardar_tres(tmp_path):
    rutas = guardar_tres(afd_completo(), tmp_path / "par")
    assert sorted(r.suffix for r in rutas) == [".jff", ".json", ".xml"]
    assert all(cargar(r) == afd_completo() for r in rutas)


def test_cruce_entre_formatos():
    m = afnd_con_simbolo_sin_uso()
    desde_xml = leer_xml(escribir_xml(m))
    assert leer_jff(escribir_jff(desde_xml)) == leer_json(escribir_json(desde_xml)) == m


@pytest.mark.parametrize("texto,nombre", [
    ("<structure><type>re</type><expression>a+b</expression></structure>", "x.jff"),
    ("<structure><type>fa</type><automaton><state id='0'/></automaton></structure>", "x.jff"),
    ('{"alfabeto": ["a"]}', "x.json"),
    ("<automata><estados><estado nombre='q0'/></estados></automata>", "x.xml"),
    ("no es xml", "x.xml"),
    ("{}", "x.txt"),
])
def test_archivos_mal_formados(texto, nombre):
    with pytest.raises(FormatoInvalido):
        desde_texto(texto, nombre)


def test_lambda_es_cadena_vacia_en_los_tres():
    m = anexo()
    assert "<read/>" in a_texto(m, "m.jff")
    assert '"lee": ""' in a_texto(m, "m.json")
    assert 'lee=""' in a_texto(m, "m.xml")
