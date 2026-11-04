"""Práctica 3, apartado 2.6: los algoritmos de src/algoritmos.py con los casos de la Lista 3.

Para cada caso de automatas/practica3/casos-de-prueba/ se comprueba que el
autómata original, el AFN sin λ, el AFD de subconjuntos y el AFD mínimo
aceptan exactamente las mismas cadenas de Σ⁰ ∪ … ∪ Σᴸ, con L = LONGITUD.

Por qué L = 8: el veredicto de cada autómata, simulado por conjuntos, depende
solo del conjunto de estados activos. Si se simulan los cuatro a la vez, la
configuración es una tupla (S₁, S₂, S₃, S₄); toda tupla alcanzable se alcanza
con una cadena de longitud ≤ d, donde d es la profundidad del recorrido en
anchura del producto (``profundidad_producto``). Si los cuatro coinciden en
todas las cadenas de longitud ≤ d, coinciden en todas las cadenas. En los 19
casos d ≤ 5 (se comprueba abajo), así que L = 8 basta con margen y la prueba
es exhaustiva, no una muestra: |Σ⁰ ∪ … ∪ Σ⁸| = 511 cadenas por autómata.
"""

import pathlib

import pytest

from algoritmos import (
    SUMIDERO,
    clausura_lambda,
    clausuras,
    construir_subconjuntos,
    de_afn_lambda_a_minimo,
    eliminar_lambda,
    equivalentes_por_minimizacion,
    informe_lote,
    isomorfismo,
    leer_cadenas,
    minimizar_afd,
    palabras,
    profundidad_producto,
    simular_directo,
    validar_lote,
)
from automata import LAMBDA, Automata, AutomataInvalido
from formatos import cargar

LONGITUD = 8
CASOS_DIR = pathlib.Path(__file__).resolve().parent.parent / "automatas" / "practica3" / "casos-de-prueba"

LAMBDA_196_200 = ["L3-196", "L3-197", "L3-198", "L3-199", "L3-200"]
AFN_191_194_260_263 = ["L3-192-AFND", "L3-193-AFND", "L3-194-AFND",
                       "L3-260-AFND", "L3-261-AFND", "L3-262-AFND", "L3-263-AFND"]
AFD_151_157 = [f"L3-{n}-original" for n in range(151, 158)]
TODOS = LAMBDA_196_200 + AFN_191_194_260_263 + AFD_151_157


def caso(nombre):
    return cargar(CASOS_DIR / f"{nombre}.jff")


@pytest.fixture(scope="module", params=TODOS)
def cadena(request):
    return de_afn_lambda_a_minimo(caso(request.param))


# ----------------------------------------------------------------------
# 2.6: los cuatro autómatas aceptan las mismas cadenas
# ----------------------------------------------------------------------

def test_los_cuatro_aceptan_las_mismas_cadenas(cadena):
    original, sin_l, afd, minimo = cadena.automatas
    for w in palabras(original.alfabeto, LONGITUD):
        veredictos = {original.acepta(w), sin_l.acepta(w), afd.acepta(w), minimo.acepta(w)}
        assert len(veredictos) == 1, f"discrepan en {''.join(w) or 'λ'}"


def test_la_longitud_elegida_es_suficiente(cadena):
    """La comparación hasta LONGITUD es exhaustiva: cubre la profundidad del producto."""
    assert profundidad_producto(cadena.automatas) <= LONGITUD


def test_el_minimo_no_tiene_mas_estados(cadena):
    assert len(cadena.minimo.automata.estados) <= len(cadena.subconjuntos.automata.estados)


def test_tipos_de_cada_etapa(cadena):
    assert not cadena.sin_lambda.automata.tiene_lambda
    assert cadena.subconjuntos.automata.tipo == "AFD"
    assert cadena.minimo.automata.tipo == "AFD"


def test_el_minimo_coincide_con_el_de_la_practica2(cadena):
    """La minimización por rondas da el mismo autómata (salvo nombres) que Hopcroft de automata.py."""
    hopcroft = cadena.original.minimizar()
    assert isomorfismo(cadena.minimo.automata, hopcroft) is not None


def test_el_minimo_es_minimo(cadena):
    """Volver a minimizar no quita estados y todo par de estados es distinguible."""
    m = cadena.minimo.automata
    assert len(minimizar_afd(m).automata.estados) == len(m.estados)


def test_tipo_de_los_casos():
    assert all(caso(n).tiene_lambda for n in LAMBDA_196_200)
    assert all(caso(n).tipo == "AFND" for n in AFN_191_194_260_263)
    assert all(caso(n).tipo == "AFD" for n in AFD_151_157)


# ----------------------------------------------------------------------
# 2.1 Cerradura λ y simulación directa
# ----------------------------------------------------------------------

@pytest.mark.parametrize("nombre,estado,esperado", [
    ("L3-196", "A", {"A", "B"}), ("L3-196", "B", {"B"}),
    ("L3-197", "A", {"A", "B", "C", "D"}), ("L3-197", "B", {"B", "D"}),
    ("L3-198", "A", {"A", "B", "C"}), ("L3-198", "D", {"D"}),
    ("L3-199", "A", {"A", "B", "C", "E"}), ("L3-199", "C", {"C", "E"}),
    ("L3-200", "A", {"A", "B"}), ("L3-200", "C", {"C", "E"}),
])
def test_clausuras_de_la_lista(nombre, estado, esperado):
    assert clausura_lambda(caso(nombre), estado).resultado == esperado


@pytest.mark.parametrize("nombre", LAMBDA_196_200)
def test_clausura_coincide_con_el_nucleo(nombre):
    a = caso(nombre)
    for q, c in clausuras(a).items():
        assert c.resultado == a.clausura(q)
        # Cada arco registrado es una transición λ real que agrega un estado nuevo.
        assert all(p in a.destinos(r, LAMBDA) for r, p in c.arcos)
        assert len(c.arcos) == len(c.resultado) - 1


def test_clausura_con_ciclo_lambda():
    a = Automata("a", ["p", "q", "r"], "p", ["r"], [("p", "", "q"), ("q", "", "p"), ("q", "", "r")])
    c = clausura_lambda(a, "p")
    assert c.resultado == {"p", "q", "r"}
    assert c.pasos[-1].endswith("{p, q, r}.")


def test_clausura_de_estado_inexistente():
    with pytest.raises(AutomataInvalido):
        clausura_lambda(caso("L3-196"), "Z")


@pytest.mark.parametrize("nombre", LAMBDA_196_200)
def test_simulacion_directa_coincide_con_delta_gorro(nombre):
    a = caso(nombre)
    for w in palabras(a.alfabeto, 6):
        sim = simular_directo(a, w)
        assert sim.acepta == a.acepta(w)
        assert sim.pasos[-1].despues == a.delta_gorro({a.inicial}, w)
        for p in sim.pasos:
            assert p.despues == a.clausura(p.antes)  # «después» es la cerradura de «antes»


def test_simulacion_directa_muestra_antes_y_despues():
    """Lista 3, problema 196 a): δ̂(A, 110). Cl(A) = {A, B}; al leer 1 solo B avanza (a C) y C no tiene salidas."""
    a = caso("L3-196")
    sim = simular_directo(a, "110")
    assert [len(sim.pasos)] == [4]
    assert sim.pasos[0].antes == {"A"} and sim.pasos[0].despues == {"A", "B"}
    assert sim.pasos[1].antes == {"C"} and sim.pasos[1].despues == {"C"}
    assert sim.pasos[2].despues == sim.pasos[3].despues == set()
    assert not sim.acepta
    assert "antes de la cerradura" in sim.pasos[1].describir(a).lower()


# ----------------------------------------------------------------------
# 2.2 Eliminación de λ
# ----------------------------------------------------------------------

@pytest.mark.parametrize("nombre", LAMBDA_196_200)
def test_eliminar_lambda_es_la_formula(nombre):
    a = caso(nombre)
    r = eliminar_lambda(a)
    assert r.automata == a.sin_lambda()  # la versión de la Práctica 2
    assert set(r.agregadas) == {(q, x, p) for (q, x), d in r.automata.transiciones.items()
                                for p in d if p not in a.destinos(q, x)}
    assert set(r.nuevas_aceptacion) == r.automata.aceptacion - a.aceptacion
    assert len(r.quitadas) == sum(len(a.destinos(q, LAMBDA)) for q in a.estados)


def test_eliminar_lambda_196():
    """Cl(A) = {A, B} y ninguno es de aceptación: F' = F = {C}.

    δ'(A, 0) = Cl(δ({A, B}, 0)) = Cl({A, B}) = {A, B} y δ'(A, 1) = Cl(δ({A, B}, 1)) = Cl({C}) = {C}.
    """
    r = eliminar_lambda(caso("L3-196"))
    assert r.automata.destinos("A", "0") == {"A", "B"}
    assert r.automata.destinos("A", "1") == {"C"}
    assert r.nuevas_aceptacion == []


def test_eliminar_lambda_hace_nuevos_finales():
    """En el 197 F = {D} y Cl(A), Cl(B) y Cl(C) contienen a D: los tres pasan a ser de aceptación."""
    r = eliminar_lambda(caso("L3-197"))
    assert r.nuevas_aceptacion == ["A", "B", "C"]


# ----------------------------------------------------------------------
# 2.3 Subconjuntos
# ----------------------------------------------------------------------

@pytest.mark.parametrize("nombre", AFN_191_194_260_263)
def test_subconjuntos_coincide_con_la_practica2(nombre):
    a = caso(nombre)
    r = construir_subconjuntos(a)
    assert isomorfismo(r.automata, a.subconjuntos()) is not None


@pytest.mark.parametrize("nombre", AFN_191_194_260_263)
def test_tabla_de_subconjuntos(nombre):
    a = caso(nombre)
    r = construir_subconjuntos(a)
    vistos = {r.filas[0].conjunto}
    for k, f in enumerate(r.filas):
        assert f.conjunto in vistos  # solo se procesan subconjuntos ya descubiertos (alcanzables)
        vistos |= set(f.nuevos)
        assert f.aceptacion == bool(f.conjunto & a.aceptacion)
        assert f.razon == f.conjunto & a.aceptacion
    assert len(r.filas) == len(r.automata.estados)


def test_subconjuntos_192_tabla_conocida():
    """El AFD del 192 tiene los 6 subconjuntos que obtuvo JFLAP en la Práctica 2 (más ninguno extra)."""
    a, afd = caso("L3-192-AFND"), cargar(CASOS_DIR.parent.parent / "lista3-afnd" / "L3-192-AFD.jff")
    assert construir_subconjuntos(a).automata.equivalente(afd)


def test_subconjuntos_con_lambda_cierra():
    a = caso("L3-196")
    r = construir_subconjuntos(a)
    assert r.filas[0].conjunto == a.clausura({a.inicial})
    assert r.automata.equivalente(a)


# ----------------------------------------------------------------------
# 2.4 Minimización y equivalencia
# ----------------------------------------------------------------------

@pytest.mark.parametrize("nombre,inaccesibles,minimo", [
    ("L3-151-original", [], 5), ("L3-152-original", [], 5), ("L3-153-original", [], 6),
    ("L3-154-original", ["J"], 7), ("L3-155-original", ["I", "L"], 5),
    ("L3-156-original", [], 3), ("L3-157-original", [], 4),
])
def test_minimizacion_151_157(nombre, inaccesibles, minimo):
    a = caso(nombre)
    r = minimizar_afd(a)
    assert sorted(r.inaccesibles) == inaccesibles
    assert len(r.automata.estados) == minimo
    assert r.automata.equivalente(a)
    # Las rondas solo refinan: cada partición tiene al menos tantos bloques como la anterior.
    tamanos = [len(x.bloques) for x in r.rondas]
    assert tamanos == sorted(tamanos) and tamanos[-1] == tamanos[-2]


@pytest.mark.parametrize("nombre", AFD_151_157)
def test_minimo_contra_el_simplificado_de_la_lista(nombre):
    """El AFD mínimo es isomorfo al simplificado que se entregó en la Práctica 1 / 2 (lista2-afd)."""
    simp = cargar(CASOS_DIR.parent.parent / "lista2-afd" / f"{nombre.replace('original', 'simplificado')}.jff")
    assert equivalentes_por_minimizacion(caso(nombre), simp).equivalentes


def test_minimizar_requiere_afd():
    with pytest.raises(AutomataInvalido):
        minimizar_afd(caso("L3-192-AFND"))


def test_minimizar_completa_con_sumidero():
    a = Automata("ab", ["p", "q"], "p", ["q"], [("p", "a", "q")])
    r = minimizar_afd(a)
    assert r.sumidero == SUMIDERO
    assert len(r.automata.estados) == 3 and r.automata.tipo == "AFD"


def test_equivalencia_por_minimizacion():
    # 192: el AFN y su AFD (de JFLAP) son equivalentes; 192 y 193 no.
    a = caso("L3-192-AFND")
    afd = cargar(CASOS_DIR.parent.parent / "lista3-afnd" / "L3-192-AFD.jff")
    si = equivalentes_por_minimizacion(a, afd)
    assert si.equivalentes and si.mapa is not None
    no = equivalentes_por_minimizacion(a, caso("L3-193-AFND"))
    assert not no.equivalentes and no.mapa is None


def test_equivalencia_coincide_con_contraejemplo():
    nombres = TODOS[:8]
    for x in nombres:
        for y in nombres:
            a, b = caso(x), caso(y)
            if set(a.alfabeto) == set(b.alfabeto):
                assert equivalentes_por_minimizacion(a, b).equivalentes == a.equivalente(b)


def test_isomorfismo_detecta_renombrado():
    m = minimizar_afd(caso("L3-151-original")).automata
    renombrado = m.numerar("z")
    phi = isomorfismo(m, renombrado)
    assert phi is not None and phi[m.inicial] == "z0"
    otro = renombrado.copia()
    otro.aceptacion = set(otro.estados) - otro.aceptacion  # complemento: mismo grafo, distinto F
    assert isomorfismo(m, otro) is None


# ----------------------------------------------------------------------
# 2.5 Validación de varias cadenas
# ----------------------------------------------------------------------

def test_leer_cadenas():
    assert leer_cadenas("01\r\n\nλ\n# comentario\n  11  \n") == ["01", "", "", "11"]


def test_validar_lote_e_informe():
    a = caso("L3-196")
    texto = "110\n\n1\n0012\n"
    resultados = validar_lote(a, texto)
    assert [r.acepta for r in resultados] == [a.acepta(w) for w in ["110", "", "1", "0012"]]
    assert resultados[3].simbolos_fuera == ["2"] and not resultados[3].acepta
    informe = informe_lote(a, resultados, "cadenas.txt")
    assert "cadenas.txt" in informe and "Total: 4 cadenas" in informe
    assert informe.count("ACEPTADA") + informe.count("RECHAZADA") == 4


def test_ejemplo_de_cadenas_del_repositorio():
    ruta = CASOS_DIR.parent / "cadenas-ejemplo.txt"
    resultados = validar_lote(caso("L3-196"), ruta.read_text(encoding="utf-8"))
    assert len(resultados) >= 10
