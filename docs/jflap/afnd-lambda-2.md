# Ejercicio 2 — AFND-λ (problemas 201-240)

[← Ejercicio 2](../02-jflap.md) · [Índice](../../README.md)

Cada autómata indica su clasificación, el diseño, la tabla de transiciones, cinco cadenas válidas y cinco inválidas con el resultado esperado (oráculo escrito a partir del enunciado), el del simulador de este proyecto y el del motor de JFLAP 7.1, el recorrido de cada cadena (en los no deterministas, el conjunto de estados activos y el árbol de caminos) y la captura de la simulación paso a paso en JFLAP.

<a id="problema-3-201-206-221"></a>

## Lista 3, problema 201, 206, 221

**Enunciado.** ¿Es verdadera la afirmación «w ∈ L(a+b)»? Afirmaciones 201, 206, 221.

**Clasificación: AFND-λ.** Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

| Afirmación | Cadena | Expresión | AFND-λ de Thompson | Respuesta | Razón |
|---|---|---|---|---|---|
| 201 | `a` | `a+b` | acepta | **V** | Se elige a en la unión. |
| 206 | `ab` | `a+b` | rechaza | **F** | Solo hay palabras de longitud 1. |
| 221 | `aa` | `a+b` | rechaza | **F** | Solo hay palabras de longitud 1. |

#### AFND-λ de Thompson de a+b — `L3-VF-201`

Archivos: [`L3-VF-201.jff`](../../automatas/lista3-afnd-lambda/L3-VF-201.jff) · [`L3-VF-201.json`](../../automatas/lista3-afnd-lambda/L3-VF-201.json) · [`L3-VF-201.xml`](../../automatas/lista3-afnd-lambda/L3-VF-201.xml). Tipo según la definición: **AFND-lambda**, |Q| = 6, Σ = {a, b, c}, 6 transiciones.

**Diseño.** Construcción de Thompson sobre Σ = {a, b, c}: cada símbolo es un fragmento i -a→ f; la unión y la estrella agregan un estado inicial y uno final unidos con λ, y la concatenación une fragmentos con λ.

| Estado | a | b | c | λ |
|---|---|---|---|---|
| →q0 | ∅ | ∅ | ∅ | {q1, q2} |
| q1 | {q3} | ∅ | ∅ | ∅ |
| q3 | ∅ | ∅ | ∅ | {q5} |
| q2 | ∅ | {q4} | ∅ | ∅ |
| q4 | ∅ | ∅ | ∅ | {q5} |
| *q5 | ∅ | ∅ | ∅ | ∅ |

**Transiciones λ.** Las λ son las de la construcción de Thompson: en la unión eligen una alternativa, en la estrella permiten repetir o saltar el fragmento y en la concatenación enlazan fragmentos.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0, q1, q2} | no |
| q1 | {q1} | no |
| q3 | {q3, q5} | sí |
| q2 | {q2} | no |
| q4 | {q4, q5} | sí |
| q5 | {q5} | sí |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `a` | acepta | acepta | acepta |
| 2 | `b` | acepta | acepta | acepta |
| 3 | λ | rechaza | rechaza | rechaza |
| 4 | `ab` | rechaza | rechaza | rechaza |
| 5 | `aaba` | rechaza | rechaza | rechaza |
| 6 | `abcacca` | rechaza | rechaza | rechaza |
| 7 | `bbbbbabccaa` | rechaza | rechaza | rechaza |

Nota sobre los casos: el lenguaje solo tiene 2 palabras.

<details><summary>Recorrido completo de cada cadena</summary>

1. `a`: {q0, q1, q2} -a→ {q3, q5} — ✔
  Árbol de cómputo: 3 caminos, 1 de aceptación:
    - q0 -λ→ q1 -a→ q3 -λ→ q5 — ✔ acepta
    - q0 -λ→ q1 -a→ q3 — ✘ termina fuera de F
    - q0 -λ→ q2 — ✘ muere tras leer λ
2. `b`: {q0, q1, q2} -b→ {q4, q5} — ✔
  Árbol de cómputo: 3 caminos, 1 de aceptación:
    - q0 -λ→ q2 -b→ q4 -λ→ q5 — ✔ acepta
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 -b→ q4 — ✘ termina fuera de F
3. λ: {q0, q1, q2} — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
    - q0 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q2 — ✘ termina fuera de F
4. `ab`: {q0, q1, q2} -a→ {q3, q5} -b→ ∅ — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -λ→ q1 -a→ q3 -λ→ q5 — ✘ muere tras leer `a`
    - q0 -λ→ q2 — ✘ muere tras leer λ
5. `aaba`: {q0, q1, q2} -a→ {q3, q5} -a→ ∅ -b→ ∅ -a→ ∅ — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -λ→ q1 -a→ q3 -λ→ q5 — ✘ muere tras leer `a`
    - q0 -λ→ q2 — ✘ muere tras leer λ
6. `abcacca`: {q0, q1, q2} -a→ {q3, q5} -b→ ∅ -c→ ∅ -a→ ∅ -c→ ∅ -c→ ∅ -a→ ∅ — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -λ→ q1 -a→ q3 -λ→ q5 — ✘ muere tras leer `a`
    - q0 -λ→ q2 — ✘ muere tras leer λ
7. `bbbbbabccaa`: {q0, q1, q2} -b→ {q4, q5} -b→ ∅ -b→ ∅ -b→ ∅ -b→ ∅ -a→ ∅ -b→ ∅ -c→ ∅ -c→ ∅ -a→ ∅ -a→ ∅ — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 -b→ q4 -λ→ q5 — ✘ muere tras leer `b`

</details>

Simulación paso a paso en JFLAP con `a`: [ver captura](../../evidencias/jflap/pasos/L3-VF-201.png).

**Conversión.** AFND-λ (6 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 4 estados, [`L3-VF-201-AFND.jff`](../../automatas/conversiones/L3-VF-201-AFND.jff). AFND (4 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 3 estados, [`L3-VF-201-AFD.jff`](../../automatas/conversiones/L3-VF-201-AFD.jff) ([.json](../../automatas/conversiones/L3-VF-201-AFD.json), [.xml](../../automatas/conversiones/L3-VF-201-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 4 estados, y el AFD mínimo (Hopcroft), 3. La cota es 2^4 = 16. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-202-207"></a>

## Lista 3, problema 202, 207

**Enunciado.** ¿Es verdadera la afirmación «w ∈ L(ab)»? Afirmaciones 202, 207.

**Clasificación: AFND-λ.** Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

| Afirmación | Cadena | Expresión | AFND-λ de Thompson | Respuesta | Razón |
|---|---|---|---|---|---|
| 202 | `a` | `ab` | rechaza | **F** | L(ab) = {ab}. |
| 207 | `ab` | `ab` | acepta | **V** | Es la propia palabra. |

#### AFND-λ de Thompson de ab — `L3-VF-202`

Archivos: [`L3-VF-202.jff`](../../automatas/lista3-afnd-lambda/L3-VF-202.jff) · [`L3-VF-202.json`](../../automatas/lista3-afnd-lambda/L3-VF-202.json) · [`L3-VF-202.xml`](../../automatas/lista3-afnd-lambda/L3-VF-202.xml). Tipo según la definición: **AFND-lambda**, |Q| = 4, Σ = {a, b, c}, 3 transiciones.

**Diseño.** Construcción de Thompson sobre Σ = {a, b, c}: cada símbolo es un fragmento i -a→ f; la unión y la estrella agregan un estado inicial y uno final unidos con λ, y la concatenación une fragmentos con λ.

| Estado | a | b | c | λ |
|---|---|---|---|---|
| →q0 | {q1} | ∅ | ∅ | ∅ |
| q1 | ∅ | ∅ | ∅ | {q2} |
| q2 | ∅ | {q3} | ∅ | ∅ |
| *q3 | ∅ | ∅ | ∅ | ∅ |

**Transiciones λ.** Las λ son las de la construcción de Thompson: en la unión eligen una alternativa, en la estrella permiten repetir o saltar el fragmento y en la concatenación enlazan fragmentos.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0} | no |
| q1 | {q1, q2} | no |
| q2 | {q2} | no |
| q3 | {q3} | sí |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `ab` | acepta | acepta | acepta |
| 2 | λ | rechaza | rechaza | rechaza |
| 3 | `cc` | rechaza | rechaza | rechaza |
| 4 | `ccab` | rechaza | rechaza | rechaza |
| 5 | `babcccc` | rechaza | rechaza | rechaza |
| 6 | `aacaaccabcc` | rechaza | rechaza | rechaza |

Nota sobre los casos: el lenguaje solo tiene 1 palabra.

<details><summary>Recorrido completo de cada cadena</summary>

1. `ab`: {q0} -a→ {q1, q2} -b→ {q3} — ✔
  Árbol de cómputo: 1 caminos, 1 de aceptación:
    - q0 -a→ q1 -λ→ q2 -b→ q3 — ✔ acepta
2. λ: {q0} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
3. `cc`: {q0} -c→ ∅ -c→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ
4. `ccab`: {q0} -c→ ∅ -c→ ∅ -a→ ∅ -b→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ
5. `babcccc`: {q0} -b→ ∅ -a→ ∅ -b→ ∅ -c→ ∅ -c→ ∅ -c→ ∅ -c→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ
6. `aacaaccabcc`: {q0} -a→ {q1, q2} -a→ ∅ -c→ ∅ -a→ ∅ -a→ ∅ -c→ ∅ -c→ ∅ -a→ ∅ -b→ ∅ -c→ ∅ -c→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 -a→ q1 -λ→ q2 — ✘ muere tras leer `a`

</details>

Simulación paso a paso en JFLAP con `ab`: [ver captura](../../evidencias/jflap/pasos/L3-VF-202.png).

**Conversión.** AFND-λ (4 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 4 estados, [`L3-VF-202-AFND.jff`](../../automatas/conversiones/L3-VF-202-AFND.jff). AFND (4 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 3 estados, [`L3-VF-202-AFD.jff`](../../automatas/conversiones/L3-VF-202-AFD.jff) ([.json](../../automatas/conversiones/L3-VF-202-AFD.json), [.xml](../../automatas/conversiones/L3-VF-202-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 4 estados, y el AFD mínimo (Hopcroft), 4. La cota es 2^4 = 16. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-203-222"></a>

## Lista 3, problema 203, 222

**Enunciado.** ¿Es verdadera la afirmación «w ∈ L(a*+b*)»? Afirmaciones 203, 222.

**Clasificación: AFND-λ.** Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

| Afirmación | Cadena | Expresión | AFND-λ de Thompson | Respuesta | Razón |
|---|---|---|---|---|---|
| 203 | `a` | `a*+b*` | acepta | **V** | a ∈ L(a*). |
| 222 | `aa` | `a*+b*` | acepta | **V** | a² ∈ L(a*). |

#### AFND-λ de Thompson de a*+b* — `L3-VF-203`

Archivos: [`L3-VF-203.jff`](../../automatas/lista3-afnd-lambda/L3-VF-203.jff) · [`L3-VF-203.json`](../../automatas/lista3-afnd-lambda/L3-VF-203.json) · [`L3-VF-203.xml`](../../automatas/lista3-afnd-lambda/L3-VF-203.xml). Tipo según la definición: **AFND-lambda**, |Q| = 10, Σ = {a, b, c}, 14 transiciones.

**Diseño.** Construcción de Thompson sobre Σ = {a, b, c}: cada símbolo es un fragmento i -a→ f; la unión y la estrella agregan un estado inicial y uno final unidos con λ, y la concatenación une fragmentos con λ.

| Estado | a | b | c | λ |
|---|---|---|---|---|
| →q0 | ∅ | ∅ | ∅ | {q1, q2} |
| q1 | ∅ | ∅ | ∅ | {q3, q4} |
| q3 | {q7} | ∅ | ∅ | ∅ |
| q7 | ∅ | ∅ | ∅ | {q3, q4} |
| q4 | ∅ | ∅ | ∅ | {q8} |
| q2 | ∅ | ∅ | ∅ | {q5, q6} |
| q5 | ∅ | {q9} | ∅ | ∅ |
| q9 | ∅ | ∅ | ∅ | {q5, q6} |
| q6 | ∅ | ∅ | ∅ | {q8} |
| *q8 | ∅ | ∅ | ∅ | ∅ |

**Transiciones λ.** Las λ son las de la construcción de Thompson: en la unión eligen una alternativa, en la estrella permiten repetir o saltar el fragmento y en la concatenación enlazan fragmentos.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0, q1, q2, q3, q4, q5, q6, q8} | sí |
| q1 | {q1, q3, q4, q8} | sí |
| q3 | {q3} | no |
| q7 | {q3, q4, q7, q8} | sí |
| q4 | {q4, q8} | sí |
| q2 | {q2, q5, q6, q8} | sí |
| q5 | {q5} | no |
| q9 | {q5, q6, q8, q9} | sí |
| q6 | {q6, q8} | sí |
| q8 | {q8} | sí |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | acepta | acepta | acepta |
| 2 | `bb` | acepta | acepta | acepta |
| 3 | `aaaa` | acepta | acepta | acepta |
| 4 | `bbbbbbb` | acepta | acepta | acepta |
| 5 | `bbbbbbbbbbb` | acepta | acepta | acepta |
| 6 | `c` | rechaza | rechaza | rechaza |
| 7 | `bba` | rechaza | rechaza | rechaza |
| 8 | `caaa` | rechaza | rechaza | rechaza |
| 9 | `aacbacc` | rechaza | rechaza | rechaza |
| 10 | `baacbbacabb` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: {q0, q1, q2, q3, q4, q5, q6, q8} — ✔
  Árbol de cómputo: 9 caminos, 2 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 — ✔ acepta
    - q0 -λ→ q2 -λ→ q6 -λ→ q8 — ✔ acepta
    - q0 — ✘ termina fuera de F
    - q0 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 — ✘ termina fuera de F
2. `bb`: {q0, q1, q2, q3, q4, q5, q6, q8} -b→ {q5, q6, q8, q9} -b→ {q5, q6, q8, q9} — ✔
  Árbol de cómputo: 8 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q2 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q6 -λ→ q8 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q6 — ✘ termina fuera de F
3. `aaaa`: {q0, q1, q2, q3, q4, q5, q6, q8} -a→ {q3, q4, q7, q8} -a→ {q3, q4, q7, q8} -a→ {q3, q4, q7, q8} -a→ {q3, q4, q7, q8} — ✔
  Árbol de cómputo: 10 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -a→ q7 -λ→ q3 -a→ q7 -λ→ q3 -a→ q7 -λ→ q3 -a→ q7 -λ→ q4 -λ→ q8 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -a→ q7 -λ→ q3 -a→ q7 -λ→ q3 -a→ q7 -λ→ q3 -a→ q7 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -a→ q7 -λ→ q3 -a→ q7 -λ→ q3 -a→ q7 -λ→ q3 -a→ q7 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -a→ q7 -λ→ q3 -a→ q7 -λ→ q3 -a→ q7 -λ→ q3 -a→ q7 -λ→ q4 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -a→ q7 -λ→ q3 -a→ q7 -λ→ q3 -a→ q7 -λ→ q4 -λ→ q8 — ✘ muere tras leer `aaa`
    - q0 -λ→ q1 -λ→ q3 -a→ q7 -λ→ q3 -a→ q7 -λ→ q4 -λ→ q8 — ✘ muere tras leer `aa`
4. `bbbbbbb`: {q0, q1, q2, q3, q4, q5, q6, q8} -b→ {q5, q6, q8, q9} -b→ {q5, q6, q8, q9} -b→ {q5, q6, q8, q9} -b→ {q5, q6, q8, q9} -b→ {q5, q6, q8, q9} -b→ {q5, q6, q8, q9} -b→ {q5, q6, q8, q9} — ✔
  Árbol de cómputo: 13 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q2 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q6 -λ→ q8 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q6 — ✘ termina fuera de F
5. `bbbbbbbbbbb`: {q0, q1, q2, q3, q4, q5, q6, q8} -b→ {q5, q6, q8, q9} -b→ {q5, q6, q8, q9} -b→ {q5, q6, q8, q9} -b→ {q5, q6, q8, q9} -b→ {q5, q6, q8, q9} -b→ {q5, q6, q8, q9} -b→ {q5, q6, q8, q9} -b→ {q5, q6, q8, q9} -b→ {q5, q6, q8, q9} -b→ {q5, q6, q8, q9} -b→ {q5, q6, q8, q9} — ✔
  Árbol de cómputo: 17 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q2 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q6 -λ→ q8 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q6 — ✘ termina fuera de F
6. `c`: {q0, q1, q2, q3, q4, q5, q6, q8} -c→ ∅ — ✘
  Árbol de cómputo: 4 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q5 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q6 -λ→ q8 — ✘ muere tras leer λ
7. `bba`: {q0, q1, q2, q3, q4, q5, q6, q8} -b→ {q5, q6, q8, q9} -b→ {q5, q6, q8, q9} -a→ ∅ — ✘
  Árbol de cómputo: 6 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q5 — ✘ muere tras leer `bb`
    - q0 -λ→ q2 -λ→ q5 -b→ q9 -λ→ q5 -b→ q9 -λ→ q6 -λ→ q8 — ✘ muere tras leer `bb`
    - q0 -λ→ q2 -λ→ q5 -b→ q9 -λ→ q6 -λ→ q8 — ✘ muere tras leer `b`
    - q0 -λ→ q2 -λ→ q6 -λ→ q8 — ✘ muere tras leer λ
8. `caaa`: {q0, q1, q2, q3, q4, q5, q6, q8} -c→ ∅ -a→ ∅ -a→ ∅ -a→ ∅ — ✘
  Árbol de cómputo: 4 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q5 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q6 -λ→ q8 — ✘ muere tras leer λ
9. `aacbacc`: {q0, q1, q2, q3, q4, q5, q6, q8} -a→ {q3, q4, q7, q8} -a→ {q3, q4, q7, q8} -c→ ∅ -b→ ∅ -a→ ∅ -c→ ∅ -c→ ∅ — ✘
  Árbol de cómputo: 6 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q3 -a→ q7 -λ→ q3 -a→ q7 -λ→ q3 — ✘ muere tras leer `aa`
    - q0 -λ→ q1 -λ→ q3 -a→ q7 -λ→ q3 -a→ q7 -λ→ q4 -λ→ q8 — ✘ muere tras leer `aa`
    - q0 -λ→ q1 -λ→ q3 -a→ q7 -λ→ q4 -λ→ q8 — ✘ muere tras leer `a`
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q5 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q6 -λ→ q8 — ✘ muere tras leer λ
10. `baacbbacabb`: {q0, q1, q2, q3, q4, q5, q6, q8} -b→ {q5, q6, q8, q9} -a→ ∅ -a→ ∅ -c→ ∅ -b→ ∅ -b→ ∅ -a→ ∅ -c→ ∅ -a→ ∅ -b→ ∅ -b→ ∅ — ✘
  Árbol de cómputo: 5 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q5 -b→ q9 -λ→ q5 — ✘ muere tras leer `b`
    - q0 -λ→ q2 -λ→ q5 -b→ q9 -λ→ q6 -λ→ q8 — ✘ muere tras leer `b`
    - q0 -λ→ q2 -λ→ q6 -λ→ q8 — ✘ muere tras leer λ

</details>

Simulación paso a paso en JFLAP con `bb`: [ver captura](../../evidencias/jflap/pasos/L3-VF-203.png).

**Conversión.** AFND-λ (10 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 8 estados, [`L3-VF-203-AFND.jff`](../../automatas/conversiones/L3-VF-203-AFND.jff). AFND (8 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 3 estados, [`L3-VF-203-AFD.jff`](../../automatas/conversiones/L3-VF-203-AFD.jff) ([.json](../../automatas/conversiones/L3-VF-203-AFD.json), [.xml](../../automatas/conversiones/L3-VF-203-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 4 estados, y el AFD mínimo (Hopcroft), 4. La cota es 2^8 = 256. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-204-233"></a>

## Lista 3, problema 204, 233

**Enunciado.** ¿Es verdadera la afirmación «w ∈ L(ab*)»? Afirmaciones 204, 233.

**Clasificación: AFND-λ.** Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

| Afirmación | Cadena | Expresión | AFND-λ de Thompson | Respuesta | Razón |
|---|---|---|---|---|---|
| 204 | `a` | `ab*` | acepta | **V** | b⁰ = λ. |
| 233 | λ | `ab*` | rechaza | **F** | Toda palabra empieza con a. |

#### AFND-λ de Thompson de ab* — `L3-VF-204`

Archivos: [`L3-VF-204.jff`](../../automatas/lista3-afnd-lambda/L3-VF-204.jff) · [`L3-VF-204.json`](../../automatas/lista3-afnd-lambda/L3-VF-204.json) · [`L3-VF-204.xml`](../../automatas/lista3-afnd-lambda/L3-VF-204.xml). Tipo según la definición: **AFND-lambda**, |Q| = 6, Σ = {a, b, c}, 7 transiciones.

**Diseño.** Construcción de Thompson sobre Σ = {a, b, c}: cada símbolo es un fragmento i -a→ f; la unión y la estrella agregan un estado inicial y uno final unidos con λ, y la concatenación une fragmentos con λ.

| Estado | a | b | c | λ |
|---|---|---|---|---|
| →q0 | {q1} | ∅ | ∅ | ∅ |
| q1 | ∅ | ∅ | ∅ | {q2} |
| q2 | ∅ | ∅ | ∅ | {q3, q4} |
| q3 | ∅ | {q5} | ∅ | ∅ |
| q5 | ∅ | ∅ | ∅ | {q3, q4} |
| *q4 | ∅ | ∅ | ∅ | ∅ |

**Transiciones λ.** Las λ son las de la construcción de Thompson: en la unión eligen una alternativa, en la estrella permiten repetir o saltar el fragmento y en la concatenación enlazan fragmentos.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0} | no |
| q1 | {q1, q2, q3, q4} | sí |
| q2 | {q2, q3, q4} | sí |
| q3 | {q3} | no |
| q5 | {q3, q4, q5} | sí |
| q4 | {q4} | sí |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `a` | acepta | acepta | acepta |
| 2 | `ab` | acepta | acepta | acepta |
| 3 | `abbb` | acepta | acepta | acepta |
| 4 | `abbbbbb` | acepta | acepta | acepta |
| 5 | `abbbbbbbbbb` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `cb` | rechaza | rechaza | rechaza |
| 8 | `ccca` | rechaza | rechaza | rechaza |
| 9 | `cababbb` | rechaza | rechaza | rechaza |
| 10 | `acacbaabaac` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `a`: {q0} -a→ {q1, q2, q3, q4} — ✔
  Árbol de cómputo: 4 caminos, 1 de aceptación:
    - q0 -a→ q1 -λ→ q2 -λ→ q4 — ✔ acepta
    - q0 -a→ q1 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q3 — ✘ termina fuera de F
2. `ab`: {q0} -a→ {q1, q2, q3, q4} -b→ {q3, q4, q5} — ✔
  Árbol de cómputo: 4 caminos, 1 de aceptación:
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q4 — ✔ acepta
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q3 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q4 — ✘ muere tras leer `a`
3. `abbb`: {q0} -a→ {q1, q2, q3, q4} -b→ {q3, q4, q5} -b→ {q3, q4, q5} -b→ {q3, q4, q5} — ✔
  Árbol de cómputo: 6 caminos, 1 de aceptación:
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q4 — ✔ acepta
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q4 — ✘ muere tras leer `abb`
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q4 — ✘ muere tras leer `ab`
    - q0 -a→ q1 -λ→ q2 -λ→ q4 — ✘ muere tras leer `a`
4. `abbbbbb`: {q0} -a→ {q1, q2, q3, q4} -b→ {q3, q4, q5} -b→ {q3, q4, q5} -b→ {q3, q4, q5} -b→ {q3, q4, q5} -b→ {q3, q4, q5} -b→ {q3, q4, q5} — ✔
  Árbol de cómputo: 9 caminos, 1 de aceptación (se muestran 6):
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q4 — ✔ acepta
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q4 — ✘ muere tras leer `abbbbb`
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q4 — ✘ muere tras leer `abbbb`
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q4 — ✘ muere tras leer `abbb`
5. `abbbbbbbbbb`: {q0} -a→ {q1, q2, q3, q4} -b→ {q3, q4, q5} -b→ {q3, q4, q5} -b→ {q3, q4, q5} -b→ {q3, q4, q5} -b→ {q3, q4, q5} -b→ {q3, q4, q5} -b→ {q3, q4, q5} -b→ {q3, q4, q5} -b→ {q3, q4, q5} -b→ {q3, q4, q5} — ✔
  Árbol de cómputo: 13 caminos, 1 de aceptación (se muestran 6):
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q4 — ✔ acepta
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q4 — ✘ muere tras leer `abbbbbbbbb`
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q4 — ✘ muere tras leer `abbbbbbbb`
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q4 — ✘ muere tras leer `abbbbbbb`
6. λ: {q0} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
7. `cb`: {q0} -c→ ∅ -b→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ
8. `ccca`: {q0} -c→ ∅ -c→ ∅ -c→ ∅ -a→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ
9. `cababbb`: {q0} -c→ ∅ -a→ ∅ -b→ ∅ -a→ ∅ -b→ ∅ -b→ ∅ -b→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ
10. `acacbaabaac`: {q0} -a→ {q1, q2, q3, q4} -c→ ∅ -a→ ∅ -c→ ∅ -b→ ∅ -a→ ∅ -a→ ∅ -b→ ∅ -a→ ∅ -a→ ∅ -c→ ∅ — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -a→ q1 -λ→ q2 -λ→ q3 — ✘ muere tras leer `a`
    - q0 -a→ q1 -λ→ q2 -λ→ q4 — ✘ muere tras leer `a`

</details>

Simulación paso a paso en JFLAP con `ab`: [ver captura](../../evidencias/jflap/pasos/L3-VF-204.png).

**Conversión.** AFND-λ (6 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 6 estados, [`L3-VF-204-AFND.jff`](../../automatas/conversiones/L3-VF-204-AFND.jff). AFND (6 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 3 estados, [`L3-VF-204-AFD.jff`](../../automatas/conversiones/L3-VF-204-AFD.jff) ([.json](../../automatas/conversiones/L3-VF-204-AFD.json), [.xml](../../automatas/conversiones/L3-VF-204-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 4 estados, y el AFD mínimo (Hopcroft), 3. La cota es 2^6 = 64. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-205"></a>

## Lista 3, problema 205

**Enunciado.** ¿Es verdadera la afirmación «w ∈ L(a*b)»? Afirmaciones 205.

**Clasificación: AFND-λ.** Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

| Afirmación | Cadena | Expresión | AFND-λ de Thompson | Respuesta | Razón |
|---|---|---|---|---|---|
| 205 | `a` | `a*b` | rechaza | **F** | Toda palabra termina en b. |

#### AFND-λ de Thompson de a*b — `L3-VF-205`

Archivos: [`L3-VF-205.jff`](../../automatas/lista3-afnd-lambda/L3-VF-205.jff) · [`L3-VF-205.json`](../../automatas/lista3-afnd-lambda/L3-VF-205.json) · [`L3-VF-205.xml`](../../automatas/lista3-afnd-lambda/L3-VF-205.xml). Tipo según la definición: **AFND-lambda**, |Q| = 6, Σ = {a, b, c}, 7 transiciones.

**Diseño.** Construcción de Thompson sobre Σ = {a, b, c}: cada símbolo es un fragmento i -a→ f; la unión y la estrella agregan un estado inicial y uno final unidos con λ, y la concatenación une fragmentos con λ.

| Estado | a | b | c | λ |
|---|---|---|---|---|
| →q0 | ∅ | ∅ | ∅ | {q1, q2} |
| q1 | {q3} | ∅ | ∅ | ∅ |
| q3 | ∅ | ∅ | ∅ | {q1, q2} |
| q2 | ∅ | ∅ | ∅ | {q4} |
| q4 | ∅ | {q5} | ∅ | ∅ |
| *q5 | ∅ | ∅ | ∅ | ∅ |

**Transiciones λ.** Las λ son las de la construcción de Thompson: en la unión eligen una alternativa, en la estrella permiten repetir o saltar el fragmento y en la concatenación enlazan fragmentos.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0, q1, q2, q4} | no |
| q1 | {q1} | no |
| q3 | {q1, q2, q3, q4} | no |
| q2 | {q2, q4} | no |
| q4 | {q4} | no |
| q5 | {q5} | sí |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `b` | acepta | acepta | acepta |
| 2 | `ab` | acepta | acepta | acepta |
| 3 | `aab` | acepta | acepta | acepta |
| 4 | `aaab` | acepta | acepta | acepta |
| 5 | `aaaaaaaaab` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `aba` | rechaza | rechaza | rechaza |
| 8 | `acbb` | rechaza | rechaza | rechaza |
| 9 | `babccba` | rechaza | rechaza | rechaza |
| 10 | `ccaacaabbac` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `b`: {q0, q1, q2, q4} -b→ {q5} — ✔
  Árbol de cómputo: 2 caminos, 1 de aceptación:
    - q0 -λ→ q2 -λ→ q4 -b→ q5 — ✔ acepta
    - q0 -λ→ q1 — ✘ muere tras leer λ
2. `ab`: {q0, q1, q2, q4} -a→ {q1, q2, q3, q4} -b→ {q5} — ✔
  Árbol de cómputo: 3 caminos, 1 de aceptación:
    - q0 -λ→ q1 -a→ q3 -λ→ q2 -λ→ q4 -b→ q5 — ✔ acepta
    - q0 -λ→ q1 -a→ q3 -λ→ q1 — ✘ muere tras leer `a`
    - q0 -λ→ q2 -λ→ q4 — ✘ muere tras leer λ
3. `aab`: {q0, q1, q2, q4} -a→ {q1, q2, q3, q4} -a→ {q1, q2, q3, q4} -b→ {q5} — ✔
  Árbol de cómputo: 4 caminos, 1 de aceptación:
    - q0 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q2 -λ→ q4 -b→ q5 — ✔ acepta
    - q0 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 — ✘ muere tras leer `aa`
    - q0 -λ→ q1 -a→ q3 -λ→ q2 -λ→ q4 — ✘ muere tras leer `a`
    - q0 -λ→ q2 -λ→ q4 — ✘ muere tras leer λ
4. `aaab`: {q0, q1, q2, q4} -a→ {q1, q2, q3, q4} -a→ {q1, q2, q3, q4} -a→ {q1, q2, q3, q4} -b→ {q5} — ✔
  Árbol de cómputo: 5 caminos, 1 de aceptación:
    - q0 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q2 -λ→ q4 -b→ q5 — ✔ acepta
    - q0 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 — ✘ muere tras leer `aaa`
    - q0 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q2 -λ→ q4 — ✘ muere tras leer `aa`
    - q0 -λ→ q1 -a→ q3 -λ→ q2 -λ→ q4 — ✘ muere tras leer `a`
    - q0 -λ→ q2 -λ→ q4 — ✘ muere tras leer λ
5. `aaaaaaaaab`: {q0, q1, q2, q4} -a→ {q1, q2, q3, q4} -a→ {q1, q2, q3, q4} -a→ {q1, q2, q3, q4} -a→ {q1, q2, q3, q4} -a→ {q1, q2, q3, q4} -a→ {q1, q2, q3, q4} -a→ {q1, q2, q3, q4} -a→ {q1, q2, q3, q4} -a→ {q1, q2, q3, q4} -b→ {q5} — ✔
  Árbol de cómputo: 11 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q2 -λ→ q4 -b→ q5 — ✔ acepta
    - q0 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 — ✘ muere tras leer `aaaaaaaaa`
    - q0 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q2 -λ→ q4 — ✘ muere tras leer `aaaaaaaa`
    - q0 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q2 -λ→ q4 — ✘ muere tras leer `aaaaaaa`
    - q0 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q2 -λ→ q4 — ✘ muere tras leer `aaaaaa`
    - q0 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q2 -λ→ q4 — ✘ muere tras leer `aaaaa`
6. λ: {q0, q1, q2, q4} — ✘
  Árbol de cómputo: 4 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
    - q0 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q2 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q4 — ✘ termina fuera de F
7. `aba`: {q0, q1, q2, q4} -a→ {q1, q2, q3, q4} -b→ {q5} -a→ ∅ — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - q0 -λ→ q1 -a→ q3 -λ→ q1 — ✘ muere tras leer `a`
    - q0 -λ→ q1 -a→ q3 -λ→ q2 -λ→ q4 -b→ q5 — ✘ muere tras leer `ab`
    - q0 -λ→ q2 -λ→ q4 — ✘ muere tras leer λ
8. `acbb`: {q0, q1, q2, q4} -a→ {q1, q2, q3, q4} -c→ ∅ -b→ ∅ -b→ ∅ — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - q0 -λ→ q1 -a→ q3 -λ→ q1 — ✘ muere tras leer `a`
    - q0 -λ→ q1 -a→ q3 -λ→ q2 -λ→ q4 — ✘ muere tras leer `a`
    - q0 -λ→ q2 -λ→ q4 — ✘ muere tras leer λ
9. `babccba`: {q0, q1, q2, q4} -b→ {q5} -a→ ∅ -b→ ∅ -c→ ∅ -c→ ∅ -b→ ∅ -a→ ∅ — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q4 -b→ q5 — ✘ muere tras leer `b`
10. `ccaacaabbac`: {q0, q1, q2, q4} -c→ ∅ -c→ ∅ -a→ ∅ -a→ ∅ -c→ ∅ -a→ ∅ -a→ ∅ -b→ ∅ -b→ ∅ -a→ ∅ -c→ ∅ — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q4 — ✘ muere tras leer λ

</details>

Simulación paso a paso en JFLAP con `ab`: [ver captura](../../evidencias/jflap/pasos/L3-VF-205.png).

**Conversión.** AFND-λ (6 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 6 estados, [`L3-VF-205-AFND.jff`](../../automatas/conversiones/L3-VF-205-AFND.jff). AFND (6 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 3 estados, [`L3-VF-205-AFD.jff`](../../automatas/conversiones/L3-VF-205-AFD.jff) ([.json](../../automatas/conversiones/L3-VF-205-AFD.json), [.xml](../../automatas/conversiones/L3-VF-205-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 4 estados, y el AFD mínimo (Hopcroft), 3. La cota es 2^6 = 64. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-208"></a>

## Lista 3, problema 208

**Enunciado.** ¿Es verdadera la afirmación «w ∈ L(λa*b)»? Afirmaciones 208.

**Clasificación: AFND-λ.** Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

| Afirmación | Cadena | Expresión | AFND-λ de Thompson | Respuesta | Razón |
|---|---|---|---|---|---|
| 208 | `ab` | `λa*b` | acepta | **V** | λ es neutro y a¹b = ab. |

#### AFND-λ de Thompson de λa*b — `L3-VF-208`

Archivos: [`L3-VF-208.jff`](../../automatas/lista3-afnd-lambda/L3-VF-208.jff) · [`L3-VF-208.json`](../../automatas/lista3-afnd-lambda/L3-VF-208.json) · [`L3-VF-208.xml`](../../automatas/lista3-afnd-lambda/L3-VF-208.xml). Tipo según la definición: **AFND-lambda**, |Q| = 8, Σ = {a, b, c}, 9 transiciones.

**Diseño.** Construcción de Thompson sobre Σ = {a, b, c}: cada símbolo es un fragmento i -a→ f; la unión y la estrella agregan un estado inicial y uno final unidos con λ, y la concatenación une fragmentos con λ.

| Estado | a | b | c | λ |
|---|---|---|---|---|
| →q0 | ∅ | ∅ | ∅ | {q1} |
| q1 | ∅ | ∅ | ∅ | {q2} |
| q2 | ∅ | ∅ | ∅ | {q3, q4} |
| q3 | {q5} | ∅ | ∅ | ∅ |
| q5 | ∅ | ∅ | ∅ | {q3, q4} |
| q4 | ∅ | ∅ | ∅ | {q6} |
| q6 | ∅ | {q7} | ∅ | ∅ |
| *q7 | ∅ | ∅ | ∅ | ∅ |

**Transiciones λ.** Las λ son las de la construcción de Thompson: en la unión eligen una alternativa, en la estrella permiten repetir o saltar el fragmento y en la concatenación enlazan fragmentos.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0, q1, q2, q3, q4, q6} | no |
| q1 | {q1, q2, q3, q4, q6} | no |
| q2 | {q2, q3, q4, q6} | no |
| q3 | {q3} | no |
| q5 | {q3, q4, q5, q6} | no |
| q4 | {q4, q6} | no |
| q6 | {q6} | no |
| q7 | {q7} | sí |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `b` | acepta | acepta | acepta |
| 2 | `ab` | acepta | acepta | acepta |
| 3 | `aab` | acepta | acepta | acepta |
| 4 | `aaaaab` | acepta | acepta | acepta |
| 5 | `aaaaaab` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `aa` | rechaza | rechaza | rechaza |
| 8 | `acac` | rechaza | rechaza | rechaza |
| 9 | `ccacabb` | rechaza | rechaza | rechaza |
| 10 | `cbabaaabbcc` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `b`: {q0, q1, q2, q3, q4, q6} -b→ {q7} — ✔
  Árbol de cómputo: 2 caminos, 1 de aceptación:
    - q0 -λ→ q1 -λ→ q2 -λ→ q4 -λ→ q6 -b→ q7 — ✔ acepta
    - q0 -λ→ q1 -λ→ q2 -λ→ q3 — ✘ muere tras leer λ
2. `ab`: {q0, q1, q2, q3, q4, q6} -a→ {q3, q4, q5, q6} -b→ {q7} — ✔
  Árbol de cómputo: 3 caminos, 1 de aceptación:
    - q0 -λ→ q1 -λ→ q2 -λ→ q3 -a→ q5 -λ→ q4 -λ→ q6 -b→ q7 — ✔ acepta
    - q0 -λ→ q1 -λ→ q2 -λ→ q3 -a→ q5 -λ→ q3 — ✘ muere tras leer `a`
    - q0 -λ→ q1 -λ→ q2 -λ→ q4 -λ→ q6 — ✘ muere tras leer λ
3. `aab`: {q0, q1, q2, q3, q4, q6} -a→ {q3, q4, q5, q6} -a→ {q3, q4, q5, q6} -b→ {q7} — ✔
  Árbol de cómputo: 4 caminos, 1 de aceptación:
    - q0 -λ→ q1 -λ→ q2 -λ→ q3 -a→ q5 -λ→ q3 -a→ q5 -λ→ q4 -λ→ q6 -b→ q7 — ✔ acepta
    - q0 -λ→ q1 -λ→ q2 -λ→ q3 -a→ q5 -λ→ q3 -a→ q5 -λ→ q3 — ✘ muere tras leer `aa`
    - q0 -λ→ q1 -λ→ q2 -λ→ q3 -a→ q5 -λ→ q4 -λ→ q6 — ✘ muere tras leer `a`
    - q0 -λ→ q1 -λ→ q2 -λ→ q4 -λ→ q6 — ✘ muere tras leer λ
4. `aaaaab`: {q0, q1, q2, q3, q4, q6} -a→ {q3, q4, q5, q6} -a→ {q3, q4, q5, q6} -a→ {q3, q4, q5, q6} -a→ {q3, q4, q5, q6} -a→ {q3, q4, q5, q6} -b→ {q7} — ✔
  Árbol de cómputo: 7 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q2 -λ→ q3 -a→ q5 -λ→ q3 -a→ q5 -λ→ q3 -a→ q5 -λ→ q3 -a→ q5 -λ→ q3 -a→ q5 -λ→ q4 -λ→ q6 -b→ q7 — ✔ acepta
    - q0 -λ→ q1 -λ→ q2 -λ→ q3 -a→ q5 -λ→ q3 -a→ q5 -λ→ q3 -a→ q5 -λ→ q3 -a→ q5 -λ→ q3 -a→ q5 -λ→ q3 — ✘ muere tras leer `aaaaa`
    - q0 -λ→ q1 -λ→ q2 -λ→ q3 -a→ q5 -λ→ q3 -a→ q5 -λ→ q3 -a→ q5 -λ→ q3 -a→ q5 -λ→ q4 -λ→ q6 — ✘ muere tras leer `aaaa`
    - q0 -λ→ q1 -λ→ q2 -λ→ q3 -a→ q5 -λ→ q3 -a→ q5 -λ→ q3 -a→ q5 -λ→ q4 -λ→ q6 — ✘ muere tras leer `aaa`
    - q0 -λ→ q1 -λ→ q2 -λ→ q3 -a→ q5 -λ→ q3 -a→ q5 -λ→ q4 -λ→ q6 — ✘ muere tras leer `aa`
    - q0 -λ→ q1 -λ→ q2 -λ→ q3 -a→ q5 -λ→ q4 -λ→ q6 — ✘ muere tras leer `a`
5. `aaaaaab`: {q0, q1, q2, q3, q4, q6} -a→ {q3, q4, q5, q6} -a→ {q3, q4, q5, q6} -a→ {q3, q4, q5, q6} -a→ {q3, q4, q5, q6} -a→ {q3, q4, q5, q6} -a→ {q3, q4, q5, q6} -b→ {q7} — ✔
  Árbol de cómputo: 8 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q2 -λ→ q3 -a→ q5 -λ→ q3 -a→ q5 -λ→ q3 -a→ q5 -λ→ q3 -a→ q5 -λ→ q3 -a→ q5 -λ→ q3 -a→ q5 -λ→ q4 -λ→ q6 -b→ q7 — ✔ acepta
    - q0 -λ→ q1 -λ→ q2 -λ→ q3 -a→ q5 -λ→ q3 -a→ q5 -λ→ q3 -a→ q5 -λ→ q3 -a→ q5 -λ→ q3 -a→ q5 -λ→ q3 -a→ q5 -λ→ q3 — ✘ muere tras leer `aaaaaa`
    - q0 -λ→ q1 -λ→ q2 -λ→ q3 -a→ q5 -λ→ q3 -a→ q5 -λ→ q3 -a→ q5 -λ→ q3 -a→ q5 -λ→ q3 -a→ q5 -λ→ q4 -λ→ q6 — ✘ muere tras leer `aaaaa`
    - q0 -λ→ q1 -λ→ q2 -λ→ q3 -a→ q5 -λ→ q3 -a→ q5 -λ→ q3 -a→ q5 -λ→ q3 -a→ q5 -λ→ q4 -λ→ q6 — ✘ muere tras leer `aaaa`
    - q0 -λ→ q1 -λ→ q2 -λ→ q3 -a→ q5 -λ→ q3 -a→ q5 -λ→ q3 -a→ q5 -λ→ q4 -λ→ q6 — ✘ muere tras leer `aaa`
    - q0 -λ→ q1 -λ→ q2 -λ→ q3 -a→ q5 -λ→ q3 -a→ q5 -λ→ q4 -λ→ q6 — ✘ muere tras leer `aa`
6. λ: {q0, q1, q2, q3, q4, q6} — ✘
  Árbol de cómputo: 6 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
    - q0 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q2 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q2 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q2 -λ→ q4 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q2 -λ→ q4 -λ→ q6 — ✘ termina fuera de F
7. `aa`: {q0, q1, q2, q3, q4, q6} -a→ {q3, q4, q5, q6} -a→ {q3, q4, q5, q6} — ✘
  Árbol de cómputo: 6 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q2 -λ→ q3 -a→ q5 -λ→ q3 -a→ q5 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q2 -λ→ q3 -a→ q5 -λ→ q3 -a→ q5 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q2 -λ→ q3 -a→ q5 -λ→ q3 -a→ q5 -λ→ q4 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q2 -λ→ q3 -a→ q5 -λ→ q3 -a→ q5 -λ→ q4 -λ→ q6 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q2 -λ→ q3 -a→ q5 -λ→ q4 -λ→ q6 — ✘ muere tras leer `a`
    - q0 -λ→ q1 -λ→ q2 -λ→ q4 -λ→ q6 — ✘ muere tras leer λ
8. `acac`: {q0, q1, q2, q3, q4, q6} -a→ {q3, q4, q5, q6} -c→ ∅ -a→ ∅ -c→ ∅ — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q2 -λ→ q3 -a→ q5 -λ→ q3 — ✘ muere tras leer `a`
    - q0 -λ→ q1 -λ→ q2 -λ→ q3 -a→ q5 -λ→ q4 -λ→ q6 — ✘ muere tras leer `a`
    - q0 -λ→ q1 -λ→ q2 -λ→ q4 -λ→ q6 — ✘ muere tras leer λ
9. `ccacabb`: {q0, q1, q2, q3, q4, q6} -c→ ∅ -c→ ∅ -a→ ∅ -c→ ∅ -a→ ∅ -b→ ∅ -b→ ∅ — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q2 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q2 -λ→ q4 -λ→ q6 — ✘ muere tras leer λ
10. `cbabaaabbcc`: {q0, q1, q2, q3, q4, q6} -c→ ∅ -b→ ∅ -a→ ∅ -b→ ∅ -a→ ∅ -a→ ∅ -a→ ∅ -b→ ∅ -b→ ∅ -c→ ∅ -c→ ∅ — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q2 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q2 -λ→ q4 -λ→ q6 — ✘ muere tras leer λ

</details>

Simulación paso a paso en JFLAP con `ab`: [ver captura](../../evidencias/jflap/pasos/L3-VF-208.png).

**Conversión.** AFND-λ (8 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 6 estados, [`L3-VF-208-AFND.jff`](../../automatas/conversiones/L3-VF-208-AFND.jff). AFND (6 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 3 estados, [`L3-VF-208-AFD.jff`](../../automatas/conversiones/L3-VF-208-AFD.jff) ([.json](../../automatas/conversiones/L3-VF-208-AFD.json), [.xml](../../automatas/conversiones/L3-VF-208-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 4 estados, y el AFD mínimo (Hopcroft), 3. La cota es 2^6 = 64. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-209"></a>

## Lista 3, problema 209

**Enunciado.** ¿Es verdadera la afirmación «w ∈ L(∅a*b)»? Afirmaciones 209.

**Clasificación: AFND-λ.** Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

| Afirmación | Cadena | Expresión | AFND-λ de Thompson | Respuesta | Razón |
|---|---|---|---|---|---|
| 209 | `ab` | `∅a*b` | rechaza | **F** | ∅ es absorbente: el lenguaje es vacío. |

#### AFND-λ de Thompson de ∅a*b — `L3-VF-209`

Archivos: [`L3-VF-209.jff`](../../automatas/lista3-afnd-lambda/L3-VF-209.jff) · [`L3-VF-209.json`](../../automatas/lista3-afnd-lambda/L3-VF-209.json) · [`L3-VF-209.xml`](../../automatas/lista3-afnd-lambda/L3-VF-209.xml). Tipo según la definición: **AFND-lambda**, |Q| = 8, Σ = {a, b, c}, 8 transiciones.

**Diseño.** Construcción de Thompson sobre Σ = {a, b, c}: cada símbolo es un fragmento i -a→ f; la unión y la estrella agregan un estado inicial y uno final unidos con λ, y la concatenación une fragmentos con λ.

| Estado | a | b | c | λ |
|---|---|---|---|---|
| →q0 | ∅ | ∅ | ∅ | ∅ |
| q1 | ∅ | ∅ | ∅ | {q2} |
| q2 | ∅ | ∅ | ∅ | {q3, q5} |
| q3 | {q4} | ∅ | ∅ | ∅ |
| q4 | ∅ | ∅ | ∅ | {q3, q5} |
| q5 | ∅ | ∅ | ∅ | {q6} |
| q6 | ∅ | {q7} | ∅ | ∅ |
| *q7 | ∅ | ∅ | ∅ | ∅ |

**Transiciones λ.** Las λ son las de la construcción de Thompson: en la unión eligen una alternativa, en la estrella permiten repetir o saltar el fragmento y en la concatenación enlazan fragmentos.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0} | no |
| q1 | {q1, q2, q3, q5, q6} | no |
| q2 | {q2, q3, q5, q6} | no |
| q3 | {q3} | no |
| q4 | {q3, q4, q5, q6} | no |
| q5 | {q5, q6} | no |
| q6 | {q6} | no |
| q7 | {q7} | sí |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | rechaza | rechaza | rechaza |
| 2 | `cb` | rechaza | rechaza | rechaza |
| 3 | `cccb` | rechaza | rechaza | rechaza |
| 4 | `bbcabba` | rechaza | rechaza | rechaza |
| 5 | `cabcbbbbbcb` | rechaza | rechaza | rechaza |

Nota sobre los casos: el lenguaje solo tiene 0 palabras.

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: {q0} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
2. `cb`: {q0} -c→ ∅ -b→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ
3. `cccb`: {q0} -c→ ∅ -c→ ∅ -c→ ∅ -b→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ
4. `bbcabba`: {q0} -b→ ∅ -b→ ∅ -c→ ∅ -a→ ∅ -b→ ∅ -b→ ∅ -a→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ
5. `cabcbbbbbcb`: {q0} -c→ ∅ -a→ ∅ -b→ ∅ -c→ ∅ -b→ ∅ -b→ ∅ -b→ ∅ -b→ ∅ -b→ ∅ -c→ ∅ -b→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ

</details>

Simulación paso a paso en JFLAP con `cb`: [ver captura](../../evidencias/jflap/pasos/L3-VF-209.png).

**Conversión.** AFND-λ (8 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 1 estados, [`L3-VF-209-AFND.jff`](../../automatas/conversiones/L3-VF-209-AFND.jff). AFND (1 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 1 estados, [`L3-VF-209-AFD.jff`](../../automatas/conversiones/L3-VF-209-AFD.jff) ([.json](../../automatas/conversiones/L3-VF-209-AFD.json), [.xml](../../automatas/conversiones/L3-VF-209-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 2 estados, y el AFD mínimo (Hopcroft), 1. La cota es 2^1 = 2. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-210-224-227"></a>

## Lista 3, problema 210, 224, 227

**Enunciado.** ¿Es verdadera la afirmación «w ∈ L((a+b)*)»? Afirmaciones 210, 224, 227.

**Clasificación: AFND-λ.** Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

| Afirmación | Cadena | Expresión | AFND-λ de Thompson | Respuesta | Razón |
|---|---|---|---|---|---|
| 210 | `ab` | `(a+b)*` | acepta | **V** | Dos repeticiones: a y b. |
| 224 | `aa` | `(a+b)*` | acepta | **V** | Dos repeticiones de a. |
| 227 | λ | `(a+b)*` | acepta | **V** | Cero repeticiones. |

#### AFND-λ de Thompson de (a+b)* — `L3-VF-210`

Archivos: [`L3-VF-210.jff`](../../automatas/lista3-afnd-lambda/L3-VF-210.jff) · [`L3-VF-210.json`](../../automatas/lista3-afnd-lambda/L3-VF-210.json) · [`L3-VF-210.xml`](../../automatas/lista3-afnd-lambda/L3-VF-210.xml). Tipo según la definición: **AFND-lambda**, |Q| = 8, Σ = {a, b, c}, 10 transiciones.

**Diseño.** Construcción de Thompson sobre Σ = {a, b, c}: cada símbolo es un fragmento i -a→ f; la unión y la estrella agregan un estado inicial y uno final unidos con λ, y la concatenación une fragmentos con λ.

| Estado | a | b | c | λ |
|---|---|---|---|---|
| →q0 | ∅ | ∅ | ∅ | {q1, q2} |
| q1 | ∅ | ∅ | ∅ | {q3, q4} |
| q3 | {q5} | ∅ | ∅ | ∅ |
| q5 | ∅ | ∅ | ∅ | {q7} |
| q4 | ∅ | {q6} | ∅ | ∅ |
| q6 | ∅ | ∅ | ∅ | {q7} |
| q7 | ∅ | ∅ | ∅ | {q1, q2} |
| *q2 | ∅ | ∅ | ∅ | ∅ |

**Transiciones λ.** Las λ son las de la construcción de Thompson: en la unión eligen una alternativa, en la estrella permiten repetir o saltar el fragmento y en la concatenación enlazan fragmentos.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0, q1, q2, q3, q4} | sí |
| q1 | {q1, q3, q4} | no |
| q3 | {q3} | no |
| q5 | {q1, q2, q3, q4, q5, q7} | sí |
| q4 | {q4} | no |
| q6 | {q1, q2, q3, q4, q6, q7} | sí |
| q7 | {q1, q2, q3, q4, q7} | sí |
| q2 | {q2} | sí |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | acepta | acepta | acepta |
| 2 | `ba` | acepta | acepta | acepta |
| 3 | `bbab` | acepta | acepta | acepta |
| 4 | `aabaaaa` | acepta | acepta | acepta |
| 5 | `aabbbbaabaa` | acepta | acepta | acepta |
| 6 | `c` | rechaza | rechaza | rechaza |
| 7 | `ac` | rechaza | rechaza | rechaza |
| 8 | `bcba` | rechaza | rechaza | rechaza |
| 9 | `bbbaccc` | rechaza | rechaza | rechaza |
| 10 | `bccbaccccac` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: {q0, q1, q2, q3, q4} — ✔
  Árbol de cómputo: 5 caminos, 1 de aceptación:
    - q0 -λ→ q2 — ✔ acepta
    - q0 — ✘ termina fuera de F
    - q0 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 — ✘ termina fuera de F
2. `ba`: {q0, q1, q2, q3, q4} -b→ {q1, q2, q3, q4, q6, q7} -a→ {q1, q2, q3, q4, q5, q7} — ✔
  Árbol de cómputo: 10 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q2 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q3 — ✘ termina fuera de F
3. `bbab`: {q0, q1, q2, q3, q4} -b→ {q1, q2, q3, q4, q6, q7} -b→ {q1, q2, q3, q4, q6, q7} -a→ {q1, q2, q3, q4, q5, q7} -b→ {q1, q2, q3, q4, q6, q7} — ✔
  Árbol de cómputo: 14 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q2 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q3 — ✘ muere tras leer `b`
    - q0 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q3 — ✘ muere tras leer `bba`
    - q0 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q4 -b→ q6 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 — ✘ termina fuera de F
4. `aabaaaa`: {q0, q1, q2, q3, q4} -a→ {q1, q2, q3, q4, q5, q7} -a→ {q1, q2, q3, q4, q5, q7} -b→ {q1, q2, q3, q4, q6, q7} -a→ {q1, q2, q3, q4, q5, q7} -a→ {q1, q2, q3, q4, q5, q7} -a→ {q1, q2, q3, q4, q5, q7} -a→ {q1, q2, q3, q4, q5, q7} — ✔
  Árbol de cómputo: 20 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q2 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q3 — ✘ muere tras leer `aa`
    - q0 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q3 — ✘ termina fuera de F
5. `aabbbbaabaa`: {q0, q1, q2, q3, q4} -a→ {q1, q2, q3, q4, q5, q7} -a→ {q1, q2, q3, q4, q5, q7} -b→ {q1, q2, q3, q4, q6, q7} -b→ {q1, q2, q3, q4, q6, q7} -b→ {q1, q2, q3, q4, q6, q7} -b→ {q1, q2, q3, q4, q6, q7} -a→ {q1, q2, q3, q4, q5, q7} -a→ {q1, q2, q3, q4, q5, q7} -b→ {q1, q2, q3, q4, q6, q7} -a→ {q1, q2, q3, q4, q5, q7} -a→ {q1, q2, q3, q4, q5, q7} — ✔
  Árbol de cómputo: 28 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q2 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q3 — ✘ muere tras leer `aa`
    - q0 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q3 — ✘ muere tras leer `aab`
    - q0 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q3 — ✘ muere tras leer `aabb`
    - q0 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q3 — ✘ muere tras leer `aabbb`
    - q0 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q3 — ✘ muere tras leer `aabbbbaa`
6. `c`: {q0, q1, q2, q3, q4} -c→ ∅ — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 — ✘ muere tras leer λ
    - q0 -λ→ q2 — ✘ muere tras leer λ
7. `ac`: {q0, q1, q2, q3, q4} -a→ {q1, q2, q3, q4, q5, q7} -c→ ∅ — ✘
  Árbol de cómputo: 5 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q3 — ✘ muere tras leer `a`
    - q0 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q4 — ✘ muere tras leer `a`
    - q0 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q2 — ✘ muere tras leer `a`
    - q0 -λ→ q1 -λ→ q4 — ✘ muere tras leer λ
    - q0 -λ→ q2 — ✘ muere tras leer λ
8. `bcba`: {q0, q1, q2, q3, q4} -b→ {q1, q2, q3, q4, q6, q7} -c→ ∅ -b→ ∅ -a→ ∅ — ✘
  Árbol de cómputo: 5 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q3 — ✘ muere tras leer `b`
    - q0 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q4 — ✘ muere tras leer `b`
    - q0 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q2 — ✘ muere tras leer `b`
    - q0 -λ→ q2 — ✘ muere tras leer λ
9. `bbbaccc`: {q0, q1, q2, q3, q4} -b→ {q1, q2, q3, q4, q6, q7} -b→ {q1, q2, q3, q4, q6, q7} -b→ {q1, q2, q3, q4, q6, q7} -a→ {q1, q2, q3, q4, q5, q7} -c→ ∅ -c→ ∅ -c→ ∅ — ✘
  Árbol de cómputo: 11 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q3 — ✘ muere tras leer `b`
    - q0 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q3 — ✘ muere tras leer `bb`
    - q0 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q3 — ✘ muere tras leer `bbba`
    - q0 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q1 -λ→ q4 — ✘ muere tras leer `bbba`
    - q0 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -a→ q5 -λ→ q7 -λ→ q2 — ✘ muere tras leer `bbba`
10. `bccbaccccac`: {q0, q1, q2, q3, q4} -b→ {q1, q2, q3, q4, q6, q7} -c→ ∅ -c→ ∅ -b→ ∅ -a→ ∅ -c→ ∅ -c→ ∅ -c→ ∅ -c→ ∅ -a→ ∅ -c→ ∅ — ✘
  Árbol de cómputo: 5 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q3 — ✘ muere tras leer `b`
    - q0 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q1 -λ→ q4 — ✘ muere tras leer `b`
    - q0 -λ→ q1 -λ→ q4 -b→ q6 -λ→ q7 -λ→ q2 — ✘ muere tras leer `b`
    - q0 -λ→ q2 — ✘ muere tras leer λ

</details>

Simulación paso a paso en JFLAP con `ba`: [ver captura](../../evidencias/jflap/pasos/L3-VF-210.png).

**Conversión.** AFND-λ (8 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 8 estados, [`L3-VF-210-AFND.jff`](../../automatas/conversiones/L3-VF-210-AFND.jff). AFND (8 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 3 estados, [`L3-VF-210-AFD.jff`](../../automatas/conversiones/L3-VF-210-AFD.jff) ([.json](../../automatas/conversiones/L3-VF-210-AFD.json), [.xml](../../automatas/conversiones/L3-VF-210-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 4 estados, y el AFD mínimo (Hopcroft), 2. La cota es 2^8 = 256. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-211"></a>

## Lista 3, problema 211

**Enunciado.** ¿Es verdadera la afirmación «w ∈ L(abc*)»? Afirmaciones 211.

**Clasificación: AFND-λ.** Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

| Afirmación | Cadena | Expresión | AFND-λ de Thompson | Respuesta | Razón |
|---|---|---|---|---|---|
| 211 | `ab` | `abc*` | acepta | **V** | c⁰ = λ. |

#### AFND-λ de Thompson de abc* — `L3-VF-211`

Archivos: [`L3-VF-211.jff`](../../automatas/lista3-afnd-lambda/L3-VF-211.jff) · [`L3-VF-211.json`](../../automatas/lista3-afnd-lambda/L3-VF-211.json) · [`L3-VF-211.xml`](../../automatas/lista3-afnd-lambda/L3-VF-211.xml). Tipo según la definición: **AFND-lambda**, |Q| = 8, Σ = {a, b, c}, 9 transiciones.

**Diseño.** Construcción de Thompson sobre Σ = {a, b, c}: cada símbolo es un fragmento i -a→ f; la unión y la estrella agregan un estado inicial y uno final unidos con λ, y la concatenación une fragmentos con λ.

| Estado | a | b | c | λ |
|---|---|---|---|---|
| →q0 | {q1} | ∅ | ∅ | ∅ |
| q1 | ∅ | ∅ | ∅ | {q2} |
| q2 | ∅ | {q3} | ∅ | ∅ |
| q3 | ∅ | ∅ | ∅ | {q4} |
| q4 | ∅ | ∅ | ∅ | {q5, q6} |
| q5 | ∅ | ∅ | {q7} | ∅ |
| q7 | ∅ | ∅ | ∅ | {q5, q6} |
| *q6 | ∅ | ∅ | ∅ | ∅ |

**Transiciones λ.** Las λ son las de la construcción de Thompson: en la unión eligen una alternativa, en la estrella permiten repetir o saltar el fragmento y en la concatenación enlazan fragmentos.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0} | no |
| q1 | {q1, q2} | no |
| q2 | {q2} | no |
| q3 | {q3, q4, q5, q6} | sí |
| q4 | {q4, q5, q6} | sí |
| q5 | {q5} | no |
| q7 | {q5, q6, q7} | sí |
| q6 | {q6} | sí |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `ab` | acepta | acepta | acepta |
| 2 | `abcc` | acepta | acepta | acepta |
| 3 | `abccccc` | acepta | acepta | acepta |
| 4 | `abccccccccc` | acepta | acepta | acepta |
| 5 | `abcccccccccccccc` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `ac` | rechaza | rechaza | rechaza |
| 8 | `abcca` | rechaza | rechaza | rechaza |
| 9 | `bacccaa` | rechaza | rechaza | rechaza |
| 10 | `aabbacbccac` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `ab`: {q0} -a→ {q1, q2} -b→ {q3, q4, q5, q6} — ✔
  Árbol de cómputo: 4 caminos, 1 de aceptación:
    - q0 -a→ q1 -λ→ q2 -b→ q3 -λ→ q4 -λ→ q6 — ✔ acepta
    - q0 -a→ q1 -λ→ q2 -b→ q3 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -b→ q3 -λ→ q4 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -b→ q3 -λ→ q4 -λ→ q5 — ✘ termina fuera de F
2. `abcc`: {q0} -a→ {q1, q2} -b→ {q3, q4, q5, q6} -c→ {q5, q6, q7} -c→ {q5, q6, q7} — ✔
  Árbol de cómputo: 5 caminos, 1 de aceptación:
    - q0 -a→ q1 -λ→ q2 -b→ q3 -λ→ q4 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q6 — ✔ acepta
    - q0 -a→ q1 -λ→ q2 -b→ q3 -λ→ q4 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -b→ q3 -λ→ q4 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -b→ q3 -λ→ q4 -λ→ q5 -c→ q7 -λ→ q6 — ✘ muere tras leer `abc`
    - q0 -a→ q1 -λ→ q2 -b→ q3 -λ→ q4 -λ→ q6 — ✘ muere tras leer `ab`
3. `abccccc`: {q0} -a→ {q1, q2} -b→ {q3, q4, q5, q6} -c→ {q5, q6, q7} -c→ {q5, q6, q7} -c→ {q5, q6, q7} -c→ {q5, q6, q7} -c→ {q5, q6, q7} — ✔
  Árbol de cómputo: 8 caminos, 1 de aceptación (se muestran 6):
    - q0 -a→ q1 -λ→ q2 -b→ q3 -λ→ q4 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q6 — ✔ acepta
    - q0 -a→ q1 -λ→ q2 -b→ q3 -λ→ q4 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -b→ q3 -λ→ q4 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -b→ q3 -λ→ q4 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q6 — ✘ muere tras leer `abcccc`
    - q0 -a→ q1 -λ→ q2 -b→ q3 -λ→ q4 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q6 — ✘ muere tras leer `abccc`
    - q0 -a→ q1 -λ→ q2 -b→ q3 -λ→ q4 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q6 — ✘ muere tras leer `abcc`
4. `abccccccccc`: {q0} -a→ {q1, q2} -b→ {q3, q4, q5, q6} -c→ {q5, q6, q7} -c→ {q5, q6, q7} -c→ {q5, q6, q7} -c→ {q5, q6, q7} -c→ {q5, q6, q7} -c→ {q5, q6, q7} -c→ {q5, q6, q7} -c→ {q5, q6, q7} -c→ {q5, q6, q7} — ✔
  Árbol de cómputo: 12 caminos, 1 de aceptación (se muestran 6):
    - q0 -a→ q1 -λ→ q2 -b→ q3 -λ→ q4 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q6 — ✔ acepta
    - q0 -a→ q1 -λ→ q2 -b→ q3 -λ→ q4 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -b→ q3 -λ→ q4 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -b→ q3 -λ→ q4 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q6 — ✘ muere tras leer `abcccccccc`
    - q0 -a→ q1 -λ→ q2 -b→ q3 -λ→ q4 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q6 — ✘ muere tras leer `abccccccc`
    - q0 -a→ q1 -λ→ q2 -b→ q3 -λ→ q4 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q6 — ✘ muere tras leer `abcccccc`
5. `abcccccccccccccc`: {q0} -a→ {q1, q2} -b→ {q3, q4, q5, q6} -c→ {q5, q6, q7} -c→ {q5, q6, q7} -c→ {q5, q6, q7} -c→ {q5, q6, q7} -c→ {q5, q6, q7} -c→ {q5, q6, q7} -c→ {q5, q6, q7} -c→ {q5, q6, q7} -c→ {q5, q6, q7} -c→ {q5, q6, q7} -c→ {q5, q6, q7} -c→ {q5, q6, q7} -c→ {q5, q6, q7} -c→ {q5, q6, q7} — ✔
  Árbol de cómputo: 17 caminos, 1 de aceptación (se muestran 6):
    - q0 -a→ q1 -λ→ q2 -b→ q3 -λ→ q4 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q6 — ✔ acepta
    - q0 -a→ q1 -λ→ q2 -b→ q3 -λ→ q4 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -b→ q3 -λ→ q4 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -b→ q3 -λ→ q4 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q6 — ✘ muere tras leer `abccccccccccccc`
    - q0 -a→ q1 -λ→ q2 -b→ q3 -λ→ q4 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q6 — ✘ muere tras leer `abcccccccccccc`
    - q0 -a→ q1 -λ→ q2 -b→ q3 -λ→ q4 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q6 — ✘ muere tras leer `abccccccccccc`
6. λ: {q0} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
7. `ac`: {q0} -a→ {q1, q2} -c→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 -a→ q1 -λ→ q2 — ✘ muere tras leer `a`
8. `abcca`: {q0} -a→ {q1, q2} -b→ {q3, q4, q5, q6} -c→ {q5, q6, q7} -c→ {q5, q6, q7} -a→ ∅ — ✘
  Árbol de cómputo: 4 caminos, 0 de aceptación:
    - q0 -a→ q1 -λ→ q2 -b→ q3 -λ→ q4 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q5 — ✘ muere tras leer `abcc`
    - q0 -a→ q1 -λ→ q2 -b→ q3 -λ→ q4 -λ→ q5 -c→ q7 -λ→ q5 -c→ q7 -λ→ q6 — ✘ muere tras leer `abcc`
    - q0 -a→ q1 -λ→ q2 -b→ q3 -λ→ q4 -λ→ q5 -c→ q7 -λ→ q6 — ✘ muere tras leer `abc`
    - q0 -a→ q1 -λ→ q2 -b→ q3 -λ→ q4 -λ→ q6 — ✘ muere tras leer `ab`
9. `bacccaa`: {q0} -b→ ∅ -a→ ∅ -c→ ∅ -c→ ∅ -c→ ∅ -a→ ∅ -a→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ
10. `aabbacbccac`: {q0} -a→ {q1, q2} -a→ ∅ -b→ ∅ -b→ ∅ -a→ ∅ -c→ ∅ -b→ ∅ -c→ ∅ -c→ ∅ -a→ ∅ -c→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 -a→ q1 -λ→ q2 — ✘ muere tras leer `a`

</details>

Simulación paso a paso en JFLAP con `ab`: [ver captura](../../evidencias/jflap/pasos/L3-VF-211.png).

**Conversión.** AFND-λ (8 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 8 estados, [`L3-VF-211-AFND.jff`](../../automatas/conversiones/L3-VF-211-AFND.jff). AFND (8 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 4 estados, [`L3-VF-211-AFD.jff`](../../automatas/conversiones/L3-VF-211-AFD.jff) ([.json](../../automatas/conversiones/L3-VF-211-AFD.json), [.xml](../../automatas/conversiones/L3-VF-211-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 5 estados, y el AFD mínimo (Hopcroft), 4. La cota es 2^8 = 256. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-212"></a>

## Lista 3, problema 212

**Enunciado.** ¿Es verdadera la afirmación «w ∈ L(ab*c)»? Afirmaciones 212.

**Clasificación: AFND-λ.** Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

| Afirmación | Cadena | Expresión | AFND-λ de Thompson | Respuesta | Razón |
|---|---|---|---|---|---|
| 212 | `ab` | `ab*c` | rechaza | **F** | Toda palabra termina en c. |

#### AFND-λ de Thompson de ab*c — `L3-VF-212`

Archivos: [`L3-VF-212.jff`](../../automatas/lista3-afnd-lambda/L3-VF-212.jff) · [`L3-VF-212.json`](../../automatas/lista3-afnd-lambda/L3-VF-212.json) · [`L3-VF-212.xml`](../../automatas/lista3-afnd-lambda/L3-VF-212.xml). Tipo según la definición: **AFND-lambda**, |Q| = 8, Σ = {a, b, c}, 9 transiciones.

**Diseño.** Construcción de Thompson sobre Σ = {a, b, c}: cada símbolo es un fragmento i -a→ f; la unión y la estrella agregan un estado inicial y uno final unidos con λ, y la concatenación une fragmentos con λ.

| Estado | a | b | c | λ |
|---|---|---|---|---|
| →q0 | {q1} | ∅ | ∅ | ∅ |
| q1 | ∅ | ∅ | ∅ | {q2} |
| q2 | ∅ | ∅ | ∅ | {q3, q4} |
| q3 | ∅ | {q5} | ∅ | ∅ |
| q5 | ∅ | ∅ | ∅ | {q3, q4} |
| q4 | ∅ | ∅ | ∅ | {q6} |
| q6 | ∅ | ∅ | {q7} | ∅ |
| *q7 | ∅ | ∅ | ∅ | ∅ |

**Transiciones λ.** Las λ son las de la construcción de Thompson: en la unión eligen una alternativa, en la estrella permiten repetir o saltar el fragmento y en la concatenación enlazan fragmentos.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0} | no |
| q1 | {q1, q2, q3, q4, q6} | no |
| q2 | {q2, q3, q4, q6} | no |
| q3 | {q3} | no |
| q5 | {q3, q4, q5, q6} | no |
| q4 | {q4, q6} | no |
| q6 | {q6} | no |
| q7 | {q7} | sí |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `ac` | acepta | acepta | acepta |
| 2 | `abc` | acepta | acepta | acepta |
| 3 | `abbc` | acepta | acepta | acepta |
| 4 | `abbbc` | acepta | acepta | acepta |
| 5 | `abbbbc` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `bb` | rechaza | rechaza | rechaza |
| 8 | `ccba` | rechaza | rechaza | rechaza |
| 9 | `cbbccbb` | rechaza | rechaza | rechaza |
| 10 | `abccccbbbbb` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `ac`: {q0} -a→ {q1, q2, q3, q4, q6} -c→ {q7} — ✔
  Árbol de cómputo: 2 caminos, 1 de aceptación:
    - q0 -a→ q1 -λ→ q2 -λ→ q4 -λ→ q6 -c→ q7 — ✔ acepta
    - q0 -a→ q1 -λ→ q2 -λ→ q3 — ✘ muere tras leer `a`
2. `abc`: {q0} -a→ {q1, q2, q3, q4, q6} -b→ {q3, q4, q5, q6} -c→ {q7} — ✔
  Árbol de cómputo: 3 caminos, 1 de aceptación:
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q4 -λ→ q6 -c→ q7 — ✔ acepta
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q3 — ✘ muere tras leer `ab`
    - q0 -a→ q1 -λ→ q2 -λ→ q4 -λ→ q6 — ✘ muere tras leer `a`
3. `abbc`: {q0} -a→ {q1, q2, q3, q4, q6} -b→ {q3, q4, q5, q6} -b→ {q3, q4, q5, q6} -c→ {q7} — ✔
  Árbol de cómputo: 4 caminos, 1 de aceptación:
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q4 -λ→ q6 -c→ q7 — ✔ acepta
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 — ✘ muere tras leer `abb`
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q4 -λ→ q6 — ✘ muere tras leer `ab`
    - q0 -a→ q1 -λ→ q2 -λ→ q4 -λ→ q6 — ✘ muere tras leer `a`
4. `abbbc`: {q0} -a→ {q1, q2, q3, q4, q6} -b→ {q3, q4, q5, q6} -b→ {q3, q4, q5, q6} -b→ {q3, q4, q5, q6} -c→ {q7} — ✔
  Árbol de cómputo: 5 caminos, 1 de aceptación:
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q4 -λ→ q6 -c→ q7 — ✔ acepta
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 — ✘ muere tras leer `abbb`
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q4 -λ→ q6 — ✘ muere tras leer `abb`
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q4 -λ→ q6 — ✘ muere tras leer `ab`
    - q0 -a→ q1 -λ→ q2 -λ→ q4 -λ→ q6 — ✘ muere tras leer `a`
5. `abbbbc`: {q0} -a→ {q1, q2, q3, q4, q6} -b→ {q3, q4, q5, q6} -b→ {q3, q4, q5, q6} -b→ {q3, q4, q5, q6} -b→ {q3, q4, q5, q6} -c→ {q7} — ✔
  Árbol de cómputo: 6 caminos, 1 de aceptación:
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q4 -λ→ q6 -c→ q7 — ✔ acepta
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 — ✘ muere tras leer `abbbb`
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q4 -λ→ q6 — ✘ muere tras leer `abbb`
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q3 -b→ q5 -λ→ q4 -λ→ q6 — ✘ muere tras leer `abb`
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q4 -λ→ q6 — ✘ muere tras leer `ab`
    - q0 -a→ q1 -λ→ q2 -λ→ q4 -λ→ q6 — ✘ muere tras leer `a`
6. λ: {q0} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
7. `bb`: {q0} -b→ ∅ -b→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ
8. `ccba`: {q0} -c→ ∅ -c→ ∅ -b→ ∅ -a→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ
9. `cbbccbb`: {q0} -c→ ∅ -b→ ∅ -b→ ∅ -c→ ∅ -c→ ∅ -b→ ∅ -b→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ
10. `abccccbbbbb`: {q0} -a→ {q1, q2, q3, q4, q6} -b→ {q3, q4, q5, q6} -c→ {q7} -c→ ∅ -c→ ∅ -c→ ∅ -b→ ∅ -b→ ∅ -b→ ∅ -b→ ∅ -b→ ∅ — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q3 — ✘ muere tras leer `ab`
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q4 -λ→ q6 -c→ q7 — ✘ muere tras leer `abc`
    - q0 -a→ q1 -λ→ q2 -λ→ q4 -λ→ q6 — ✘ muere tras leer `a`

</details>

Simulación paso a paso en JFLAP con `ac`: [ver captura](../../evidencias/jflap/pasos/L3-VF-212.png).

**Conversión.** AFND-λ (8 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 8 estados, [`L3-VF-212-AFND.jff`](../../automatas/conversiones/L3-VF-212-AFND.jff). AFND (8 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 4 estados, [`L3-VF-212-AFD.jff`](../../automatas/conversiones/L3-VF-212-AFD.jff) ([.json](../../automatas/conversiones/L3-VF-212-AFD.json), [.xml](../../automatas/conversiones/L3-VF-212-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 5 estados, y el AFD mínimo (Hopcroft), 4. La cota es 2^8 = 256. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-213"></a>

## Lista 3, problema 213

**Enunciado.** ¿Es verdadera la afirmación «w ∈ L(ab*c*)»? Afirmaciones 213.

**Clasificación: AFND-λ.** Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

| Afirmación | Cadena | Expresión | AFND-λ de Thompson | Respuesta | Razón |
|---|---|---|---|---|---|
| 213 | `ab` | `ab*c*` | acepta | **V** | b¹ y c⁰. |

#### AFND-λ de Thompson de ab*c* — `L3-VF-213`

Archivos: [`L3-VF-213.jff`](../../automatas/lista3-afnd-lambda/L3-VF-213.jff) · [`L3-VF-213.json`](../../automatas/lista3-afnd-lambda/L3-VF-213.json) · [`L3-VF-213.xml`](../../automatas/lista3-afnd-lambda/L3-VF-213.xml). Tipo según la definición: **AFND-lambda**, |Q| = 10, Σ = {a, b, c}, 13 transiciones.

**Diseño.** Construcción de Thompson sobre Σ = {a, b, c}: cada símbolo es un fragmento i -a→ f; la unión y la estrella agregan un estado inicial y uno final unidos con λ, y la concatenación une fragmentos con λ.

| Estado | a | b | c | λ |
|---|---|---|---|---|
| →q0 | {q1} | ∅ | ∅ | ∅ |
| q1 | ∅ | ∅ | ∅ | {q2} |
| q2 | ∅ | ∅ | ∅ | {q3, q4} |
| q3 | ∅ | {q5} | ∅ | ∅ |
| q5 | ∅ | ∅ | ∅ | {q3, q4} |
| q4 | ∅ | ∅ | ∅ | {q6} |
| q6 | ∅ | ∅ | ∅ | {q7, q8} |
| q7 | ∅ | ∅ | {q9} | ∅ |
| q9 | ∅ | ∅ | ∅ | {q7, q8} |
| *q8 | ∅ | ∅ | ∅ | ∅ |

**Transiciones λ.** Las λ son las de la construcción de Thompson: en la unión eligen una alternativa, en la estrella permiten repetir o saltar el fragmento y en la concatenación enlazan fragmentos.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0} | no |
| q1 | {q1, q2, q3, q4, q6, q7, q8} | sí |
| q2 | {q2, q3, q4, q6, q7, q8} | sí |
| q3 | {q3} | no |
| q5 | {q3, q4, q5, q6, q7, q8} | sí |
| q4 | {q4, q6, q7, q8} | sí |
| q6 | {q6, q7, q8} | sí |
| q7 | {q7} | no |
| q9 | {q7, q8, q9} | sí |
| q8 | {q8} | sí |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `a` | acepta | acepta | acepta |
| 2 | `ac` | acepta | acepta | acepta |
| 3 | `accc` | acepta | acepta | acepta |
| 4 | `acccccc` | acepta | acepta | acepta |
| 5 | `abccccccccc` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `ca` | rechaza | rechaza | rechaza |
| 8 | `acca` | rechaza | rechaza | rechaza |
| 9 | `cacbcbb` | rechaza | rechaza | rechaza |
| 10 | `cbccabbcccc` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `a`: {q0} -a→ {q1, q2, q3, q4, q6, q7, q8} — ✔
  Árbol de cómputo: 7 caminos, 1 de aceptación (se muestran 6):
    - q0 -a→ q1 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q8 — ✔ acepta
    - q0 -a→ q1 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q3 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q4 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q4 -λ→ q6 — ✘ termina fuera de F
2. `ac`: {q0} -a→ {q1, q2, q3, q4, q6, q7, q8} -c→ {q7, q8, q9} — ✔
  Árbol de cómputo: 5 caminos, 1 de aceptación:
    - q0 -a→ q1 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q7 -c→ q9 -λ→ q8 — ✔ acepta
    - q0 -a→ q1 -λ→ q2 -λ→ q3 — ✘ muere tras leer `a`
    - q0 -a→ q1 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q7 -c→ q9 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q7 -c→ q9 -λ→ q7 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q8 — ✘ muere tras leer `a`
3. `accc`: {q0} -a→ {q1, q2, q3, q4, q6, q7, q8} -c→ {q7, q8, q9} -c→ {q7, q8, q9} -c→ {q7, q8, q9} — ✔
  Árbol de cómputo: 7 caminos, 1 de aceptación (se muestran 6):
    - q0 -a→ q1 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q8 — ✔ acepta
    - q0 -a→ q1 -λ→ q2 -λ→ q3 — ✘ muere tras leer `a`
    - q0 -a→ q1 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q8 — ✘ muere tras leer `acc`
    - q0 -a→ q1 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q7 -c→ q9 -λ→ q8 — ✘ muere tras leer `ac`
4. `acccccc`: {q0} -a→ {q1, q2, q3, q4, q6, q7, q8} -c→ {q7, q8, q9} -c→ {q7, q8, q9} -c→ {q7, q8, q9} -c→ {q7, q8, q9} -c→ {q7, q8, q9} -c→ {q7, q8, q9} — ✔
  Árbol de cómputo: 10 caminos, 1 de aceptación (se muestran 6):
    - q0 -a→ q1 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q8 — ✔ acepta
    - q0 -a→ q1 -λ→ q2 -λ→ q3 — ✘ muere tras leer `a`
    - q0 -a→ q1 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q8 — ✘ muere tras leer `accccc`
    - q0 -a→ q1 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q8 — ✘ muere tras leer `acccc`
5. `abccccccccc`: {q0} -a→ {q1, q2, q3, q4, q6, q7, q8} -b→ {q3, q4, q5, q6, q7, q8} -c→ {q7, q8, q9} -c→ {q7, q8, q9} -c→ {q7, q8, q9} -c→ {q7, q8, q9} -c→ {q7, q8, q9} -c→ {q7, q8, q9} -c→ {q7, q8, q9} -c→ {q7, q8, q9} -c→ {q7, q8, q9} — ✔
  Árbol de cómputo: 15 caminos, 1 de aceptación (se muestran 6):
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q4 -λ→ q6 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q8 — ✔ acepta
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q3 — ✘ muere tras leer `ab`
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q4 -λ→ q6 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q4 -λ→ q6 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q4 -λ→ q6 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q8 — ✘ muere tras leer `abcccccccc`
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q4 -λ→ q6 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q8 — ✘ muere tras leer `abccccccc`
6. λ: {q0} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
7. `ca`: {q0} -c→ ∅ -a→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ
8. `acca`: {q0} -a→ {q1, q2, q3, q4, q6, q7, q8} -c→ {q7, q8, q9} -c→ {q7, q8, q9} -a→ ∅ — ✘
  Árbol de cómputo: 5 caminos, 0 de aceptación:
    - q0 -a→ q1 -λ→ q2 -λ→ q3 — ✘ muere tras leer `a`
    - q0 -a→ q1 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q7 — ✘ muere tras leer `acc`
    - q0 -a→ q1 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q7 -c→ q9 -λ→ q7 -c→ q9 -λ→ q8 — ✘ muere tras leer `acc`
    - q0 -a→ q1 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q7 -c→ q9 -λ→ q8 — ✘ muere tras leer `ac`
    - q0 -a→ q1 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q8 — ✘ muere tras leer `a`
9. `cacbcbb`: {q0} -c→ ∅ -a→ ∅ -c→ ∅ -b→ ∅ -c→ ∅ -b→ ∅ -b→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ
10. `cbccabbcccc`: {q0} -c→ ∅ -b→ ∅ -c→ ∅ -c→ ∅ -a→ ∅ -b→ ∅ -b→ ∅ -c→ ∅ -c→ ∅ -c→ ∅ -c→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ

</details>

Simulación paso a paso en JFLAP con `ac`: [ver captura](../../evidencias/jflap/pasos/L3-VF-213.png).

**Conversión.** AFND-λ (10 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 10 estados, [`L3-VF-213-AFND.jff`](../../automatas/conversiones/L3-VF-213-AFND.jff). AFND (10 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 4 estados, [`L3-VF-213-AFD.jff`](../../automatas/conversiones/L3-VF-213-AFD.jff) ([.json](../../automatas/conversiones/L3-VF-213-AFD.json), [.xml](../../automatas/conversiones/L3-VF-213-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 5 estados, y el AFD mínimo (Hopcroft), 4. La cota es 2^10 = 1024. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-214"></a>

## Lista 3, problema 214

**Enunciado.** ¿Es verdadera la afirmación «w ∈ L((a+b+c)*)»? Afirmaciones 214.

**Clasificación: AFND-λ.** Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

| Afirmación | Cadena | Expresión | AFND-λ de Thompson | Respuesta | Razón |
|---|---|---|---|---|---|
| 214 | `ab` | `(a+b+c)*` | acepta | **V** | Dos repeticiones: a y b. |

#### AFND-λ de Thompson de (a+b+c)* — `L3-VF-214`

Archivos: [`L3-VF-214.jff`](../../automatas/lista3-afnd-lambda/L3-VF-214.jff) · [`L3-VF-214.json`](../../automatas/lista3-afnd-lambda/L3-VF-214.json) · [`L3-VF-214.xml`](../../automatas/lista3-afnd-lambda/L3-VF-214.xml). Tipo según la definición: **AFND-lambda**, |Q| = 10, Σ = {a, b, c}, 13 transiciones.

**Diseño.** Construcción de Thompson sobre Σ = {a, b, c}: cada símbolo es un fragmento i -a→ f; la unión y la estrella agregan un estado inicial y uno final unidos con λ, y la concatenación une fragmentos con λ.

| Estado | a | b | c | λ |
|---|---|---|---|---|
| →q0 | ∅ | ∅ | ∅ | {q1, q2} |
| q1 | ∅ | ∅ | ∅ | {q3, q4, q5} |
| q3 | {q6} | ∅ | ∅ | ∅ |
| q6 | ∅ | ∅ | ∅ | {q9} |
| q4 | ∅ | {q7} | ∅ | ∅ |
| q7 | ∅ | ∅ | ∅ | {q9} |
| q5 | ∅ | ∅ | {q8} | ∅ |
| q8 | ∅ | ∅ | ∅ | {q9} |
| q9 | ∅ | ∅ | ∅ | {q1, q2} |
| *q2 | ∅ | ∅ | ∅ | ∅ |

**Transiciones λ.** Las λ son las de la construcción de Thompson: en la unión eligen una alternativa, en la estrella permiten repetir o saltar el fragmento y en la concatenación enlazan fragmentos.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0, q1, q2, q3, q4, q5} | sí |
| q1 | {q1, q3, q4, q5} | no |
| q3 | {q3} | no |
| q6 | {q1, q2, q3, q4, q5, q6, q9} | sí |
| q4 | {q4} | no |
| q7 | {q1, q2, q3, q4, q5, q7, q9} | sí |
| q5 | {q5} | no |
| q8 | {q1, q2, q3, q4, q5, q8, q9} | sí |
| q9 | {q1, q2, q3, q4, q5, q9} | sí |
| q2 | {q2} | sí |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | acepta | acepta | acepta |
| 2 | `aa` | acepta | acepta | acepta |
| 3 | `bacc` | acepta | acepta | acepta |
| 4 | `accaaca` | acepta | acepta | acepta |
| 5 | `cbcbbaaacac` | acepta | acepta | acepta |
| 6 | `#` (símbolo fuera de Σ) | rechaza | rechaza | rechaza |
| 7 | `a#` (símbolo fuera de Σ) | rechaza | rechaza | rechaza |
| 8 | `#cc` (símbolo fuera de Σ) | rechaza | rechaza | rechaza |

Nota sobre los casos: todas las cadenas sobre Σ pertenecen al lenguaje, así que las inválidas usan un símbolo fuera de Σ (#).

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: {q0, q1, q2, q3, q4, q5} — ✔
  Árbol de cómputo: 6 caminos, 1 de aceptación:
    - q0 -λ→ q2 — ✔ acepta
    - q0 — ✘ termina fuera de F
    - q0 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q5 — ✘ termina fuera de F
2. `aa`: {q0, q1, q2, q3, q4, q5} -a→ {q1, q2, q3, q4, q5, q6, q9} -a→ {q1, q2, q3, q4, q5, q6, q9} — ✔
  Árbol de cómputo: 13 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q2 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q4 — ✘ termina fuera de F
3. `bacc`: {q0, q1, q2, q3, q4, q5} -b→ {q1, q2, q3, q4, q5, q7, q9} -a→ {q1, q2, q3, q4, q5, q6, q9} -c→ {q1, q2, q3, q4, q5, q8, q9} -c→ {q1, q2, q3, q4, q5, q8, q9} — ✔
  Árbol de cómputo: 19 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q5 -c→ q8 -λ→ q9 -λ→ q1 -λ→ q5 -c→ q8 -λ→ q9 -λ→ q2 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `ba`
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q4 — ✘ muere tras leer `ba`
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q5 -c→ q8 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `bac`
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q5 -c→ q8 -λ→ q9 -λ→ q1 -λ→ q4 — ✘ muere tras leer `bac`
4. `accaaca`: {q0, q1, q2, q3, q4, q5} -a→ {q1, q2, q3, q4, q5, q6, q9} -c→ {q1, q2, q3, q4, q5, q8, q9} -c→ {q1, q2, q3, q4, q5, q8, q9} -a→ {q1, q2, q3, q4, q5, q6, q9} -a→ {q1, q2, q3, q4, q5, q6, q9} -c→ {q1, q2, q3, q4, q5, q8, q9} -a→ {q1, q2, q3, q4, q5, q6, q9} — ✔
  Árbol de cómputo: 28 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q5 -c→ q8 -λ→ q9 -λ→ q1 -λ→ q5 -c→ q8 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q5 -c→ q8 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q2 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `a`
    - q0 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q4 — ✘ muere tras leer `a`
    - q0 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q5 -c→ q8 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `ac`
    - q0 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q5 -c→ q8 -λ→ q9 -λ→ q1 -λ→ q4 — ✘ muere tras leer `ac`
    - q0 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q5 -c→ q8 -λ→ q9 -λ→ q1 -λ→ q5 -c→ q8 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `accaa`
5. `cbcbbaaacac`: {q0, q1, q2, q3, q4, q5} -c→ {q1, q2, q3, q4, q5, q8, q9} -b→ {q1, q2, q3, q4, q5, q7, q9} -c→ {q1, q2, q3, q4, q5, q8, q9} -b→ {q1, q2, q3, q4, q5, q7, q9} -b→ {q1, q2, q3, q4, q5, q7, q9} -a→ {q1, q2, q3, q4, q5, q6, q9} -a→ {q1, q2, q3, q4, q5, q6, q9} -a→ {q1, q2, q3, q4, q5, q6, q9} -c→ {q1, q2, q3, q4, q5, q8, q9} -a→ {q1, q2, q3, q4, q5, q6, q9} -c→ {q1, q2, q3, q4, q5, q8, q9} — ✔
  Árbol de cómputo: 40 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q5 -c→ q8 -λ→ q9 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q5 -c→ q8 -λ→ q9 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q5 -c→ q8 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q5 -c→ q8 -λ→ q9 -λ→ q2 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q5 -c→ q8 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `c`
    - q0 -λ→ q1 -λ→ q5 -c→ q8 -λ→ q9 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `cb`
    - q0 -λ→ q1 -λ→ q5 -c→ q8 -λ→ q9 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q4 — ✘ muere tras leer `cb`
6. `#`: {q0, q1, q2, q3, q4, q5} -#→ ∅ — ✘
  Árbol de cómputo: 4 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q5 — ✘ muere tras leer λ
    - q0 -λ→ q2 — ✘ muere tras leer λ
7. `a#`: {q0, q1, q2, q3, q4, q5} -a→ {q1, q2, q3, q4, q5, q6, q9} -#→ ∅ — ✘
  Árbol de cómputo: 7 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `a`
    - q0 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q4 — ✘ muere tras leer `a`
    - q0 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q5 — ✘ muere tras leer `a`
    - q0 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q2 — ✘ muere tras leer `a`
    - q0 -λ→ q1 -λ→ q4 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q5 — ✘ muere tras leer λ
8. `#cc`: {q0, q1, q2, q3, q4, q5} -#→ ∅ -c→ ∅ -c→ ∅ — ✘
  Árbol de cómputo: 4 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q5 — ✘ muere tras leer λ
    - q0 -λ→ q2 — ✘ muere tras leer λ

</details>

Simulación paso a paso en JFLAP con `aa`: [ver captura](../../evidencias/jflap/pasos/L3-VF-214.png).

**Conversión.** AFND-λ (10 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 10 estados, [`L3-VF-214-AFND.jff`](../../automatas/conversiones/L3-VF-214-AFND.jff). AFND (10 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 4 estados, [`L3-VF-214-AFD.jff`](../../automatas/conversiones/L3-VF-214-AFD.jff) ([.json](../../automatas/conversiones/L3-VF-214-AFD.json), [.xml](../../automatas/conversiones/L3-VF-214-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 4 estados, y el AFD mínimo (Hopcroft), 1. La cota es 2^10 = 1024. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-215"></a>

## Lista 3, problema 215

**Enunciado.** ¿Es verdadera la afirmación «w ∈ L((abc)*)»? Afirmaciones 215.

**Clasificación: AFND-λ.** Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

| Afirmación | Cadena | Expresión | AFND-λ de Thompson | Respuesta | Razón |
|---|---|---|---|---|---|
| 215 | `ab` | `(abc)*` | rechaza | **F** | Las longitudes son múltiplos de 3. |

#### AFND-λ de Thompson de (abc)* — `L3-VF-215`

Archivos: [`L3-VF-215.jff`](../../automatas/lista3-afnd-lambda/L3-VF-215.jff) · [`L3-VF-215.json`](../../automatas/lista3-afnd-lambda/L3-VF-215.json) · [`L3-VF-215.xml`](../../automatas/lista3-afnd-lambda/L3-VF-215.xml). Tipo según la definición: **AFND-lambda**, |Q| = 8, Σ = {a, b, c}, 9 transiciones.

**Diseño.** Construcción de Thompson sobre Σ = {a, b, c}: cada símbolo es un fragmento i -a→ f; la unión y la estrella agregan un estado inicial y uno final unidos con λ, y la concatenación une fragmentos con λ.

| Estado | a | b | c | λ |
|---|---|---|---|---|
| →q0 | ∅ | ∅ | ∅ | {q1, q2} |
| q1 | {q3} | ∅ | ∅ | ∅ |
| q3 | ∅ | ∅ | ∅ | {q4} |
| q4 | ∅ | {q5} | ∅ | ∅ |
| q5 | ∅ | ∅ | ∅ | {q6} |
| q6 | ∅ | ∅ | {q7} | ∅ |
| q7 | ∅ | ∅ | ∅ | {q1, q2} |
| *q2 | ∅ | ∅ | ∅ | ∅ |

**Transiciones λ.** Las λ son las de la construcción de Thompson: en la unión eligen una alternativa, en la estrella permiten repetir o saltar el fragmento y en la concatenación enlazan fragmentos.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0, q1, q2} | sí |
| q1 | {q1} | no |
| q3 | {q3, q4} | no |
| q4 | {q4} | no |
| q5 | {q5, q6} | no |
| q6 | {q6} | no |
| q7 | {q1, q2, q7} | sí |
| q2 | {q2} | sí |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | acepta | acepta | acepta |
| 2 | `abc` | acepta | acepta | acepta |
| 3 | `abcabc` | acepta | acepta | acepta |
| 4 | `abcabcabc` | acepta | acepta | acepta |
| 5 | `abcabcabcabc` | acepta | acepta | acepta |
| 6 | `a` | rechaza | rechaza | — |
| 7 | `ba` | rechaza | rechaza | rechaza |
| 8 | `caba` | rechaza | rechaza | rechaza |
| 9 | `cccbccc` | rechaza | rechaza | rechaza |
| 10 | `baaababcccc` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: {q0, q1, q2} — ✔
  Árbol de cómputo: 3 caminos, 1 de aceptación:
    - q0 -λ→ q2 — ✔ acepta
    - q0 — ✘ termina fuera de F
    - q0 -λ→ q1 — ✘ termina fuera de F
2. `abc`: {q0, q1, q2} -a→ {q3, q4} -b→ {q5, q6} -c→ {q1, q2, q7} — ✔
  Árbol de cómputo: 4 caminos, 1 de aceptación:
    - q0 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q6 -c→ q7 -λ→ q2 — ✔ acepta
    - q0 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q6 -c→ q7 — ✘ termina fuera de F
    - q0 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q6 -c→ q7 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q2 — ✘ muere tras leer λ
3. `abcabc`: {q0, q1, q2} -a→ {q3, q4} -b→ {q5, q6} -c→ {q1, q2, q7} -a→ {q3, q4} -b→ {q5, q6} -c→ {q1, q2, q7} — ✔
  Árbol de cómputo: 5 caminos, 1 de aceptación:
    - q0 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q6 -c→ q7 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q6 -c→ q7 -λ→ q2 — ✔ acepta
    - q0 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q6 -c→ q7 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q6 -c→ q7 — ✘ termina fuera de F
    - q0 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q6 -c→ q7 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q6 -c→ q7 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q6 -c→ q7 -λ→ q2 — ✘ muere tras leer `abc`
    - q0 -λ→ q2 — ✘ muere tras leer λ
4. `abcabcabc`: {q0, q1, q2} -a→ {q3, q4} -b→ {q5, q6} -c→ {q1, q2, q7} -a→ {q3, q4} -b→ {q5, q6} -c→ {q1, q2, q7} -a→ {q3, q4} -b→ {q5, q6} -c→ {q1, q2, q7} — ✔
  Árbol de cómputo: 6 caminos, 1 de aceptación:
    - q0 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q6 -c→ q7 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q6 -c→ q7 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q6 -c→ q7 -λ→ q2 — ✔ acepta
    - q0 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q6 -c→ q7 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q6 -c→ q7 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q6 -c→ q7 — ✘ termina fuera de F
    - q0 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q6 -c→ q7 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q6 -c→ q7 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q6 -c→ q7 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q6 -c→ q7 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q6 -c→ q7 -λ→ q2 — ✘ muere tras leer `abcabc`
    - q0 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q6 -c→ q7 -λ→ q2 — ✘ muere tras leer `abc`
    - q0 -λ→ q2 — ✘ muere tras leer λ
5. `abcabcabcabc`: {q0, q1, q2} -a→ {q3, q4} -b→ {q5, q6} -c→ {q1, q2, q7} -a→ {q3, q4} -b→ {q5, q6} -c→ {q1, q2, q7} -a→ {q3, q4} -b→ {q5, q6} -c→ {q1, q2, q7} -a→ {q3, q4} -b→ {q5, q6} -c→ {q1, q2, q7} — ✔
  Árbol de cómputo: 7 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q6 -c→ q7 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q6 -c→ q7 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q6 -c→ q7 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q6 -c→ q7 -λ→ q2 — ✔ acepta
    - q0 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q6 -c→ q7 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q6 -c→ q7 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q6 -c→ q7 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q6 -c→ q7 — ✘ termina fuera de F
    - q0 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q6 -c→ q7 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q6 -c→ q7 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q6 -c→ q7 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q6 -c→ q7 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q6 -c→ q7 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q6 -c→ q7 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q6 -c→ q7 -λ→ q2 — ✘ muere tras leer `abcabcabc`
    - q0 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q6 -c→ q7 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q6 -c→ q7 -λ→ q2 — ✘ muere tras leer `abcabc`
    - q0 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q6 -c→ q7 -λ→ q2 — ✘ muere tras leer `abc`
6. `a`: {q0, q1, q2} -a→ {q3, q4} — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - q0 -λ→ q1 -a→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -a→ q3 -λ→ q4 — ✘ termina fuera de F
    - q0 -λ→ q2 — ✘ muere tras leer λ
7. `ba`: {q0, q1, q2} -b→ ∅ -a→ ∅ — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 — ✘ muere tras leer λ
8. `caba`: {q0, q1, q2} -c→ ∅ -a→ ∅ -b→ ∅ -a→ ∅ — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 — ✘ muere tras leer λ
9. `cccbccc`: {q0, q1, q2} -c→ ∅ -c→ ∅ -c→ ∅ -b→ ∅ -c→ ∅ -c→ ∅ -c→ ∅ — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 — ✘ muere tras leer λ
10. `baaababcccc`: {q0, q1, q2} -b→ ∅ -a→ ∅ -a→ ∅ -a→ ∅ -b→ ∅ -a→ ∅ -b→ ∅ -c→ ∅ -c→ ∅ -c→ ∅ -c→ ∅ — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 — ✘ muere tras leer λ

</details>

Simulación paso a paso en JFLAP con `abc`: [ver captura](../../evidencias/jflap/pasos/L3-VF-215.png).

**Conversión.** AFND-λ (8 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 8 estados, [`L3-VF-215-AFND.jff`](../../automatas/conversiones/L3-VF-215-AFND.jff). AFND (8 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 4 estados, [`L3-VF-215-AFD.jff`](../../automatas/conversiones/L3-VF-215-AFD.jff) ([.json](../../automatas/conversiones/L3-VF-215-AFD.json), [.xml](../../automatas/conversiones/L3-VF-215-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 5 estados, y el AFD mínimo (Hopcroft), 4. La cota es 2^8 = 256. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-216"></a>

## Lista 3, problema 216

**Enunciado.** ¿Es verdadera la afirmación «w ∈ L((ab)*c)»? Afirmaciones 216.

**Clasificación: AFND-λ.** Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

| Afirmación | Cadena | Expresión | AFND-λ de Thompson | Respuesta | Razón |
|---|---|---|---|---|---|
| 216 | `ab` | `(ab)*c` | rechaza | **F** | Toda palabra termina en c. |

#### AFND-λ de Thompson de (ab)*c — `L3-VF-216`

Archivos: [`L3-VF-216.jff`](../../automatas/lista3-afnd-lambda/L3-VF-216.jff) · [`L3-VF-216.json`](../../automatas/lista3-afnd-lambda/L3-VF-216.json) · [`L3-VF-216.xml`](../../automatas/lista3-afnd-lambda/L3-VF-216.xml). Tipo según la definición: **AFND-lambda**, |Q| = 8, Σ = {a, b, c}, 9 transiciones.

**Diseño.** Construcción de Thompson sobre Σ = {a, b, c}: cada símbolo es un fragmento i -a→ f; la unión y la estrella agregan un estado inicial y uno final unidos con λ, y la concatenación une fragmentos con λ.

| Estado | a | b | c | λ |
|---|---|---|---|---|
| →q0 | ∅ | ∅ | ∅ | {q1, q2} |
| q1 | {q3} | ∅ | ∅ | ∅ |
| q3 | ∅ | ∅ | ∅ | {q5} |
| q5 | ∅ | {q7} | ∅ | ∅ |
| q7 | ∅ | ∅ | ∅ | {q1, q2} |
| q2 | ∅ | ∅ | ∅ | {q4} |
| q4 | ∅ | ∅ | {q6} | ∅ |
| *q6 | ∅ | ∅ | ∅ | ∅ |

**Transiciones λ.** Las λ son las de la construcción de Thompson: en la unión eligen una alternativa, en la estrella permiten repetir o saltar el fragmento y en la concatenación enlazan fragmentos.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0, q1, q2, q4} | no |
| q1 | {q1} | no |
| q3 | {q3, q5} | no |
| q5 | {q5} | no |
| q7 | {q1, q2, q4, q7} | no |
| q2 | {q2, q4} | no |
| q4 | {q4} | no |
| q6 | {q6} | sí |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `c` | acepta | acepta | acepta |
| 2 | `abc` | acepta | acepta | acepta |
| 3 | `ababc` | acepta | acepta | acepta |
| 4 | `abababc` | acepta | acepta | acepta |
| 5 | `ababababc` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `cb` | rechaza | rechaza | rechaza |
| 8 | `cccb` | rechaza | rechaza | rechaza |
| 9 | `bbacbca` | rechaza | rechaza | rechaza |
| 10 | `caaccaacabc` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `c`: {q0, q1, q2, q4} -c→ {q6} — ✔
  Árbol de cómputo: 2 caminos, 1 de aceptación:
    - q0 -λ→ q2 -λ→ q4 -c→ q6 — ✔ acepta
    - q0 -λ→ q1 — ✘ muere tras leer λ
2. `abc`: {q0, q1, q2, q4} -a→ {q3, q5} -b→ {q1, q2, q4, q7} -c→ {q6} — ✔
  Árbol de cómputo: 3 caminos, 1 de aceptación:
    - q0 -λ→ q1 -a→ q3 -λ→ q5 -b→ q7 -λ→ q2 -λ→ q4 -c→ q6 — ✔ acepta
    - q0 -λ→ q1 -a→ q3 -λ→ q5 -b→ q7 -λ→ q1 — ✘ muere tras leer `ab`
    - q0 -λ→ q2 -λ→ q4 — ✘ muere tras leer λ
3. `ababc`: {q0, q1, q2, q4} -a→ {q3, q5} -b→ {q1, q2, q4, q7} -a→ {q3, q5} -b→ {q1, q2, q4, q7} -c→ {q6} — ✔
  Árbol de cómputo: 4 caminos, 1 de aceptación:
    - q0 -λ→ q1 -a→ q3 -λ→ q5 -b→ q7 -λ→ q1 -a→ q3 -λ→ q5 -b→ q7 -λ→ q2 -λ→ q4 -c→ q6 — ✔ acepta
    - q0 -λ→ q1 -a→ q3 -λ→ q5 -b→ q7 -λ→ q1 -a→ q3 -λ→ q5 -b→ q7 -λ→ q1 — ✘ muere tras leer `abab`
    - q0 -λ→ q1 -a→ q3 -λ→ q5 -b→ q7 -λ→ q2 -λ→ q4 — ✘ muere tras leer `ab`
    - q0 -λ→ q2 -λ→ q4 — ✘ muere tras leer λ
4. `abababc`: {q0, q1, q2, q4} -a→ {q3, q5} -b→ {q1, q2, q4, q7} -a→ {q3, q5} -b→ {q1, q2, q4, q7} -a→ {q3, q5} -b→ {q1, q2, q4, q7} -c→ {q6} — ✔
  Árbol de cómputo: 5 caminos, 1 de aceptación:
    - q0 -λ→ q1 -a→ q3 -λ→ q5 -b→ q7 -λ→ q1 -a→ q3 -λ→ q5 -b→ q7 -λ→ q1 -a→ q3 -λ→ q5 -b→ q7 -λ→ q2 -λ→ q4 -c→ q6 — ✔ acepta
    - q0 -λ→ q1 -a→ q3 -λ→ q5 -b→ q7 -λ→ q1 -a→ q3 -λ→ q5 -b→ q7 -λ→ q1 -a→ q3 -λ→ q5 -b→ q7 -λ→ q1 — ✘ muere tras leer `ababab`
    - q0 -λ→ q1 -a→ q3 -λ→ q5 -b→ q7 -λ→ q1 -a→ q3 -λ→ q5 -b→ q7 -λ→ q2 -λ→ q4 — ✘ muere tras leer `abab`
    - q0 -λ→ q1 -a→ q3 -λ→ q5 -b→ q7 -λ→ q2 -λ→ q4 — ✘ muere tras leer `ab`
    - q0 -λ→ q2 -λ→ q4 — ✘ muere tras leer λ
5. `ababababc`: {q0, q1, q2, q4} -a→ {q3, q5} -b→ {q1, q2, q4, q7} -a→ {q3, q5} -b→ {q1, q2, q4, q7} -a→ {q3, q5} -b→ {q1, q2, q4, q7} -a→ {q3, q5} -b→ {q1, q2, q4, q7} -c→ {q6} — ✔
  Árbol de cómputo: 6 caminos, 1 de aceptación:
    - q0 -λ→ q1 -a→ q3 -λ→ q5 -b→ q7 -λ→ q1 -a→ q3 -λ→ q5 -b→ q7 -λ→ q1 -a→ q3 -λ→ q5 -b→ q7 -λ→ q1 -a→ q3 -λ→ q5 -b→ q7 -λ→ q2 -λ→ q4 -c→ q6 — ✔ acepta
    - q0 -λ→ q1 -a→ q3 -λ→ q5 -b→ q7 -λ→ q1 -a→ q3 -λ→ q5 -b→ q7 -λ→ q1 -a→ q3 -λ→ q5 -b→ q7 -λ→ q1 -a→ q3 -λ→ q5 -b→ q7 -λ→ q1 — ✘ muere tras leer `abababab`
    - q0 -λ→ q1 -a→ q3 -λ→ q5 -b→ q7 -λ→ q1 -a→ q3 -λ→ q5 -b→ q7 -λ→ q1 -a→ q3 -λ→ q5 -b→ q7 -λ→ q2 -λ→ q4 — ✘ muere tras leer `ababab`
    - q0 -λ→ q1 -a→ q3 -λ→ q5 -b→ q7 -λ→ q1 -a→ q3 -λ→ q5 -b→ q7 -λ→ q2 -λ→ q4 — ✘ muere tras leer `abab`
    - q0 -λ→ q1 -a→ q3 -λ→ q5 -b→ q7 -λ→ q2 -λ→ q4 — ✘ muere tras leer `ab`
    - q0 -λ→ q2 -λ→ q4 — ✘ muere tras leer λ
6. λ: {q0, q1, q2, q4} — ✘
  Árbol de cómputo: 4 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
    - q0 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q2 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q4 — ✘ termina fuera de F
7. `cb`: {q0, q1, q2, q4} -c→ {q6} -b→ ∅ — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q4 -c→ q6 — ✘ muere tras leer `c`
8. `cccb`: {q0, q1, q2, q4} -c→ {q6} -c→ ∅ -c→ ∅ -b→ ∅ — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q4 -c→ q6 — ✘ muere tras leer `c`
9. `bbacbca`: {q0, q1, q2, q4} -b→ ∅ -b→ ∅ -a→ ∅ -c→ ∅ -b→ ∅ -c→ ∅ -a→ ∅ — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q4 — ✘ muere tras leer λ
10. `caaccaacabc`: {q0, q1, q2, q4} -c→ {q6} -a→ ∅ -a→ ∅ -c→ ∅ -c→ ∅ -a→ ∅ -a→ ∅ -c→ ∅ -a→ ∅ -b→ ∅ -c→ ∅ — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q4 -c→ q6 — ✘ muere tras leer `c`

</details>

Simulación paso a paso en JFLAP con `abc`: [ver captura](../../evidencias/jflap/pasos/L3-VF-216.png).

**Conversión.** AFND-λ (8 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 8 estados, [`L3-VF-216-AFND.jff`](../../automatas/conversiones/L3-VF-216-AFND.jff). AFND (8 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 4 estados, [`L3-VF-216-AFD.jff`](../../automatas/conversiones/L3-VF-216-AFD.jff) ([.json](../../automatas/conversiones/L3-VF-216-AFD.json), [.xml](../../automatas/conversiones/L3-VF-216-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 5 estados, y el AFD mínimo (Hopcroft), 4. La cota es 2^8 = 256. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-217"></a>

## Lista 3, problema 217

**Enunciado.** ¿Es verdadera la afirmación «w ∈ L(a(bc)*)»? Afirmaciones 217.

**Clasificación: AFND-λ.** Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

| Afirmación | Cadena | Expresión | AFND-λ de Thompson | Respuesta | Razón |
|---|---|---|---|---|---|
| 217 | `ab` | `a(bc)*` | rechaza | **F** | Las palabras tienen longitud impar. |

#### AFND-λ de Thompson de a(bc)* — `L3-VF-217`

Archivos: [`L3-VF-217.jff`](../../automatas/lista3-afnd-lambda/L3-VF-217.jff) · [`L3-VF-217.json`](../../automatas/lista3-afnd-lambda/L3-VF-217.json) · [`L3-VF-217.xml`](../../automatas/lista3-afnd-lambda/L3-VF-217.xml). Tipo según la definición: **AFND-lambda**, |Q| = 8, Σ = {a, b, c}, 9 transiciones.

**Diseño.** Construcción de Thompson sobre Σ = {a, b, c}: cada símbolo es un fragmento i -a→ f; la unión y la estrella agregan un estado inicial y uno final unidos con λ, y la concatenación une fragmentos con λ.

| Estado | a | b | c | λ |
|---|---|---|---|---|
| →q0 | {q1} | ∅ | ∅ | ∅ |
| q1 | ∅ | ∅ | ∅ | {q2} |
| q2 | ∅ | ∅ | ∅ | {q3, q4} |
| q3 | ∅ | {q5} | ∅ | ∅ |
| q5 | ∅ | ∅ | ∅ | {q6} |
| q6 | ∅ | ∅ | {q7} | ∅ |
| q7 | ∅ | ∅ | ∅ | {q3, q4} |
| *q4 | ∅ | ∅ | ∅ | ∅ |

**Transiciones λ.** Las λ son las de la construcción de Thompson: en la unión eligen una alternativa, en la estrella permiten repetir o saltar el fragmento y en la concatenación enlazan fragmentos.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0} | no |
| q1 | {q1, q2, q3, q4} | sí |
| q2 | {q2, q3, q4} | sí |
| q3 | {q3} | no |
| q5 | {q5, q6} | no |
| q6 | {q6} | no |
| q7 | {q3, q4, q7} | sí |
| q4 | {q4} | sí |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `a` | acepta | acepta | acepta |
| 2 | `abc` | acepta | acepta | acepta |
| 3 | `abcbc` | acepta | acepta | acepta |
| 4 | `abcbcbc` | acepta | acepta | acepta |
| 5 | `abcbcbcbcbc` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `bb` | rechaza | rechaza | rechaza |
| 8 | `aacb` | rechaza | rechaza | rechaza |
| 9 | `caccbac` | rechaza | rechaza | rechaza |
| 10 | `cacacbacbbb` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `a`: {q0} -a→ {q1, q2, q3, q4} — ✔
  Árbol de cómputo: 4 caminos, 1 de aceptación:
    - q0 -a→ q1 -λ→ q2 -λ→ q4 — ✔ acepta
    - q0 -a→ q1 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q3 — ✘ termina fuera de F
2. `abc`: {q0} -a→ {q1, q2, q3, q4} -b→ {q5, q6} -c→ {q3, q4, q7} — ✔
  Árbol de cómputo: 4 caminos, 1 de aceptación:
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q4 — ✔ acepta
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q3 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q4 — ✘ muere tras leer `a`
3. `abcbc`: {q0} -a→ {q1, q2, q3, q4} -b→ {q5, q6} -c→ {q3, q4, q7} -b→ {q5, q6} -c→ {q3, q4, q7} — ✔
  Árbol de cómputo: 5 caminos, 1 de aceptación:
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q4 — ✔ acepta
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q3 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q4 — ✘ muere tras leer `abc`
    - q0 -a→ q1 -λ→ q2 -λ→ q4 — ✘ muere tras leer `a`
4. `abcbcbc`: {q0} -a→ {q1, q2, q3, q4} -b→ {q5, q6} -c→ {q3, q4, q7} -b→ {q5, q6} -c→ {q3, q4, q7} -b→ {q5, q6} -c→ {q3, q4, q7} — ✔
  Árbol de cómputo: 6 caminos, 1 de aceptación:
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q4 — ✔ acepta
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q3 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q4 — ✘ muere tras leer `abcbc`
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q4 — ✘ muere tras leer `abc`
    - q0 -a→ q1 -λ→ q2 -λ→ q4 — ✘ muere tras leer `a`
5. `abcbcbcbcbc`: {q0} -a→ {q1, q2, q3, q4} -b→ {q5, q6} -c→ {q3, q4, q7} -b→ {q5, q6} -c→ {q3, q4, q7} -b→ {q5, q6} -c→ {q3, q4, q7} -b→ {q5, q6} -c→ {q3, q4, q7} -b→ {q5, q6} -c→ {q3, q4, q7} — ✔
  Árbol de cómputo: 8 caminos, 1 de aceptación (se muestran 6):
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q4 — ✔ acepta
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q3 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q4 — ✘ muere tras leer `abcbcbcbc`
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q4 — ✘ muere tras leer `abcbcbc`
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q3 -b→ q5 -λ→ q6 -c→ q7 -λ→ q4 — ✘ muere tras leer `abcbc`
6. λ: {q0} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
7. `bb`: {q0} -b→ ∅ -b→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ
8. `aacb`: {q0} -a→ {q1, q2, q3, q4} -a→ ∅ -c→ ∅ -b→ ∅ — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -a→ q1 -λ→ q2 -λ→ q3 — ✘ muere tras leer `a`
    - q0 -a→ q1 -λ→ q2 -λ→ q4 — ✘ muere tras leer `a`
9. `caccbac`: {q0} -c→ ∅ -a→ ∅ -c→ ∅ -c→ ∅ -b→ ∅ -a→ ∅ -c→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ
10. `cacacbacbbb`: {q0} -c→ ∅ -a→ ∅ -c→ ∅ -a→ ∅ -c→ ∅ -b→ ∅ -a→ ∅ -c→ ∅ -b→ ∅ -b→ ∅ -b→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ

</details>

Simulación paso a paso en JFLAP con `abc`: [ver captura](../../evidencias/jflap/pasos/L3-VF-217.png).

**Conversión.** AFND-λ (8 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 8 estados, [`L3-VF-217-AFND.jff`](../../automatas/conversiones/L3-VF-217-AFND.jff). AFND (8 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 4 estados, [`L3-VF-217-AFD.jff`](../../automatas/conversiones/L3-VF-217-AFD.jff) ([.json](../../automatas/conversiones/L3-VF-217-AFD.json), [.xml](../../automatas/conversiones/L3-VF-217-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 5 estados, y el AFD mínimo (Hopcroft), 4. La cota es 2^8 = 256. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-218"></a>

## Lista 3, problema 218

**Enunciado.** ¿Es verdadera la afirmación «w ∈ L(a(b+c)*)»? Afirmaciones 218.

**Clasificación: AFND-λ.** Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

| Afirmación | Cadena | Expresión | AFND-λ de Thompson | Respuesta | Razón |
|---|---|---|---|---|---|
| 218 | `ab` | `a(b+c)*` | acepta | **V** | a seguida de una b. |

#### AFND-λ de Thompson de a(b+c)* — `L3-VF-218`

Archivos: [`L3-VF-218.jff`](../../automatas/lista3-afnd-lambda/L3-VF-218.jff) · [`L3-VF-218.json`](../../automatas/lista3-afnd-lambda/L3-VF-218.json) · [`L3-VF-218.xml`](../../automatas/lista3-afnd-lambda/L3-VF-218.xml). Tipo según la definición: **AFND-lambda**, |Q| = 10, Σ = {a, b, c}, 12 transiciones.

**Diseño.** Construcción de Thompson sobre Σ = {a, b, c}: cada símbolo es un fragmento i -a→ f; la unión y la estrella agregan un estado inicial y uno final unidos con λ, y la concatenación une fragmentos con λ.

| Estado | a | b | c | λ |
|---|---|---|---|---|
| →q0 | {q1} | ∅ | ∅ | ∅ |
| q1 | ∅ | ∅ | ∅ | {q2} |
| q2 | ∅ | ∅ | ∅ | {q3, q4} |
| q3 | ∅ | ∅ | ∅ | {q5, q6} |
| q5 | ∅ | {q7} | ∅ | ∅ |
| q7 | ∅ | ∅ | ∅ | {q9} |
| q6 | ∅ | ∅ | {q8} | ∅ |
| q8 | ∅ | ∅ | ∅ | {q9} |
| q9 | ∅ | ∅ | ∅ | {q3, q4} |
| *q4 | ∅ | ∅ | ∅ | ∅ |

**Transiciones λ.** Las λ son las de la construcción de Thompson: en la unión eligen una alternativa, en la estrella permiten repetir o saltar el fragmento y en la concatenación enlazan fragmentos.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0} | no |
| q1 | {q1, q2, q3, q4, q5, q6} | sí |
| q2 | {q2, q3, q4, q5, q6} | sí |
| q3 | {q3, q5, q6} | no |
| q5 | {q5} | no |
| q7 | {q3, q4, q5, q6, q7, q9} | sí |
| q6 | {q6} | no |
| q8 | {q3, q4, q5, q6, q8, q9} | sí |
| q9 | {q3, q4, q5, q6, q9} | sí |
| q4 | {q4} | sí |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `a` | acepta | acepta | acepta |
| 2 | `ab` | acepta | acepta | acepta |
| 3 | `abbc` | acepta | acepta | acepta |
| 4 | `accbcbb` | acepta | acepta | acepta |
| 5 | `abcbbcbcbcb` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `cb` | rechaza | rechaza | rechaza |
| 8 | `acac` | rechaza | rechaza | rechaza |
| 9 | `ccbabbc` | rechaza | rechaza | rechaza |
| 10 | `caacbbabacb` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `a`: {q0} -a→ {q1, q2, q3, q4, q5, q6} — ✔
  Árbol de cómputo: 6 caminos, 1 de aceptación:
    - q0 -a→ q1 -λ→ q2 -λ→ q4 — ✔ acepta
    - q0 -a→ q1 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q3 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q5 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q6 — ✘ termina fuera de F
2. `ab`: {q0} -a→ {q1, q2, q3, q4, q5, q6} -b→ {q3, q4, q5, q6, q7, q9} — ✔
  Árbol de cómputo: 8 caminos, 1 de aceptación (se muestran 6):
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q4 — ✔ acepta
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -b→ q7 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q5 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q6 — ✘ termina fuera de F
3. `abbc`: {q0} -a→ {q1, q2, q3, q4, q5, q6} -b→ {q3, q4, q5, q6, q7, q9} -b→ {q3, q4, q5, q6, q7, q9} -c→ {q3, q4, q5, q6, q8, q9} — ✔
  Árbol de cómputo: 12 caminos, 1 de aceptación (se muestran 6):
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -c→ q8 -λ→ q9 -λ→ q4 — ✔ acepta
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q5 — ✘ muere tras leer `abb`
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -c→ q8 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -c→ q8 -λ→ q9 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -c→ q8 -λ→ q9 -λ→ q3 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -c→ q8 -λ→ q9 -λ→ q3 -λ→ q5 — ✘ termina fuera de F
4. `accbcbb`: {q0} -a→ {q1, q2, q3, q4, q5, q6} -c→ {q3, q4, q5, q6, q8, q9} -c→ {q3, q4, q5, q6, q8, q9} -b→ {q3, q4, q5, q6, q7, q9} -c→ {q3, q4, q5, q6, q8, q9} -b→ {q3, q4, q5, q6, q7, q9} -b→ {q3, q4, q5, q6, q7, q9} — ✔
  Árbol de cómputo: 18 caminos, 1 de aceptación (se muestran 6):
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q6 -c→ q8 -λ→ q9 -λ→ q3 -λ→ q6 -c→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -c→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q4 — ✔ acepta
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q5 — ✘ muere tras leer `a`
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q6 -c→ q8 -λ→ q9 -λ→ q3 -λ→ q5 — ✘ muere tras leer `ac`
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q6 -c→ q8 -λ→ q9 -λ→ q3 -λ→ q6 -c→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q5 — ✘ muere tras leer `accb`
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q6 -c→ q8 -λ→ q9 -λ→ q3 -λ→ q6 -c→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -c→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q5 -b→ q7 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q6 -c→ q8 -λ→ q9 -λ→ q3 -λ→ q6 -c→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -c→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 — ✘ termina fuera de F
5. `abcbbcbcbcb`: {q0} -a→ {q1, q2, q3, q4, q5, q6} -b→ {q3, q4, q5, q6, q7, q9} -c→ {q3, q4, q5, q6, q8, q9} -b→ {q3, q4, q5, q6, q7, q9} -b→ {q3, q4, q5, q6, q7, q9} -c→ {q3, q4, q5, q6, q8, q9} -b→ {q3, q4, q5, q6, q7, q9} -c→ {q3, q4, q5, q6, q8, q9} -b→ {q3, q4, q5, q6, q7, q9} -c→ {q3, q4, q5, q6, q8, q9} -b→ {q3, q4, q5, q6, q7, q9} — ✔
  Árbol de cómputo: 26 caminos, 1 de aceptación (se muestran 6):
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -c→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -c→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -c→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -c→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q4 — ✔ acepta
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q5 — ✘ muere tras leer `ab`
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -c→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q5 — ✘ muere tras leer `abcbb`
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -c→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -c→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q5 — ✘ muere tras leer `abcbbcb`
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -c→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -c→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -c→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q5 — ✘ muere tras leer `abcbbcbcb`
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -c→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -c→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -c→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -b→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -c→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -b→ q7 — ✘ termina fuera de F
6. λ: {q0} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
7. `cb`: {q0} -c→ ∅ -b→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ
8. `acac`: {q0} -a→ {q1, q2, q3, q4, q5, q6} -c→ {q3, q4, q5, q6, q8, q9} -a→ ∅ -c→ ∅ — ✘
  Árbol de cómputo: 5 caminos, 0 de aceptación:
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q5 — ✘ muere tras leer `a`
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q6 -c→ q8 -λ→ q9 -λ→ q3 -λ→ q5 — ✘ muere tras leer `ac`
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q6 -c→ q8 -λ→ q9 -λ→ q3 -λ→ q6 — ✘ muere tras leer `ac`
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q6 -c→ q8 -λ→ q9 -λ→ q4 — ✘ muere tras leer `ac`
    - q0 -a→ q1 -λ→ q2 -λ→ q4 — ✘ muere tras leer `a`
9. `ccbabbc`: {q0} -c→ ∅ -c→ ∅ -b→ ∅ -a→ ∅ -b→ ∅ -b→ ∅ -c→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ
10. `caacbbabacb`: {q0} -c→ ∅ -a→ ∅ -a→ ∅ -c→ ∅ -b→ ∅ -b→ ∅ -a→ ∅ -b→ ∅ -a→ ∅ -c→ ∅ -b→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ

</details>

Simulación paso a paso en JFLAP con `ab`: [ver captura](../../evidencias/jflap/pasos/L3-VF-218.png).

**Conversión.** AFND-λ (10 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 10 estados, [`L3-VF-218-AFND.jff`](../../automatas/conversiones/L3-VF-218-AFND.jff). AFND (10 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 4 estados, [`L3-VF-218-AFD.jff`](../../automatas/conversiones/L3-VF-218-AFD.jff) ([.json](../../automatas/conversiones/L3-VF-218-AFD.json), [.xml](../../automatas/conversiones/L3-VF-218-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 5 estados, y el AFD mínimo (Hopcroft), 3. La cota es 2^10 = 1024. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-219"></a>

## Lista 3, problema 219

**Enunciado.** ¿Es verdadera la afirmación «w ∈ L((a+b)*c)»? Afirmaciones 219.

**Clasificación: AFND-λ.** Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

| Afirmación | Cadena | Expresión | AFND-λ de Thompson | Respuesta | Razón |
|---|---|---|---|---|---|
| 219 | `ab` | `(a+b)*c` | rechaza | **F** | Toda palabra termina en c. |

#### AFND-λ de Thompson de (a+b)*c — `L3-VF-219`

Archivos: [`L3-VF-219.jff`](../../automatas/lista3-afnd-lambda/L3-VF-219.jff) · [`L3-VF-219.json`](../../automatas/lista3-afnd-lambda/L3-VF-219.json) · [`L3-VF-219.xml`](../../automatas/lista3-afnd-lambda/L3-VF-219.xml). Tipo según la definición: **AFND-lambda**, |Q| = 10, Σ = {a, b, c}, 12 transiciones.

**Diseño.** Construcción de Thompson sobre Σ = {a, b, c}: cada símbolo es un fragmento i -a→ f; la unión y la estrella agregan un estado inicial y uno final unidos con λ, y la concatenación une fragmentos con λ.

| Estado | a | b | c | λ |
|---|---|---|---|---|
| →q0 | ∅ | ∅ | ∅ | {q1, q2} |
| q1 | ∅ | ∅ | ∅ | {q3, q4} |
| q3 | {q6} | ∅ | ∅ | ∅ |
| q6 | ∅ | ∅ | ∅ | {q9} |
| q4 | ∅ | {q7} | ∅ | ∅ |
| q7 | ∅ | ∅ | ∅ | {q9} |
| q9 | ∅ | ∅ | ∅ | {q1, q2} |
| q2 | ∅ | ∅ | ∅ | {q5} |
| q5 | ∅ | ∅ | {q8} | ∅ |
| *q8 | ∅ | ∅ | ∅ | ∅ |

**Transiciones λ.** Las λ son las de la construcción de Thompson: en la unión eligen una alternativa, en la estrella permiten repetir o saltar el fragmento y en la concatenación enlazan fragmentos.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0, q1, q2, q3, q4, q5} | no |
| q1 | {q1, q3, q4} | no |
| q3 | {q3} | no |
| q6 | {q1, q2, q3, q4, q5, q6, q9} | no |
| q4 | {q4} | no |
| q7 | {q1, q2, q3, q4, q5, q7, q9} | no |
| q9 | {q1, q2, q3, q4, q5, q9} | no |
| q2 | {q2, q5} | no |
| q5 | {q5} | no |
| q8 | {q8} | sí |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `c` | acepta | acepta | acepta |
| 2 | `bc` | acepta | acepta | acepta |
| 3 | `bac` | acepta | acepta | acepta |
| 4 | `abac` | acepta | acepta | acepta |
| 5 | `babaac` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `bb` | rechaza | rechaza | rechaza |
| 8 | `bbaca` | rechaza | rechaza | rechaza |
| 9 | `bacbaaa` | rechaza | rechaza | rechaza |
| 10 | `caabccbbccc` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `c`: {q0, q1, q2, q3, q4, q5} -c→ {q8} — ✔
  Árbol de cómputo: 3 caminos, 1 de aceptación:
    - q0 -λ→ q2 -λ→ q5 -c→ q8 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 — ✘ muere tras leer λ
2. `bc`: {q0, q1, q2, q3, q4, q5} -b→ {q1, q2, q3, q4, q5, q7, q9} -c→ {q8} — ✔
  Árbol de cómputo: 5 caminos, 1 de aceptación:
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q2 -λ→ q5 -c→ q8 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `b`
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q4 — ✘ muere tras leer `b`
    - q0 -λ→ q2 -λ→ q5 — ✘ muere tras leer λ
3. `bac`: {q0, q1, q2, q3, q4, q5} -b→ {q1, q2, q3, q4, q5, q7, q9} -a→ {q1, q2, q3, q4, q5, q6, q9} -c→ {q8} — ✔
  Árbol de cómputo: 7 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q2 -λ→ q5 -c→ q8 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `ba`
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q4 — ✘ muere tras leer `ba`
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q4 — ✘ muere tras leer `b`
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q2 -λ→ q5 — ✘ muere tras leer `b`
4. `abac`: {q0, q1, q2, q3, q4, q5} -a→ {q1, q2, q3, q4, q5, q6, q9} -b→ {q1, q2, q3, q4, q5, q7, q9} -a→ {q1, q2, q3, q4, q5, q6, q9} -c→ {q8} — ✔
  Árbol de cómputo: 9 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q2 -λ→ q5 -c→ q8 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `a`
    - q0 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `aba`
    - q0 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q4 — ✘ muere tras leer `aba`
    - q0 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q4 — ✘ muere tras leer `ab`
    - q0 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q2 -λ→ q5 — ✘ muere tras leer `ab`
5. `babaac`: {q0, q1, q2, q3, q4, q5} -b→ {q1, q2, q3, q4, q5, q7, q9} -a→ {q1, q2, q3, q4, q5, q6, q9} -b→ {q1, q2, q3, q4, q5, q7, q9} -a→ {q1, q2, q3, q4, q5, q6, q9} -a→ {q1, q2, q3, q4, q5, q6, q9} -c→ {q8} — ✔
  Árbol de cómputo: 13 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q2 -λ→ q5 -c→ q8 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `ba`
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `babaa`
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q4 — ✘ muere tras leer `babaa`
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q4 — ✘ muere tras leer `baba`
6. λ: {q0, q1, q2, q3, q4, q5} — ✘
  Árbol de cómputo: 6 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
    - q0 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 — ✘ termina fuera de F
    - q0 -λ→ q2 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q5 — ✘ termina fuera de F
7. `bb`: {q0, q1, q2, q3, q4, q5} -b→ {q1, q2, q3, q4, q5, q7, q9} -b→ {q1, q2, q3, q4, q5, q7, q9} — ✘
  Árbol de cómputo: 11 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `b`
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -b→ q7 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ termina fuera de F
8. `bbaca`: {q0, q1, q2, q3, q4, q5} -b→ {q1, q2, q3, q4, q5, q7, q9} -b→ {q1, q2, q3, q4, q5, q7, q9} -a→ {q1, q2, q3, q4, q5, q6, q9} -c→ {q8} -a→ ∅ — ✘
  Árbol de cómputo: 9 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `b`
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `bba`
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q4 — ✘ muere tras leer `bba`
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q2 -λ→ q5 -c→ q8 — ✘ muere tras leer `bbac`
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q4 — ✘ muere tras leer `bb`
9. `bacbaaa`: {q0, q1, q2, q3, q4, q5} -b→ {q1, q2, q3, q4, q5, q7, q9} -a→ {q1, q2, q3, q4, q5, q6, q9} -c→ {q8} -b→ ∅ -a→ ∅ -a→ ∅ -a→ ∅ — ✘
  Árbol de cómputo: 7 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `ba`
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q1 -λ→ q4 — ✘ muere tras leer `ba`
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q9 -λ→ q2 -λ→ q5 -c→ q8 — ✘ muere tras leer `bac`
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q1 -λ→ q4 — ✘ muere tras leer `b`
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q9 -λ→ q2 -λ→ q5 — ✘ muere tras leer `b`
10. `caabccbbccc`: {q0, q1, q2, q3, q4, q5} -c→ {q8} -a→ ∅ -a→ ∅ -b→ ∅ -c→ ∅ -c→ ∅ -b→ ∅ -b→ ∅ -c→ ∅ -c→ ∅ -c→ ∅ — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q5 -c→ q8 — ✘ muere tras leer `c`

</details>

Simulación paso a paso en JFLAP con `bc`: [ver captura](../../evidencias/jflap/pasos/L3-VF-219.png).

**Conversión.** AFND-λ (10 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 10 estados, [`L3-VF-219-AFND.jff`](../../automatas/conversiones/L3-VF-219-AFND.jff). AFND (10 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 4 estados, [`L3-VF-219-AFD.jff`](../../automatas/conversiones/L3-VF-219-AFD.jff) ([.json](../../automatas/conversiones/L3-VF-219-AFD.json), [.xml](../../automatas/conversiones/L3-VF-219-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 5 estados, y el AFD mínimo (Hopcroft), 3. La cota es 2^10 = 1024. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-220"></a>

## Lista 3, problema 220

**Enunciado.** ¿Es verdadera la afirmación «w ∈ L((a+b)*c*)»? Afirmaciones 220.

**Clasificación: AFND-λ.** Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

| Afirmación | Cadena | Expresión | AFND-λ de Thompson | Respuesta | Razón |
|---|---|---|---|---|---|
| 220 | `ab` | `(a+b)*c*` | acepta | **V** | ab y c⁰. |

#### AFND-λ de Thompson de (a+b)*c* — `L3-VF-220`

Archivos: [`L3-VF-220.jff`](../../automatas/lista3-afnd-lambda/L3-VF-220.jff) · [`L3-VF-220.json`](../../automatas/lista3-afnd-lambda/L3-VF-220.json) · [`L3-VF-220.xml`](../../automatas/lista3-afnd-lambda/L3-VF-220.xml). Tipo según la definición: **AFND-lambda**, |Q| = 12, Σ = {a, b, c}, 16 transiciones.

**Diseño.** Construcción de Thompson sobre Σ = {a, b, c}: cada símbolo es un fragmento i -a→ f; la unión y la estrella agregan un estado inicial y uno final unidos con λ, y la concatenación une fragmentos con λ.

| Estado | a | b | c | λ |
|---|---|---|---|---|
| →q0 | ∅ | ∅ | ∅ | {q1, q2} |
| q1 | ∅ | ∅ | ∅ | {q3, q4} |
| q3 | {q6} | ∅ | ∅ | ∅ |
| q6 | ∅ | ∅ | ∅ | {q10} |
| q4 | ∅ | {q7} | ∅ | ∅ |
| q7 | ∅ | ∅ | ∅ | {q10} |
| q10 | ∅ | ∅ | ∅ | {q1, q2} |
| q2 | ∅ | ∅ | ∅ | {q5} |
| q5 | ∅ | ∅ | ∅ | {q8, q9} |
| q9 | ∅ | ∅ | {q11} | ∅ |
| q11 | ∅ | ∅ | ∅ | {q8, q9} |
| *q8 | ∅ | ∅ | ∅ | ∅ |

**Transiciones λ.** Las λ son las de la construcción de Thompson: en la unión eligen una alternativa, en la estrella permiten repetir o saltar el fragmento y en la concatenación enlazan fragmentos.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0, q1, q2, q3, q4, q5, q8, q9} | sí |
| q1 | {q1, q3, q4} | no |
| q3 | {q3} | no |
| q6 | {q1, q10, q2, q3, q4, q5, q6, q8, q9} | sí |
| q4 | {q4} | no |
| q7 | {q1, q10, q2, q3, q4, q5, q7, q8, q9} | sí |
| q10 | {q1, q10, q2, q3, q4, q5, q8, q9} | sí |
| q2 | {q2, q5, q8, q9} | sí |
| q5 | {q5, q8, q9} | sí |
| q9 | {q9} | no |
| q11 | {q11, q8, q9} | sí |
| q8 | {q8} | sí |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | acepta | acepta | acepta |
| 2 | `aa` | acepta | acepta | acepta |
| 3 | `cccc` | acepta | acepta | acepta |
| 4 | `ccccccc` | acepta | acepta | acepta |
| 5 | `bcccccccccc` | acepta | acepta | acepta |
| 6 | `ca` | rechaza | rechaza | rechaza |
| 7 | `baca` | rechaza | rechaza | rechaza |
| 8 | `cbca` | rechaza | rechaza | rechaza |
| 9 | `bcabbcb` | rechaza | rechaza | rechaza |
| 10 | `bbbbbcabccc` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: {q0, q1, q2, q3, q4, q5, q8, q9} — ✔
  Árbol de cómputo: 8 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q2 -λ→ q5 -λ→ q8 — ✔ acepta
    - q0 — ✘ termina fuera de F
    - q0 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 — ✘ termina fuera de F
    - q0 -λ→ q2 — ✘ termina fuera de F
2. `aa`: {q0, q1, q2, q3, q4, q5, q8, q9} -a→ {q1, q10, q2, q3, q4, q5, q6, q8, q9} -a→ {q1, q10, q2, q3, q4, q5, q6, q8, q9} — ✔
  Árbol de cómputo: 15 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q10 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q10 -λ→ q2 -λ→ q5 -λ→ q8 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q10 -λ→ q1 -λ→ q3 -a→ q6 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q10 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q10 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q10 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q10 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q10 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q10 -λ→ q1 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q10 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q10 -λ→ q1 -λ→ q4 — ✘ termina fuera de F
3. `cccc`: {q0, q1, q2, q3, q4, q5, q8, q9} -c→ {q11, q8, q9} -c→ {q11, q8, q9} -c→ {q11, q8, q9} -c→ {q11, q8, q9} — ✔
  Árbol de cómputo: 9 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q2 -λ→ q5 -λ→ q9 -c→ q11 -λ→ q9 -c→ q11 -λ→ q9 -c→ q11 -λ→ q9 -c→ q11 -λ→ q8 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q5 -λ→ q8 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q5 -λ→ q9 -c→ q11 -λ→ q8 — ✘ muere tras leer `c`
    - q0 -λ→ q2 -λ→ q5 -λ→ q9 -c→ q11 -λ→ q9 -c→ q11 -λ→ q8 — ✘ muere tras leer `cc`
4. `ccccccc`: {q0, q1, q2, q3, q4, q5, q8, q9} -c→ {q11, q8, q9} -c→ {q11, q8, q9} -c→ {q11, q8, q9} -c→ {q11, q8, q9} -c→ {q11, q8, q9} -c→ {q11, q8, q9} -c→ {q11, q8, q9} — ✔
  Árbol de cómputo: 12 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q2 -λ→ q5 -λ→ q9 -c→ q11 -λ→ q9 -c→ q11 -λ→ q9 -c→ q11 -λ→ q9 -c→ q11 -λ→ q9 -c→ q11 -λ→ q9 -c→ q11 -λ→ q9 -c→ q11 -λ→ q8 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q5 -λ→ q8 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q5 -λ→ q9 -c→ q11 -λ→ q8 — ✘ muere tras leer `c`
    - q0 -λ→ q2 -λ→ q5 -λ→ q9 -c→ q11 -λ→ q9 -c→ q11 -λ→ q8 — ✘ muere tras leer `cc`
5. `bcccccccccc`: {q0, q1, q2, q3, q4, q5, q8, q9} -b→ {q1, q10, q2, q3, q4, q5, q7, q8, q9} -c→ {q11, q8, q9} -c→ {q11, q8, q9} -c→ {q11, q8, q9} -c→ {q11, q8, q9} -c→ {q11, q8, q9} -c→ {q11, q8, q9} -c→ {q11, q8, q9} -c→ {q11, q8, q9} -c→ {q11, q8, q9} -c→ {q11, q8, q9} — ✔
  Árbol de cómputo: 18 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q10 -λ→ q2 -λ→ q5 -λ→ q9 -c→ q11 -λ→ q9 -c→ q11 -λ→ q9 -c→ q11 -λ→ q9 -c→ q11 -λ→ q9 -c→ q11 -λ→ q9 -c→ q11 -λ→ q9 -c→ q11 -λ→ q9 -c→ q11 -λ→ q9 -c→ q11 -λ→ q9 -c→ q11 -λ→ q8 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q10 -λ→ q1 -λ→ q3 — ✘ muere tras leer `b`
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q10 -λ→ q1 -λ→ q4 — ✘ muere tras leer `b`
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q10 -λ→ q2 -λ→ q5 -λ→ q8 — ✘ muere tras leer `b`
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q10 -λ→ q2 -λ→ q5 -λ→ q9 -c→ q11 -λ→ q8 — ✘ muere tras leer `bc`
6. `ca`: {q0, q1, q2, q3, q4, q5, q8, q9} -c→ {q11, q8, q9} -a→ ∅ — ✘
  Árbol de cómputo: 5 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q5 -λ→ q8 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q5 -λ→ q9 -c→ q11 -λ→ q8 — ✘ muere tras leer `c`
    - q0 -λ→ q2 -λ→ q5 -λ→ q9 -c→ q11 -λ→ q9 — ✘ muere tras leer `c`
7. `baca`: {q0, q1, q2, q3, q4, q5, q8, q9} -b→ {q1, q10, q2, q3, q4, q5, q7, q8, q9} -a→ {q1, q10, q2, q3, q4, q5, q6, q8, q9} -c→ {q11, q8, q9} -a→ ∅ — ✘
  Árbol de cómputo: 11 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q10 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q10 -λ→ q1 -λ→ q3 — ✘ muere tras leer `ba`
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q10 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q10 -λ→ q1 -λ→ q4 — ✘ muere tras leer `ba`
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q10 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q10 -λ→ q2 -λ→ q5 -λ→ q8 — ✘ muere tras leer `ba`
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q10 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q10 -λ→ q2 -λ→ q5 -λ→ q9 -c→ q11 -λ→ q8 — ✘ muere tras leer `bac`
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q10 -λ→ q1 -λ→ q3 -a→ q6 -λ→ q10 -λ→ q2 -λ→ q5 -λ→ q9 -c→ q11 -λ→ q9 — ✘ muere tras leer `bac`
8. `cbca`: {q0, q1, q2, q3, q4, q5, q8, q9} -c→ {q11, q8, q9} -b→ ∅ -c→ ∅ -a→ ∅ — ✘
  Árbol de cómputo: 5 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q5 -λ→ q8 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q5 -λ→ q9 -c→ q11 -λ→ q8 — ✘ muere tras leer `c`
    - q0 -λ→ q2 -λ→ q5 -λ→ q9 -c→ q11 -λ→ q9 — ✘ muere tras leer `c`
9. `bcabbcb`: {q0, q1, q2, q3, q4, q5, q8, q9} -b→ {q1, q10, q2, q3, q4, q5, q7, q8, q9} -c→ {q11, q8, q9} -a→ ∅ -b→ ∅ -b→ ∅ -c→ ∅ -b→ ∅ — ✘
  Árbol de cómputo: 8 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q10 -λ→ q1 -λ→ q3 — ✘ muere tras leer `b`
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q10 -λ→ q1 -λ→ q4 — ✘ muere tras leer `b`
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q10 -λ→ q2 -λ→ q5 -λ→ q8 — ✘ muere tras leer `b`
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q10 -λ→ q2 -λ→ q5 -λ→ q9 -c→ q11 -λ→ q8 — ✘ muere tras leer `bc`
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q10 -λ→ q2 -λ→ q5 -λ→ q9 -c→ q11 -λ→ q9 — ✘ muere tras leer `bc`
10. `bbbbbcabccc`: {q0, q1, q2, q3, q4, q5, q8, q9} -b→ {q1, q10, q2, q3, q4, q5, q7, q8, q9} -b→ {q1, q10, q2, q3, q4, q5, q7, q8, q9} -b→ {q1, q10, q2, q3, q4, q5, q7, q8, q9} -b→ {q1, q10, q2, q3, q4, q5, q7, q8, q9} -b→ {q1, q10, q2, q3, q4, q5, q7, q8, q9} -c→ {q11, q8, q9} -a→ ∅ -b→ ∅ -c→ ∅ -c→ ∅ -c→ ∅ — ✘
  Árbol de cómputo: 20 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q10 -λ→ q1 -λ→ q3 — ✘ muere tras leer `b`
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q10 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q10 -λ→ q1 -λ→ q3 — ✘ muere tras leer `bb`
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q10 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q10 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q10 -λ→ q1 -λ→ q3 — ✘ muere tras leer `bbb`
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q10 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q10 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q10 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q10 -λ→ q1 -λ→ q3 — ✘ muere tras leer `bbbb`
    - q0 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q10 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q10 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q10 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q10 -λ→ q1 -λ→ q4 -b→ q7 -λ→ q10 -λ→ q1 -λ→ q3 — ✘ muere tras leer `bbbbb`

</details>

Simulación paso a paso en JFLAP con `aa`: [ver captura](../../evidencias/jflap/pasos/L3-VF-220.png).

**Conversión.** AFND-λ (12 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 12 estados, [`L3-VF-220-AFND.jff`](../../automatas/conversiones/L3-VF-220-AFND.jff). AFND (12 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 4 estados, [`L3-VF-220-AFD.jff`](../../automatas/conversiones/L3-VF-220-AFD.jff) ([.json](../../automatas/conversiones/L3-VF-220-AFD.json), [.xml](../../automatas/conversiones/L3-VF-220-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 5 estados, y el AFD mínimo (Hopcroft), 3. La cota es 2^12 = 4096. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-223"></a>

## Lista 3, problema 223

**Enunciado.** ¿Es verdadera la afirmación «w ∈ L(a*b*)»? Afirmaciones 223.

**Clasificación: AFND-λ.** Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

| Afirmación | Cadena | Expresión | AFND-λ de Thompson | Respuesta | Razón |
|---|---|---|---|---|---|
| 223 | `aa` | `a*b*` | acepta | **V** | a² y b⁰. |

#### AFND-λ de Thompson de a*b* — `L3-VF-223`

Archivos: [`L3-VF-223.jff`](../../automatas/lista3-afnd-lambda/L3-VF-223.jff) · [`L3-VF-223.json`](../../automatas/lista3-afnd-lambda/L3-VF-223.json) · [`L3-VF-223.xml`](../../automatas/lista3-afnd-lambda/L3-VF-223.xml). Tipo según la definición: **AFND-lambda**, |Q| = 8, Σ = {a, b, c}, 11 transiciones.

**Diseño.** Construcción de Thompson sobre Σ = {a, b, c}: cada símbolo es un fragmento i -a→ f; la unión y la estrella agregan un estado inicial y uno final unidos con λ, y la concatenación une fragmentos con λ.

| Estado | a | b | c | λ |
|---|---|---|---|---|
| →q0 | ∅ | ∅ | ∅ | {q1, q2} |
| q1 | {q3} | ∅ | ∅ | ∅ |
| q3 | ∅ | ∅ | ∅ | {q1, q2} |
| q2 | ∅ | ∅ | ∅ | {q4} |
| q4 | ∅ | ∅ | ∅ | {q5, q6} |
| q5 | ∅ | {q7} | ∅ | ∅ |
| q7 | ∅ | ∅ | ∅ | {q5, q6} |
| *q6 | ∅ | ∅ | ∅ | ∅ |

**Transiciones λ.** Las λ son las de la construcción de Thompson: en la unión eligen una alternativa, en la estrella permiten repetir o saltar el fragmento y en la concatenación enlazan fragmentos.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0, q1, q2, q4, q5, q6} | sí |
| q1 | {q1} | no |
| q3 | {q1, q2, q3, q4, q5, q6} | sí |
| q2 | {q2, q4, q5, q6} | sí |
| q4 | {q4, q5, q6} | sí |
| q5 | {q5} | no |
| q7 | {q5, q6, q7} | sí |
| q6 | {q6} | sí |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | acepta | acepta | acepta |
| 2 | `ab` | acepta | acepta | acepta |
| 3 | `bbbb` | acepta | acepta | acepta |
| 4 | `bbbbbbb` | acepta | acepta | acepta |
| 5 | `bbbbbbbbbbb` | acepta | acepta | acepta |
| 6 | `c` | rechaza | rechaza | rechaza |
| 7 | `ca` | rechaza | rechaza | rechaza |
| 8 | `aaaba` | rechaza | rechaza | rechaza |
| 9 | `bbbcaca` | rechaza | rechaza | rechaza |
| 10 | `acbcacaaabc` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: {q0, q1, q2, q4, q5, q6} — ✔
  Árbol de cómputo: 6 caminos, 1 de aceptación:
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 — ✔ acepta
    - q0 — ✘ termina fuera de F
    - q0 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q2 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q4 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q4 -λ→ q5 — ✘ termina fuera de F
2. `ab`: {q0, q1, q2, q4, q5, q6} -a→ {q1, q2, q3, q4, q5, q6} -b→ {q5, q6, q7} — ✔
  Árbol de cómputo: 7 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -a→ q3 -λ→ q2 -λ→ q4 -λ→ q5 -b→ q7 -λ→ q6 — ✔ acepta
    - q0 -λ→ q1 -a→ q3 -λ→ q1 — ✘ muere tras leer `a`
    - q0 -λ→ q1 -a→ q3 -λ→ q2 -λ→ q4 -λ→ q5 -b→ q7 — ✘ termina fuera de F
    - q0 -λ→ q1 -a→ q3 -λ→ q2 -λ→ q4 -λ→ q5 -b→ q7 -λ→ q5 — ✘ termina fuera de F
    - q0 -λ→ q1 -a→ q3 -λ→ q2 -λ→ q4 -λ→ q6 — ✘ muere tras leer `a`
    - q0 -λ→ q2 -λ→ q4 -λ→ q5 — ✘ muere tras leer λ
3. `bbbb`: {q0, q1, q2, q4, q5, q6} -b→ {q5, q6, q7} -b→ {q5, q6, q7} -b→ {q5, q6, q7} -b→ {q5, q6, q7} — ✔
  Árbol de cómputo: 8 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q2 -λ→ q4 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q6 — ✔ acepta
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q4 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q4 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q4 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q6 — ✘ muere tras leer `bbb`
    - q0 -λ→ q2 -λ→ q4 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q6 — ✘ muere tras leer `bb`
4. `bbbbbbb`: {q0, q1, q2, q4, q5, q6} -b→ {q5, q6, q7} -b→ {q5, q6, q7} -b→ {q5, q6, q7} -b→ {q5, q6, q7} -b→ {q5, q6, q7} -b→ {q5, q6, q7} -b→ {q5, q6, q7} — ✔
  Árbol de cómputo: 11 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q2 -λ→ q4 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q6 — ✔ acepta
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q4 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q4 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q4 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q6 — ✘ muere tras leer `bbbbbb`
    - q0 -λ→ q2 -λ→ q4 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q6 — ✘ muere tras leer `bbbbb`
5. `bbbbbbbbbbb`: {q0, q1, q2, q4, q5, q6} -b→ {q5, q6, q7} -b→ {q5, q6, q7} -b→ {q5, q6, q7} -b→ {q5, q6, q7} -b→ {q5, q6, q7} -b→ {q5, q6, q7} -b→ {q5, q6, q7} -b→ {q5, q6, q7} -b→ {q5, q6, q7} -b→ {q5, q6, q7} -b→ {q5, q6, q7} — ✔
  Árbol de cómputo: 15 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q2 -λ→ q4 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q6 — ✔ acepta
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q4 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q4 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q4 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q6 — ✘ muere tras leer `bbbbbbbbbb`
    - q0 -λ→ q2 -λ→ q4 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q6 — ✘ muere tras leer `bbbbbbbbb`
6. `c`: {q0, q1, q2, q4, q5, q6} -c→ ∅ — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q4 -λ→ q5 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 — ✘ muere tras leer λ
7. `ca`: {q0, q1, q2, q4, q5, q6} -c→ ∅ -a→ ∅ — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q4 -λ→ q5 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 — ✘ muere tras leer λ
8. `aaaba`: {q0, q1, q2, q4, q5, q6} -a→ {q1, q2, q3, q4, q5, q6} -a→ {q1, q2, q3, q4, q5, q6} -a→ {q1, q2, q3, q4, q5, q6} -b→ {q5, q6, q7} -a→ ∅ — ✘
  Árbol de cómputo: 10 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 — ✘ muere tras leer `aaa`
    - q0 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q2 -λ→ q4 -λ→ q5 -b→ q7 -λ→ q5 — ✘ muere tras leer `aaab`
    - q0 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q2 -λ→ q4 -λ→ q5 -b→ q7 -λ→ q6 — ✘ muere tras leer `aaab`
    - q0 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q2 -λ→ q4 -λ→ q6 — ✘ muere tras leer `aaa`
    - q0 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q2 -λ→ q4 -λ→ q5 — ✘ muere tras leer `aa`
    - q0 -λ→ q1 -a→ q3 -λ→ q1 -a→ q3 -λ→ q2 -λ→ q4 -λ→ q6 — ✘ muere tras leer `aa`
9. `bbbcaca`: {q0, q1, q2, q4, q5, q6} -b→ {q5, q6, q7} -b→ {q5, q6, q7} -b→ {q5, q6, q7} -c→ ∅ -a→ ∅ -c→ ∅ -a→ ∅ — ✘
  Árbol de cómputo: 6 caminos, 0 de aceptación:
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q4 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 — ✘ muere tras leer `bbb`
    - q0 -λ→ q2 -λ→ q4 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q6 — ✘ muere tras leer `bbb`
    - q0 -λ→ q2 -λ→ q4 -λ→ q5 -b→ q7 -λ→ q5 -b→ q7 -λ→ q6 — ✘ muere tras leer `bb`
    - q0 -λ→ q2 -λ→ q4 -λ→ q5 -b→ q7 -λ→ q6 — ✘ muere tras leer `b`
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 — ✘ muere tras leer λ
10. `acbcacaaabc`: {q0, q1, q2, q4, q5, q6} -a→ {q1, q2, q3, q4, q5, q6} -c→ ∅ -b→ ∅ -c→ ∅ -a→ ∅ -c→ ∅ -a→ ∅ -a→ ∅ -a→ ∅ -b→ ∅ -c→ ∅ — ✘
  Árbol de cómputo: 5 caminos, 0 de aceptación:
    - q0 -λ→ q1 -a→ q3 -λ→ q1 — ✘ muere tras leer `a`
    - q0 -λ→ q1 -a→ q3 -λ→ q2 -λ→ q4 -λ→ q5 — ✘ muere tras leer `a`
    - q0 -λ→ q1 -a→ q3 -λ→ q2 -λ→ q4 -λ→ q6 — ✘ muere tras leer `a`
    - q0 -λ→ q2 -λ→ q4 -λ→ q5 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 — ✘ muere tras leer λ

</details>

Simulación paso a paso en JFLAP con `ab`: [ver captura](../../evidencias/jflap/pasos/L3-VF-223.png).

**Conversión.** AFND-λ (8 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 8 estados, [`L3-VF-223-AFND.jff`](../../automatas/conversiones/L3-VF-223-AFND.jff). AFND (8 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 3 estados, [`L3-VF-223-AFD.jff`](../../automatas/conversiones/L3-VF-223-AFD.jff) ([.json](../../automatas/conversiones/L3-VF-223-AFD.json), [.xml](../../automatas/conversiones/L3-VF-223-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 4 estados, y el AFD mínimo (Hopcroft), 3. La cota es 2^8 = 256. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-225"></a>

## Lista 3, problema 225

**Enunciado.** ¿Es verdadera la afirmación «w ∈ L(a(a+b)*)»? Afirmaciones 225.

**Clasificación: AFND-λ.** Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

| Afirmación | Cadena | Expresión | AFND-λ de Thompson | Respuesta | Razón |
|---|---|---|---|---|---|
| 225 | `aa` | `a(a+b)*` | acepta | **V** | a seguida de a. |

#### AFND-λ de Thompson de a(a+b)* — `L3-VF-225`

Archivos: [`L3-VF-225.jff`](../../automatas/lista3-afnd-lambda/L3-VF-225.jff) · [`L3-VF-225.json`](../../automatas/lista3-afnd-lambda/L3-VF-225.json) · [`L3-VF-225.xml`](../../automatas/lista3-afnd-lambda/L3-VF-225.xml). Tipo según la definición: **AFND-lambda**, |Q| = 10, Σ = {a, b, c}, 12 transiciones.

**Diseño.** Construcción de Thompson sobre Σ = {a, b, c}: cada símbolo es un fragmento i -a→ f; la unión y la estrella agregan un estado inicial y uno final unidos con λ, y la concatenación une fragmentos con λ.

| Estado | a | b | c | λ |
|---|---|---|---|---|
| →q0 | {q1} | ∅ | ∅ | ∅ |
| q1 | ∅ | ∅ | ∅ | {q2} |
| q2 | ∅ | ∅ | ∅ | {q3, q4} |
| q3 | ∅ | ∅ | ∅ | {q5, q6} |
| q5 | {q7} | ∅ | ∅ | ∅ |
| q7 | ∅ | ∅ | ∅ | {q9} |
| q6 | ∅ | {q8} | ∅ | ∅ |
| q8 | ∅ | ∅ | ∅ | {q9} |
| q9 | ∅ | ∅ | ∅ | {q3, q4} |
| *q4 | ∅ | ∅ | ∅ | ∅ |

**Transiciones λ.** Las λ son las de la construcción de Thompson: en la unión eligen una alternativa, en la estrella permiten repetir o saltar el fragmento y en la concatenación enlazan fragmentos.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0} | no |
| q1 | {q1, q2, q3, q4, q5, q6} | sí |
| q2 | {q2, q3, q4, q5, q6} | sí |
| q3 | {q3, q5, q6} | no |
| q5 | {q5} | no |
| q7 | {q3, q4, q5, q6, q7, q9} | sí |
| q6 | {q6} | no |
| q8 | {q3, q4, q5, q6, q8, q9} | sí |
| q9 | {q3, q4, q5, q6, q9} | sí |
| q4 | {q4} | sí |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `a` | acepta | acepta | acepta |
| 2 | `aa` | acepta | acepta | acepta |
| 3 | `abbb` | acepta | acepta | acepta |
| 4 | `aababab` | acepta | acepta | acepta |
| 5 | `ababbbababa` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `ca` | rechaza | rechaza | rechaza |
| 8 | `babc` | rechaza | rechaza | rechaza |
| 9 | `bccbcab` | rechaza | rechaza | rechaza |
| 10 | `cbcbacbcbaa` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `a`: {q0} -a→ {q1, q2, q3, q4, q5, q6} — ✔
  Árbol de cómputo: 6 caminos, 1 de aceptación:
    - q0 -a→ q1 -λ→ q2 -λ→ q4 — ✔ acepta
    - q0 -a→ q1 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q3 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q5 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q6 — ✘ termina fuera de F
2. `aa`: {q0} -a→ {q1, q2, q3, q4, q5, q6} -a→ {q3, q4, q5, q6, q7, q9} — ✔
  Árbol de cómputo: 8 caminos, 1 de aceptación (se muestran 6):
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -a→ q7 -λ→ q9 -λ→ q4 — ✔ acepta
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -a→ q7 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -a→ q7 -λ→ q9 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -a→ q7 -λ→ q9 -λ→ q3 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -a→ q7 -λ→ q9 -λ→ q3 -λ→ q5 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -a→ q7 -λ→ q9 -λ→ q3 -λ→ q6 — ✘ termina fuera de F
3. `abbb`: {q0} -a→ {q1, q2, q3, q4, q5, q6} -b→ {q3, q4, q5, q6, q8, q9} -b→ {q3, q4, q5, q6, q8, q9} -b→ {q3, q4, q5, q6, q8, q9} — ✔
  Árbol de cómputo: 12 caminos, 1 de aceptación (se muestran 6):
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q6 -b→ q8 -λ→ q9 -λ→ q3 -λ→ q6 -b→ q8 -λ→ q9 -λ→ q3 -λ→ q6 -b→ q8 -λ→ q9 -λ→ q4 — ✔ acepta
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q5 — ✘ muere tras leer `a`
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q6 -b→ q8 -λ→ q9 -λ→ q3 -λ→ q5 — ✘ muere tras leer `ab`
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q6 -b→ q8 -λ→ q9 -λ→ q3 -λ→ q6 -b→ q8 -λ→ q9 -λ→ q3 -λ→ q5 — ✘ muere tras leer `abb`
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q6 -b→ q8 -λ→ q9 -λ→ q3 -λ→ q6 -b→ q8 -λ→ q9 -λ→ q3 -λ→ q6 -b→ q8 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q6 -b→ q8 -λ→ q9 -λ→ q3 -λ→ q6 -b→ q8 -λ→ q9 -λ→ q3 -λ→ q6 -b→ q8 -λ→ q9 — ✘ termina fuera de F
4. `aababab`: {q0} -a→ {q1, q2, q3, q4, q5, q6} -a→ {q3, q4, q5, q6, q7, q9} -b→ {q3, q4, q5, q6, q8, q9} -a→ {q3, q4, q5, q6, q7, q9} -b→ {q3, q4, q5, q6, q8, q9} -a→ {q3, q4, q5, q6, q7, q9} -b→ {q3, q4, q5, q6, q8, q9} — ✔
  Árbol de cómputo: 18 caminos, 1 de aceptación (se muestran 6):
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -a→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -b→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -a→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -b→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -a→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -b→ q8 -λ→ q9 -λ→ q4 — ✔ acepta
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -a→ q7 -λ→ q9 -λ→ q3 -λ→ q5 — ✘ muere tras leer `aa`
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -a→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -b→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -a→ q7 -λ→ q9 -λ→ q3 -λ→ q5 — ✘ muere tras leer `aaba`
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -a→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -b→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -a→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -b→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -a→ q7 -λ→ q9 -λ→ q3 -λ→ q5 — ✘ muere tras leer `aababa`
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -a→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -b→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -a→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -b→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -a→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -b→ q8 — ✘ termina fuera de F
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -a→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -b→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -a→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -b→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -a→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -b→ q8 -λ→ q9 — ✘ termina fuera de F
5. `ababbbababa`: {q0} -a→ {q1, q2, q3, q4, q5, q6} -b→ {q3, q4, q5, q6, q8, q9} -a→ {q3, q4, q5, q6, q7, q9} -b→ {q3, q4, q5, q6, q8, q9} -b→ {q3, q4, q5, q6, q8, q9} -b→ {q3, q4, q5, q6, q8, q9} -a→ {q3, q4, q5, q6, q7, q9} -b→ {q3, q4, q5, q6, q8, q9} -a→ {q3, q4, q5, q6, q7, q9} -b→ {q3, q4, q5, q6, q8, q9} -a→ {q3, q4, q5, q6, q7, q9} — ✔
  Árbol de cómputo: 26 caminos, 1 de aceptación (se muestran 6):
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q6 -b→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -a→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -b→ q8 -λ→ q9 -λ→ q3 -λ→ q6 -b→ q8 -λ→ q9 -λ→ q3 -λ→ q6 -b→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -a→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -b→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -a→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -b→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -a→ q7 -λ→ q9 -λ→ q4 — ✔ acepta
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q5 — ✘ muere tras leer `a`
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q6 -b→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -a→ q7 -λ→ q9 -λ→ q3 -λ→ q5 — ✘ muere tras leer `aba`
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q6 -b→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -a→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -b→ q8 -λ→ q9 -λ→ q3 -λ→ q5 — ✘ muere tras leer `abab`
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q6 -b→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -a→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -b→ q8 -λ→ q9 -λ→ q3 -λ→ q6 -b→ q8 -λ→ q9 -λ→ q3 -λ→ q5 — ✘ muere tras leer `ababb`
    - q0 -a→ q1 -λ→ q2 -λ→ q3 -λ→ q6 -b→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -a→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -b→ q8 -λ→ q9 -λ→ q3 -λ→ q6 -b→ q8 -λ→ q9 -λ→ q3 -λ→ q6 -b→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -a→ q7 -λ→ q9 -λ→ q3 -λ→ q5 — ✘ muere tras leer `ababbba`
6. λ: {q0} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
7. `ca`: {q0} -c→ ∅ -a→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ
8. `babc`: {q0} -b→ ∅ -a→ ∅ -b→ ∅ -c→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ
9. `bccbcab`: {q0} -b→ ∅ -c→ ∅ -c→ ∅ -b→ ∅ -c→ ∅ -a→ ∅ -b→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ
10. `cbcbacbcbaa`: {q0} -c→ ∅ -b→ ∅ -c→ ∅ -b→ ∅ -a→ ∅ -c→ ∅ -b→ ∅ -c→ ∅ -b→ ∅ -a→ ∅ -a→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ

</details>

Simulación paso a paso en JFLAP con `aa`: [ver captura](../../evidencias/jflap/pasos/L3-VF-225.png).

**Conversión.** AFND-λ (10 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 10 estados, [`L3-VF-225-AFND.jff`](../../automatas/conversiones/L3-VF-225-AFND.jff). AFND (10 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 4 estados, [`L3-VF-225-AFD.jff`](../../automatas/conversiones/L3-VF-225-AFD.jff) ([.json](../../automatas/conversiones/L3-VF-225-AFD.json), [.xml](../../automatas/conversiones/L3-VF-225-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 5 estados, y el AFD mínimo (Hopcroft), 3. La cota es 2^10 = 1024. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-226"></a>

## Lista 3, problema 226

**Enunciado.** ¿Es verdadera la afirmación «w ∈ L(a)»? Afirmaciones 226.

**Clasificación: AFND-λ.** Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

| Afirmación | Cadena | Expresión | AFND-λ de Thompson | Respuesta | Razón |
|---|---|---|---|---|---|
| 226 | λ | `a` | rechaza | **F** | L(a) = {a}. |

#### AFND-λ de Thompson de a — `L3-VF-226`

Archivos: [`L3-VF-226.jff`](../../automatas/lista3-afnd-lambda/L3-VF-226.jff) · [`L3-VF-226.json`](../../automatas/lista3-afnd-lambda/L3-VF-226.json) · [`L3-VF-226.xml`](../../automatas/lista3-afnd-lambda/L3-VF-226.xml). Tipo según la definición: **AFND**, |Q| = 2, Σ = {a, b, c}, 1 transiciones.

**Diseño.** Construcción de Thompson sobre Σ = {a, b, c}: cada símbolo es un fragmento i -a→ f; la unión y la estrella agregan un estado inicial y uno final unidos con λ, y la concatenación une fragmentos con λ.

| Estado | a | b | c |
|---|---|---|---|
| →q0 | q1 | — | — |
| *q1 | — | — | — |

**Transiciones λ.** La construcción de Thompson de una expresión sin operadores (un símbolo o ∅) no produce transiciones λ: el fragmento básico ya es el autómata completo.

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `a` | acepta | acepta | acepta |
| 2 | λ | rechaza | rechaza | rechaza |
| 3 | `cc` | rechaza | rechaza | rechaza |
| 4 | `aabc` | rechaza | rechaza | rechaza |
| 5 | `babbbcc` | rechaza | rechaza | rechaza |
| 6 | `bbbcaacbccc` | rechaza | rechaza | rechaza |

Nota sobre los casos: el lenguaje solo tiene 1 palabra.

<details><summary>Recorrido completo de cada cadena</summary>

1. `a`: q0 -a→ q1 — ✔
2. λ: q0 — ✘
3. `cc`: q0 -c→ (sin transición) — ✘
4. `aabc`: q0 -a→ q1 -a→ (sin transición) — ✘
5. `babbbcc`: q0 -b→ (sin transición) — ✘
6. `bbbcaacbccc`: q0 -b→ (sin transición) — ✘

</details>

Simulación paso a paso en JFLAP con `a`: [ver captura](../../evidencias/jflap/pasos/L3-VF-226.png).

**Conversión.** AFND (2 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 2 estados, [`L3-VF-226-AFD.jff`](../../automatas/conversiones/L3-VF-226-AFD.jff) ([.json](../../automatas/conversiones/L3-VF-226-AFD.json), [.xml](../../automatas/conversiones/L3-VF-226-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 3 estados, y el AFD mínimo (Hopcroft), 3. La cota es 2^2 = 4. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-228"></a>

## Lista 3, problema 228

**Enunciado.** ¿Es verdadera la afirmación «w ∈ L((a+b)*+a)»? Afirmaciones 228.

**Clasificación: AFND-λ.** Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

| Afirmación | Cadena | Expresión | AFND-λ de Thompson | Respuesta | Razón |
|---|---|---|---|---|---|
| 228 | λ | `(a+b)*+a` | acepta | **V** | λ ∈ L((a+b)*). |

#### AFND-λ de Thompson de (a+b)*+a — `L3-VF-228`

Archivos: [`L3-VF-228.jff`](../../automatas/lista3-afnd-lambda/L3-VF-228.jff) · [`L3-VF-228.json`](../../automatas/lista3-afnd-lambda/L3-VF-228.json) · [`L3-VF-228.xml`](../../automatas/lista3-afnd-lambda/L3-VF-228.xml). Tipo según la definición: **AFND-lambda**, |Q| = 12, Σ = {a, b, c}, 15 transiciones.

**Diseño.** Construcción de Thompson sobre Σ = {a, b, c}: cada símbolo es un fragmento i -a→ f; la unión y la estrella agregan un estado inicial y uno final unidos con λ, y la concatenación une fragmentos con λ.

| Estado | a | b | c | λ |
|---|---|---|---|---|
| →q0 | ∅ | ∅ | ∅ | {q1, q2} |
| q1 | ∅ | ∅ | ∅ | {q3, q4} |
| q3 | ∅ | ∅ | ∅ | {q6, q7} |
| q6 | {q9} | ∅ | ∅ | ∅ |
| q9 | ∅ | ∅ | ∅ | {q11} |
| q7 | ∅ | {q10} | ∅ | ∅ |
| q10 | ∅ | ∅ | ∅ | {q11} |
| q11 | ∅ | ∅ | ∅ | {q3, q4} |
| q4 | ∅ | ∅ | ∅ | {q8} |
| q2 | {q5} | ∅ | ∅ | ∅ |
| q5 | ∅ | ∅ | ∅ | {q8} |
| *q8 | ∅ | ∅ | ∅ | ∅ |

**Transiciones λ.** Las λ son las de la construcción de Thompson: en la unión eligen una alternativa, en la estrella permiten repetir o saltar el fragmento y en la concatenación enlazan fragmentos.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0, q1, q2, q3, q4, q6, q7, q8} | sí |
| q1 | {q1, q3, q4, q6, q7, q8} | sí |
| q3 | {q3, q6, q7} | no |
| q6 | {q6} | no |
| q9 | {q11, q3, q4, q6, q7, q8, q9} | sí |
| q7 | {q7} | no |
| q10 | {q10, q11, q3, q4, q6, q7, q8} | sí |
| q11 | {q11, q3, q4, q6, q7, q8} | sí |
| q4 | {q4, q8} | sí |
| q2 | {q2} | no |
| q5 | {q5, q8} | sí |
| q8 | {q8} | sí |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | acepta | acepta | acepta |
| 2 | `bb` | acepta | acepta | acepta |
| 3 | `aabb` | acepta | acepta | acepta |
| 4 | `aababbb` | acepta | acepta | acepta |
| 5 | `bbaaabbabbb` | acepta | acepta | acepta |
| 6 | `c` | rechaza | rechaza | rechaza |
| 7 | `aac` | rechaza | rechaza | rechaza |
| 8 | `aaac` | rechaza | rechaza | rechaza |
| 9 | `abcccbb` | rechaza | rechaza | rechaza |
| 10 | `ccccacccbaa` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: {q0, q1, q2, q3, q4, q6, q7, q8} — ✔
  Árbol de cómputo: 8 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 — ✔ acepta
    - q0 — ✘ termina fuera de F
    - q0 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -λ→ q6 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 — ✘ termina fuera de F
2. `bb`: {q0, q1, q2, q3, q4, q6, q7, q8} -b→ {q10, q11, q3, q4, q6, q7, q8} -b→ {q10, q11, q3, q4, q6, q7, q8} — ✔
  Árbol de cómputo: 12 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q4 -λ→ q8 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -λ→ q6 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 -λ→ q6 — ✘ muere tras leer `b`
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 — ✘ termina fuera de F
3. `aabb`: {q0, q1, q2, q3, q4, q6, q7, q8} -a→ {q11, q3, q4, q5, q6, q7, q8, q9} -a→ {q11, q3, q4, q6, q7, q8, q9} -b→ {q10, q11, q3, q4, q6, q7, q8} -b→ {q10, q11, q3, q4, q6, q7, q8} — ✔
  Árbol de cómputo: 16 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q4 -λ→ q8 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q6 — ✘ muere tras leer `aa`
    - q0 -λ→ q1 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 -λ→ q6 — ✘ muere tras leer `aab`
    - q0 -λ→ q1 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 — ✘ termina fuera de F
4. `aababbb`: {q0, q1, q2, q3, q4, q6, q7, q8} -a→ {q11, q3, q4, q5, q6, q7, q8, q9} -a→ {q11, q3, q4, q6, q7, q8, q9} -b→ {q10, q11, q3, q4, q6, q7, q8} -a→ {q11, q3, q4, q6, q7, q8, q9} -b→ {q10, q11, q3, q4, q6, q7, q8} -b→ {q10, q11, q3, q4, q6, q7, q8} -b→ {q10, q11, q3, q4, q6, q7, q8} — ✔
  Árbol de cómputo: 22 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q4 -λ→ q8 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q6 — ✘ muere tras leer `aa`
    - q0 -λ→ q1 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q6 — ✘ muere tras leer `aaba`
    - q0 -λ→ q1 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 -λ→ q6 — ✘ muere tras leer `aabab`
    - q0 -λ→ q1 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 -λ→ q6 — ✘ muere tras leer `aababb`
    - q0 -λ→ q1 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 — ✘ termina fuera de F
5. `bbaaabbabbb`: {q0, q1, q2, q3, q4, q6, q7, q8} -b→ {q10, q11, q3, q4, q6, q7, q8} -b→ {q10, q11, q3, q4, q6, q7, q8} -a→ {q11, q3, q4, q6, q7, q8, q9} -a→ {q11, q3, q4, q6, q7, q8, q9} -a→ {q11, q3, q4, q6, q7, q8, q9} -b→ {q10, q11, q3, q4, q6, q7, q8} -b→ {q10, q11, q3, q4, q6, q7, q8} -a→ {q11, q3, q4, q6, q7, q8, q9} -b→ {q10, q11, q3, q4, q6, q7, q8} -b→ {q10, q11, q3, q4, q6, q7, q8} -b→ {q10, q11, q3, q4, q6, q7, q8} — ✔
  Árbol de cómputo: 30 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q4 -λ→ q8 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -λ→ q6 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 -λ→ q6 — ✘ muere tras leer `b`
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q6 — ✘ muere tras leer `bbaaa`
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 -λ→ q6 — ✘ muere tras leer `bbaaab`
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q6 — ✘ muere tras leer `bbaaabba`
6. `c`: {q0, q1, q2, q3, q4, q6, q7, q8} -c→ ∅ — ✘
  Árbol de cómputo: 4 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q3 -λ→ q6 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 — ✘ muere tras leer λ
    - q0 -λ→ q2 — ✘ muere tras leer λ
7. `aac`: {q0, q1, q2, q3, q4, q6, q7, q8} -a→ {q11, q3, q4, q5, q6, q7, q8, q9} -a→ {q11, q3, q4, q6, q7, q8, q9} -c→ ∅ — ✘
  Árbol de cómputo: 8 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q6 — ✘ muere tras leer `aa`
    - q0 -λ→ q1 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q7 — ✘ muere tras leer `aa`
    - q0 -λ→ q1 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q4 -λ→ q8 — ✘ muere tras leer `aa`
    - q0 -λ→ q1 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q7 — ✘ muere tras leer `a`
    - q0 -λ→ q1 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q4 -λ→ q8 — ✘ muere tras leer `a`
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 — ✘ muere tras leer λ
8. `aaac`: {q0, q1, q2, q3, q4, q6, q7, q8} -a→ {q11, q3, q4, q5, q6, q7, q8, q9} -a→ {q11, q3, q4, q6, q7, q8, q9} -a→ {q11, q3, q4, q6, q7, q8, q9} -c→ ∅ — ✘
  Árbol de cómputo: 10 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q6 — ✘ muere tras leer `aaa`
    - q0 -λ→ q1 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q7 — ✘ muere tras leer `aaa`
    - q0 -λ→ q1 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q4 -λ→ q8 — ✘ muere tras leer `aaa`
    - q0 -λ→ q1 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q7 — ✘ muere tras leer `aa`
    - q0 -λ→ q1 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q4 -λ→ q8 — ✘ muere tras leer `aa`
    - q0 -λ→ q1 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q7 — ✘ muere tras leer `a`
9. `abcccbb`: {q0, q1, q2, q3, q4, q6, q7, q8} -a→ {q11, q3, q4, q5, q6, q7, q8, q9} -b→ {q10, q11, q3, q4, q6, q7, q8} -c→ ∅ -c→ ∅ -c→ ∅ -b→ ∅ -b→ ∅ — ✘
  Árbol de cómputo: 8 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q6 — ✘ muere tras leer `a`
    - q0 -λ→ q1 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 -λ→ q6 — ✘ muere tras leer `ab`
    - q0 -λ→ q1 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q3 -λ→ q7 — ✘ muere tras leer `ab`
    - q0 -λ→ q1 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q3 -λ→ q7 -b→ q10 -λ→ q11 -λ→ q4 -λ→ q8 — ✘ muere tras leer `ab`
    - q0 -λ→ q1 -λ→ q3 -λ→ q6 -a→ q9 -λ→ q11 -λ→ q4 -λ→ q8 — ✘ muere tras leer `a`
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 — ✘ muere tras leer λ
10. `ccccacccbaa`: {q0, q1, q2, q3, q4, q6, q7, q8} -c→ ∅ -c→ ∅ -c→ ∅ -c→ ∅ -a→ ∅ -c→ ∅ -c→ ∅ -c→ ∅ -b→ ∅ -a→ ∅ -a→ ∅ — ✘
  Árbol de cómputo: 4 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q3 -λ→ q6 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 — ✘ muere tras leer λ
    - q0 -λ→ q2 — ✘ muere tras leer λ

</details>

Simulación paso a paso en JFLAP con `bb`: [ver captura](../../evidencias/jflap/pasos/L3-VF-228.png).

**Conversión.** AFND-λ (12 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 10 estados, [`L3-VF-228-AFND.jff`](../../automatas/conversiones/L3-VF-228-AFND.jff). AFND (10 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 4 estados, [`L3-VF-228-AFD.jff`](../../automatas/conversiones/L3-VF-228-AFD.jff) ([.json](../../automatas/conversiones/L3-VF-228-AFD.json), [.xml](../../automatas/conversiones/L3-VF-228-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 5 estados, y el AFD mínimo (Hopcroft), 2. La cota es 2^10 = 1024. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-229-235"></a>

## Lista 3, problema 229, 235

**Enunciado.** ¿Es verdadera la afirmación «w ∈ L(∅)»? Afirmaciones 229, 235.

**Clasificación: AFND-λ.** Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena.

| Afirmación | Cadena | Expresión | AFND-λ de Thompson | Respuesta | Razón |
|---|---|---|---|---|---|
| 229 | λ | `∅` | rechaza | **F** | L(∅) no tiene palabras. |
| 235 | ∅ (no es cadena) | `∅` | — | **F** | ∅ no es una cadena: es el conjunto vacío. L(∅) = ∅ no tiene elementos, y aun si se leyera como «λ ∈ L(∅)», L(∅) no contiene ninguna cadena. Es falso. |

#### AFND-λ de Thompson de ∅ — `L3-VF-229`

Archivos: [`L3-VF-229.jff`](../../automatas/lista3-afnd-lambda/L3-VF-229.jff) · [`L3-VF-229.json`](../../automatas/lista3-afnd-lambda/L3-VF-229.json) · [`L3-VF-229.xml`](../../automatas/lista3-afnd-lambda/L3-VF-229.xml). Tipo según la definición: **AFND**, |Q| = 2, Σ = {a, b, c}, 0 transiciones.

**Diseño.** Construcción de Thompson sobre Σ = {a, b, c}: cada símbolo es un fragmento i -a→ f; la unión y la estrella agregan un estado inicial y uno final unidos con λ, y la concatenación une fragmentos con λ.

| Estado | a | b | c |
|---|---|---|---|
| →q0 | — | — | — |
| *q1 | — | — | — |

**Transiciones λ.** La construcción de Thompson de una expresión sin operadores (un símbolo o ∅) no produce transiciones λ: el fragmento básico ya es el autómata completo.

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | rechaza | rechaza | rechaza |
| 2 | `cb` | rechaza | rechaza | rechaza |
| 3 | `ccca` | rechaza | rechaza | rechaza |
| 4 | `bbbcabb` | rechaza | rechaza | rechaza |
| 5 | `cababcbcacb` | rechaza | rechaza | rechaza |

Nota sobre los casos: el lenguaje solo tiene 0 palabras.

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: q0 — ✘
2. `cb`: q0 -c→ (sin transición) — ✘
3. `ccca`: q0 -c→ (sin transición) — ✘
4. `bbbcabb`: q0 -b→ (sin transición) — ✘
5. `cababcbcacb`: q0 -c→ (sin transición) — ✘

</details>

Simulación paso a paso en JFLAP con `cb`: [ver captura](../../evidencias/jflap/pasos/L3-VF-229.png).

**Conversión.** AFND (2 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 2 estados, [`L3-VF-229-AFD.jff`](../../automatas/conversiones/L3-VF-229-AFD.jff) ([.json](../../automatas/conversiones/L3-VF-229-AFD.json), [.xml](../../automatas/conversiones/L3-VF-229-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 2 estados, y el AFD mínimo (Hopcroft), 1. La cota es 2^2 = 4. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-230"></a>

## Lista 3, problema 230

**Enunciado.** ¿Es verdadera la afirmación «w ∈ L(λ)»? Afirmaciones 230.

**Clasificación: AFND-λ.** Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

| Afirmación | Cadena | Expresión | AFND-λ de Thompson | Respuesta | Razón |
|---|---|---|---|---|---|
| 230 | λ | `λ` | acepta | **V** | L(λ) = {λ}. |

#### AFND-λ de Thompson de λ — `L3-VF-230`

Archivos: [`L3-VF-230.jff`](../../automatas/lista3-afnd-lambda/L3-VF-230.jff) · [`L3-VF-230.json`](../../automatas/lista3-afnd-lambda/L3-VF-230.json) · [`L3-VF-230.xml`](../../automatas/lista3-afnd-lambda/L3-VF-230.xml). Tipo según la definición: **AFND-lambda**, |Q| = 2, Σ = {a, b, c}, 1 transiciones.

**Diseño.** Construcción de Thompson sobre Σ = {a, b, c}: cada símbolo es un fragmento i -a→ f; la unión y la estrella agregan un estado inicial y uno final unidos con λ, y la concatenación une fragmentos con λ.

| Estado | a | b | c | λ |
|---|---|---|---|---|
| →q0 | ∅ | ∅ | ∅ | {q1} |
| *q1 | ∅ | ∅ | ∅ | ∅ |

**Transiciones λ.** Las λ son las de la construcción de Thompson: en la unión eligen una alternativa, en la estrella permiten repetir o saltar el fragmento y en la concatenación enlazan fragmentos.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0, q1} | sí |
| q1 | {q1} | sí |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | acepta | acepta | acepta |
| 2 | `a` | rechaza | rechaza | rechaza |
| 3 | `bc` | rechaza | rechaza | rechaza |
| 4 | `abaa` | rechaza | rechaza | rechaza |
| 5 | `caacaab` | rechaza | rechaza | rechaza |
| 6 | `bcabaacabcc` | rechaza | rechaza | rechaza |

Nota sobre los casos: el lenguaje solo tiene 1 palabra.

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: {q0, q1} — ✔
  Árbol de cómputo: 2 caminos, 1 de aceptación:
    - q0 -λ→ q1 — ✔ acepta
    - q0 — ✘ termina fuera de F
2. `a`: {q0, q1} -a→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 -λ→ q1 — ✘ muere tras leer λ
3. `bc`: {q0, q1} -b→ ∅ -c→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 -λ→ q1 — ✘ muere tras leer λ
4. `abaa`: {q0, q1} -a→ ∅ -b→ ∅ -a→ ∅ -a→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 -λ→ q1 — ✘ muere tras leer λ
5. `caacaab`: {q0, q1} -c→ ∅ -a→ ∅ -a→ ∅ -c→ ∅ -a→ ∅ -a→ ∅ -b→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 -λ→ q1 — ✘ muere tras leer λ
6. `bcabaacabcc`: {q0, q1} -b→ ∅ -c→ ∅ -a→ ∅ -b→ ∅ -a→ ∅ -a→ ∅ -c→ ∅ -a→ ∅ -b→ ∅ -c→ ∅ -c→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 -λ→ q1 — ✘ muere tras leer λ

</details>

Simulación paso a paso en JFLAP con `a`: [ver captura](../../evidencias/jflap/pasos/L3-VF-230.png).

**Conversión.** AFND-λ (2 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 1 estados, [`L3-VF-230-AFND.jff`](../../automatas/conversiones/L3-VF-230-AFND.jff). AFND (1 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 1 estados, [`L3-VF-230-AFD.jff`](../../automatas/conversiones/L3-VF-230-AFD.jff) ([.json](../../automatas/conversiones/L3-VF-230-AFD.json), [.xml](../../automatas/conversiones/L3-VF-230-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 2 estados, y el AFD mínimo (Hopcroft), 2. La cota es 2^1 = 2. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-231"></a>

## Lista 3, problema 231

**Enunciado.** ¿Es verdadera la afirmación «w ∈ L(λ+a)»? Afirmaciones 231.

**Clasificación: AFND-λ.** Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

| Afirmación | Cadena | Expresión | AFND-λ de Thompson | Respuesta | Razón |
|---|---|---|---|---|---|
| 231 | λ | `λ+a` | acepta | **V** | Se elige λ en la unión. |

#### AFND-λ de Thompson de λ+a — `L3-VF-231`

Archivos: [`L3-VF-231.jff`](../../automatas/lista3-afnd-lambda/L3-VF-231.jff) · [`L3-VF-231.json`](../../automatas/lista3-afnd-lambda/L3-VF-231.json) · [`L3-VF-231.xml`](../../automatas/lista3-afnd-lambda/L3-VF-231.xml). Tipo según la definición: **AFND-lambda**, |Q| = 6, Σ = {a, b, c}, 6 transiciones.

**Diseño.** Construcción de Thompson sobre Σ = {a, b, c}: cada símbolo es un fragmento i -a→ f; la unión y la estrella agregan un estado inicial y uno final unidos con λ, y la concatenación une fragmentos con λ.

| Estado | a | b | c | λ |
|---|---|---|---|---|
| →q0 | ∅ | ∅ | ∅ | {q1, q2} |
| q1 | ∅ | ∅ | ∅ | {q3} |
| q3 | ∅ | ∅ | ∅ | {q5} |
| q2 | {q4} | ∅ | ∅ | ∅ |
| q4 | ∅ | ∅ | ∅ | {q5} |
| *q5 | ∅ | ∅ | ∅ | ∅ |

**Transiciones λ.** Las λ son las de la construcción de Thompson: en la unión eligen una alternativa, en la estrella permiten repetir o saltar el fragmento y en la concatenación enlazan fragmentos.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0, q1, q2, q3, q5} | sí |
| q1 | {q1, q3, q5} | sí |
| q3 | {q3, q5} | sí |
| q2 | {q2} | no |
| q4 | {q4, q5} | sí |
| q5 | {q5} | sí |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | acepta | acepta | acepta |
| 2 | `a` | acepta | acepta | acepta |
| 3 | `b` | rechaza | rechaza | rechaza |
| 4 | `cb` | rechaza | rechaza | rechaza |
| 5 | `ccba` | rechaza | rechaza | rechaza |
| 6 | `aaacccb` | rechaza | rechaza | rechaza |
| 7 | `baacbcabcac` | rechaza | rechaza | rechaza |

Nota sobre los casos: el lenguaje solo tiene 2 palabras.

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: {q0, q1, q2, q3, q5} — ✔
  Árbol de cómputo: 5 caminos, 1 de aceptación:
    - q0 -λ→ q1 -λ→ q3 -λ→ q5 — ✔ acepta
    - q0 — ✘ termina fuera de F
    - q0 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q2 — ✘ termina fuera de F
2. `a`: {q0, q1, q2, q3, q5} -a→ {q4, q5} — ✔
  Árbol de cómputo: 3 caminos, 1 de aceptación:
    - q0 -λ→ q2 -a→ q4 -λ→ q5 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -λ→ q5 — ✘ muere tras leer λ
    - q0 -λ→ q2 -a→ q4 — ✘ termina fuera de F
3. `b`: {q0, q1, q2, q3, q5} -b→ ∅ — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q3 -λ→ q5 — ✘ muere tras leer λ
    - q0 -λ→ q2 — ✘ muere tras leer λ
4. `cb`: {q0, q1, q2, q3, q5} -c→ ∅ -b→ ∅ — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q3 -λ→ q5 — ✘ muere tras leer λ
    - q0 -λ→ q2 — ✘ muere tras leer λ
5. `ccba`: {q0, q1, q2, q3, q5} -c→ ∅ -c→ ∅ -b→ ∅ -a→ ∅ — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q3 -λ→ q5 — ✘ muere tras leer λ
    - q0 -λ→ q2 — ✘ muere tras leer λ
6. `aaacccb`: {q0, q1, q2, q3, q5} -a→ {q4, q5} -a→ ∅ -a→ ∅ -c→ ∅ -c→ ∅ -c→ ∅ -b→ ∅ — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q3 -λ→ q5 — ✘ muere tras leer λ
    - q0 -λ→ q2 -a→ q4 -λ→ q5 — ✘ muere tras leer `a`
7. `baacbcabcac`: {q0, q1, q2, q3, q5} -b→ ∅ -a→ ∅ -a→ ∅ -c→ ∅ -b→ ∅ -c→ ∅ -a→ ∅ -b→ ∅ -c→ ∅ -a→ ∅ -c→ ∅ — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q3 -λ→ q5 — ✘ muere tras leer λ
    - q0 -λ→ q2 — ✘ muere tras leer λ

</details>

Simulación paso a paso en JFLAP con `a`: [ver captura](../../evidencias/jflap/pasos/L3-VF-231.png).

**Conversión.** AFND-λ (6 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 3 estados, [`L3-VF-231-AFND.jff`](../../automatas/conversiones/L3-VF-231-AFND.jff). AFND (3 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 2 estados, [`L3-VF-231-AFD.jff`](../../automatas/conversiones/L3-VF-231-AFD.jff) ([.json](../../automatas/conversiones/L3-VF-231-AFD.json), [.xml](../../automatas/conversiones/L3-VF-231-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 3 estados, y el AFD mínimo (Hopcroft), 3. La cota es 2^3 = 8. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-232"></a>

## Lista 3, problema 232

**Enunciado.** ¿Es verdadera la afirmación «w ∈ L(λa)»? Afirmaciones 232.

**Clasificación: AFND-λ.** Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

| Afirmación | Cadena | Expresión | AFND-λ de Thompson | Respuesta | Razón |
|---|---|---|---|---|---|
| 232 | λ | `λa` | rechaza | **F** | L(λa) = {a}. |

#### AFND-λ de Thompson de λa — `L3-VF-232`

Archivos: [`L3-VF-232.jff`](../../automatas/lista3-afnd-lambda/L3-VF-232.jff) · [`L3-VF-232.json`](../../automatas/lista3-afnd-lambda/L3-VF-232.json) · [`L3-VF-232.xml`](../../automatas/lista3-afnd-lambda/L3-VF-232.xml). Tipo según la definición: **AFND-lambda**, |Q| = 4, Σ = {a, b, c}, 3 transiciones.

**Diseño.** Construcción de Thompson sobre Σ = {a, b, c}: cada símbolo es un fragmento i -a→ f; la unión y la estrella agregan un estado inicial y uno final unidos con λ, y la concatenación une fragmentos con λ.

| Estado | a | b | c | λ |
|---|---|---|---|---|
| →q0 | ∅ | ∅ | ∅ | {q1} |
| q1 | ∅ | ∅ | ∅ | {q2} |
| q2 | {q3} | ∅ | ∅ | ∅ |
| *q3 | ∅ | ∅ | ∅ | ∅ |

**Transiciones λ.** Las λ son las de la construcción de Thompson: en la unión eligen una alternativa, en la estrella permiten repetir o saltar el fragmento y en la concatenación enlazan fragmentos.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0, q1, q2} | no |
| q1 | {q1, q2} | no |
| q2 | {q2} | no |
| q3 | {q3} | sí |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `a` | acepta | acepta | acepta |
| 2 | λ | rechaza | rechaza | rechaza |
| 3 | `bb` | rechaza | rechaza | rechaza |
| 4 | `cbcb` | rechaza | rechaza | rechaza |
| 5 | `cbabbac` | rechaza | rechaza | rechaza |
| 6 | `acaaccbaaab` | rechaza | rechaza | rechaza |

Nota sobre los casos: el lenguaje solo tiene 1 palabra.

<details><summary>Recorrido completo de cada cadena</summary>

1. `a`: {q0, q1, q2} -a→ {q3} — ✔
  Árbol de cómputo: 1 caminos, 1 de aceptación:
    - q0 -λ→ q1 -λ→ q2 -a→ q3 — ✔ acepta
2. λ: {q0, q1, q2} — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
    - q0 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q2 — ✘ termina fuera de F
3. `bb`: {q0, q1, q2} -b→ ∅ -b→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q2 — ✘ muere tras leer λ
4. `cbcb`: {q0, q1, q2} -c→ ∅ -b→ ∅ -c→ ∅ -b→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q2 — ✘ muere tras leer λ
5. `cbabbac`: {q0, q1, q2} -c→ ∅ -b→ ∅ -a→ ∅ -b→ ∅ -b→ ∅ -a→ ∅ -c→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q2 — ✘ muere tras leer λ
6. `acaaccbaaab`: {q0, q1, q2} -a→ {q3} -c→ ∅ -a→ ∅ -a→ ∅ -c→ ∅ -c→ ∅ -b→ ∅ -a→ ∅ -a→ ∅ -a→ ∅ -b→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q2 -a→ q3 — ✘ muere tras leer `a`

</details>

Simulación paso a paso en JFLAP con `a`: [ver captura](../../evidencias/jflap/pasos/L3-VF-232.png).

**Conversión.** AFND-λ (4 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 2 estados, [`L3-VF-232-AFND.jff`](../../automatas/conversiones/L3-VF-232-AFND.jff). AFND (2 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 2 estados, [`L3-VF-232-AFD.jff`](../../automatas/conversiones/L3-VF-232-AFD.jff) ([.json](../../automatas/conversiones/L3-VF-232-AFD.json), [.xml](../../automatas/conversiones/L3-VF-232-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 3 estados, y el AFD mínimo (Hopcroft), 3. La cota es 2^2 = 4. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-234"></a>

## Lista 3, problema 234

**Enunciado.** ¿Es verdadera la afirmación «w ∈ L((ab)*)»? Afirmaciones 234.

**Clasificación: AFND-λ.** Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

| Afirmación | Cadena | Expresión | AFND-λ de Thompson | Respuesta | Razón |
|---|---|---|---|---|---|
| 234 | λ | `(ab)*` | acepta | **V** | Cero repeticiones. |

#### AFND-λ de Thompson de (ab)* — `L3-VF-234`

Archivos: [`L3-VF-234.jff`](../../automatas/lista3-afnd-lambda/L3-VF-234.jff) · [`L3-VF-234.json`](../../automatas/lista3-afnd-lambda/L3-VF-234.json) · [`L3-VF-234.xml`](../../automatas/lista3-afnd-lambda/L3-VF-234.xml). Tipo según la definición: **AFND-lambda**, |Q| = 6, Σ = {a, b, c}, 7 transiciones.

**Diseño.** Construcción de Thompson sobre Σ = {a, b, c}: cada símbolo es un fragmento i -a→ f; la unión y la estrella agregan un estado inicial y uno final unidos con λ, y la concatenación une fragmentos con λ.

| Estado | a | b | c | λ |
|---|---|---|---|---|
| →q0 | ∅ | ∅ | ∅ | {q1, q2} |
| q1 | {q3} | ∅ | ∅ | ∅ |
| q3 | ∅ | ∅ | ∅ | {q4} |
| q4 | ∅ | {q5} | ∅ | ∅ |
| q5 | ∅ | ∅ | ∅ | {q1, q2} |
| *q2 | ∅ | ∅ | ∅ | ∅ |

**Transiciones λ.** Las λ son las de la construcción de Thompson: en la unión eligen una alternativa, en la estrella permiten repetir o saltar el fragmento y en la concatenación enlazan fragmentos.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0, q1, q2} | sí |
| q1 | {q1} | no |
| q3 | {q3, q4} | no |
| q4 | {q4} | no |
| q5 | {q1, q2, q5} | sí |
| q2 | {q2} | sí |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | acepta | acepta | acepta |
| 2 | `ab` | acepta | acepta | acepta |
| 3 | `abab` | acepta | acepta | acepta |
| 4 | `abababab` | acepta | acepta | acepta |
| 5 | `abababababab` | acepta | acepta | acepta |
| 6 | `a` | rechaza | rechaza | rechaza |
| 7 | `bc` | rechaza | rechaza | rechaza |
| 8 | `acbc` | rechaza | rechaza | rechaza |
| 9 | `cbbaacb` | rechaza | rechaza | rechaza |
| 10 | `aaacccbacba` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: {q0, q1, q2} — ✔
  Árbol de cómputo: 3 caminos, 1 de aceptación:
    - q0 -λ→ q2 — ✔ acepta
    - q0 — ✘ termina fuera de F
    - q0 -λ→ q1 — ✘ termina fuera de F
2. `ab`: {q0, q1, q2} -a→ {q3, q4} -b→ {q1, q2, q5} — ✔
  Árbol de cómputo: 4 caminos, 1 de aceptación:
    - q0 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q2 — ✔ acepta
    - q0 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 — ✘ termina fuera de F
    - q0 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q2 — ✘ muere tras leer λ
3. `abab`: {q0, q1, q2} -a→ {q3, q4} -b→ {q1, q2, q5} -a→ {q3, q4} -b→ {q1, q2, q5} — ✔
  Árbol de cómputo: 5 caminos, 1 de aceptación:
    - q0 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q2 — ✔ acepta
    - q0 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 — ✘ termina fuera de F
    - q0 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q2 — ✘ muere tras leer `ab`
    - q0 -λ→ q2 — ✘ muere tras leer λ
4. `abababab`: {q0, q1, q2} -a→ {q3, q4} -b→ {q1, q2, q5} -a→ {q3, q4} -b→ {q1, q2, q5} -a→ {q3, q4} -b→ {q1, q2, q5} -a→ {q3, q4} -b→ {q1, q2, q5} — ✔
  Árbol de cómputo: 7 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q2 — ✔ acepta
    - q0 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 — ✘ termina fuera de F
    - q0 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q2 — ✘ muere tras leer `ababab`
    - q0 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q2 — ✘ muere tras leer `abab`
    - q0 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q2 — ✘ muere tras leer `ab`
5. `abababababab`: {q0, q1, q2} -a→ {q3, q4} -b→ {q1, q2, q5} -a→ {q3, q4} -b→ {q1, q2, q5} -a→ {q3, q4} -b→ {q1, q2, q5} -a→ {q3, q4} -b→ {q1, q2, q5} -a→ {q3, q4} -b→ {q1, q2, q5} -a→ {q3, q4} -b→ {q1, q2, q5} — ✔
  Árbol de cómputo: 9 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q2 — ✔ acepta
    - q0 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 — ✘ termina fuera de F
    - q0 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q2 — ✘ muere tras leer `ababababab`
    - q0 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q2 — ✘ muere tras leer `abababab`
    - q0 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q1 -a→ q3 -λ→ q4 -b→ q5 -λ→ q2 — ✘ muere tras leer `ababab`
6. `a`: {q0, q1, q2} -a→ {q3, q4} — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - q0 -λ→ q1 -a→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -a→ q3 -λ→ q4 — ✘ termina fuera de F
    - q0 -λ→ q2 — ✘ muere tras leer λ
7. `bc`: {q0, q1, q2} -b→ ∅ -c→ ∅ — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 — ✘ muere tras leer λ
8. `acbc`: {q0, q1, q2} -a→ {q3, q4} -c→ ∅ -b→ ∅ -c→ ∅ — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -λ→ q1 -a→ q3 -λ→ q4 — ✘ muere tras leer `a`
    - q0 -λ→ q2 — ✘ muere tras leer λ
9. `cbbaacb`: {q0, q1, q2} -c→ ∅ -b→ ∅ -b→ ∅ -a→ ∅ -a→ ∅ -c→ ∅ -b→ ∅ — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 — ✘ muere tras leer λ
10. `aaacccbacba`: {q0, q1, q2} -a→ {q3, q4} -a→ ∅ -a→ ∅ -c→ ∅ -c→ ∅ -c→ ∅ -b→ ∅ -a→ ∅ -c→ ∅ -b→ ∅ -a→ ∅ — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -λ→ q1 -a→ q3 -λ→ q4 — ✘ muere tras leer `a`
    - q0 -λ→ q2 — ✘ muere tras leer λ

</details>

Simulación paso a paso en JFLAP con `ab`: [ver captura](../../evidencias/jflap/pasos/L3-VF-234.png).

**Conversión.** AFND-λ (6 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 6 estados, [`L3-VF-234-AFND.jff`](../../automatas/conversiones/L3-VF-234-AFND.jff). AFND (6 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 3 estados, [`L3-VF-234-AFD.jff`](../../automatas/conversiones/L3-VF-234-AFD.jff) ([.json](../../automatas/conversiones/L3-VF-234-AFD.json), [.xml](../../automatas/conversiones/L3-VF-234-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 4 estados, y el AFD mínimo (Hopcroft), 3. La cota es 2^6 = 64. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-236"></a>

## Lista 3, problema 236

**Enunciado.** L = {x001y : x, y ∈ Σ*}. Encontrar una expresión regular.

**Clasificación: AFND-λ.** La respuesta es una expresión regular; su AFND-λ de Thompson es la forma de simularla. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

**Expresión regular** (archivo de JFLAP [`L3-236-ER.jff`](../../automatas/lista3-afnd-lambda/L3-236-ER.jff)): `(0+1)*001(0+1)*` (en JFLAP, `+` es la unión y `!` es λ).

#### AFND-λ de Thompson de la expresión — `L3-236`

Archivos: [`L3-236.jff`](../../automatas/lista3-afnd-lambda/L3-236.jff) · [`L3-236.json`](../../automatas/lista3-afnd-lambda/L3-236.json) · [`L3-236.xml`](../../automatas/lista3-afnd-lambda/L3-236.xml). Tipo según la definición: **AFND-lambda**, |Q| = 22, Σ = {0, 1}, 27 transiciones.

**Diseño.** Cualquier prefijo, 001 y cualquier sufijo.

<details><summary>Tabla de transiciones (22 estados)</summary>

| Estado | 0 | 1 | λ |
|---|---|---|---|
| →q0 | ∅ | ∅ | {q1, q2} |
| q1 | ∅ | ∅ | {q3, q4} |
| q3 | {q6} | ∅ | ∅ |
| q6 | ∅ | ∅ | {q9} |
| q4 | ∅ | {q7} | ∅ |
| q7 | ∅ | ∅ | {q9} |
| q9 | ∅ | ∅ | {q1, q2} |
| q2 | ∅ | ∅ | {q5} |
| q5 | {q8} | ∅ | ∅ |
| q8 | ∅ | ∅ | {q10} |
| q10 | {q11} | ∅ | ∅ |
| q11 | ∅ | ∅ | {q12} |
| q12 | ∅ | {q13} | ∅ |
| q13 | ∅ | ∅ | {q14} |
| q14 | ∅ | ∅ | {q15, q16} |
| q15 | ∅ | ∅ | {q17, q18} |
| q17 | {q19} | ∅ | ∅ |
| q19 | ∅ | ∅ | {q21} |
| q18 | ∅ | {q20} | ∅ |
| q20 | ∅ | ∅ | {q21} |
| q21 | ∅ | ∅ | {q15, q16} |
| *q16 | ∅ | ∅ | ∅ |

</details>

**Transiciones λ.** Las λ son las de la construcción de Thompson (unión, estrella y concatenación).

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

<details><summary>λ-clausuras de los 22 estados</summary>

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0, q1, q2, q3, q4, q5} | no |
| q1 | {q1, q3, q4} | no |
| q3 | {q3} | no |
| q6 | {q1, q2, q3, q4, q5, q6, q9} | no |
| q4 | {q4} | no |
| q7 | {q1, q2, q3, q4, q5, q7, q9} | no |
| q9 | {q1, q2, q3, q4, q5, q9} | no |
| q2 | {q2, q5} | no |
| q5 | {q5} | no |
| q8 | {q10, q8} | no |
| q10 | {q10} | no |
| q11 | {q11, q12} | no |
| q12 | {q12} | no |
| q13 | {q13, q14, q15, q16, q17, q18} | sí |
| q14 | {q14, q15, q16, q17, q18} | sí |
| q15 | {q15, q17, q18} | no |
| q17 | {q17} | no |
| q19 | {q15, q16, q17, q18, q19, q21} | sí |
| q18 | {q18} | no |
| q20 | {q15, q16, q17, q18, q20, q21} | sí |
| q21 | {q15, q16, q17, q18, q21} | sí |
| q16 | {q16} | sí |

</details>

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `001` | acepta | acepta | acepta |
| 2 | `01001` | acepta | acepta | acepta |
| 3 | `11001` | acepta | acepta | acepta |
| 4 | `0011100` | acepta | acepta | acepta |
| 5 | `00010110101` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `10` | rechaza | rechaza | rechaza |
| 8 | `0101` | rechaza | rechaza | rechaza |
| 9 | `0000000` | rechaza | rechaza | rechaza |
| 10 | `11011010000` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `001`: {q0, q1, q2, q3, q4, q5} -0→ {q1, q10, q2, q3, q4, q5, q6, q8, q9} -0→ {q1, q10, q11, q12, q2, q3, q4, q5, q6, q8, q9} -1→ {q1, q13, q14, q15, q16, q17, q18, q2, q3, q4, q5, q7, q9} — ✔
  Árbol de cómputo: 18 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q2 -λ→ q5 -0→ q8 -λ→ q10 -0→ q11 -λ→ q12 -1→ q13 -λ→ q14 -λ→ q16 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `00`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ termina fuera de F
2. `01001`: {q0, q1, q2, q3, q4, q5} -0→ {q1, q10, q2, q3, q4, q5, q6, q8, q9} -1→ {q1, q2, q3, q4, q5, q7, q9} -0→ {q1, q10, q2, q3, q4, q5, q6, q8, q9} -0→ {q1, q10, q11, q12, q2, q3, q4, q5, q6, q8, q9} -1→ {q1, q13, q14, q15, q16, q17, q18, q2, q3, q4, q5, q7, q9} — ✔
  Árbol de cómputo: 22 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q2 -λ→ q5 -0→ q8 -λ→ q10 -0→ q11 -λ→ q12 -1→ q13 -λ→ q14 -λ→ q16 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `0100`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 — ✘ termina fuera de F
3. `11001`: {q0, q1, q2, q3, q4, q5} -1→ {q1, q2, q3, q4, q5, q7, q9} -1→ {q1, q2, q3, q4, q5, q7, q9} -0→ {q1, q10, q2, q3, q4, q5, q6, q8, q9} -0→ {q1, q10, q11, q12, q2, q3, q4, q5, q6, q8, q9} -1→ {q1, q13, q14, q15, q16, q17, q18, q2, q3, q4, q5, q7, q9} — ✔
  Árbol de cómputo: 22 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q2 -λ→ q5 -0→ q8 -λ→ q10 -0→ q11 -λ→ q12 -1→ q13 -λ→ q14 -λ→ q16 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `1`
    - q0 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `1100`
    - q0 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 — ✘ termina fuera de F
4. `0011100`: {q0, q1, q2, q3, q4, q5} -0→ {q1, q10, q2, q3, q4, q5, q6, q8, q9} -0→ {q1, q10, q11, q12, q2, q3, q4, q5, q6, q8, q9} -1→ {q1, q13, q14, q15, q16, q17, q18, q2, q3, q4, q5, q7, q9} -1→ {q1, q15, q16, q17, q18, q2, q20, q21, q3, q4, q5, q7, q9} -1→ {q1, q15, q16, q17, q18, q2, q20, q21, q3, q4, q5, q7, q9} -0→ {q1, q10, q15, q16, q17, q18, q19, q2, q21, q3, q4, q5, q6, q8, q9} -0→ {q1, q10, q11, q12, q15, q16, q17, q18, q19, q2, q21, q3, q4, q5, q6, q8, q9} — ✔
  Árbol de cómputo: 36 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q2 -λ→ q5 -0→ q8 -λ→ q10 -0→ q11 -λ→ q12 -1→ q13 -λ→ q14 -λ→ q15 -λ→ q18 -1→ q20 -λ→ q21 -λ→ q15 -λ→ q18 -1→ q20 -λ→ q21 -λ→ q15 -λ→ q17 -0→ q19 -λ→ q21 -λ→ q15 -λ→ q17 -0→ q19 -λ→ q21 -λ→ q16 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `00`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `001`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `0011`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 — ✘ termina fuera de F
5. `00010110101`: {q0, q1, q2, q3, q4, q5} -0→ {q1, q10, q2, q3, q4, q5, q6, q8, q9} -0→ {q1, q10, q11, q12, q2, q3, q4, q5, q6, q8, q9} -0→ {q1, q10, q11, q12, q2, q3, q4, q5, q6, q8, q9} -1→ {q1, q13, q14, q15, q16, q17, q18, q2, q3, q4, q5, q7, q9} -0→ {q1, q10, q15, q16, q17, q18, q19, q2, q21, q3, q4, q5, q6, q8, q9} -1→ {q1, q15, q16, q17, q18, q2, q20, q21, q3, q4, q5, q7, q9} -1→ {q1, q15, q16, q17, q18, q2, q20, q21, q3, q4, q5, q7, q9} -0→ {q1, q10, q15, q16, q17, q18, q19, q2, q21, q3, q4, q5, q6, q8, q9} -1→ {q1, q15, q16, q17, q18, q2, q20, q21, q3, q4, q5, q7, q9} -0→ {q1, q10, q15, q16, q17, q18, q19, q2, q21, q3, q4, q5, q6, q8, q9} -1→ {q1, q15, q16, q17, q18, q2, q20, q21, q3, q4, q5, q7, q9} — ✔
  Árbol de cómputo: 48 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q2 -λ→ q5 -0→ q8 -λ→ q10 -0→ q11 -λ→ q12 -1→ q13 -λ→ q14 -λ→ q15 -λ→ q17 -0→ q19 -λ→ q21 -λ→ q15 -λ→ q18 -1→ q20 -λ→ q21 -λ→ q15 -λ→ q18 -1→ q20 -λ→ q21 -λ→ q15 -λ→ q17 -0→ q19 -λ→ q21 -λ→ q15 -λ→ q18 -1→ q20 -λ→ q21 -λ→ q15 -λ→ q17 -0→ q19 -λ→ q21 -λ→ q15 -λ→ q18 -1→ q20 -λ→ q21 -λ→ q16 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `000`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `00010`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `000101`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `00010110`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `0001011010`
6. λ: {q0, q1, q2, q3, q4, q5} — ✘
  Árbol de cómputo: 6 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
    - q0 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 — ✘ termina fuera de F
    - q0 -λ→ q2 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q5 — ✘ termina fuera de F
7. `10`: {q0, q1, q2, q3, q4, q5} -1→ {q1, q2, q3, q4, q5, q7, q9} -0→ {q1, q10, q2, q3, q4, q5, q6, q8, q9} — ✘
  Árbol de cómputo: 12 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 — ✘ termina fuera de F
8. `0101`: {q0, q1, q2, q3, q4, q5} -0→ {q1, q10, q2, q3, q4, q5, q6, q8, q9} -1→ {q1, q2, q3, q4, q5, q7, q9} -0→ {q1, q10, q2, q3, q4, q5, q6, q8, q9} -1→ {q1, q2, q3, q4, q5, q7, q9} — ✘
  Árbol de cómputo: 15 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `010`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ termina fuera de F
9. `0000000`: {q0, q1, q2, q3, q4, q5} -0→ {q1, q10, q2, q3, q4, q5, q6, q8, q9} -0→ {q1, q10, q11, q12, q2, q3, q4, q5, q6, q8, q9} -0→ {q1, q10, q11, q12, q2, q3, q4, q5, q6, q8, q9} -0→ {q1, q10, q11, q12, q2, q3, q4, q5, q6, q8, q9} -0→ {q1, q10, q11, q12, q2, q3, q4, q5, q6, q8, q9} -0→ {q1, q10, q11, q12, q2, q3, q4, q5, q6, q8, q9} -0→ {q1, q10, q11, q12, q2, q3, q4, q5, q6, q8, q9} — ✘
  Árbol de cómputo: 23 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q2 — ✘ termina fuera de F
10. `11011010000`: {q0, q1, q2, q3, q4, q5} -1→ {q1, q2, q3, q4, q5, q7, q9} -1→ {q1, q2, q3, q4, q5, q7, q9} -0→ {q1, q10, q2, q3, q4, q5, q6, q8, q9} -1→ {q1, q2, q3, q4, q5, q7, q9} -1→ {q1, q2, q3, q4, q5, q7, q9} -0→ {q1, q10, q2, q3, q4, q5, q6, q8, q9} -1→ {q1, q2, q3, q4, q5, q7, q9} -0→ {q1, q10, q2, q3, q4, q5, q6, q8, q9} -0→ {q1, q10, q11, q12, q2, q3, q4, q5, q6, q8, q9} -0→ {q1, q10, q11, q12, q2, q3, q4, q5, q6, q8, q9} -0→ {q1, q10, q11, q12, q2, q3, q4, q5, q6, q8, q9} — ✘
  Árbol de cómputo: 31 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `1`
    - q0 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `110`
    - q0 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `1101`
    - q0 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `110110`
    - q0 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 — ✘ termina fuera de F

</details>

Simulación paso a paso en JFLAP con `001`: [ver captura](../../evidencias/jflap/pasos/L3-236.png).

**Conversión.** AFND-λ (22 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 22 estados, [`L3-236-AFND.jff`](../../automatas/conversiones/L3-236-AFND.jff). AFND (22 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 9 estados, [`L3-236-AFD.jff`](../../automatas/conversiones/L3-236-AFD.jff) ([.json](../../automatas/conversiones/L3-236-AFD.json), [.xml](../../automatas/conversiones/L3-236-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 9 estados, y el AFD mínimo (Hopcroft), 4. La cota es 2^22 = 4194304. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-237"></a>

## Lista 3, problema 237

**Enunciado.** L = {x010 : x ∈ Σ*}. Encontrar una expresión regular.

**Clasificación: AFND-λ.** La respuesta es una expresión regular; su AFND-λ de Thompson es la forma de simularla. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

**Expresión regular** (archivo de JFLAP [`L3-237-ER.jff`](../../automatas/lista3-afnd-lambda/L3-237-ER.jff)): `(0+1)*010` (en JFLAP, `+` es la unión y `!` es λ).

#### AFND-λ de Thompson de la expresión — `L3-237`

Archivos: [`L3-237.jff`](../../automatas/lista3-afnd-lambda/L3-237.jff) · [`L3-237.json`](../../automatas/lista3-afnd-lambda/L3-237.json) · [`L3-237.xml`](../../automatas/lista3-afnd-lambda/L3-237.xml). Tipo según la definición: **AFND-lambda**, |Q| = 14, Σ = {0, 1}, 16 transiciones.

**Diseño.** Cualquier prefijo seguido de 010.

<details><summary>Tabla de transiciones (14 estados)</summary>

| Estado | 0 | 1 | λ |
|---|---|---|---|
| →q0 | ∅ | ∅ | {q1, q2} |
| q1 | ∅ | ∅ | {q3, q4} |
| q3 | {q6} | ∅ | ∅ |
| q6 | ∅ | ∅ | {q9} |
| q4 | ∅ | {q7} | ∅ |
| q7 | ∅ | ∅ | {q9} |
| q9 | ∅ | ∅ | {q1, q2} |
| q2 | ∅ | ∅ | {q5} |
| q5 | {q8} | ∅ | ∅ |
| q8 | ∅ | ∅ | {q10} |
| q10 | ∅ | {q11} | ∅ |
| q11 | ∅ | ∅ | {q12} |
| q12 | {q13} | ∅ | ∅ |
| *q13 | ∅ | ∅ | ∅ |

</details>

**Transiciones λ.** Las λ son las de la construcción de Thompson (unión, estrella y concatenación).

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

<details><summary>λ-clausuras de los 14 estados</summary>

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0, q1, q2, q3, q4, q5} | no |
| q1 | {q1, q3, q4} | no |
| q3 | {q3} | no |
| q6 | {q1, q2, q3, q4, q5, q6, q9} | no |
| q4 | {q4} | no |
| q7 | {q1, q2, q3, q4, q5, q7, q9} | no |
| q9 | {q1, q2, q3, q4, q5, q9} | no |
| q2 | {q2, q5} | no |
| q5 | {q5} | no |
| q8 | {q10, q8} | no |
| q10 | {q10} | no |
| q11 | {q11, q12} | no |
| q12 | {q12} | no |
| q13 | {q13} | sí |

</details>

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `010` | acepta | acepta | acepta |
| 2 | `1010` | acepta | acepta | acepta |
| 3 | `00010` | acepta | acepta | acepta |
| 4 | `101000010` | acepta | acepta | acepta |
| 5 | `0001111011010` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `00` | rechaza | rechaza | rechaza |
| 8 | `1111` | rechaza | rechaza | rechaza |
| 9 | `0101100` | rechaza | rechaza | rechaza |
| 10 | `00010101011` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `010`: {q0, q1, q2, q3, q4, q5} -0→ {q1, q10, q2, q3, q4, q5, q6, q8, q9} -1→ {q1, q11, q12, q2, q3, q4, q5, q7, q9} -0→ {q1, q10, q13, q2, q3, q4, q5, q6, q8, q9} — ✔
  Árbol de cómputo: 14 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q2 -λ→ q5 -0→ q8 -λ→ q10 -1→ q11 -λ→ q12 -0→ q13 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ termina fuera de F
2. `1010`: {q0, q1, q2, q3, q4, q5} -1→ {q1, q2, q3, q4, q5, q7, q9} -0→ {q1, q10, q2, q3, q4, q5, q6, q8, q9} -1→ {q1, q11, q12, q2, q3, q4, q5, q7, q9} -0→ {q1, q10, q13, q2, q3, q4, q5, q6, q8, q9} — ✔
  Árbol de cómputo: 16 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q2 -λ→ q5 -0→ q8 -λ→ q10 -1→ q11 -λ→ q12 -0→ q13 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `10`
    - q0 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 — ✘ termina fuera de F
3. `00010`: {q0, q1, q2, q3, q4, q5} -0→ {q1, q10, q2, q3, q4, q5, q6, q8, q9} -0→ {q1, q10, q2, q3, q4, q5, q6, q8, q9} -0→ {q1, q10, q2, q3, q4, q5, q6, q8, q9} -1→ {q1, q11, q12, q2, q3, q4, q5, q7, q9} -0→ {q1, q10, q13, q2, q3, q4, q5, q6, q8, q9} — ✔
  Árbol de cómputo: 18 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q2 -λ→ q5 -0→ q8 -λ→ q10 -1→ q11 -λ→ q12 -0→ q13 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `000`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ termina fuera de F
4. `101000010`: {q0, q1, q2, q3, q4, q5} -1→ {q1, q2, q3, q4, q5, q7, q9} -0→ {q1, q10, q2, q3, q4, q5, q6, q8, q9} -1→ {q1, q11, q12, q2, q3, q4, q5, q7, q9} -0→ {q1, q10, q13, q2, q3, q4, q5, q6, q8, q9} -0→ {q1, q10, q2, q3, q4, q5, q6, q8, q9} -0→ {q1, q10, q2, q3, q4, q5, q6, q8, q9} -0→ {q1, q10, q2, q3, q4, q5, q6, q8, q9} -1→ {q1, q11, q12, q2, q3, q4, q5, q7, q9} -0→ {q1, q10, q13, q2, q3, q4, q5, q6, q8, q9} — ✔
  Árbol de cómputo: 26 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q2 -λ→ q5 -0→ q8 -λ→ q10 -1→ q11 -λ→ q12 -0→ q13 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `10`
    - q0 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `1010000`
    - q0 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 — ✘ termina fuera de F
5. `0001111011010`: {q0, q1, q2, q3, q4, q5} -0→ {q1, q10, q2, q3, q4, q5, q6, q8, q9} -0→ {q1, q10, q2, q3, q4, q5, q6, q8, q9} -0→ {q1, q10, q2, q3, q4, q5, q6, q8, q9} -1→ {q1, q11, q12, q2, q3, q4, q5, q7, q9} -1→ {q1, q2, q3, q4, q5, q7, q9} -1→ {q1, q2, q3, q4, q5, q7, q9} -1→ {q1, q2, q3, q4, q5, q7, q9} -0→ {q1, q10, q2, q3, q4, q5, q6, q8, q9} -1→ {q1, q11, q12, q2, q3, q4, q5, q7, q9} -1→ {q1, q2, q3, q4, q5, q7, q9} -0→ {q1, q10, q2, q3, q4, q5, q6, q8, q9} -1→ {q1, q11, q12, q2, q3, q4, q5, q7, q9} -0→ {q1, q10, q13, q2, q3, q4, q5, q6, q8, q9} — ✔
  Árbol de cómputo: 34 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q2 -λ→ q5 -0→ q8 -λ→ q10 -1→ q11 -λ→ q12 -0→ q13 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `000`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `0001`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `00011`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `000111`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `00011110`
6. λ: {q0, q1, q2, q3, q4, q5} — ✘
  Árbol de cómputo: 6 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
    - q0 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 — ✘ termina fuera de F
    - q0 -λ→ q2 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q5 — ✘ termina fuera de F
7. `00`: {q0, q1, q2, q3, q4, q5} -0→ {q1, q10, q2, q3, q4, q5, q6, q8, q9} -0→ {q1, q10, q2, q3, q4, q5, q6, q8, q9} — ✘
  Árbol de cómputo: 12 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q2 — ✘ termina fuera de F
8. `1111`: {q0, q1, q2, q3, q4, q5} -1→ {q1, q2, q3, q4, q5, q7, q9} -1→ {q1, q2, q3, q4, q5, q7, q9} -1→ {q1, q2, q3, q4, q5, q7, q9} -1→ {q1, q2, q3, q4, q5, q7, q9} — ✘
  Árbol de cómputo: 15 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `1`
    - q0 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `11`
    - q0 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `111`
    - q0 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 — ✘ termina fuera de F
9. `0101100`: {q0, q1, q2, q3, q4, q5} -0→ {q1, q10, q2, q3, q4, q5, q6, q8, q9} -1→ {q1, q11, q12, q2, q3, q4, q5, q7, q9} -0→ {q1, q10, q13, q2, q3, q4, q5, q6, q8, q9} -1→ {q1, q11, q12, q2, q3, q4, q5, q7, q9} -1→ {q1, q2, q3, q4, q5, q7, q9} -0→ {q1, q10, q2, q3, q4, q5, q6, q8, q9} -0→ {q1, q10, q2, q3, q4, q5, q6, q8, q9} — ✘
  Árbol de cómputo: 22 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `010`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `0101`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 — ✘ termina fuera de F
10. `00010101011`: {q0, q1, q2, q3, q4, q5} -0→ {q1, q10, q2, q3, q4, q5, q6, q8, q9} -0→ {q1, q10, q2, q3, q4, q5, q6, q8, q9} -0→ {q1, q10, q2, q3, q4, q5, q6, q8, q9} -1→ {q1, q11, q12, q2, q3, q4, q5, q7, q9} -0→ {q1, q10, q13, q2, q3, q4, q5, q6, q8, q9} -1→ {q1, q11, q12, q2, q3, q4, q5, q7, q9} -0→ {q1, q10, q13, q2, q3, q4, q5, q6, q8, q9} -1→ {q1, q11, q12, q2, q3, q4, q5, q7, q9} -0→ {q1, q10, q13, q2, q3, q4, q5, q6, q8, q9} -1→ {q1, q11, q12, q2, q3, q4, q5, q7, q9} -1→ {q1, q2, q3, q4, q5, q7, q9} — ✘
  Árbol de cómputo: 29 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `000`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `00010`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `0001010`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `000101010`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 — ✘ muere tras leer `0001010101`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 -λ→ q9 -λ→ q1 -λ→ q4 -1→ q7 — ✘ termina fuera de F

</details>

Simulación paso a paso en JFLAP con `010`: [ver captura](../../evidencias/jflap/pasos/L3-237.png).

**Conversión.** AFND-λ (14 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 14 estados, [`L3-237-AFND.jff`](../../automatas/conversiones/L3-237-AFND.jff). AFND (14 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 5 estados, [`L3-237-AFD.jff`](../../automatas/conversiones/L3-237-AFD.jff) ([.json](../../automatas/conversiones/L3-237-AFD.json), [.xml](../../automatas/conversiones/L3-237-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 5 estados, y el AFD mínimo (Hopcroft), 4. La cota es 2^14 = 16384. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-238"></a>

## Lista 3, problema 238

**Enunciado.** L = Σ³ ∪ Σ⁵. Encontrar una expresión regular.

**Clasificación: AFND-λ.** La respuesta es una expresión regular; su AFND-λ de Thompson es la forma de simularla. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

**Expresión regular** (archivo de JFLAP [`L3-238-ER.jff`](../../automatas/lista3-afnd-lambda/L3-238-ER.jff)): `(0+1)(0+1)(0+1)(λ+(0+1)(0+1))` (en JFLAP, `+` es la unión y `!` es λ).

#### AFND-λ de Thompson de la expresión — `L3-238`

Archivos: [`L3-238.jff`](../../automatas/lista3-afnd-lambda/L3-238.jff) · [`L3-238.json`](../../automatas/lista3-afnd-lambda/L3-238.json) · [`L3-238.xml`](../../automatas/lista3-afnd-lambda/L3-238.xml). Tipo según la definición: **AFND-lambda**, |Q| = 34, Σ = {0, 1}, 39 transiciones.

**Diseño.** Tres símbolos y, opcionalmente, dos más (en JFLAP, ! es λ).

<details><summary>Tabla de transiciones (34 estados)</summary>

| Estado | 0 | 1 | λ |
|---|---|---|---|
| →q0 | ∅ | ∅ | {q1, q2} |
| q1 | {q3} | ∅ | ∅ |
| q3 | ∅ | ∅ | {q5} |
| q2 | ∅ | {q4} | ∅ |
| q4 | ∅ | ∅ | {q5} |
| q5 | ∅ | ∅ | {q6} |
| q6 | ∅ | ∅ | {q7, q8} |
| q7 | {q9} | ∅ | ∅ |
| q9 | ∅ | ∅ | {q11} |
| q8 | ∅ | {q10} | ∅ |
| q10 | ∅ | ∅ | {q11} |
| q11 | ∅ | ∅ | {q12} |
| q12 | ∅ | ∅ | {q13, q14} |
| q13 | {q15} | ∅ | ∅ |
| q15 | ∅ | ∅ | {q17} |
| q14 | ∅ | {q16} | ∅ |
| q16 | ∅ | ∅ | {q17} |
| q17 | ∅ | ∅ | {q18} |
| q18 | ∅ | ∅ | {q19, q20} |
| q19 | ∅ | ∅ | {q21} |
| q21 | ∅ | ∅ | {q24} |
| q20 | ∅ | ∅ | {q22, q23} |
| q22 | {q25} | ∅ | ∅ |
| q25 | ∅ | ∅ | {q27} |
| q23 | ∅ | {q26} | ∅ |
| q26 | ∅ | ∅ | {q27} |
| q27 | ∅ | ∅ | {q28} |
| q28 | ∅ | ∅ | {q29, q30} |
| q29 | {q31} | ∅ | ∅ |
| q31 | ∅ | ∅ | {q33} |
| q30 | ∅ | {q32} | ∅ |
| q32 | ∅ | ∅ | {q33} |
| q33 | ∅ | ∅ | {q24} |
| *q24 | ∅ | ∅ | ∅ |

</details>

**Transiciones λ.** Las λ son las de la construcción de Thompson (unión, estrella y concatenación).

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

<details><summary>λ-clausuras de los 34 estados</summary>

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0, q1, q2} | no |
| q1 | {q1} | no |
| q3 | {q3, q5, q6, q7, q8} | no |
| q2 | {q2} | no |
| q4 | {q4, q5, q6, q7, q8} | no |
| q5 | {q5, q6, q7, q8} | no |
| q6 | {q6, q7, q8} | no |
| q7 | {q7} | no |
| q9 | {q11, q12, q13, q14, q9} | no |
| q8 | {q8} | no |
| q10 | {q10, q11, q12, q13, q14} | no |
| q11 | {q11, q12, q13, q14} | no |
| q12 | {q12, q13, q14} | no |
| q13 | {q13} | no |
| q15 | {q15, q17, q18, q19, q20, q21, q22, q23, q24} | sí |
| q14 | {q14} | no |
| q16 | {q16, q17, q18, q19, q20, q21, q22, q23, q24} | sí |
| q17 | {q17, q18, q19, q20, q21, q22, q23, q24} | sí |
| q18 | {q18, q19, q20, q21, q22, q23, q24} | sí |
| q19 | {q19, q21, q24} | sí |
| q21 | {q21, q24} | sí |
| q20 | {q20, q22, q23} | no |
| q22 | {q22} | no |
| q25 | {q25, q27, q28, q29, q30} | no |
| q23 | {q23} | no |
| q26 | {q26, q27, q28, q29, q30} | no |
| q27 | {q27, q28, q29, q30} | no |
| q28 | {q28, q29, q30} | no |
| q29 | {q29} | no |
| q31 | {q24, q31, q33} | sí |
| q30 | {q30} | no |
| q32 | {q24, q32, q33} | sí |
| q33 | {q24, q33} | sí |
| q24 | {q24} | sí |

</details>

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `000` | acepta | acepta | acepta |
| 2 | `010` | acepta | acepta | acepta |
| 3 | `00100` | acepta | acepta | acepta |
| 4 | `01000` | acepta | acepta | acepta |
| 5 | `11000` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `10` | rechaza | rechaza | rechaza |
| 8 | `0110` | rechaza | rechaza | rechaza |
| 9 | `0000111` | rechaza | rechaza | rechaza |
| 10 | `11011101101` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `000`: {q0, q1, q2} -0→ {q3, q5, q6, q7, q8} -0→ {q11, q12, q13, q14, q9} -0→ {q15, q17, q18, q19, q20, q21, q22, q23, q24} — ✔
  Árbol de cómputo: 12 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -0→ q3 -λ→ q5 -λ→ q6 -λ→ q7 -0→ q9 -λ→ q11 -λ→ q12 -λ→ q13 -0→ q15 -λ→ q17 -λ→ q18 -λ→ q19 -λ→ q21 -λ→ q24 — ✔ acepta
    - q0 -λ→ q1 -0→ q3 -λ→ q5 -λ→ q6 -λ→ q7 -0→ q9 -λ→ q11 -λ→ q12 -λ→ q13 -0→ q15 — ✘ termina fuera de F
    - q0 -λ→ q1 -0→ q3 -λ→ q5 -λ→ q6 -λ→ q7 -0→ q9 -λ→ q11 -λ→ q12 -λ→ q13 -0→ q15 -λ→ q17 — ✘ termina fuera de F
    - q0 -λ→ q1 -0→ q3 -λ→ q5 -λ→ q6 -λ→ q7 -0→ q9 -λ→ q11 -λ→ q12 -λ→ q13 -0→ q15 -λ→ q17 -λ→ q18 — ✘ termina fuera de F
    - q0 -λ→ q1 -0→ q3 -λ→ q5 -λ→ q6 -λ→ q7 -0→ q9 -λ→ q11 -λ→ q12 -λ→ q13 -0→ q15 -λ→ q17 -λ→ q18 -λ→ q19 — ✘ termina fuera de F
    - q0 -λ→ q1 -0→ q3 -λ→ q5 -λ→ q6 -λ→ q7 -0→ q9 -λ→ q11 -λ→ q12 -λ→ q13 -0→ q15 -λ→ q17 -λ→ q18 -λ→ q19 -λ→ q21 — ✘ termina fuera de F
2. `010`: {q0, q1, q2} -0→ {q3, q5, q6, q7, q8} -1→ {q10, q11, q12, q13, q14} -0→ {q15, q17, q18, q19, q20, q21, q22, q23, q24} — ✔
  Árbol de cómputo: 12 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -0→ q3 -λ→ q5 -λ→ q6 -λ→ q8 -1→ q10 -λ→ q11 -λ→ q12 -λ→ q13 -0→ q15 -λ→ q17 -λ→ q18 -λ→ q19 -λ→ q21 -λ→ q24 — ✔ acepta
    - q0 -λ→ q1 -0→ q3 -λ→ q5 -λ→ q6 -λ→ q7 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -0→ q3 -λ→ q5 -λ→ q6 -λ→ q8 -1→ q10 -λ→ q11 -λ→ q12 -λ→ q13 -0→ q15 — ✘ termina fuera de F
    - q0 -λ→ q1 -0→ q3 -λ→ q5 -λ→ q6 -λ→ q8 -1→ q10 -λ→ q11 -λ→ q12 -λ→ q13 -0→ q15 -λ→ q17 — ✘ termina fuera de F
    - q0 -λ→ q1 -0→ q3 -λ→ q5 -λ→ q6 -λ→ q8 -1→ q10 -λ→ q11 -λ→ q12 -λ→ q13 -0→ q15 -λ→ q17 -λ→ q18 — ✘ termina fuera de F
    - q0 -λ→ q1 -0→ q3 -λ→ q5 -λ→ q6 -λ→ q8 -1→ q10 -λ→ q11 -λ→ q12 -λ→ q13 -0→ q15 -λ→ q17 -λ→ q18 -λ→ q19 — ✘ termina fuera de F
3. `00100`: {q0, q1, q2} -0→ {q3, q5, q6, q7, q8} -0→ {q11, q12, q13, q14, q9} -1→ {q16, q17, q18, q19, q20, q21, q22, q23, q24} -0→ {q25, q27, q28, q29, q30} -0→ {q24, q31, q33} — ✔
  Árbol de cómputo: 9 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -0→ q3 -λ→ q5 -λ→ q6 -λ→ q7 -0→ q9 -λ→ q11 -λ→ q12 -λ→ q14 -1→ q16 -λ→ q17 -λ→ q18 -λ→ q20 -λ→ q22 -0→ q25 -λ→ q27 -λ→ q28 -λ→ q29 -0→ q31 -λ→ q33 -λ→ q24 — ✔ acepta
    - q0 -λ→ q1 -0→ q3 -λ→ q5 -λ→ q6 -λ→ q7 -0→ q9 -λ→ q11 -λ→ q12 -λ→ q13 — ✘ muere tras leer `00`
    - q0 -λ→ q1 -0→ q3 -λ→ q5 -λ→ q6 -λ→ q7 -0→ q9 -λ→ q11 -λ→ q12 -λ→ q14 -1→ q16 -λ→ q17 -λ→ q18 -λ→ q19 -λ→ q21 -λ→ q24 — ✘ muere tras leer `001`
    - q0 -λ→ q1 -0→ q3 -λ→ q5 -λ→ q6 -λ→ q7 -0→ q9 -λ→ q11 -λ→ q12 -λ→ q14 -1→ q16 -λ→ q17 -λ→ q18 -λ→ q20 -λ→ q22 -0→ q25 -λ→ q27 -λ→ q28 -λ→ q29 -0→ q31 — ✘ termina fuera de F
    - q0 -λ→ q1 -0→ q3 -λ→ q5 -λ→ q6 -λ→ q7 -0→ q9 -λ→ q11 -λ→ q12 -λ→ q14 -1→ q16 -λ→ q17 -λ→ q18 -λ→ q20 -λ→ q22 -0→ q25 -λ→ q27 -λ→ q28 -λ→ q29 -0→ q31 -λ→ q33 — ✘ termina fuera de F
    - q0 -λ→ q1 -0→ q3 -λ→ q5 -λ→ q6 -λ→ q7 -0→ q9 -λ→ q11 -λ→ q12 -λ→ q14 -1→ q16 -λ→ q17 -λ→ q18 -λ→ q20 -λ→ q22 -0→ q25 -λ→ q27 -λ→ q28 -λ→ q30 — ✘ muere tras leer `0010`
4. `01000`: {q0, q1, q2} -0→ {q3, q5, q6, q7, q8} -1→ {q10, q11, q12, q13, q14} -0→ {q15, q17, q18, q19, q20, q21, q22, q23, q24} -0→ {q25, q27, q28, q29, q30} -0→ {q24, q31, q33} — ✔
  Árbol de cómputo: 9 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -0→ q3 -λ→ q5 -λ→ q6 -λ→ q8 -1→ q10 -λ→ q11 -λ→ q12 -λ→ q13 -0→ q15 -λ→ q17 -λ→ q18 -λ→ q20 -λ→ q22 -0→ q25 -λ→ q27 -λ→ q28 -λ→ q29 -0→ q31 -λ→ q33 -λ→ q24 — ✔ acepta
    - q0 -λ→ q1 -0→ q3 -λ→ q5 -λ→ q6 -λ→ q7 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -0→ q3 -λ→ q5 -λ→ q6 -λ→ q8 -1→ q10 -λ→ q11 -λ→ q12 -λ→ q13 -0→ q15 -λ→ q17 -λ→ q18 -λ→ q19 -λ→ q21 -λ→ q24 — ✘ muere tras leer `010`
    - q0 -λ→ q1 -0→ q3 -λ→ q5 -λ→ q6 -λ→ q8 -1→ q10 -λ→ q11 -λ→ q12 -λ→ q13 -0→ q15 -λ→ q17 -λ→ q18 -λ→ q20 -λ→ q22 -0→ q25 -λ→ q27 -λ→ q28 -λ→ q29 -0→ q31 — ✘ termina fuera de F
    - q0 -λ→ q1 -0→ q3 -λ→ q5 -λ→ q6 -λ→ q8 -1→ q10 -λ→ q11 -λ→ q12 -λ→ q13 -0→ q15 -λ→ q17 -λ→ q18 -λ→ q20 -λ→ q22 -0→ q25 -λ→ q27 -λ→ q28 -λ→ q29 -0→ q31 -λ→ q33 — ✘ termina fuera de F
    - q0 -λ→ q1 -0→ q3 -λ→ q5 -λ→ q6 -λ→ q8 -1→ q10 -λ→ q11 -λ→ q12 -λ→ q13 -0→ q15 -λ→ q17 -λ→ q18 -λ→ q20 -λ→ q22 -0→ q25 -λ→ q27 -λ→ q28 -λ→ q30 — ✘ muere tras leer `0100`
5. `11000`: {q0, q1, q2} -1→ {q4, q5, q6, q7, q8} -1→ {q10, q11, q12, q13, q14} -0→ {q15, q17, q18, q19, q20, q21, q22, q23, q24} -0→ {q25, q27, q28, q29, q30} -0→ {q24, q31, q33} — ✔
  Árbol de cómputo: 9 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q2 -1→ q4 -λ→ q5 -λ→ q6 -λ→ q8 -1→ q10 -λ→ q11 -λ→ q12 -λ→ q13 -0→ q15 -λ→ q17 -λ→ q18 -λ→ q20 -λ→ q22 -0→ q25 -λ→ q27 -λ→ q28 -λ→ q29 -0→ q31 -λ→ q33 -λ→ q24 — ✔ acepta
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 -1→ q4 -λ→ q5 -λ→ q6 -λ→ q7 — ✘ muere tras leer `1`
    - q0 -λ→ q2 -1→ q4 -λ→ q5 -λ→ q6 -λ→ q8 -1→ q10 -λ→ q11 -λ→ q12 -λ→ q13 -0→ q15 -λ→ q17 -λ→ q18 -λ→ q19 -λ→ q21 -λ→ q24 — ✘ muere tras leer `110`
    - q0 -λ→ q2 -1→ q4 -λ→ q5 -λ→ q6 -λ→ q8 -1→ q10 -λ→ q11 -λ→ q12 -λ→ q13 -0→ q15 -λ→ q17 -λ→ q18 -λ→ q20 -λ→ q22 -0→ q25 -λ→ q27 -λ→ q28 -λ→ q29 -0→ q31 — ✘ termina fuera de F
    - q0 -λ→ q2 -1→ q4 -λ→ q5 -λ→ q6 -λ→ q8 -1→ q10 -λ→ q11 -λ→ q12 -λ→ q13 -0→ q15 -λ→ q17 -λ→ q18 -λ→ q20 -λ→ q22 -0→ q25 -λ→ q27 -λ→ q28 -λ→ q29 -0→ q31 -λ→ q33 — ✘ termina fuera de F
6. λ: {q0, q1, q2} — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
    - q0 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q2 — ✘ termina fuera de F
7. `10`: {q0, q1, q2} -1→ {q4, q5, q6, q7, q8} -0→ {q11, q12, q13, q14, q9} — ✘
  Árbol de cómputo: 7 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 -1→ q4 -λ→ q5 -λ→ q6 -λ→ q7 -0→ q9 — ✘ termina fuera de F
    - q0 -λ→ q2 -1→ q4 -λ→ q5 -λ→ q6 -λ→ q7 -0→ q9 -λ→ q11 — ✘ termina fuera de F
    - q0 -λ→ q2 -1→ q4 -λ→ q5 -λ→ q6 -λ→ q7 -0→ q9 -λ→ q11 -λ→ q12 — ✘ termina fuera de F
    - q0 -λ→ q2 -1→ q4 -λ→ q5 -λ→ q6 -λ→ q7 -0→ q9 -λ→ q11 -λ→ q12 -λ→ q13 — ✘ termina fuera de F
    - q0 -λ→ q2 -1→ q4 -λ→ q5 -λ→ q6 -λ→ q7 -0→ q9 -λ→ q11 -λ→ q12 -λ→ q14 — ✘ termina fuera de F
8. `0110`: {q0, q1, q2} -0→ {q3, q5, q6, q7, q8} -1→ {q10, q11, q12, q13, q14} -1→ {q16, q17, q18, q19, q20, q21, q22, q23, q24} -0→ {q25, q27, q28, q29, q30} — ✘
  Árbol de cómputo: 10 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -0→ q3 -λ→ q5 -λ→ q6 -λ→ q7 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -0→ q3 -λ→ q5 -λ→ q6 -λ→ q8 -1→ q10 -λ→ q11 -λ→ q12 -λ→ q13 — ✘ muere tras leer `01`
    - q0 -λ→ q1 -0→ q3 -λ→ q5 -λ→ q6 -λ→ q8 -1→ q10 -λ→ q11 -λ→ q12 -λ→ q14 -1→ q16 -λ→ q17 -λ→ q18 -λ→ q19 -λ→ q21 -λ→ q24 — ✘ muere tras leer `011`
    - q0 -λ→ q1 -0→ q3 -λ→ q5 -λ→ q6 -λ→ q8 -1→ q10 -λ→ q11 -λ→ q12 -λ→ q14 -1→ q16 -λ→ q17 -λ→ q18 -λ→ q20 -λ→ q22 -0→ q25 — ✘ termina fuera de F
    - q0 -λ→ q1 -0→ q3 -λ→ q5 -λ→ q6 -λ→ q8 -1→ q10 -λ→ q11 -λ→ q12 -λ→ q14 -1→ q16 -λ→ q17 -λ→ q18 -λ→ q20 -λ→ q22 -0→ q25 -λ→ q27 — ✘ termina fuera de F
    - q0 -λ→ q1 -0→ q3 -λ→ q5 -λ→ q6 -λ→ q8 -1→ q10 -λ→ q11 -λ→ q12 -λ→ q14 -1→ q16 -λ→ q17 -λ→ q18 -λ→ q20 -λ→ q22 -0→ q25 -λ→ q27 -λ→ q28 — ✘ termina fuera de F
9. `0000111`: {q0, q1, q2} -0→ {q3, q5, q6, q7, q8} -0→ {q11, q12, q13, q14, q9} -0→ {q15, q17, q18, q19, q20, q21, q22, q23, q24} -0→ {q25, q27, q28, q29, q30} -1→ {q24, q32, q33} -1→ ∅ -1→ ∅ — ✘
  Árbol de cómputo: 7 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -0→ q3 -λ→ q5 -λ→ q6 -λ→ q7 -0→ q9 -λ→ q11 -λ→ q12 -λ→ q13 -0→ q15 -λ→ q17 -λ→ q18 -λ→ q19 -λ→ q21 -λ→ q24 — ✘ muere tras leer `000`
    - q0 -λ→ q1 -0→ q3 -λ→ q5 -λ→ q6 -λ→ q7 -0→ q9 -λ→ q11 -λ→ q12 -λ→ q13 -0→ q15 -λ→ q17 -λ→ q18 -λ→ q20 -λ→ q22 -0→ q25 -λ→ q27 -λ→ q28 -λ→ q29 — ✘ muere tras leer `0000`
    - q0 -λ→ q1 -0→ q3 -λ→ q5 -λ→ q6 -λ→ q7 -0→ q9 -λ→ q11 -λ→ q12 -λ→ q13 -0→ q15 -λ→ q17 -λ→ q18 -λ→ q20 -λ→ q22 -0→ q25 -λ→ q27 -λ→ q28 -λ→ q30 -1→ q32 -λ→ q33 -λ→ q24 — ✘ muere tras leer `00001`
    - q0 -λ→ q1 -0→ q3 -λ→ q5 -λ→ q6 -λ→ q7 -0→ q9 -λ→ q11 -λ→ q12 -λ→ q13 -0→ q15 -λ→ q17 -λ→ q18 -λ→ q20 -λ→ q23 — ✘ muere tras leer `000`
    - q0 -λ→ q1 -0→ q3 -λ→ q5 -λ→ q6 -λ→ q7 -0→ q9 -λ→ q11 -λ→ q12 -λ→ q14 — ✘ muere tras leer `00`
    - q0 -λ→ q1 -0→ q3 -λ→ q5 -λ→ q6 -λ→ q8 — ✘ muere tras leer `0`
10. `11011101101`: {q0, q1, q2} -1→ {q4, q5, q6, q7, q8} -1→ {q10, q11, q12, q13, q14} -0→ {q15, q17, q18, q19, q20, q21, q22, q23, q24} -1→ {q26, q27, q28, q29, q30} -1→ {q24, q32, q33} -1→ ∅ -0→ ∅ -1→ ∅ -1→ ∅ -0→ ∅ -1→ ∅ — ✘
  Árbol de cómputo: 7 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 -1→ q4 -λ→ q5 -λ→ q6 -λ→ q7 — ✘ muere tras leer `1`
    - q0 -λ→ q2 -1→ q4 -λ→ q5 -λ→ q6 -λ→ q8 -1→ q10 -λ→ q11 -λ→ q12 -λ→ q13 -0→ q15 -λ→ q17 -λ→ q18 -λ→ q19 -λ→ q21 -λ→ q24 — ✘ muere tras leer `110`
    - q0 -λ→ q2 -1→ q4 -λ→ q5 -λ→ q6 -λ→ q8 -1→ q10 -λ→ q11 -λ→ q12 -λ→ q13 -0→ q15 -λ→ q17 -λ→ q18 -λ→ q20 -λ→ q22 — ✘ muere tras leer `110`
    - q0 -λ→ q2 -1→ q4 -λ→ q5 -λ→ q6 -λ→ q8 -1→ q10 -λ→ q11 -λ→ q12 -λ→ q13 -0→ q15 -λ→ q17 -λ→ q18 -λ→ q20 -λ→ q23 -1→ q26 -λ→ q27 -λ→ q28 -λ→ q29 — ✘ muere tras leer `1101`
    - q0 -λ→ q2 -1→ q4 -λ→ q5 -λ→ q6 -λ→ q8 -1→ q10 -λ→ q11 -λ→ q12 -λ→ q13 -0→ q15 -λ→ q17 -λ→ q18 -λ→ q20 -λ→ q23 -1→ q26 -λ→ q27 -λ→ q28 -λ→ q30 -1→ q32 -λ→ q33 -λ→ q24 — ✘ muere tras leer `11011`

</details>

Simulación paso a paso en JFLAP con `000`: [ver captura](../../evidencias/jflap/pasos/L3-238.png).

**Conversión.** AFND-λ (34 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 32 estados, [`L3-238-AFND.jff`](../../automatas/conversiones/L3-238-AFND.jff). AFND (32 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 11 estados, [`L3-238-AFD.jff`](../../automatas/conversiones/L3-238-AFD.jff) ([.json](../../automatas/conversiones/L3-238-AFD.json), [.xml](../../automatas/conversiones/L3-238-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 12 estados, y el AFD mínimo (Hopcroft), 7. La cota es 2^32 = 4294967296. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-239"></a>

## Lista 3, problema 239

**Enunciado.** Cadenas que comienzan con 01 o terminan con 10. Encontrar una expresión regular.

**Clasificación: AFND-λ.** La respuesta es una expresión regular; su AFND-λ de Thompson es la forma de simularla. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

**Expresión regular** (archivo de JFLAP [`L3-239-ER.jff`](../../automatas/lista3-afnd-lambda/L3-239-ER.jff)): `01(0+1)*+(0+1)*10` (en JFLAP, `+` es la unión y `!` es λ).

#### AFND-λ de Thompson de la expresión — `L3-239`

Archivos: [`L3-239.jff`](../../automatas/lista3-afnd-lambda/L3-239.jff) · [`L3-239.json`](../../automatas/lista3-afnd-lambda/L3-239.json) · [`L3-239.xml`](../../automatas/lista3-afnd-lambda/L3-239.xml). Tipo según la definición: **AFND-lambda**, |Q| = 26, Σ = {0, 1}, 32 transiciones.

**Diseño.** Unión de las dos condiciones.

<details><summary>Tabla de transiciones (26 estados)</summary>

| Estado | 0 | 1 | λ |
|---|---|---|---|
| →q0 | ∅ | ∅ | {q1, q2} |
| q1 | {q3} | ∅ | ∅ |
| q3 | ∅ | ∅ | {q6} |
| q6 | ∅ | {q10} | ∅ |
| q10 | ∅ | ∅ | {q14} |
| q14 | ∅ | ∅ | {q17, q18} |
| q18 | ∅ | ∅ | {q21, q22} |
| q21 | {q23} | ∅ | ∅ |
| q23 | ∅ | ∅ | {q25} |
| q22 | ∅ | {q24} | ∅ |
| q24 | ∅ | ∅ | {q25} |
| q25 | ∅ | ∅ | {q17, q18} |
| q17 | ∅ | ∅ | {q20} |
| q2 | ∅ | ∅ | {q4, q5} |
| q4 | ∅ | ∅ | {q7, q8} |
| q7 | {q11} | ∅ | ∅ |
| q11 | ∅ | ∅ | {q15} |
| q8 | ∅ | {q12} | ∅ |
| q12 | ∅ | ∅ | {q15} |
| q15 | ∅ | ∅ | {q4, q5} |
| q5 | ∅ | ∅ | {q9} |
| q9 | ∅ | {q13} | ∅ |
| q13 | ∅ | ∅ | {q16} |
| q16 | {q19} | ∅ | ∅ |
| q19 | ∅ | ∅ | {q20} |
| *q20 | ∅ | ∅ | ∅ |

</details>

**Transiciones λ.** Las λ son las de la construcción de Thompson (unión, estrella y concatenación).

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

<details><summary>λ-clausuras de los 26 estados</summary>

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0, q1, q2, q4, q5, q7, q8, q9} | no |
| q1 | {q1} | no |
| q3 | {q3, q6} | no |
| q6 | {q6} | no |
| q10 | {q10, q14, q17, q18, q20, q21, q22} | sí |
| q14 | {q14, q17, q18, q20, q21, q22} | sí |
| q18 | {q18, q21, q22} | no |
| q21 | {q21} | no |
| q23 | {q17, q18, q20, q21, q22, q23, q25} | sí |
| q22 | {q22} | no |
| q24 | {q17, q18, q20, q21, q22, q24, q25} | sí |
| q25 | {q17, q18, q20, q21, q22, q25} | sí |
| q17 | {q17, q20} | sí |
| q2 | {q2, q4, q5, q7, q8, q9} | no |
| q4 | {q4, q7, q8} | no |
| q7 | {q7} | no |
| q11 | {q11, q15, q4, q5, q7, q8, q9} | no |
| q8 | {q8} | no |
| q12 | {q12, q15, q4, q5, q7, q8, q9} | no |
| q15 | {q15, q4, q5, q7, q8, q9} | no |
| q5 | {q5, q9} | no |
| q9 | {q9} | no |
| q13 | {q13, q16} | no |
| q16 | {q16} | no |
| q19 | {q19, q20} | sí |
| q20 | {q20} | sí |

</details>

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `10` | acepta | acepta | acepta |
| 2 | `0010` | acepta | acepta | — |
| 3 | `0110` | acepta | acepta | — |
| 4 | `11011110` | acepta | acepta | — |
| 5 | `1100011100010` | acepta | acepta | — |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `11` | rechaza | rechaza | — |
| 8 | `0000` | rechaza | rechaza | — |
| 9 | `1100001` | rechaza | rechaza | — |
| 10 | `00101011100` | rechaza | rechaza | — |

<details><summary>Recorrido completo de cada cadena</summary>

1. `10`: {q0, q1, q2, q4, q5, q7, q8, q9} -1→ {q12, q13, q15, q16, q4, q5, q7, q8, q9} -0→ {q11, q15, q19, q20, q4, q5, q7, q8, q9} — ✔
  Árbol de cómputo: 13 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q2 -λ→ q5 -λ→ q9 -1→ q13 -λ→ q16 -0→ q19 -λ→ q20 — ✔ acepta
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q4 -λ→ q7 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 — ✘ termina fuera de F
2. `0010`: {q0, q1, q2, q4, q5, q7, q8, q9} -0→ {q11, q15, q3, q4, q5, q6, q7, q8, q9} -0→ {q11, q15, q4, q5, q7, q8, q9} -1→ {q12, q13, q15, q16, q4, q5, q7, q8, q9} -0→ {q11, q15, q19, q20, q4, q5, q7, q8, q9} — ✔
  Árbol de cómputo: 17 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q2 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q5 -λ→ q9 -1→ q13 -λ→ q16 -0→ q19 -λ→ q20 — ✔ acepta
    - q0 -λ→ q1 -0→ q3 -λ→ q6 — ✘ muere tras leer `0`
    - q0 -λ→ q2 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 — ✘ muere tras leer `00`
    - q0 -λ→ q2 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 — ✘ termina fuera de F
3. `0110`: {q0, q1, q2, q4, q5, q7, q8, q9} -0→ {q11, q15, q3, q4, q5, q6, q7, q8, q9} -1→ {q10, q12, q13, q14, q15, q16, q17, q18, q20, q21, q22, q4, q5, q7, q8, q9} -1→ {q12, q13, q15, q16, q17, q18, q20, q21, q22, q24, q25, q4, q5, q7, q8, q9} -0→ {q11, q15, q17, q18, q19, q20, q21, q22, q23, q25, q4, q5, q7, q8, q9} — ✔
  Árbol de cómputo: 27 caminos, 2 de aceptación (se muestran 6):
    - q0 -λ→ q1 -0→ q3 -λ→ q6 -1→ q10 -λ→ q14 -λ→ q18 -λ→ q22 -1→ q24 -λ→ q25 -λ→ q18 -λ→ q21 -0→ q23 -λ→ q25 -λ→ q17 -λ→ q20 — ✔ acepta
    - q0 -λ→ q2 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q5 -λ→ q9 -1→ q13 -λ→ q16 -0→ q19 -λ→ q20 — ✔ acepta
    - q0 -λ→ q1 -0→ q3 -λ→ q6 -1→ q10 -λ→ q14 -λ→ q17 -λ→ q20 — ✘ muere tras leer `01`
    - q0 -λ→ q1 -0→ q3 -λ→ q6 -1→ q10 -λ→ q14 -λ→ q18 -λ→ q21 — ✘ muere tras leer `01`
    - q0 -λ→ q1 -0→ q3 -λ→ q6 -1→ q10 -λ→ q14 -λ→ q18 -λ→ q22 -1→ q24 -λ→ q25 -λ→ q17 -λ→ q20 — ✘ muere tras leer `011`
    - q0 -λ→ q1 -0→ q3 -λ→ q6 -1→ q10 -λ→ q14 -λ→ q18 -λ→ q22 -1→ q24 -λ→ q25 -λ→ q18 -λ→ q21 -0→ q23 — ✘ termina fuera de F
4. `11011110`: {q0, q1, q2, q4, q5, q7, q8, q9} -1→ {q12, q13, q15, q16, q4, q5, q7, q8, q9} -1→ {q12, q13, q15, q16, q4, q5, q7, q8, q9} -0→ {q11, q15, q19, q20, q4, q5, q7, q8, q9} -1→ {q12, q13, q15, q16, q4, q5, q7, q8, q9} -1→ {q12, q13, q15, q16, q4, q5, q7, q8, q9} -1→ {q12, q13, q15, q16, q4, q5, q7, q8, q9} -1→ {q12, q13, q15, q16, q4, q5, q7, q8, q9} -0→ {q11, q15, q19, q20, q4, q5, q7, q8, q9} — ✔
  Árbol de cómputo: 25 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q2 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q5 -λ→ q9 -1→ q13 -λ→ q16 -0→ q19 -λ→ q20 — ✔ acepta
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q4 -λ→ q7 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q7 — ✘ muere tras leer `1`
    - q0 -λ→ q2 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 — ✘ muere tras leer `110`
    - q0 -λ→ q2 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q7 — ✘ muere tras leer `1101`
5. `1100011100010`: {q0, q1, q2, q4, q5, q7, q8, q9} -1→ {q12, q13, q15, q16, q4, q5, q7, q8, q9} -1→ {q12, q13, q15, q16, q4, q5, q7, q8, q9} -0→ {q11, q15, q19, q20, q4, q5, q7, q8, q9} -0→ {q11, q15, q4, q5, q7, q8, q9} -0→ {q11, q15, q4, q5, q7, q8, q9} -1→ {q12, q13, q15, q16, q4, q5, q7, q8, q9} -1→ {q12, q13, q15, q16, q4, q5, q7, q8, q9} -1→ {q12, q13, q15, q16, q4, q5, q7, q8, q9} -0→ {q11, q15, q19, q20, q4, q5, q7, q8, q9} -0→ {q11, q15, q4, q5, q7, q8, q9} -0→ {q11, q15, q4, q5, q7, q8, q9} -1→ {q12, q13, q15, q16, q4, q5, q7, q8, q9} -0→ {q11, q15, q19, q20, q4, q5, q7, q8, q9} — ✔
  Árbol de cómputo: 35 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q2 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q5 -λ→ q9 -1→ q13 -λ→ q16 -0→ q19 -λ→ q20 — ✔ acepta
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q4 -λ→ q7 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q7 — ✘ muere tras leer `1`
    - q0 -λ→ q2 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 — ✘ muere tras leer `11000`
    - q0 -λ→ q2 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q7 — ✘ muere tras leer `110001`
6. λ: {q0, q1, q2, q4, q5, q7, q8, q9} — ✘
  Árbol de cómputo: 8 caminos, 0 de aceptación (se muestran 6):
    - q0 — ✘ termina fuera de F
    - q0 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q2 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q4 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q4 -λ→ q7 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q4 -λ→ q8 — ✘ termina fuera de F
7. `11`: {q0, q1, q2, q4, q5, q7, q8, q9} -1→ {q12, q13, q15, q16, q4, q5, q7, q8, q9} -1→ {q12, q13, q15, q16, q4, q5, q7, q8, q9} — ✘
  Árbol de cómputo: 13 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q4 -λ→ q7 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q7 — ✘ muere tras leer `1`
    - q0 -λ→ q2 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q8 -1→ q12 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 — ✘ termina fuera de F
8. `0000`: {q0, q1, q2, q4, q5, q7, q8, q9} -0→ {q11, q15, q3, q4, q5, q6, q7, q8, q9} -0→ {q11, q15, q4, q5, q7, q8, q9} -0→ {q11, q15, q4, q5, q7, q8, q9} -0→ {q11, q15, q4, q5, q7, q8, q9} — ✘
  Árbol de cómputo: 16 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -0→ q3 -λ→ q6 — ✘ muere tras leer `0`
    - q0 -λ→ q2 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q8 — ✘ termina fuera de F
9. `1100001`: {q0, q1, q2, q4, q5, q7, q8, q9} -1→ {q12, q13, q15, q16, q4, q5, q7, q8, q9} -1→ {q12, q13, q15, q16, q4, q5, q7, q8, q9} -0→ {q11, q15, q19, q20, q4, q5, q7, q8, q9} -0→ {q11, q15, q4, q5, q7, q8, q9} -0→ {q11, q15, q4, q5, q7, q8, q9} -0→ {q11, q15, q4, q5, q7, q8, q9} -1→ {q12, q13, q15, q16, q4, q5, q7, q8, q9} — ✘
  Árbol de cómputo: 23 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q4 -λ→ q7 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q7 — ✘ muere tras leer `1`
    - q0 -λ→ q2 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 — ✘ muere tras leer `110000`
    - q0 -λ→ q2 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q8 -1→ q12 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 — ✘ termina fuera de F
10. `00101011100`: {q0, q1, q2, q4, q5, q7, q8, q9} -0→ {q11, q15, q3, q4, q5, q6, q7, q8, q9} -0→ {q11, q15, q4, q5, q7, q8, q9} -1→ {q12, q13, q15, q16, q4, q5, q7, q8, q9} -0→ {q11, q15, q19, q20, q4, q5, q7, q8, q9} -1→ {q12, q13, q15, q16, q4, q5, q7, q8, q9} -0→ {q11, q15, q19, q20, q4, q5, q7, q8, q9} -1→ {q12, q13, q15, q16, q4, q5, q7, q8, q9} -1→ {q12, q13, q15, q16, q4, q5, q7, q8, q9} -1→ {q12, q13, q15, q16, q4, q5, q7, q8, q9} -0→ {q11, q15, q19, q20, q4, q5, q7, q8, q9} -0→ {q11, q15, q4, q5, q7, q8, q9} — ✘
  Árbol de cómputo: 30 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -0→ q3 -λ→ q6 — ✘ muere tras leer `0`
    - q0 -λ→ q2 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 — ✘ muere tras leer `00`
    - q0 -λ→ q2 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 — ✘ muere tras leer `0010`
    - q0 -λ→ q2 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 — ✘ muere tras leer `001010`
    - q0 -λ→ q2 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q7 — ✘ muere tras leer `0010101`
    - q0 -λ→ q2 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q7 -0→ q11 -λ→ q15 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q8 -1→ q12 -λ→ q15 -λ→ q4 -λ→ q7 — ✘ muere tras leer `00101011`

</details>

Simulación paso a paso en JFLAP con `01`: [ver captura](../../evidencias/jflap/pasos/L3-239.png).

**Conversión.** AFND-λ (26 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 24 estados, [`L3-239-AFND.jff`](../../automatas/conversiones/L3-239-AFND.jff). AFND (24 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 9 estados, [`L3-239-AFD.jff`](../../automatas/conversiones/L3-239-AFD.jff) ([.json](../../automatas/conversiones/L3-239-AFD.json), [.xml](../../automatas/conversiones/L3-239-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 9 estados, y el AFD mínimo (Hopcroft), 6. La cota es 2^24 = 16777216. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-240"></a>

## Lista 3, problema 240

**Enunciado.** Cadenas de longitud par que contienen 01. Encontrar una expresión regular.

**Clasificación: AFND-λ.** La respuesta es una expresión regular; su AFND-λ de Thompson es la forma de simularla. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

**Expresión regular** (archivo de JFLAP [`L3-240-ER.jff`](../../automatas/lista3-afnd-lambda/L3-240-ER.jff)): `((0+1)(0+1))*01((0+1)(0+1))*+((0+1)(0+1))*(0+1)01(0+1)((0+1)(0+1))*` (en JFLAP, `+` es la unión y `!` es λ).

#### AFND-λ de Thompson de la expresión — `L3-240`

Archivos: [`L3-240.jff`](../../automatas/lista3-afnd-lambda/L3-240.jff) · [`L3-240.json`](../../automatas/lista3-afnd-lambda/L3-240.json) · [`L3-240.xml`](../../automatas/lista3-afnd-lambda/L3-240.xml). Tipo según la definición: **AFND-lambda**, |Q| = 78, Σ = {0, 1}, 96 transiciones.

**Diseño.** Con E = ((0+1)(0+1))*: o 01 empieza en posición par (E 01 E), o en impar (E(0+1)01(0+1)E).

<details><summary>Tabla de transiciones (78 estados)</summary>

| Estado | 0 | 1 | λ |
|---|---|---|---|
| →q0 | ∅ | ∅ | {q1, q2} |
| q1 | ∅ | ∅ | {q3, q4} |
| q4 | ∅ | ∅ | {q8, q9} |
| q8 | {q14} | ∅ | ∅ |
| q14 | ∅ | ∅ | {q21} |
| q9 | ∅ | {q15} | ∅ |
| q15 | ∅ | ∅ | {q21} |
| q21 | ∅ | ∅ | {q26} |
| q26 | ∅ | ∅ | {q30, q31} |
| q31 | {q38} | ∅ | ∅ |
| q38 | ∅ | ∅ | {q45} |
| q30 | ∅ | {q37} | ∅ |
| q37 | ∅ | ∅ | {q45} |
| q45 | ∅ | ∅ | {q3, q4} |
| q3 | ∅ | ∅ | {q7} |
| q7 | {q13} | ∅ | ∅ |
| q13 | ∅ | ∅ | {q20} |
| q20 | ∅ | {q25} | ∅ |
| q25 | ∅ | ∅ | {q29} |
| q29 | ∅ | ∅ | {q35, q36} |
| q35 | ∅ | ∅ | {q42, q43} |
| q42 | {q48} | ∅ | ∅ |
| q48 | ∅ | ∅ | {q51} |
| q43 | ∅ | {q49} | ∅ |
| q49 | ∅ | ∅ | {q51} |
| q51 | ∅ | ∅ | {q53} |
| q53 | ∅ | ∅ | {q56, q57} |
| q56 | {q60} | ∅ | ∅ |
| q60 | ∅ | ∅ | {q63} |
| q57 | ∅ | {q61} | ∅ |
| q61 | ∅ | ∅ | {q63} |
| q63 | ∅ | ∅ | {q35, q36} |
| q36 | ∅ | ∅ | {q44} |
| q2 | ∅ | ∅ | {q5, q6} |
| q5 | ∅ | ∅ | {q10, q11} |
| q10 | {q16} | ∅ | ∅ |
| q16 | ∅ | ∅ | {q22} |
| q11 | ∅ | {q17} | ∅ |
| q17 | ∅ | ∅ | {q22} |
| q22 | ∅ | ∅ | {q27} |
| q27 | ∅ | ∅ | {q32, q33} |
| q32 | {q39} | ∅ | ∅ |
| q39 | ∅ | ∅ | {q46} |
| q33 | ∅ | {q40} | ∅ |
| q40 | ∅ | ∅ | {q46} |
| q46 | ∅ | ∅ | {q5, q6} |
| q6 | ∅ | ∅ | {q12} |
| q12 | ∅ | ∅ | {q18, q19} |
| q18 | {q23} | ∅ | ∅ |
| q23 | ∅ | ∅ | {q28} |
| q19 | ∅ | {q24} | ∅ |
| q24 | ∅ | ∅ | {q28} |
| q28 | ∅ | ∅ | {q34} |
| q34 | {q41} | ∅ | ∅ |
| q41 | ∅ | ∅ | {q47} |
| q47 | ∅ | {q50} | ∅ |
| q50 | ∅ | ∅ | {q52} |
| q52 | ∅ | ∅ | {q54, q55} |
| q54 | {q58} | ∅ | ∅ |
| q58 | ∅ | ∅ | {q62} |
| q55 | ∅ | {q59} | ∅ |
| q59 | ∅ | ∅ | {q62} |
| q62 | ∅ | ∅ | {q64} |
| q64 | ∅ | ∅ | {q65, q66} |
| q65 | ∅ | ∅ | {q67, q68} |
| q67 | {q69} | ∅ | ∅ |
| q69 | ∅ | ∅ | {q71} |
| q68 | ∅ | {q70} | ∅ |
| q70 | ∅ | ∅ | {q71} |
| q71 | ∅ | ∅ | {q72} |
| q72 | ∅ | ∅ | {q73, q74} |
| q73 | {q75} | ∅ | ∅ |
| q75 | ∅ | ∅ | {q77} |
| q74 | ∅ | {q76} | ∅ |
| q76 | ∅ | ∅ | {q77} |
| q77 | ∅ | ∅ | {q65, q66} |
| q66 | ∅ | ∅ | {q44} |
| *q44 | ∅ | ∅ | ∅ |

</details>

**Transiciones λ.** Las λ son las de la construcción de Thompson (unión, estrella y concatenación).

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

<details><summary>λ-clausuras de los 78 estados</summary>

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0, q1, q10, q11, q12, q18, q19, q2, q3, q4, q5, q6, q7, q8, q9} | no |
| q1 | {q1, q3, q4, q7, q8, q9} | no |
| q4 | {q4, q8, q9} | no |
| q8 | {q8} | no |
| q14 | {q14, q21, q26, q30, q31} | no |
| q9 | {q9} | no |
| q15 | {q15, q21, q26, q30, q31} | no |
| q21 | {q21, q26, q30, q31} | no |
| q26 | {q26, q30, q31} | no |
| q31 | {q31} | no |
| q38 | {q3, q38, q4, q45, q7, q8, q9} | no |
| q30 | {q30} | no |
| q37 | {q3, q37, q4, q45, q7, q8, q9} | no |
| q45 | {q3, q4, q45, q7, q8, q9} | no |
| q3 | {q3, q7} | no |
| q7 | {q7} | no |
| q13 | {q13, q20} | no |
| q20 | {q20} | no |
| q25 | {q25, q29, q35, q36, q42, q43, q44} | sí |
| q29 | {q29, q35, q36, q42, q43, q44} | sí |
| q35 | {q35, q42, q43} | no |
| q42 | {q42} | no |
| q48 | {q48, q51, q53, q56, q57} | no |
| q43 | {q43} | no |
| q49 | {q49, q51, q53, q56, q57} | no |
| q51 | {q51, q53, q56, q57} | no |
| q53 | {q53, q56, q57} | no |
| q56 | {q56} | no |
| q60 | {q35, q36, q42, q43, q44, q60, q63} | sí |
| q57 | {q57} | no |
| q61 | {q35, q36, q42, q43, q44, q61, q63} | sí |
| q63 | {q35, q36, q42, q43, q44, q63} | sí |
| q36 | {q36, q44} | sí |
| q2 | {q10, q11, q12, q18, q19, q2, q5, q6} | no |
| q5 | {q10, q11, q5} | no |
| q10 | {q10} | no |
| q16 | {q16, q22, q27, q32, q33} | no |
| q11 | {q11} | no |
| q17 | {q17, q22, q27, q32, q33} | no |
| q22 | {q22, q27, q32, q33} | no |
| q27 | {q27, q32, q33} | no |
| q32 | {q32} | no |
| q39 | {q10, q11, q12, q18, q19, q39, q46, q5, q6} | no |
| q33 | {q33} | no |
| q40 | {q10, q11, q12, q18, q19, q40, q46, q5, q6} | no |
| q46 | {q10, q11, q12, q18, q19, q46, q5, q6} | no |
| q6 | {q12, q18, q19, q6} | no |
| q12 | {q12, q18, q19} | no |
| q18 | {q18} | no |
| q23 | {q23, q28, q34} | no |
| q19 | {q19} | no |
| q24 | {q24, q28, q34} | no |
| q28 | {q28, q34} | no |
| q34 | {q34} | no |
| q41 | {q41, q47} | no |
| q47 | {q47} | no |
| q50 | {q50, q52, q54, q55} | no |
| q52 | {q52, q54, q55} | no |
| q54 | {q54} | no |
| q58 | {q44, q58, q62, q64, q65, q66, q67, q68} | sí |
| q55 | {q55} | no |
| q59 | {q44, q59, q62, q64, q65, q66, q67, q68} | sí |
| q62 | {q44, q62, q64, q65, q66, q67, q68} | sí |
| q64 | {q44, q64, q65, q66, q67, q68} | sí |
| q65 | {q65, q67, q68} | no |
| q67 | {q67} | no |
| q69 | {q69, q71, q72, q73, q74} | no |
| q68 | {q68} | no |
| q70 | {q70, q71, q72, q73, q74} | no |
| q71 | {q71, q72, q73, q74} | no |
| q72 | {q72, q73, q74} | no |
| q73 | {q73} | no |
| q75 | {q44, q65, q66, q67, q68, q75, q77} | sí |
| q74 | {q74} | no |
| q76 | {q44, q65, q66, q67, q68, q76, q77} | sí |
| q77 | {q44, q65, q66, q67, q68, q77} | sí |
| q66 | {q44, q66} | sí |
| q44 | {q44} | sí |

</details>

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `01` | acepta | acepta | acepta |
| 2 | `1001` | acepta | acepta | acepta |
| 3 | `1101` | acepta | acepta | acepta |
| 4 | `10101000` | acepta | acepta | acepta |
| 5 | `011111110010` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `010` | rechaza | rechaza | rechaza |
| 8 | `0000` | rechaza | rechaza | rechaza |
| 9 | `1110111` | rechaza | rechaza | rechaza |
| 10 | `00001101001` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `01`: {q0, q1, q10, q11, q12, q18, q19, q2, q3, q4, q5, q6, q7, q8, q9} -0→ {q13, q14, q16, q20, q21, q22, q23, q26, q27, q28, q30, q31, q32, q33, q34} -1→ {q10, q11, q12, q18, q19, q25, q29, q3, q35, q36, q37, q4, q40, q42, q43, q44, q45, q46, q5, q6, q7, q8, q9} — ✔
  Árbol de cómputo: 29 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -0→ q13 -λ→ q20 -1→ q25 -λ→ q29 -λ→ q36 -λ→ q44 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -0→ q13 -λ→ q20 -1→ q25 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -0→ q13 -λ→ q20 -1→ q25 -λ→ q29 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -0→ q13 -λ→ q20 -1→ q25 -λ→ q29 -λ→ q35 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -0→ q13 -λ→ q20 -1→ q25 -λ→ q29 -λ→ q35 -λ→ q42 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -0→ q13 -λ→ q20 -1→ q25 -λ→ q29 -λ→ q35 -λ→ q43 — ✘ termina fuera de F
2. `1001`: {q0, q1, q10, q11, q12, q18, q19, q2, q3, q4, q5, q6, q7, q8, q9} -1→ {q15, q17, q21, q22, q24, q26, q27, q28, q30, q31, q32, q33, q34} -0→ {q10, q11, q12, q18, q19, q3, q38, q39, q4, q41, q45, q46, q47, q5, q6, q7, q8, q9} -0→ {q13, q14, q16, q20, q21, q22, q23, q26, q27, q28, q30, q31, q32, q33, q34} -1→ {q10, q11, q12, q18, q19, q25, q29, q3, q35, q36, q37, q4, q40, q42, q43, q44, q45, q46, q5, q6, q7, q8, q9} — ✔
  Árbol de cómputo: 36 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q4 -λ→ q9 -1→ q15 -λ→ q21 -λ→ q26 -λ→ q31 -0→ q38 -λ→ q45 -λ→ q3 -λ→ q7 -0→ q13 -λ→ q20 -1→ q25 -λ→ q29 -λ→ q36 -λ→ q44 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q9 -1→ q15 -λ→ q21 -λ→ q26 -λ→ q30 — ✘ muere tras leer `1`
    - q0 -λ→ q1 -λ→ q4 -λ→ q9 -1→ q15 -λ→ q21 -λ→ q26 -λ→ q31 -0→ q38 -λ→ q45 -λ→ q3 -λ→ q7 -0→ q13 -λ→ q20 -1→ q25 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -λ→ q9 -1→ q15 -λ→ q21 -λ→ q26 -λ→ q31 -0→ q38 -λ→ q45 -λ→ q3 -λ→ q7 -0→ q13 -λ→ q20 -1→ q25 -λ→ q29 — ✘ termina fuera de F
3. `1101`: {q0, q1, q10, q11, q12, q18, q19, q2, q3, q4, q5, q6, q7, q8, q9} -1→ {q15, q17, q21, q22, q24, q26, q27, q28, q30, q31, q32, q33, q34} -1→ {q10, q11, q12, q18, q19, q3, q37, q4, q40, q45, q46, q5, q6, q7, q8, q9} -0→ {q13, q14, q16, q20, q21, q22, q23, q26, q27, q28, q30, q31, q32, q33, q34} -1→ {q10, q11, q12, q18, q19, q25, q29, q3, q35, q36, q37, q4, q40, q42, q43, q44, q45, q46, q5, q6, q7, q8, q9} — ✔
  Árbol de cómputo: 36 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q4 -λ→ q9 -1→ q15 -λ→ q21 -λ→ q26 -λ→ q30 -1→ q37 -λ→ q45 -λ→ q3 -λ→ q7 -0→ q13 -λ→ q20 -1→ q25 -λ→ q29 -λ→ q36 -λ→ q44 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q9 -1→ q15 -λ→ q21 -λ→ q26 -λ→ q30 -1→ q37 -λ→ q45 -λ→ q3 -λ→ q7 -0→ q13 -λ→ q20 -1→ q25 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -λ→ q9 -1→ q15 -λ→ q21 -λ→ q26 -λ→ q30 -1→ q37 -λ→ q45 -λ→ q3 -λ→ q7 -0→ q13 -λ→ q20 -1→ q25 -λ→ q29 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -λ→ q9 -1→ q15 -λ→ q21 -λ→ q26 -λ→ q30 -1→ q37 -λ→ q45 -λ→ q3 -λ→ q7 -0→ q13 -λ→ q20 -1→ q25 -λ→ q29 -λ→ q35 — ✘ termina fuera de F
4. `10101000`: {q0, q1, q10, q11, q12, q18, q19, q2, q3, q4, q5, q6, q7, q8, q9} -1→ {q15, q17, q21, q22, q24, q26, q27, q28, q30, q31, q32, q33, q34} -0→ {q10, q11, q12, q18, q19, q3, q38, q39, q4, q41, q45, q46, q47, q5, q6, q7, q8, q9} -1→ {q15, q17, q21, q22, q24, q26, q27, q28, q30, q31, q32, q33, q34, q50, q52, q54, q55} -0→ {q10, q11, q12, q18, q19, q3, q38, q39, q4, q41, q44, q45, q46, q47, q5, q58, q6, q62, q64, q65, q66, q67, q68, q7, q8, q9} -1→ {q15, q17, q21, q22, q24, q26, q27, q28, q30, q31, q32, q33, q34, q50, q52, q54, q55, q70, q71, q72, q73, q74} -0→ {q10, q11, q12, q18, q19, q3, q38, q39, q4, q41, q44, q45, q46, q47, q5, q58, q6, q62, q64, q65, q66, q67, q68, q7, q75, q77, q8, q9} -0→ {q13, q14, q16, q20, q21, q22, q23, q26, q27, q28, q30, q31, q32, q33, q34, q69, q71, q72, q73, q74} -0→ {q10, q11, q12, q18, q19, q3, q38, q39, q4, q41, q44, q45, q46, q47, q5, q6, q65, q66, q67, q68, q7, q75, q77, q8, q9} — ✔
  Árbol de cómputo: 68 caminos, 2 de aceptación (se muestran 6):
    - q0 -λ→ q2 -λ→ q5 -λ→ q11 -1→ q17 -λ→ q22 -λ→ q27 -λ→ q32 -0→ q39 -λ→ q46 -λ→ q6 -λ→ q12 -λ→ q19 -1→ q24 -λ→ q28 -λ→ q34 -0→ q41 -λ→ q47 -1→ q50 -λ→ q52 -λ→ q54 -0→ q58 -λ→ q62 -λ→ q64 -λ→ q65 -λ→ q67 -0→ q69 -λ→ q71 -λ→ q72 -λ→ q73 -0→ q75 -λ→ q77 -λ→ q66 -λ→ q44 — ✔ acepta
    - q0 -λ→ q2 -λ→ q6 -λ→ q12 -λ→ q19 -1→ q24 -λ→ q28 -λ→ q34 -0→ q41 -λ→ q47 -1→ q50 -λ→ q52 -λ→ q54 -0→ q58 -λ→ q62 -λ→ q64 -λ→ q65 -λ→ q68 -1→ q70 -λ→ q71 -λ→ q72 -λ→ q73 -0→ q75 -λ→ q77 -λ→ q65 -λ→ q67 -0→ q69 -λ→ q71 -λ→ q72 -λ→ q73 -0→ q75 -λ→ q77 -λ→ q66 -λ→ q44 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q9 -1→ q15 -λ→ q21 -λ→ q26 -λ→ q30 — ✘ muere tras leer `1`
    - q0 -λ→ q1 -λ→ q4 -λ→ q9 -1→ q15 -λ→ q21 -λ→ q26 -λ→ q31 -0→ q38 -λ→ q45 -λ→ q3 -λ→ q7 — ✘ muere tras leer `10`
5. `011111110010`: {q0, q1, q10, q11, q12, q18, q19, q2, q3, q4, q5, q6, q7, q8, q9} -0→ {q13, q14, q16, q20, q21, q22, q23, q26, q27, q28, q30, q31, q32, q33, q34} -1→ {q10, q11, q12, q18, q19, q25, q29, q3, q35, q36, q37, q4, q40, q42, q43, q44, q45, q46, q5, q6, q7, q8, q9} -1→ {q15, q17, q21, q22, q24, q26, q27, q28, q30, q31, q32, q33, q34, q49, q51, q53, q56, q57} -1→ {q10, q11, q12, q18, q19, q3, q35, q36, q37, q4, q40, q42, q43, q44, q45, q46, q5, q6, q61, q63, q7, q8, q9} -1→ {q15, q17, q21, q22, q24, q26, q27, q28, q30, q31, q32, q33, q34, q49, q51, q53, q56, q57} -1→ {q10, q11, q12, q18, q19, q3, q35, q36, q37, q4, q40, q42, q43, q44, q45, q46, q5, q6, q61, q63, q7, q8, q9} -1→ {q15, q17, q21, q22, q24, q26, q27, q28, q30, q31, q32, q33, q34, q49, q51, q53, q56, q57} -1→ {q10, q11, q12, q18, q19, q3, q35, q36, q37, q4, q40, q42, q43, q44, q45, q46, q5, q6, q61, q63, q7, q8, q9} -0→ {q13, q14, q16, q20, q21, q22, q23, q26, q27, q28, q30, q31, q32, q33, q34, q48, q51, q53, q56, q57} -0→ {q10, q11, q12, q18, q19, q3, q35, q36, q38, q39, q4, q41, q42, q43, q44, q45, q46, q47, q5, q6, q60, q63, q7, q8, q9} -1→ {q15, q17, q21, q22, q24, q26, q27, q28, q30, q31, q32, q33, q34, q49, q50, q51, q52, q53, q54, q55, q56, q57} -0→ {q10, q11, q12, q18, q19, q3, q35, q36, q38, q39, q4, q41, q42, q43, q44, q45, q46, q47, q5, q58, q6, q60, q62, q63, q64, q65, q66, q67, q68, q7, q8, q9} — ✔
  Árbol de cómputo: 88 caminos, 2 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -0→ q13 -λ→ q20 -1→ q25 -λ→ q29 -λ→ q35 -λ→ q43 -1→ q49 -λ→ q51 -λ→ q53 -λ→ q57 -1→ q61 -λ→ q63 -λ→ q35 -λ→ q43 -1→ q49 -λ→ q51 -λ→ q53 -λ→ q57 -1→ q61 -λ→ q63 -λ→ q35 -λ→ q43 -1→ q49 -λ→ q51 -λ→ q53 -λ→ q57 -1→ q61 -λ→ q63 -λ→ q35 -λ→ q42 -0→ q48 -λ→ q51 -λ→ q53 -λ→ q56 -0→ q60 -λ→ q63 -λ→ q35 -λ→ q43 -1→ q49 -λ→ q51 -λ→ q53 -λ→ q56 -0→ q60 -λ→ q63 -λ→ q36 -λ→ q44 — ✔ acepta
    - q0 -λ→ q2 -λ→ q5 -λ→ q10 -0→ q16 -λ→ q22 -λ→ q27 -λ→ q33 -1→ q40 -λ→ q46 -λ→ q5 -λ→ q11 -1→ q17 -λ→ q22 -λ→ q27 -λ→ q33 -1→ q40 -λ→ q46 -λ→ q5 -λ→ q11 -1→ q17 -λ→ q22 -λ→ q27 -λ→ q33 -1→ q40 -λ→ q46 -λ→ q5 -λ→ q11 -1→ q17 -λ→ q22 -λ→ q27 -λ→ q33 -1→ q40 -λ→ q46 -λ→ q6 -λ→ q12 -λ→ q18 -0→ q23 -λ→ q28 -λ→ q34 -0→ q41 -λ→ q47 -1→ q50 -λ→ q52 -λ→ q54 -0→ q58 -λ→ q62 -λ→ q64 -λ→ q66 -λ→ q44 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -0→ q13 -λ→ q20 -1→ q25 -λ→ q29 -λ→ q35 -λ→ q42 — ✘ muere tras leer `01`
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -0→ q13 -λ→ q20 -1→ q25 -λ→ q29 -λ→ q35 -λ→ q43 -1→ q49 -λ→ q51 -λ→ q53 -λ→ q56 — ✘ muere tras leer `011`
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -0→ q13 -λ→ q20 -1→ q25 -λ→ q29 -λ→ q35 -λ→ q43 -1→ q49 -λ→ q51 -λ→ q53 -λ→ q57 -1→ q61 -λ→ q63 -λ→ q35 -λ→ q42 — ✘ muere tras leer `0111`
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -0→ q13 -λ→ q20 -1→ q25 -λ→ q29 -λ→ q35 -λ→ q43 -1→ q49 -λ→ q51 -λ→ q53 -λ→ q57 -1→ q61 -λ→ q63 -λ→ q35 -λ→ q43 -1→ q49 -λ→ q51 -λ→ q53 -λ→ q56 — ✘ muere tras leer `01111`
6. λ: {q0, q1, q10, q11, q12, q18, q19, q2, q3, q4, q5, q6, q7, q8, q9} — ✘
  Árbol de cómputo: 15 caminos, 0 de aceptación (se muestran 6):
    - q0 — ✘ termina fuera de F
    - q0 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 — ✘ termina fuera de F
7. `010`: {q0, q1, q10, q11, q12, q18, q19, q2, q3, q4, q5, q6, q7, q8, q9} -0→ {q13, q14, q16, q20, q21, q22, q23, q26, q27, q28, q30, q31, q32, q33, q34} -1→ {q10, q11, q12, q18, q19, q25, q29, q3, q35, q36, q37, q4, q40, q42, q43, q44, q45, q46, q5, q6, q7, q8, q9} -0→ {q13, q14, q16, q20, q21, q22, q23, q26, q27, q28, q30, q31, q32, q33, q34, q48, q51, q53, q56, q57} — ✘
  Árbol de cómputo: 31 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -0→ q13 -λ→ q20 -1→ q25 -λ→ q29 -λ→ q35 -λ→ q42 -0→ q48 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -0→ q13 -λ→ q20 -1→ q25 -λ→ q29 -λ→ q35 -λ→ q42 -0→ q48 -λ→ q51 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -0→ q13 -λ→ q20 -1→ q25 -λ→ q29 -λ→ q35 -λ→ q42 -0→ q48 -λ→ q51 -λ→ q53 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -0→ q13 -λ→ q20 -1→ q25 -λ→ q29 -λ→ q35 -λ→ q42 -0→ q48 -λ→ q51 -λ→ q53 -λ→ q56 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -0→ q13 -λ→ q20 -1→ q25 -λ→ q29 -λ→ q35 -λ→ q42 -0→ q48 -λ→ q51 -λ→ q53 -λ→ q57 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -0→ q13 -λ→ q20 -1→ q25 -λ→ q29 -λ→ q35 -λ→ q43 — ✘ muere tras leer `01`
8. `0000`: {q0, q1, q10, q11, q12, q18, q19, q2, q3, q4, q5, q6, q7, q8, q9} -0→ {q13, q14, q16, q20, q21, q22, q23, q26, q27, q28, q30, q31, q32, q33, q34} -0→ {q10, q11, q12, q18, q19, q3, q38, q39, q4, q41, q45, q46, q47, q5, q6, q7, q8, q9} -0→ {q13, q14, q16, q20, q21, q22, q23, q26, q27, q28, q30, q31, q32, q33, q34} -0→ {q10, q11, q12, q18, q19, q3, q38, q39, q4, q41, q45, q46, q47, q5, q6, q7, q8, q9} — ✘
  Árbol de cómputo: 31 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -0→ q13 -λ→ q20 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -0→ q14 -λ→ q21 -λ→ q26 -λ→ q30 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -0→ q14 -λ→ q21 -λ→ q26 -λ→ q31 -0→ q38 -λ→ q45 -λ→ q3 -λ→ q7 -0→ q13 -λ→ q20 — ✘ muere tras leer `000`
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -0→ q14 -λ→ q21 -λ→ q26 -λ→ q31 -0→ q38 -λ→ q45 -λ→ q4 -λ→ q8 -0→ q14 -λ→ q21 -λ→ q26 -λ→ q30 — ✘ muere tras leer `000`
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -0→ q14 -λ→ q21 -λ→ q26 -λ→ q31 -0→ q38 -λ→ q45 -λ→ q4 -λ→ q8 -0→ q14 -λ→ q21 -λ→ q26 -λ→ q31 -0→ q38 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -0→ q14 -λ→ q21 -λ→ q26 -λ→ q31 -0→ q38 -λ→ q45 -λ→ q4 -λ→ q8 -0→ q14 -λ→ q21 -λ→ q26 -λ→ q31 -0→ q38 -λ→ q45 — ✘ termina fuera de F
9. `1110111`: {q0, q1, q10, q11, q12, q18, q19, q2, q3, q4, q5, q6, q7, q8, q9} -1→ {q15, q17, q21, q22, q24, q26, q27, q28, q30, q31, q32, q33, q34} -1→ {q10, q11, q12, q18, q19, q3, q37, q4, q40, q45, q46, q5, q6, q7, q8, q9} -1→ {q15, q17, q21, q22, q24, q26, q27, q28, q30, q31, q32, q33, q34} -0→ {q10, q11, q12, q18, q19, q3, q38, q39, q4, q41, q45, q46, q47, q5, q6, q7, q8, q9} -1→ {q15, q17, q21, q22, q24, q26, q27, q28, q30, q31, q32, q33, q34, q50, q52, q54, q55} -1→ {q10, q11, q12, q18, q19, q3, q37, q4, q40, q44, q45, q46, q5, q59, q6, q62, q64, q65, q66, q67, q68, q7, q8, q9} -1→ {q15, q17, q21, q22, q24, q26, q27, q28, q30, q31, q32, q33, q34, q70, q71, q72, q73, q74} — ✘
  Árbol de cómputo: 45 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q9 -1→ q15 -λ→ q21 -λ→ q26 -λ→ q30 -1→ q37 -λ→ q45 -λ→ q3 -λ→ q7 — ✘ muere tras leer `11`
    - q0 -λ→ q1 -λ→ q4 -λ→ q9 -1→ q15 -λ→ q21 -λ→ q26 -λ→ q30 -1→ q37 -λ→ q45 -λ→ q4 -λ→ q8 — ✘ muere tras leer `11`
    - q0 -λ→ q1 -λ→ q4 -λ→ q9 -1→ q15 -λ→ q21 -λ→ q26 -λ→ q30 -1→ q37 -λ→ q45 -λ→ q4 -λ→ q9 -1→ q15 -λ→ q21 -λ→ q26 -λ→ q30 — ✘ muere tras leer `111`
    - q0 -λ→ q1 -λ→ q4 -λ→ q9 -1→ q15 -λ→ q21 -λ→ q26 -λ→ q30 -1→ q37 -λ→ q45 -λ→ q4 -λ→ q9 -1→ q15 -λ→ q21 -λ→ q26 -λ→ q31 -0→ q38 -λ→ q45 -λ→ q3 -λ→ q7 — ✘ muere tras leer `1110`
10. `00001101001`: {q0, q1, q10, q11, q12, q18, q19, q2, q3, q4, q5, q6, q7, q8, q9} -0→ {q13, q14, q16, q20, q21, q22, q23, q26, q27, q28, q30, q31, q32, q33, q34} -0→ {q10, q11, q12, q18, q19, q3, q38, q39, q4, q41, q45, q46, q47, q5, q6, q7, q8, q9} -0→ {q13, q14, q16, q20, q21, q22, q23, q26, q27, q28, q30, q31, q32, q33, q34} -0→ {q10, q11, q12, q18, q19, q3, q38, q39, q4, q41, q45, q46, q47, q5, q6, q7, q8, q9} -1→ {q15, q17, q21, q22, q24, q26, q27, q28, q30, q31, q32, q33, q34, q50, q52, q54, q55} -1→ {q10, q11, q12, q18, q19, q3, q37, q4, q40, q44, q45, q46, q5, q59, q6, q62, q64, q65, q66, q67, q68, q7, q8, q9} -0→ {q13, q14, q16, q20, q21, q22, q23, q26, q27, q28, q30, q31, q32, q33, q34, q69, q71, q72, q73, q74} -1→ {q10, q11, q12, q18, q19, q25, q29, q3, q35, q36, q37, q4, q40, q42, q43, q44, q45, q46, q5, q6, q65, q66, q67, q68, q7, q76, q77, q8, q9} -0→ {q13, q14, q16, q20, q21, q22, q23, q26, q27, q28, q30, q31, q32, q33, q34, q48, q51, q53, q56, q57, q69, q71, q72, q73, q74} -0→ {q10, q11, q12, q18, q19, q3, q35, q36, q38, q39, q4, q41, q42, q43, q44, q45, q46, q47, q5, q6, q60, q63, q65, q66, q67, q68, q7, q75, q77, q8, q9} -1→ {q15, q17, q21, q22, q24, q26, q27, q28, q30, q31, q32, q33, q34, q49, q50, q51, q52, q53, q54, q55, q56, q57, q70, q71, q72, q73, q74} — ✘
  Árbol de cómputo: 77 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -0→ q13 -λ→ q20 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -0→ q14 -λ→ q21 -λ→ q26 -λ→ q30 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -0→ q14 -λ→ q21 -λ→ q26 -λ→ q31 -0→ q38 -λ→ q45 -λ→ q3 -λ→ q7 -0→ q13 -λ→ q20 — ✘ muere tras leer `000`
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -0→ q14 -λ→ q21 -λ→ q26 -λ→ q31 -0→ q38 -λ→ q45 -λ→ q4 -λ→ q8 -0→ q14 -λ→ q21 -λ→ q26 -λ→ q30 — ✘ muere tras leer `000`
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -0→ q14 -λ→ q21 -λ→ q26 -λ→ q31 -0→ q38 -λ→ q45 -λ→ q4 -λ→ q8 -0→ q14 -λ→ q21 -λ→ q26 -λ→ q31 -0→ q38 -λ→ q45 -λ→ q3 -λ→ q7 — ✘ muere tras leer `0000`
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -0→ q14 -λ→ q21 -λ→ q26 -λ→ q31 -0→ q38 -λ→ q45 -λ→ q4 -λ→ q8 -0→ q14 -λ→ q21 -λ→ q26 -λ→ q31 -0→ q38 -λ→ q45 -λ→ q4 -λ→ q8 — ✘ muere tras leer `0000`

</details>

Simulación paso a paso en JFLAP con `01`: [ver captura](../../evidencias/jflap/pasos/L3-240.png).

**Conversión.** AFND-λ (78 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 76 estados, [`L3-240-AFND.jff`](../../automatas/conversiones/L3-240-AFND.jff). AFND (76 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 33 estados, [`L3-240-AFD.jff`](../../automatas/conversiones/L3-240-AFD.jff) ([.json](../../automatas/conversiones/L3-240-AFD.json), [.xml](../../automatas/conversiones/L3-240-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 33 estados, y el AFD mínimo (Hopcroft), 6. La cota es 2^76 = 75557863725914323419136. Se verificó que los tres autómatas aceptan el mismo lenguaje.

