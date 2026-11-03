"""Genera los autómatas, la evidencia de JFLAP y la documentación del Ejercicio 2.

Uso, desde la raíz del repositorio (requiere Java y JFLAP 7.1):

    set JFLAP_JAR=C:\\ruta\\JFLAP7.1.jar        (o export JFLAP_JAR=... en bash)
    python herramientas/generar.py todo

Etapas (se pueden correr por separado):

    archivos     .json y .xml de cada autómata (.jff de los nuevos), conversión
                 AFND-λ → AFND y lista de casos de prueba
    jflap        corre los casos en el motor de JFLAP, convierte AFN → AFD con
                 NFAToDFA de JFLAP y captura la simulación paso a paso
    documentos   construye automatas/conversiones/*-AFD y escribe docs/

Los resultados de JFLAP se guardan en evidencias/jflap/*.tsv, así que
``documentos`` puede repetirse sin Java.
"""

from __future__ import annotations

import collections
import os
import pathlib
import random
import subprocess
import sys
import xml.etree.ElementTree as ET
from collections import deque

RAIZ = pathlib.Path(__file__).resolve().parent.parent
sys.path[:0] = [str(RAIZ / "src"), str(RAIZ / "herramientas")]

import practica1 as p1  # noqa: E402
from automata import AFD, Automata, mostrar_conjunto  # noqa: E402
from catalogo import AFD_, AFND_, CARPETA, EJERCICIOS, LAMBDA_, NINGUNA, expresion_de, piezas  # noqa: E402
from formatos import cargar, escribir_jff, guardar, guardar_tres  # noqa: E402

AUT = RAIZ / "automatas"
CONV = AUT / "conversiones"
EVID = RAIZ / "evidencias" / "jflap"
PASOS = EVID / "pasos"
DOCS = RAIZ / "docs"
DOCS_J = DOCS / "jflap"
CASOS_TSV = EVID / "casos.tsv"
RES_TSV = EVID / "resultados-jflap.tsv"
CONV_LST = EVID / "conversiones.txt"
CONV_TSV = EVID / "conversiones-jflap.tsv"
PASOS_TSV = EVID / "pasos.tsv"
FUERA = "#"  # símbolo que no pertenece a ningún alfabeto del catálogo


# ======================================================================
# Utilidades
# ======================================================================

def cargar_pieza(ejercicio, pieza) -> Automata:
    if pieza.automata is not None:
        return pieza.automata
    return cargar(AUT / ejercicio.carpeta / f"{pieza.archivo}.jff")


def ruta(ejercicio, pieza, ext=".jff"):
    return AUT / ejercicio.carpeta / f"{pieza.archivo}{ext}"


def rel(p, desde=DOCS_J):
    return os.path.relpath(p, desde).replace(os.sep, "/")


def v(w):
    return f"`{w}`" if w else "λ"


def oraculo(pieza, cache):
    o = pieza.oraculo
    if isinstance(o, str):
        return cache[o].acepta
    return o


def distancias(m: Automata, objetivo):
    """Para cada estado de un AFD completo, la cadena más corta que lleva a ``objetivo``."""
    inversa = collections.defaultdict(list)
    for (q, a), d in m.transiciones.items():
        for p in d:
            inversa[p].append((q, a))
    camino = {q: "" for q in objetivo}
    cola = deque(objetivo)
    while cola:
        p = cola.popleft()
        for q, a in sorted(inversa[p]):
            if q not in camino:
                camino[q] = a + camino[p]
                cola.append(q)
    return camino


def seleccionar(aut: Automata, semilla: int):
    """Cinco cadenas válidas y cinco inválidas, de longitudes crecientes.

    Se camina al azar por el AFD mínimo, sin salir de los estados desde los que
    todavía se puede aceptar (o rechazar), y se completa con el camino más corto.
    """
    m = aut.minimizar()
    azar = random.Random(semilla)
    resultado = {}
    for acepta in (True, False):
        objetivo = m.aceptacion if acepta else set(m.estados) - m.aceptacion
        faltan = distancias(m, objetivo)
        elegidas = []
        if m.inicial in faltan:
            elegidas.append(faltan[m.inicial])
            for largo in (2, 4, 7, 11, 16, 9, 13, 5, 3, 20):
                for _ in range(30):
                    q, w = m.inicial, ""
                    for _ in range(largo):
                        opciones = [a for a in m.alfabeto if next(iter(m.destinos(q, a))) in faltan]
                        if not opciones:
                            break
                        a = azar.choice(opciones)
                        w += a
                        q = next(iter(m.destinos(q, a)))
                    w += faltan[q]
                    if w not in elegidas:
                        elegidas.append(w)
                        break
                if len(elegidas) >= 5:
                    break
        if not acepta:
            for extra in (FUERA, m.alfabeto[0] + FUERA, FUERA + m.alfabeto[-1] * 2):
                if len(elegidas) < 5:
                    elegidas.append(extra)
        elegidas = sorted(set(elegidas), key=lambda w: (len(w), w))[:5]
        resultado[acepta] = elegidas
    return resultado[True], resultado[False]


def leer_tsv(p):
    if not p.exists():
        return []
    return [linea.split("\t") for linea in p.read_text(encoding="utf-8").split("\n") if linea]


# ======================================================================
# Etapa 1: archivos
# ======================================================================

def etapa_archivos():
    CONV.mkdir(parents=True, exist_ok=True)
    PASOS.mkdir(parents=True, exist_ok=True)
    cache = {}
    casos, convertir, pasos = [], [], []
    for k, (e, p) in enumerate(piezas()):
        aut = cargar_pieza(e, p)
        aut.nombre = p.archivo
        cache[p.archivo] = aut
        if p.automata is not None:
            guardar(aut, ruta(e, p))
        for ext in (".json", ".xml"):
            guardar(aut, ruta(e, p, ext))
        val, inv = seleccionar(aut, k)
        for w in val + inv:
            casos.append(f"{rel(ruta(e, p), RAIZ)}\t{w}")
        # Para la simulación paso a paso en JFLAP: una válida corta pero no trivial.
        candidatas = [w for w in val if 2 <= len(w) <= 5] or [w for w in val if w and len(w) <= 6] \
            or [w for w in inv if w and FUERA not in w and len(w) <= 5] or [""]
        pasos.append(f"{rel(ruta(e, p), RAIZ)}\t{candidatas[0]}\t{rel(PASOS / (p.archivo + '.png'), RAIZ)}")
        if p.convertir and e.seccion in (AFND_, LAMBDA_) and aut.tipo != AFD:
            if aut.tiene_lambda:
                sin = aut.sin_lambda(nombre=f"{p.archivo}-AFND").sin_inaccesibles()
                assert sin.equivalente(aut)
                guardar_tres(sin, CONV / f"{p.archivo}-AFND")
                convertir.append(rel(CONV / f"{p.archivo}-AFND.jff", RAIZ))
            else:
                convertir.append(rel(ruta(e, p), RAIZ))
    # Familia Lₙ = {w : el n-ésimo símbolo desde el final es 1}: el peor caso de la construcción.
    for n in range(1, 7):
        m = familia(n)
        guardar_tres(m, CONV / f"familia-L{n}-AFND")
        convertir.append(rel(CONV / f"familia-L{n}-AFND.jff", RAIZ))
    CASOS_TSV.write_text("\n".join(casos) + "\n", encoding="utf-8", newline="\n")
    CONV_LST.write_text("\n".join(convertir) + "\n", encoding="utf-8", newline="\n")
    PASOS_TSV.write_text("\n".join(pasos) + "\n", encoding="utf-8", newline="\n")
    print(f"{len(cache)} autómatas, {len(casos)} casos, {len(convertir)} conversiones, {len(pasos)} simulaciones")


def familia(n):
    estados = [f"q{i}" for i in range(n + 1)]
    trans = [("q0", "0", "q0"), ("q0", "1", "q0"), ("q0", "1", "q1")]
    trans += [(f"q{i}", a, f"q{i + 1}") for i in range(1, n) for a in "01"]
    return Automata("01", estados, "q0", [f"q{n}"], trans, f"familia-L{n}-AFND")


# ======================================================================
# Etapa 2: JFLAP
# ======================================================================

def etapa_jflap():
    jar = os.environ.get("JFLAP_JAR")
    if not jar:
        sys.exit("Defina JFLAP_JAR con la ruta de JFLAP7.1.jar")
    java = os.environ.get("JAVA", "java")
    javac = os.environ.get("JAVAC", "javac")
    clases = RAIZ / "build" / "clases"
    clases.mkdir(parents=True, exist_ok=True)
    fuentes = [str(p) for p in (RAIZ / "herramientas").glob("Jflap*.java")]
    subprocess.run([javac, "-nowarn", "-cp", jar, "-d", str(clases), *fuentes], check=True)
    cp = os.pathsep.join([str(clases), jar])
    base = [java, "-Duser.language=en", "-cp", cp]
    if not os.environ.get("SOLO_PASOS"):
        subprocess.run(base + ["JflapLote", str(CASOS_TSV), str(RES_TSV)], check=True, cwd=RAIZ)
        subprocess.run(base + ["JflapConvertir", str(CONV_LST), str(CONV_TSV)], check=True, cwd=RAIZ)
    if os.environ.get("SIN_PASOS") is None or os.environ.get("SOLO_PASOS"):
        subprocess.run(base + ["JflapPasos", str(PASOS_TSV)], check=True, cwd=RAIZ)


# ======================================================================
# Etapa 3: conversiones de JFLAP → archivos
# ======================================================================

def ids_a_nombres(jff):
    raiz = ET.parse(RAIZ / jff).getroot()
    return {s.get("id"): s.get("name") for s in raiz.iter("state")}


def afd_de_jflap():
    """{ruta del AFN: AFD que produjo JFLAP}, con cada estado llamado como su conjunto de estados del AFN."""
    filas = collections.defaultdict(list)
    for r in leer_tsv(CONV_TSV):
        filas[r[0]].append(r[1:])
    resultado = {}
    for jff, renglones in filas.items():
        nombres = ids_a_nombres(jff)
        nombre_de, finales, inicial, trans = {}, set(), None, []
        for r in renglones:
            if r[0] == "S":
                # Si el AFN ya era determinista, JFLAP lo devuelve sin etiquetas: cada estado es él mismo.
                conjunto = {nombres[i] for i in r[2].split(",") if i} if r[2] else {r[1]}
                nombre_de[r[1]] = mostrar_conjunto(conjunto)
                if r[3] == "true":
                    inicial = nombre_de[r[1]]
                if r[4] == "true":
                    finales.add(nombre_de[r[1]])
        for r in renglones:
            if r[0] == "T":
                trans.append((nombre_de[r[1]], r[3], nombre_de[r[2]]))
        afn = cargar(RAIZ / jff)
        orden = sorted(nombre_de.values(), key=lambda s: (s != inicial, s))
        resultado[jff] = Automata(afn.alfabeto, orden, inicial, finales, trans)
    return resultado


# ======================================================================
# Etapa 3: documentos
# ======================================================================

def recorrido_afd(aut, w):
    pasos = aut.traza(w)
    texto = next(iter(pasos[0].despues))
    for p in pasos[1:]:
        if not p.despues:
            return texto + f" -{p.simbolo}→ (sin transición)"
        texto += f" -{p.simbolo}→ {next(iter(p.despues))}"
    return texto


def recorrido_conjuntos(aut, w):
    pasos = aut.traza(w)
    texto = mostrar_conjunto(pasos[0].despues)
    for p in pasos[1:]:
        texto += f" -{p.simbolo}→ {mostrar_conjunto(p.despues)}"
    return texto


def bloque_caminos(aut, w, limite=6):
    caminos, truncado = aut.caminos(w, limite=200)
    simbolos = aut.simbolos(w)
    aceptan = [c for c in caminos if c.acepta]
    otros = [c for c in caminos if not c.acepta]
    mostrados = (aceptan[:3] + otros)[:limite]
    lineas = []
    for c in mostrados:
        if c.acepta:
            marca = "✔ acepta"
        elif c.leidos < len(simbolos):
            marca = f"✘ muere tras leer {v(''.join(simbolos[:c.leidos]))}"
        else:
            marca = "✘ termina fuera de F"
        lineas.append(f"    - {c.texto(aut.inicial)} — {marca}")
    resto = len(caminos) - len(mostrados)
    total = f"{len(caminos)}{'+' if truncado else ''}"
    cab = f"  Árbol de cómputo: {total} caminos, {len(aceptan)} de aceptación"
    if resto > 0:
        cab += f" (se muestran {len(mostrados)})"
    return [cab + ":"] + lineas


def tabla_md(aut: Automata, significado=None):
    filas = aut.tabla()
    cab = filas[0] + (["Significado"] if significado else [])
    out = ["| " + " | ".join(cab) + " |", "|" + "---|" * len(cab)]
    for f in filas[1:]:
        q = f[0].lstrip("→*")
        celdas = [c.replace("|", "\\|") for c in f]
        if significado:
            celdas.append(significado.get(q, ""))
        out.append("| " + " | ".join(celdas) + " |")
    t = "\n".join(out)
    if len(aut.estados) > 12:
        t = f"<details><summary>Tabla de transiciones ({len(aut.estados)} estados)</summary>\n\n{t}\n\n</details>"
    return t


def clausuras_md(aut: Automata):
    filas = ["| Estado | Cl(q) | ¿Contiene un estado de F? |", "|---|---|---|"]
    for q in aut.estados:
        c = aut.clausura(q)
        filas.append(f"| {q} | {mostrar_conjunto(c)} | {'sí' if c & aut.aceptacion else 'no'} |")
    t = "\n".join(filas)
    if len(aut.estados) > 12:
        t = f"<details><summary>λ-clausuras de los {len(aut.estados)} estados</summary>\n\n{t}\n\n</details>"
    return t


def r_kleene(aut: Automata):
    """Rᵢⱼ⁽ᵏ⁾ del algoritmo de Kleene para R_{inicial, final}⁽ⁿ⁾, con simplificación de ∅ y λ."""
    est = aut.estados
    n = len(est)

    def par(x):
        return f"({x})" if "+" in x and not (x.startswith("(") and x.endswith(")") and x.count("(") == 1) else x

    def union(a, b):
        if a == "∅":
            return b
        if b == "∅" or a == b:
            return a
        return f"{a}+{b}"

    def conc(*xs):
        if "∅" in xs:
            return "∅"
        xs = [x for x in xs if x != "λ"]
        return "".join(par(x) for x in xs) or "λ"

    def estrella(a):
        if a in ("∅", "λ"):
            return "λ"
        return f"{par(a) if len(a) > 1 else a}*"

    memo, necesarios = {}, collections.defaultdict(set)

    def R(i, j, k):
        necesarios[k].add((i, j))
        if (i, j, k) in memo:
            return memo[i, j, k]
        if k == 0:
            s = [a for a in aut.alfabeto if est[j - 1] in aut.destinos(est[i - 1], a)]
            if i == j:
                s.append("λ")
            r = "+".join(s) if s else "∅"
        else:
            r = union(R(i, j, k - 1), conc(R(i, k, k - 1), estrella(R(k, k, k - 1)), R(k, j, k - 1)))
        memo[i, j, k] = r
        return r

    i0 = est.index(aut.inicial) + 1
    finales = [est.index(q) + 1 for q in aut.aceptacion]
    total = {f: R(i0, f, n) for f in finales}
    return total, necesarios, memo


def notas_md(e: Ejercicio, cache) -> list[str]:  # noqa: F821
    out = []
    if isinstance(e.notas, str):
        if e.notas:
            out += [e.notas, ""]
        return out
    vf = [n for n in e.notas if n[0] == "vf"]
    if vf:
        aut = cache[e.piezas[0].archivo]
        out += ["| Afirmación | Cadena | Expresión | AFND-λ de Thompson | Respuesta | Razón |", "|---|---|---|---|---|---|"]
        for _, num, cadena, expresion, razon in vf:
            if cadena is None:
                out.append(f"| {num} | ∅ (no es cadena) | `{expresion}` | — | **F** | {razon} |")
                continue
            resultado = aut.acepta(cadena)
            esperado = p1.re.fullmatch(p1.vf_python(expresion), cadena) is not None
            assert resultado == esperado, (num, cadena, expresion)
            out.append(f"| {num} | {v(cadena)} | `{expresion}` | {'acepta' if resultado else 'rechaza'} | "
                       f"**{'V' if resultado else 'F'}** | {razon} |")
        out.append("")
    for n in e.notas:
        if n[0] == "er":
            out += [f"**Expresión regular** (archivo de JFLAP [`{n[1]}.jff`]"
                    f"({rel(AUT / ('lista2-afd' if e.seccion == AFD_ else 'lista3-afnd-lambda') / (n[1] + '.jff'))})): "
                    f"`{expresion_de(n[1])}` (en JFLAP, `+` es la unión y `!` es λ).", ""]
        elif n[0] == "texto":
            out += [f"**Obtención.** {n[1]}", ""]
        elif n[0] == "thompson":
            out += [f"**Expresión:** `{n[1]}`.", ""]
        elif n[0] == "kleene":
            aut = cache["L3-259"]
            total, necesarios, memo = r_kleene(aut)
            out += ["Con los estados numerados 1-4, R₁₄⁽⁴⁾ = R₁₄⁽³⁾ + R₁₄⁽³⁾ (R₄₄⁽³⁾)* R₄₄⁽³⁾, y cada Rᵢⱼ⁽ᵏ⁾ se obtiene de "
                    "Rᵢⱼ⁽ᵏ⁻¹⁾ + Rᵢₖ⁽ᵏ⁻¹⁾ (Rₖₖ⁽ᵏ⁻¹⁾)* Rₖⱼ⁽ᵏ⁻¹⁾. Desarrollando la recursión desde R₁₄⁽⁴⁾, los valores "
                    "necesarios son:", "", "| k | Pares (i, j) necesarios | Valores |", "|---|---|---|"]
            for k in sorted(necesarios, reverse=True):
                pares = sorted(necesarios[k])
                valores = "; ".join(f"R{i}{j}⁽{k}⁾ = `{memo[i, j, k]}`" for i, j in pares)
                out.append(f"| {k} | {', '.join(f'({i},{j})' for i, j in pares)} | {valores} |")
            out += ["", f"**Resultado:** R₁₄⁽⁴⁾ = `{total[4]}`. El estado 4 no es alcanzable desde 1 (de 1, 2 y 3 solo se "
                    "llega a 1, 2 y 3), así que todos los Rᵢ₄⁽ᵏ⁾ con i ≤ 3 valen ∅ y la expresión equivalente al "
                    "autómata es **∅**: el lenguaje es vacío.", ""]
    incisos = [n for n in e.notas if n[0] in ("dg", "cl", "d")]
    if incisos:
        aut = cache[e.piezas[0].archivo]
        out += ["**Incisos** (δ es la función del autómata original):", ""]
        for letra, n in zip("abcdefgh", incisos):
            if n[0] == "cl":
                out.append(f"- {letra}) Cl({{{', '.join(n[1])}}}) = {mostrar_conjunto(aut.clausura(set(n[1])))}")
            elif n[0] == "d":
                out.append(f"- {letra}) δ({n[1]}, {n[2]}) = {mostrar_conjunto(aut.destinos(n[1], n[2]))} "
                           f"(sin clausura; con ella, δ̂({n[1]}, {n[2]}) = {mostrar_conjunto(aut.delta_gorro({n[1]}, n[2]))})")
            else:
                cam = recorrido_conjuntos(Automata(aut.alfabeto, aut.estados, n[1], aut.aceptacion, aut.transiciones), n[2])
                out.append(f"- {letra}) δ̂({n[1]}, {n[2]}) = {mostrar_conjunto(aut.delta_gorro({n[1]}, n[2]))}: {cam}")
        out.append("")
    return out


def delta_gorro_p1(num):
    for n, desde, t, consultas in p1.DELTA_GORRO:
        if str(n) == num:
            lineas = ["**Valores pedidos** (con los nombres de estado de la tabla):", ""]
            for c in consultas:
                z, w = c.split("|")
                pasos = p1.traza(t, z, w)
                cadena = mostrar_conjunto(pasos[0])
                for a, s in zip(w, pasos[1:]):
                    cadena += f" -{a}→ {mostrar_conjunto(s)}"
                lineas.append(f"- δ̂({{{', '.join(z)}}}, {w}) = {mostrar_conjunto(pasos[-1])}: {cadena}")
            return lineas + [""]
    return []


def seccion_pieza(e, p, aut, jflap, conversiones, cache, k):
    out = []
    val, inv = seleccionar(aut, k)
    o = oraculo(p, cache) or aut.acepta
    archivos = " · ".join(f"[`{p.archivo}{x}`]({rel(ruta(e, p, x))})" for x in (".jff", ".json", ".xml"))
    out += [f"#### {p.titulo} — `{p.archivo}`", "", f"Archivos: {archivos}. Tipo según la definición: **{aut.tipo}**, "
            f"|Q| = {len(aut.estados)}, Σ = {{{', '.join(aut.alfabeto)}}}, {aut.num_transiciones()} transiciones.", "",
            f"**Diseño.** {p.diseno}", "", tabla_md(aut, p.significado), ""]
    if aut.tiene_lambda or e.seccion == LAMBDA_:
        if aut.tiene_lambda:
            out += [f"**Transiciones λ.** {p.lambda_razon}", "", "**λ-clausuras.** Cl(q) son los estados a los que se "
                    "llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra "
                    "el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.", "",
                    clausuras_md(aut), ""]
        else:
            out += ["**Transiciones λ.** La construcción de Thompson de una expresión sin operadores (un símbolo o ∅) "
                    "no produce transiciones λ: el fragmento básico ya es el autómata completo.", ""]
    out += ["| # | Cadena | Se espera | Simulador | JFLAP |", "|---|---|---|---|---|"]
    filas_rec = []
    for i, (w, tipo) in enumerate([(x, True) for x in val] + [(x, False) for x in inv], 1):
        esperado = bool(o(w)) if FUERA not in w else False
        sim = aut.acepta(w)
        jf = jflap.get((rel(ruta(e, p), RAIZ), w))
        assert esperado == tipo == sim, (p.archivo, w)
        if jf is not None:
            assert jf == sim, ("JFLAP", p.archivo, w)
        nota = " (símbolo fuera de Σ)" if FUERA in w else ""
        out.append(f"| {i} | {v(w)}{nota} | {'acepta' if tipo else 'rechaza'} | {'acepta' if sim else 'rechaza'} | "
                   f"{'—' if jf is None else ('acepta' if jf else 'rechaza')} |")
        if aut.es_determinista and not aut.tiene_lambda:
            filas_rec.append(f"{i}. {v(w)}: {recorrido_afd(aut, w)} — {'✔' if sim else '✘'}")
        else:
            filas_rec.append(f"{i}. {v(w)}: {recorrido_conjuntos(aut, w)} — {'✔' if sim else '✘'}")
            filas_rec += bloque_caminos(aut, w)
    faltan = []
    if len(val) < 5:
        faltan.append(f"el lenguaje solo tiene {len(val)} palabra{'s' if len(val) != 1 else ''}")
    if any(FUERA in w for w in inv):
        faltan.append("todas las cadenas sobre Σ pertenecen al lenguaje, así que las inválidas usan un símbolo "
                      f"fuera de Σ ({FUERA})")
    if faltan:
        out += ["", "Nota sobre los casos: " + "; ".join(faltan) + "."]
    out += ["", "<details><summary>Recorrido completo de cada cadena</summary>", ""] + filas_rec + ["", "</details>", ""]
    img = PASOS / f"{p.archivo}.png"
    if img.exists():
        w_paso = next((r[1] for r in leer_tsv(PASOS_TSV) if r[0] == rel(ruta(e, p), RAIZ)), "")
        out += [f"Simulación paso a paso en JFLAP con {v(w_paso)}: [ver captura]({rel(img)}).", ""]
    conv = conversiones.get(p.archivo)
    if conv:
        out += conv + [""]
    return out


def etapa_documentos():
    jflap = {(r[0], r[1]): r[2] == "true" for r in leer_tsv(RES_TSV)}
    afds = afd_de_jflap()
    cache = {}
    for e, p in piezas():
        cache[p.archivo] = cargar_pieza(e, p)
    comparacion, conversiones = [], {}
    # Conversiones: AFND-λ → AFND (este proyecto) y AFND → AFD (NFAToDFA de JFLAP).
    for e, p in piezas():
        aut = cache[p.archivo]
        afn_jff = rel(CONV / f"{p.archivo}-AFND.jff", RAIZ) if aut.tiene_lambda else rel(ruta(e, p), RAIZ)
        if afn_jff not in afds:
            continue
        afn = cargar(RAIZ / afn_jff)
        afd = afds[afn_jff]
        afd.nombre = f"{p.archivo}-AFD"
        assert afd.equivalente(aut), p.archivo
        guardar_tres(afd, CONV / f"{p.archivo}-AFD")
        completo = aut.subconjuntos()
        minimo = aut.minimizar()
        n = len(afn.estados)
        fila = dict(archivo=p.archivo, ejercicio=e.num, seccion=e.seccion, n_lambda=len(aut.estados) if aut.tiene_lambda else None,
                    n=n, t_afn=afn.num_transiciones(), afd=len(afd.estados), t_afd=afd.num_transiciones(),
                    completo=len(completo.estados), minimo=len(minimo.estados), cota=2 ** n,
                    activos=max(len(s.despues) for w in aut.cadenas_aceptadas(6, 3) or [""] for s in afn.traza(w)))
        comparacion.append(fila)
        lineas = ["**Conversión.**"]
        if aut.tiene_lambda:
            lineas.append(f"AFND-λ ({len(aut.estados)} estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y "
                          f"F' = {{q : Cl(q) ∩ F ≠ ∅}}, quitando los inaccesibles: {n} estados, "
                          f"[`{p.archivo}-AFND.jff`]({rel(CONV / (p.archivo + '-AFND.jff'))}).")
        lineas.append(f"AFND ({n} estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): {len(afd.estados)} "
                      f"estados, [`{p.archivo}-AFD.jff`]({rel(CONV / (p.archivo + '-AFD.jff'))}) "
                      f"([.json]({rel(CONV / (p.archivo + '-AFD.json'))}), [.xml]({rel(CONV / (p.archivo + '-AFD.xml'))})). "
                      f"JFLAP omite el conjunto vacío; con él, el AFD completo tiene {len(completo.estados)} estados, y el "
                      f"AFD mínimo (Hopcroft), {len(minimo.estados)}. La cota es 2^{n} = {2 ** n}. Se verificó que los "
                      "tres autómatas aceptan el mismo lenguaje.")
        conversiones[p.archivo] = [" ".join(lineas[:1]) + " " + " ".join(lineas[1:])]
    # Familia Lₙ.
    familia_filas = []
    for n in range(1, 7):
        jff = rel(CONV / f"familia-L{n}-AFND.jff", RAIZ)
        if jff in afds:
            afd = afds[jff]
            afd.nombre = f"familia-L{n}-AFD"
            guardar_tres(afd, CONV / f"familia-L{n}-AFD")
            familia_filas.append((n, n + 1, len(afd.estados), len(afd.minimizar().estados), 2 ** (n + 1)))

    # Documentos por sección.
    DOCS_J.mkdir(parents=True, exist_ok=True)
    grupos = [
        ("afd-lista2.md", "AFD — Lista 2", lambda e: e.seccion in (AFD_, NINGUNA) and e.lista == 2),
        ("afd-lista3.md", "AFD — Lista 3", lambda e: e.seccion == AFD_ and e.lista == 3),
        ("afnd.md", "AFND estándar", lambda e: e.seccion in (AFND_,) or (e.seccion == NINGUNA and e.lista == 3)),
        ("afnd-lambda-1.md", "AFND-λ (problemas 162-200)", lambda e: e.seccion == LAMBDA_ and e.orden[0] <= 200),
        ("afnd-lambda-2.md", "AFND-λ (problemas 201-240)", lambda e: e.seccion == LAMBDA_ and 200 < e.orden[0] <= 240),
        ("afnd-lambda-3.md", "AFND-λ (problemas 241-253)", lambda e: e.seccion == LAMBDA_ and e.orden[0] > 240),
    ]
    doc_de = {}
    k = 0
    indices = {id(p): i for i, (_, p) in enumerate(piezas())}
    for archivo, titulo, filtro in grupos:
        out = [f"# Ejercicio 2 — {titulo}", "", "[← Ejercicio 2](../02-jflap.md) · [Índice](../../README.md)", "",
               "Cada autómata indica su clasificación, el diseño, la tabla de transiciones, cinco cadenas válidas y cinco "
               "inválidas con el resultado esperado (oráculo escrito a partir del enunciado), el del simulador de este "
               "proyecto y el del motor de JFLAP 7.1, el recorrido de cada cadena (en los no deterministas, el conjunto "
               "de estados activos y el árbol de caminos) y la captura de la simulación paso a paso en JFLAP.", ""]
        for e in [x for x in EJERCICIOS if filtro(x)]:
            doc_de[e.num, e.lista] = archivo
            ancla = f"problema-{e.lista}-{e.num}".replace(" ", "-").replace("(", "").replace(")", "").replace(",", "").replace(".", "")
            out += [f'<a id="{ancla}"></a>', "", f"## Lista {e.lista}, problema {e.num}", "",
                    f"**Enunciado.** {e.enunciado}", "",
                    f"**Clasificación: {e.seccion}.** {e.justificacion}" + (" *(Entregado en la Práctica 1; aquí se agregan "
                                                                             "los formatos .json y .xml, las pruebas y "
                                                                             "los recorridos.)*" if e.practica1 else ""), ""]
            out += notas_md(e, cache)
            out += delta_gorro_p1(e.num)
            for p in e.piezas:
                out += seccion_pieza(e, p, cache[p.archivo], jflap, conversiones, cache, indices[id(p)])
        (DOCS_J / archivo).write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
        print(archivo, round((DOCS_J / archivo).stat().st_size / 1024), "KB")
    escribir_resumen(doc_de, comparacion, familia_filas, cache, jflap)


def ancla_de(e):
    return f"problema-{e.lista}-{e.num}".replace(" ", "-").replace("(", "").replace(")", "").replace(",", "").replace(".", "")


def escribir_resumen(doc_de, comparacion, familia_filas, cache, jflap):
    import resumen

    texto = resumen.documento(EJERCICIOS, doc_de, comparacion, familia_filas, cache, jflap, ancla_de)
    (DOCS / "02-jflap.md").write_text(texto, encoding="utf-8", newline="\n")
    print("02-jflap.md", round((DOCS / "02-jflap.md").stat().st_size / 1024), "KB")


if __name__ == "__main__":
    etapa = sys.argv[1] if len(sys.argv) > 1 else "todo"
    if etapa in ("archivos", "todo"):
        etapa_archivos()
    if etapa in ("jflap", "todo"):
        etapa_jflap()
    if etapa in ("documentos", "todo"):
        etapa_documentos()
