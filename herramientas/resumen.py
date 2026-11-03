"""Escribe docs/02-jflap.md: clasificación, λ-clausuras y análisis comparativo de las conversiones."""

import collections

from automata import mostrar_conjunto

DESTACADOS = ["L3-192-AFND", "L3-193-AFND", "L3-195-AFND", "L3-260-AFND", "L3-190", "L3-AFND-p099",
              "L3-196", "L3-200", "L3-252"]

DOC_SECCION = {"AFD": "lista2-afd", "AFND": "lista3-afnd", "AFND-λ": "lista3-afnd-lambda"}


def cota(n):
    return f"{2 ** n:,}" if n <= 20 else f"2^{n}"


def documento(ejercicios, doc_de, comparacion, familia, cache, jflap, ancla_de):
    out = ["# Ejercicio 2. AFND y AFND-λ en JFLAP", "", "[← Volver al índice](../README.md)", ""]
    n_piezas = sum(len(e.piezas) for e in ejercicios)
    n_jflap = len(jflap)
    out += [
        "Este documento resume el ejercicio. El detalle de cada autómata (diseño, tabla, diez cadenas con su "
        "recorrido, λ-clausuras, captura de JFLAP y conversión) está en seis documentos, uno por sección:", "",
        "| Documento | Contenido |", "|---|---|",
        "| [AFD — Lista 2](jflap/afd-lista2.md) | Problemas 94-150 |",
        "| [AFD — Lista 3](jflap/afd-lista3.md) | Problemas 151-157 y 254-259 |",
        "| [AFND estándar](jflap/afnd.md) | 143(b), 158-161, 162-188, 189-195 y 260-263 |",
        "| [AFND-λ, parte 1](jflap/afnd-lambda-1.md) | 162-188 resueltos con λ, y 196-200 |",
        "| [AFND-λ, parte 2](jflap/afnd-lambda-2.md) | 201-235 (verdadero o falso) y 236-240 |",
        "| [AFND-λ, parte 3](jflap/afnd-lambda-3.md) | 241-253 (de expresión regular a AFND-λ) |", "",
        "## Cómo se construyó y se verificó", "",
        f"- **{len(ejercicios)} ejercicios** (todos los números del 94 al 263; los de verdadero o falso que comparten "
        f"expresión se agrupan) y **{n_piezas} autómatas**, cada uno en `.jff`, `.json` y `.xml` dentro de "
        "`automatas/`. Los 101 archivos `.jff` de la Práctica 1 se copiaron sin cambios con "
        "`herramientas/importar_p1.py`; los nuevos los escribe `herramientas/generar.py` con `src/formatos.py`.",
        "- **Oráculo independiente.** Cada autómata se comparó con una definición del lenguaje escrita a partir del "
        "enunciado (`herramientas/catalogo.py`), sobre todas las cadenas cortas y cientos de cadenas al azar. Las "
        "pruebas `tests/test_catalogo.py` repiten esa comparación en cada ejecución de pytest.",
        f"- **JFLAP.** Las {n_jflap} cadenas de prueba se corrieron en el motor de simulación de JFLAP 7.1 "
        "(`herramientas/JflapLote.java`); JFLAP coincidió con el resultado esperado en todas. Los resultados están en "
        "[`evidencias/jflap/resultados-jflap.tsv`](../evidencias/jflap/resultados-jflap.tsv).",
        "- **Paso a paso.** Para cada autómata se ejecutó *Input → Step with Closure* en la ventana de JFLAP y se "
        "guardó cada paso (`herramientas/JflapPasos.java`); las capturas están en "
        "[`evidencias/jflap/pasos/`](../evidencias/jflap/pasos/) y se enlazan desde cada autómata.",
        "- **Conversiones.** Los AFND se convirtieron con *Convert → Convert to DFA* de JFLAP (la clase `NFAToDFA`, "
        "`herramientas/JflapConvertir.java`). Los AFND-λ se convirtieron primero a AFND estándar con "
        "`Automata.sin_lambda()` y después a AFD con JFLAP. Todos los resultados están en "
        "[`automatas/conversiones/`](../automatas/conversiones/) y se verificó que cada uno acepta el mismo lenguaje "
        "que el autómata original.", "",
        "Convención: Σ₁ = {0, 1, 2}, Σ₂ = {a, b, c, 0, 1}, Σ₃ = {a, b}; λ es la cadena vacía. Siguiendo la definición "
        "del curso, un **AFD** tiene δ total (δ: Q × Σ → Q). Un autómata determinista con alguna celda vacía es, "
        "formalmente, un AFND con δ(q, a) = ∅; JFLAP lo llamaría DFA.", "",
    ]

    # ------------------------------------------------------------------
    out += ["## 2.1 Clasificación y cobertura", ""]
    cuenta = collections.Counter(e.seccion for e in ejercicios)
    out += ["| Sección | Carpeta | Ejercicios |", "|---|---|---|"]
    for s in ("AFD", "AFND", "AFND-λ", "Ninguna"):
        carpeta = f"[`automatas/{DOC_SECCION[s]}/`](../automatas/{DOC_SECCION[s]}/)" if s in DOC_SECCION else "—"
        out.append(f"| {s} | {carpeta} | {cuenta.get(s, 0)} |")
    out += ["",
            "Las carpetas llevan el nombre que sugiere el enunciado, pero cada una es una **sección por tipo de "
            "autómata**: `lista2-afd/` contiene todos los AFD (los de la Lista 2 y los AFD dados por tabla en la Lista "
            "3, como 151-157 y 254-259), `lista3-afnd/` los AFND estándar (incluido el 143(b) de la Lista 2) y "
            "`lista3-afnd-lambda/` los AFND-λ. El prefijo del archivo (`L2-` o `L3-`) indica la lista.", "",
            "El criterio de clasificación es la forma del autómata que resuelve el ejercicio: **AFD** si el "
            "enunciado pide o da un autómata con δ total y un solo estado activo; **AFND** si hay celdas con varios "
            "destinos o con ∅ y no hay λ; **AFND-λ** si la solución usa transiciones que no consumen símbolos. Los "
            "ejercicios de expresiones regulares (201-253) caen en AFND-λ porque la manera de simular una expresión "
            "es su autómata de Thompson. El problema 116 no cabe en ninguna: su lenguaje no es regular.", "",
            "| Lista | Problema | Sección | Justificación (una línea) |", "|---|---|---|---|"]
    for e in ejercicios:
        destino = doc_de.get((e.num, e.lista))
        enlace = f"[{e.num}](jflap/{destino}#{ancla_de(e)})" if destino else e.num
        p1 = " ★" if e.practica1 else ""
        out.append(f"| {e.lista} | {enlace}{p1} | {e.seccion} | {e.justificacion} |")
    out += ["", "★ = entregado en la Práctica 1 (se conservan sus `.jff`; aquí se agregan `.json`, `.xml`, pruebas y "
            "recorridos).", ""]

    # ------------------------------------------------------------------
    out += ["## 2.2 Diseño y validación", "",
            "En cada documento de sección, cada autómata trae:", "",
            "1. **Diseño y justificación**: qué recuerda cada estado (columna *Significado* de la tabla en los "
            "autómatas nuevos) y por qué la construcción reconoce exactamente el lenguaje.",
            "2. **Cinco cadenas válidas y cinco inválidas** de longitudes crecientes: la más corta, y otras obtenidas "
            "caminando al azar por el AFD mínimo sin salir de los estados desde los que aún se puede aceptar (o "
            "rechazar). Para cada una se muestra lo esperado según el oráculo, lo que da el simulador y lo que da JFLAP.",
            "3. **Recorrido completo**: en un AFD, la sucesión de estados; en un AFND o AFND-λ, el conjunto de estados "
            "activos tras cada símbolo y el **árbol de cómputo** con cada camino: los que aceptan, los que mueren "
            "porque no hay transición y los que terminan fuera de F. Ahí se ven las bifurcaciones.",
            "4. **Captura de JFLAP** con la simulación paso a paso de una de las cadenas.", "",
            "Cuando no existen cinco cadenas de un tipo, se indica: por ejemplo, L(126) = ∅ no tiene ninguna válida, "
            "{ab, ba} (262) tiene dos, y L(127) = Σ* solo tiene inválidas con símbolos fuera de Σ.", ""]

    # ------------------------------------------------------------------
    lambdas = [(e, p) for e in ejercicios for p in e.piezas if cache[p.archivo].tiene_lambda]
    a196 = cache["L3-196"]
    out += ["## 2.3 Transiciones λ", "",
            "Una transición λ cambia de estado sin consumir símbolos. En los autómatas de esta práctica aparecen por "
            "tres motivos: (1) **unión**: desde un estado se elige, sin leer nada, cuál de varias alternativas "
            "seguir (108, uniones de Thompson); (2) **concatenación**: al terminar un bloque se pasa al siguiente "
            "(117, concatenaciones de Thompson); (3) **repetición**: en una estrella, regresar al inicio del bloque o "
            "saltarlo (Thompson). En los problemas 196-200 las λ vienen dadas en la tabla.", "",
            "La **λ-clausura** Cl(q) es el conjunto de estados alcanzables desde q con cero o más transiciones λ; se "
            "calcula con un recorrido en profundidad que agrega cada estado nuevo alcanzado por λ hasta que no hay "
            "cambios (`Automata.clausura`). Su papel en el reconocimiento es doble: el cómputo empieza en Cl(q₀) y no en "
            "{q₀}, y después de leer cada símbolo el conjunto alcanzado se vuelve a cerrar: "
            "δ̂(S, wa) = Cl(⋃_{q ∈ δ̂(S, w)} δ(q, a)). Una cadena se acepta si el conjunto final contiene un estado de "
            "F, aunque solo se llegue a él por λ.", "",
            "Ejemplo, problema 196 (tabla completa en [AFND-λ, parte 1](jflap/afnd-lambda-1.md)):", "",
            "| q | Cl(q) |", "|---|---|"]
    for q in a196.estados:
        out.append(f"| {q} | {mostrar_conjunto(a196.clausura(q))} |")
    traza = a196.traza("110")
    pasos = " → ".join(f"{mostrar_conjunto(p.despues)}" + (f" (lee {p.simbolo})" if p.indice else " (Cl(A))")
                       for p in traza)
    out += ["", f"δ̂(A, 110): {pasos}. Sin la clausura inicial, el 1 no tendría transición desde A (δ(A, 1) = ∅) y la "
            f"cadena moriría; con ella, B ∈ Cl(A) lee el 1 hacia C.", "",
            f"Hay {len(lambdas)} autómatas con transiciones λ. Para cada uno, su documento presenta la justificación "
            "de las λ y la tabla de λ-clausuras de **todos** sus estados:", "",
            "| Problema | Archivo | Estados | Transiciones λ | Estados con Cl(q) ≠ {q} |", "|---|---|---|---|---|"]
    for e, p in lambdas:
        a = cache[p.archivo]
        nl = sum(len(d) for (q, s), d in a.transiciones.items() if s == "")
        no_triv = sum(1 for q in a.estados if len(a.clausura(q)) > 1)
        destino = doc_de.get((e.num, e.lista))
        out.append(f"| [{e.num}](jflap/{destino}#{ancla_de(e)}) | `{p.archivo}` | {len(a.estados)} | {nl} | {no_triv} |")
    out.append("")

    # ------------------------------------------------------------------
    por = {f["archivo"]: f for f in comparacion}
    destacados = [por[a] for a in DESTACADOS if a in por]
    out += ["## 2.4 Conversiones y análisis comparativo", "",
            "### Casos destacados", "",
            "n = estados del AFND convertido (para un AFND-λ, el AFND ya sin λ y sin inaccesibles). «AFD de JFLAP» "
            "es el resultado de *Convert to DFA*, que no dibuja el conjunto vacío; «completo» lo incluye cuando hace "
            "falta para que δ sea total; «mínimo» es el AFD de Hopcroft.", "",
            "| Problema | Archivo | AFND-λ | n (AFND) | Trans. AFND | AFD de JFLAP | Trans. AFD | AFD completo | AFD mínimo | Cota 2ⁿ |",
            "|---|---|---|---|---|---|---|---|---|---|"]
    for f in destacados:
        out.append(f"| {f['ejercicio']} | `{f['archivo']}` | {f['n_lambda'] or '—'} | {f['n']} | {f['t_afn']} | "
                   f"{f['afd']} | {f['t_afd']} | {f['completo']} | {f['minimo']} | {cota(f['n'])} |")
    proporcion = [f["completo"] / f["cota"] for f in comparacion]
    mayor = max(comparacion, key=lambda f: f["completo"] / f["cota"])
    menor_igual = sum(1 for f in comparacion if f["completo"] <= 2 * f["n"])
    out += ["", f"<details><summary>Las {len(comparacion)} conversiones</summary>", "",
            "| Problema | Archivo | n | AFD de JFLAP | AFD completo | AFD mínimo | 2ⁿ |", "|---|---|---|---|---|---|---|"]
    for f in comparacion:
        out.append(f"| {f['ejercicio']} | `{f['archivo']}` | {f['n']} | {f['afd']} | {f['completo']} | {f['minimo']} | {cota(f['n'])} |")
    out += ["", "</details>", "",
            "### Comparación", "",
            f"**Número de estados.** En las {len(comparacion)} conversiones, el AFD completo nunca pasó de "
            f"{max(f['completo'] for f in comparacion)} estados, mientras que la cota 2ⁿ llega a {cota(max(f['n'] for f in comparacion))}. "
            f"La proporción más alta entre estados obtenidos y cota fue {mayor['completo']}/{mayor['cota']} "
            f"(`{mayor['archivo']}`, un AFND de dos estados cuyo AFD usa los cuatro subconjuntos, incluido ∅), y en {menor_igual} de los {len(comparacion)} casos el AFD tuvo a lo sumo el doble de "
            "estados que el AFND. En los AFND de búsqueda de patrones (lazo inicial que «adivina» dónde empieza "
            "el patrón) el AFD tiene casi los mismos estados que el AFND: la construcción de subconjuntos reproduce "
            "la función de fallo del algoritmo KMP. En cambio, en los AFND-λ de Thompson el AFND de partida tiene "
            "muchos estados redundantes y el AFD mínimo es mucho menor.", "",
            "**Complejidad de las transiciones.** El AFND tiene menos transiciones pero cada celda es un conjunto; el "
            "AFD tiene exactamente |Q|·|Σ| transiciones (una por celda) y cada una es un solo estado. En los AFND-λ, "
            "además, una parte de las transiciones no consume símbolos y obliga a calcular clausuras.", "",
            "**Facilidad de diseño e interpretación.** El AFND y el AFND-λ son más fáciles de diseñar: se describen "
            "con la estructura del enunciado (un lazo que adivina, ramas para una unión, bloques concatenados por λ) "
            "y cada estado tiene un significado local. El AFD resultante es más difícil de leer: cada estado es un "
            "conjunto como {A, C, D}, cuyo significado es «el autómata podría estar en A, en C o en D». Esa es la "
            "razón por la que la lista pide AFN «más simples» en 162-188.", "",
            "**Eficiencia en el reconocimiento.** Un AFD procesa cada símbolo con una consulta a la tabla: tiempo "
            "O(|w|) y memoria constante. Simular un AFND sin convertirlo exige mantener el conjunto de estados activos: "
            "cada símbolo cuesta O(n²) en el peor caso (para cada estado activo, unir sus destinos) más el cálculo "
            "de clausuras en un AFND-λ. Convertir de antemano cuesta hasta O(2ⁿ·|Σ|·n) en tiempo y 2ⁿ estados en "
            "memoria, pero se paga una sola vez; conviene cuando el autómata se usa con muchas cadenas.", "",
            "### Por qué la cota 2ⁿ rara vez se alcanza", "",
            "La construcción de subconjuntos solo crea los subconjuntos **alcanzables** desde Cl(q₀), y en la mayoría "
            "de los autómatas muchos de los 2ⁿ subconjuntos no lo son: si q₀ tiene un lazo con todo Σ, q₀ está en "
            "todos los conjuntos alcanzables, lo que ya divide la cota entre dos; si el AFND es casi determinista, "
            "los conjuntos tienen uno o dos elementos; y si varios estados solo se alcanzan en un orden fijo (una "
            "cadena lineal), sus combinaciones posibles son pocas. Además, varios subconjuntos alcanzables pueden ser "
            "equivalentes y fundirse al minimizar. Hopcroft, Motwani y Ullman (2007, sección 2.3.5) observan que en "
            "la práctica el AFD suele tener aproximadamente tantos estados como el AFN, aunque el peor caso sea "
            "exponencial.", "",
            "### Una familia en la que sí se alcanza", "",
            "Hopcroft, Motwani y Ullman (2007, sección 2.3.6) presentan el «caso malo» de la construcción: "
            "Lₙ = {w ∈ {0,1}* : el n-ésimo símbolo desde el final es 1}. Su AFND tiene n + 1 estados (q₀ con lazo que "
            "adivina cuál 1 está a n posiciones del final, seguido de una cadena de n estados), y todo AFD que lo "
            "reconozca necesita al menos 2ⁿ estados, porque debe recordar los últimos n símbolos: dos cadenas que "
            "difieren en la posición i desde el final son distinguibles por la cadena 0ⁱ⁻¹. Se construyeron los "
            "AFND de L₁ a L₆ y se convirtieron con JFLAP:", "",
            "| n | Estados del AFND (n + 1) | AFD de JFLAP | AFD mínimo | 2ⁿ | Cota 2^(n+1) |", "|---|---|---|---|---|---|"]
    for n, n_afn, afd, minimo, cota_n1 in familia:
        out.append(f"| {n} | {n_afn} | {afd} | {minimo} | {2 ** n} | {cota_n1} |")
    out += ["", "El AFD mínimo tiene exactamente 2ⁿ estados para cada n (archivos `familia-L*` en "
            "[`automatas/conversiones/`](../automatas/conversiones/)): el crecimiento exponencial es inevitable, "
            "no un defecto de la construcción. Respecto de los n + 1 estados del AFND queda a un factor 2 de la cota. "
            "Moore (1971) dio una familia de AFND de n estados cuyo AFD mínimo tiene exactamente 2ⁿ estados, con lo "
            "que la cota de la construcción de subconjuntos es justa.", "",
            "Fuentes: Hopcroft, Motwani y Ullman (2007); Moore (1971); Rabin y Scott (1959). Ver "
            "[bibliografía](bibliografia.md).", ""]
    _ = proporcion
    return "\n".join(out)
