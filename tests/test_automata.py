"""Pruebas del núcleo (src/automata.py): simulación, λ-clausura y conversiones."""

import itertools

import pytest

from automata import AFD, AFND, AFND_LAMBDA, Automata, AutomataInvalido


def cadenas(alfabeto, n):
    for k in range(n + 1):
        for t in itertools.product(alfabeto, repeat=k):
            yield "".join(t)


@pytest.fixture
def pares_de_ceros():
    """AFD del problema 139: número par de ceros sobre {0, 1}."""
    return Automata("01", ["par", "impar"], "par", ["par"],
                    [("par", "0", "impar"), ("par", "1", "par"),
                     ("impar", "0", "par"), ("impar", "1", "impar")])


@pytest.fixture
def termina_en_01():
    """AFND del problema 263: q0 adivina dónde empieza el sufijo 01."""
    return Automata("01", ["q0", "q1", "q2"], "q0", ["q2"],
                    [("q0", "0", "q0"), ("q0", "1", "q0"), ("q0", "0", "q1"), ("q1", "1", "q2")])


@pytest.fixture
def anexo3():
    """El AFND-λ de dos estados del Anexo 3 del enunciado."""
    return Automata("ab", ["q0", "q1"], "q0", ["q1"],
                    [("q0", "a", "q1"), ("q0", "b", "q0"), ("q0", "", "q1")])


@pytest.fixture
def a_estrella_b_estrella():
    """AFND-λ para a*b*: λ separa la fase de las a de la fase de las b."""
    return Automata("ab", ["p", "r"], "p", ["r"],
                    [("p", "a", "p"), ("p", "", "r"), ("r", "b", "r")])


# ----------------------------------------------------------------------
# AFD: aceptación y rechazo
# ----------------------------------------------------------------------

def test_tipo_afd(pares_de_ceros):
    assert pares_de_ceros.tipo == AFD
    assert pares_de_ceros.es_completo


@pytest.mark.parametrize("w", ["", "1", "00", "1001", "0110", "100100"])
def test_afd_acepta(pares_de_ceros, w):
    assert pares_de_ceros.acepta(w)


@pytest.mark.parametrize("w", ["0", "10", "000", "0100", "1110111"])
def test_afd_rechaza(pares_de_ceros, w):
    assert not pares_de_ceros.acepta(w)


def test_afd_traza_un_estado_por_paso(pares_de_ceros):
    pasos = pares_de_ceros.traza("0110")
    assert [sorted(p.despues) for p in pasos] == [["par"], ["impar"], ["impar"], ["impar"], ["par"]]
    assert pasos[1].tomadas == [("par", "0", "impar")]


def test_simbolo_fuera_del_alfabeto_rechaza(pares_de_ceros):
    assert not pares_de_ceros.acepta("012")


# ----------------------------------------------------------------------
# AFND
# ----------------------------------------------------------------------

def test_tipo_afnd(termina_en_01):
    assert termina_en_01.tipo == AFND


@pytest.mark.parametrize("w,esperado", [("01", True), ("1101", True), ("0", False), ("010", False), ("", False)])
def test_afnd_acepta(termina_en_01, w, esperado):
    assert termina_en_01.acepta(w) is esperado


def test_afnd_caminos_bifurcan(termina_en_01):
    caminos, truncado = termina_en_01.caminos("001")
    assert not truncado
    aceptan = [c for c in caminos if c.acepta]
    assert len(aceptan) == 1
    assert aceptan[0].texto("q0") == "q0 -0→ q0 -0→ q1 -1→ q2"
    # El camino que adivina el 01 en la primera posición muere al leer el segundo 0.
    assert any(not c.acepta and c.leidos == 1 for c in caminos)


def test_subconjuntos_equivalente(termina_en_01):
    afd = termina_en_01.subconjuntos()
    assert afd.tipo == AFD and afd.es_completo
    assert afd.equivalente(termina_en_01)
    assert len(afd.estados) == 3  # {q0}, {q0,q1}, {q0,q2}


# ----------------------------------------------------------------------
# AFND-λ
# ----------------------------------------------------------------------

def test_tipo_afnd_lambda(anexo3):
    assert anexo3.tipo == AFND_LAMBDA


def test_lambda_clausura(anexo3, a_estrella_b_estrella):
    assert anexo3.clausura("q0") == {"q0", "q1"}
    assert anexo3.clausura("q1") == {"q1"}
    assert a_estrella_b_estrella.clausura({"p"}) == {"p", "r"}


def test_acepta_cadena_que_requiere_clausura(anexo3, a_estrella_b_estrella):
    # "b" solo se acepta porque, tras leerla en q0, la λ-clausura alcanza q1.
    assert anexo3.acepta("b")
    assert anexo3.acepta("")
    assert not anexo3.mover({"q0"}, "b") & anexo3.aceptacion
    # En a*b*, "aabb" exige cruzar la transición λ de p a r entre las a y las b.
    assert a_estrella_b_estrella.acepta("aabb")
    assert not a_estrella_b_estrella.acepta("aba")


def test_traza_registra_transiciones_lambda(anexo3):
    pasos = anexo3.traza("b")
    assert pasos[0].por_lambda == [("q0", "", "q1")]
    assert pasos[1].despues == {"q0", "q1"}


def test_sin_lambda_y_afd_equivalentes(a_estrella_b_estrella):
    afnd = a_estrella_b_estrella.sin_lambda()
    assert afnd.tipo in (AFD, AFND) and not afnd.tiene_lambda
    afd = afnd.subconjuntos()
    for w in cadenas("ab", 7):
        esperado = w == "a" * w.count("a") + "b" * w.count("b")
        assert a_estrella_b_estrella.acepta(w) is afnd.acepta(w) is afd.acepta(w) is esperado


def test_ciclo_lambda_no_cuelga():
    m = Automata("a", ["x", "y"], "x", ["y"], [("x", "", "y"), ("y", "", "x"), ("y", "a", "y")])
    assert m.clausura("x") == {"x", "y"}
    caminos, _ = m.caminos("aa")
    assert any(c.acepta for c in caminos)


# ----------------------------------------------------------------------
# Minimización y validación
# ----------------------------------------------------------------------

def test_hopcroft_reduce_estados_equivalentes():
    # Dos copias del mismo contador de paridad: el mínimo tiene 2 estados.
    m = Automata("01", "ABCD", "A", ["A", "C"],
                 [("A", "0", "B"), ("A", "1", "C"), ("B", "0", "C"), ("B", "1", "D"),
                  ("C", "0", "D"), ("C", "1", "A"), ("D", "0", "A"), ("D", "1", "B")])
    minimo = m.minimizar()
    assert len(minimo.estados) == 2
    assert minimo.equivalente(m)


def test_familia_n_esimo_desde_el_final_alcanza_2_a_la_n():
    """L_n = {w : el n-ésimo símbolo desde el final es 1}: AFND de n+1 estados, AFD mínimo de 2^n."""
    for n in range(1, 7):
        estados = [f"q{i}" for i in range(n + 1)]
        trans = [("q0", "0", "q0"), ("q0", "1", "q0"), ("q0", "1", "q1")]
        trans += [(f"q{i}", a, f"q{i + 1}") for i in range(1, n) for a in "01"]
        m = Automata("01", estados, "q0", [f"q{n}"], trans)
        assert len(m.minimizar().estados) == 2 ** n


def test_contraejemplo_es_la_cadena_mas_corta(pares_de_ceros, termina_en_01):
    assert pares_de_ceros.contraejemplo(termina_en_01) == ""


def test_validacion_detecta_errores():
    with pytest.raises(AutomataInvalido):
        Automata("ab", ["q0"], "q9", [], []).validar()
    with pytest.raises(AutomataInvalido):
        Automata("ab", ["q0"], "q0", [], [("q0", "c", "q0")]).validar()
    with pytest.raises(AutomataInvalido):
        Automata(["a", ""], ["q0"], "q0", [], []).validar()


def test_simbolos_de_varios_caracteres():
    m = Automata(["SYN", "ACK"], ["a", "b", "c"], "a", ["c"], [("a", "SYN", "b"), ("b", "ACK", "c")])
    assert m.simbolos("SYN ACK") == ["SYN", "ACK"]
    assert m.simbolos("SYNACK") == ["SYN", "ACK"]
    assert m.acepta("SYN ACK")
    assert not m.acepta("ACK")


# ----------------------------------------------------------------------
# Tabla interactiva de la interfaz (sin Flet)
# ----------------------------------------------------------------------

def test_desde_tabla_como_la_escribe_el_usuario():
    from automata import desde_tabla

    celdas = {("q0", "a"): "q1", ("q0", "b"): " q0 ", ("q0", ""): "{q1}", ("q1", "a"): "∅", ("q1", "b"): ""}
    m = desde_tabla("a, b", "q0, q1", "q0", {"q1"}, celdas)
    assert m.tipo == AFND_LAMBDA
    assert m.acepta("bb") and m.acepta("ba") and not m.acepta("ab")


def test_desde_tabla_rechaza_destino_desconocido():
    from automata import desde_tabla

    with pytest.raises(AutomataInvalido):
        desde_tabla("a", "q0", "q0", set(), {("q0", "a"): "q7"})
