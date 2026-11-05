"""Práctica 4: analizador de expresiones, teorema de Kleene (I y II), equivalencia y validadores.

Casos de prueba del enunciado: Lista 3, 241-253 (expresión → autómata) y 254-258 (autómata → expresión);
Lista 4, 272, 273 y 278 (expresión → autómata) y 276 y 277 (autómata → expresión); los cinco AFD del
Ejercicio 1 de la Práctica 3 con las expresiones que dio JFLAP. Para los validadores, la congruencia entre el
autómata y re.fullmatch sobre al menos 500 cadenas por validador.
"""

import pathlib
import re

import pytest

from algoritmos import clausura_lambda, isomorfismo, palabras, simular_directo
from automata import LAMBDA, Automata, AutomataInvalido
from expresiones import (
    Clase,
    Concat,
    ErrorDeSintaxis,
    Estrella,
    Lambda,
    Simbolo,
    Union,
    Vacio,
    a_python,
    analizar,
    comparar_expresiones,
    concat,
    construir_afn,
    de_expresion_a_minimo,
    eliminar_estados,
    equivalente_al_automata,
    escribir_expresion_jff,
    estrella,
    leer_expresion_jff,
    problemas_de_determinismo,
    transiciones_faltantes,
    union,
)
from formatos import cargar, desde_texto, escribir_jff, leer_jff
from validadores import VALIDADORES, ejemplos

RAIZ = pathlib.Path(__file__).resolve().parent.parent
AUTOMATAS = RAIZ / "automatas"
P4 = AUTOMATAS / "practica4"
LONGITUD = 8

ER_241_253 = {
    "241": "0+1", "242": "0*+1", "243": "(0+1)*", "244": "0(0+1)", "245": "0(0+1)*", "246": "0*(0+1)",
    "247": "(01)*+1*", "248": "(0*+1)0", "249": "(0*+1)0*", "250": "0*1*+1*0", "251": "(0+1*)0+1*1",
    "252": "(0+1)*(00+11)+(00+11)(0+1)*", "253": "(0+(11+00)*)(11+10+01)*(λ+110)",
}
ER_272 = {"272a": "a+b*", "272b": "(ab)*a", "272c": "(a+b)*abb", "272d": "a(ba)*+b", "272e": "(a+λ)(b+∅)"}
ER_278 = "(a+b)*b"

# Expresiones de JFLAP de la Práctica 3 (docs/practica3/01-afd-a-er-jflap.md) para los cinco AFD.
JFLAP_P3 = {
    "L2-130": "0*1(1+0(0+1))*", "L2-138": "(a+ba*ba*b)*", "L2-141": "(1+01)*",
    "L3-257": "((1+01*0)(0+1))*(01*+1+01*0)", "L3-258": "((0+1)(01)*(1+00))*(0+1)(01)*",
}
# Expresiones obtenidas a mano con el lema de Arden en la Lista 4.
ARDEN_L4 = {"L4-276": "(b+ab*ab*a)*", "L4-277": "(0+11*0)*11*"}


def coinciden_con_re(cadena, longitud=LONGITUD):
    p = re.compile(a_python(cadena.expresion))
    for w in palabras(cadena.afn_lambda.alfabeto, longitud):
        texto = "".join(w)
        assert (p.fullmatch(texto) is not None) == cadena.acepta(w), f"discrepan en {texto or 'λ'}"


# ----------------------------------------------------------------------
# Analizador
# ----------------------------------------------------------------------

def test_precedencia_y_parentesis():
    assert analizar("a+bc*") == Union((Simbolo("a"), Concat((Simbolo("b"), Estrella(Simbolo("c"))))))
    assert analizar("(a+b)c*") == Concat((Union((Simbolo("a"), Simbolo("b"))), Estrella(Simbolo("c"))))
    assert analizar("(ab)*") == Estrella(Concat((Simbolo("a"), Simbolo("b"))))
    assert analizar("a**") == Estrella(Estrella(Simbolo("a")))
    assert analizar("λ+∅") == Union((Lambda(), Vacio()))
    assert analizar("!") == Lambda() and analizar("ε") == Lambda() and analizar("Ø") == Vacio()
    assert analizar(" a b ") == Concat((Simbolo("a"), Simbolo("b")))  # los espacios se ignoran


def test_el_texto_del_arbol_se_vuelve_a_analizar():
    for er in list(ER_241_253.values()) + list(ER_272.values()) + list(JFLAP_P3.values()):
        arbol = analizar(er)
        assert analizar(str(arbol)) == arbol
        assert str(arbol) == er.replace(" ", "")


def test_escapes_y_clases():
    assert analizar("\\+\\*\\(\\)") == Concat(tuple(Simbolo(c) for c in "+*()"))
    assert analizar("a␣b") == Concat((Simbolo("a"), Simbolo(" "), Simbolo("b")))
    arbol = analizar("D*", {"D": "0123456789"})
    assert arbol == Estrella(Clase("D", tuple("0123456789")))
    assert arbol.simbolos() == set("0123456789")
    with pytest.raises(ValueError):
        analizar("a", {"+": "ab"})


@pytest.mark.parametrize("texto,posicion,fragmento", [
    ("", 1, "vacía"),
    ("a+", 3, "final de la expresión"),
    ("*a", 1, "cerradura"),
    ("a+*b", 3, "cerradura"),
    ("(ab", 4, "posición 1"),
    ("ab)", 3, "sin su paréntesis de apertura"),
    ("a(b))", 5, "sin su paréntesis de apertura"),
    ("()", 2, "vacíos"),
    ("a++b", 3, "unión"),
    ("(+b)", 2, "unión"),
    ("ab\\", 3, "barra"),
])
def test_errores_con_posicion(texto, posicion, fragmento):
    with pytest.raises(ErrorDeSintaxis) as info:
        analizar(texto)
    assert info.value.posicion == posicion
    assert fragmento in str(info.value)
    assert info.value.senalar().splitlines()[-1] == " " * (posicion - 1) + "^"


def test_constructores_aplican_las_leyes():
    a, b = Simbolo("a"), Simbolo("b")
    assert union(a, Vacio()) == a and union(Vacio(), Vacio()) == Vacio()
    assert union(a, a) == a and union(a, b, a) == Union((a, b))
    assert concat(a, Lambda(), b) == Concat((a, b)) and concat(a, Vacio()) == Vacio()
    assert concat(Lambda(), Lambda()) == Lambda()
    assert estrella(Vacio()) == Lambda() and estrella(Lambda()) == Lambda()
    assert estrella(Estrella(a)) == Estrella(a)
    assert estrella(Union((Lambda(), a))) == Estrella(a)  # (λ + r)* = r*


# ----------------------------------------------------------------------
# Teorema de Kleene, parte I
# ----------------------------------------------------------------------

@pytest.mark.parametrize("numero,er", ER_241_253.items())
def test_241_253_contra_re_y_contra_la_practica2(numero, er):
    c = de_expresion_a_minimo(er)
    coinciden_con_re(c)
    # El AFN-λ de la Práctica 2 (herramientas/construir.py, generado para JFLAP) acepta el mismo lenguaje.
    viejo = cargar(AUTOMATAS / "lista3-afnd-lambda" / f"L3-{numero}.jff")
    assert viejo.equivalente(c.afn_lambda)
    assert c.cadena.minimo.automata.tipo == "AFD"
    assert c.tamanos()["AFD mínimo"] <= c.tamanos()["AFD"]


def test_pasos_de_la_construccion_272b():
    """Lista 4, 272(b): (ab)*a. Mismo orden y numeración que la construcción a mano."""
    r = construir_afn(analizar("(ab)*a"))
    assert [(p.regla, str(p.expresion), p.inicial, p.final) for p in r.pasos] == [
        ("símbolo", "a", "q0", "q1"), ("símbolo", "b", "q2", "q3"), ("concatenación", "ab", "q0", "q3"),
        ("estrella", "(ab)*", "q4", "q5"), ("símbolo", "a", "q6", "q7"), ("concatenación", "(ab)*a", "q4", "q7"),
    ]
    assert r.automata.inicial == "q4" and r.automata.aceptacion == {"q7"}
    assert len(r.automata.estados) == 8
    # Cada autómata parcial es el fragmento N(r): su inicial no tiene entradas y su final no tiene salidas.
    for p in r.pasos:
        parcial = p.automata
        assert parcial.inicial == p.inicial and parcial.aceptacion == {p.final}
        assert not any(p.inicial in d for d in parcial.transiciones.values())
        assert not any(q == p.final for (q, _), d in parcial.transiciones.items() if d)
    assert clausura_lambda(r.automata, "q4").resultado == {"q0", "q4", "q5", "q6"}


def test_272e_con_lambda_y_vacio():
    r = construir_afn(analizar("(a+λ)(b+∅)"))
    assert [p.regla for p in r.pasos] == ["símbolo", "λ", "unión", "símbolo", "∅", "unión", "concatenación"]
    assert r.pasos[4].automata.num_transiciones() == 0
    assert sorted(r.automata.cadenas_aceptadas(4)) == ["ab", "b"]  # L = (a + λ)b = {b, ab}


@pytest.mark.parametrize("clave,er", ER_272.items())
def test_272_contra_los_afn_de_la_lista4(clave, er):
    """Los AFN-λ construidos a mano en la Lista 4 (automatas/practica4/lista4/) son equivalentes."""
    c = de_expresion_a_minimo(er)
    coinciden_con_re(c)
    hecho_a_mano = cargar(P4 / "lista4" / f"{clave}.jff")
    assert hecho_a_mano.equivalente(c.afn_lambda)
    assert len(hecho_a_mano.estados) == len(c.afn_lambda.estados)


def test_273_cadenas_por_clausuras():
    """Lista 4, 273: aba, ab, babb y abab en los autómatas de 272(b) y 272(c), con la simulación directa."""
    b = construir_afn(analizar(ER_272["272b"])).automata
    c = construir_afn(analizar(ER_272["272c"])).automata
    esperado = {"aba": (True, False), "ab": (False, False), "babb": (False, True), "abab": (False, False)}
    for w, (en_b, en_c) in esperado.items():
        assert simular_directo(b, w).acepta is en_b
        assert simular_directo(c, w).acepta is en_c
    # Las cerraduras intermedias de la Lista 4 para aba en 272(b).
    pasos = simular_directo(b, "aba").pasos
    assert [set(p.despues) for p in pasos] == [{"q0", "q4", "q5", "q6"}, {"q1", "q2", "q7"},
                                               {"q0", "q3", "q5", "q6"}, {"q1", "q2", "q7"}]


def test_278_ciclo_completo():
    """Lista 4, 278: (a+b)*b → AFN-λ de 10 estados → AFN → AFD → mínimo de 2 estados → expresión equivalente."""
    c = de_expresion_a_minimo(ER_278)
    assert c.tamanos() == {"AFN-λ": 10, "AFN": 10, "AFD": 3, "AFD mínimo": 2}
    coinciden_con_re(c)
    r = eliminar_estados(c.minimo)
    assert comparar_expresiones(str(r.expresion), ER_278).equivalentes
    # Los archivos de la Lista 4 hechos en JFLAP para el mismo ciclo.
    for etapa, mio in (("afn", c.cadena.sin_lambda.automata), ("afd", c.cadena.subconjuntos.automata), ("min", c.minimo)):
        assert cargar(P4 / "lista4" / f"278_{etapa}.jff").equivalente(mio)


def test_alfabeto_explicito():
    c = de_expresion_a_minimo("a", alfabeto="abc")
    assert c.minimo.alfabeto == ["a", "b", "c"] and c.minimo.tipo == "AFD"
    with pytest.raises(AutomataInvalido):
        de_expresion_a_minimo("ab", alfabeto="a")


def test_exportar_cada_automata_a_jff():
    c = de_expresion_a_minimo(ER_241_253["252"])
    for m in c.cadena.automatas:
        assert leer_jff(escribir_jff(m)) == m
    texto = escribir_expresion_jff(c.expresion)
    assert "<type>re</type>" in texto and leer_expresion_jff(texto) == str(c.expresion)
    assert leer_expresion_jff(escribir_expresion_jff(analizar("λ+a"))) == "λ+a"


# ----------------------------------------------------------------------
# Teorema de Kleene, parte II
# ----------------------------------------------------------------------

def test_verificacion_de_determinismo():
    afn = cargar(AUTOMATAS / "practica3" / "casos-de-prueba" / "L3-192-AFND.jff")
    problemas = problemas_de_determinismo(afn)
    assert problemas and all("destinos" in p for p in problemas)
    con_lambda = cargar(AUTOMATAS / "practica3" / "casos-de-prueba" / "L3-196.jff")
    assert any("transición λ" in p for p in problemas_de_determinismo(con_lambda))
    with pytest.raises(AutomataInvalido) as info:
        eliminar_estados(afn)
    assert "no es determinista" in str(info.value)
    afd = cargar(AUTOMATAS / "practica3" / "afd-a-er" / "L2-130.jff")
    assert problemas_de_determinismo(afd) == [] and transiciones_faltantes(afd) == []
    parcial = Automata("ab", ["p", "q"], "p", ["q"], [("p", "a", "q")])
    assert problemas_de_determinismo(parcial) == [] and len(transiciones_faltantes(parcial)) == 3


@pytest.mark.parametrize("nombre,jflap", JFLAP_P3.items())
def test_los_cinco_afd_de_la_practica3(nombre, jflap):
    afd = cargar(AUTOMATAS / "practica3" / "afd-a-er" / f"{nombre}.jff")
    r = eliminar_estados(afd)
    # Mismo orden de eliminación que JFLAP (alfabético) → la misma expresión, carácter por carácter.
    assert str(r.expresion) == jflap
    assert equivalente_al_automata(str(r.expresion), afd).equivalentes
    assert comparar_expresiones(str(r.expresion), jflap).equivalentes


@pytest.mark.parametrize("numero", ["254", "255", "256", "257", "258"])
def test_254_258_contra_arden_de_la_practica1(numero):
    afd = cargar(AUTOMATAS / "lista2-afd" / f"L3-{numero}.jff")
    arden = leer_expresion_jff((AUTOMATAS / "lista2-afd" / f"L3-{numero}-ER.jff").read_text(encoding="utf-8"))
    r = eliminar_estados(afd)
    assert equivalente_al_automata(str(r.expresion), afd).equivalentes
    assert comparar_expresiones(str(r.expresion), arden).equivalentes


@pytest.mark.parametrize("nombre,arden", ARDEN_L4.items())
def test_276_277_contra_arden_de_la_lista4(nombre, arden):
    afd = cargar(P4 / "casos-de-prueba" / "afd" / f"{nombre}.jff")
    r = eliminar_estados(afd)
    assert str(r.expresion) == arden  # con este orden de eliminación coincide con la solución a mano
    assert equivalente_al_automata(arden, afd).equivalentes


def test_pasos_de_la_eliminacion_257():
    """257 tiene dos finales: se agrega f, se eliminan B y C, y queda la fórmula de dos estados."""
    afd = cargar(AUTOMATAS / "practica3" / "afd-a-er" / "L3-257.jff")
    r = eliminar_estados(afd)
    assert r.final_nuevo and r.final == "f" and r.orden == ["B", "C"]
    assert [p.eliminado for p in r.pasos] == [None, "B", "C", None]
    assert [p.estados for p in r.pasos] == [["A", "B", "C", "f"], ["A", "C", "f"], ["A", "f"], ["A", "f"]]
    assert str(r.pasos[1].etiquetas["A", "C"]) == "1+01*0"
    assert str(r.pasos[2].etiquetas["A", "A"]) == "(1+01*0)(0+1)"
    g = r.pasos[1].generalizado()
    assert g.inicial == "A" and g.aceptacion == {"f"} and ("A", "1+01*0") in g.transiciones


def test_orden_de_eliminacion_distinto_da_una_expresion_equivalente():
    afd = cargar(AUTOMATAS / "practica3" / "afd-a-er" / "L3-257.jff")
    r1, r2 = eliminar_estados(afd, orden=["B", "C"]), eliminar_estados(afd, orden=["C", "B"])
    assert str(r1.expresion) != str(r2.expresion)
    assert comparar_expresiones(str(r1.expresion), str(r2.expresion)).equivalentes
    with pytest.raises(AutomataInvalido):
        eliminar_estados(afd, orden=["B"])


def test_eliminacion_con_afn_si_se_permite():
    afn = cargar(AUTOMATAS / "practica3" / "casos-de-prueba" / "L3-196.jff")
    r = eliminar_estados(afn, requerir_afd=False)
    assert equivalente_al_automata(str(r.expresion), afn).equivalentes


def test_comparar_expresiones_no_equivalentes():
    c = comparar_expresiones("(0+1)*1", "(0+1)*")
    assert not c.equivalentes and "estados" in c.resultado.motivo
    assert comparar_expresiones("0*1(0*1)*", "(0+11*0)*11*").equivalentes  # las dos formas del 277


# ----------------------------------------------------------------------
# Traducción a re
# ----------------------------------------------------------------------

@pytest.mark.parametrize("er,esperado", [
    ("0+1", "0|1"), ("(0+1)*1", "(?:0|1)*1"), ("a**", "(?:a*)*"), ("λ+a", "(?:)|a"), ("∅", "(?!)"),
    ("a.b", "a\\.b"), ("\\+", "\\+"), ("(ab)*", "(?:ab)*"),
])
def test_a_python(er, esperado):
    assert a_python(er) == esperado
    re.compile(a_python(er))


def test_a_python_con_clases():
    p = a_python("D*", {"D": "0123456789"})
    assert p == "[0-9]*" and re.fullmatch(p, "2026")
    assert a_python("X", {"X": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-+"}) == "[+\\-0-9A-Z_a-z]"
    p = a_python("S", {"S": "a-]"})
    assert re.fullmatch(p, "-") and re.fullmatch(p, "]") and not re.fullmatch(p, "b")
    assert a_python("S", {"S": "acegik"}) == "[acegik]"


# ----------------------------------------------------------------------
# Validadores (Ejercicio 4): congruencia entre el autómata y re.fullmatch
# ----------------------------------------------------------------------

@pytest.mark.parametrize("clave", list(VALIDADORES))
def test_validador_congruente_con_re(clave):
    v = VALIDADORES[clave]
    validas, invalidas = ejemplos(clave)
    assert len(validas) >= 250 and len(invalidas) >= 250 and len(validas) + len(invalidas) >= 500
    assert all(v.valida_con_re(w) for w in validas)
    assert not any(v.valida_con_re(w) for w in invalidas)
    for w in validas + invalidas:
        assert v.valida_con_automata(w) == v.valida_con_re(w), f"discrepan en {w!r}"


@pytest.mark.parametrize("clave", list(VALIDADORES))
def test_validador_ejemplos_fijos(clave):
    v = VALIDADORES[clave]
    assert all(v.valida_con_automata(w) for w in v.validas)
    assert not any(v.valida_con_automata(w) for w in v.invalidas)
    assert v.cadena().minimo.tipo == "AFD"
    tam = v.cadena().tamanos()
    assert tam["AFD mínimo"] <= tam["AFD"] <= tam["AFN"] == tam["AFN-λ"]


def test_validadores_exportados_al_repositorio():
    for clave, v in VALIDADORES.items():
        exportado = cargar(P4 / "validadores" / f"{clave}-min.jff")
        assert isomorfismo(exportado, v.cadena().minimo) is not None
        er = leer_expresion_jff((P4 / "validadores" / f"{clave}-ER.jff").read_text(encoding="utf-8"))
        assert er == str(analizar(v.expresion, v.clases))


# ----------------------------------------------------------------------
# Archivos generados para los casos de prueba (herramientas/practica4_generar.py)
# ----------------------------------------------------------------------

@pytest.mark.parametrize("numero,er", {**ER_241_253, **{k: v for k, v in ER_272.items()}, "278": ER_278}.items())
def test_archivos_generados_de_cada_expresion(numero, er):
    prefijo = f"L3-{numero}" if numero.isdigit() and int(numero) < 260 else f"L4-{numero}"
    carpeta = P4 / "casos-de-prueba" / "er"
    assert leer_expresion_jff((carpeta / f"{prefijo}-ER.jff").read_text(encoding="utf-8")) == er
    c = de_expresion_a_minimo(er)
    for etapa, mio in (("afn-lambda", c.afn_lambda), ("afn", c.cadena.sin_lambda.automata),
                       ("afd", c.cadena.subconjuntos.automata), ("min", c.minimo)):
        assert cargar(carpeta / f"{prefijo}-{etapa}.jff") == mio
