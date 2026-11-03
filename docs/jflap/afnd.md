# Ejercicio 2 — AFND estándar

[← Ejercicio 2](../02-jflap.md) · [Índice](../../README.md)

Cada autómata indica su clasificación, el diseño, la tabla de transiciones, cinco cadenas válidas y cinco inválidas con el resultado esperado (oráculo escrito a partir del enunciado), el del simulador de este proyecto y el del motor de JFLAP 7.1, el recorrido de cada cadena (en los no deterministas, el conjunto de estados activos y el árbol de caminos) y la captura de la simulación paso a paso en JFLAP.

<a id="problema-2-143b"></a>

## Lista 2, problema 143b

**Enunciado.** Lenguaje del autómata de la figura (b).

**Clasificación: AFND.** La figura (b) tiene dos transiciones con b desde q1 y ninguna con b desde q0: es no determinista. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### Lenguaje del autómata de la figura (b). — `L2-143b`

Archivos: [`L2-143b.jff`](../../automatas/lista3-afnd/L2-143b.jff) · [`L2-143b.json`](../../automatas/lista3-afnd/L2-143b.json) · [`L2-143b.xml`](../../automatas/lista3-afnd/L2-143b.xml). Tipo según la definición: **AFND**, |Q| = 2, Σ = {a, b}, 4 transiciones.

**Diseño.** Transcripción de la figura: q0 -a→ q1, lazos a y b en q1, y q1 -b→ q0. Es no determinista en (q1, b) y q0 no tiene transición con b. Si la palabra empieza con a, el camino que se queda en q1 la acepta; si empieza con b, el cómputo muere; λ termina en q0. L = a(a+b)*.

| Estado | a | b |
|---|---|---|
| *q1 | {q1} | {q0, q1} |
| →q0 | {q1} | ∅ |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `a` | acepta | acepta | acepta |
| 2 | `ab` | acepta | acepta | acepta |
| 3 | `abba` | acepta | acepta | acepta |
| 4 | `aababaa` | acepta | acepta | acepta |
| 5 | `ababaaaabbb` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `bb` | rechaza | rechaza | rechaza |
| 8 | `baab` | rechaza | rechaza | rechaza |
| 9 | `bbaaabb` | rechaza | rechaza | rechaza |
| 10 | `bbaaaaaabbb` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `a`: {q0} -a→ {q1} — ✔
  Árbol de cómputo: 1 caminos, 1 de aceptación:
    - q0 -a→ q1 — ✔ acepta
2. `ab`: {q0} -a→ {q1} -b→ {q0, q1} — ✔
  Árbol de cómputo: 2 caminos, 1 de aceptación:
    - q0 -a→ q1 -b→ q1 — ✔ acepta
    - q0 -a→ q1 -b→ q0 — ✘ termina fuera de F
3. `abba`: {q0} -a→ {q1} -b→ {q0, q1} -b→ {q0, q1} -a→ {q1} — ✔
  Árbol de cómputo: 3 caminos, 2 de aceptación:
    - q0 -a→ q1 -b→ q1 -b→ q0 -a→ q1 — ✔ acepta
    - q0 -a→ q1 -b→ q1 -b→ q1 -a→ q1 — ✔ acepta
    - q0 -a→ q1 -b→ q0 — ✘ muere tras leer `ab`
4. `aababaa`: {q0} -a→ {q1} -a→ {q1} -b→ {q0, q1} -a→ {q1} -b→ {q0, q1} -a→ {q1} -a→ {q1} — ✔
  Árbol de cómputo: 4 caminos, 4 de aceptación (se muestran 3):
    - q0 -a→ q1 -a→ q1 -b→ q0 -a→ q1 -b→ q0 -a→ q1 -a→ q1 — ✔ acepta
    - q0 -a→ q1 -a→ q1 -b→ q0 -a→ q1 -b→ q1 -a→ q1 -a→ q1 — ✔ acepta
    - q0 -a→ q1 -a→ q1 -b→ q1 -a→ q1 -b→ q0 -a→ q1 -a→ q1 — ✔ acepta
5. `ababaaaabbb`: {q0} -a→ {q1} -b→ {q0, q1} -a→ {q1} -b→ {q0, q1} -a→ {q1} -a→ {q1} -a→ {q1} -a→ {q1} -b→ {q0, q1} -b→ {q0, q1} -b→ {q0, q1} — ✔
  Árbol de cómputo: 16 caminos, 4 de aceptación (se muestran 6):
    - q0 -a→ q1 -b→ q0 -a→ q1 -b→ q0 -a→ q1 -a→ q1 -a→ q1 -a→ q1 -b→ q1 -b→ q1 -b→ q1 — ✔ acepta
    - q0 -a→ q1 -b→ q0 -a→ q1 -b→ q1 -a→ q1 -a→ q1 -a→ q1 -a→ q1 -b→ q1 -b→ q1 -b→ q1 — ✔ acepta
    - q0 -a→ q1 -b→ q1 -a→ q1 -b→ q0 -a→ q1 -a→ q1 -a→ q1 -a→ q1 -b→ q1 -b→ q1 -b→ q1 — ✔ acepta
    - q0 -a→ q1 -b→ q0 -a→ q1 -b→ q0 -a→ q1 -a→ q1 -a→ q1 -a→ q1 -b→ q0 — ✘ muere tras leer `ababaaaab`
    - q0 -a→ q1 -b→ q0 -a→ q1 -b→ q0 -a→ q1 -a→ q1 -a→ q1 -a→ q1 -b→ q1 -b→ q0 — ✘ muere tras leer `ababaaaabb`
    - q0 -a→ q1 -b→ q0 -a→ q1 -b→ q0 -a→ q1 -a→ q1 -a→ q1 -a→ q1 -b→ q1 -b→ q1 -b→ q0 — ✘ termina fuera de F
6. λ: {q0} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
7. `bb`: {q0} -b→ ∅ -b→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ
8. `baab`: {q0} -b→ ∅ -a→ ∅ -a→ ∅ -b→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ
9. `bbaaabb`: {q0} -b→ ∅ -b→ ∅ -a→ ∅ -a→ ∅ -a→ ∅ -b→ ∅ -b→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ
10. `bbaaaaaabbb`: {q0} -b→ ∅ -b→ ∅ -a→ ∅ -a→ ∅ -a→ ∅ -a→ ∅ -a→ ∅ -a→ ∅ -b→ ∅ -b→ ∅ -b→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ

</details>

Simulación paso a paso en JFLAP con `ab`: [ver captura](../../evidencias/jflap/pasos/L2-143b.png).

**Conversión.** AFND (2 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 3 estados, [`L2-143b-AFD.jff`](../../automatas/conversiones/L2-143b-AFD.jff) ([.json](../../automatas/conversiones/L2-143b-AFD.json), [.xml](../../automatas/conversiones/L2-143b-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 4 estados, y el AFD mínimo (Hopcroft), 3. La cota es 2^2 = 4. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-158"></a>

## Lista 3, problema 158

**Enunciado.** Describir el AFN de la figura 158.

**Clasificación: AFND.** Los diagramas dejan transiciones indefinidas (δ(q, a) = ∅); la lista los presenta como AFN. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### Describir el AFN de la figura 158. — `L3-158`

Archivos: [`L3-158.jff`](../../automatas/lista3-afnd/L3-158.jff) · [`L3-158.json`](../../automatas/lista3-afnd/L3-158.json) · [`L3-158.xml`](../../automatas/lista3-afnd/L3-158.xml). Tipo según la definición: **AFND**, |Q| = 3, Σ = {0, 1}, 2 transiciones.

**Diseño.** Cadena lineal q1→q2→q3: acepta únicamente 01.

| Estado | 0 | 1 |
|---|---|---|
| →q1 | q2 | — |
| q2 | — | q3 |
| *q3 | — | — |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `01` | acepta | acepta | acepta |
| 2 | λ | rechaza | rechaza | rechaza |
| 3 | `11` | rechaza | rechaza | rechaza |
| 4 | `1110` | rechaza | rechaza | rechaza |
| 5 | `1001101` | rechaza | rechaza | rechaza |
| 6 | `01101010110` | rechaza | rechaza | rechaza |

Nota sobre los casos: el lenguaje solo tiene 1 palabra.

<details><summary>Recorrido completo de cada cadena</summary>

1. `01`: q1 -0→ q2 -1→ q3 — ✔
2. λ: q1 — ✘
3. `11`: q1 -1→ (sin transición) — ✘
4. `1110`: q1 -1→ (sin transición) — ✘
5. `1001101`: q1 -1→ (sin transición) — ✘
6. `01101010110`: q1 -0→ q2 -1→ q3 -1→ (sin transición) — ✘

</details>

Simulación paso a paso en JFLAP con `01`: [ver captura](../../evidencias/jflap/pasos/L3-158.png).

**Conversión.** AFND (3 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 3 estados, [`L3-158-AFD.jff`](../../automatas/conversiones/L3-158-AFD.jff) ([.json](../../automatas/conversiones/L3-158-AFD.json), [.xml](../../automatas/conversiones/L3-158-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 4 estados, y el AFD mínimo (Hopcroft), 4. La cota es 2^3 = 8. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-159"></a>

## Lista 3, problema 159

**Enunciado.** Describir el AFN de la figura 159.

**Clasificación: AFND.** Los diagramas dejan transiciones indefinidas (δ(q, a) = ∅); la lista los presenta como AFN. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### Describir el AFN de la figura 159. — `L3-159`

Archivos: [`L3-159.jff`](../../automatas/lista3-afnd/L3-159.jff) · [`L3-159.json`](../../automatas/lista3-afnd/L3-159.json) · [`L3-159.xml`](../../automatas/lista3-afnd/L3-159.xml). Tipo según la definición: **AFND**, |Q| = 3, Σ = {0, 1}, 3 transiciones.

**Diseño.** q1 consume unos; luego exige 01: L = 1*01.

| Estado | 0 | 1 |
|---|---|---|
| →q1 | q2 | q1 |
| q2 | — | q3 |
| *q3 | — | — |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `01` | acepta | acepta | acepta |
| 2 | `101` | acepta | acepta | acepta |
| 3 | `1101` | acepta | acepta | acepta |
| 4 | `11101` | acepta | acepta | acepta |
| 5 | `11111101` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `010` | rechaza | rechaza | rechaza |
| 8 | `1111` | rechaza | rechaza | rechaza |
| 9 | `0110001` | rechaza | rechaza | rechaza |
| 10 | `11001101100` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `01`: q1 -0→ q2 -1→ q3 — ✔
2. `101`: q1 -1→ q1 -0→ q2 -1→ q3 — ✔
3. `1101`: q1 -1→ q1 -1→ q1 -0→ q2 -1→ q3 — ✔
4. `11101`: q1 -1→ q1 -1→ q1 -1→ q1 -0→ q2 -1→ q3 — ✔
5. `11111101`: q1 -1→ q1 -1→ q1 -1→ q1 -1→ q1 -1→ q1 -1→ q1 -0→ q2 -1→ q3 — ✔
6. λ: q1 — ✘
7. `010`: q1 -0→ q2 -1→ q3 -0→ (sin transición) — ✘
8. `1111`: q1 -1→ q1 -1→ q1 -1→ q1 -1→ q1 — ✘
9. `0110001`: q1 -0→ q2 -1→ q3 -1→ (sin transición) — ✘
10. `11001101100`: q1 -1→ q1 -1→ q1 -0→ q2 -0→ (sin transición) — ✘

</details>

Simulación paso a paso en JFLAP con `01`: [ver captura](../../evidencias/jflap/pasos/L3-159.png).

**Conversión.** AFND (3 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 3 estados, [`L3-159-AFD.jff`](../../automatas/conversiones/L3-159-AFD.jff) ([.json](../../automatas/conversiones/L3-159-AFD.json), [.xml](../../automatas/conversiones/L3-159-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 4 estados, y el AFD mínimo (Hopcroft), 4. La cota es 2^3 = 8. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-160"></a>

## Lista 3, problema 160

**Enunciado.** Describir el AFN de la figura 160.

**Clasificación: AFND.** Los diagramas dejan transiciones indefinidas (δ(q, a) = ∅); la lista los presenta como AFN. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### Describir el AFN de la figura 160. — `L3-160`

Archivos: [`L3-160.jff`](../../automatas/lista3-afnd/L3-160.jff) · [`L3-160.json`](../../automatas/lista3-afnd/L3-160.json) · [`L3-160.xml`](../../automatas/lista3-afnd/L3-160.xml). Tipo según la definición: **AFND**, |Q| = 3, Σ = {0, 1}, 4 transiciones.

**Diseño.** Exige el prefijo 01 y q3 absorbe el resto: L = 01(0+1)*.

| Estado | 0 | 1 |
|---|---|---|
| →q1 | q2 | — |
| q2 | — | q3 |
| *q3 | q3 | q3 |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `01` | acepta | acepta | acepta |
| 2 | `0111` | acepta | acepta | acepta |
| 3 | `0101010` | acepta | acepta | acepta |
| 4 | `01100101001` | acepta | acepta | acepta |
| 5 | `0101010110111100` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `00` | rechaza | rechaza | rechaza |
| 8 | `0010` | rechaza | rechaza | rechaza |
| 9 | `1100011` | rechaza | rechaza | rechaza |
| 10 | `00111000110` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `01`: q1 -0→ q2 -1→ q3 — ✔
2. `0111`: q1 -0→ q2 -1→ q3 -1→ q3 -1→ q3 — ✔
3. `0101010`: q1 -0→ q2 -1→ q3 -0→ q3 -1→ q3 -0→ q3 -1→ q3 -0→ q3 — ✔
4. `01100101001`: q1 -0→ q2 -1→ q3 -1→ q3 -0→ q3 -0→ q3 -1→ q3 -0→ q3 -1→ q3 -0→ q3 -0→ q3 -1→ q3 — ✔
5. `0101010110111100`: q1 -0→ q2 -1→ q3 -0→ q3 -1→ q3 -0→ q3 -1→ q3 -0→ q3 -1→ q3 -1→ q3 -0→ q3 -1→ q3 -1→ q3 -1→ q3 -1→ q3 -0→ q3 -0→ q3 — ✔
6. λ: q1 — ✘
7. `00`: q1 -0→ q2 -0→ (sin transición) — ✘
8. `0010`: q1 -0→ q2 -0→ (sin transición) — ✘
9. `1100011`: q1 -1→ (sin transición) — ✘
10. `00111000110`: q1 -0→ q2 -0→ (sin transición) — ✘

</details>

Simulación paso a paso en JFLAP con `01`: [ver captura](../../evidencias/jflap/pasos/L3-160.png).

**Conversión.** AFND (3 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 3 estados, [`L3-160-AFD.jff`](../../automatas/conversiones/L3-160-AFD.jff) ([.json](../../automatas/conversiones/L3-160-AFD.json), [.xml](../../automatas/conversiones/L3-160-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 4 estados, y el AFD mínimo (Hopcroft), 4. La cota es 2^3 = 8. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-161"></a>

## Lista 3, problema 161

**Enunciado.** Describir el AFN de la figura 161.

**Clasificación: AFND.** Los diagramas dejan transiciones indefinidas (δ(q, a) = ∅); la lista los presenta como AFN. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### Describir el AFN de la figura 161. — `L3-161`

Archivos: [`L3-161.jff`](../../automatas/lista3-afnd/L3-161.jff) · [`L3-161.json`](../../automatas/lista3-afnd/L3-161.json) · [`L3-161.xml`](../../automatas/lista3-afnd/L3-161.xml). Tipo según la definición: **AFND**, |Q| = 3, Σ = {0, 1}, 3 transiciones.

**Diseño.** Ciclo q1→q2→q3→q1 que lee 010; q1 acepta: L = (010)*.

| Estado | 0 | 1 |
|---|---|---|
| →*q1 | q2 | — |
| q2 | — | q3 |
| q3 | q1 | — |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | acepta | acepta | acepta |
| 2 | `010` | acepta | acepta | acepta |
| 3 | `010010` | acepta | acepta | acepta |
| 4 | `010010010` | acepta | acepta | acepta |
| 5 | `010010010010` | acepta | acepta | acepta |
| 6 | `0` | rechaza | rechaza | rechaza |
| 7 | `00` | rechaza | rechaza | rechaza |
| 8 | `0101` | rechaza | rechaza | rechaza |
| 9 | `0100010` | rechaza | rechaza | rechaza |
| 10 | `01000010111` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: q1 — ✔
2. `010`: q1 -0→ q2 -1→ q3 -0→ q1 — ✔
3. `010010`: q1 -0→ q2 -1→ q3 -0→ q1 -0→ q2 -1→ q3 -0→ q1 — ✔
4. `010010010`: q1 -0→ q2 -1→ q3 -0→ q1 -0→ q2 -1→ q3 -0→ q1 -0→ q2 -1→ q3 -0→ q1 — ✔
5. `010010010010`: q1 -0→ q2 -1→ q3 -0→ q1 -0→ q2 -1→ q3 -0→ q1 -0→ q2 -1→ q3 -0→ q1 -0→ q2 -1→ q3 -0→ q1 — ✔
6. `0`: q1 -0→ q2 — ✘
7. `00`: q1 -0→ q2 -0→ (sin transición) — ✘
8. `0101`: q1 -0→ q2 -1→ q3 -0→ q1 -1→ (sin transición) — ✘
9. `0100010`: q1 -0→ q2 -1→ q3 -0→ q1 -0→ q2 -0→ (sin transición) — ✘
10. `01000010111`: q1 -0→ q2 -1→ q3 -0→ q1 -0→ q2 -0→ (sin transición) — ✘

</details>

Simulación paso a paso en JFLAP con `010`: [ver captura](../../evidencias/jflap/pasos/L3-161.png).

**Conversión.** AFND (3 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 3 estados, [`L3-161-AFD.jff`](../../automatas/conversiones/L3-161-AFD.jff) ([.json](../../automatas/conversiones/L3-161-AFD.json), [.xml](../../automatas/conversiones/L3-161-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 4 estados, y el AFD mínimo (Hopcroft), 4. La cota es 2^3 = 8. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-162-188-p-100"></a>

## Lista 3, problema 162-188 (p. 100)

**Enunciado.** AFN para el problema 100 de la Lista 2: Las palabras de Σ₂ = {a,b,c,0,1} tales que el primer símbolo es una letra y el segundo es un dígito.

**Clasificación: AFND.** El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD.

#### AFND — `L3-AFND-p100`

Archivos: [`L3-AFND-p100.jff`](../../automatas/lista3-afnd/L3-AFND-p100.jff) · [`L3-AFND-p100.json`](../../automatas/lista3-afnd/L3-AFND-p100.json) · [`L3-AFND-p100.xml`](../../automatas/lista3-afnd/L3-AFND-p100.xml). Tipo según la definición: **AFND**, |Q| = 3, Σ = {a, b, c, 0, 1}, 10 transiciones.

**Diseño.** Letra, dígito y un lazo final con todo Σ₂; sin estado de rechazo.

| Estado | a | b | c | 0 | 1 |
|---|---|---|---|---|---|
| →q0 | q1 | q1 | q1 | — | — |
| q1 | — | — | — | q2 | q2 |
| *q2 | q2 | q2 | q2 | q2 | q2 |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `a0` | acepta | acepta | acepta |
| 2 | `b0` | acepta | acepta | acepta |
| 3 | `a1c1` | acepta | acepta | acepta |
| 4 | `a111b11` | acepta | acepta | acepta |
| 5 | `c110aa1a001` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `00` | rechaza | rechaza | rechaza |
| 8 | `bcbb` | rechaza | rechaza | rechaza |
| 9 | `0acba01` | rechaza | rechaza | rechaza |
| 10 | `bc1ba0cbaca` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `a0`: q0 -a→ q1 -0→ q2 — ✔
2. `b0`: q0 -b→ q1 -0→ q2 — ✔
3. `a1c1`: q0 -a→ q1 -1→ q2 -c→ q2 -1→ q2 — ✔
4. `a111b11`: q0 -a→ q1 -1→ q2 -1→ q2 -1→ q2 -b→ q2 -1→ q2 -1→ q2 — ✔
5. `c110aa1a001`: q0 -c→ q1 -1→ q2 -1→ q2 -0→ q2 -a→ q2 -a→ q2 -1→ q2 -a→ q2 -0→ q2 -0→ q2 -1→ q2 — ✔
6. λ: q0 — ✘
7. `00`: q0 -0→ (sin transición) — ✘
8. `bcbb`: q0 -b→ q1 -c→ (sin transición) — ✘
9. `0acba01`: q0 -0→ (sin transición) — ✘
10. `bc1ba0cbaca`: q0 -b→ q1 -c→ (sin transición) — ✘

</details>

Simulación paso a paso en JFLAP con `a0`: [ver captura](../../evidencias/jflap/pasos/L3-AFND-p100.png).

**Conversión.** AFND (3 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 3 estados, [`L3-AFND-p100-AFD.jff`](../../automatas/conversiones/L3-AFND-p100-AFD.jff) ([.json](../../automatas/conversiones/L3-AFND-p100-AFD.json), [.xml](../../automatas/conversiones/L3-AFND-p100-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 4 estados, y el AFD mínimo (Hopcroft), 4. La cota es 2^3 = 8. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-162-188-p-101"></a>

## Lista 3, problema 162-188 (p. 101)

**Enunciado.** AFN para el problema 101 de la Lista 2: Las palabras de Σ₃ = {a,b} que contienen la cadena aba.

**Clasificación: AFND.** El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD.

#### AFND — `L3-AFND-p101`

Archivos: [`L3-AFND-p101.jff`](../../automatas/lista3-afnd/L3-AFND-p101.jff) · [`L3-AFND-p101.json`](../../automatas/lista3-afnd/L3-AFND-p101.json) · [`L3-AFND-p101.xml`](../../automatas/lista3-afnd/L3-AFND-p101.xml). Tipo según la definición: **AFND**, |Q| = 4, Σ = {a, b}, 7 transiciones.

**Diseño.** q0 con lazo adivina el inicio de aba; q3 absorbente.

| Estado | a | b |
|---|---|---|
| →q0 | {q0, q1} | {q0} |
| q1 | ∅ | {q2} |
| q2 | {q3} | ∅ |
| *q3 | {q3} | {q3} |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `aba` | acepta | acepta | acepta |
| 2 | `aaba` | acepta | acepta | acepta |
| 3 | `bbaaba` | acepta | acepta | acepta |
| 4 | `bbaaaba` | acepta | acepta | acepta |
| 5 | `abbabbabbaba` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `bb` | rechaza | rechaza | rechaza |
| 8 | `bbaa` | rechaza | rechaza | rechaza |
| 9 | `abbbbbb` | rechaza | rechaza | rechaza |
| 10 | `bbbabbbaaaa` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `aba`: {q0} -a→ {q0, q1} -b→ {q0, q2} -a→ {q0, q1, q3} — ✔
  Árbol de cómputo: 3 caminos, 1 de aceptación:
    - q0 -a→ q1 -b→ q2 -a→ q3 — ✔ acepta
    - q0 -a→ q0 -b→ q0 -a→ q0 — ✘ termina fuera de F
    - q0 -a→ q0 -b→ q0 -a→ q1 — ✘ termina fuera de F
2. `aaba`: {q0} -a→ {q0, q1} -a→ {q0, q1} -b→ {q0, q2} -a→ {q0, q1, q3} — ✔
  Árbol de cómputo: 4 caminos, 1 de aceptación:
    - q0 -a→ q0 -a→ q1 -b→ q2 -a→ q3 — ✔ acepta
    - q0 -a→ q0 -a→ q0 -b→ q0 -a→ q0 — ✘ termina fuera de F
    - q0 -a→ q0 -a→ q0 -b→ q0 -a→ q1 — ✘ termina fuera de F
    - q0 -a→ q1 — ✘ muere tras leer `a`
3. `bbaaba`: {q0} -b→ {q0} -b→ {q0} -a→ {q0, q1} -a→ {q0, q1} -b→ {q0, q2} -a→ {q0, q1, q3} — ✔
  Árbol de cómputo: 4 caminos, 1 de aceptación:
    - q0 -b→ q0 -b→ q0 -a→ q0 -a→ q1 -b→ q2 -a→ q3 — ✔ acepta
    - q0 -b→ q0 -b→ q0 -a→ q0 -a→ q0 -b→ q0 -a→ q0 — ✘ termina fuera de F
    - q0 -b→ q0 -b→ q0 -a→ q0 -a→ q0 -b→ q0 -a→ q1 — ✘ termina fuera de F
    - q0 -b→ q0 -b→ q0 -a→ q1 — ✘ muere tras leer `bba`
4. `bbaaaba`: {q0} -b→ {q0} -b→ {q0} -a→ {q0, q1} -a→ {q0, q1} -a→ {q0, q1} -b→ {q0, q2} -a→ {q0, q1, q3} — ✔
  Árbol de cómputo: 5 caminos, 1 de aceptación:
    - q0 -b→ q0 -b→ q0 -a→ q0 -a→ q0 -a→ q1 -b→ q2 -a→ q3 — ✔ acepta
    - q0 -b→ q0 -b→ q0 -a→ q0 -a→ q0 -a→ q0 -b→ q0 -a→ q0 — ✘ termina fuera de F
    - q0 -b→ q0 -b→ q0 -a→ q0 -a→ q0 -a→ q0 -b→ q0 -a→ q1 — ✘ termina fuera de F
    - q0 -b→ q0 -b→ q0 -a→ q0 -a→ q1 — ✘ muere tras leer `bbaa`
    - q0 -b→ q0 -b→ q0 -a→ q1 — ✘ muere tras leer `bba`
5. `abbabbabbaba`: {q0} -a→ {q0, q1} -b→ {q0, q2} -b→ {q0} -a→ {q0, q1} -b→ {q0, q2} -b→ {q0} -a→ {q0, q1} -b→ {q0, q2} -b→ {q0} -a→ {q0, q1} -b→ {q0, q2} -a→ {q0, q1, q3} — ✔
  Árbol de cómputo: 6 caminos, 1 de aceptación:
    - q0 -a→ q0 -b→ q0 -b→ q0 -a→ q0 -b→ q0 -b→ q0 -a→ q0 -b→ q0 -b→ q0 -a→ q1 -b→ q2 -a→ q3 — ✔ acepta
    - q0 -a→ q0 -b→ q0 -b→ q0 -a→ q0 -b→ q0 -b→ q0 -a→ q0 -b→ q0 -b→ q0 -a→ q0 -b→ q0 -a→ q0 — ✘ termina fuera de F
    - q0 -a→ q0 -b→ q0 -b→ q0 -a→ q0 -b→ q0 -b→ q0 -a→ q0 -b→ q0 -b→ q0 -a→ q0 -b→ q0 -a→ q1 — ✘ termina fuera de F
    - q0 -a→ q0 -b→ q0 -b→ q0 -a→ q0 -b→ q0 -b→ q0 -a→ q1 -b→ q2 — ✘ muere tras leer `abbabbab`
    - q0 -a→ q0 -b→ q0 -b→ q0 -a→ q1 -b→ q2 — ✘ muere tras leer `abbab`
    - q0 -a→ q1 -b→ q2 — ✘ muere tras leer `ab`
6. λ: {q0} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
7. `bb`: {q0} -b→ {q0} -b→ {q0} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 -b→ q0 -b→ q0 — ✘ termina fuera de F
8. `bbaa`: {q0} -b→ {q0} -b→ {q0} -a→ {q0, q1} -a→ {q0, q1} — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - q0 -b→ q0 -b→ q0 -a→ q0 -a→ q0 — ✘ termina fuera de F
    - q0 -b→ q0 -b→ q0 -a→ q0 -a→ q1 — ✘ termina fuera de F
    - q0 -b→ q0 -b→ q0 -a→ q1 — ✘ muere tras leer `bba`
9. `abbbbbb`: {q0} -a→ {q0, q1} -b→ {q0, q2} -b→ {q0} -b→ {q0} -b→ {q0} -b→ {q0} -b→ {q0} — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -a→ q0 -b→ q0 -b→ q0 -b→ q0 -b→ q0 -b→ q0 -b→ q0 — ✘ termina fuera de F
    - q0 -a→ q1 -b→ q2 — ✘ muere tras leer `ab`
10. `bbbabbbaaaa`: {q0} -b→ {q0} -b→ {q0} -b→ {q0} -a→ {q0, q1} -b→ {q0, q2} -b→ {q0} -b→ {q0} -a→ {q0, q1} -a→ {q0, q1} -a→ {q0, q1} -a→ {q0, q1} — ✘
  Árbol de cómputo: 6 caminos, 0 de aceptación:
    - q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q0 — ✘ termina fuera de F
    - q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q1 — ✘ termina fuera de F
    - q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 -a→ q0 -a→ q1 — ✘ muere tras leer `bbbabbbaaa`
    - q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 -a→ q1 — ✘ muere tras leer `bbbabbbaa`
    - q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q1 — ✘ muere tras leer `bbbabbba`
    - q0 -b→ q0 -b→ q0 -b→ q0 -a→ q1 -b→ q2 — ✘ muere tras leer `bbbab`

</details>

Simulación paso a paso en JFLAP con `aba`: [ver captura](../../evidencias/jflap/pasos/L3-AFND-p101.png).

**Conversión.** AFND (4 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 6 estados, [`L3-AFND-p101-AFD.jff`](../../automatas/conversiones/L3-AFND-p101-AFD.jff) ([.json](../../automatas/conversiones/L3-AFND-p101-AFD.json), [.xml](../../automatas/conversiones/L3-AFND-p101-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 6 estados, y el AFD mínimo (Hopcroft), 4. La cota es 2^4 = 16. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-162-188-p-102"></a>

## Lista 3, problema 162-188 (p. 102)

**Enunciado.** AFN para el problema 102 de la Lista 2: Palabras de Σ₃ que contienen abbbab.

**Clasificación: AFND.** El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### AFND — `L3-AFND-p102`

Archivos: [`L3-AFND-p102.jff`](../../automatas/lista3-afnd/L3-AFND-p102.jff) · [`L3-AFND-p102.json`](../../automatas/lista3-afnd/L3-AFND-p102.json) · [`L3-AFND-p102.xml`](../../automatas/lista3-afnd/L3-AFND-p102.xml). Tipo según la definición: **AFND**, |Q| = 7, Σ = {a, b}, 10 transiciones.

**Diseño.** q0 con lazo adivina el inicio de abbbab; el último estado es absorbente.

| Estado | a | b |
|---|---|---|
| →q0 | {q0, q1} | {q0} |
| q1 | ∅ | {q2} |
| q2 | ∅ | {q3} |
| q3 | ∅ | {q4} |
| q4 | {q5} | ∅ |
| q5 | ∅ | {q6} |
| *q6 | {q6} | {q6} |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `abbbab` | acepta | acepta | acepta |
| 2 | `aabbbab` | acepta | acepta | acepta |
| 3 | `ababbbab` | acepta | acepta | acepta |
| 4 | `babaababbbab` | acepta | acepta | acepta |
| 5 | `ababbbbbababbbab` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `bb` | rechaza | rechaza | rechaza |
| 8 | `abab` | rechaza | rechaza | rechaza |
| 9 | `babbaaa` | rechaza | rechaza | rechaza |
| 10 | `abbabbababb` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `abbbab`: {q0} -a→ {q0, q1} -b→ {q0, q2} -b→ {q0, q3} -b→ {q0, q4} -a→ {q0, q1, q5} -b→ {q0, q2, q6} — ✔
  Árbol de cómputo: 3 caminos, 1 de aceptación:
    - q0 -a→ q1 -b→ q2 -b→ q3 -b→ q4 -a→ q5 -b→ q6 — ✔ acepta
    - q0 -a→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 -b→ q0 — ✘ termina fuera de F
    - q0 -a→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q1 -b→ q2 — ✘ termina fuera de F
2. `aabbbab`: {q0} -a→ {q0, q1} -a→ {q0, q1} -b→ {q0, q2} -b→ {q0, q3} -b→ {q0, q4} -a→ {q0, q1, q5} -b→ {q0, q2, q6} — ✔
  Árbol de cómputo: 4 caminos, 1 de aceptación:
    - q0 -a→ q0 -a→ q1 -b→ q2 -b→ q3 -b→ q4 -a→ q5 -b→ q6 — ✔ acepta
    - q0 -a→ q0 -a→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 -b→ q0 — ✘ termina fuera de F
    - q0 -a→ q0 -a→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q1 -b→ q2 — ✘ termina fuera de F
    - q0 -a→ q1 — ✘ muere tras leer `a`
3. `ababbbab`: {q0} -a→ {q0, q1} -b→ {q0, q2} -a→ {q0, q1} -b→ {q0, q2} -b→ {q0, q3} -b→ {q0, q4} -a→ {q0, q1, q5} -b→ {q0, q2, q6} — ✔
  Árbol de cómputo: 4 caminos, 1 de aceptación:
    - q0 -a→ q0 -b→ q0 -a→ q1 -b→ q2 -b→ q3 -b→ q4 -a→ q5 -b→ q6 — ✔ acepta
    - q0 -a→ q0 -b→ q0 -a→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 -b→ q0 — ✘ termina fuera de F
    - q0 -a→ q0 -b→ q0 -a→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q1 -b→ q2 — ✘ termina fuera de F
    - q0 -a→ q1 -b→ q2 — ✘ muere tras leer `ab`
4. `babaababbbab`: {q0} -b→ {q0} -a→ {q0, q1} -b→ {q0, q2} -a→ {q0, q1} -a→ {q0, q1} -b→ {q0, q2} -a→ {q0, q1} -b→ {q0, q2} -b→ {q0, q3} -b→ {q0, q4} -a→ {q0, q1, q5} -b→ {q0, q2, q6} — ✔
  Árbol de cómputo: 6 caminos, 1 de aceptación:
    - q0 -b→ q0 -a→ q0 -b→ q0 -a→ q0 -a→ q0 -b→ q0 -a→ q1 -b→ q2 -b→ q3 -b→ q4 -a→ q5 -b→ q6 — ✔ acepta
    - q0 -b→ q0 -a→ q0 -b→ q0 -a→ q0 -a→ q0 -b→ q0 -a→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 -b→ q0 — ✘ termina fuera de F
    - q0 -b→ q0 -a→ q0 -b→ q0 -a→ q0 -a→ q0 -b→ q0 -a→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q1 -b→ q2 — ✘ termina fuera de F
    - q0 -b→ q0 -a→ q0 -b→ q0 -a→ q0 -a→ q1 -b→ q2 — ✘ muere tras leer `babaab`
    - q0 -b→ q0 -a→ q0 -b→ q0 -a→ q1 — ✘ muere tras leer `baba`
    - q0 -b→ q0 -a→ q1 -b→ q2 — ✘ muere tras leer `bab`
5. `ababbbbbababbbab`: {q0} -a→ {q0, q1} -b→ {q0, q2} -a→ {q0, q1} -b→ {q0, q2} -b→ {q0, q3} -b→ {q0, q4} -b→ {q0} -b→ {q0} -a→ {q0, q1} -b→ {q0, q2} -a→ {q0, q1} -b→ {q0, q2} -b→ {q0, q3} -b→ {q0, q4} -a→ {q0, q1, q5} -b→ {q0, q2, q6} — ✔
  Árbol de cómputo: 6 caminos, 1 de aceptación:
    - q0 -a→ q0 -b→ q0 -a→ q0 -b→ q0 -b→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 -b→ q0 -a→ q1 -b→ q2 -b→ q3 -b→ q4 -a→ q5 -b→ q6 — ✔ acepta
    - q0 -a→ q0 -b→ q0 -a→ q0 -b→ q0 -b→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 -b→ q0 -a→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 -b→ q0 — ✘ termina fuera de F
    - q0 -a→ q0 -b→ q0 -a→ q0 -b→ q0 -b→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 -b→ q0 -a→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q1 -b→ q2 — ✘ termina fuera de F
    - q0 -a→ q0 -b→ q0 -a→ q0 -b→ q0 -b→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q1 -b→ q2 — ✘ muere tras leer `ababbbbbab`
    - q0 -a→ q0 -b→ q0 -a→ q1 -b→ q2 -b→ q3 -b→ q4 — ✘ muere tras leer `ababbb`
    - q0 -a→ q1 -b→ q2 — ✘ muere tras leer `ab`
6. λ: {q0} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
7. `bb`: {q0} -b→ {q0} -b→ {q0} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 -b→ q0 -b→ q0 — ✘ termina fuera de F
8. `abab`: {q0} -a→ {q0, q1} -b→ {q0, q2} -a→ {q0, q1} -b→ {q0, q2} — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - q0 -a→ q0 -b→ q0 -a→ q0 -b→ q0 — ✘ termina fuera de F
    - q0 -a→ q0 -b→ q0 -a→ q1 -b→ q2 — ✘ termina fuera de F
    - q0 -a→ q1 -b→ q2 — ✘ muere tras leer `ab`
9. `babbaaa`: {q0} -b→ {q0} -a→ {q0, q1} -b→ {q0, q2} -b→ {q0, q3} -a→ {q0, q1} -a→ {q0, q1} -a→ {q0, q1} — ✘
  Árbol de cómputo: 5 caminos, 0 de aceptación:
    - q0 -b→ q0 -a→ q0 -b→ q0 -b→ q0 -a→ q0 -a→ q0 -a→ q0 — ✘ termina fuera de F
    - q0 -b→ q0 -a→ q0 -b→ q0 -b→ q0 -a→ q0 -a→ q0 -a→ q1 — ✘ termina fuera de F
    - q0 -b→ q0 -a→ q0 -b→ q0 -b→ q0 -a→ q0 -a→ q1 — ✘ muere tras leer `babbaa`
    - q0 -b→ q0 -a→ q0 -b→ q0 -b→ q0 -a→ q1 — ✘ muere tras leer `babba`
    - q0 -b→ q0 -a→ q1 -b→ q2 -b→ q3 — ✘ muere tras leer `babb`
10. `abbabbababb`: {q0} -a→ {q0, q1} -b→ {q0, q2} -b→ {q0, q3} -a→ {q0, q1} -b→ {q0, q2} -b→ {q0, q3} -a→ {q0, q1} -b→ {q0, q2} -a→ {q0, q1} -b→ {q0, q2} -b→ {q0, q3} — ✘
  Árbol de cómputo: 5 caminos, 0 de aceptación:
    - q0 -a→ q0 -b→ q0 -b→ q0 -a→ q0 -b→ q0 -b→ q0 -a→ q0 -b→ q0 -a→ q0 -b→ q0 -b→ q0 — ✘ termina fuera de F
    - q0 -a→ q0 -b→ q0 -b→ q0 -a→ q0 -b→ q0 -b→ q0 -a→ q0 -b→ q0 -a→ q1 -b→ q2 -b→ q3 — ✘ termina fuera de F
    - q0 -a→ q0 -b→ q0 -b→ q0 -a→ q0 -b→ q0 -b→ q0 -a→ q1 -b→ q2 — ✘ muere tras leer `abbabbab`
    - q0 -a→ q0 -b→ q0 -b→ q0 -a→ q1 -b→ q2 -b→ q3 — ✘ muere tras leer `abbabb`
    - q0 -a→ q1 -b→ q2 -b→ q3 — ✘ muere tras leer `abb`

</details>

Simulación paso a paso en JFLAP con `abbbab`: [ver captura](../../evidencias/jflap/pasos/L3-AFND-p102.png).

**Conversión.** AFND (7 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 12 estados, [`L3-AFND-p102-AFD.jff`](../../automatas/conversiones/L3-AFND-p102-AFD.jff) ([.json](../../automatas/conversiones/L3-AFND-p102-AFD.json), [.xml](../../automatas/conversiones/L3-AFND-p102-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 12 estados, y el AFD mínimo (Hopcroft), 7. La cota es 2^7 = 128. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-162-188-p-103"></a>

## Lista 3, problema 162-188 (p. 103)

**Enunciado.** AFN para el problema 103 de la Lista 2: Palabras de Σ₃ que contienen aabbba.

**Clasificación: AFND.** El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### AFND — `L3-AFND-p103`

Archivos: [`L3-AFND-p103.jff`](../../automatas/lista3-afnd/L3-AFND-p103.jff) · [`L3-AFND-p103.json`](../../automatas/lista3-afnd/L3-AFND-p103.json) · [`L3-AFND-p103.xml`](../../automatas/lista3-afnd/L3-AFND-p103.xml). Tipo según la definición: **AFND**, |Q| = 7, Σ = {a, b}, 10 transiciones.

**Diseño.** q0 con lazo adivina el inicio de aabbba; el último estado es absorbente.

| Estado | a | b |
|---|---|---|
| →q0 | {q0, q1} | {q0} |
| q1 | {q2} | ∅ |
| q2 | ∅ | {q3} |
| q3 | ∅ | {q4} |
| q4 | ∅ | {q5} |
| q5 | {q6} | ∅ |
| *q6 | {q6} | {q6} |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `aabbba` | acepta | acepta | acepta |
| 2 | `baabbba` | acepta | acepta | acepta |
| 3 | `baaabbba` | acepta | acepta | acepta |
| 4 | `bbaaaaabbba` | acepta | acepta | acepta |
| 5 | `bbbbabaabbaabbba` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `aa` | rechaza | rechaza | rechaza |
| 8 | `baaa` | rechaza | rechaza | rechaza |
| 9 | `aababbb` | rechaza | rechaza | rechaza |
| 10 | `bababaaabba` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `aabbba`: {q0} -a→ {q0, q1} -a→ {q0, q1, q2} -b→ {q0, q3} -b→ {q0, q4} -b→ {q0, q5} -a→ {q0, q1, q6} — ✔
  Árbol de cómputo: 4 caminos, 1 de aceptación:
    - q0 -a→ q1 -a→ q2 -b→ q3 -b→ q4 -b→ q5 -a→ q6 — ✔ acepta
    - q0 -a→ q0 -a→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 — ✘ termina fuera de F
    - q0 -a→ q0 -a→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q1 — ✘ termina fuera de F
    - q0 -a→ q0 -a→ q1 — ✘ muere tras leer `aa`
2. `baabbba`: {q0} -b→ {q0} -a→ {q0, q1} -a→ {q0, q1, q2} -b→ {q0, q3} -b→ {q0, q4} -b→ {q0, q5} -a→ {q0, q1, q6} — ✔
  Árbol de cómputo: 4 caminos, 1 de aceptación:
    - q0 -b→ q0 -a→ q1 -a→ q2 -b→ q3 -b→ q4 -b→ q5 -a→ q6 — ✔ acepta
    - q0 -b→ q0 -a→ q0 -a→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 — ✘ termina fuera de F
    - q0 -b→ q0 -a→ q0 -a→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q1 — ✘ termina fuera de F
    - q0 -b→ q0 -a→ q0 -a→ q1 — ✘ muere tras leer `baa`
3. `baaabbba`: {q0} -b→ {q0} -a→ {q0, q1} -a→ {q0, q1, q2} -a→ {q0, q1, q2} -b→ {q0, q3} -b→ {q0, q4} -b→ {q0, q5} -a→ {q0, q1, q6} — ✔
  Árbol de cómputo: 5 caminos, 1 de aceptación:
    - q0 -b→ q0 -a→ q0 -a→ q1 -a→ q2 -b→ q3 -b→ q4 -b→ q5 -a→ q6 — ✔ acepta
    - q0 -b→ q0 -a→ q0 -a→ q0 -a→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 — ✘ termina fuera de F
    - q0 -b→ q0 -a→ q0 -a→ q0 -a→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q1 — ✘ termina fuera de F
    - q0 -b→ q0 -a→ q0 -a→ q0 -a→ q1 — ✘ muere tras leer `baaa`
    - q0 -b→ q0 -a→ q1 -a→ q2 — ✘ muere tras leer `baa`
4. `bbaaaaabbba`: {q0} -b→ {q0} -b→ {q0} -a→ {q0, q1} -a→ {q0, q1, q2} -a→ {q0, q1, q2} -a→ {q0, q1, q2} -a→ {q0, q1, q2} -b→ {q0, q3} -b→ {q0, q4} -b→ {q0, q5} -a→ {q0, q1, q6} — ✔
  Árbol de cómputo: 7 caminos, 1 de aceptación (se muestran 6):
    - q0 -b→ q0 -b→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q1 -a→ q2 -b→ q3 -b→ q4 -b→ q5 -a→ q6 — ✔ acepta
    - q0 -b→ q0 -b→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 — ✘ termina fuera de F
    - q0 -b→ q0 -b→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q1 — ✘ termina fuera de F
    - q0 -b→ q0 -b→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q1 — ✘ muere tras leer `bbaaaaa`
    - q0 -b→ q0 -b→ q0 -a→ q0 -a→ q0 -a→ q1 -a→ q2 — ✘ muere tras leer `bbaaaa`
    - q0 -b→ q0 -b→ q0 -a→ q0 -a→ q1 -a→ q2 — ✘ muere tras leer `bbaaa`
5. `bbbbabaabbaabbba`: {q0} -b→ {q0} -b→ {q0} -b→ {q0} -b→ {q0} -a→ {q0, q1} -b→ {q0} -a→ {q0, q1} -a→ {q0, q1, q2} -b→ {q0, q3} -b→ {q0, q4} -a→ {q0, q1} -a→ {q0, q1, q2} -b→ {q0, q3} -b→ {q0, q4} -b→ {q0, q5} -a→ {q0, q1, q6} — ✔
  Árbol de cómputo: 7 caminos, 1 de aceptación (se muestran 6):
    - q0 -b→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 -b→ q0 -a→ q0 -a→ q0 -b→ q0 -b→ q0 -a→ q1 -a→ q2 -b→ q3 -b→ q4 -b→ q5 -a→ q6 — ✔ acepta
    - q0 -b→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 -b→ q0 -a→ q0 -a→ q0 -b→ q0 -b→ q0 -a→ q0 -a→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 — ✘ termina fuera de F
    - q0 -b→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 -b→ q0 -a→ q0 -a→ q0 -b→ q0 -b→ q0 -a→ q0 -a→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q1 — ✘ termina fuera de F
    - q0 -b→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 -b→ q0 -a→ q0 -a→ q0 -b→ q0 -b→ q0 -a→ q0 -a→ q1 — ✘ muere tras leer `bbbbabaabbaa`
    - q0 -b→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 -b→ q0 -a→ q0 -a→ q1 — ✘ muere tras leer `bbbbabaa`
    - q0 -b→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 -b→ q0 -a→ q1 -a→ q2 -b→ q3 -b→ q4 — ✘ muere tras leer `bbbbabaabb`
6. λ: {q0} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
7. `aa`: {q0} -a→ {q0, q1} -a→ {q0, q1, q2} — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - q0 -a→ q0 -a→ q0 — ✘ termina fuera de F
    - q0 -a→ q0 -a→ q1 — ✘ termina fuera de F
    - q0 -a→ q1 -a→ q2 — ✘ termina fuera de F
8. `baaa`: {q0} -b→ {q0} -a→ {q0, q1} -a→ {q0, q1, q2} -a→ {q0, q1, q2} — ✘
  Árbol de cómputo: 4 caminos, 0 de aceptación:
    - q0 -b→ q0 -a→ q0 -a→ q0 -a→ q0 — ✘ termina fuera de F
    - q0 -b→ q0 -a→ q0 -a→ q0 -a→ q1 — ✘ termina fuera de F
    - q0 -b→ q0 -a→ q0 -a→ q1 -a→ q2 — ✘ termina fuera de F
    - q0 -b→ q0 -a→ q1 -a→ q2 — ✘ muere tras leer `baa`
9. `aababbb`: {q0} -a→ {q0, q1} -a→ {q0, q1, q2} -b→ {q0, q3} -a→ {q0, q1} -b→ {q0} -b→ {q0} -b→ {q0} — ✘
  Árbol de cómputo: 4 caminos, 0 de aceptación:
    - q0 -a→ q0 -a→ q0 -b→ q0 -a→ q0 -b→ q0 -b→ q0 -b→ q0 — ✘ termina fuera de F
    - q0 -a→ q0 -a→ q0 -b→ q0 -a→ q1 — ✘ muere tras leer `aaba`
    - q0 -a→ q0 -a→ q1 — ✘ muere tras leer `aa`
    - q0 -a→ q1 -a→ q2 -b→ q3 — ✘ muere tras leer `aab`
10. `bababaaabba`: {q0} -b→ {q0} -a→ {q0, q1} -b→ {q0} -a→ {q0, q1} -b→ {q0} -a→ {q0, q1} -a→ {q0, q1, q2} -a→ {q0, q1, q2} -b→ {q0, q3} -b→ {q0, q4} -a→ {q0, q1} — ✘
  Árbol de cómputo: 7 caminos, 0 de aceptación (se muestran 6):
    - q0 -b→ q0 -a→ q0 -b→ q0 -a→ q0 -b→ q0 -a→ q0 -a→ q0 -a→ q0 -b→ q0 -b→ q0 -a→ q0 — ✘ termina fuera de F
    - q0 -b→ q0 -a→ q0 -b→ q0 -a→ q0 -b→ q0 -a→ q0 -a→ q0 -a→ q0 -b→ q0 -b→ q0 -a→ q1 — ✘ termina fuera de F
    - q0 -b→ q0 -a→ q0 -b→ q0 -a→ q0 -b→ q0 -a→ q0 -a→ q0 -a→ q1 — ✘ muere tras leer `bababaaa`
    - q0 -b→ q0 -a→ q0 -b→ q0 -a→ q0 -b→ q0 -a→ q0 -a→ q1 -a→ q2 -b→ q3 -b→ q4 — ✘ muere tras leer `bababaaabb`
    - q0 -b→ q0 -a→ q0 -b→ q0 -a→ q0 -b→ q0 -a→ q1 -a→ q2 — ✘ muere tras leer `bababaa`
    - q0 -b→ q0 -a→ q0 -b→ q0 -a→ q1 — ✘ muere tras leer `baba`

</details>

Simulación paso a paso en JFLAP con `aabbba`: [ver captura](../../evidencias/jflap/pasos/L3-AFND-p103.png).

**Conversión.** AFND (7 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 12 estados, [`L3-AFND-p103-AFD.jff`](../../automatas/conversiones/L3-AFND-p103-AFD.jff) ([.json](../../automatas/conversiones/L3-AFND-p103-AFD.json), [.xml](../../automatas/conversiones/L3-AFND-p103-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 12 estados, y el AFD mínimo (Hopcroft), 7. La cota es 2^7 = 128. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-162-188-p-104"></a>

## Lista 3, problema 162-188 (p. 104)

**Enunciado.** AFN para el problema 104 de la Lista 2: Las palabras de Σ₃ que inician con la cadena abbab.

**Clasificación: AFND.** El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD.

#### AFND — `L3-AFND-p104`

Archivos: [`L3-AFND-p104.jff`](../../automatas/lista3-afnd/L3-AFND-p104.jff) · [`L3-AFND-p104.json`](../../automatas/lista3-afnd/L3-AFND-p104.json) · [`L3-AFND-p104.xml`](../../automatas/lista3-afnd/L3-AFND-p104.xml). Tipo según la definición: **AFND**, |Q| = 6, Σ = {a, b}, 7 transiciones.

**Diseño.** Cadena lineal abbab con lazo final; sin estado de rechazo.

| Estado | a | b |
|---|---|---|
| →q0 | q1 | — |
| q1 | — | q2 |
| q2 | — | q3 |
| q3 | q4 | — |
| q4 | — | q5 |
| *q5 | q5 | q5 |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `abbab` | acepta | acepta | acepta |
| 2 | `abbabbb` | acepta | acepta | acepta |
| 3 | `abbabbabb` | acepta | acepta | acepta |
| 4 | `abbabbaaaab` | acepta | acepta | acepta |
| 5 | `abbabbbbbabababb` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `ba` | rechaza | rechaza | rechaza |
| 8 | `bbaa` | rechaza | rechaza | rechaza |
| 9 | `baaabbb` | rechaza | rechaza | rechaza |
| 10 | `baaaababaab` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `abbab`: q0 -a→ q1 -b→ q2 -b→ q3 -a→ q4 -b→ q5 — ✔
2. `abbabbb`: q0 -a→ q1 -b→ q2 -b→ q3 -a→ q4 -b→ q5 -b→ q5 -b→ q5 — ✔
3. `abbabbabb`: q0 -a→ q1 -b→ q2 -b→ q3 -a→ q4 -b→ q5 -b→ q5 -a→ q5 -b→ q5 -b→ q5 — ✔
4. `abbabbaaaab`: q0 -a→ q1 -b→ q2 -b→ q3 -a→ q4 -b→ q5 -b→ q5 -a→ q5 -a→ q5 -a→ q5 -a→ q5 -b→ q5 — ✔
5. `abbabbbbbabababb`: q0 -a→ q1 -b→ q2 -b→ q3 -a→ q4 -b→ q5 -b→ q5 -b→ q5 -b→ q5 -b→ q5 -a→ q5 -b→ q5 -a→ q5 -b→ q5 -a→ q5 -b→ q5 -b→ q5 — ✔
6. λ: q0 — ✘
7. `ba`: q0 -b→ (sin transición) — ✘
8. `bbaa`: q0 -b→ (sin transición) — ✘
9. `baaabbb`: q0 -b→ (sin transición) — ✘
10. `baaaababaab`: q0 -b→ (sin transición) — ✘

</details>

Simulación paso a paso en JFLAP con `abbab`: [ver captura](../../evidencias/jflap/pasos/L3-AFND-p104.png).

**Conversión.** AFND (6 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 6 estados, [`L3-AFND-p104-AFD.jff`](../../automatas/conversiones/L3-AFND-p104-AFD.jff) ([.json](../../automatas/conversiones/L3-AFND-p104-AFD.json), [.xml](../../automatas/conversiones/L3-AFND-p104-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 7 estados, y el AFD mínimo (Hopcroft), 7. La cota es 2^6 = 64. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-162-188-p-105"></a>

## Lista 3, problema 162-188 (p. 105)

**Enunciado.** AFN para el problema 105 de la Lista 2: Las palabras de Σ₃ que terminan con la cadena abaa.

**Clasificación: AFND.** El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD.

#### AFND — `L3-AFND-p105`

Archivos: [`L3-AFND-p105.jff`](../../automatas/lista3-afnd/L3-AFND-p105.jff) · [`L3-AFND-p105.json`](../../automatas/lista3-afnd/L3-AFND-p105.json) · [`L3-AFND-p105.xml`](../../automatas/lista3-afnd/L3-AFND-p105.xml). Tipo según la definición: **AFND**, |Q| = 5, Σ = {a, b}, 6 transiciones.

**Diseño.** q0 con lazo adivina dónde empieza el sufijo abaa.

| Estado | a | b |
|---|---|---|
| →q0 | {q0, q1} | {q0} |
| q1 | ∅ | {q2} |
| q2 | {q3} | ∅ |
| q3 | {q4} | ∅ |
| *q4 | ∅ | ∅ |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `abaa` | acepta | acepta | acepta |
| 2 | `aabaa` | acepta | acepta | acepta |
| 3 | `bbbbabaa` | acepta | acepta | acepta |
| 4 | `bbbbbaabaa` | acepta | acepta | acepta |
| 5 | `abbbaaaaaaabaa` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `ba` | rechaza | rechaza | rechaza |
| 8 | `aaba` | rechaza | rechaza | rechaza |
| 9 | `aaaaaab` | rechaza | rechaza | rechaza |
| 10 | `abbbbabbbbb` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `abaa`: {q0} -a→ {q0, q1} -b→ {q0, q2} -a→ {q0, q1, q3} -a→ {q0, q1, q4} — ✔
  Árbol de cómputo: 4 caminos, 1 de aceptación:
    - q0 -a→ q1 -b→ q2 -a→ q3 -a→ q4 — ✔ acepta
    - q0 -a→ q0 -b→ q0 -a→ q0 -a→ q0 — ✘ termina fuera de F
    - q0 -a→ q0 -b→ q0 -a→ q0 -a→ q1 — ✘ termina fuera de F
    - q0 -a→ q0 -b→ q0 -a→ q1 — ✘ muere tras leer `aba`
2. `aabaa`: {q0} -a→ {q0, q1} -a→ {q0, q1} -b→ {q0, q2} -a→ {q0, q1, q3} -a→ {q0, q1, q4} — ✔
  Árbol de cómputo: 5 caminos, 1 de aceptación:
    - q0 -a→ q0 -a→ q1 -b→ q2 -a→ q3 -a→ q4 — ✔ acepta
    - q0 -a→ q0 -a→ q0 -b→ q0 -a→ q0 -a→ q0 — ✘ termina fuera de F
    - q0 -a→ q0 -a→ q0 -b→ q0 -a→ q0 -a→ q1 — ✘ termina fuera de F
    - q0 -a→ q0 -a→ q0 -b→ q0 -a→ q1 — ✘ muere tras leer `aaba`
    - q0 -a→ q1 — ✘ muere tras leer `a`
3. `bbbbabaa`: {q0} -b→ {q0} -b→ {q0} -b→ {q0} -b→ {q0} -a→ {q0, q1} -b→ {q0, q2} -a→ {q0, q1, q3} -a→ {q0, q1, q4} — ✔
  Árbol de cómputo: 4 caminos, 1 de aceptación:
    - q0 -b→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q1 -b→ q2 -a→ q3 -a→ q4 — ✔ acepta
    - q0 -b→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 -b→ q0 -a→ q0 -a→ q0 — ✘ termina fuera de F
    - q0 -b→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 -b→ q0 -a→ q0 -a→ q1 — ✘ termina fuera de F
    - q0 -b→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 -b→ q0 -a→ q1 — ✘ muere tras leer `bbbbaba`
4. `bbbbbaabaa`: {q0} -b→ {q0} -b→ {q0} -b→ {q0} -b→ {q0} -b→ {q0} -a→ {q0, q1} -a→ {q0, q1} -b→ {q0, q2} -a→ {q0, q1, q3} -a→ {q0, q1, q4} — ✔
  Árbol de cómputo: 5 caminos, 1 de aceptación:
    - q0 -b→ q0 -b→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 -a→ q1 -b→ q2 -a→ q3 -a→ q4 — ✔ acepta
    - q0 -b→ q0 -b→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 -a→ q0 -b→ q0 -a→ q0 -a→ q0 — ✘ termina fuera de F
    - q0 -b→ q0 -b→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 -a→ q0 -b→ q0 -a→ q0 -a→ q1 — ✘ termina fuera de F
    - q0 -b→ q0 -b→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 -a→ q0 -b→ q0 -a→ q1 — ✘ muere tras leer `bbbbbaaba`
    - q0 -b→ q0 -b→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q1 — ✘ muere tras leer `bbbbba`
5. `abbbaaaaaaabaa`: {q0} -a→ {q0, q1} -b→ {q0, q2} -b→ {q0} -b→ {q0} -a→ {q0, q1} -a→ {q0, q1} -a→ {q0, q1} -a→ {q0, q1} -a→ {q0, q1} -a→ {q0, q1} -a→ {q0, q1} -b→ {q0, q2} -a→ {q0, q1, q3} -a→ {q0, q1, q4} — ✔
  Árbol de cómputo: 11 caminos, 1 de aceptación (se muestran 6):
    - q0 -a→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q1 -b→ q2 -a→ q3 -a→ q4 — ✔ acepta
    - q0 -a→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q0 -b→ q0 -a→ q0 -a→ q0 — ✘ termina fuera de F
    - q0 -a→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q0 -b→ q0 -a→ q0 -a→ q1 — ✘ termina fuera de F
    - q0 -a→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q0 -b→ q0 -a→ q1 — ✘ muere tras leer `abbbaaaaaaaba`
    - q0 -a→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q1 — ✘ muere tras leer `abbbaaaaaa`
    - q0 -a→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q1 — ✘ muere tras leer `abbbaaaaa`
6. λ: {q0} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
7. `ba`: {q0} -b→ {q0} -a→ {q0, q1} — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -b→ q0 -a→ q0 — ✘ termina fuera de F
    - q0 -b→ q0 -a→ q1 — ✘ termina fuera de F
8. `aaba`: {q0} -a→ {q0, q1} -a→ {q0, q1} -b→ {q0, q2} -a→ {q0, q1, q3} — ✘
  Árbol de cómputo: 4 caminos, 0 de aceptación:
    - q0 -a→ q0 -a→ q0 -b→ q0 -a→ q0 — ✘ termina fuera de F
    - q0 -a→ q0 -a→ q0 -b→ q0 -a→ q1 — ✘ termina fuera de F
    - q0 -a→ q0 -a→ q1 -b→ q2 -a→ q3 — ✘ termina fuera de F
    - q0 -a→ q1 — ✘ muere tras leer `a`
9. `aaaaaab`: {q0} -a→ {q0, q1} -a→ {q0, q1} -a→ {q0, q1} -a→ {q0, q1} -a→ {q0, q1} -a→ {q0, q1} -b→ {q0, q2} — ✘
  Árbol de cómputo: 7 caminos, 0 de aceptación (se muestran 6):
    - q0 -a→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q0 -b→ q0 — ✘ termina fuera de F
    - q0 -a→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q1 -b→ q2 — ✘ termina fuera de F
    - q0 -a→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q1 — ✘ muere tras leer `aaaaa`
    - q0 -a→ q0 -a→ q0 -a→ q0 -a→ q1 — ✘ muere tras leer `aaaa`
    - q0 -a→ q0 -a→ q0 -a→ q1 — ✘ muere tras leer `aaa`
    - q0 -a→ q0 -a→ q1 — ✘ muere tras leer `aa`
10. `abbbbabbbbb`: {q0} -a→ {q0, q1} -b→ {q0, q2} -b→ {q0} -b→ {q0} -b→ {q0} -a→ {q0, q1} -b→ {q0, q2} -b→ {q0} -b→ {q0} -b→ {q0} -b→ {q0} — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - q0 -a→ q0 -b→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 -b→ q0 -b→ q0 -b→ q0 -b→ q0 -b→ q0 — ✘ termina fuera de F
    - q0 -a→ q0 -b→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q1 -b→ q2 — ✘ muere tras leer `abbbbab`
    - q0 -a→ q1 -b→ q2 — ✘ muere tras leer `ab`

</details>

Simulación paso a paso en JFLAP con `abaa`: [ver captura](../../evidencias/jflap/pasos/L3-AFND-p105.png).

**Conversión.** AFND (5 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 5 estados, [`L3-AFND-p105-AFD.jff`](../../automatas/conversiones/L3-AFND-p105-AFD.jff) ([.json](../../automatas/conversiones/L3-AFND-p105-AFD.json), [.xml](../../automatas/conversiones/L3-AFND-p105-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 5 estados, y el AFD mínimo (Hopcroft), 5. La cota es 2^5 = 32. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-162-188-p-106"></a>

## Lista 3, problema 162-188 (p. 106)

**Enunciado.** AFN para el problema 106 de la Lista 2: Palabras de Σ₁ que incluyen 1101001.

**Clasificación: AFND.** El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### AFND — `L3-AFND-p106`

Archivos: [`L3-AFND-p106.jff`](../../automatas/lista3-afnd/L3-AFND-p106.jff) · [`L3-AFND-p106.json`](../../automatas/lista3-afnd/L3-AFND-p106.json) · [`L3-AFND-p106.xml`](../../automatas/lista3-afnd/L3-AFND-p106.xml). Tipo según la definición: **AFND**, |Q| = 8, Σ = {0, 1, 2}, 13 transiciones.

**Diseño.** q0 con lazo adivina el inicio de 1101001; el último estado es absorbente.

| Estado | 0 | 1 | 2 |
|---|---|---|---|
| →q0 | {q0} | {q0, q1} | {q0} |
| q1 | ∅ | {q2} | ∅ |
| q2 | {q3} | ∅ | ∅ |
| q3 | ∅ | {q4} | ∅ |
| q4 | {q5} | ∅ | ∅ |
| q5 | {q6} | ∅ | ∅ |
| q6 | ∅ | {q7} | ∅ |
| *q7 | {q7} | {q7} | {q7} |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `1101001` | acepta | acepta | acepta |
| 2 | `021101001` | acepta | acepta | acepta |
| 3 | `02201101001` | acepta | acepta | acepta |
| 4 | `112111101001` | acepta | acepta | acepta |
| 5 | `002110010021101001` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `12` | rechaza | rechaza | rechaza |
| 8 | `2211` | rechaza | rechaza | rechaza |
| 9 | `2112222` | rechaza | rechaza | rechaza |
| 10 | `10101212201` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `1101001`: {q0} -1→ {q0, q1} -1→ {q0, q1, q2} -0→ {q0, q3} -1→ {q0, q1, q4} -0→ {q0, q5} -0→ {q0, q6} -1→ {q0, q1, q7} — ✔
  Árbol de cómputo: 5 caminos, 1 de aceptación:
    - q0 -1→ q1 -1→ q2 -0→ q3 -1→ q4 -0→ q5 -0→ q6 -1→ q7 — ✔ acepta
    - q0 -1→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 — ✘ termina fuera de F
    - q0 -1→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q1 — ✘ termina fuera de F
    - q0 -1→ q0 -1→ q0 -0→ q0 -1→ q1 — ✘ muere tras leer `1101`
    - q0 -1→ q0 -1→ q1 — ✘ muere tras leer `11`
2. `021101001`: {q0} -0→ {q0} -2→ {q0} -1→ {q0, q1} -1→ {q0, q1, q2} -0→ {q0, q3} -1→ {q0, q1, q4} -0→ {q0, q5} -0→ {q0, q6} -1→ {q0, q1, q7} — ✔
  Árbol de cómputo: 5 caminos, 1 de aceptación:
    - q0 -0→ q0 -2→ q0 -1→ q1 -1→ q2 -0→ q3 -1→ q4 -0→ q5 -0→ q6 -1→ q7 — ✔ acepta
    - q0 -0→ q0 -2→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 — ✘ termina fuera de F
    - q0 -0→ q0 -2→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q1 — ✘ termina fuera de F
    - q0 -0→ q0 -2→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q1 — ✘ muere tras leer `021101`
    - q0 -0→ q0 -2→ q0 -1→ q0 -1→ q1 — ✘ muere tras leer `0211`
3. `02201101001`: {q0} -0→ {q0} -2→ {q0} -2→ {q0} -0→ {q0} -1→ {q0, q1} -1→ {q0, q1, q2} -0→ {q0, q3} -1→ {q0, q1, q4} -0→ {q0, q5} -0→ {q0, q6} -1→ {q0, q1, q7} — ✔
  Árbol de cómputo: 5 caminos, 1 de aceptación:
    - q0 -0→ q0 -2→ q0 -2→ q0 -0→ q0 -1→ q1 -1→ q2 -0→ q3 -1→ q4 -0→ q5 -0→ q6 -1→ q7 — ✔ acepta
    - q0 -0→ q0 -2→ q0 -2→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 — ✘ termina fuera de F
    - q0 -0→ q0 -2→ q0 -2→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q1 — ✘ termina fuera de F
    - q0 -0→ q0 -2→ q0 -2→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q1 — ✘ muere tras leer `02201101`
    - q0 -0→ q0 -2→ q0 -2→ q0 -0→ q0 -1→ q0 -1→ q1 — ✘ muere tras leer `022011`
4. `112111101001`: {q0} -1→ {q0, q1} -1→ {q0, q1, q2} -2→ {q0} -1→ {q0, q1} -1→ {q0, q1, q2} -1→ {q0, q1, q2} -1→ {q0, q1, q2} -0→ {q0, q3} -1→ {q0, q1, q4} -0→ {q0, q5} -0→ {q0, q6} -1→ {q0, q1, q7} — ✔
  Árbol de cómputo: 9 caminos, 1 de aceptación (se muestran 6):
    - q0 -1→ q0 -1→ q0 -2→ q0 -1→ q0 -1→ q0 -1→ q1 -1→ q2 -0→ q3 -1→ q4 -0→ q5 -0→ q6 -1→ q7 — ✔ acepta
    - q0 -1→ q0 -1→ q0 -2→ q0 -1→ q0 -1→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 — ✘ termina fuera de F
    - q0 -1→ q0 -1→ q0 -2→ q0 -1→ q0 -1→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q1 — ✘ termina fuera de F
    - q0 -1→ q0 -1→ q0 -2→ q0 -1→ q0 -1→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q1 — ✘ muere tras leer `112111101`
    - q0 -1→ q0 -1→ q0 -2→ q0 -1→ q0 -1→ q0 -1→ q0 -1→ q1 — ✘ muere tras leer `1121111`
    - q0 -1→ q0 -1→ q0 -2→ q0 -1→ q0 -1→ q1 -1→ q2 — ✘ muere tras leer `112111`
5. `002110010021101001`: {q0} -0→ {q0} -0→ {q0} -2→ {q0} -1→ {q0, q1} -1→ {q0, q1, q2} -0→ {q0, q3} -0→ {q0} -1→ {q0, q1} -0→ {q0} -0→ {q0} -2→ {q0} -1→ {q0, q1} -1→ {q0, q1, q2} -0→ {q0, q3} -1→ {q0, q1, q4} -0→ {q0, q5} -0→ {q0, q6} -1→ {q0, q1, q7} — ✔
  Árbol de cómputo: 8 caminos, 1 de aceptación (se muestran 6):
    - q0 -0→ q0 -0→ q0 -2→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 -2→ q0 -1→ q1 -1→ q2 -0→ q3 -1→ q4 -0→ q5 -0→ q6 -1→ q7 — ✔ acepta
    - q0 -0→ q0 -0→ q0 -2→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 -2→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 — ✘ termina fuera de F
    - q0 -0→ q0 -0→ q0 -2→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 -2→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q1 — ✘ termina fuera de F
    - q0 -0→ q0 -0→ q0 -2→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 -2→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q1 — ✘ muere tras leer `002110010021101`
    - q0 -0→ q0 -0→ q0 -2→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 -2→ q0 -1→ q0 -1→ q1 — ✘ muere tras leer `0021100100211`
    - q0 -0→ q0 -0→ q0 -2→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q1 — ✘ muere tras leer `00211001`
6. λ: {q0} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
7. `12`: {q0} -1→ {q0, q1} -2→ {q0} — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -1→ q0 -2→ q0 — ✘ termina fuera de F
    - q0 -1→ q1 — ✘ muere tras leer `1`
8. `2211`: {q0} -2→ {q0} -2→ {q0} -1→ {q0, q1} -1→ {q0, q1, q2} — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - q0 -2→ q0 -2→ q0 -1→ q0 -1→ q0 — ✘ termina fuera de F
    - q0 -2→ q0 -2→ q0 -1→ q0 -1→ q1 — ✘ termina fuera de F
    - q0 -2→ q0 -2→ q0 -1→ q1 -1→ q2 — ✘ termina fuera de F
9. `2112222`: {q0} -2→ {q0} -1→ {q0, q1} -1→ {q0, q1, q2} -2→ {q0} -2→ {q0} -2→ {q0} -2→ {q0} — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - q0 -2→ q0 -1→ q0 -1→ q0 -2→ q0 -2→ q0 -2→ q0 -2→ q0 — ✘ termina fuera de F
    - q0 -2→ q0 -1→ q0 -1→ q1 — ✘ muere tras leer `211`
    - q0 -2→ q0 -1→ q1 -1→ q2 — ✘ muere tras leer `211`
10. `10101212201`: {q0} -1→ {q0, q1} -0→ {q0} -1→ {q0, q1} -0→ {q0} -1→ {q0, q1} -2→ {q0} -1→ {q0, q1} -2→ {q0} -2→ {q0} -0→ {q0} -1→ {q0, q1} — ✘
  Árbol de cómputo: 6 caminos, 0 de aceptación:
    - q0 -1→ q0 -0→ q0 -1→ q0 -0→ q0 -1→ q0 -2→ q0 -1→ q0 -2→ q0 -2→ q0 -0→ q0 -1→ q0 — ✘ termina fuera de F
    - q0 -1→ q0 -0→ q0 -1→ q0 -0→ q0 -1→ q0 -2→ q0 -1→ q0 -2→ q0 -2→ q0 -0→ q0 -1→ q1 — ✘ termina fuera de F
    - q0 -1→ q0 -0→ q0 -1→ q0 -0→ q0 -1→ q0 -2→ q0 -1→ q1 — ✘ muere tras leer `1010121`
    - q0 -1→ q0 -0→ q0 -1→ q0 -0→ q0 -1→ q1 — ✘ muere tras leer `10101`
    - q0 -1→ q0 -0→ q0 -1→ q1 — ✘ muere tras leer `101`
    - q0 -1→ q1 — ✘ muere tras leer `1`

</details>

Simulación paso a paso en JFLAP con `12`: [ver captura](../../evidencias/jflap/pasos/L3-AFND-p106.png).

**Conversión.** AFND (8 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 14 estados, [`L3-AFND-p106-AFD.jff`](../../automatas/conversiones/L3-AFND-p106-AFD.jff) ([.json](../../automatas/conversiones/L3-AFND-p106-AFD.json), [.xml](../../automatas/conversiones/L3-AFND-p106-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 14 estados, y el AFD mínimo (Hopcroft), 8. La cota es 2^8 = 256. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-162-188-p-107"></a>

## Lista 3, problema 162-188 (p. 107)

**Enunciado.** AFN para el problema 107 de la Lista 2: Palabras de Σ₁ con 0101 y con 021.

**Clasificación: AFND.** El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### AFND — `L3-AFND-p107`

Archivos: [`L3-AFND-p107.jff`](../../automatas/lista3-afnd/L3-AFND-p107.jff) · [`L3-AFND-p107.json`](../../automatas/lista3-afnd/L3-AFND-p107.json) · [`L3-AFND-p107.xml`](../../automatas/lista3-afnd/L3-AFND-p107.xml). Tipo según la definición: **AFND**, |Q| = 14, Σ = {0, 1, 2}, 26 transiciones.

**Diseño.** Adivina el orden de los patrones: una rama busca 0101 y luego 021; otra, al revés; más las ramas con traslape.

<details><summary>Tabla de transiciones (14 estados)</summary>

| Estado | 0 | 1 | 2 |
|---|---|---|---|
| →q0 | {q0, q1, q7} | {q0} | {q0} |
| q1 | ∅ | {q2} | ∅ |
| q2 | {q3} | ∅ | ∅ |
| q3 | ∅ | {q4} | ∅ |
| q4 | {q4, q5} | {q4} | {q4} |
| q5 | ∅ | ∅ | {q6} |
| q6 | ∅ | {q13} | ∅ |
| q7 | ∅ | ∅ | {q8} |
| q8 | ∅ | {q9} | ∅ |
| q9 | {q10, q9} | {q9} | {q9} |
| q10 | ∅ | {q11} | ∅ |
| q11 | {q12} | ∅ | ∅ |
| q12 | ∅ | {q13} | ∅ |
| *q13 | {q13} | {q13} | {q13} |

</details>

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `0210101` | acepta | acepta | acepta |
| 2 | `120210101` | acepta | acepta | acepta |
| 3 | `22220210101` | acepta | acepta | acepta |
| 4 | `1202210210101` | acepta | acepta | acepta |
| 5 | `02221000220210101` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `20` | rechaza | rechaza | rechaza |
| 8 | `2202` | rechaza | rechaza | rechaza |
| 9 | `1122020` | rechaza | rechaza | rechaza |
| 10 | `20101110102` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `0210101`: {q0} -0→ {q0, q1, q7} -2→ {q0, q8} -1→ {q0, q9} -0→ {q0, q1, q10, q7, q9} -1→ {q0, q11, q2, q9} -0→ {q0, q1, q10, q12, q3, q7, q9} -1→ {q0, q11, q13, q2, q4, q9} — ✔
  Árbol de cómputo: 9 caminos, 1 de aceptación (se muestran 6):
    - q0 -0→ q7 -2→ q8 -1→ q9 -0→ q10 -1→ q11 -0→ q12 -1→ q13 — ✔ acepta
    - q0 -0→ q0 -2→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q0 -1→ q0 — ✘ termina fuera de F
    - q0 -0→ q0 -2→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q1 -1→ q2 — ✘ termina fuera de F
    - q0 -0→ q0 -2→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q7 — ✘ muere tras leer `021010`
    - q0 -0→ q0 -2→ q0 -1→ q0 -0→ q1 -1→ q2 -0→ q3 -1→ q4 — ✘ termina fuera de F
    - q0 -0→ q0 -2→ q0 -1→ q0 -0→ q7 — ✘ muere tras leer `0210`
2. `120210101`: {q0} -1→ {q0} -2→ {q0} -0→ {q0, q1, q7} -2→ {q0, q8} -1→ {q0, q9} -0→ {q0, q1, q10, q7, q9} -1→ {q0, q11, q2, q9} -0→ {q0, q1, q10, q12, q3, q7, q9} -1→ {q0, q11, q13, q2, q4, q9} — ✔
  Árbol de cómputo: 9 caminos, 1 de aceptación (se muestran 6):
    - q0 -1→ q0 -2→ q0 -0→ q7 -2→ q8 -1→ q9 -0→ q10 -1→ q11 -0→ q12 -1→ q13 — ✔ acepta
    - q0 -1→ q0 -2→ q0 -0→ q0 -2→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q0 -1→ q0 — ✘ termina fuera de F
    - q0 -1→ q0 -2→ q0 -0→ q0 -2→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q1 -1→ q2 — ✘ termina fuera de F
    - q0 -1→ q0 -2→ q0 -0→ q0 -2→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q7 — ✘ muere tras leer `12021010`
    - q0 -1→ q0 -2→ q0 -0→ q0 -2→ q0 -1→ q0 -0→ q1 -1→ q2 -0→ q3 -1→ q4 — ✘ termina fuera de F
    - q0 -1→ q0 -2→ q0 -0→ q0 -2→ q0 -1→ q0 -0→ q7 — ✘ muere tras leer `120210`
3. `22220210101`: {q0} -2→ {q0} -2→ {q0} -2→ {q0} -2→ {q0} -0→ {q0, q1, q7} -2→ {q0, q8} -1→ {q0, q9} -0→ {q0, q1, q10, q7, q9} -1→ {q0, q11, q2, q9} -0→ {q0, q1, q10, q12, q3, q7, q9} -1→ {q0, q11, q13, q2, q4, q9} — ✔
  Árbol de cómputo: 9 caminos, 1 de aceptación (se muestran 6):
    - q0 -2→ q0 -2→ q0 -2→ q0 -2→ q0 -0→ q7 -2→ q8 -1→ q9 -0→ q10 -1→ q11 -0→ q12 -1→ q13 — ✔ acepta
    - q0 -2→ q0 -2→ q0 -2→ q0 -2→ q0 -0→ q0 -2→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q0 -1→ q0 — ✘ termina fuera de F
    - q0 -2→ q0 -2→ q0 -2→ q0 -2→ q0 -0→ q0 -2→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q1 -1→ q2 — ✘ termina fuera de F
    - q0 -2→ q0 -2→ q0 -2→ q0 -2→ q0 -0→ q0 -2→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q7 — ✘ muere tras leer `2222021010`
    - q0 -2→ q0 -2→ q0 -2→ q0 -2→ q0 -0→ q0 -2→ q0 -1→ q0 -0→ q1 -1→ q2 -0→ q3 -1→ q4 — ✘ termina fuera de F
    - q0 -2→ q0 -2→ q0 -2→ q0 -2→ q0 -0→ q0 -2→ q0 -1→ q0 -0→ q7 — ✘ muere tras leer `22220210`
4. `1202210210101`: {q0} -1→ {q0} -2→ {q0} -0→ {q0, q1, q7} -2→ {q0, q8} -2→ {q0} -1→ {q0} -0→ {q0, q1, q7} -2→ {q0, q8} -1→ {q0, q9} -0→ {q0, q1, q10, q7, q9} -1→ {q0, q11, q2, q9} -0→ {q0, q1, q10, q12, q3, q7, q9} -1→ {q0, q11, q13, q2, q4, q9} — ✔
  Árbol de cómputo: 11 caminos, 1 de aceptación (se muestran 6):
    - q0 -1→ q0 -2→ q0 -0→ q0 -2→ q0 -2→ q0 -1→ q0 -0→ q7 -2→ q8 -1→ q9 -0→ q10 -1→ q11 -0→ q12 -1→ q13 — ✔ acepta
    - q0 -1→ q0 -2→ q0 -0→ q0 -2→ q0 -2→ q0 -1→ q0 -0→ q0 -2→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q0 -1→ q0 — ✘ termina fuera de F
    - q0 -1→ q0 -2→ q0 -0→ q0 -2→ q0 -2→ q0 -1→ q0 -0→ q0 -2→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q1 -1→ q2 — ✘ termina fuera de F
    - q0 -1→ q0 -2→ q0 -0→ q0 -2→ q0 -2→ q0 -1→ q0 -0→ q0 -2→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q7 — ✘ muere tras leer `120221021010`
    - q0 -1→ q0 -2→ q0 -0→ q0 -2→ q0 -2→ q0 -1→ q0 -0→ q0 -2→ q0 -1→ q0 -0→ q1 -1→ q2 -0→ q3 -1→ q4 — ✘ termina fuera de F
    - q0 -1→ q0 -2→ q0 -0→ q0 -2→ q0 -2→ q0 -1→ q0 -0→ q0 -2→ q0 -1→ q0 -0→ q7 — ✘ muere tras leer `1202210210`
5. `02221000220210101`: {q0} -0→ {q0, q1, q7} -2→ {q0, q8} -2→ {q0} -2→ {q0} -1→ {q0} -0→ {q0, q1, q7} -0→ {q0, q1, q7} -0→ {q0, q1, q7} -2→ {q0, q8} -2→ {q0} -0→ {q0, q1, q7} -2→ {q0, q8} -1→ {q0, q9} -0→ {q0, q1, q10, q7, q9} -1→ {q0, q11, q2, q9} -0→ {q0, q1, q10, q12, q3, q7, q9} -1→ {q0, q11, q13, q2, q4, q9} — ✔
  Árbol de cómputo: 17 caminos, 1 de aceptación (se muestran 6):
    - q0 -0→ q0 -2→ q0 -2→ q0 -2→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -2→ q0 -2→ q0 -0→ q7 -2→ q8 -1→ q9 -0→ q10 -1→ q11 -0→ q12 -1→ q13 — ✔ acepta
    - q0 -0→ q0 -2→ q0 -2→ q0 -2→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -2→ q0 -2→ q0 -0→ q0 -2→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q0 -1→ q0 — ✘ termina fuera de F
    - q0 -0→ q0 -2→ q0 -2→ q0 -2→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -2→ q0 -2→ q0 -0→ q0 -2→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q1 -1→ q2 — ✘ termina fuera de F
    - q0 -0→ q0 -2→ q0 -2→ q0 -2→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -2→ q0 -2→ q0 -0→ q0 -2→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q7 — ✘ muere tras leer `0222100022021010`
    - q0 -0→ q0 -2→ q0 -2→ q0 -2→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -2→ q0 -2→ q0 -0→ q0 -2→ q0 -1→ q0 -0→ q1 -1→ q2 -0→ q3 -1→ q4 — ✘ termina fuera de F
    - q0 -0→ q0 -2→ q0 -2→ q0 -2→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -2→ q0 -2→ q0 -0→ q0 -2→ q0 -1→ q0 -0→ q7 — ✘ muere tras leer `02221000220210`
6. λ: {q0} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
7. `20`: {q0} -2→ {q0} -0→ {q0, q1, q7} — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - q0 -2→ q0 -0→ q0 — ✘ termina fuera de F
    - q0 -2→ q0 -0→ q1 — ✘ termina fuera de F
    - q0 -2→ q0 -0→ q7 — ✘ termina fuera de F
8. `2202`: {q0} -2→ {q0} -2→ {q0} -0→ {q0, q1, q7} -2→ {q0, q8} — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - q0 -2→ q0 -2→ q0 -0→ q0 -2→ q0 — ✘ termina fuera de F
    - q0 -2→ q0 -2→ q0 -0→ q1 — ✘ muere tras leer `220`
    - q0 -2→ q0 -2→ q0 -0→ q7 -2→ q8 — ✘ termina fuera de F
9. `1122020`: {q0} -1→ {q0} -1→ {q0} -2→ {q0} -2→ {q0} -0→ {q0, q1, q7} -2→ {q0, q8} -0→ {q0, q1, q7} — ✘
  Árbol de cómputo: 5 caminos, 0 de aceptación:
    - q0 -1→ q0 -1→ q0 -2→ q0 -2→ q0 -0→ q0 -2→ q0 -0→ q0 — ✘ termina fuera de F
    - q0 -1→ q0 -1→ q0 -2→ q0 -2→ q0 -0→ q0 -2→ q0 -0→ q1 — ✘ termina fuera de F
    - q0 -1→ q0 -1→ q0 -2→ q0 -2→ q0 -0→ q0 -2→ q0 -0→ q7 — ✘ termina fuera de F
    - q0 -1→ q0 -1→ q0 -2→ q0 -2→ q0 -0→ q1 — ✘ muere tras leer `11220`
    - q0 -1→ q0 -1→ q0 -2→ q0 -2→ q0 -0→ q7 -2→ q8 — ✘ muere tras leer `112202`
10. `20101110102`: {q0} -2→ {q0} -0→ {q0, q1, q7} -1→ {q0, q2} -0→ {q0, q1, q3, q7} -1→ {q0, q2, q4} -1→ {q0, q4} -1→ {q0, q4} -0→ {q0, q1, q4, q5, q7} -1→ {q0, q2, q4} -0→ {q0, q1, q3, q4, q5, q7} -2→ {q0, q4, q6, q8} — ✘
  Árbol de cómputo: 11 caminos, 0 de aceptación (se muestran 6):
    - q0 -2→ q0 -0→ q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q0 -2→ q0 — ✘ termina fuera de F
    - q0 -2→ q0 -0→ q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q1 — ✘ muere tras leer `2010111010`
    - q0 -2→ q0 -0→ q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q7 -2→ q8 — ✘ termina fuera de F
    - q0 -2→ q0 -0→ q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -1→ q0 -0→ q1 -1→ q2 -0→ q3 — ✘ muere tras leer `2010111010`
    - q0 -2→ q0 -0→ q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -1→ q0 -0→ q7 — ✘ muere tras leer `20101110`
    - q0 -2→ q0 -0→ q0 -1→ q0 -0→ q1 -1→ q2 — ✘ muere tras leer `20101`

</details>

Simulación paso a paso en JFLAP con `20`: [ver captura](../../evidencias/jflap/pasos/L3-AFND-p107.png).

**Conversión.** AFND (14 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 20 estados, [`L3-AFND-p107-AFD.jff`](../../automatas/conversiones/L3-AFND-p107-AFD.jff) ([.json](../../automatas/conversiones/L3-AFND-p107-AFD.json), [.xml](../../automatas/conversiones/L3-AFND-p107-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 20 estados, y el AFD mínimo (Hopcroft), 13. La cota es 2^14 = 16384. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-162-188-p-109"></a>

## Lista 3, problema 162-188 (p. 109)

**Enunciado.** AFN para el problema 109 de la Lista 2: Σ₂: abbcb y cbaabb, con traslape.

**Clasificación: AFND.** El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### AFND — `L3-AFND-p109`

Archivos: [`L3-AFND-p109.jff`](../../automatas/lista3-afnd/L3-AFND-p109.jff) · [`L3-AFND-p109.json`](../../automatas/lista3-afnd/L3-AFND-p109.json) · [`L3-AFND-p109.xml`](../../automatas/lista3-afnd/L3-AFND-p109.xml). Tipo según la definición: **AFND**, |Q| = 37, Σ = {0, 1, a, b, c}, 59 transiciones.

**Diseño.** Ramas para cada orden de los patrones y para los traslapes posibles.

<details><summary>Tabla de transiciones (37 estados)</summary>

| Estado | 0 | 1 | a | b | c |
|---|---|---|---|---|---|
| →q0 | {q0} | {q0} | {q0, q1, q21} | {q0} | {q0, q11, q29} |
| q1 | ∅ | ∅ | ∅ | {q2} | ∅ |
| q2 | ∅ | ∅ | ∅ | {q3} | ∅ |
| q3 | ∅ | ∅ | ∅ | ∅ | {q4} |
| q4 | ∅ | ∅ | ∅ | {q5} | ∅ |
| q5 | {q5} | {q5} | {q5} | {q5} | {q5, q6} |
| q6 | ∅ | ∅ | ∅ | {q7} | ∅ |
| q7 | ∅ | ∅ | {q8} | ∅ | ∅ |
| q8 | ∅ | ∅ | {q9} | ∅ | ∅ |
| q9 | ∅ | ∅ | ∅ | {q10} | ∅ |
| q10 | ∅ | ∅ | ∅ | {q36} | ∅ |
| q11 | ∅ | ∅ | ∅ | {q12} | ∅ |
| q12 | ∅ | ∅ | {q13} | ∅ | ∅ |
| q13 | ∅ | ∅ | {q14} | ∅ | ∅ |
| q14 | ∅ | ∅ | ∅ | {q15} | ∅ |
| q15 | ∅ | ∅ | ∅ | {q16} | ∅ |
| q16 | {q16} | {q16} | {q16, q17} | {q16} | {q16} |
| q17 | ∅ | ∅ | ∅ | {q18} | ∅ |
| q18 | ∅ | ∅ | ∅ | {q19} | ∅ |
| q19 | ∅ | ∅ | ∅ | ∅ | {q20} |
| q20 | ∅ | ∅ | ∅ | {q36} | ∅ |
| q21 | ∅ | ∅ | ∅ | {q22} | ∅ |
| q22 | ∅ | ∅ | ∅ | {q23} | ∅ |
| q23 | ∅ | ∅ | ∅ | ∅ | {q24} |
| q24 | ∅ | ∅ | ∅ | {q25} | ∅ |
| q25 | ∅ | ∅ | {q26} | ∅ | ∅ |
| q26 | ∅ | ∅ | {q27} | ∅ | ∅ |
| q27 | ∅ | ∅ | ∅ | {q28} | ∅ |
| q28 | ∅ | ∅ | ∅ | {q36} | ∅ |
| q29 | ∅ | ∅ | ∅ | {q30} | ∅ |
| q30 | ∅ | ∅ | {q31} | ∅ | ∅ |
| q31 | ∅ | ∅ | {q32} | ∅ | ∅ |
| q32 | ∅ | ∅ | ∅ | {q33} | ∅ |
| q33 | ∅ | ∅ | ∅ | {q34} | ∅ |
| q34 | ∅ | ∅ | ∅ | ∅ | {q35} |
| q35 | ∅ | ∅ | ∅ | {q36} | ∅ |
| *q36 | {q36} | {q36} | {q36} | {q36} | {q36} |

</details>

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `cbaabbcb` | acepta | acepta | acepta |
| 2 | `c1cbaabbcb` | acepta | acepta | acepta |
| 3 | `0aabbcbaabb` | acepta | acepta | acepta |
| 4 | `0baabcabbcbaabb` | acepta | acepta | acepta |
| 5 | `c0b0baba10bcbaabbcb` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `b1` | rechaza | rechaza | rechaza |
| 8 | `a10a` | rechaza | rechaza | rechaza |
| 9 | `ba0aba0` | rechaza | rechaza | rechaza |
| 10 | `c0a10ba1a10` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `cbaabbcb`: {q0} -c→ {q0, q11, q29} -b→ {q0, q12, q30} -a→ {q0, q1, q13, q21, q31} -a→ {q0, q1, q14, q21, q32} -b→ {q0, q15, q2, q22, q33} -b→ {q0, q16, q23, q3, q34} -c→ {q0, q11, q16, q24, q29, q35, q4} -b→ {q0, q12, q16, q25, q30, q36, q5} — ✔
  Árbol de cómputo: 9 caminos, 1 de aceptación (se muestran 6):
    - q0 -c→ q29 -b→ q30 -a→ q31 -a→ q32 -b→ q33 -b→ q34 -c→ q35 -b→ q36 — ✔ acepta
    - q0 -c→ q0 -b→ q0 -a→ q0 -a→ q0 -b→ q0 -b→ q0 -c→ q0 -b→ q0 — ✘ termina fuera de F
    - q0 -c→ q0 -b→ q0 -a→ q0 -a→ q0 -b→ q0 -b→ q0 -c→ q11 -b→ q12 — ✘ termina fuera de F
    - q0 -c→ q0 -b→ q0 -a→ q0 -a→ q0 -b→ q0 -b→ q0 -c→ q29 -b→ q30 — ✘ termina fuera de F
    - q0 -c→ q0 -b→ q0 -a→ q0 -a→ q1 -b→ q2 -b→ q3 -c→ q4 -b→ q5 — ✘ termina fuera de F
    - q0 -c→ q0 -b→ q0 -a→ q0 -a→ q21 -b→ q22 -b→ q23 -c→ q24 -b→ q25 — ✘ termina fuera de F
2. `c1cbaabbcb`: {q0} -c→ {q0, q11, q29} -1→ {q0} -c→ {q0, q11, q29} -b→ {q0, q12, q30} -a→ {q0, q1, q13, q21, q31} -a→ {q0, q1, q14, q21, q32} -b→ {q0, q15, q2, q22, q33} -b→ {q0, q16, q23, q3, q34} -c→ {q0, q11, q16, q24, q29, q35, q4} -b→ {q0, q12, q16, q25, q30, q36, q5} — ✔
  Árbol de cómputo: 11 caminos, 1 de aceptación (se muestran 6):
    - q0 -c→ q0 -1→ q0 -c→ q29 -b→ q30 -a→ q31 -a→ q32 -b→ q33 -b→ q34 -c→ q35 -b→ q36 — ✔ acepta
    - q0 -c→ q0 -1→ q0 -c→ q0 -b→ q0 -a→ q0 -a→ q0 -b→ q0 -b→ q0 -c→ q0 -b→ q0 — ✘ termina fuera de F
    - q0 -c→ q0 -1→ q0 -c→ q0 -b→ q0 -a→ q0 -a→ q0 -b→ q0 -b→ q0 -c→ q11 -b→ q12 — ✘ termina fuera de F
    - q0 -c→ q0 -1→ q0 -c→ q0 -b→ q0 -a→ q0 -a→ q0 -b→ q0 -b→ q0 -c→ q29 -b→ q30 — ✘ termina fuera de F
    - q0 -c→ q0 -1→ q0 -c→ q0 -b→ q0 -a→ q0 -a→ q1 -b→ q2 -b→ q3 -c→ q4 -b→ q5 — ✘ termina fuera de F
    - q0 -c→ q0 -1→ q0 -c→ q0 -b→ q0 -a→ q0 -a→ q21 -b→ q22 -b→ q23 -c→ q24 -b→ q25 — ✘ termina fuera de F
3. `0aabbcbaabb`: {q0} -0→ {q0} -a→ {q0, q1, q21} -a→ {q0, q1, q21} -b→ {q0, q2, q22} -b→ {q0, q23, q3} -c→ {q0, q11, q24, q29, q4} -b→ {q0, q12, q25, q30, q5} -a→ {q0, q1, q13, q21, q26, q31, q5} -a→ {q0, q1, q14, q21, q27, q32, q5} -b→ {q0, q15, q2, q22, q28, q33, q5} -b→ {q0, q16, q23, q3, q34, q36, q5} — ✔
  Árbol de cómputo: 11 caminos, 1 de aceptación (se muestran 6):
    - q0 -0→ q0 -a→ q0 -a→ q21 -b→ q22 -b→ q23 -c→ q24 -b→ q25 -a→ q26 -a→ q27 -b→ q28 -b→ q36 — ✔ acepta
    - q0 -0→ q0 -a→ q0 -a→ q0 -b→ q0 -b→ q0 -c→ q0 -b→ q0 -a→ q0 -a→ q0 -b→ q0 -b→ q0 — ✘ termina fuera de F
    - q0 -0→ q0 -a→ q0 -a→ q0 -b→ q0 -b→ q0 -c→ q0 -b→ q0 -a→ q0 -a→ q1 -b→ q2 -b→ q3 — ✘ termina fuera de F
    - q0 -0→ q0 -a→ q0 -a→ q0 -b→ q0 -b→ q0 -c→ q0 -b→ q0 -a→ q0 -a→ q21 -b→ q22 -b→ q23 — ✘ termina fuera de F
    - q0 -0→ q0 -a→ q0 -a→ q0 -b→ q0 -b→ q0 -c→ q0 -b→ q0 -a→ q1 — ✘ muere tras leer `0aabbcba`
    - q0 -0→ q0 -a→ q0 -a→ q0 -b→ q0 -b→ q0 -c→ q0 -b→ q0 -a→ q21 — ✘ muere tras leer `0aabbcba`
4. `0baabcabbcbaabb`: {q0} -0→ {q0} -b→ {q0} -a→ {q0, q1, q21} -a→ {q0, q1, q21} -b→ {q0, q2, q22} -c→ {q0, q11, q29} -a→ {q0, q1, q21} -b→ {q0, q2, q22} -b→ {q0, q23, q3} -c→ {q0, q11, q24, q29, q4} -b→ {q0, q12, q25, q30, q5} -a→ {q0, q1, q13, q21, q26, q31, q5} -a→ {q0, q1, q14, q21, q27, q32, q5} -b→ {q0, q15, q2, q22, q28, q33, q5} -b→ {q0, q16, q23, q3, q34, q36, q5} — ✔
  Árbol de cómputo: 15 caminos, 1 de aceptación (se muestran 6):
    - q0 -0→ q0 -b→ q0 -a→ q0 -a→ q0 -b→ q0 -c→ q0 -a→ q21 -b→ q22 -b→ q23 -c→ q24 -b→ q25 -a→ q26 -a→ q27 -b→ q28 -b→ q36 — ✔ acepta
    - q0 -0→ q0 -b→ q0 -a→ q0 -a→ q0 -b→ q0 -c→ q0 -a→ q0 -b→ q0 -b→ q0 -c→ q0 -b→ q0 -a→ q0 -a→ q0 -b→ q0 -b→ q0 — ✘ termina fuera de F
    - q0 -0→ q0 -b→ q0 -a→ q0 -a→ q0 -b→ q0 -c→ q0 -a→ q0 -b→ q0 -b→ q0 -c→ q0 -b→ q0 -a→ q0 -a→ q1 -b→ q2 -b→ q3 — ✘ termina fuera de F
    - q0 -0→ q0 -b→ q0 -a→ q0 -a→ q0 -b→ q0 -c→ q0 -a→ q0 -b→ q0 -b→ q0 -c→ q0 -b→ q0 -a→ q0 -a→ q21 -b→ q22 -b→ q23 — ✘ termina fuera de F
    - q0 -0→ q0 -b→ q0 -a→ q0 -a→ q0 -b→ q0 -c→ q0 -a→ q0 -b→ q0 -b→ q0 -c→ q0 -b→ q0 -a→ q1 — ✘ muere tras leer `0baabcabbcba`
    - q0 -0→ q0 -b→ q0 -a→ q0 -a→ q0 -b→ q0 -c→ q0 -a→ q0 -b→ q0 -b→ q0 -c→ q0 -b→ q0 -a→ q21 — ✘ muere tras leer `0baabcabbcba`
5. `c0b0baba10bcbaabbcb`: {q0} -c→ {q0, q11, q29} -0→ {q0} -b→ {q0} -0→ {q0} -b→ {q0} -a→ {q0, q1, q21} -b→ {q0, q2, q22} -a→ {q0, q1, q21} -1→ {q0} -0→ {q0} -b→ {q0} -c→ {q0, q11, q29} -b→ {q0, q12, q30} -a→ {q0, q1, q13, q21, q31} -a→ {q0, q1, q14, q21, q32} -b→ {q0, q15, q2, q22, q33} -b→ {q0, q16, q23, q3, q34} -c→ {q0, q11, q16, q24, q29, q35, q4} -b→ {q0, q12, q16, q25, q30, q36, q5} — ✔
  Árbol de cómputo: 15 caminos, 1 de aceptación (se muestran 6):
    - q0 -c→ q0 -0→ q0 -b→ q0 -0→ q0 -b→ q0 -a→ q0 -b→ q0 -a→ q0 -1→ q0 -0→ q0 -b→ q0 -c→ q29 -b→ q30 -a→ q31 -a→ q32 -b→ q33 -b→ q34 -c→ q35 -b→ q36 — ✔ acepta
    - q0 -c→ q0 -0→ q0 -b→ q0 -0→ q0 -b→ q0 -a→ q0 -b→ q0 -a→ q0 -1→ q0 -0→ q0 -b→ q0 -c→ q0 -b→ q0 -a→ q0 -a→ q0 -b→ q0 -b→ q0 -c→ q0 -b→ q0 — ✘ termina fuera de F
    - q0 -c→ q0 -0→ q0 -b→ q0 -0→ q0 -b→ q0 -a→ q0 -b→ q0 -a→ q0 -1→ q0 -0→ q0 -b→ q0 -c→ q0 -b→ q0 -a→ q0 -a→ q0 -b→ q0 -b→ q0 -c→ q11 -b→ q12 — ✘ termina fuera de F
    - q0 -c→ q0 -0→ q0 -b→ q0 -0→ q0 -b→ q0 -a→ q0 -b→ q0 -a→ q0 -1→ q0 -0→ q0 -b→ q0 -c→ q0 -b→ q0 -a→ q0 -a→ q0 -b→ q0 -b→ q0 -c→ q29 -b→ q30 — ✘ termina fuera de F
    - q0 -c→ q0 -0→ q0 -b→ q0 -0→ q0 -b→ q0 -a→ q0 -b→ q0 -a→ q0 -1→ q0 -0→ q0 -b→ q0 -c→ q0 -b→ q0 -a→ q0 -a→ q1 -b→ q2 -b→ q3 -c→ q4 -b→ q5 — ✘ termina fuera de F
    - q0 -c→ q0 -0→ q0 -b→ q0 -0→ q0 -b→ q0 -a→ q0 -b→ q0 -a→ q0 -1→ q0 -0→ q0 -b→ q0 -c→ q0 -b→ q0 -a→ q0 -a→ q21 -b→ q22 -b→ q23 -c→ q24 -b→ q25 — ✘ termina fuera de F
6. λ: {q0} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
7. `b1`: {q0} -b→ {q0} -1→ {q0} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 -b→ q0 -1→ q0 — ✘ termina fuera de F
8. `a10a`: {q0} -a→ {q0, q1, q21} -1→ {q0} -0→ {q0} -a→ {q0, q1, q21} — ✘
  Árbol de cómputo: 5 caminos, 0 de aceptación:
    - q0 -a→ q0 -1→ q0 -0→ q0 -a→ q0 — ✘ termina fuera de F
    - q0 -a→ q0 -1→ q0 -0→ q0 -a→ q1 — ✘ termina fuera de F
    - q0 -a→ q0 -1→ q0 -0→ q0 -a→ q21 — ✘ termina fuera de F
    - q0 -a→ q1 — ✘ muere tras leer `a`
    - q0 -a→ q21 — ✘ muere tras leer `a`
9. `ba0aba0`: {q0} -b→ {q0} -a→ {q0, q1, q21} -0→ {q0} -a→ {q0, q1, q21} -b→ {q0, q2, q22} -a→ {q0, q1, q21} -0→ {q0} — ✘
  Árbol de cómputo: 7 caminos, 0 de aceptación (se muestran 6):
    - q0 -b→ q0 -a→ q0 -0→ q0 -a→ q0 -b→ q0 -a→ q0 -0→ q0 — ✘ termina fuera de F
    - q0 -b→ q0 -a→ q0 -0→ q0 -a→ q0 -b→ q0 -a→ q1 — ✘ muere tras leer `ba0aba`
    - q0 -b→ q0 -a→ q0 -0→ q0 -a→ q0 -b→ q0 -a→ q21 — ✘ muere tras leer `ba0aba`
    - q0 -b→ q0 -a→ q0 -0→ q0 -a→ q1 -b→ q2 — ✘ muere tras leer `ba0ab`
    - q0 -b→ q0 -a→ q0 -0→ q0 -a→ q21 -b→ q22 — ✘ muere tras leer `ba0ab`
    - q0 -b→ q0 -a→ q1 — ✘ muere tras leer `ba`
10. `c0a10ba1a10`: {q0} -c→ {q0, q11, q29} -0→ {q0} -a→ {q0, q1, q21} -1→ {q0} -0→ {q0} -b→ {q0} -a→ {q0, q1, q21} -1→ {q0} -a→ {q0, q1, q21} -1→ {q0} -0→ {q0} — ✘
  Árbol de cómputo: 9 caminos, 0 de aceptación (se muestran 6):
    - q0 -c→ q0 -0→ q0 -a→ q0 -1→ q0 -0→ q0 -b→ q0 -a→ q0 -1→ q0 -a→ q0 -1→ q0 -0→ q0 — ✘ termina fuera de F
    - q0 -c→ q0 -0→ q0 -a→ q0 -1→ q0 -0→ q0 -b→ q0 -a→ q0 -1→ q0 -a→ q1 — ✘ muere tras leer `c0a10ba1a`
    - q0 -c→ q0 -0→ q0 -a→ q0 -1→ q0 -0→ q0 -b→ q0 -a→ q0 -1→ q0 -a→ q21 — ✘ muere tras leer `c0a10ba1a`
    - q0 -c→ q0 -0→ q0 -a→ q0 -1→ q0 -0→ q0 -b→ q0 -a→ q1 — ✘ muere tras leer `c0a10ba`
    - q0 -c→ q0 -0→ q0 -a→ q0 -1→ q0 -0→ q0 -b→ q0 -a→ q21 — ✘ muere tras leer `c0a10ba`
    - q0 -c→ q0 -0→ q0 -a→ q1 — ✘ muere tras leer `c0a`

</details>

Simulación paso a paso en JFLAP con `b1`: [ver captura](../../evidencias/jflap/pasos/L3-AFND-p109.png).

**Conversión.** AFND (37 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 64 estados, [`L3-AFND-p109-AFD.jff`](../../automatas/conversiones/L3-AFND-p109-AFD.jff) ([.json](../../automatas/conversiones/L3-AFND-p109-AFD.json), [.xml](../../automatas/conversiones/L3-AFND-p109-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 64 estados, y el AFD mínimo (Hopcroft), 22. La cota es 2^37 = 137438953472. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-162-188-p-110"></a>

## Lista 3, problema 162-188 (p. 110)

**Enunciado.** AFN para el problema 110 de la Lista 2: Las palabras de Σ₁ que contienen exactamente tres veces la subcadena 01.

**Clasificación: AFND.** El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD.

#### AFND — `L3-AFND-p110`

Archivos: [`L3-AFND-p110.jff`](../../automatas/lista3-afnd/L3-AFND-p110.jff) · [`L3-AFND-p110.json`](../../automatas/lista3-afnd/L3-AFND-p110.json) · [`L3-AFND-p110.xml`](../../automatas/lista3-afnd/L3-AFND-p110.xml). Tipo según la definición: **AFD**, |Q| = 9, Σ = {0, 1, 2}, 27 transiciones.

**Diseño.** Se conserva el AFD (como en los problemas 111-113 de la Práctica 1): un AFND acepta si algún camino acepta, así que adivinar tres ocurrencias no impide que haya una cuarta. Contar «exactamente» exige descartar todas las demás, y eso lo hace el AFD.

| Estado | 0 | 1 | 2 |
|---|---|---|---|
| →q0 | q1 | q0 | q0 |
| q1 | q1 | q2 | q0 |
| q2 | q3 | q2 | q2 |
| q3 | q3 | q4 | q2 |
| q4 | q5 | q4 | q4 |
| q5 | q5 | q6 | q4 |
| *q6 | q7 | q6 | q6 |
| *q7 | q7 | q8 | q6 |
| q8 | q8 | q8 | q8 |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `010101` | acepta | acepta | acepta |
| 2 | `22010101` | acepta | acepta | acepta |
| 3 | `0002010101` | acepta | acepta | acepta |
| 4 | `0210022010101` | acepta | acepta | acepta |
| 5 | `220220112110101` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `00` | rechaza | rechaza | rechaza |
| 8 | `0112` | rechaza | rechaza | rechaza |
| 9 | `0212122` | rechaza | rechaza | rechaza |
| 10 | `00202121100` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `010101`: q0 -0→ q1 -1→ q2 -0→ q3 -1→ q4 -0→ q5 -1→ q6 — ✔
2. `22010101`: q0 -2→ q0 -2→ q0 -0→ q1 -1→ q2 -0→ q3 -1→ q4 -0→ q5 -1→ q6 — ✔
3. `0002010101`: q0 -0→ q1 -0→ q1 -0→ q1 -2→ q0 -0→ q1 -1→ q2 -0→ q3 -1→ q4 -0→ q5 -1→ q6 — ✔
4. `0210022010101`: q0 -0→ q1 -2→ q0 -1→ q0 -0→ q1 -0→ q1 -2→ q0 -2→ q0 -0→ q1 -1→ q2 -0→ q3 -1→ q4 -0→ q5 -1→ q6 — ✔
5. `220220112110101`: q0 -2→ q0 -2→ q0 -0→ q1 -2→ q0 -2→ q0 -0→ q1 -1→ q2 -1→ q2 -2→ q2 -1→ q2 -1→ q2 -0→ q3 -1→ q4 -0→ q5 -1→ q6 — ✔
6. λ: q0 — ✘
7. `00`: q0 -0→ q1 -0→ q1 — ✘
8. `0112`: q0 -0→ q1 -1→ q2 -1→ q2 -2→ q2 — ✘
9. `0212122`: q0 -0→ q1 -2→ q0 -1→ q0 -2→ q0 -1→ q0 -2→ q0 -2→ q0 — ✘
10. `00202121100`: q0 -0→ q1 -0→ q1 -2→ q0 -0→ q1 -2→ q0 -1→ q0 -2→ q0 -1→ q0 -1→ q0 -0→ q1 -0→ q1 — ✘

</details>

Simulación paso a paso en JFLAP con `010101`: [ver captura](../../evidencias/jflap/pasos/L3-AFND-p110.png).

<a id="problema-3-162-188-p-111"></a>

## Lista 3, problema 162-188 (p. 111)

**Enunciado.** AFN para el problema 111 de la Lista 2: Exactamente tres veces 01002.

**Clasificación: AFND.** El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### AFND — `L3-AFND-p111`

Archivos: [`L3-AFND-p111.jff`](../../automatas/lista3-afnd/L3-AFND-p111.jff) · [`L3-AFND-p111.json`](../../automatas/lista3-afnd/L3-AFND-p111.json) · [`L3-AFND-p111.xml`](../../automatas/lista3-afnd/L3-AFND-p111.xml). Tipo según la definición: **AFD**, |Q| = 21, Σ = {0, 1, 2}, 63 transiciones.

**Diseño.** Se conserva el AFD: el AFN acepta si algún camino acepta, por lo que adivinar posiciones no garantiza que no haya más ocurrencias.

<details><summary>Tabla de transiciones (21 estados)</summary>

| Estado | 0 | 1 | 2 |
|---|---|---|---|
| →q0 | q1 | q0 | q0 |
| q1 | q1 | q2 | q0 |
| q2 | q3 | q0 | q0 |
| q3 | q4 | q2 | q0 |
| q4 | q1 | q2 | q5 |
| q5 | q6 | q5 | q5 |
| q6 | q6 | q7 | q5 |
| q7 | q8 | q5 | q5 |
| q8 | q9 | q7 | q5 |
| q9 | q6 | q7 | q10 |
| q10 | q11 | q10 | q10 |
| q11 | q11 | q12 | q10 |
| q12 | q13 | q10 | q10 |
| q13 | q14 | q12 | q10 |
| q14 | q11 | q12 | q15 |
| *q15 | q16 | q15 | q15 |
| *q16 | q16 | q17 | q15 |
| *q17 | q18 | q15 | q15 |
| *q18 | q19 | q17 | q15 |
| *q19 | q16 | q17 | q20 |
| q20 | q20 | q20 | q20 |

</details>

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `010020100201002` | acepta | acepta | acepta |
| 2 | `11010020100201002` | acepta | acepta | acepta |
| 3 | `210010020100201002` | acepta | acepta | acepta |
| 4 | `1020012010020100201002` | acepta | acepta | acepta |
| 5 | `10111102021010020100201002` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `21` | rechaza | rechaza | rechaza |
| 8 | `1102` | rechaza | rechaza | rechaza |
| 9 | `1221000` | rechaza | rechaza | rechaza |
| 10 | `01201002202` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `010020100201002`: q0 -0→ q1 -1→ q2 -0→ q3 -0→ q4 -2→ q5 -0→ q6 -1→ q7 -0→ q8 -0→ q9 -2→ q10 -0→ q11 -1→ q12 -0→ q13 -0→ q14 -2→ q15 — ✔
2. `11010020100201002`: q0 -1→ q0 -1→ q0 -0→ q1 -1→ q2 -0→ q3 -0→ q4 -2→ q5 -0→ q6 -1→ q7 -0→ q8 -0→ q9 -2→ q10 -0→ q11 -1→ q12 -0→ q13 -0→ q14 -2→ q15 — ✔
3. `210010020100201002`: q0 -2→ q0 -1→ q0 -0→ q1 -0→ q1 -1→ q2 -0→ q3 -0→ q4 -2→ q5 -0→ q6 -1→ q7 -0→ q8 -0→ q9 -2→ q10 -0→ q11 -1→ q12 -0→ q13 -0→ q14 -2→ q15 — ✔
4. `1020012010020100201002`: q0 -1→ q0 -0→ q1 -2→ q0 -0→ q1 -0→ q1 -1→ q2 -2→ q0 -0→ q1 -1→ q2 -0→ q3 -0→ q4 -2→ q5 -0→ q6 -1→ q7 -0→ q8 -0→ q9 -2→ q10 -0→ q11 -1→ q12 -0→ q13 -0→ q14 -2→ q15 — ✔
5. `10111102021010020100201002`: q0 -1→ q0 -0→ q1 -1→ q2 -1→ q0 -1→ q0 -1→ q0 -0→ q1 -2→ q0 -0→ q1 -2→ q0 -1→ q0 -0→ q1 -1→ q2 -0→ q3 -0→ q4 -2→ q5 -0→ q6 -1→ q7 -0→ q8 -0→ q9 -2→ q10 -0→ q11 -1→ q12 -0→ q13 -0→ q14 -2→ q15 — ✔
6. λ: q0 — ✘
7. `21`: q0 -2→ q0 -1→ q0 — ✘
8. `1102`: q0 -1→ q0 -1→ q0 -0→ q1 -2→ q0 — ✘
9. `1221000`: q0 -1→ q0 -2→ q0 -2→ q0 -1→ q0 -0→ q1 -0→ q1 -0→ q1 — ✘
10. `01201002202`: q0 -0→ q1 -1→ q2 -2→ q0 -0→ q1 -1→ q2 -0→ q3 -0→ q4 -2→ q5 -2→ q5 -0→ q6 -2→ q5 — ✘

</details>

Simulación paso a paso en JFLAP con `21`: [ver captura](../../evidencias/jflap/pasos/L3-AFND-p111.png).

<a id="problema-3-162-188-p-112"></a>

## Lista 3, problema 162-188 (p. 112)

**Enunciado.** AFN para el problema 112 de la Lista 2: Dos veces 010 sin traslape.

**Clasificación: AFND.** El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### AFND — `L3-AFND-p112`

Archivos: [`L3-AFND-p112.jff`](../../automatas/lista3-afnd/L3-AFND-p112.jff) · [`L3-AFND-p112.json`](../../automatas/lista3-afnd/L3-AFND-p112.json) · [`L3-AFND-p112.xml`](../../automatas/lista3-afnd/L3-AFND-p112.xml). Tipo según la definición: **AFD**, |Q| = 10, Σ = {0, 1, 2}, 30 transiciones.

**Diseño.** Se conserva el AFD por la misma razón que el 111: contar exactamente requiere descartar todas las demás ocurrencias.

| Estado | 0 | 1 | 2 |
|---|---|---|---|
| →q0 | q1 | q0 | q0 |
| q1 | q1 | q2 | q0 |
| q2 | q3 | q0 | q0 |
| q3 | q4 | q3 | q3 |
| q4 | q4 | q5 | q3 |
| q5 | q6 | q3 | q3 |
| *q6 | q7 | q6 | q6 |
| *q7 | q7 | q8 | q6 |
| *q8 | q9 | q6 | q6 |
| q9 | q9 | q9 | q9 |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `010010` | acepta | acepta | acepta |
| 2 | `1010010` | acepta | acepta | acepta |
| 3 | `202010010` | acepta | acepta | acepta |
| 4 | `0211002010010` | acepta | acepta | acepta |
| 5 | `11201010112010` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `00` | rechaza | rechaza | rechaza |
| 8 | `0022` | rechaza | rechaza | rechaza |
| 9 | `0020002` | rechaza | rechaza | rechaza |
| 10 | `21202010000` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `010010`: q0 -0→ q1 -1→ q2 -0→ q3 -0→ q4 -1→ q5 -0→ q6 — ✔
2. `1010010`: q0 -1→ q0 -0→ q1 -1→ q2 -0→ q3 -0→ q4 -1→ q5 -0→ q6 — ✔
3. `202010010`: q0 -2→ q0 -0→ q1 -2→ q0 -0→ q1 -1→ q2 -0→ q3 -0→ q4 -1→ q5 -0→ q6 — ✔
4. `0211002010010`: q0 -0→ q1 -2→ q0 -1→ q0 -1→ q0 -0→ q1 -0→ q1 -2→ q0 -0→ q1 -1→ q2 -0→ q3 -0→ q4 -1→ q5 -0→ q6 — ✔
5. `11201010112010`: q0 -1→ q0 -1→ q0 -2→ q0 -0→ q1 -1→ q2 -0→ q3 -1→ q3 -0→ q4 -1→ q5 -1→ q3 -2→ q3 -0→ q4 -1→ q5 -0→ q6 — ✔
6. λ: q0 — ✘
7. `00`: q0 -0→ q1 -0→ q1 — ✘
8. `0022`: q0 -0→ q1 -0→ q1 -2→ q0 -2→ q0 — ✘
9. `0020002`: q0 -0→ q1 -0→ q1 -2→ q0 -0→ q1 -0→ q1 -0→ q1 -2→ q0 — ✘
10. `21202010000`: q0 -2→ q0 -1→ q0 -2→ q0 -0→ q1 -2→ q0 -0→ q1 -1→ q2 -0→ q3 -0→ q4 -0→ q4 -0→ q4 — ✘

</details>

Simulación paso a paso en JFLAP con `010010`: [ver captura](../../evidencias/jflap/pasos/L3-AFND-p112.png).

<a id="problema-3-162-188-p-113"></a>

## Lista 3, problema 162-188 (p. 113)

**Enunciado.** AFN para el problema 113 de la Lista 2: Dos veces 010 con traslape.

**Clasificación: AFND.** El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### AFND — `L3-AFND-p113`

Archivos: [`L3-AFND-p113.jff`](../../automatas/lista3-afnd/L3-AFND-p113.jff) · [`L3-AFND-p113.json`](../../automatas/lista3-afnd/L3-AFND-p113.json) · [`L3-AFND-p113.xml`](../../automatas/lista3-afnd/L3-AFND-p113.xml). Tipo según la definición: **AFD**, |Q| = 10, Σ = {0, 1, 2}, 30 transiciones.

**Diseño.** Se conserva el AFD por la misma razón que el 111.

| Estado | 0 | 1 | 2 |
|---|---|---|---|
| →q0 | q1 | q0 | q0 |
| q1 | q1 | q2 | q0 |
| q2 | q3 | q0 | q0 |
| q3 | q3 | q4 | q5 |
| q4 | q6 | q5 | q5 |
| q5 | q3 | q5 | q5 |
| *q6 | q6 | q7 | q8 |
| *q7 | q9 | q8 | q8 |
| *q8 | q6 | q8 | q8 |
| q9 | q9 | q9 | q9 |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `01010` | acepta | acepta | acepta |
| 2 | `1201010` | acepta | acepta | acepta |
| 3 | `01101010` | acepta | acepta | acepta |
| 4 | `1122201010` | acepta | acepta | acepta |
| 5 | `01022100111010` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `02` | rechaza | rechaza | rechaza |
| 8 | `2210` | rechaza | rechaza | rechaza |
| 9 | `2010220` | rechaza | rechaza | rechaza |
| 10 | `12200202120` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `01010`: q0 -0→ q1 -1→ q2 -0→ q3 -1→ q4 -0→ q6 — ✔
2. `1201010`: q0 -1→ q0 -2→ q0 -0→ q1 -1→ q2 -0→ q3 -1→ q4 -0→ q6 — ✔
3. `01101010`: q0 -0→ q1 -1→ q2 -1→ q0 -0→ q1 -1→ q2 -0→ q3 -1→ q4 -0→ q6 — ✔
4. `1122201010`: q0 -1→ q0 -1→ q0 -2→ q0 -2→ q0 -2→ q0 -0→ q1 -1→ q2 -0→ q3 -1→ q4 -0→ q6 — ✔
5. `01022100111010`: q0 -0→ q1 -1→ q2 -0→ q3 -2→ q5 -2→ q5 -1→ q5 -0→ q3 -0→ q3 -1→ q4 -1→ q5 -1→ q5 -0→ q3 -1→ q4 -0→ q6 — ✔
6. λ: q0 — ✘
7. `02`: q0 -0→ q1 -2→ q0 — ✘
8. `2210`: q0 -2→ q0 -2→ q0 -1→ q0 -0→ q1 — ✘
9. `2010220`: q0 -2→ q0 -0→ q1 -1→ q2 -0→ q3 -2→ q5 -2→ q5 -0→ q3 — ✘
10. `12200202120`: q0 -1→ q0 -2→ q0 -2→ q0 -0→ q1 -0→ q1 -2→ q0 -0→ q1 -2→ q0 -1→ q0 -2→ q0 -0→ q1 — ✘

</details>

Simulación paso a paso en JFLAP con `01010`: [ver captura](../../evidencias/jflap/pasos/L3-AFND-p113.png).

<a id="problema-3-162-188-p-114"></a>

## Lista 3, problema 162-188 (p. 114)

**Enunciado.** AFN para el problema 114 de la Lista 2: L = {w ∈ Σ₃* : w = aⁿbᵐ, m, n ∈ ℕ}.

**Clasificación: AFND.** El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD.

#### AFND — `L3-AFND-p114`

Archivos: [`L3-AFND-p114.jff`](../../automatas/lista3-afnd/L3-AFND-p114.jff) · [`L3-AFND-p114.json`](../../automatas/lista3-afnd/L3-AFND-p114.json) · [`L3-AFND-p114.xml`](../../automatas/lista3-afnd/L3-AFND-p114.xml). Tipo según la definición: **AFND**, |Q| = 3, Σ = {a, b}, 4 transiciones.

**Diseño.** Lazo de a y lazo de b sin estado de rechazo: δ parcial.

| Estado | a | b |
|---|---|---|
| →q0 | q1 | — |
| q1 | q1 | q2 |
| *q2 | — | q2 |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `ab` | acepta | acepta | acepta |
| 2 | `aab` | acepta | acepta | acepta |
| 3 | `aaaab` | acepta | acepta | acepta |
| 4 | `abbbbbb` | acepta | acepta | acepta |
| 5 | `abbbbbbbbbb` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `ba` | rechaza | rechaza | rechaza |
| 8 | `baba` | rechaza | rechaza | rechaza |
| 9 | `bababab` | rechaza | rechaza | rechaza |
| 10 | `aaabaaaaaab` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `ab`: q0 -a→ q1 -b→ q2 — ✔
2. `aab`: q0 -a→ q1 -a→ q1 -b→ q2 — ✔
3. `aaaab`: q0 -a→ q1 -a→ q1 -a→ q1 -a→ q1 -b→ q2 — ✔
4. `abbbbbb`: q0 -a→ q1 -b→ q2 -b→ q2 -b→ q2 -b→ q2 -b→ q2 -b→ q2 — ✔
5. `abbbbbbbbbb`: q0 -a→ q1 -b→ q2 -b→ q2 -b→ q2 -b→ q2 -b→ q2 -b→ q2 -b→ q2 -b→ q2 -b→ q2 -b→ q2 — ✔
6. λ: q0 — ✘
7. `ba`: q0 -b→ (sin transición) — ✘
8. `baba`: q0 -b→ (sin transición) — ✘
9. `bababab`: q0 -b→ (sin transición) — ✘
10. `aaabaaaaaab`: q0 -a→ q1 -a→ q1 -a→ q1 -b→ q2 -a→ (sin transición) — ✘

</details>

Simulación paso a paso en JFLAP con `ab`: [ver captura](../../evidencias/jflap/pasos/L3-AFND-p114.png).

**Conversión.** AFND (3 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 3 estados, [`L3-AFND-p114-AFD.jff`](../../automatas/conversiones/L3-AFND-p114-AFD.jff) ([.json](../../automatas/conversiones/L3-AFND-p114-AFD.json), [.xml](../../automatas/conversiones/L3-AFND-p114-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 4 estados, y el AFD mínimo (Hopcroft), 4. La cota es 2^3 = 8. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-162-188-p-115"></a>

## Lista 3, problema 162-188 (p. 115)

**Enunciado.** AFN para el problema 115 de la Lista 2: L = {w ∈ Σ₂* : w = (abc)ⁿ, n ∈ ℕ}.

**Clasificación: AFND.** El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD.

#### AFND — `L3-AFND-p115`

Archivos: [`L3-AFND-p115.jff`](../../automatas/lista3-afnd/L3-AFND-p115.jff) · [`L3-AFND-p115.json`](../../automatas/lista3-afnd/L3-AFND-p115.json) · [`L3-AFND-p115.xml`](../../automatas/lista3-afnd/L3-AFND-p115.xml). Tipo según la definición: **AFND**, |Q| = 4, Σ = {a, b, c, 0, 1}, 4 transiciones.

**Diseño.** Ciclo abc sin estado de rechazo; δ parcial.

| Estado | a | b | c | 0 | 1 |
|---|---|---|---|---|---|
| →q0 | q1 | — | — | — | — |
| q1 | — | q2 | — | — | — |
| q2 | — | — | q3 | — | — |
| *q3 | q1 | — | — | — | — |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `abc` | acepta | acepta | acepta |
| 2 | `abcabc` | acepta | acepta | acepta |
| 3 | `abcabcabc` | acepta | acepta | acepta |
| 4 | `abcabcabcabc` | acepta | acepta | acepta |
| 5 | `abcabcabcabcabcabc` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `ba` | rechaza | rechaza | rechaza |
| 8 | `aca0` | rechaza | rechaza | rechaza |
| 9 | `a1000c0` | rechaza | rechaza | rechaza |
| 10 | `1b11c0bb0a1` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `abc`: q0 -a→ q1 -b→ q2 -c→ q3 — ✔
2. `abcabc`: q0 -a→ q1 -b→ q2 -c→ q3 -a→ q1 -b→ q2 -c→ q3 — ✔
3. `abcabcabc`: q0 -a→ q1 -b→ q2 -c→ q3 -a→ q1 -b→ q2 -c→ q3 -a→ q1 -b→ q2 -c→ q3 — ✔
4. `abcabcabcabc`: q0 -a→ q1 -b→ q2 -c→ q3 -a→ q1 -b→ q2 -c→ q3 -a→ q1 -b→ q2 -c→ q3 -a→ q1 -b→ q2 -c→ q3 — ✔
5. `abcabcabcabcabcabc`: q0 -a→ q1 -b→ q2 -c→ q3 -a→ q1 -b→ q2 -c→ q3 -a→ q1 -b→ q2 -c→ q3 -a→ q1 -b→ q2 -c→ q3 -a→ q1 -b→ q2 -c→ q3 -a→ q1 -b→ q2 -c→ q3 — ✔
6. λ: q0 — ✘
7. `ba`: q0 -b→ (sin transición) — ✘
8. `aca0`: q0 -a→ q1 -c→ (sin transición) — ✘
9. `a1000c0`: q0 -a→ q1 -1→ (sin transición) — ✘
10. `1b11c0bb0a1`: q0 -1→ (sin transición) — ✘

</details>

Simulación paso a paso en JFLAP con `abc`: [ver captura](../../evidencias/jflap/pasos/L3-AFND-p115.png).

**Conversión.** AFND (4 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 4 estados, [`L3-AFND-p115-AFD.jff`](../../automatas/conversiones/L3-AFND-p115-AFD.jff) ([.json](../../automatas/conversiones/L3-AFND-p115-AFD.json), [.xml](../../automatas/conversiones/L3-AFND-p115-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 5 estados, y el AFD mínimo (Hopcroft), 5. La cota es 2^4 = 16. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-162-188-p-116"></a>

## Lista 3, problema 162-188 (p. 116)

**Enunciado.** AFN para el problema 116 de la Lista 2.

**Clasificación: Ninguna.** El lenguaje del 116 no es regular: tampoco existe un AFN (ver el problema 116).

Ver la demostración en el problema 116: L no es regular.

<a id="problema-3-162-188-p-118"></a>

## Lista 3, problema 162-188 (p. 118)

**Enunciado.** AFN para el problema 118 de la Lista 2: L = {w ∈ Σ₃ : w = a x ab y a}.

**Clasificación: AFND.** El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### AFND — `L3-AFND-p118`

Archivos: [`L3-AFND-p118.jff`](../../automatas/lista3-afnd/L3-AFND-p118.jff) · [`L3-AFND-p118.json`](../../automatas/lista3-afnd/L3-AFND-p118.json) · [`L3-AFND-p118.xml`](../../automatas/lista3-afnd/L3-AFND-p118.xml). Tipo según la definición: **AFND**, |Q| = 5, Σ = {a, b}, 8 transiciones.

**Diseño.** Lee a, adivina dónde está ab y adivina la a final.

| Estado | a | b |
|---|---|---|
| →q0 | {q1} | ∅ |
| q1 | {q1, q2} | {q1} |
| q2 | ∅ | {q3} |
| q3 | {q3, q4} | {q3} |
| *q4 | ∅ | ∅ |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `aaba` | acepta | acepta | acepta |
| 2 | `aabba` | acepta | acepta | acepta |
| 3 | `ababa` | acepta | acepta | acepta |
| 4 | `aaabbaa` | acepta | acepta | acepta |
| 5 | `aaabaabbbaa` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `ab` | rechaza | rechaza | rechaza |
| 8 | `babb` | rechaza | rechaza | rechaza |
| 9 | `baabaaa` | rechaza | rechaza | rechaza |
| 10 | `bbabbbbbaba` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `aaba`: {q0} -a→ {q1} -a→ {q1, q2} -b→ {q1, q3} -a→ {q1, q2, q3, q4} — ✔
  Árbol de cómputo: 4 caminos, 1 de aceptación:
    - q0 -a→ q1 -a→ q2 -b→ q3 -a→ q4 — ✔ acepta
    - q0 -a→ q1 -a→ q1 -b→ q1 -a→ q1 — ✘ termina fuera de F
    - q0 -a→ q1 -a→ q1 -b→ q1 -a→ q2 — ✘ termina fuera de F
    - q0 -a→ q1 -a→ q2 -b→ q3 -a→ q3 — ✘ termina fuera de F
2. `aabba`: {q0} -a→ {q1} -a→ {q1, q2} -b→ {q1, q3} -b→ {q1, q3} -a→ {q1, q2, q3, q4} — ✔
  Árbol de cómputo: 4 caminos, 1 de aceptación:
    - q0 -a→ q1 -a→ q2 -b→ q3 -b→ q3 -a→ q4 — ✔ acepta
    - q0 -a→ q1 -a→ q1 -b→ q1 -b→ q1 -a→ q1 — ✘ termina fuera de F
    - q0 -a→ q1 -a→ q1 -b→ q1 -b→ q1 -a→ q2 — ✘ termina fuera de F
    - q0 -a→ q1 -a→ q2 -b→ q3 -b→ q3 -a→ q3 — ✘ termina fuera de F
3. `ababa`: {q0} -a→ {q1} -b→ {q1} -a→ {q1, q2} -b→ {q1, q3} -a→ {q1, q2, q3, q4} — ✔
  Árbol de cómputo: 4 caminos, 1 de aceptación:
    - q0 -a→ q1 -b→ q1 -a→ q2 -b→ q3 -a→ q4 — ✔ acepta
    - q0 -a→ q1 -b→ q1 -a→ q1 -b→ q1 -a→ q1 — ✘ termina fuera de F
    - q0 -a→ q1 -b→ q1 -a→ q1 -b→ q1 -a→ q2 — ✘ termina fuera de F
    - q0 -a→ q1 -b→ q1 -a→ q2 -b→ q3 -a→ q3 — ✘ termina fuera de F
4. `aaabbaa`: {q0} -a→ {q1} -a→ {q1, q2} -a→ {q1, q2} -b→ {q1, q3} -b→ {q1, q3} -a→ {q1, q2, q3, q4} -a→ {q1, q2, q3, q4} — ✔
  Árbol de cómputo: 7 caminos, 1 de aceptación (se muestran 6):
    - q0 -a→ q1 -a→ q1 -a→ q2 -b→ q3 -b→ q3 -a→ q3 -a→ q4 — ✔ acepta
    - q0 -a→ q1 -a→ q1 -a→ q1 -b→ q1 -b→ q1 -a→ q1 -a→ q1 — ✘ termina fuera de F
    - q0 -a→ q1 -a→ q1 -a→ q1 -b→ q1 -b→ q1 -a→ q1 -a→ q2 — ✘ termina fuera de F
    - q0 -a→ q1 -a→ q1 -a→ q1 -b→ q1 -b→ q1 -a→ q2 — ✘ muere tras leer `aaabba`
    - q0 -a→ q1 -a→ q1 -a→ q2 -b→ q3 -b→ q3 -a→ q3 -a→ q3 — ✘ termina fuera de F
    - q0 -a→ q1 -a→ q1 -a→ q2 -b→ q3 -b→ q3 -a→ q4 — ✘ muere tras leer `aaabba`
5. `aaabaabbbaa`: {q0} -a→ {q1} -a→ {q1, q2} -a→ {q1, q2} -b→ {q1, q3} -a→ {q1, q2, q3, q4} -a→ {q1, q2, q3, q4} -b→ {q1, q3} -b→ {q1, q3} -b→ {q1, q3} -a→ {q1, q2, q3, q4} -a→ {q1, q2, q3, q4} — ✔
  Árbol de cómputo: 13 caminos, 2 de aceptación (se muestran 6):
    - q0 -a→ q1 -a→ q1 -a→ q1 -b→ q1 -a→ q1 -a→ q2 -b→ q3 -b→ q3 -b→ q3 -a→ q3 -a→ q4 — ✔ acepta
    - q0 -a→ q1 -a→ q1 -a→ q2 -b→ q3 -a→ q3 -a→ q3 -b→ q3 -b→ q3 -b→ q3 -a→ q3 -a→ q4 — ✔ acepta
    - q0 -a→ q1 -a→ q1 -a→ q1 -b→ q1 -a→ q1 -a→ q1 -b→ q1 -b→ q1 -b→ q1 -a→ q1 -a→ q1 — ✘ termina fuera de F
    - q0 -a→ q1 -a→ q1 -a→ q1 -b→ q1 -a→ q1 -a→ q1 -b→ q1 -b→ q1 -b→ q1 -a→ q1 -a→ q2 — ✘ termina fuera de F
    - q0 -a→ q1 -a→ q1 -a→ q1 -b→ q1 -a→ q1 -a→ q1 -b→ q1 -b→ q1 -b→ q1 -a→ q2 — ✘ muere tras leer `aaabaabbba`
    - q0 -a→ q1 -a→ q1 -a→ q1 -b→ q1 -a→ q1 -a→ q2 -b→ q3 -b→ q3 -b→ q3 -a→ q3 -a→ q3 — ✘ termina fuera de F
6. λ: {q0} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
7. `ab`: {q0} -a→ {q1} -b→ {q1} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 -a→ q1 -b→ q1 — ✘ termina fuera de F
8. `babb`: {q0} -b→ ∅ -a→ ∅ -b→ ∅ -b→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ
9. `baabaaa`: {q0} -b→ ∅ -a→ ∅ -a→ ∅ -b→ ∅ -a→ ∅ -a→ ∅ -a→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ
10. `bbabbbbbaba`: {q0} -b→ ∅ -b→ ∅ -a→ ∅ -b→ ∅ -b→ ∅ -b→ ∅ -b→ ∅ -b→ ∅ -a→ ∅ -b→ ∅ -a→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ

</details>

Simulación paso a paso en JFLAP con `aaba`: [ver captura](../../evidencias/jflap/pasos/L3-AFND-p118.png).

**Conversión.** AFND (5 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 5 estados, [`L3-AFND-p118-AFD.jff`](../../automatas/conversiones/L3-AFND-p118-AFD.jff) ([.json](../../automatas/conversiones/L3-AFND-p118-AFD.json), [.xml](../../automatas/conversiones/L3-AFND-p118-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 6 estados, y el AFD mínimo (Hopcroft), 6. La cota es 2^5 = 32. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-162-188-p-119"></a>

## Lista 3, problema 162-188 (p. 119)

**Enunciado.** AFN para el problema 119 de la Lista 2: Las palabras de Σ₃ tales que después de cada subcadena aa aparece una b.

**Clasificación: AFND.** El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD.

#### AFND — `L3-AFND-p119`

Archivos: [`L3-AFND-p119.jff`](../../automatas/lista3-afnd/L3-AFND-p119.jff) · [`L3-AFND-p119.json`](../../automatas/lista3-afnd/L3-AFND-p119.json) · [`L3-AFND-p119.xml`](../../automatas/lista3-afnd/L3-AFND-p119.xml). Tipo según la definición: **AFND**, |Q| = 3, Σ = {a, b}, 5 transiciones.

**Diseño.** Los tres estados útiles del AFD; leer a con aa pendiente no tiene transición (δ parcial).

| Estado | a | b |
|---|---|---|
| →*q0 | q1 | q0 |
| *q1 | q2 | q0 |
| q2 | — | q0 |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | acepta | acepta | acepta |
| 2 | `ba` | acepta | acepta | acepta |
| 3 | `aabb` | acepta | acepta | acepta |
| 4 | `babaaba` | acepta | acepta | acepta |
| 5 | `aabababbaab` | acepta | acepta | acepta |
| 6 | `aa` | rechaza | rechaza | rechaza |
| 7 | `baa` | rechaza | rechaza | rechaza |
| 8 | `abbbaa` | rechaza | rechaza | rechaza |
| 9 | `abababaa` | rechaza | rechaza | rechaza |
| 10 | `abbabbaabbaa` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: q0 — ✔
2. `ba`: q0 -b→ q0 -a→ q1 — ✔
3. `aabb`: q0 -a→ q1 -a→ q2 -b→ q0 -b→ q0 — ✔
4. `babaaba`: q0 -b→ q0 -a→ q1 -b→ q0 -a→ q1 -a→ q2 -b→ q0 -a→ q1 — ✔
5. `aabababbaab`: q0 -a→ q1 -a→ q2 -b→ q0 -a→ q1 -b→ q0 -a→ q1 -b→ q0 -b→ q0 -a→ q1 -a→ q2 -b→ q0 — ✔
6. `aa`: q0 -a→ q1 -a→ q2 — ✘
7. `baa`: q0 -b→ q0 -a→ q1 -a→ q2 — ✘
8. `abbbaa`: q0 -a→ q1 -b→ q0 -b→ q0 -b→ q0 -a→ q1 -a→ q2 — ✘
9. `abababaa`: q0 -a→ q1 -b→ q0 -a→ q1 -b→ q0 -a→ q1 -b→ q0 -a→ q1 -a→ q2 — ✘
10. `abbabbaabbaa`: q0 -a→ q1 -b→ q0 -b→ q0 -a→ q1 -b→ q0 -b→ q0 -a→ q1 -a→ q2 -b→ q0 -b→ q0 -a→ q1 -a→ q2 — ✘

</details>

Simulación paso a paso en JFLAP con `ba`: [ver captura](../../evidencias/jflap/pasos/L3-AFND-p119.png).

**Conversión.** AFND (3 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 3 estados, [`L3-AFND-p119-AFD.jff`](../../automatas/conversiones/L3-AFND-p119-AFD.jff) ([.json](../../automatas/conversiones/L3-AFND-p119-AFD.json), [.xml](../../automatas/conversiones/L3-AFND-p119-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 4 estados, y el AFD mínimo (Hopcroft), 4. La cota es 2^3 = 8. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-162-188-p-120"></a>

## Lista 3, problema 162-188 (p. 120)

**Enunciado.** AFN para el problema 120 de la Lista 2: Palabras de Σ₁ cuyo primer y último carácter son distintos.

**Clasificación: AFND.** El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### AFND — `L3-AFND-p120`

Archivos: [`L3-AFND-p120.jff`](../../automatas/lista3-afnd/L3-AFND-p120.jff) · [`L3-AFND-p120.json`](../../automatas/lista3-afnd/L3-AFND-p120.json) · [`L3-AFND-p120.xml`](../../automatas/lista3-afnd/L3-AFND-p120.xml). Tipo según la definición: **AFND**, |Q| = 5, Σ = {0, 1, 2}, 18 transiciones.

**Diseño.** Recuerda el primer símbolo y adivina que el símbolo actual, distinto de él, es el último.

| Estado | 0 | 1 | 2 |
|---|---|---|---|
| →q0 | {q1} | {q2} | {q3} |
| q1 | {q1} | {q1, q4} | {q1, q4} |
| q2 | {q2, q4} | {q2} | {q2, q4} |
| q3 | {q3, q4} | {q3, q4} | {q3} |
| *q4 | ∅ | ∅ | ∅ |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `10` | acepta | acepta | acepta |
| 2 | `001` | acepta | acepta | acepta |
| 3 | `2011` | acepta | acepta | acepta |
| 4 | `02000001` | acepta | acepta | acepta |
| 5 | `00211200211` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `121` | rechaza | rechaza | rechaza |
| 8 | `02110` | rechaza | rechaza | rechaza |
| 9 | `0112010` | rechaza | rechaza | rechaza |
| 10 | `200020012112` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `10`: {q0} -1→ {q2} -0→ {q2, q4} — ✔
  Árbol de cómputo: 2 caminos, 1 de aceptación:
    - q0 -1→ q2 -0→ q4 — ✔ acepta
    - q0 -1→ q2 -0→ q2 — ✘ termina fuera de F
2. `001`: {q0} -0→ {q1} -0→ {q1} -1→ {q1, q4} — ✔
  Árbol de cómputo: 2 caminos, 1 de aceptación:
    - q0 -0→ q1 -0→ q1 -1→ q4 — ✔ acepta
    - q0 -0→ q1 -0→ q1 -1→ q1 — ✘ termina fuera de F
3. `2011`: {q0} -2→ {q3} -0→ {q3, q4} -1→ {q3, q4} -1→ {q3, q4} — ✔
  Árbol de cómputo: 4 caminos, 1 de aceptación:
    - q0 -2→ q3 -0→ q3 -1→ q3 -1→ q4 — ✔ acepta
    - q0 -2→ q3 -0→ q3 -1→ q3 -1→ q3 — ✘ termina fuera de F
    - q0 -2→ q3 -0→ q3 -1→ q4 — ✘ muere tras leer `201`
    - q0 -2→ q3 -0→ q4 — ✘ muere tras leer `20`
4. `02000001`: {q0} -0→ {q1} -2→ {q1, q4} -0→ {q1} -0→ {q1} -0→ {q1} -0→ {q1} -0→ {q1} -1→ {q1, q4} — ✔
  Árbol de cómputo: 3 caminos, 1 de aceptación:
    - q0 -0→ q1 -2→ q1 -0→ q1 -0→ q1 -0→ q1 -0→ q1 -0→ q1 -1→ q4 — ✔ acepta
    - q0 -0→ q1 -2→ q1 -0→ q1 -0→ q1 -0→ q1 -0→ q1 -0→ q1 -1→ q1 — ✘ termina fuera de F
    - q0 -0→ q1 -2→ q4 — ✘ muere tras leer `02`
5. `00211200211`: {q0} -0→ {q1} -0→ {q1} -2→ {q1, q4} -1→ {q1, q4} -1→ {q1, q4} -2→ {q1, q4} -0→ {q1} -0→ {q1} -2→ {q1, q4} -1→ {q1, q4} -1→ {q1, q4} — ✔
  Árbol de cómputo: 8 caminos, 1 de aceptación (se muestran 6):
    - q0 -0→ q1 -0→ q1 -2→ q1 -1→ q1 -1→ q1 -2→ q1 -0→ q1 -0→ q1 -2→ q1 -1→ q1 -1→ q4 — ✔ acepta
    - q0 -0→ q1 -0→ q1 -2→ q1 -1→ q1 -1→ q1 -2→ q1 -0→ q1 -0→ q1 -2→ q1 -1→ q1 -1→ q1 — ✘ termina fuera de F
    - q0 -0→ q1 -0→ q1 -2→ q1 -1→ q1 -1→ q1 -2→ q1 -0→ q1 -0→ q1 -2→ q1 -1→ q4 — ✘ muere tras leer `0021120021`
    - q0 -0→ q1 -0→ q1 -2→ q1 -1→ q1 -1→ q1 -2→ q1 -0→ q1 -0→ q1 -2→ q4 — ✘ muere tras leer `002112002`
    - q0 -0→ q1 -0→ q1 -2→ q1 -1→ q1 -1→ q1 -2→ q4 — ✘ muere tras leer `002112`
    - q0 -0→ q1 -0→ q1 -2→ q1 -1→ q1 -1→ q4 — ✘ muere tras leer `00211`
6. λ: {q0} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
7. `121`: {q0} -1→ {q2} -2→ {q2, q4} -1→ {q2} — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -1→ q2 -2→ q2 -1→ q2 — ✘ termina fuera de F
    - q0 -1→ q2 -2→ q4 — ✘ muere tras leer `12`
8. `02110`: {q0} -0→ {q1} -2→ {q1, q4} -1→ {q1, q4} -1→ {q1, q4} -0→ {q1} — ✘
  Árbol de cómputo: 4 caminos, 0 de aceptación:
    - q0 -0→ q1 -2→ q1 -1→ q1 -1→ q1 -0→ q1 — ✘ termina fuera de F
    - q0 -0→ q1 -2→ q1 -1→ q1 -1→ q4 — ✘ muere tras leer `0211`
    - q0 -0→ q1 -2→ q1 -1→ q4 — ✘ muere tras leer `021`
    - q0 -0→ q1 -2→ q4 — ✘ muere tras leer `02`
9. `0112010`: {q0} -0→ {q1} -1→ {q1, q4} -1→ {q1, q4} -2→ {q1, q4} -0→ {q1} -1→ {q1, q4} -0→ {q1} — ✘
  Árbol de cómputo: 5 caminos, 0 de aceptación:
    - q0 -0→ q1 -1→ q1 -1→ q1 -2→ q1 -0→ q1 -1→ q1 -0→ q1 — ✘ termina fuera de F
    - q0 -0→ q1 -1→ q1 -1→ q1 -2→ q1 -0→ q1 -1→ q4 — ✘ muere tras leer `011201`
    - q0 -0→ q1 -1→ q1 -1→ q1 -2→ q4 — ✘ muere tras leer `0112`
    - q0 -0→ q1 -1→ q1 -1→ q4 — ✘ muere tras leer `011`
    - q0 -0→ q1 -1→ q4 — ✘ muere tras leer `01`
10. `200020012112`: {q0} -2→ {q3} -0→ {q3, q4} -0→ {q3, q4} -0→ {q3, q4} -2→ {q3} -0→ {q3, q4} -0→ {q3, q4} -1→ {q3, q4} -2→ {q3} -1→ {q3, q4} -1→ {q3, q4} -2→ {q3} — ✘
  Árbol de cómputo: 9 caminos, 0 de aceptación (se muestran 6):
    - q0 -2→ q3 -0→ q3 -0→ q3 -0→ q3 -2→ q3 -0→ q3 -0→ q3 -1→ q3 -2→ q3 -1→ q3 -1→ q3 -2→ q3 — ✘ termina fuera de F
    - q0 -2→ q3 -0→ q3 -0→ q3 -0→ q3 -2→ q3 -0→ q3 -0→ q3 -1→ q3 -2→ q3 -1→ q3 -1→ q4 — ✘ muere tras leer `20002001211`
    - q0 -2→ q3 -0→ q3 -0→ q3 -0→ q3 -2→ q3 -0→ q3 -0→ q3 -1→ q3 -2→ q3 -1→ q4 — ✘ muere tras leer `2000200121`
    - q0 -2→ q3 -0→ q3 -0→ q3 -0→ q3 -2→ q3 -0→ q3 -0→ q3 -1→ q4 — ✘ muere tras leer `20002001`
    - q0 -2→ q3 -0→ q3 -0→ q3 -0→ q3 -2→ q3 -0→ q3 -0→ q4 — ✘ muere tras leer `2000200`
    - q0 -2→ q3 -0→ q3 -0→ q3 -0→ q3 -2→ q3 -0→ q4 — ✘ muere tras leer `200020`

</details>

Simulación paso a paso en JFLAP con `10`: [ver captura](../../evidencias/jflap/pasos/L3-AFND-p120.png).

**Conversión.** AFND (5 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 7 estados, [`L3-AFND-p120-AFD.jff`](../../automatas/conversiones/L3-AFND-p120-AFD.jff) ([.json](../../automatas/conversiones/L3-AFND-p120-AFD.json), [.xml](../../automatas/conversiones/L3-AFND-p120-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 7 estados, y el AFD mínimo (Hopcroft), 7. La cota es 2^5 = 32. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-162-188-p-121"></a>

## Lista 3, problema 162-188 (p. 121)

**Enunciado.** AFN para el problema 121 de la Lista 2: Palabras de Σ₁ de longitud 3n, tales que cada bloque de 3 tiene al menos un 0 (se toma n ≥ 1).

**Clasificación: AFND.** El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### AFND — `L3-AFND-p121`

Archivos: [`L3-AFND-p121.jff`](../../automatas/lista3-afnd/L3-AFND-p121.jff) · [`L3-AFND-p121.json`](../../automatas/lista3-afnd/L3-AFND-p121.json) · [`L3-AFND-p121.xml`](../../automatas/lista3-afnd/L3-AFND-p121.xml). Tipo según la definición: **AFND**, |Q| = 7, Σ = {0, 1, 2}, 25 transiciones.

**Diseño.** Adivina en cada bloque en qué posición está su 0.

| Estado | 0 | 1 | 2 |
|---|---|---|---|
| →q0 | {q2, q4, q5} | {q4, q5} | {q4, q5} |
| *q1 | {q2, q4, q5} | {q4, q5} | {q4, q5} |
| q2 | {q3} | {q3} | {q3} |
| q3 | {q1} | {q1} | {q1} |
| q4 | {q3} | ∅ | ∅ |
| q5 | {q6} | {q6} | {q6} |
| q6 | {q1} | ∅ | ∅ |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `000` | acepta | acepta | acepta |
| 2 | `210` | acepta | acepta | acepta |
| 3 | `200100` | acepta | acepta | acepta |
| 4 | `220101000` | acepta | acepta | acepta |
| 5 | `002110120110` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `20` | rechaza | rechaza | rechaza |
| 8 | `2021` | rechaza | rechaza | rechaza |
| 9 | `2101201` | rechaza | rechaza | rechaza |
| 10 | `22021222221` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `000`: {q0} -0→ {q2, q4, q5} -0→ {q3, q6} -0→ {q1} — ✔
  Árbol de cómputo: 3 caminos, 3 de aceptación:
    - q0 -0→ q2 -0→ q3 -0→ q1 — ✔ acepta
    - q0 -0→ q4 -0→ q3 -0→ q1 — ✔ acepta
    - q0 -0→ q5 -0→ q6 -0→ q1 — ✔ acepta
2. `210`: {q0} -2→ {q4, q5} -1→ {q6} -0→ {q1} — ✔
  Árbol de cómputo: 2 caminos, 1 de aceptación:
    - q0 -2→ q5 -1→ q6 -0→ q1 — ✔ acepta
    - q0 -2→ q4 — ✘ muere tras leer `2`
3. `200100`: {q0} -2→ {q4, q5} -0→ {q3, q6} -0→ {q1} -1→ {q4, q5} -0→ {q3, q6} -0→ {q1} — ✔
  Árbol de cómputo: 4 caminos, 4 de aceptación (se muestran 3):
    - q0 -2→ q4 -0→ q3 -0→ q1 -1→ q4 -0→ q3 -0→ q1 — ✔ acepta
    - q0 -2→ q4 -0→ q3 -0→ q1 -1→ q5 -0→ q6 -0→ q1 — ✔ acepta
    - q0 -2→ q5 -0→ q6 -0→ q1 -1→ q4 -0→ q3 -0→ q1 — ✔ acepta
4. `220101000`: {q0} -2→ {q4, q5} -2→ {q6} -0→ {q1} -1→ {q4, q5} -0→ {q3, q6} -1→ {q1} -0→ {q2, q4, q5} -0→ {q3, q6} -0→ {q1} — ✔
  Árbol de cómputo: 5 caminos, 3 de aceptación:
    - q0 -2→ q5 -2→ q6 -0→ q1 -1→ q4 -0→ q3 -1→ q1 -0→ q2 -0→ q3 -0→ q1 — ✔ acepta
    - q0 -2→ q5 -2→ q6 -0→ q1 -1→ q4 -0→ q3 -1→ q1 -0→ q4 -0→ q3 -0→ q1 — ✔ acepta
    - q0 -2→ q5 -2→ q6 -0→ q1 -1→ q4 -0→ q3 -1→ q1 -0→ q5 -0→ q6 -0→ q1 — ✔ acepta
    - q0 -2→ q4 — ✘ muere tras leer `2`
    - q0 -2→ q5 -2→ q6 -0→ q1 -1→ q5 -0→ q6 — ✘ muere tras leer `22010`
5. `002110120110`: {q0} -0→ {q2, q4, q5} -0→ {q3, q6} -2→ {q1} -1→ {q4, q5} -1→ {q6} -0→ {q1} -1→ {q4, q5} -2→ {q6} -0→ {q1} -1→ {q4, q5} -1→ {q6} -0→ {q1} — ✔
  Árbol de cómputo: 9 caminos, 2 de aceptación (se muestran 6):
    - q0 -0→ q2 -0→ q3 -2→ q1 -1→ q5 -1→ q6 -0→ q1 -1→ q5 -2→ q6 -0→ q1 -1→ q5 -1→ q6 -0→ q1 — ✔ acepta
    - q0 -0→ q4 -0→ q3 -2→ q1 -1→ q5 -1→ q6 -0→ q1 -1→ q5 -2→ q6 -0→ q1 -1→ q5 -1→ q6 -0→ q1 — ✔ acepta
    - q0 -0→ q2 -0→ q3 -2→ q1 -1→ q4 — ✘ muere tras leer `0021`
    - q0 -0→ q2 -0→ q3 -2→ q1 -1→ q5 -1→ q6 -0→ q1 -1→ q4 — ✘ muere tras leer `0021101`
    - q0 -0→ q2 -0→ q3 -2→ q1 -1→ q5 -1→ q6 -0→ q1 -1→ q5 -2→ q6 -0→ q1 -1→ q4 — ✘ muere tras leer `0021101201`
    - q0 -0→ q4 -0→ q3 -2→ q1 -1→ q4 — ✘ muere tras leer `0021`
6. λ: {q0} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
7. `20`: {q0} -2→ {q4, q5} -0→ {q3, q6} — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -2→ q4 -0→ q3 — ✘ termina fuera de F
    - q0 -2→ q5 -0→ q6 — ✘ termina fuera de F
8. `2021`: {q0} -2→ {q4, q5} -0→ {q3, q6} -2→ {q1} -1→ {q4, q5} — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - q0 -2→ q4 -0→ q3 -2→ q1 -1→ q4 — ✘ termina fuera de F
    - q0 -2→ q4 -0→ q3 -2→ q1 -1→ q5 — ✘ termina fuera de F
    - q0 -2→ q5 -0→ q6 — ✘ muere tras leer `20`
9. `2101201`: {q0} -2→ {q4, q5} -1→ {q6} -0→ {q1} -1→ {q4, q5} -2→ {q6} -0→ {q1} -1→ {q4, q5} — ✘
  Árbol de cómputo: 4 caminos, 0 de aceptación:
    - q0 -2→ q4 — ✘ muere tras leer `2`
    - q0 -2→ q5 -1→ q6 -0→ q1 -1→ q4 — ✘ muere tras leer `2101`
    - q0 -2→ q5 -1→ q6 -0→ q1 -1→ q5 -2→ q6 -0→ q1 -1→ q4 — ✘ termina fuera de F
    - q0 -2→ q5 -1→ q6 -0→ q1 -1→ q5 -2→ q6 -0→ q1 -1→ q5 — ✘ termina fuera de F
10. `22021222221`: {q0} -2→ {q4, q5} -2→ {q6} -0→ {q1} -2→ {q4, q5} -1→ {q6} -2→ ∅ -2→ ∅ -2→ ∅ -2→ ∅ -2→ ∅ -1→ ∅ — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - q0 -2→ q4 — ✘ muere tras leer `2`
    - q0 -2→ q5 -2→ q6 -0→ q1 -2→ q4 — ✘ muere tras leer `2202`
    - q0 -2→ q5 -2→ q6 -0→ q1 -2→ q5 -1→ q6 — ✘ muere tras leer `22021`

</details>

Simulación paso a paso en JFLAP con `000`: [ver captura](../../evidencias/jflap/pasos/L3-AFND-p121.png).

**Conversión.** AFND (7 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 6 estados, [`L3-AFND-p121-AFD.jff`](../../automatas/conversiones/L3-AFND-p121-AFD.jff) ([.json](../../automatas/conversiones/L3-AFND-p121-AFD.json), [.xml](../../automatas/conversiones/L3-AFND-p121-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 7 estados, y el AFD mínimo (Hopcroft), 7. La cota es 2^7 = 128. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-162-188-p-122"></a>

## Lista 3, problema 162-188 (p. 122)

**Enunciado.** AFN para el problema 122 de la Lista 2: Palabras de Σ₁ en las que toda terna de símbolos consecutivos tiene un 0.

**Clasificación: AFND.** El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### AFND — `L3-AFND-p122`

Archivos: [`L3-AFND-p122.jff`](../../automatas/lista3-afnd/L3-AFND-p122.jff) · [`L3-AFND-p122.json`](../../automatas/lista3-afnd/L3-AFND-p122.json) · [`L3-AFND-p122.xml`](../../automatas/lista3-afnd/L3-AFND-p122.xml). Tipo según la definición: **AFND**, |Q| = 3, Σ = {0, 1, 2}, 7 transiciones.

**Diseño.** Solo los estados útiles de la racha; la transición indefinida reemplaza al estado de rechazo.

| Estado | 0 | 1 | 2 |
|---|---|---|---|
| →*q0 | q0 | q1 | q1 |
| *q1 | q0 | q2 | q2 |
| *q2 | q0 | — | — |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | acepta | acepta | acepta |
| 2 | `21` | acepta | acepta | acepta |
| 3 | `0220` | acepta | acepta | acepta |
| 4 | `0100110` | acepta | acepta | acepta |
| 5 | `12020210210` | acepta | acepta | acepta |
| 6 | `111` | rechaza | rechaza | rechaza |
| 7 | `0111` | rechaza | rechaza | rechaza |
| 8 | `1110` | rechaza | rechaza | rechaza |
| 9 | `1110010` | rechaza | rechaza | rechaza |
| 10 | `00210202112` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: q0 — ✔
2. `21`: q0 -2→ q1 -1→ q2 — ✔
3. `0220`: q0 -0→ q0 -2→ q1 -2→ q2 -0→ q0 — ✔
4. `0100110`: q0 -0→ q0 -1→ q1 -0→ q0 -0→ q0 -1→ q1 -1→ q2 -0→ q0 — ✔
5. `12020210210`: q0 -1→ q1 -2→ q2 -0→ q0 -2→ q1 -0→ q0 -2→ q1 -1→ q2 -0→ q0 -2→ q1 -1→ q2 -0→ q0 — ✔
6. `111`: q0 -1→ q1 -1→ q2 -1→ (sin transición) — ✘
7. `0111`: q0 -0→ q0 -1→ q1 -1→ q2 -1→ (sin transición) — ✘
8. `1110`: q0 -1→ q1 -1→ q2 -1→ (sin transición) — ✘
9. `1110010`: q0 -1→ q1 -1→ q2 -1→ (sin transición) — ✘
10. `00210202112`: q0 -0→ q0 -0→ q0 -2→ q1 -1→ q2 -0→ q0 -2→ q1 -0→ q0 -2→ q1 -1→ q2 -1→ (sin transición) — ✘

</details>

Simulación paso a paso en JFLAP con `21`: [ver captura](../../evidencias/jflap/pasos/L3-AFND-p122.png).

**Conversión.** AFND (3 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 3 estados, [`L3-AFND-p122-AFD.jff`](../../automatas/conversiones/L3-AFND-p122-AFD.jff) ([.json](../../automatas/conversiones/L3-AFND-p122-AFD.json), [.xml](../../automatas/conversiones/L3-AFND-p122-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 4 estados, y el AFD mínimo (Hopcroft), 4. La cota es 2^3 = 8. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-162-188-p-123"></a>

## Lista 3, problema 162-188 (p. 123)

**Enunciado.** AFN para el problema 123 de la Lista 2: Palabras de Σ₃ de la forma w x w, con w ∈ Σ₃² y x ∈ Σ₃*.

**Clasificación: AFND.** El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### AFND — `L3-AFND-p123`

Archivos: [`L3-AFND-p123.jff`](../../automatas/lista3-afnd/L3-AFND-p123.jff) · [`L3-AFND-p123.json`](../../automatas/lista3-afnd/L3-AFND-p123.json) · [`L3-AFND-p123.xml`](../../automatas/lista3-afnd/L3-AFND-p123.xml). Tipo según la definición: **AFND**, |Q| = 12, Σ = {a, b}, 22 transiciones.

**Diseño.** Recuerda w, adivina dónde comienza su segunda copia al final.

| Estado | a | b |
|---|---|---|
| →q0 | {q1} | {q2} |
| q1 | {q3} | {q4} |
| q2 | {q5} | {q6} |
| q3 | {q3, q7} | {q3} |
| q4 | {q4, q8} | {q4} |
| q5 | {q5} | {q5, q9} |
| q6 | {q6} | {q10, q6} |
| q7 | {q11} | ∅ |
| q8 | ∅ | {q11} |
| q9 | {q11} | ∅ |
| q10 | ∅ | {q11} |
| *q11 | ∅ | ∅ |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `abab` | acepta | acepta | acepta |
| 2 | `bbbb` | acepta | acepta | — |
| 3 | `bbabb` | acepta | acepta | acepta |
| 4 | `abbabbab` | acepta | acepta | acepta |
| 5 | `aaaaabaaaabaa` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `aa` | rechaza | rechaza | rechaza |
| 8 | `bbaa` | rechaza | rechaza | rechaza |
| 9 | `bbbaabba` | rechaza | rechaza | rechaza |
| 10 | `bbabbaaaaba` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `abab`: {q0} -a→ {q1} -b→ {q4} -a→ {q4, q8} -b→ {q11, q4} — ✔
  Árbol de cómputo: 2 caminos, 1 de aceptación:
    - q0 -a→ q1 -b→ q4 -a→ q8 -b→ q11 — ✔ acepta
    - q0 -a→ q1 -b→ q4 -a→ q4 -b→ q4 — ✘ termina fuera de F
2. `bbbb`: {q0} -b→ {q2} -b→ {q6} -b→ {q10, q6} -b→ {q10, q11, q6} — ✔
  Árbol de cómputo: 3 caminos, 1 de aceptación:
    - q0 -b→ q2 -b→ q6 -b→ q10 -b→ q11 — ✔ acepta
    - q0 -b→ q2 -b→ q6 -b→ q6 -b→ q10 — ✘ termina fuera de F
    - q0 -b→ q2 -b→ q6 -b→ q6 -b→ q6 — ✘ termina fuera de F
3. `bbabb`: {q0} -b→ {q2} -b→ {q6} -a→ {q6} -b→ {q10, q6} -b→ {q10, q11, q6} — ✔
  Árbol de cómputo: 3 caminos, 1 de aceptación:
    - q0 -b→ q2 -b→ q6 -a→ q6 -b→ q10 -b→ q11 — ✔ acepta
    - q0 -b→ q2 -b→ q6 -a→ q6 -b→ q6 -b→ q10 — ✘ termina fuera de F
    - q0 -b→ q2 -b→ q6 -a→ q6 -b→ q6 -b→ q6 — ✘ termina fuera de F
4. `abbabbab`: {q0} -a→ {q1} -b→ {q4} -b→ {q4} -a→ {q4, q8} -b→ {q11, q4} -b→ {q4} -a→ {q4, q8} -b→ {q11, q4} — ✔
  Árbol de cómputo: 3 caminos, 1 de aceptación:
    - q0 -a→ q1 -b→ q4 -b→ q4 -a→ q4 -b→ q4 -b→ q4 -a→ q8 -b→ q11 — ✔ acepta
    - q0 -a→ q1 -b→ q4 -b→ q4 -a→ q4 -b→ q4 -b→ q4 -a→ q4 -b→ q4 — ✘ termina fuera de F
    - q0 -a→ q1 -b→ q4 -b→ q4 -a→ q8 -b→ q11 — ✘ muere tras leer `abbab`
5. `aaaaabaaaabaa`: {q0} -a→ {q1} -a→ {q3} -a→ {q3, q7} -a→ {q11, q3, q7} -a→ {q11, q3, q7} -b→ {q3} -a→ {q3, q7} -a→ {q11, q3, q7} -a→ {q11, q3, q7} -a→ {q11, q3, q7} -b→ {q3} -a→ {q3, q7} -a→ {q11, q3, q7} — ✔
  Árbol de cómputo: 10 caminos, 1 de aceptación (se muestran 6):
    - q0 -a→ q1 -a→ q3 -a→ q3 -a→ q3 -a→ q3 -b→ q3 -a→ q3 -a→ q3 -a→ q3 -a→ q3 -b→ q3 -a→ q7 -a→ q11 — ✔ acepta
    - q0 -a→ q1 -a→ q3 -a→ q3 -a→ q3 -a→ q3 -b→ q3 -a→ q3 -a→ q3 -a→ q3 -a→ q3 -b→ q3 -a→ q3 -a→ q3 — ✘ termina fuera de F
    - q0 -a→ q1 -a→ q3 -a→ q3 -a→ q3 -a→ q3 -b→ q3 -a→ q3 -a→ q3 -a→ q3 -a→ q3 -b→ q3 -a→ q3 -a→ q7 — ✘ termina fuera de F
    - q0 -a→ q1 -a→ q3 -a→ q3 -a→ q3 -a→ q3 -b→ q3 -a→ q3 -a→ q3 -a→ q3 -a→ q7 — ✘ muere tras leer `aaaaabaaaa`
    - q0 -a→ q1 -a→ q3 -a→ q3 -a→ q3 -a→ q3 -b→ q3 -a→ q3 -a→ q3 -a→ q7 -a→ q11 — ✘ muere tras leer `aaaaabaaaa`
    - q0 -a→ q1 -a→ q3 -a→ q3 -a→ q3 -a→ q3 -b→ q3 -a→ q3 -a→ q7 -a→ q11 — ✘ muere tras leer `aaaaabaaa`
6. λ: {q0} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
7. `aa`: {q0} -a→ {q1} -a→ {q3} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 -a→ q1 -a→ q3 — ✘ termina fuera de F
8. `bbaa`: {q0} -b→ {q2} -b→ {q6} -a→ {q6} -a→ {q6} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 -b→ q2 -b→ q6 -a→ q6 -a→ q6 — ✘ termina fuera de F
9. `bbbaabba`: {q0} -b→ {q2} -b→ {q6} -b→ {q10, q6} -a→ {q6} -a→ {q6} -b→ {q10, q6} -b→ {q10, q11, q6} -a→ {q6} — ✘
  Árbol de cómputo: 4 caminos, 0 de aceptación:
    - q0 -b→ q2 -b→ q6 -b→ q10 — ✘ muere tras leer `bbb`
    - q0 -b→ q2 -b→ q6 -b→ q6 -a→ q6 -a→ q6 -b→ q10 -b→ q11 — ✘ muere tras leer `bbbaabb`
    - q0 -b→ q2 -b→ q6 -b→ q6 -a→ q6 -a→ q6 -b→ q6 -b→ q10 — ✘ muere tras leer `bbbaabb`
    - q0 -b→ q2 -b→ q6 -b→ q6 -a→ q6 -a→ q6 -b→ q6 -b→ q6 -a→ q6 — ✘ termina fuera de F
10. `bbabbaaaaba`: {q0} -b→ {q2} -b→ {q6} -a→ {q6} -b→ {q10, q6} -b→ {q10, q11, q6} -a→ {q6} -a→ {q6} -a→ {q6} -a→ {q6} -b→ {q10, q6} -a→ {q6} — ✘
  Árbol de cómputo: 4 caminos, 0 de aceptación:
    - q0 -b→ q2 -b→ q6 -a→ q6 -b→ q10 -b→ q11 — ✘ muere tras leer `bbabb`
    - q0 -b→ q2 -b→ q6 -a→ q6 -b→ q6 -b→ q10 — ✘ muere tras leer `bbabb`
    - q0 -b→ q2 -b→ q6 -a→ q6 -b→ q6 -b→ q6 -a→ q6 -a→ q6 -a→ q6 -a→ q6 -b→ q10 — ✘ muere tras leer `bbabbaaaab`
    - q0 -b→ q2 -b→ q6 -a→ q6 -b→ q6 -b→ q6 -a→ q6 -a→ q6 -a→ q6 -a→ q6 -b→ q6 -a→ q6 — ✘ termina fuera de F

</details>

Simulación paso a paso en JFLAP con `abab`: [ver captura](../../evidencias/jflap/pasos/L3-AFND-p123.png).

**Conversión.** AFND (12 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 15 estados, [`L3-AFND-p123-AFD.jff`](../../automatas/conversiones/L3-AFND-p123-AFD.jff) ([.json](../../automatas/conversiones/L3-AFND-p123-AFD.json), [.xml](../../automatas/conversiones/L3-AFND-p123-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 15 estados, y el AFD mínimo (Hopcroft), 15. La cota es 2^12 = 4096. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-162-188-p-94"></a>

## Lista 3, problema 162-188 (p. 94)

**Enunciado.** AFN para el problema 94 de la Lista 2: Las palabras de Σ₁ = {0,1,2} que comienzan con 1 y terminan con 2.

**Clasificación: AFND.** El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD.

#### AFND — `L3-AFND-p094`

Archivos: [`L3-AFND-p094.jff`](../../automatas/lista3-afnd/L3-AFND-p094.jff) · [`L3-AFND-p094.json`](../../automatas/lista3-afnd/L3-AFND-p094.json) · [`L3-AFND-p094.xml`](../../automatas/lista3-afnd/L3-AFND-p094.xml). Tipo según la definición: **AFND**, |Q| = 3, Σ = {0, 1, 2}, 5 transiciones.

**Diseño.** q0 lee el 1 inicial; q1 consume cualquier símbolo y adivina cuál es el 2 final, que lleva a q2 sin salidas.

| Estado | 0 | 1 | 2 |
|---|---|---|---|
| →q0 | ∅ | {q1} | ∅ |
| q1 | {q1} | {q1} | {q1, q2} |
| *q2 | ∅ | ∅ | ∅ |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `12` | acepta | acepta | acepta |
| 2 | `112` | acepta | acepta | acepta |
| 3 | `10102` | acepta | acepta | acepta |
| 4 | `10210002` | acepta | acepta | acepta |
| 5 | `12102121022` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `22` | rechaza | rechaza | rechaza |
| 8 | `0222` | rechaza | rechaza | rechaza |
| 9 | `1012120` | rechaza | rechaza | rechaza |
| 10 | `02100012010` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `12`: {q0} -1→ {q1} -2→ {q1, q2} — ✔
  Árbol de cómputo: 2 caminos, 1 de aceptación:
    - q0 -1→ q1 -2→ q2 — ✔ acepta
    - q0 -1→ q1 -2→ q1 — ✘ termina fuera de F
2. `112`: {q0} -1→ {q1} -1→ {q1} -2→ {q1, q2} — ✔
  Árbol de cómputo: 2 caminos, 1 de aceptación:
    - q0 -1→ q1 -1→ q1 -2→ q2 — ✔ acepta
    - q0 -1→ q1 -1→ q1 -2→ q1 — ✘ termina fuera de F
3. `10102`: {q0} -1→ {q1} -0→ {q1} -1→ {q1} -0→ {q1} -2→ {q1, q2} — ✔
  Árbol de cómputo: 2 caminos, 1 de aceptación:
    - q0 -1→ q1 -0→ q1 -1→ q1 -0→ q1 -2→ q2 — ✔ acepta
    - q0 -1→ q1 -0→ q1 -1→ q1 -0→ q1 -2→ q1 — ✘ termina fuera de F
4. `10210002`: {q0} -1→ {q1} -0→ {q1} -2→ {q1, q2} -1→ {q1} -0→ {q1} -0→ {q1} -0→ {q1} -2→ {q1, q2} — ✔
  Árbol de cómputo: 3 caminos, 1 de aceptación:
    - q0 -1→ q1 -0→ q1 -2→ q1 -1→ q1 -0→ q1 -0→ q1 -0→ q1 -2→ q2 — ✔ acepta
    - q0 -1→ q1 -0→ q1 -2→ q1 -1→ q1 -0→ q1 -0→ q1 -0→ q1 -2→ q1 — ✘ termina fuera de F
    - q0 -1→ q1 -0→ q1 -2→ q2 — ✘ muere tras leer `102`
5. `12102121022`: {q0} -1→ {q1} -2→ {q1, q2} -1→ {q1} -0→ {q1} -2→ {q1, q2} -1→ {q1} -2→ {q1, q2} -1→ {q1} -0→ {q1} -2→ {q1, q2} -2→ {q1, q2} — ✔
  Árbol de cómputo: 6 caminos, 1 de aceptación:
    - q0 -1→ q1 -2→ q1 -1→ q1 -0→ q1 -2→ q1 -1→ q1 -2→ q1 -1→ q1 -0→ q1 -2→ q1 -2→ q2 — ✔ acepta
    - q0 -1→ q1 -2→ q1 -1→ q1 -0→ q1 -2→ q1 -1→ q1 -2→ q1 -1→ q1 -0→ q1 -2→ q1 -2→ q1 — ✘ termina fuera de F
    - q0 -1→ q1 -2→ q1 -1→ q1 -0→ q1 -2→ q1 -1→ q1 -2→ q1 -1→ q1 -0→ q1 -2→ q2 — ✘ muere tras leer `1210212102`
    - q0 -1→ q1 -2→ q1 -1→ q1 -0→ q1 -2→ q1 -1→ q1 -2→ q2 — ✘ muere tras leer `1210212`
    - q0 -1→ q1 -2→ q1 -1→ q1 -0→ q1 -2→ q2 — ✘ muere tras leer `12102`
    - q0 -1→ q1 -2→ q2 — ✘ muere tras leer `12`
6. λ: {q0} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
7. `22`: {q0} -2→ ∅ -2→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ
8. `0222`: {q0} -0→ ∅ -2→ ∅ -2→ ∅ -2→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ
9. `1012120`: {q0} -1→ {q1} -0→ {q1} -1→ {q1} -2→ {q1, q2} -1→ {q1} -2→ {q1, q2} -0→ {q1} — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - q0 -1→ q1 -0→ q1 -1→ q1 -2→ q1 -1→ q1 -2→ q1 -0→ q1 — ✘ termina fuera de F
    - q0 -1→ q1 -0→ q1 -1→ q1 -2→ q1 -1→ q1 -2→ q2 — ✘ muere tras leer `101212`
    - q0 -1→ q1 -0→ q1 -1→ q1 -2→ q2 — ✘ muere tras leer `1012`
10. `02100012010`: {q0} -0→ ∅ -2→ ∅ -1→ ∅ -0→ ∅ -0→ ∅ -0→ ∅ -1→ ∅ -2→ ∅ -0→ ∅ -1→ ∅ -0→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ

</details>

Simulación paso a paso en JFLAP con `12`: [ver captura](../../evidencias/jflap/pasos/L3-AFND-p094.png).

**Conversión.** AFND (3 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 3 estados, [`L3-AFND-p094-AFD.jff`](../../automatas/conversiones/L3-AFND-p094-AFD.jff) ([.json](../../automatas/conversiones/L3-AFND-p094-AFD.json), [.xml](../../automatas/conversiones/L3-AFND-p094-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 4 estados, y el AFD mínimo (Hopcroft), 4. La cota es 2^3 = 8. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-162-188-p-95"></a>

## Lista 3, problema 162-188 (p. 95)

**Enunciado.** AFN para el problema 95 de la Lista 2: Las palabras de Σ₁ que tienen longitud 4.

**Clasificación: AFND.** El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD.

#### AFND — `L3-AFND-p095`

Archivos: [`L3-AFND-p095.jff`](../../automatas/lista3-afnd/L3-AFND-p095.jff) · [`L3-AFND-p095.json`](../../automatas/lista3-afnd/L3-AFND-p095.json) · [`L3-AFND-p095.xml`](../../automatas/lista3-afnd/L3-AFND-p095.xml). Tipo según la definición: **AFND**, |Q| = 5, Σ = {0, 1, 2}, 12 transiciones.

**Diseño.** Cadena de cuatro transiciones con cualquier símbolo; sin estado de rechazo (δ parcial): una quinta letra no tiene transición y el cómputo muere.

| Estado | 0 | 1 | 2 |
|---|---|---|---|
| →q0 | q1 | q1 | q1 |
| q1 | q2 | q2 | q2 |
| q2 | q3 | q3 | q3 |
| q3 | q4 | q4 | q4 |
| *q4 | — | — | — |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `0000` | acepta | acepta | acepta |
| 2 | `0021` | acepta | acepta | acepta |
| 3 | `1000` | acepta | acepta | acepta |
| 4 | `1120` | acepta | acepta | acepta |
| 5 | `1220` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `01` | rechaza | rechaza | rechaza |
| 8 | `21120` | rechaza | rechaza | rechaza |
| 9 | `0122210` | rechaza | rechaza | rechaza |
| 10 | `20202120022` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `0000`: q0 -0→ q1 -0→ q2 -0→ q3 -0→ q4 — ✔
2. `0021`: q0 -0→ q1 -0→ q2 -2→ q3 -1→ q4 — ✔
3. `1000`: q0 -1→ q1 -0→ q2 -0→ q3 -0→ q4 — ✔
4. `1120`: q0 -1→ q1 -1→ q2 -2→ q3 -0→ q4 — ✔
5. `1220`: q0 -1→ q1 -2→ q2 -2→ q3 -0→ q4 — ✔
6. λ: q0 — ✘
7. `01`: q0 -0→ q1 -1→ q2 — ✘
8. `21120`: q0 -2→ q1 -1→ q2 -1→ q3 -2→ q4 -0→ (sin transición) — ✘
9. `0122210`: q0 -0→ q1 -1→ q2 -2→ q3 -2→ q4 -2→ (sin transición) — ✘
10. `20202120022`: q0 -2→ q1 -0→ q2 -2→ q3 -0→ q4 -2→ (sin transición) — ✘

</details>

Simulación paso a paso en JFLAP con `0000`: [ver captura](../../evidencias/jflap/pasos/L3-AFND-p095.png).

**Conversión.** AFND (5 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 5 estados, [`L3-AFND-p095-AFD.jff`](../../automatas/conversiones/L3-AFND-p095-AFD.jff) ([.json](../../automatas/conversiones/L3-AFND-p095-AFD.json), [.xml](../../automatas/conversiones/L3-AFND-p095-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 6 estados, y el AFD mínimo (Hopcroft), 6. La cota es 2^5 = 32. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-162-188-p-96"></a>

## Lista 3, problema 162-188 (p. 96)

**Enunciado.** AFN para el problema 96 de la Lista 2: Las palabras de Σ₁ con prefijo 20 y longitud 4.

**Clasificación: AFND.** El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD.

#### AFND — `L3-AFND-p096`

Archivos: [`L3-AFND-p096.jff`](../../automatas/lista3-afnd/L3-AFND-p096.jff) · [`L3-AFND-p096.json`](../../automatas/lista3-afnd/L3-AFND-p096.json) · [`L3-AFND-p096.xml`](../../automatas/lista3-afnd/L3-AFND-p096.xml). Tipo según la definición: **AFND**, |Q| = 5, Σ = {0, 1, 2}, 8 transiciones.

**Diseño.** Cadena 2, 0, Σ, Σ sin estado de rechazo; δ parcial.

| Estado | 0 | 1 | 2 |
|---|---|---|---|
| →q0 | — | — | q1 |
| q1 | q2 | — | — |
| q2 | q3 | q3 | q3 |
| q3 | q4 | q4 | q4 |
| *q4 | — | — | — |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `2000` | acepta | acepta | acepta |
| 2 | `2010` | acepta | acepta | acepta |
| 3 | `2012` | acepta | acepta | acepta |
| 4 | `2020` | acepta | acepta | acepta |
| 5 | `2022` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `22` | rechaza | rechaza | rechaza |
| 8 | `1020` | rechaza | rechaza | rechaza |
| 9 | `0220002` | rechaza | rechaza | rechaza |
| 10 | `02020102001` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `2000`: q0 -2→ q1 -0→ q2 -0→ q3 -0→ q4 — ✔
2. `2010`: q0 -2→ q1 -0→ q2 -1→ q3 -0→ q4 — ✔
3. `2012`: q0 -2→ q1 -0→ q2 -1→ q3 -2→ q4 — ✔
4. `2020`: q0 -2→ q1 -0→ q2 -2→ q3 -0→ q4 — ✔
5. `2022`: q0 -2→ q1 -0→ q2 -2→ q3 -2→ q4 — ✔
6. λ: q0 — ✘
7. `22`: q0 -2→ q1 -2→ (sin transición) — ✘
8. `1020`: q0 -1→ (sin transición) — ✘
9. `0220002`: q0 -0→ (sin transición) — ✘
10. `02020102001`: q0 -0→ (sin transición) — ✘

</details>

Simulación paso a paso en JFLAP con `2000`: [ver captura](../../evidencias/jflap/pasos/L3-AFND-p096.png).

**Conversión.** AFND (5 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 5 estados, [`L3-AFND-p096-AFD.jff`](../../automatas/conversiones/L3-AFND-p096-AFD.jff) ([.json](../../automatas/conversiones/L3-AFND-p096-AFD.json), [.xml](../../automatas/conversiones/L3-AFND-p096-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 6 estados, y el AFD mínimo (Hopcroft), 6. La cota es 2^5 = 32. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-162-188-p-97"></a>

## Lista 3, problema 162-188 (p. 97)

**Enunciado.** AFN para el problema 97 de la Lista 2: Palabras de Σ₁ cuya longitud es múltiplo de 3.

**Clasificación: AFND.** El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### AFND — `L3-AFND-p097`

Archivos: [`L3-AFND-p097.jff`](../../automatas/lista3-afnd/L3-AFND-p097.jff) · [`L3-AFND-p097.json`](../../automatas/lista3-afnd/L3-AFND-p097.json) · [`L3-AFND-p097.xml`](../../automatas/lista3-afnd/L3-AFND-p097.xml). Tipo según la definición: **AFD**, |Q| = 3, Σ = {0, 1, 2}, 9 transiciones.

**Diseño.** Contador módulo 3; el no determinismo no reduce nada.

| Estado | 0 | 1 | 2 |
|---|---|---|---|
| →*q0 | q1 | q1 | q1 |
| q1 | q2 | q2 | q2 |
| q2 | q0 | q0 | q0 |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | acepta | acepta | acepta |
| 2 | `010` | acepta | acepta | acepta |
| 3 | `101100` | acepta | acepta | acepta |
| 4 | `202021200` | acepta | acepta | acepta |
| 5 | `002111211020` | acepta | acepta | acepta |
| 6 | `0` | rechaza | rechaza | rechaza |
| 7 | `21` | rechaza | rechaza | rechaza |
| 8 | `1012` | rechaza | rechaza | rechaza |
| 9 | `2021101` | rechaza | rechaza | rechaza |
| 10 | `20101101020` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: q0 — ✔
2. `010`: q0 -0→ q1 -1→ q2 -0→ q0 — ✔
3. `101100`: q0 -1→ q1 -0→ q2 -1→ q0 -1→ q1 -0→ q2 -0→ q0 — ✔
4. `202021200`: q0 -2→ q1 -0→ q2 -2→ q0 -0→ q1 -2→ q2 -1→ q0 -2→ q1 -0→ q2 -0→ q0 — ✔
5. `002111211020`: q0 -0→ q1 -0→ q2 -2→ q0 -1→ q1 -1→ q2 -1→ q0 -2→ q1 -1→ q2 -1→ q0 -0→ q1 -2→ q2 -0→ q0 — ✔
6. `0`: q0 -0→ q1 — ✘
7. `21`: q0 -2→ q1 -1→ q2 — ✘
8. `1012`: q0 -1→ q1 -0→ q2 -1→ q0 -2→ q1 — ✘
9. `2021101`: q0 -2→ q1 -0→ q2 -2→ q0 -1→ q1 -1→ q2 -0→ q0 -1→ q1 — ✘
10. `20101101020`: q0 -2→ q1 -0→ q2 -1→ q0 -0→ q1 -1→ q2 -1→ q0 -0→ q1 -1→ q2 -0→ q0 -2→ q1 -0→ q2 — ✘

</details>

Simulación paso a paso en JFLAP con `010`: [ver captura](../../evidencias/jflap/pasos/L3-AFND-p097.png).

<a id="problema-3-162-188-p-98"></a>

## Lista 3, problema 162-188 (p. 98)

**Enunciado.** AFN para el problema 98 de la Lista 2: Las palabras de Σ₁ que terminan con la cadena 00102.

**Clasificación: AFND.** El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD.

#### AFND — `L3-AFND-p098`

Archivos: [`L3-AFND-p098.jff`](../../automatas/lista3-afnd/L3-AFND-p098.jff) · [`L3-AFND-p098.json`](../../automatas/lista3-afnd/L3-AFND-p098.json) · [`L3-AFND-p098.xml`](../../automatas/lista3-afnd/L3-AFND-p098.xml). Tipo según la definición: **AFND**, |Q| = 6, Σ = {0, 1, 2}, 8 transiciones.

**Diseño.** q0 con lazo adivina dónde empieza el sufijo 00102; el resto es una cadena lineal sin salidas al final. Sustituye la función de fallo del AFD por la adivinanza.

| Estado | 0 | 1 | 2 |
|---|---|---|---|
| →q0 | {q0, q1} | {q0} | {q0} |
| q1 | {q2} | ∅ | ∅ |
| q2 | ∅ | {q3} | ∅ |
| q3 | {q4} | ∅ | ∅ |
| q4 | ∅ | ∅ | {q5} |
| *q5 | ∅ | ∅ | ∅ |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `00102` | acepta | acepta | acepta |
| 2 | `1200102` | acepta | acepta | acepta |
| 3 | `221200102` | acepta | acepta | acepta |
| 4 | `112010200102` | acepta | acepta | acepta |
| 5 | `101202111100102` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `02` | rechaza | rechaza | rechaza |
| 8 | `2220` | rechaza | rechaza | rechaza |
| 9 | `2121121` | rechaza | rechaza | rechaza |
| 10 | `10002011202` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `00102`: {q0} -0→ {q0, q1} -0→ {q0, q1, q2} -1→ {q0, q3} -0→ {q0, q1, q4} -2→ {q0, q5} — ✔
  Árbol de cómputo: 4 caminos, 1 de aceptación:
    - q0 -0→ q1 -0→ q2 -1→ q3 -0→ q4 -2→ q5 — ✔ acepta
    - q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -2→ q0 — ✘ termina fuera de F
    - q0 -0→ q0 -0→ q0 -1→ q0 -0→ q1 — ✘ muere tras leer `0010`
    - q0 -0→ q0 -0→ q1 — ✘ muere tras leer `00`
2. `1200102`: {q0} -1→ {q0} -2→ {q0} -0→ {q0, q1} -0→ {q0, q1, q2} -1→ {q0, q3} -0→ {q0, q1, q4} -2→ {q0, q5} — ✔
  Árbol de cómputo: 4 caminos, 1 de aceptación:
    - q0 -1→ q0 -2→ q0 -0→ q1 -0→ q2 -1→ q3 -0→ q4 -2→ q5 — ✔ acepta
    - q0 -1→ q0 -2→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -2→ q0 — ✘ termina fuera de F
    - q0 -1→ q0 -2→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q1 — ✘ muere tras leer `120010`
    - q0 -1→ q0 -2→ q0 -0→ q0 -0→ q1 — ✘ muere tras leer `1200`
3. `221200102`: {q0} -2→ {q0} -2→ {q0} -1→ {q0} -2→ {q0} -0→ {q0, q1} -0→ {q0, q1, q2} -1→ {q0, q3} -0→ {q0, q1, q4} -2→ {q0, q5} — ✔
  Árbol de cómputo: 4 caminos, 1 de aceptación:
    - q0 -2→ q0 -2→ q0 -1→ q0 -2→ q0 -0→ q1 -0→ q2 -1→ q3 -0→ q4 -2→ q5 — ✔ acepta
    - q0 -2→ q0 -2→ q0 -1→ q0 -2→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -2→ q0 — ✘ termina fuera de F
    - q0 -2→ q0 -2→ q0 -1→ q0 -2→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q1 — ✘ muere tras leer `22120010`
    - q0 -2→ q0 -2→ q0 -1→ q0 -2→ q0 -0→ q0 -0→ q1 — ✘ muere tras leer `221200`
4. `112010200102`: {q0} -1→ {q0} -1→ {q0} -2→ {q0} -0→ {q0, q1} -1→ {q0} -0→ {q0, q1} -2→ {q0} -0→ {q0, q1} -0→ {q0, q1, q2} -1→ {q0, q3} -0→ {q0, q1, q4} -2→ {q0, q5} — ✔
  Árbol de cómputo: 6 caminos, 1 de aceptación:
    - q0 -1→ q0 -1→ q0 -2→ q0 -0→ q0 -1→ q0 -0→ q0 -2→ q0 -0→ q1 -0→ q2 -1→ q3 -0→ q4 -2→ q5 — ✔ acepta
    - q0 -1→ q0 -1→ q0 -2→ q0 -0→ q0 -1→ q0 -0→ q0 -2→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -2→ q0 — ✘ termina fuera de F
    - q0 -1→ q0 -1→ q0 -2→ q0 -0→ q0 -1→ q0 -0→ q0 -2→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q1 — ✘ muere tras leer `11201020010`
    - q0 -1→ q0 -1→ q0 -2→ q0 -0→ q0 -1→ q0 -0→ q0 -2→ q0 -0→ q0 -0→ q1 — ✘ muere tras leer `112010200`
    - q0 -1→ q0 -1→ q0 -2→ q0 -0→ q0 -1→ q0 -0→ q1 — ✘ muere tras leer `112010`
    - q0 -1→ q0 -1→ q0 -2→ q0 -0→ q1 — ✘ muere tras leer `1120`
5. `101202111100102`: {q0} -1→ {q0} -0→ {q0, q1} -1→ {q0} -2→ {q0} -0→ {q0, q1} -2→ {q0} -1→ {q0} -1→ {q0} -1→ {q0} -1→ {q0} -0→ {q0, q1} -0→ {q0, q1, q2} -1→ {q0, q3} -0→ {q0, q1, q4} -2→ {q0, q5} — ✔
  Árbol de cómputo: 6 caminos, 1 de aceptación:
    - q0 -1→ q0 -0→ q0 -1→ q0 -2→ q0 -0→ q0 -2→ q0 -1→ q0 -1→ q0 -1→ q0 -1→ q0 -0→ q1 -0→ q2 -1→ q3 -0→ q4 -2→ q5 — ✔ acepta
    - q0 -1→ q0 -0→ q0 -1→ q0 -2→ q0 -0→ q0 -2→ q0 -1→ q0 -1→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -2→ q0 — ✘ termina fuera de F
    - q0 -1→ q0 -0→ q0 -1→ q0 -2→ q0 -0→ q0 -2→ q0 -1→ q0 -1→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q1 — ✘ muere tras leer `10120211110010`
    - q0 -1→ q0 -0→ q0 -1→ q0 -2→ q0 -0→ q0 -2→ q0 -1→ q0 -1→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q1 — ✘ muere tras leer `101202111100`
    - q0 -1→ q0 -0→ q0 -1→ q0 -2→ q0 -0→ q1 — ✘ muere tras leer `10120`
    - q0 -1→ q0 -0→ q1 — ✘ muere tras leer `10`
6. λ: {q0} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
7. `02`: {q0} -0→ {q0, q1} -2→ {q0} — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -0→ q0 -2→ q0 — ✘ termina fuera de F
    - q0 -0→ q1 — ✘ muere tras leer `0`
8. `2220`: {q0} -2→ {q0} -2→ {q0} -2→ {q0} -0→ {q0, q1} — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -2→ q0 -2→ q0 -2→ q0 -0→ q0 — ✘ termina fuera de F
    - q0 -2→ q0 -2→ q0 -2→ q0 -0→ q1 — ✘ termina fuera de F
9. `2121121`: {q0} -2→ {q0} -1→ {q0} -2→ {q0} -1→ {q0} -1→ {q0} -2→ {q0} -1→ {q0} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 -2→ q0 -1→ q0 -2→ q0 -1→ q0 -1→ q0 -2→ q0 -1→ q0 — ✘ termina fuera de F
10. `10002011202`: {q0} -1→ {q0} -0→ {q0, q1} -0→ {q0, q1, q2} -0→ {q0, q1, q2} -2→ {q0} -0→ {q0, q1} -1→ {q0} -1→ {q0} -2→ {q0} -0→ {q0, q1} -2→ {q0} — ✘
  Árbol de cómputo: 6 caminos, 0 de aceptación:
    - q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -2→ q0 -0→ q0 -1→ q0 -1→ q0 -2→ q0 -0→ q0 -2→ q0 — ✘ termina fuera de F
    - q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -2→ q0 -0→ q0 -1→ q0 -1→ q0 -2→ q0 -0→ q1 — ✘ muere tras leer `1000201120`
    - q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -2→ q0 -0→ q1 — ✘ muere tras leer `100020`
    - q0 -1→ q0 -0→ q0 -0→ q0 -0→ q1 — ✘ muere tras leer `1000`
    - q0 -1→ q0 -0→ q0 -0→ q1 -0→ q2 — ✘ muere tras leer `1000`
    - q0 -1→ q0 -0→ q1 -0→ q2 — ✘ muere tras leer `100`

</details>

Simulación paso a paso en JFLAP con `00102`: [ver captura](../../evidencias/jflap/pasos/L3-AFND-p098.png).

**Conversión.** AFND (6 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 6 estados, [`L3-AFND-p098-AFD.jff`](../../automatas/conversiones/L3-AFND-p098-AFD.jff) ([.json](../../automatas/conversiones/L3-AFND-p098-AFD.json), [.xml](../../automatas/conversiones/L3-AFND-p098-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 6 estados, y el AFD mínimo (Hopcroft), 6. La cota es 2^6 = 64. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-162-188-p-99"></a>

## Lista 3, problema 162-188 (p. 99)

**Enunciado.** AFN para el problema 99 de la Lista 2: Palabras de Σ₁ que terminan con 001001.

**Clasificación: AFND.** El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### AFND — `L3-AFND-p099`

Archivos: [`L3-AFND-p099.jff`](../../automatas/lista3-afnd/L3-AFND-p099.jff) · [`L3-AFND-p099.json`](../../automatas/lista3-afnd/L3-AFND-p099.json) · [`L3-AFND-p099.xml`](../../automatas/lista3-afnd/L3-AFND-p099.xml). Tipo según la definición: **AFND**, |Q| = 7, Σ = {0, 1, 2}, 9 transiciones.

**Diseño.** q0 se queda con cualquier símbolo y adivina dónde empieza 001001; el resto es una cadena lineal sin salidas al final.

| Estado | 0 | 1 | 2 |
|---|---|---|---|
| →q0 | {q0, q1} | {q0} | {q0} |
| q1 | {q2} | ∅ | ∅ |
| q2 | ∅ | {q3} | ∅ |
| q3 | {q4} | ∅ | ∅ |
| q4 | {q5} | ∅ | ∅ |
| q5 | ∅ | {q6} | ∅ |
| *q6 | ∅ | ∅ | ∅ |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `001001` | acepta | acepta | acepta |
| 2 | `02001001` | acepta | acepta | acepta |
| 3 | `2101001001` | acepta | acepta | acepta |
| 4 | `0211111001001` | acepta | acepta | acepta |
| 5 | `1101112021001001` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `20` | rechaza | rechaza | rechaza |
| 8 | `2121` | rechaza | rechaza | rechaza |
| 9 | `2101121` | rechaza | rechaza | rechaza |
| 10 | `20020010022` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `001001`: {q0} -0→ {q0, q1} -0→ {q0, q1, q2} -1→ {q0, q3} -0→ {q0, q1, q4} -0→ {q0, q1, q2, q5} -1→ {q0, q3, q6} — ✔
  Árbol de cómputo: 5 caminos, 1 de aceptación:
    - q0 -0→ q1 -0→ q2 -1→ q3 -0→ q4 -0→ q5 -1→ q6 — ✔ acepta
    - q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 — ✘ termina fuera de F
    - q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q1 — ✘ muere tras leer `00100`
    - q0 -0→ q0 -0→ q0 -1→ q0 -0→ q1 -0→ q2 -1→ q3 — ✘ termina fuera de F
    - q0 -0→ q0 -0→ q1 — ✘ muere tras leer `00`
2. `02001001`: {q0} -0→ {q0, q1} -2→ {q0} -0→ {q0, q1} -0→ {q0, q1, q2} -1→ {q0, q3} -0→ {q0, q1, q4} -0→ {q0, q1, q2, q5} -1→ {q0, q3, q6} — ✔
  Árbol de cómputo: 6 caminos, 1 de aceptación:
    - q0 -0→ q0 -2→ q0 -0→ q1 -0→ q2 -1→ q3 -0→ q4 -0→ q5 -1→ q6 — ✔ acepta
    - q0 -0→ q0 -2→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 — ✘ termina fuera de F
    - q0 -0→ q0 -2→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q1 — ✘ muere tras leer `0200100`
    - q0 -0→ q0 -2→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q1 -0→ q2 -1→ q3 — ✘ termina fuera de F
    - q0 -0→ q0 -2→ q0 -0→ q0 -0→ q1 — ✘ muere tras leer `0200`
    - q0 -0→ q1 — ✘ muere tras leer `0`
3. `2101001001`: {q0} -2→ {q0} -1→ {q0} -0→ {q0, q1} -1→ {q0} -0→ {q0, q1} -0→ {q0, q1, q2} -1→ {q0, q3} -0→ {q0, q1, q4} -0→ {q0, q1, q2, q5} -1→ {q0, q3, q6} — ✔
  Árbol de cómputo: 6 caminos, 1 de aceptación:
    - q0 -2→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q1 -0→ q2 -1→ q3 -0→ q4 -0→ q5 -1→ q6 — ✔ acepta
    - q0 -2→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 — ✘ termina fuera de F
    - q0 -2→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q1 — ✘ muere tras leer `210100100`
    - q0 -2→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q1 -0→ q2 -1→ q3 — ✘ termina fuera de F
    - q0 -2→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q1 — ✘ muere tras leer `210100`
    - q0 -2→ q0 -1→ q0 -0→ q1 — ✘ muere tras leer `210`
4. `0211111001001`: {q0} -0→ {q0, q1} -2→ {q0} -1→ {q0} -1→ {q0} -1→ {q0} -1→ {q0} -1→ {q0} -0→ {q0, q1} -0→ {q0, q1, q2} -1→ {q0, q3} -0→ {q0, q1, q4} -0→ {q0, q1, q2, q5} -1→ {q0, q3, q6} — ✔
  Árbol de cómputo: 6 caminos, 1 de aceptación:
    - q0 -0→ q0 -2→ q0 -1→ q0 -1→ q0 -1→ q0 -1→ q0 -1→ q0 -0→ q1 -0→ q2 -1→ q3 -0→ q4 -0→ q5 -1→ q6 — ✔ acepta
    - q0 -0→ q0 -2→ q0 -1→ q0 -1→ q0 -1→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 — ✘ termina fuera de F
    - q0 -0→ q0 -2→ q0 -1→ q0 -1→ q0 -1→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q1 — ✘ muere tras leer `021111100100`
    - q0 -0→ q0 -2→ q0 -1→ q0 -1→ q0 -1→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q1 -0→ q2 -1→ q3 — ✘ termina fuera de F
    - q0 -0→ q0 -2→ q0 -1→ q0 -1→ q0 -1→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q1 — ✘ muere tras leer `021111100`
    - q0 -0→ q1 — ✘ muere tras leer `0`
5. `1101112021001001`: {q0} -1→ {q0} -1→ {q0} -0→ {q0, q1} -1→ {q0} -1→ {q0} -1→ {q0} -2→ {q0} -0→ {q0, q1} -2→ {q0} -1→ {q0} -0→ {q0, q1} -0→ {q0, q1, q2} -1→ {q0, q3} -0→ {q0, q1, q4} -0→ {q0, q1, q2, q5} -1→ {q0, q3, q6} — ✔
  Árbol de cómputo: 7 caminos, 1 de aceptación (se muestran 6):
    - q0 -1→ q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -1→ q0 -2→ q0 -0→ q0 -2→ q0 -1→ q0 -0→ q1 -0→ q2 -1→ q3 -0→ q4 -0→ q5 -1→ q6 — ✔ acepta
    - q0 -1→ q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -1→ q0 -2→ q0 -0→ q0 -2→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 — ✘ termina fuera de F
    - q0 -1→ q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -1→ q0 -2→ q0 -0→ q0 -2→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q1 — ✘ muere tras leer `110111202100100`
    - q0 -1→ q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -1→ q0 -2→ q0 -0→ q0 -2→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q1 -0→ q2 -1→ q3 — ✘ termina fuera de F
    - q0 -1→ q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -1→ q0 -2→ q0 -0→ q0 -2→ q0 -1→ q0 -0→ q0 -0→ q1 — ✘ muere tras leer `110111202100`
    - q0 -1→ q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -1→ q0 -2→ q0 -0→ q1 — ✘ muere tras leer `11011120`
6. λ: {q0} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
7. `20`: {q0} -2→ {q0} -0→ {q0, q1} — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -2→ q0 -0→ q0 — ✘ termina fuera de F
    - q0 -2→ q0 -0→ q1 — ✘ termina fuera de F
8. `2121`: {q0} -2→ {q0} -1→ {q0} -2→ {q0} -1→ {q0} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 -2→ q0 -1→ q0 -2→ q0 -1→ q0 — ✘ termina fuera de F
9. `2101121`: {q0} -2→ {q0} -1→ {q0} -0→ {q0, q1} -1→ {q0} -1→ {q0} -2→ {q0} -1→ {q0} — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -2→ q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -2→ q0 -1→ q0 — ✘ termina fuera de F
    - q0 -2→ q0 -1→ q0 -0→ q1 — ✘ muere tras leer `210`
10. `20020010022`: {q0} -2→ {q0} -0→ {q0, q1} -0→ {q0, q1, q2} -2→ {q0} -0→ {q0, q1} -0→ {q0, q1, q2} -1→ {q0, q3} -0→ {q0, q1, q4} -0→ {q0, q1, q2, q5} -2→ {q0} -2→ {q0} — ✘
  Árbol de cómputo: 7 caminos, 0 de aceptación (se muestran 6):
    - q0 -2→ q0 -0→ q0 -0→ q0 -2→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 -2→ q0 -2→ q0 — ✘ termina fuera de F
    - q0 -2→ q0 -0→ q0 -0→ q0 -2→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q1 — ✘ muere tras leer `200200100`
    - q0 -2→ q0 -0→ q0 -0→ q0 -2→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q1 -0→ q2 — ✘ muere tras leer `200200100`
    - q0 -2→ q0 -0→ q0 -0→ q0 -2→ q0 -0→ q0 -0→ q1 — ✘ muere tras leer `200200`
    - q0 -2→ q0 -0→ q0 -0→ q0 -2→ q0 -0→ q1 -0→ q2 -1→ q3 -0→ q4 -0→ q5 — ✘ muere tras leer `200200100`
    - q0 -2→ q0 -0→ q0 -0→ q1 — ✘ muere tras leer `200`

</details>

Simulación paso a paso en JFLAP con `001001`: [ver captura](../../evidencias/jflap/pasos/L3-AFND-p099.png).

**Conversión.** AFND (7 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 7 estados, [`L3-AFND-p099-AFD.jff`](../../automatas/conversiones/L3-AFND-p099-AFD.jff) ([.json](../../automatas/conversiones/L3-AFND-p099-AFD.json), [.xml](../../automatas/conversiones/L3-AFND-p099-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 7 estados, y el AFD mínimo (Hopcroft), 7. La cota es 2^7 = 128. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-189"></a>

## Lista 3, problema 189

**Enunciado.** AFN para palabras que contienen 00101 o 00110.

**Clasificación: AFND.** Se pide un AFN: un lazo inicial adivina dónde empieza cada patrón. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### AFN para palabras que contienen 00101 o 00110. — `L3-189`

Archivos: [`L3-189.jff`](../../automatas/lista3-afnd/L3-189.jff) · [`L3-189.json`](../../automatas/lista3-afnd/L3-189.json) · [`L3-189.xml`](../../automatas/lista3-afnd/L3-189.xml). Tipo según la definición: **AFND**, |Q| = 7, Σ = {0, 1}, 11 transiciones.

**Diseño.** q0 con lazo adivina dónde empieza el patrón; dos ramas comparten 001 y terminan en un estado absorbente.

| Estado | 0 | 1 |
|---|---|---|
| →q0 | {q0, q1} | {q0} |
| q1 | {q2} | ∅ |
| q2 | ∅ | {q3} |
| q3 | {q4} | {q5} |
| q4 | ∅ | {q6} |
| q5 | {q6} | ∅ |
| *q6 | {q6} | {q6} |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `00101` | acepta | acepta | acepta |
| 2 | `100101` | acepta | acepta | acepta |
| 3 | `1100101` | acepta | acepta | acepta |
| 4 | `01011000110` | acepta | acepta | acepta |
| 5 | `110111100101` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `01` | rechaza | rechaza | rechaza |
| 8 | `1000` | rechaza | rechaza | rechaza |
| 9 | `1100100` | rechaza | rechaza | rechaza |
| 10 | `10000100111` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `00101`: {q0} -0→ {q0, q1} -0→ {q0, q1, q2} -1→ {q0, q3} -0→ {q0, q1, q4} -1→ {q0, q6} — ✔
  Árbol de cómputo: 4 caminos, 1 de aceptación:
    - q0 -0→ q1 -0→ q2 -1→ q3 -0→ q4 -1→ q6 — ✔ acepta
    - q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -1→ q0 — ✘ termina fuera de F
    - q0 -0→ q0 -0→ q0 -1→ q0 -0→ q1 — ✘ muere tras leer `0010`
    - q0 -0→ q0 -0→ q1 — ✘ muere tras leer `00`
2. `100101`: {q0} -1→ {q0} -0→ {q0, q1} -0→ {q0, q1, q2} -1→ {q0, q3} -0→ {q0, q1, q4} -1→ {q0, q6} — ✔
  Árbol de cómputo: 4 caminos, 1 de aceptación:
    - q0 -1→ q0 -0→ q1 -0→ q2 -1→ q3 -0→ q4 -1→ q6 — ✔ acepta
    - q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -1→ q0 — ✘ termina fuera de F
    - q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q1 — ✘ muere tras leer `10010`
    - q0 -1→ q0 -0→ q0 -0→ q1 — ✘ muere tras leer `100`
3. `1100101`: {q0} -1→ {q0} -1→ {q0} -0→ {q0, q1} -0→ {q0, q1, q2} -1→ {q0, q3} -0→ {q0, q1, q4} -1→ {q0, q6} — ✔
  Árbol de cómputo: 4 caminos, 1 de aceptación:
    - q0 -1→ q0 -1→ q0 -0→ q1 -0→ q2 -1→ q3 -0→ q4 -1→ q6 — ✔ acepta
    - q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -1→ q0 — ✘ termina fuera de F
    - q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q1 — ✘ muere tras leer `110010`
    - q0 -1→ q0 -1→ q0 -0→ q0 -0→ q1 — ✘ muere tras leer `1100`
4. `01011000110`: {q0} -0→ {q0, q1} -1→ {q0} -0→ {q0, q1} -1→ {q0} -1→ {q0} -0→ {q0, q1} -0→ {q0, q1, q2} -0→ {q0, q1, q2} -1→ {q0, q3} -1→ {q0, q5} -0→ {q0, q1, q6} — ✔
  Árbol de cómputo: 7 caminos, 1 de aceptación (se muestran 6):
    - q0 -0→ q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q1 -0→ q2 -1→ q3 -1→ q5 -0→ q6 — ✔ acepta
    - q0 -0→ q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 — ✘ termina fuera de F
    - q0 -0→ q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q1 — ✘ termina fuera de F
    - q0 -0→ q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q1 — ✘ muere tras leer `01011000`
    - q0 -0→ q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q1 -0→ q2 — ✘ muere tras leer `0101100`
    - q0 -0→ q0 -1→ q0 -0→ q1 — ✘ muere tras leer `010`
5. `110111100101`: {q0} -1→ {q0} -1→ {q0} -0→ {q0, q1} -1→ {q0} -1→ {q0} -1→ {q0} -1→ {q0} -0→ {q0, q1} -0→ {q0, q1, q2} -1→ {q0, q3} -0→ {q0, q1, q4} -1→ {q0, q6} — ✔
  Árbol de cómputo: 5 caminos, 1 de aceptación:
    - q0 -1→ q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -1→ q0 -1→ q0 -0→ q1 -0→ q2 -1→ q3 -0→ q4 -1→ q6 — ✔ acepta
    - q0 -1→ q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -1→ q0 — ✘ termina fuera de F
    - q0 -1→ q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q1 — ✘ muere tras leer `11011110010`
    - q0 -1→ q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q1 — ✘ muere tras leer `110111100`
    - q0 -1→ q0 -1→ q0 -0→ q1 — ✘ muere tras leer `110`
6. λ: {q0} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
7. `01`: {q0} -0→ {q0, q1} -1→ {q0} — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -0→ q0 -1→ q0 — ✘ termina fuera de F
    - q0 -0→ q1 — ✘ muere tras leer `0`
8. `1000`: {q0} -1→ {q0} -0→ {q0, q1} -0→ {q0, q1, q2} -0→ {q0, q1, q2} — ✘
  Árbol de cómputo: 4 caminos, 0 de aceptación:
    - q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 — ✘ termina fuera de F
    - q0 -1→ q0 -0→ q0 -0→ q0 -0→ q1 — ✘ termina fuera de F
    - q0 -1→ q0 -0→ q0 -0→ q1 -0→ q2 — ✘ termina fuera de F
    - q0 -1→ q0 -0→ q1 -0→ q2 — ✘ muere tras leer `100`
9. `1100100`: {q0} -1→ {q0} -1→ {q0} -0→ {q0, q1} -0→ {q0, q1, q2} -1→ {q0, q3} -0→ {q0, q1, q4} -0→ {q0, q1, q2} — ✘
  Árbol de cómputo: 5 caminos, 0 de aceptación:
    - q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 — ✘ termina fuera de F
    - q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q1 — ✘ termina fuera de F
    - q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q1 -0→ q2 — ✘ termina fuera de F
    - q0 -1→ q0 -1→ q0 -0→ q0 -0→ q1 — ✘ muere tras leer `1100`
    - q0 -1→ q0 -1→ q0 -0→ q1 -0→ q2 -1→ q3 -0→ q4 — ✘ muere tras leer `110010`
10. `10000100111`: {q0} -1→ {q0} -0→ {q0, q1} -0→ {q0, q1, q2} -0→ {q0, q1, q2} -0→ {q0, q1, q2} -1→ {q0, q3} -0→ {q0, q1, q4} -0→ {q0, q1, q2} -1→ {q0, q3} -1→ {q0, q5} -1→ {q0} — ✘
  Árbol de cómputo: 7 caminos, 0 de aceptación (se muestran 6):
    - q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -1→ q0 -1→ q0 — ✘ termina fuera de F
    - q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q1 — ✘ muere tras leer `10000100`
    - q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q1 -0→ q2 -1→ q3 -1→ q5 — ✘ muere tras leer `1000010011`
    - q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -0→ q1 — ✘ muere tras leer `10000`
    - q0 -1→ q0 -0→ q0 -0→ q0 -0→ q1 -0→ q2 -1→ q3 -0→ q4 — ✘ muere tras leer `1000010`
    - q0 -1→ q0 -0→ q0 -0→ q1 -0→ q2 — ✘ muere tras leer `1000`

</details>

Simulación paso a paso en JFLAP con `00101`: [ver captura](../../evidencias/jflap/pasos/L3-189.png).

**Conversión.** AFND (7 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 12 estados, [`L3-189-AFD.jff`](../../automatas/conversiones/L3-189-AFD.jff) ([.json](../../automatas/conversiones/L3-189-AFD.json), [.xml](../../automatas/conversiones/L3-189-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 12 estados, y el AFD mínimo (Hopcroft), 7. La cota es 2^7 = 128. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-190"></a>

## Lista 3, problema 190

**Enunciado.** AFN para palabras que contienen 11010 y 10100.

**Clasificación: AFND.** Se pide un AFN: un lazo inicial adivina dónde empieza cada patrón. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### AFN para palabras que contienen 11010 y 10100. — `L3-190`

Archivos: [`L3-190.jff`](../../automatas/lista3-afnd/L3-190.jff) · [`L3-190.json`](../../automatas/lista3-afnd/L3-190.json) · [`L3-190.xml`](../../automatas/lista3-afnd/L3-190.xml). Tipo según la definición: **AFND**, |Q| = 32, Σ = {0, 1}, 42 transiciones.

**Diseño.** Una rama por cada orden de los patrones y por cada traslape posible; cada estado indica qué patrón y cuántos símbolos se llevan.

<details><summary>Tabla de transiciones (32 estados)</summary>

| Estado | 0 | 1 |
|---|---|---|
| →q0 | {q0} | {q0, q1, q10, q19, q24} |
| q1 | ∅ | {q2} |
| q2 | {q3} | ∅ |
| q3 | ∅ | {q4} |
| q4 | {q5} | ∅ |
| q5 | {q5} | {q5, q6} |
| q6 | {q7} | ∅ |
| q7 | ∅ | {q8} |
| q8 | {q9} | ∅ |
| q9 | {q31} | ∅ |
| q10 | {q11} | ∅ |
| q11 | ∅ | {q12} |
| q12 | {q13} | ∅ |
| q13 | {q14} | ∅ |
| q14 | {q14} | {q14, q15} |
| q15 | ∅ | {q16} |
| q16 | {q17} | ∅ |
| q17 | ∅ | {q18} |
| q18 | {q31} | ∅ |
| q19 | ∅ | {q20} |
| q20 | {q21} | ∅ |
| q21 | ∅ | {q22} |
| q22 | {q23} | ∅ |
| q23 | {q31} | ∅ |
| q24 | ∅ | {q25} |
| q25 | {q26} | ∅ |
| q26 | ∅ | {q27} |
| q27 | {q28} | ∅ |
| q28 | ∅ | {q29} |
| q29 | {q30} | ∅ |
| q30 | {q31} | ∅ |
| *q31 | {q31} | {q31} |

</details>

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `110100` | acepta | acepta | acepta |
| 2 | `00110100` | acepta | acepta | acepta |
| 3 | `10110100` | acepta | acepta | acepta |
| 4 | `1110000110100` | acepta | acepta | acepta |
| 5 | `1010000001011010` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `01` | rechaza | rechaza | rechaza |
| 8 | `0101` | rechaza | rechaza | rechaza |
| 9 | `1101101` | rechaza | rechaza | rechaza |
| 10 | `11001100011` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `110100`: {q0} -1→ {q0, q1, q10, q19, q24} -1→ {q0, q1, q10, q19, q2, q20, q24, q25} -0→ {q0, q11, q21, q26, q3} -1→ {q0, q1, q10, q12, q19, q22, q24, q27, q4} -0→ {q0, q11, q13, q23, q28, q5} -0→ {q0, q14, q31, q5} — ✔
  Árbol de cómputo: 13 caminos, 1 de aceptación (se muestran 6):
    - q0 -1→ q19 -1→ q20 -0→ q21 -1→ q22 -0→ q23 -0→ q31 — ✔ acepta
    - q0 -1→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 — ✘ termina fuera de F
    - q0 -1→ q0 -1→ q0 -0→ q0 -1→ q1 — ✘ muere tras leer `1101`
    - q0 -1→ q0 -1→ q0 -0→ q0 -1→ q10 -0→ q11 — ✘ muere tras leer `11010`
    - q0 -1→ q0 -1→ q0 -0→ q0 -1→ q19 — ✘ muere tras leer `1101`
    - q0 -1→ q0 -1→ q0 -0→ q0 -1→ q24 — ✘ muere tras leer `1101`
2. `00110100`: {q0} -0→ {q0} -0→ {q0} -1→ {q0, q1, q10, q19, q24} -1→ {q0, q1, q10, q19, q2, q20, q24, q25} -0→ {q0, q11, q21, q26, q3} -1→ {q0, q1, q10, q12, q19, q22, q24, q27, q4} -0→ {q0, q11, q13, q23, q28, q5} -0→ {q0, q14, q31, q5} — ✔
  Árbol de cómputo: 13 caminos, 1 de aceptación (se muestran 6):
    - q0 -0→ q0 -0→ q0 -1→ q19 -1→ q20 -0→ q21 -1→ q22 -0→ q23 -0→ q31 — ✔ acepta
    - q0 -0→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 — ✘ termina fuera de F
    - q0 -0→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q1 — ✘ muere tras leer `001101`
    - q0 -0→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q10 -0→ q11 — ✘ muere tras leer `0011010`
    - q0 -0→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q19 — ✘ muere tras leer `001101`
    - q0 -0→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q24 — ✘ muere tras leer `001101`
3. `10110100`: {q0} -1→ {q0, q1, q10, q19, q24} -0→ {q0, q11} -1→ {q0, q1, q10, q12, q19, q24} -1→ {q0, q1, q10, q19, q2, q20, q24, q25} -0→ {q0, q11, q21, q26, q3} -1→ {q0, q1, q10, q12, q19, q22, q24, q27, q4} -0→ {q0, q11, q13, q23, q28, q5} -0→ {q0, q14, q31, q5} — ✔
  Árbol de cómputo: 17 caminos, 1 de aceptación (se muestran 6):
    - q0 -1→ q0 -0→ q0 -1→ q19 -1→ q20 -0→ q21 -1→ q22 -0→ q23 -0→ q31 — ✔ acepta
    - q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 — ✘ termina fuera de F
    - q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q1 — ✘ muere tras leer `101101`
    - q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q10 -0→ q11 — ✘ muere tras leer `1011010`
    - q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q19 — ✘ muere tras leer `101101`
    - q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q24 — ✘ muere tras leer `101101`
4. `1110000110100`: {q0} -1→ {q0, q1, q10, q19, q24} -1→ {q0, q1, q10, q19, q2, q20, q24, q25} -1→ {q0, q1, q10, q19, q2, q20, q24, q25} -0→ {q0, q11, q21, q26, q3} -0→ {q0} -0→ {q0} -0→ {q0} -1→ {q0, q1, q10, q19, q24} -1→ {q0, q1, q10, q19, q2, q20, q24, q25} -0→ {q0, q11, q21, q26, q3} -1→ {q0, q1, q10, q12, q19, q22, q24, q27, q4} -0→ {q0, q11, q13, q23, q28, q5} -0→ {q0, q14, q31, q5} — ✔
  Árbol de cómputo: 25 caminos, 1 de aceptación (se muestran 6):
    - q0 -1→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -0→ q0 -1→ q19 -1→ q20 -0→ q21 -1→ q22 -0→ q23 -0→ q31 — ✔ acepta
    - q0 -1→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 — ✘ termina fuera de F
    - q0 -1→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q1 — ✘ muere tras leer `11100001101`
    - q0 -1→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q10 -0→ q11 — ✘ muere tras leer `111000011010`
    - q0 -1→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q19 — ✘ muere tras leer `11100001101`
    - q0 -1→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q24 — ✘ muere tras leer `11100001101`
5. `1010000001011010`: {q0} -1→ {q0, q1, q10, q19, q24} -0→ {q0, q11} -1→ {q0, q1, q10, q12, q19, q24} -0→ {q0, q11, q13} -0→ {q0, q14} -0→ {q0, q14} -0→ {q0, q14} -0→ {q0, q14} -0→ {q0, q14} -1→ {q0, q1, q10, q14, q15, q19, q24} -0→ {q0, q11, q14} -1→ {q0, q1, q10, q12, q14, q15, q19, q24} -1→ {q0, q1, q10, q14, q15, q16, q19, q2, q20, q24, q25} -0→ {q0, q11, q14, q17, q21, q26, q3} -1→ {q0, q1, q10, q12, q14, q15, q18, q19, q22, q24, q27, q4} -0→ {q0, q11, q13, q14, q23, q28, q31, q5} — ✔
  Árbol de cómputo: 29 caminos, 1 de aceptación (se muestran 6):
    - q0 -1→ q10 -0→ q11 -1→ q12 -0→ q13 -0→ q14 -0→ q14 -0→ q14 -0→ q14 -0→ q14 -1→ q14 -0→ q14 -1→ q15 -1→ q16 -0→ q17 -1→ q18 -0→ q31 — ✔ acepta
    - q0 -1→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q0 — ✘ termina fuera de F
    - q0 -1→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q1 — ✘ muere tras leer `101000000101101`
    - q0 -1→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q10 -0→ q11 — ✘ termina fuera de F
    - q0 -1→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q19 — ✘ muere tras leer `101000000101101`
    - q0 -1→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q24 — ✘ muere tras leer `101000000101101`
6. λ: {q0} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
7. `01`: {q0} -0→ {q0} -1→ {q0, q1, q10, q19, q24} — ✘
  Árbol de cómputo: 5 caminos, 0 de aceptación:
    - q0 -0→ q0 -1→ q0 — ✘ termina fuera de F
    - q0 -0→ q0 -1→ q1 — ✘ termina fuera de F
    - q0 -0→ q0 -1→ q10 — ✘ termina fuera de F
    - q0 -0→ q0 -1→ q19 — ✘ termina fuera de F
    - q0 -0→ q0 -1→ q24 — ✘ termina fuera de F
8. `0101`: {q0} -0→ {q0} -1→ {q0, q1, q10, q19, q24} -0→ {q0, q11} -1→ {q0, q1, q10, q12, q19, q24} — ✘
  Árbol de cómputo: 9 caminos, 0 de aceptación (se muestran 6):
    - q0 -0→ q0 -1→ q0 -0→ q0 -1→ q0 — ✘ termina fuera de F
    - q0 -0→ q0 -1→ q0 -0→ q0 -1→ q1 — ✘ termina fuera de F
    - q0 -0→ q0 -1→ q0 -0→ q0 -1→ q10 — ✘ termina fuera de F
    - q0 -0→ q0 -1→ q0 -0→ q0 -1→ q19 — ✘ termina fuera de F
    - q0 -0→ q0 -1→ q0 -0→ q0 -1→ q24 — ✘ termina fuera de F
    - q0 -0→ q0 -1→ q1 — ✘ muere tras leer `01`
9. `1101101`: {q0} -1→ {q0, q1, q10, q19, q24} -1→ {q0, q1, q10, q19, q2, q20, q24, q25} -0→ {q0, q11, q21, q26, q3} -1→ {q0, q1, q10, q12, q19, q22, q24, q27, q4} -1→ {q0, q1, q10, q19, q2, q20, q24, q25} -0→ {q0, q11, q21, q26, q3} -1→ {q0, q1, q10, q12, q19, q22, q24, q27, q4} — ✘
  Árbol de cómputo: 21 caminos, 0 de aceptación (se muestran 6):
    - q0 -1→ q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q0 — ✘ termina fuera de F
    - q0 -1→ q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q1 — ✘ termina fuera de F
    - q0 -1→ q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q10 — ✘ termina fuera de F
    - q0 -1→ q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q19 — ✘ termina fuera de F
    - q0 -1→ q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q24 — ✘ termina fuera de F
    - q0 -1→ q0 -1→ q0 -0→ q0 -1→ q0 -1→ q1 — ✘ muere tras leer `11011`
10. `11001100011`: {q0} -1→ {q0, q1, q10, q19, q24} -1→ {q0, q1, q10, q19, q2, q20, q24, q25} -0→ {q0, q11, q21, q26, q3} -0→ {q0} -1→ {q0, q1, q10, q19, q24} -1→ {q0, q1, q10, q19, q2, q20, q24, q25} -0→ {q0, q11, q21, q26, q3} -0→ {q0} -0→ {q0} -1→ {q0, q1, q10, q19, q24} -1→ {q0, q1, q10, q19, q2, q20, q24, q25} — ✘
  Árbol de cómputo: 25 caminos, 0 de aceptación (se muestran 6):
    - q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 -1→ q0 — ✘ termina fuera de F
    - q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 -1→ q1 — ✘ termina fuera de F
    - q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 -1→ q10 — ✘ termina fuera de F
    - q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 -1→ q19 — ✘ termina fuera de F
    - q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 -1→ q24 — ✘ termina fuera de F
    - q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -1→ q1 -1→ q2 — ✘ termina fuera de F

</details>

Simulación paso a paso en JFLAP con `110100`: [ver captura](../../evidencias/jflap/pasos/L3-190.png).

**Conversión.** AFND (32 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 44 estados, [`L3-190-AFD.jff`](../../automatas/conversiones/L3-190-AFD.jff) ([.json](../../automatas/conversiones/L3-190-AFD.json), [.xml](../../automatas/conversiones/L3-190-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 44 estados, y el AFD mínimo (Hopcroft), 19. La cota es 2^32 = 4294967296. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-191"></a>

## Lista 3, problema 191

**Enunciado.** En los problemas 191-194, considere el AFN A = (Q, Σ, δ, A₀, F) definido en cada tabla. Encuentre un AFD equivalente y calcule δ̂(Z, ω) y δ̂_D(Z, ω).

**Clasificación: AFND.** Es el planteamiento común de los problemas 192-194: dado un AFN, hallar el AFD por subconjuntos.

El método común es la construcción de subconjuntos: el AFD tiene por estados los subconjuntos de Q alcanzables desde {A₀}; δ_D(S, a) = ⋃_{q ∈ S} δ(q, a) y S es de aceptación si S ∩ F ≠ ∅. Como el AFD simula todos los caminos a la vez, δ̂_D({…}, ω) = δ̂(Z, ω) para todo Z y toda ω: los incisos a) y b) dan el mismo conjunto, uno visto como conjunto de estados del AFN y el otro como un solo estado del AFD. Los valores numéricos se calculan en cada problema.

<a id="problema-3-192"></a>

## Lista 3, problema 192

**Enunciado.** AFN de la tabla 192.

**Clasificación: AFND.** El autómata dado tiene celdas con dos o más estados y celdas ∅: es un AFN; el AFD es su conversión. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

**Valores pedidos** (con los nombres de estado de la tabla):

- δ̂({A}, 0111) = ∅: {A} -0→ {B} -1→ ∅ -1→ ∅ -1→ ∅
- δ̂({B, C}, 010111) = ∅: {B, C} -0→ {A, B, C} -1→ {B, C} -0→ {A, B, C} -1→ {B, C} -1→ ∅ -1→ ∅

#### AFN de la tabla 192. — `L3-192-AFND`

Archivos: [`L3-192-AFND.jff`](../../automatas/lista3-afnd/L3-192-AFND.jff) · [`L3-192-AFND.json`](../../automatas/lista3-afnd/L3-192-AFND.json) · [`L3-192-AFND.xml`](../../automatas/lista3-afnd/L3-192-AFND.xml). Tipo según la definición: **AFND**, |Q| = 3, Σ = {0, 1}, 7 transiciones.

**Diseño.** Transcripción de la tabla.

| Estado | 0 | 1 |
|---|---|---|
| →A | {B} | {B, C} |
| B | {A, B} | ∅ |
| *C | {A, C} | ∅ |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `1` | acepta | acepta | acepta |
| 2 | `10` | acepta | acepta | acepta |
| 3 | `0010` | acepta | acepta | acepta |
| 4 | `0010010` | acepta | acepta | acepta |
| 5 | `10100100101` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `01` | rechaza | rechaza | rechaza |
| 8 | `0111` | rechaza | rechaza | rechaza |
| 9 | `10101011` | rechaza | rechaza | rechaza |
| 10 | `00111011101` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `1`: {A} -1→ {B, C} — ✔
  Árbol de cómputo: 2 caminos, 1 de aceptación:
    - A -1→ C — ✔ acepta
    - A -1→ B — ✘ termina fuera de F
2. `10`: {A} -1→ {B, C} -0→ {A, B, C} — ✔
  Árbol de cómputo: 4 caminos, 1 de aceptación:
    - A -1→ C -0→ C — ✔ acepta
    - A -1→ B -0→ A — ✘ termina fuera de F
    - A -1→ B -0→ B — ✘ termina fuera de F
    - A -1→ C -0→ A — ✘ termina fuera de F
3. `0010`: {A} -0→ {B} -0→ {A, B} -1→ {B, C} -0→ {A, B, C} — ✔
  Árbol de cómputo: 5 caminos, 1 de aceptación:
    - A -0→ B -0→ A -1→ C -0→ C — ✔ acepta
    - A -0→ B -0→ A -1→ B -0→ A — ✘ termina fuera de F
    - A -0→ B -0→ A -1→ B -0→ B — ✘ termina fuera de F
    - A -0→ B -0→ A -1→ C -0→ A — ✘ termina fuera de F
    - A -0→ B -0→ B — ✘ muere tras leer `00`
4. `0010010`: {A} -0→ {B} -0→ {A, B} -1→ {B, C} -0→ {A, B, C} -0→ {A, B, C} -1→ {B, C} -0→ {A, B, C} — ✔
  Árbol de cómputo: 13 caminos, 2 de aceptación (se muestran 6):
    - A -0→ B -0→ A -1→ B -0→ B -0→ A -1→ C -0→ C — ✔ acepta
    - A -0→ B -0→ A -1→ C -0→ C -0→ A -1→ C -0→ C — ✔ acepta
    - A -0→ B -0→ A -1→ B -0→ A -0→ B — ✘ muere tras leer `00100`
    - A -0→ B -0→ A -1→ B -0→ B -0→ A -1→ B -0→ A — ✘ termina fuera de F
    - A -0→ B -0→ A -1→ B -0→ B -0→ A -1→ B -0→ B — ✘ termina fuera de F
    - A -0→ B -0→ A -1→ B -0→ B -0→ A -1→ C -0→ A — ✘ termina fuera de F
5. `10100100101`: {A} -1→ {B, C} -0→ {A, B, C} -1→ {B, C} -0→ {A, B, C} -0→ {A, B, C} -1→ {B, C} -0→ {A, B, C} -0→ {A, B, C} -1→ {B, C} -0→ {A, B, C} -1→ {B, C} — ✔
  Árbol de cómputo: 74 caminos, 16 de aceptación (se muestran 6):
    - A -1→ B -0→ A -1→ B -0→ B -0→ A -1→ B -0→ B -0→ A -1→ B -0→ A -1→ C — ✔ acepta
    - A -1→ B -0→ A -1→ B -0→ B -0→ A -1→ B -0→ B -0→ A -1→ C -0→ A -1→ C — ✔ acepta
    - A -1→ B -0→ A -1→ B -0→ B -0→ A -1→ C -0→ C -0→ A -1→ B -0→ A -1→ C — ✔ acepta
    - A -1→ B -0→ A -1→ B -0→ A -0→ B — ✘ muere tras leer `10100`
    - A -1→ B -0→ A -1→ B -0→ B -0→ A -1→ B -0→ A -0→ B — ✘ muere tras leer `10100100`
    - A -1→ B -0→ A -1→ B -0→ B -0→ A -1→ B -0→ B -0→ A -1→ B -0→ A -1→ B — ✘ termina fuera de F
6. λ: {A} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - A — ✘ termina fuera de F
7. `01`: {A} -0→ {B} -1→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - A -0→ B — ✘ muere tras leer `0`
8. `0111`: {A} -0→ {B} -1→ ∅ -1→ ∅ -1→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - A -0→ B — ✘ muere tras leer `0`
9. `10101011`: {A} -1→ {B, C} -0→ {A, B, C} -1→ {B, C} -0→ {A, B, C} -1→ {B, C} -0→ {A, B, C} -1→ {B, C} -1→ ∅ — ✘
  Árbol de cómputo: 30 caminos, 0 de aceptación (se muestran 6):
    - A -1→ B -0→ A -1→ B -0→ A -1→ B -0→ A -1→ B — ✘ muere tras leer `1010101`
    - A -1→ B -0→ A -1→ B -0→ A -1→ B -0→ A -1→ C — ✘ muere tras leer `1010101`
    - A -1→ B -0→ A -1→ B -0→ A -1→ B -0→ B — ✘ muere tras leer `101010`
    - A -1→ B -0→ A -1→ B -0→ A -1→ C -0→ A -1→ B — ✘ muere tras leer `1010101`
    - A -1→ B -0→ A -1→ B -0→ A -1→ C -0→ A -1→ C — ✘ muere tras leer `1010101`
    - A -1→ B -0→ A -1→ B -0→ A -1→ C -0→ C — ✘ muere tras leer `101010`
10. `00111011101`: {A} -0→ {B} -0→ {A, B} -1→ {B, C} -1→ ∅ -1→ ∅ -0→ ∅ -1→ ∅ -1→ ∅ -1→ ∅ -0→ ∅ -1→ ∅ — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - A -0→ B -0→ A -1→ B — ✘ muere tras leer `001`
    - A -0→ B -0→ A -1→ C — ✘ muere tras leer `001`
    - A -0→ B -0→ B — ✘ muere tras leer `00`

</details>

Simulación paso a paso en JFLAP con `10`: [ver captura](../../evidencias/jflap/pasos/L3-192-AFND.png).

**Conversión.** AFND (3 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 5 estados, [`L3-192-AFND-AFD.jff`](../../automatas/conversiones/L3-192-AFND-AFD.jff) ([.json](../../automatas/conversiones/L3-192-AFND-AFD.json), [.xml](../../automatas/conversiones/L3-192-AFND-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 6 estados, y el AFD mínimo (Hopcroft), 6. La cota es 2^3 = 8. Se verificó que los tres autómatas aceptan el mismo lenguaje.

#### AFD equivalente al 192. — `L3-192-AFD`

Archivos: [`L3-192-AFD.jff`](../../automatas/lista3-afnd/L3-192-AFD.jff) · [`L3-192-AFD.json`](../../automatas/lista3-afnd/L3-192-AFD.json) · [`L3-192-AFD.xml`](../../automatas/lista3-afnd/L3-192-AFD.xml). Tipo según la definición: **AFD**, |Q| = 6, Σ = {0, 1}, 12 transiciones.

**Diseño.** Construcción de subconjuntos: cada estado es el conjunto de estados del AFN alcanzables con el prefijo leído; acepta si contiene un estado final.

| Estado | 0 | 1 |
|---|---|---|
| →{A} | {B} | {B,C} |
| {B} | {A,B} | ∅ |
| *{B,C} | {A,B,C} | ∅ |
| {A,B} | {A,B} | {B,C} |
| ∅ | ∅ | ∅ |
| *{A,B,C} | {A,B,C} | {B,C} |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `1` | acepta | acepta | acepta |
| 2 | `001` | acepta | acepta | acepta |
| 3 | `0010` | acepta | acepta | acepta |
| 4 | `1010100` | acepta | acepta | acepta |
| 5 | `10001010001` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `00` | rechaza | rechaza | rechaza |
| 8 | `1110` | rechaza | rechaza | rechaza |
| 9 | `0100000` | rechaza | rechaza | rechaza |
| 10 | `11111111001` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `1`: {A} -1→ {B,C} — ✔
2. `001`: {A} -0→ {B} -0→ {A,B} -1→ {B,C} — ✔
3. `0010`: {A} -0→ {B} -0→ {A,B} -1→ {B,C} -0→ {A,B,C} — ✔
4. `1010100`: {A} -1→ {B,C} -0→ {A,B,C} -1→ {B,C} -0→ {A,B,C} -1→ {B,C} -0→ {A,B,C} -0→ {A,B,C} — ✔
5. `10001010001`: {A} -1→ {B,C} -0→ {A,B,C} -0→ {A,B,C} -0→ {A,B,C} -1→ {B,C} -0→ {A,B,C} -1→ {B,C} -0→ {A,B,C} -0→ {A,B,C} -0→ {A,B,C} -1→ {B,C} — ✔
6. λ: {A} — ✘
7. `00`: {A} -0→ {B} -0→ {A,B} — ✘
8. `1110`: {A} -1→ {B,C} -1→ ∅ -1→ ∅ -0→ ∅ — ✘
9. `0100000`: {A} -0→ {B} -1→ ∅ -0→ ∅ -0→ ∅ -0→ ∅ -0→ ∅ -0→ ∅ — ✘
10. `11111111001`: {A} -1→ {B,C} -1→ ∅ -1→ ∅ -1→ ∅ -1→ ∅ -1→ ∅ -1→ ∅ -1→ ∅ -0→ ∅ -0→ ∅ -1→ ∅ — ✘

</details>

Simulación paso a paso en JFLAP con `001`: [ver captura](../../evidencias/jflap/pasos/L3-192-AFD.png).

<a id="problema-3-193"></a>

## Lista 3, problema 193

**Enunciado.** AFN de la tabla 193.

**Clasificación: AFND.** El autómata dado tiene celdas con dos o más estados y celdas ∅: es un AFN; el AFD es su conversión. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

**Valores pedidos** (con los nombres de estado de la tabla):

- δ̂({A}, 01101) = ∅: {A} -0→ ∅ -1→ ∅ -1→ ∅ -0→ ∅ -1→ ∅
- δ̂({A, B}, 1101) = {A, B, C, D}: {A, B} -1→ {B, C, D} -1→ {A, B, C, D} -0→ {A, C, D} -1→ {A, B, C, D}
- δ̂({C}, 1101) = {A, B, C, D}: {C} -1→ {A, C} -1→ {A, B, C} -0→ {A, C, D} -1→ {A, B, C, D}

#### AFN de la tabla 193. — `L3-193-AFND`

Archivos: [`L3-193-AFND.jff`](../../automatas/lista3-afnd/L3-193-AFND.jff) · [`L3-193-AFND.json`](../../automatas/lista3-afnd/L3-193-AFND.json) · [`L3-193-AFND.xml`](../../automatas/lista3-afnd/L3-193-AFND.xml). Tipo según la definición: **AFND**, |Q| = 4, Σ = {0, 1}, 12 transiciones.

**Diseño.** Transcripción de la tabla.

| Estado | 0 | 1 |
|---|---|---|
| →A | ∅ | {B, C} |
| B | {A, D} | {B, C, D} |
| C | {C} | {A, C} |
| *D | {C} | {D} |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `10` | acepta | acepta | acepta |
| 2 | `11` | acepta | acepta | acepta |
| 3 | `1101` | acepta | acepta | acepta |
| 4 | `10000111` | acepta | acepta | acepta |
| 5 | `10111101010` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `100` | rechaza | rechaza | rechaza |
| 8 | `1000` | rechaza | rechaza | rechaza |
| 9 | `0110001` | rechaza | rechaza | rechaza |
| 10 | `10010000010` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `10`: {A} -1→ {B, C} -0→ {A, C, D} — ✔
  Árbol de cómputo: 3 caminos, 1 de aceptación:
    - A -1→ B -0→ D — ✔ acepta
    - A -1→ B -0→ A — ✘ termina fuera de F
    - A -1→ C -0→ C — ✘ termina fuera de F
2. `11`: {A} -1→ {B, C} -1→ {A, B, C, D} — ✔
  Árbol de cómputo: 5 caminos, 1 de aceptación:
    - A -1→ B -1→ D — ✔ acepta
    - A -1→ B -1→ B — ✘ termina fuera de F
    - A -1→ B -1→ C — ✘ termina fuera de F
    - A -1→ C -1→ A — ✘ termina fuera de F
    - A -1→ C -1→ C — ✘ termina fuera de F
3. `1101`: {A} -1→ {B, C} -1→ {A, B, C, D} -0→ {A, C, D} -1→ {A, B, C, D} — ✔
  Árbol de cómputo: 10 caminos, 1 de aceptación (se muestran 6):
    - A -1→ B -1→ B -0→ D -1→ D — ✔ acepta
    - A -1→ B -1→ B -0→ A -1→ B — ✘ termina fuera de F
    - A -1→ B -1→ B -0→ A -1→ C — ✘ termina fuera de F
    - A -1→ B -1→ C -0→ C -1→ A — ✘ termina fuera de F
    - A -1→ B -1→ C -0→ C -1→ C — ✘ termina fuera de F
    - A -1→ B -1→ D -0→ C -1→ A — ✘ termina fuera de F
4. `10000111`: {A} -1→ {B, C} -0→ {A, C, D} -0→ {C} -0→ {C} -0→ {C} -1→ {A, C} -1→ {A, B, C} -1→ {A, B, C, D} — ✔
  Árbol de cómputo: 19 caminos, 2 de aceptación (se muestran 6):
    - A -1→ B -0→ D -0→ C -0→ C -0→ C -1→ A -1→ B -1→ D — ✔ acepta
    - A -1→ C -0→ C -0→ C -0→ C -0→ C -1→ A -1→ B -1→ D — ✔ acepta
    - A -1→ B -0→ A — ✘ muere tras leer `10`
    - A -1→ B -0→ D -0→ C -0→ C -0→ C -1→ A -1→ B -1→ B — ✘ termina fuera de F
    - A -1→ B -0→ D -0→ C -0→ C -0→ C -1→ A -1→ B -1→ C — ✘ termina fuera de F
    - A -1→ B -0→ D -0→ C -0→ C -0→ C -1→ A -1→ C -1→ A — ✘ termina fuera de F
5. `10111101010`: {A} -1→ {B, C} -0→ {A, C, D} -1→ {A, B, C, D} -1→ {A, B, C, D} -1→ {A, B, C, D} -1→ {A, B, C, D} -0→ {A, C, D} -1→ {A, B, C, D} -0→ {A, C, D} -1→ {A, B, C, D} -0→ {A, C, D} — ✔
  Árbol de cómputo: 144 caminos, 8 de aceptación (se muestran 6):
    - A -1→ B -0→ A -1→ B -1→ B -1→ B -1→ B -0→ A -1→ B -0→ A -1→ B -0→ D — ✔ acepta
    - A -1→ B -0→ A -1→ B -1→ C -1→ A -1→ B -0→ A -1→ B -0→ A -1→ B -0→ D — ✔ acepta
    - A -1→ B -0→ A -1→ C -1→ A -1→ B -1→ B -0→ A -1→ B -0→ A -1→ B -0→ D — ✔ acepta
    - A -1→ B -0→ A -1→ B -1→ B -1→ B -1→ B -0→ A -1→ B -0→ A -1→ B -0→ A — ✘ termina fuera de F
    - A -1→ B -0→ A -1→ B -1→ B -1→ B -1→ B -0→ A -1→ B -0→ A -1→ C -0→ C — ✘ termina fuera de F
    - A -1→ B -0→ A -1→ B -1→ B -1→ B -1→ B -0→ A -1→ B -0→ D -1→ D -0→ C — ✘ termina fuera de F
6. λ: {A} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - A — ✘ termina fuera de F
7. `100`: {A} -1→ {B, C} -0→ {A, C, D} -0→ {C} — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - A -1→ B -0→ A — ✘ muere tras leer `10`
    - A -1→ B -0→ D -0→ C — ✘ termina fuera de F
    - A -1→ C -0→ C -0→ C — ✘ termina fuera de F
8. `1000`: {A} -1→ {B, C} -0→ {A, C, D} -0→ {C} -0→ {C} — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - A -1→ B -0→ A — ✘ muere tras leer `10`
    - A -1→ B -0→ D -0→ C -0→ C — ✘ termina fuera de F
    - A -1→ C -0→ C -0→ C -0→ C — ✘ termina fuera de F
9. `0110001`: {A} -0→ ∅ -1→ ∅ -1→ ∅ -0→ ∅ -0→ ∅ -0→ ∅ -1→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - A — ✘ muere tras leer λ
10. `10010000010`: {A} -1→ {B, C} -0→ {A, C, D} -0→ {C} -1→ {A, C} -0→ {C} -0→ {C} -0→ {C} -0→ {C} -0→ {C} -1→ {A, C} -0→ {C} — ✘
  Árbol de cómputo: 7 caminos, 0 de aceptación (se muestran 6):
    - A -1→ B -0→ A — ✘ muere tras leer `10`
    - A -1→ B -0→ D -0→ C -1→ A — ✘ muere tras leer `1001`
    - A -1→ B -0→ D -0→ C -1→ C -0→ C -0→ C -0→ C -0→ C -0→ C -1→ A — ✘ muere tras leer `1001000001`
    - A -1→ B -0→ D -0→ C -1→ C -0→ C -0→ C -0→ C -0→ C -0→ C -1→ C -0→ C — ✘ termina fuera de F
    - A -1→ C -0→ C -0→ C -1→ A — ✘ muere tras leer `1001`
    - A -1→ C -0→ C -0→ C -1→ C -0→ C -0→ C -0→ C -0→ C -0→ C -1→ A — ✘ muere tras leer `1001000001`

</details>

Simulación paso a paso en JFLAP con `10`: [ver captura](../../evidencias/jflap/pasos/L3-193-AFND.png).

**Conversión.** AFND (4 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 7 estados, [`L3-193-AFND-AFD.jff`](../../automatas/conversiones/L3-193-AFND-AFD.jff) ([.json](../../automatas/conversiones/L3-193-AFND-AFD.json), [.xml](../../automatas/conversiones/L3-193-AFND-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 8 estados, y el AFD mínimo (Hopcroft), 7. La cota es 2^4 = 16. Se verificó que los tres autómatas aceptan el mismo lenguaje.

#### AFD equivalente al 193. — `L3-193-AFD`

Archivos: [`L3-193-AFD.jff`](../../automatas/lista3-afnd/L3-193-AFD.jff) · [`L3-193-AFD.json`](../../automatas/lista3-afnd/L3-193-AFD.json) · [`L3-193-AFD.xml`](../../automatas/lista3-afnd/L3-193-AFD.xml). Tipo según la definición: **AFD**, |Q| = 8, Σ = {0, 1}, 16 transiciones.

**Diseño.** Construcción de subconjuntos: cada estado es el conjunto de estados del AFN alcanzables con el prefijo leído; acepta si contiene un estado final.

| Estado | 0 | 1 |
|---|---|---|
| →{A} | ∅ | {B,C} |
| ∅ | ∅ | ∅ |
| {B,C} | {A,C,D} | {A,B,C,D} |
| *{A,C,D} | {C} | {A,B,C,D} |
| *{A,B,C,D} | {A,C,D} | {A,B,C,D} |
| {C} | {C} | {A,C} |
| {A,C} | {C} | {A,B,C} |
| {A,B,C} | {A,C,D} | {A,B,C,D} |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `10` | acepta | acepta | acepta |
| 2 | `11` | acepta | acepta | acepta |
| 3 | `100111` | acepta | acepta | acepta |
| 4 | `1011010` | acepta | acepta | acepta |
| 5 | `111010010111` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `00` | rechaza | rechaza | rechaza |
| 8 | `0011` | rechaza | rechaza | rechaza |
| 9 | `1000000` | rechaza | rechaza | rechaza |
| 10 | `01111100010` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `10`: {A} -1→ {B,C} -0→ {A,C,D} — ✔
2. `11`: {A} -1→ {B,C} -1→ {A,B,C,D} — ✔
3. `100111`: {A} -1→ {B,C} -0→ {A,C,D} -0→ {C} -1→ {A,C} -1→ {A,B,C} -1→ {A,B,C,D} — ✔
4. `1011010`: {A} -1→ {B,C} -0→ {A,C,D} -1→ {A,B,C,D} -1→ {A,B,C,D} -0→ {A,C,D} -1→ {A,B,C,D} -0→ {A,C,D} — ✔
5. `111010010111`: {A} -1→ {B,C} -1→ {A,B,C,D} -1→ {A,B,C,D} -0→ {A,C,D} -1→ {A,B,C,D} -0→ {A,C,D} -0→ {C} -1→ {A,C} -0→ {C} -1→ {A,C} -1→ {A,B,C} -1→ {A,B,C,D} — ✔
6. λ: {A} — ✘
7. `00`: {A} -0→ ∅ -0→ ∅ — ✘
8. `0011`: {A} -0→ ∅ -0→ ∅ -1→ ∅ -1→ ∅ — ✘
9. `1000000`: {A} -1→ {B,C} -0→ {A,C,D} -0→ {C} -0→ {C} -0→ {C} -0→ {C} -0→ {C} — ✘
10. `01111100010`: {A} -0→ ∅ -1→ ∅ -1→ ∅ -1→ ∅ -1→ ∅ -1→ ∅ -0→ ∅ -0→ ∅ -0→ ∅ -1→ ∅ -0→ ∅ — ✘

</details>

Simulación paso a paso en JFLAP con `10`: [ver captura](../../evidencias/jflap/pasos/L3-193-AFD.png).

<a id="problema-3-194"></a>

## Lista 3, problema 194

**Enunciado.** AFN de la tabla 194.

**Clasificación: AFND.** El autómata dado tiene celdas con dos o más estados y celdas ∅: es un AFN; el AFD es su conversión. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

**Valores pedidos** (con los nombres de estado de la tabla):

- δ̂({A, C}, 0121) = {A, C}: {A, C} -0→ {A, B} -1→ {A, C} -2→ {A} -1→ {A, C}
- δ̂({B}, 20111) = ∅: {B} -2→ ∅ -0→ ∅ -1→ ∅ -1→ ∅ -1→ ∅
- δ̂({C}, 02112) = {A}: {C} -0→ {A, B} -2→ {A} -1→ {A, C} -1→ {A, B, C, D} -2→ {A}
- δ̂({A, B}, 0121) = {A, C}: {A, B} -0→ {A, B} -1→ {A, C} -2→ {A} -1→ {A, C}

#### AFN de la tabla 194. — `L3-194-AFND`

Archivos: [`L3-194-AFND.jff`](../../automatas/lista3-afnd/L3-194-AFND.jff) · [`L3-194-AFND.json`](../../automatas/lista3-afnd/L3-194-AFND.json) · [`L3-194-AFND.xml`](../../automatas/lista3-afnd/L3-194-AFND.xml). Tipo según la definición: **AFND**, |Q| = 4, Σ = {0, 1, 2}, 13 transiciones.

**Diseño.** Transcripción de la tabla.

| Estado | 0 | 1 | 2 |
|---|---|---|---|
| →A | {A, B} | {A, C} | {A} |
| B | ∅ | ∅ | ∅ |
| *C | {A, B} | {A, B, C, D} | ∅ |
| *D | {B} | {A} | ∅ |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `1` | acepta | acepta | acepta |
| 2 | `201` | acepta | acepta | acepta |
| 3 | `02221` | acepta | acepta | acepta |
| 4 | `2101001` | acepta | acepta | acepta |
| 5 | `211200221101` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `110` | rechaza | rechaza | rechaza |
| 8 | `1002` | rechaza | rechaza | rechaza |
| 9 | `2201002` | rechaza | rechaza | rechaza |
| 10 | `00011122112` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `1`: {A} -1→ {A, C} — ✔
  Árbol de cómputo: 2 caminos, 1 de aceptación:
    - A -1→ C — ✔ acepta
    - A -1→ A — ✘ termina fuera de F
2. `201`: {A} -2→ {A} -0→ {A, B} -1→ {A, C} — ✔
  Árbol de cómputo: 3 caminos, 1 de aceptación:
    - A -2→ A -0→ A -1→ C — ✔ acepta
    - A -2→ A -0→ A -1→ A — ✘ termina fuera de F
    - A -2→ A -0→ B — ✘ muere tras leer `20`
3. `02221`: {A} -0→ {A, B} -2→ {A} -2→ {A} -2→ {A} -1→ {A, C} — ✔
  Árbol de cómputo: 3 caminos, 1 de aceptación:
    - A -0→ A -2→ A -2→ A -2→ A -1→ C — ✔ acepta
    - A -0→ A -2→ A -2→ A -2→ A -1→ A — ✘ termina fuera de F
    - A -0→ B — ✘ muere tras leer `0`
4. `2101001`: {A} -2→ {A} -1→ {A, C} -0→ {A, B} -1→ {A, C} -0→ {A, B} -0→ {A, B} -1→ {A, C} — ✔
  Árbol de cómputo: 18 caminos, 4 de aceptación (se muestran 6):
    - A -2→ A -1→ A -0→ A -1→ A -0→ A -0→ A -1→ C — ✔ acepta
    - A -2→ A -1→ A -0→ A -1→ C -0→ A -0→ A -1→ C — ✔ acepta
    - A -2→ A -1→ C -0→ A -1→ A -0→ A -0→ A -1→ C — ✔ acepta
    - A -2→ A -1→ A -0→ A -1→ A -0→ A -0→ A -1→ A — ✘ termina fuera de F
    - A -2→ A -1→ A -0→ A -1→ A -0→ A -0→ B — ✘ muere tras leer `210100`
    - A -2→ A -1→ A -0→ A -1→ A -0→ B — ✘ muere tras leer `21010`
5. `211200221101`: {A} -2→ {A} -1→ {A, C} -1→ {A, B, C, D} -2→ {A} -0→ {A, B} -0→ {A, B} -2→ {A} -2→ {A} -1→ {A, C} -1→ {A, B, C, D} -0→ {A, B} -1→ {A, C} — ✔
  Árbol de cómputo: 36 caminos, 8 de aceptación (se muestran 6):
    - A -2→ A -1→ A -1→ A -2→ A -0→ A -0→ A -2→ A -2→ A -1→ A -1→ A -0→ A -1→ C — ✔ acepta
    - A -2→ A -1→ A -1→ A -2→ A -0→ A -0→ A -2→ A -2→ A -1→ A -1→ C -0→ A -1→ C — ✔ acepta
    - A -2→ A -1→ A -1→ A -2→ A -0→ A -0→ A -2→ A -2→ A -1→ C -1→ A -0→ A -1→ C — ✔ acepta
    - A -2→ A -1→ A -1→ A -2→ A -0→ A -0→ A -2→ A -2→ A -1→ A -1→ A -0→ A -1→ A — ✘ termina fuera de F
    - A -2→ A -1→ A -1→ A -2→ A -0→ A -0→ A -2→ A -2→ A -1→ A -1→ A -0→ B — ✘ muere tras leer `21120022110`
    - A -2→ A -1→ A -1→ A -2→ A -0→ A -0→ A -2→ A -2→ A -1→ A -1→ C -0→ A -1→ A — ✘ termina fuera de F
6. λ: {A} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - A — ✘ termina fuera de F
7. `110`: {A} -1→ {A, C} -1→ {A, B, C, D} -0→ {A, B} — ✘
  Árbol de cómputo: 10 caminos, 0 de aceptación (se muestran 6):
    - A -1→ A -1→ A -0→ A — ✘ termina fuera de F
    - A -1→ A -1→ A -0→ B — ✘ termina fuera de F
    - A -1→ A -1→ C -0→ A — ✘ termina fuera de F
    - A -1→ A -1→ C -0→ B — ✘ termina fuera de F
    - A -1→ C -1→ A -0→ A — ✘ termina fuera de F
    - A -1→ C -1→ A -0→ B — ✘ termina fuera de F
8. `1002`: {A} -1→ {A, C} -0→ {A, B} -0→ {A, B} -2→ {A} — ✘
  Árbol de cómputo: 6 caminos, 0 de aceptación:
    - A -1→ A -0→ A -0→ A -2→ A — ✘ termina fuera de F
    - A -1→ A -0→ A -0→ B — ✘ muere tras leer `100`
    - A -1→ A -0→ B — ✘ muere tras leer `10`
    - A -1→ C -0→ A -0→ A -2→ A — ✘ termina fuera de F
    - A -1→ C -0→ A -0→ B — ✘ muere tras leer `100`
    - A -1→ C -0→ B — ✘ muere tras leer `10`
9. `2201002`: {A} -2→ {A} -2→ {A} -0→ {A, B} -1→ {A, C} -0→ {A, B} -0→ {A, B} -2→ {A} — ✘
  Árbol de cómputo: 7 caminos, 0 de aceptación (se muestran 6):
    - A -2→ A -2→ A -0→ A -1→ A -0→ A -0→ A -2→ A — ✘ termina fuera de F
    - A -2→ A -2→ A -0→ A -1→ A -0→ A -0→ B — ✘ muere tras leer `220100`
    - A -2→ A -2→ A -0→ A -1→ A -0→ B — ✘ muere tras leer `22010`
    - A -2→ A -2→ A -0→ A -1→ C -0→ A -0→ A -2→ A — ✘ termina fuera de F
    - A -2→ A -2→ A -0→ A -1→ C -0→ A -0→ B — ✘ muere tras leer `220100`
    - A -2→ A -2→ A -0→ A -1→ C -0→ B — ✘ muere tras leer `22010`
10. `00011122112`: {A} -0→ {A, B} -0→ {A, B} -0→ {A, B} -1→ {A, C} -1→ {A, B, C, D} -1→ {A, B, C, D} -2→ {A} -2→ {A} -1→ {A, C} -1→ {A, B, C, D} -2→ {A} — ✘
  Árbol de cómputo: 42 caminos, 0 de aceptación (se muestran 6):
    - A -0→ A -0→ A -0→ A -1→ A -1→ A -1→ A -2→ A -2→ A -1→ A -1→ A -2→ A — ✘ termina fuera de F
    - A -0→ A -0→ A -0→ A -1→ A -1→ A -1→ A -2→ A -2→ A -1→ A -1→ C — ✘ muere tras leer `0001112211`
    - A -0→ A -0→ A -0→ A -1→ A -1→ A -1→ A -2→ A -2→ A -1→ C -1→ A -2→ A — ✘ termina fuera de F
    - A -0→ A -0→ A -0→ A -1→ A -1→ A -1→ A -2→ A -2→ A -1→ C -1→ B — ✘ muere tras leer `0001112211`
    - A -0→ A -0→ A -0→ A -1→ A -1→ A -1→ A -2→ A -2→ A -1→ C -1→ C — ✘ muere tras leer `0001112211`
    - A -0→ A -0→ A -0→ A -1→ A -1→ A -1→ A -2→ A -2→ A -1→ C -1→ D — ✘ muere tras leer `0001112211`

</details>

Simulación paso a paso en JFLAP con `201`: [ver captura](../../evidencias/jflap/pasos/L3-194-AFND.png).

**Conversión.** AFND (4 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 4 estados, [`L3-194-AFND-AFD.jff`](../../automatas/conversiones/L3-194-AFND-AFD.jff) ([.json](../../automatas/conversiones/L3-194-AFND-AFD.json), [.xml](../../automatas/conversiones/L3-194-AFND-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 4 estados, y el AFD mínimo (Hopcroft), 2. La cota es 2^4 = 16. Se verificó que los tres autómatas aceptan el mismo lenguaje.

#### AFD equivalente al 194. — `L3-194-AFD`

Archivos: [`L3-194-AFD.jff`](../../automatas/lista3-afnd/L3-194-AFD.jff) · [`L3-194-AFD.json`](../../automatas/lista3-afnd/L3-194-AFD.json) · [`L3-194-AFD.xml`](../../automatas/lista3-afnd/L3-194-AFD.xml). Tipo según la definición: **AFD**, |Q| = 4, Σ = {0, 1, 2}, 12 transiciones.

**Diseño.** Construcción de subconjuntos: cada estado es el conjunto de estados del AFN alcanzables con el prefijo leído; acepta si contiene un estado final.

| Estado | 0 | 1 | 2 |
|---|---|---|---|
| →{A} | {A,B} | {A,C} | {A} |
| {A,B} | {A,B} | {A,C} | {A} |
| *{A,C} | {A,B} | {A,B,C,D} | {A} |
| *{A,B,C,D} | {A,B} | {A,B,C,D} | {A} |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `1` | acepta | acepta | acepta |
| 2 | `001` | acepta | acepta | acepta |
| 3 | `21201` | acepta | acepta | acepta |
| 4 | `22011021` | acepta | acepta | acepta |
| 5 | `10222100111` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `12` | rechaza | rechaza | rechaza |
| 8 | `0010` | rechaza | rechaza | rechaza |
| 9 | `1010212` | rechaza | rechaza | rechaza |
| 10 | `102101001110` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `1`: {A} -1→ {A,C} — ✔
2. `001`: {A} -0→ {A,B} -0→ {A,B} -1→ {A,C} — ✔
3. `21201`: {A} -2→ {A} -1→ {A,C} -2→ {A} -0→ {A,B} -1→ {A,C} — ✔
4. `22011021`: {A} -2→ {A} -2→ {A} -0→ {A,B} -1→ {A,C} -1→ {A,B,C,D} -0→ {A,B} -2→ {A} -1→ {A,C} — ✔
5. `10222100111`: {A} -1→ {A,C} -0→ {A,B} -2→ {A} -2→ {A} -2→ {A} -1→ {A,C} -0→ {A,B} -0→ {A,B} -1→ {A,C} -1→ {A,B,C,D} -1→ {A,B,C,D} — ✔
6. λ: {A} — ✘
7. `12`: {A} -1→ {A,C} -2→ {A} — ✘
8. `0010`: {A} -0→ {A,B} -0→ {A,B} -1→ {A,C} -0→ {A,B} — ✘
9. `1010212`: {A} -1→ {A,C} -0→ {A,B} -1→ {A,C} -0→ {A,B} -2→ {A} -1→ {A,C} -2→ {A} — ✘
10. `102101001110`: {A} -1→ {A,C} -0→ {A,B} -2→ {A} -1→ {A,C} -0→ {A,B} -1→ {A,C} -0→ {A,B} -0→ {A,B} -1→ {A,C} -1→ {A,B,C,D} -1→ {A,B,C,D} -0→ {A,B} — ✘

</details>

Simulación paso a paso en JFLAP con `001`: [ver captura](../../evidencias/jflap/pasos/L3-194-AFD.png).

<a id="problema-3-195"></a>

## Lista 3, problema 195

**Enunciado.** AFN de la tabla 195.

**Clasificación: AFND.** El autómata dado tiene celdas con dos o más estados y celdas ∅: es un AFN; el AFD es su conversión. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

**Valores pedidos** (con los nombres de estado de la tabla):

- δ̂({A}, 10010) = {A, B}: {A} -1→ {A} -0→ {A, B} -0→ {A, B} -1→ {A, C} -0→ {A, B}
- δ̂({A, D}, 0110) = {A, B, D}: {A, D} -0→ {A, B, D} -1→ {A, C, E} -1→ {A, C, D} -0→ {A, B, D}
- δ̂({B, E}, 0100) = {A, B, D}: {B, E} -0→ {A, E} -1→ {A, C, D} -0→ {A, B, D} -0→ {A, B, D}
- δ̂({B, C, D}, 10100) = {A, B, D, E}: {B, C, D} -1→ {C, D, E} -0→ {A, D, E} -1→ {A, C, D, E} -0→ {A, B, D, E} -0→ {A, B, D, E}

#### AFN de la tabla 195. — `L3-195-AFND`

Archivos: [`L3-195-AFND.jff`](../../automatas/lista3-afnd/L3-195-AFND.jff) · [`L3-195-AFND.json`](../../automatas/lista3-afnd/L3-195-AFND.json) · [`L3-195-AFND.xml`](../../automatas/lista3-afnd/L3-195-AFND.xml). Tipo según la definición: **AFND**, |Q| = 5, Σ = {0, 1}, 12 transiciones.

**Diseño.** Transcripción de la tabla.

| Estado | 0 | 1 |
|---|---|---|
| →A | {A, B} | {A} |
| B | {A} | {C} |
| *C | {A} | {D} |
| D | {D} | {E} |
| *E | {E} | {C, D} |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `01` | acepta | acepta | acepta |
| 2 | `001` | acepta | acepta | acepta |
| 3 | `1101` | acepta | acepta | acepta |
| 4 | `1011101` | acepta | acepta | acepta |
| 5 | `01011101110` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `11` | rechaza | rechaza | rechaza |
| 8 | `0100` | rechaza | rechaza | rechaza |
| 9 | `0011110` | rechaza | rechaza | rechaza |
| 10 | `00011011000` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `01`: {A} -0→ {A, B} -1→ {A, C} — ✔
  Árbol de cómputo: 2 caminos, 1 de aceptación:
    - A -0→ B -1→ C — ✔ acepta
    - A -0→ A -1→ A — ✘ termina fuera de F
2. `001`: {A} -0→ {A, B} -0→ {A, B} -1→ {A, C} — ✔
  Árbol de cómputo: 3 caminos, 1 de aceptación:
    - A -0→ A -0→ B -1→ C — ✔ acepta
    - A -0→ A -0→ A -1→ A — ✘ termina fuera de F
    - A -0→ B -0→ A -1→ A — ✘ termina fuera de F
3. `1101`: {A} -1→ {A} -1→ {A} -0→ {A, B} -1→ {A, C} — ✔
  Árbol de cómputo: 2 caminos, 1 de aceptación:
    - A -1→ A -1→ A -0→ B -1→ C — ✔ acepta
    - A -1→ A -1→ A -0→ A -1→ A — ✘ termina fuera de F
4. `1011101`: {A} -1→ {A} -0→ {A, B} -1→ {A, C} -1→ {A, D} -1→ {A, E} -0→ {A, B, E} -1→ {A, C, D} — ✔
  Árbol de cómputo: 4 caminos, 2 de aceptación:
    - A -1→ A -0→ A -1→ A -1→ A -1→ A -0→ B -1→ C — ✔ acepta
    - A -1→ A -0→ B -1→ C -1→ D -1→ E -0→ E -1→ C — ✔ acepta
    - A -1→ A -0→ A -1→ A -1→ A -1→ A -0→ A -1→ A — ✘ termina fuera de F
    - A -1→ A -0→ B -1→ C -1→ D -1→ E -0→ E -1→ D — ✘ termina fuera de F
5. `01011101110`: {A} -0→ {A, B} -1→ {A, C} -0→ {A, B} -1→ {A, C} -1→ {A, D} -1→ {A, E} -0→ {A, B, E} -1→ {A, C, D} -1→ {A, D, E} -1→ {A, C, D, E} -0→ {A, B, D, E} — ✔
  Árbol de cómputo: 9 caminos, 3 de aceptación (se muestran 6):
    - A -0→ A -1→ A -0→ A -1→ A -1→ A -1→ A -0→ B -1→ C -1→ D -1→ E -0→ E — ✔ acepta
    - A -0→ A -1→ A -0→ B -1→ C -1→ D -1→ E -0→ E -1→ C -1→ D -1→ E -0→ E — ✔ acepta
    - A -0→ B -1→ C -0→ A -1→ A -1→ A -1→ A -0→ B -1→ C -1→ D -1→ E -0→ E — ✔ acepta
    - A -0→ A -1→ A -0→ A -1→ A -1→ A -1→ A -0→ A -1→ A -1→ A -1→ A -0→ A — ✘ termina fuera de F
    - A -0→ A -1→ A -0→ A -1→ A -1→ A -1→ A -0→ A -1→ A -1→ A -1→ A -0→ B — ✘ termina fuera de F
    - A -0→ A -1→ A -0→ B -1→ C -1→ D -1→ E -0→ E -1→ D -1→ E -1→ C -0→ A — ✘ termina fuera de F
6. λ: {A} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - A — ✘ termina fuera de F
7. `11`: {A} -1→ {A} -1→ {A} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - A -1→ A -1→ A — ✘ termina fuera de F
8. `0100`: {A} -0→ {A, B} -1→ {A, C} -0→ {A, B} -0→ {A, B} — ✘
  Árbol de cómputo: 5 caminos, 0 de aceptación:
    - A -0→ A -1→ A -0→ A -0→ A — ✘ termina fuera de F
    - A -0→ A -1→ A -0→ A -0→ B — ✘ termina fuera de F
    - A -0→ A -1→ A -0→ B -0→ A — ✘ termina fuera de F
    - A -0→ B -1→ C -0→ A -0→ A — ✘ termina fuera de F
    - A -0→ B -1→ C -0→ A -0→ B — ✘ termina fuera de F
9. `0011110`: {A} -0→ {A, B} -0→ {A, B} -1→ {A, C} -1→ {A, D} -1→ {A, E} -1→ {A, C, D} -0→ {A, B, D} — ✘
  Árbol de cómputo: 6 caminos, 0 de aceptación:
    - A -0→ A -0→ A -1→ A -1→ A -1→ A -1→ A -0→ A — ✘ termina fuera de F
    - A -0→ A -0→ A -1→ A -1→ A -1→ A -1→ A -0→ B — ✘ termina fuera de F
    - A -0→ A -0→ B -1→ C -1→ D -1→ E -1→ C -0→ A — ✘ termina fuera de F
    - A -0→ A -0→ B -1→ C -1→ D -1→ E -1→ D -0→ D — ✘ termina fuera de F
    - A -0→ B -0→ A -1→ A -1→ A -1→ A -1→ A -0→ A — ✘ termina fuera de F
    - A -0→ B -0→ A -1→ A -1→ A -1→ A -1→ A -0→ B — ✘ termina fuera de F
10. `00011011000`: {A} -0→ {A, B} -0→ {A, B} -0→ {A, B} -1→ {A, C} -1→ {A, D} -0→ {A, B, D} -1→ {A, C, E} -1→ {A, C, D} -0→ {A, B, D} -0→ {A, B, D} -0→ {A, B, D} — ✘
  Árbol de cómputo: 26 caminos, 0 de aceptación (se muestran 6):
    - A -0→ A -0→ A -0→ A -1→ A -1→ A -0→ A -1→ A -1→ A -0→ A -0→ A -0→ A — ✘ termina fuera de F
    - A -0→ A -0→ A -0→ A -1→ A -1→ A -0→ A -1→ A -1→ A -0→ A -0→ A -0→ B — ✘ termina fuera de F
    - A -0→ A -0→ A -0→ A -1→ A -1→ A -0→ A -1→ A -1→ A -0→ A -0→ B -0→ A — ✘ termina fuera de F
    - A -0→ A -0→ A -0→ A -1→ A -1→ A -0→ A -1→ A -1→ A -0→ B -0→ A -0→ A — ✘ termina fuera de F
    - A -0→ A -0→ A -0→ A -1→ A -1→ A -0→ A -1→ A -1→ A -0→ B -0→ A -0→ B — ✘ termina fuera de F
    - A -0→ A -0→ A -0→ A -1→ A -1→ A -0→ B -1→ C -1→ D -0→ D -0→ D -0→ D — ✘ termina fuera de F

</details>

Simulación paso a paso en JFLAP con `01`: [ver captura](../../evidencias/jflap/pasos/L3-195-AFND.png).

**Conversión.** AFND (5 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 12 estados, [`L3-195-AFND-AFD.jff`](../../automatas/conversiones/L3-195-AFND-AFD.jff) ([.json](../../automatas/conversiones/L3-195-AFND-AFD.json), [.xml](../../automatas/conversiones/L3-195-AFND-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 12 estados, y el AFD mínimo (Hopcroft), 7. La cota es 2^5 = 32. Se verificó que los tres autómatas aceptan el mismo lenguaje.

#### AFD equivalente al 195. — `L3-195-AFD`

Archivos: [`L3-195-AFD.jff`](../../automatas/lista3-afnd/L3-195-AFD.jff) · [`L3-195-AFD.json`](../../automatas/lista3-afnd/L3-195-AFD.json) · [`L3-195-AFD.xml`](../../automatas/lista3-afnd/L3-195-AFD.xml). Tipo según la definición: **AFD**, |Q| = 12, Σ = {0, 1}, 24 transiciones.

**Diseño.** Construcción de subconjuntos: cada estado es el conjunto de estados del AFN alcanzables con el prefijo leído; acepta si contiene un estado final.

| Estado | 0 | 1 |
|---|---|---|
| →{A} | {A,B} | {A} |
| {A,B} | {A,B} | {A,C} |
| *{A,C} | {A,B} | {A,D} |
| {A,D} | {A,B,D} | {A,E} |
| {A,B,D} | {A,B,D} | {A,C,E} |
| *{A,E} | {A,B,E} | {A,C,D} |
| *{A,C,E} | {A,B,E} | {A,C,D} |
| *{A,B,E} | {A,B,E} | {A,C,D} |
| *{A,C,D} | {A,B,D} | {A,D,E} |
| *{A,D,E} | {A,B,D,E} | {A,C,D,E} |
| *{A,B,D,E} | {A,B,D,E} | {A,C,D,E} |
| *{A,C,D,E} | {A,B,D,E} | {A,C,D,E} |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `01` | acepta | acepta | acepta |
| 2 | `101` | acepta | acepta | acepta |
| 3 | `0111` | acepta | acepta | acepta |
| 4 | `00011001` | acepta | acepta | acepta |
| 5 | `010100110001` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `00` | rechaza | rechaza | rechaza |
| 8 | `011110` | rechaza | rechaza | rechaza |
| 9 | `110111010` | rechaza | rechaza | rechaza |
| 10 | `1011110000110` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `01`: {A} -0→ {A,B} -1→ {A,C} — ✔
2. `101`: {A} -1→ {A} -0→ {A,B} -1→ {A,C} — ✔
3. `0111`: {A} -0→ {A,B} -1→ {A,C} -1→ {A,D} -1→ {A,E} — ✔
4. `00011001`: {A} -0→ {A,B} -0→ {A,B} -0→ {A,B} -1→ {A,C} -1→ {A,D} -0→ {A,B,D} -0→ {A,B,D} -1→ {A,C,E} — ✔
5. `010100110001`: {A} -0→ {A,B} -1→ {A,C} -0→ {A,B} -1→ {A,C} -0→ {A,B} -0→ {A,B} -1→ {A,C} -1→ {A,D} -0→ {A,B,D} -0→ {A,B,D} -0→ {A,B,D} -1→ {A,C,E} — ✔
6. λ: {A} — ✘
7. `00`: {A} -0→ {A,B} -0→ {A,B} — ✘
8. `011110`: {A} -0→ {A,B} -1→ {A,C} -1→ {A,D} -1→ {A,E} -1→ {A,C,D} -0→ {A,B,D} — ✘
9. `110111010`: {A} -1→ {A} -1→ {A} -0→ {A,B} -1→ {A,C} -1→ {A,D} -1→ {A,E} -0→ {A,B,E} -1→ {A,C,D} -0→ {A,B,D} — ✘
10. `1011110000110`: {A} -1→ {A} -0→ {A,B} -1→ {A,C} -1→ {A,D} -1→ {A,E} -1→ {A,C,D} -0→ {A,B,D} -0→ {A,B,D} -0→ {A,B,D} -0→ {A,B,D} -1→ {A,C,E} -1→ {A,C,D} -0→ {A,B,D} — ✘

</details>

Simulación paso a paso en JFLAP con `01`: [ver captura](../../evidencias/jflap/pasos/L3-195-AFD.png).

<a id="problema-3-260"></a>

## Lista 3, problema 260

**Enunciado.** AFN de la tabla 260.

**Clasificación: AFND.** El autómata de partida es un AFN (varios destinos por símbolo); el AFD es su conversión. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### AFN de la tabla 260. — `L3-260-AFND`

Archivos: [`L3-260-AFND.jff`](../../automatas/lista3-afnd/L3-260-AFND.jff) · [`L3-260-AFND.json`](../../automatas/lista3-afnd/L3-260-AFND.json) · [`L3-260-AFND.xml`](../../automatas/lista3-afnd/L3-260-AFND.xml). Tipo según la definición: **AFND**, |Q| = 5, Σ = {0, 1}, 15 transiciones.

**Diseño.** Transcripción de la tabla.

| Estado | 0 | 1 |
|---|---|---|
| →A | ∅ | {B, C} |
| B | {A, B, D} | {C, D} |
| C | {A, C} | {A, E} |
| *D | ∅ | {D, E} |
| E | {A, E} | ∅ |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `10` | acepta | acepta | acepta |
| 2 | `11` | acepta | acepta | acepta |
| 3 | `11010` | acepta | acepta | — |
| 4 | `1000000` | acepta | acepta | acepta |
| 5 | `10011011000` | acepta | acepta | — |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `01` | rechaza | rechaza | — |
| 8 | `1101` | rechaza | rechaza | rechaza |
| 9 | `110001` | rechaza | rechaza | — |
| 10 | `0010010` | rechaza | rechaza | — |

<details><summary>Recorrido completo de cada cadena</summary>

1. `10`: {A} -1→ {B, C} -0→ {A, B, C, D} — ✔
  Árbol de cómputo: 5 caminos, 1 de aceptación:
    - A -1→ B -0→ D — ✔ acepta
    - A -1→ B -0→ A — ✘ termina fuera de F
    - A -1→ B -0→ B — ✘ termina fuera de F
    - A -1→ C -0→ A — ✘ termina fuera de F
    - A -1→ C -0→ C — ✘ termina fuera de F
2. `11`: {A} -1→ {B, C} -1→ {A, C, D, E} — ✔
  Árbol de cómputo: 4 caminos, 1 de aceptación:
    - A -1→ B -1→ D — ✔ acepta
    - A -1→ B -1→ C — ✘ termina fuera de F
    - A -1→ C -1→ A — ✘ termina fuera de F
    - A -1→ C -1→ E — ✘ termina fuera de F
3. `11010`: {A} -1→ {B, C} -1→ {A, C, D, E} -0→ {A, C, E} -1→ {A, B, C, E} -0→ {A, B, C, D, E} — ✔
  Árbol de cómputo: 16 caminos, 2 de aceptación (se muestran 6):
    - A -1→ B -1→ C -0→ A -1→ B -0→ D — ✔ acepta
    - A -1→ C -1→ E -0→ A -1→ B -0→ D — ✔ acepta
    - A -1→ B -1→ C -0→ A -1→ B -0→ A — ✘ termina fuera de F
    - A -1→ B -1→ C -0→ A -1→ B -0→ B — ✘ termina fuera de F
    - A -1→ B -1→ C -0→ A -1→ C -0→ A — ✘ termina fuera de F
    - A -1→ B -1→ C -0→ A -1→ C -0→ C — ✘ termina fuera de F
4. `1000000`: {A} -1→ {B, C} -0→ {A, B, C, D} -0→ {A, B, C, D} -0→ {A, B, C, D} -0→ {A, B, C, D} -0→ {A, B, C, D} -0→ {A, B, C, D} — ✔
  Árbol de cómputo: 20 caminos, 1 de aceptación (se muestran 6):
    - A -1→ B -0→ B -0→ B -0→ B -0→ B -0→ B -0→ D — ✔ acepta
    - A -1→ B -0→ A — ✘ muere tras leer `10`
    - A -1→ B -0→ B -0→ A — ✘ muere tras leer `100`
    - A -1→ B -0→ B -0→ B -0→ A — ✘ muere tras leer `1000`
    - A -1→ B -0→ B -0→ B -0→ B -0→ A — ✘ muere tras leer `10000`
    - A -1→ B -0→ B -0→ B -0→ B -0→ B -0→ A — ✘ muere tras leer `100000`
5. `10011011000`: {A} -1→ {B, C} -0→ {A, B, C, D} -0→ {A, B, C, D} -1→ {A, B, C, D, E} -1→ {A, B, C, D, E} -0→ {A, B, C, D, E} -1→ {A, B, C, D, E} -1→ {A, B, C, D, E} -0→ {A, B, C, D, E} -0→ {A, B, C, D, E} -0→ {A, B, C, D, E} — ✔
  Árbol de cómputo: 159 caminos, 3 de aceptación (se muestran 6):
    - A -1→ B -0→ B -0→ A -1→ B -1→ C -0→ C -1→ A -1→ B -0→ B -0→ B -0→ D — ✔ acepta
    - A -1→ C -0→ C -0→ A -1→ B -1→ C -0→ C -1→ A -1→ B -0→ B -0→ B -0→ D — ✔ acepta
    - A -1→ C -0→ C -0→ C -1→ A -1→ C -0→ C -1→ A -1→ B -0→ B -0→ B -0→ D — ✔ acepta
    - A -1→ B -0→ A — ✘ muere tras leer `10`
    - A -1→ B -0→ B -0→ A -1→ B -1→ C -0→ A -1→ B -1→ C -0→ A — ✘ muere tras leer `100110110`
    - A -1→ B -0→ B -0→ A -1→ B -1→ C -0→ A -1→ B -1→ C -0→ C -0→ A — ✘ muere tras leer `1001101100`
6. λ: {A} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - A — ✘ termina fuera de F
7. `01`: {A} -0→ ∅ -1→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - A — ✘ muere tras leer λ
8. `1101`: {A} -1→ {B, C} -1→ {A, C, D, E} -0→ {A, C, E} -1→ {A, B, C, E} — ✘
  Árbol de cómputo: 9 caminos, 0 de aceptación (se muestran 6):
    - A -1→ B -1→ C -0→ A -1→ B — ✘ termina fuera de F
    - A -1→ B -1→ C -0→ A -1→ C — ✘ termina fuera de F
    - A -1→ B -1→ C -0→ C -1→ A — ✘ termina fuera de F
    - A -1→ B -1→ C -0→ C -1→ E — ✘ termina fuera de F
    - A -1→ B -1→ D — ✘ muere tras leer `11`
    - A -1→ C -1→ A — ✘ muere tras leer `11`
9. `110001`: {A} -1→ {B, C} -1→ {A, C, D, E} -0→ {A, C, E} -0→ {A, C, E} -0→ {A, C, E} -1→ {A, B, C, E} — ✘
  Árbol de cómputo: 13 caminos, 0 de aceptación (se muestran 6):
    - A -1→ B -1→ C -0→ A — ✘ muere tras leer `110`
    - A -1→ B -1→ C -0→ C -0→ A — ✘ muere tras leer `1100`
    - A -1→ B -1→ C -0→ C -0→ C -0→ A -1→ B — ✘ termina fuera de F
    - A -1→ B -1→ C -0→ C -0→ C -0→ A -1→ C — ✘ termina fuera de F
    - A -1→ B -1→ C -0→ C -0→ C -0→ C -1→ A — ✘ termina fuera de F
    - A -1→ B -1→ C -0→ C -0→ C -0→ C -1→ E — ✘ termina fuera de F
10. `0010010`: {A} -0→ ∅ -0→ ∅ -1→ ∅ -0→ ∅ -0→ ∅ -1→ ∅ -0→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - A — ✘ muere tras leer λ

</details>

Simulación paso a paso en JFLAP con `10`: [ver captura](../../evidencias/jflap/pasos/L3-260-AFND.png).

**Conversión.** AFND (5 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 7 estados, [`L3-260-AFND-AFD.jff`](../../automatas/conversiones/L3-260-AFND-AFD.jff) ([.json](../../automatas/conversiones/L3-260-AFND-AFD.json), [.xml](../../automatas/conversiones/L3-260-AFND-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 8 estados, y el AFD mínimo (Hopcroft), 7. La cota es 2^5 = 32. Se verificó que los tres autómatas aceptan el mismo lenguaje.

#### AFD equivalente al 260. — `L3-260-AFD`

Archivos: [`L3-260-AFD.jff`](../../automatas/lista3-afnd/L3-260-AFD.jff) · [`L3-260-AFD.json`](../../automatas/lista3-afnd/L3-260-AFD.json) · [`L3-260-AFD.xml`](../../automatas/lista3-afnd/L3-260-AFD.xml). Tipo según la definición: **AFD**, |Q| = 8, Σ = {0, 1}, 16 transiciones.

**Diseño.** Construcción de subconjuntos: cada estado es el conjunto de estados del AFN alcanzables con el prefijo leído; acepta si contiene un estado final.

| Estado | 0 | 1 |
|---|---|---|
| →{A} | ∅ | {B,C} |
| ∅ | ∅ | ∅ |
| {B,C} | {A,B,C,D} | {A,C,D,E} |
| *{A,B,C,D} | {A,B,C,D} | {A,B,C,D,E} |
| *{A,C,D,E} | {A,C,E} | {A,B,C,D,E} |
| *{A,B,C,D,E} | {A,B,C,D,E} | {A,B,C,D,E} |
| {A,C,E} | {A,C,E} | {A,B,C,E} |
| {A,B,C,E} | {A,B,C,D,E} | {A,B,C,D,E} |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `10` | acepta | acepta | acepta |
| 2 | `11` | acepta | acepta | acepta |
| 3 | `1110` | acepta | acepta | — |
| 4 | `110000010` | acepta | acepta | — |
| 5 | `11111111100` | acepta | acepta | — |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `110` | rechaza | rechaza | — |
| 8 | `0100` | rechaza | rechaza | — |
| 9 | `1101` | rechaza | rechaza | rechaza |
| 10 | `0100001` | rechaza | rechaza | — |

<details><summary>Recorrido completo de cada cadena</summary>

1. `10`: {A} -1→ {B,C} -0→ {A,B,C,D} — ✔
2. `11`: {A} -1→ {B,C} -1→ {A,C,D,E} — ✔
3. `1110`: {A} -1→ {B,C} -1→ {A,C,D,E} -1→ {A,B,C,D,E} -0→ {A,B,C,D,E} — ✔
4. `110000010`: {A} -1→ {B,C} -1→ {A,C,D,E} -0→ {A,C,E} -0→ {A,C,E} -0→ {A,C,E} -0→ {A,C,E} -0→ {A,C,E} -1→ {A,B,C,E} -0→ {A,B,C,D,E} — ✔
5. `11111111100`: {A} -1→ {B,C} -1→ {A,C,D,E} -1→ {A,B,C,D,E} -1→ {A,B,C,D,E} -1→ {A,B,C,D,E} -1→ {A,B,C,D,E} -1→ {A,B,C,D,E} -1→ {A,B,C,D,E} -1→ {A,B,C,D,E} -0→ {A,B,C,D,E} -0→ {A,B,C,D,E} — ✔
6. λ: {A} — ✘
7. `110`: {A} -1→ {B,C} -1→ {A,C,D,E} -0→ {A,C,E} — ✘
8. `0100`: {A} -0→ ∅ -1→ ∅ -0→ ∅ -0→ ∅ — ✘
9. `1101`: {A} -1→ {B,C} -1→ {A,C,D,E} -0→ {A,C,E} -1→ {A,B,C,E} — ✘
10. `0100001`: {A} -0→ ∅ -1→ ∅ -0→ ∅ -0→ ∅ -0→ ∅ -0→ ∅ -1→ ∅ — ✘

</details>

Simulación paso a paso en JFLAP con `10`: [ver captura](../../evidencias/jflap/pasos/L3-260-AFD.png).

#### AFD del 260, minimizado. — `L3-260-AFD-min`

Archivos: [`L3-260-AFD-min.jff`](../../automatas/lista3-afnd/L3-260-AFD-min.jff) · [`L3-260-AFD-min.json`](../../automatas/lista3-afnd/L3-260-AFD-min.json) · [`L3-260-AFD-min.xml`](../../automatas/lista3-afnd/L3-260-AFD-min.xml). Tipo según la definición: **AFD**, |Q| = 7, Σ = {0, 1}, 14 transiciones.

**Diseño.** Partición: se inicia con {no finales, finales} y se separan los estados que van a bloques distintos con algún símbolo, hasta estabilizar; cada estado del resultado representa un bloque de estados equivalentes.

| Estado | 0 | 1 |
|---|---|---|
| →{A} | ∅ | {B,C} |
| ∅ | ∅ | ∅ |
| {B,C} | {{A,B,C,D},{A,B,C,D,E}} | {A,C,D,E} |
| *{{A,B,C,D},{A,B,C,D,E}} | {{A,B,C,D},{A,B,C,D,E}} | {{A,B,C,D},{A,B,C,D,E}} |
| *{A,C,D,E} | {A,C,E} | {{A,B,C,D},{A,B,C,D,E}} |
| {A,C,E} | {A,C,E} | {A,B,C,E} |
| {A,B,C,E} | {{A,B,C,D},{A,B,C,D,E}} | {{A,B,C,D},{A,B,C,D,E}} |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `10` | acepta | acepta | acepta |
| 2 | `11` | acepta | acepta | acepta |
| 3 | `1011` | acepta | acepta | acepta |
| 4 | `1010110` | acepta | acepta | acepta |
| 5 | `10100000001` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `01` | rechaza | rechaza | rechaza |
| 8 | `0111` | rechaza | rechaza | rechaza |
| 9 | `1101` | rechaza | rechaza | rechaza |
| 10 | `0010110` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `10`: {A} -1→ {B,C} -0→ {{A,B,C,D},{A,B,C,D,E}} — ✔
2. `11`: {A} -1→ {B,C} -1→ {A,C,D,E} — ✔
3. `1011`: {A} -1→ {B,C} -0→ {{A,B,C,D},{A,B,C,D,E}} -1→ {{A,B,C,D},{A,B,C,D,E}} -1→ {{A,B,C,D},{A,B,C,D,E}} — ✔
4. `1010110`: {A} -1→ {B,C} -0→ {{A,B,C,D},{A,B,C,D,E}} -1→ {{A,B,C,D},{A,B,C,D,E}} -0→ {{A,B,C,D},{A,B,C,D,E}} -1→ {{A,B,C,D},{A,B,C,D,E}} -1→ {{A,B,C,D},{A,B,C,D,E}} -0→ {{A,B,C,D},{A,B,C,D,E}} — ✔
5. `10100000001`: {A} -1→ {B,C} -0→ {{A,B,C,D},{A,B,C,D,E}} -1→ {{A,B,C,D},{A,B,C,D,E}} -0→ {{A,B,C,D},{A,B,C,D,E}} -0→ {{A,B,C,D},{A,B,C,D,E}} -0→ {{A,B,C,D},{A,B,C,D,E}} -0→ {{A,B,C,D},{A,B,C,D,E}} -0→ {{A,B,C,D},{A,B,C,D,E}} -0→ {{A,B,C,D},{A,B,C,D,E}} -0→ {{A,B,C,D},{A,B,C,D,E}} -1→ {{A,B,C,D},{A,B,C,D,E}} — ✔
6. λ: {A} — ✘
7. `01`: {A} -0→ ∅ -1→ ∅ — ✘
8. `0111`: {A} -0→ ∅ -1→ ∅ -1→ ∅ -1→ ∅ — ✘
9. `1101`: {A} -1→ {B,C} -1→ {A,C,D,E} -0→ {A,C,E} -1→ {A,B,C,E} — ✘
10. `0010110`: {A} -0→ ∅ -0→ ∅ -1→ ∅ -0→ ∅ -1→ ∅ -1→ ∅ -0→ ∅ — ✘

</details>

Simulación paso a paso en JFLAP con `10`: [ver captura](../../evidencias/jflap/pasos/L3-260-AFD-min.png).

<a id="problema-3-261"></a>

## Lista 3, problema 261

**Enunciado.** AFN de la figura 261.

**Clasificación: AFND.** El autómata de partida es un AFN (varios destinos por símbolo); el AFD es su conversión. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### AFN de la figura 261. — `L3-261-AFND`

Archivos: [`L3-261-AFND.jff`](../../automatas/lista3-afnd/L3-261-AFND.jff) · [`L3-261-AFND.json`](../../automatas/lista3-afnd/L3-261-AFND.json) · [`L3-261-AFND.xml`](../../automatas/lista3-afnd/L3-261-AFND.xml). Tipo según la definición: **AFND**, |Q| = 5, Σ = {0, 1}, 6 transiciones.

**Diseño.** q0 con lazo adivina el inicio de 00; la rama q3, q4 no acepta nunca.

| Estado | 0 | 1 |
|---|---|---|
| →q0 | {q0, q1} | {q0, q3} |
| q1 | {q2} | ∅ |
| *q2 | ∅ | ∅ |
| q3 | ∅ | {q4} |
| q4 | ∅ | ∅ |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `00` | acepta | acepta | acepta |
| 2 | `0100` | acepta | acepta | acepta |
| 3 | `1000` | acepta | acepta | acepta |
| 4 | `000100100` | acepta | acepta | acepta |
| 5 | `0011000111100` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `11` | rechaza | rechaza | rechaza |
| 8 | `0110` | rechaza | rechaza | rechaza |
| 9 | `1000101` | rechaza | rechaza | rechaza |
| 10 | `11100001001` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `00`: {q0} -0→ {q0, q1} -0→ {q0, q1, q2} — ✔
  Árbol de cómputo: 3 caminos, 1 de aceptación:
    - q0 -0→ q1 -0→ q2 — ✔ acepta
    - q0 -0→ q0 -0→ q0 — ✘ termina fuera de F
    - q0 -0→ q0 -0→ q1 — ✘ termina fuera de F
2. `0100`: {q0} -0→ {q0, q1} -1→ {q0, q3} -0→ {q0, q1} -0→ {q0, q1, q2} — ✔
  Árbol de cómputo: 5 caminos, 1 de aceptación:
    - q0 -0→ q0 -1→ q0 -0→ q1 -0→ q2 — ✔ acepta
    - q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 — ✘ termina fuera de F
    - q0 -0→ q0 -1→ q0 -0→ q0 -0→ q1 — ✘ termina fuera de F
    - q0 -0→ q0 -1→ q3 — ✘ muere tras leer `01`
    - q0 -0→ q1 — ✘ muere tras leer `0`
3. `1000`: {q0} -1→ {q0, q3} -0→ {q0, q1} -0→ {q0, q1, q2} -0→ {q0, q1, q2} — ✔
  Árbol de cómputo: 5 caminos, 1 de aceptación:
    - q0 -1→ q0 -0→ q0 -0→ q1 -0→ q2 — ✔ acepta
    - q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 — ✘ termina fuera de F
    - q0 -1→ q0 -0→ q0 -0→ q0 -0→ q1 — ✘ termina fuera de F
    - q0 -1→ q0 -0→ q1 -0→ q2 — ✘ muere tras leer `100`
    - q0 -1→ q3 — ✘ muere tras leer `1`
4. `000100100`: {q0} -0→ {q0, q1} -0→ {q0, q1, q2} -0→ {q0, q1, q2} -1→ {q0, q3} -0→ {q0, q1} -0→ {q0, q1, q2} -1→ {q0, q3} -0→ {q0, q1} -0→ {q0, q1, q2} — ✔
  Árbol de cómputo: 10 caminos, 1 de aceptación (se muestran 6):
    - q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q1 -0→ q2 — ✔ acepta
    - q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 — ✘ termina fuera de F
    - q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q1 — ✘ termina fuera de F
    - q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q3 — ✘ muere tras leer `0001001`
    - q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q1 — ✘ muere tras leer `000100`
    - q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q1 -0→ q2 — ✘ muere tras leer `000100`
5. `0011000111100`: {q0} -0→ {q0, q1} -0→ {q0, q1, q2} -1→ {q0, q3} -1→ {q0, q3, q4} -0→ {q0, q1} -0→ {q0, q1, q2} -0→ {q0, q1, q2} -1→ {q0, q3} -1→ {q0, q3, q4} -1→ {q0, q3, q4} -1→ {q0, q3, q4} -0→ {q0, q1} -0→ {q0, q1, q2} — ✔
  Árbol de cómputo: 14 caminos, 1 de aceptación (se muestran 6):
    - q0 -0→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 -1→ q0 -1→ q0 -1→ q0 -0→ q1 -0→ q2 — ✔ acepta
    - q0 -0→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 -1→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 — ✘ termina fuera de F
    - q0 -0→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 -1→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q1 — ✘ termina fuera de F
    - q0 -0→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 -1→ q0 -1→ q0 -1→ q3 — ✘ muere tras leer `00110001111`
    - q0 -0→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 -1→ q0 -1→ q3 -1→ q4 — ✘ muere tras leer `00110001111`
    - q0 -0→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 -1→ q3 -1→ q4 — ✘ muere tras leer `0011000111`
6. λ: {q0} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
7. `11`: {q0} -1→ {q0, q3} -1→ {q0, q3, q4} — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - q0 -1→ q0 -1→ q0 — ✘ termina fuera de F
    - q0 -1→ q0 -1→ q3 — ✘ termina fuera de F
    - q0 -1→ q3 -1→ q4 — ✘ termina fuera de F
8. `0110`: {q0} -0→ {q0, q1} -1→ {q0, q3} -1→ {q0, q3, q4} -0→ {q0, q1} — ✘
  Árbol de cómputo: 5 caminos, 0 de aceptación:
    - q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 — ✘ termina fuera de F
    - q0 -0→ q0 -1→ q0 -1→ q0 -0→ q1 — ✘ termina fuera de F
    - q0 -0→ q0 -1→ q0 -1→ q3 — ✘ muere tras leer `011`
    - q0 -0→ q0 -1→ q3 -1→ q4 — ✘ muere tras leer `011`
    - q0 -0→ q1 — ✘ muere tras leer `0`
9. `1000101`: {q0} -1→ {q0, q3} -0→ {q0, q1} -0→ {q0, q1, q2} -0→ {q0, q1, q2} -1→ {q0, q3} -0→ {q0, q1} -1→ {q0, q3} — ✘
  Árbol de cómputo: 8 caminos, 0 de aceptación (se muestran 6):
    - q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -1→ q0 — ✘ termina fuera de F
    - q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -1→ q3 — ✘ termina fuera de F
    - q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q1 — ✘ muere tras leer `100010`
    - q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -1→ q3 — ✘ muere tras leer `10001`
    - q0 -1→ q0 -0→ q0 -0→ q0 -0→ q1 — ✘ muere tras leer `1000`
    - q0 -1→ q0 -0→ q0 -0→ q1 -0→ q2 — ✘ muere tras leer `1000`
10. `11100001001`: {q0} -1→ {q0, q3} -1→ {q0, q3, q4} -1→ {q0, q3, q4} -0→ {q0, q1} -0→ {q0, q1, q2} -0→ {q0, q1, q2} -0→ {q0, q1, q2} -1→ {q0, q3} -0→ {q0, q1} -0→ {q0, q1, q2} -1→ {q0, q3} — ✘
  Árbol de cómputo: 12 caminos, 0 de aceptación (se muestran 6):
    - q0 -1→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 — ✘ termina fuera de F
    - q0 -1→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q3 — ✘ termina fuera de F
    - q0 -1→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -0→ q1 — ✘ muere tras leer `1110000100`
    - q0 -1→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q1 -0→ q2 — ✘ muere tras leer `1110000100`
    - q0 -1→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -0→ q0 -1→ q3 — ✘ muere tras leer `11100001`
    - q0 -1→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -0→ q1 — ✘ muere tras leer `1110000`

</details>

Simulación paso a paso en JFLAP con `00`: [ver captura](../../evidencias/jflap/pasos/L3-261-AFND.png).

**Conversión.** AFND (5 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 5 estados, [`L3-261-AFND-AFD.jff`](../../automatas/conversiones/L3-261-AFND-AFD.jff) ([.json](../../automatas/conversiones/L3-261-AFND-AFD.json), [.xml](../../automatas/conversiones/L3-261-AFND-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 5 estados, y el AFD mínimo (Hopcroft), 3. La cota es 2^5 = 32. Se verificó que los tres autómatas aceptan el mismo lenguaje.

#### AFD equivalente al 261. — `L3-261-AFD`

Archivos: [`L3-261-AFD.jff`](../../automatas/lista3-afnd/L3-261-AFD.jff) · [`L3-261-AFD.json`](../../automatas/lista3-afnd/L3-261-AFD.json) · [`L3-261-AFD.xml`](../../automatas/lista3-afnd/L3-261-AFD.xml). Tipo según la definición: **AFD**, |Q| = 5, Σ = {0, 1}, 10 transiciones.

**Diseño.** Construcción de subconjuntos: cada estado es el conjunto de estados del AFN alcanzables con el prefijo leído; acepta si contiene un estado final.

| Estado | 0 | 1 |
|---|---|---|
| →{q0} | {q0,q1} | {q0,q3} |
| {q0,q1} | {q0,q1,q2} | {q0,q3} |
| {q0,q3} | {q0,q1} | {q0,q3,q4} |
| *{q0,q1,q2} | {q0,q1,q2} | {q0,q3} |
| {q0,q3,q4} | {q0,q1} | {q0,q3,q4} |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `00` | acepta | acepta | acepta |
| 2 | `100` | acepta | acepta | acepta |
| 3 | `011100` | acepta | acepta | acepta |
| 4 | `01001100` | acepta | acepta | acepta |
| 5 | `1001000101100` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `01` | rechaza | rechaza | rechaza |
| 8 | `0111` | rechaza | rechaza | rechaza |
| 9 | `01000001` | rechaza | rechaza | rechaza |
| 10 | `01111100101` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `00`: {q0} -0→ {q0,q1} -0→ {q0,q1,q2} — ✔
2. `100`: {q0} -1→ {q0,q3} -0→ {q0,q1} -0→ {q0,q1,q2} — ✔
3. `011100`: {q0} -0→ {q0,q1} -1→ {q0,q3} -1→ {q0,q3,q4} -1→ {q0,q3,q4} -0→ {q0,q1} -0→ {q0,q1,q2} — ✔
4. `01001100`: {q0} -0→ {q0,q1} -1→ {q0,q3} -0→ {q0,q1} -0→ {q0,q1,q2} -1→ {q0,q3} -1→ {q0,q3,q4} -0→ {q0,q1} -0→ {q0,q1,q2} — ✔
5. `1001000101100`: {q0} -1→ {q0,q3} -0→ {q0,q1} -0→ {q0,q1,q2} -1→ {q0,q3} -0→ {q0,q1} -0→ {q0,q1,q2} -0→ {q0,q1,q2} -1→ {q0,q3} -0→ {q0,q1} -1→ {q0,q3} -1→ {q0,q3,q4} -0→ {q0,q1} -0→ {q0,q1,q2} — ✔
6. λ: {q0} — ✘
7. `01`: {q0} -0→ {q0,q1} -1→ {q0,q3} — ✘
8. `0111`: {q0} -0→ {q0,q1} -1→ {q0,q3} -1→ {q0,q3,q4} -1→ {q0,q3,q4} — ✘
9. `01000001`: {q0} -0→ {q0,q1} -1→ {q0,q3} -0→ {q0,q1} -0→ {q0,q1,q2} -0→ {q0,q1,q2} -0→ {q0,q1,q2} -0→ {q0,q1,q2} -1→ {q0,q3} — ✘
10. `01111100101`: {q0} -0→ {q0,q1} -1→ {q0,q3} -1→ {q0,q3,q4} -1→ {q0,q3,q4} -1→ {q0,q3,q4} -1→ {q0,q3,q4} -0→ {q0,q1} -0→ {q0,q1,q2} -1→ {q0,q3} -0→ {q0,q1} -1→ {q0,q3} — ✘

</details>

Simulación paso a paso en JFLAP con `00`: [ver captura](../../evidencias/jflap/pasos/L3-261-AFD.png).

#### AFD del 261, minimizado. — `L3-261-AFD-min`

Archivos: [`L3-261-AFD-min.jff`](../../automatas/lista3-afnd/L3-261-AFD-min.jff) · [`L3-261-AFD-min.json`](../../automatas/lista3-afnd/L3-261-AFD-min.json) · [`L3-261-AFD-min.xml`](../../automatas/lista3-afnd/L3-261-AFD-min.xml). Tipo según la definición: **AFD**, |Q| = 3, Σ = {0, 1}, 6 transiciones.

**Diseño.** El estado guarda cuántos ceros finales se llevan (0, 1, 2 o más).

| Estado | 0 | 1 |
|---|---|---|
| →{{q0},{q0,q3},{q0,q3,q4}} | {q0,q1} | {{q0},{q0,q3},{q0,q3,q4}} |
| {q0,q1} | {q0,q1,q2} | {{q0},{q0,q3},{q0,q3,q4}} |
| *{q0,q1,q2} | {q0,q1,q2} | {{q0},{q0,q3},{q0,q3,q4}} |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `00` | acepta | acepta | acepta |
| 2 | `0100` | acepta | acepta | acepta |
| 3 | `11100` | acepta | acepta | acepta |
| 4 | `001100100` | acepta | acepta | acepta |
| 5 | `11101100000` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `11` | rechaza | rechaza | rechaza |
| 8 | `10001` | rechaza | rechaza | rechaza |
| 9 | `01111001` | rechaza | rechaza | rechaza |
| 10 | `110101111001` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `00`: {{q0},{q0,q3},{q0,q3,q4}} -0→ {q0,q1} -0→ {q0,q1,q2} — ✔
2. `0100`: {{q0},{q0,q3},{q0,q3,q4}} -0→ {q0,q1} -1→ {{q0},{q0,q3},{q0,q3,q4}} -0→ {q0,q1} -0→ {q0,q1,q2} — ✔
3. `11100`: {{q0},{q0,q3},{q0,q3,q4}} -1→ {{q0},{q0,q3},{q0,q3,q4}} -1→ {{q0},{q0,q3},{q0,q3,q4}} -1→ {{q0},{q0,q3},{q0,q3,q4}} -0→ {q0,q1} -0→ {q0,q1,q2} — ✔
4. `001100100`: {{q0},{q0,q3},{q0,q3,q4}} -0→ {q0,q1} -0→ {q0,q1,q2} -1→ {{q0},{q0,q3},{q0,q3,q4}} -1→ {{q0},{q0,q3},{q0,q3,q4}} -0→ {q0,q1} -0→ {q0,q1,q2} -1→ {{q0},{q0,q3},{q0,q3,q4}} -0→ {q0,q1} -0→ {q0,q1,q2} — ✔
5. `11101100000`: {{q0},{q0,q3},{q0,q3,q4}} -1→ {{q0},{q0,q3},{q0,q3,q4}} -1→ {{q0},{q0,q3},{q0,q3,q4}} -1→ {{q0},{q0,q3},{q0,q3,q4}} -0→ {q0,q1} -1→ {{q0},{q0,q3},{q0,q3,q4}} -1→ {{q0},{q0,q3},{q0,q3,q4}} -0→ {q0,q1} -0→ {q0,q1,q2} -0→ {q0,q1,q2} -0→ {q0,q1,q2} -0→ {q0,q1,q2} — ✔
6. λ: {{q0},{q0,q3},{q0,q3,q4}} — ✘
7. `11`: {{q0},{q0,q3},{q0,q3,q4}} -1→ {{q0},{q0,q3},{q0,q3,q4}} -1→ {{q0},{q0,q3},{q0,q3,q4}} — ✘
8. `10001`: {{q0},{q0,q3},{q0,q3,q4}} -1→ {{q0},{q0,q3},{q0,q3,q4}} -0→ {q0,q1} -0→ {q0,q1,q2} -0→ {q0,q1,q2} -1→ {{q0},{q0,q3},{q0,q3,q4}} — ✘
9. `01111001`: {{q0},{q0,q3},{q0,q3,q4}} -0→ {q0,q1} -1→ {{q0},{q0,q3},{q0,q3,q4}} -1→ {{q0},{q0,q3},{q0,q3,q4}} -1→ {{q0},{q0,q3},{q0,q3,q4}} -1→ {{q0},{q0,q3},{q0,q3,q4}} -0→ {q0,q1} -0→ {q0,q1,q2} -1→ {{q0},{q0,q3},{q0,q3,q4}} — ✘
10. `110101111001`: {{q0},{q0,q3},{q0,q3,q4}} -1→ {{q0},{q0,q3},{q0,q3,q4}} -1→ {{q0},{q0,q3},{q0,q3,q4}} -0→ {q0,q1} -1→ {{q0},{q0,q3},{q0,q3,q4}} -0→ {q0,q1} -1→ {{q0},{q0,q3},{q0,q3,q4}} -1→ {{q0},{q0,q3},{q0,q3,q4}} -1→ {{q0},{q0,q3},{q0,q3,q4}} -1→ {{q0},{q0,q3},{q0,q3,q4}} -0→ {q0,q1} -0→ {q0,q1,q2} -1→ {{q0},{q0,q3},{q0,q3,q4}} — ✘

</details>

Simulación paso a paso en JFLAP con `00`: [ver captura](../../evidencias/jflap/pasos/L3-261-AFD-min.png).

<a id="problema-3-262"></a>

## Lista 3, problema 262

**Enunciado.** AFN que acepta {ab, ba}.

**Clasificación: AFND.** El autómata de partida es un AFN (varios destinos por símbolo); el AFD es su conversión. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### AFN que acepta {ab, ba}. — `L3-262-AFND`

Archivos: [`L3-262-AFND.jff`](../../automatas/lista3-afnd/L3-262-AFND.jff) · [`L3-262-AFND.json`](../../automatas/lista3-afnd/L3-262-AFND.json) · [`L3-262-AFND.xml`](../../automatas/lista3-afnd/L3-262-AFND.xml). Tipo según la definición: **AFND**, |Q| = 4, Σ = {a, b}, 4 transiciones.

**Diseño.** Dos ramas que convergen en el estado final: q1 = leí a; q2 = leí b.

| Estado | a | b |
|---|---|---|
| →q0 | q1 | q2 |
| q1 | — | q3 |
| q2 | q3 | — |
| *q3 | — | — |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `ab` | acepta | acepta | acepta |
| 2 | `ba` | acepta | acepta | acepta |
| 3 | λ | rechaza | rechaza | rechaza |
| 4 | `aa` | rechaza | rechaza | rechaza |
| 5 | `baaa` | rechaza | rechaza | rechaza |
| 6 | `bbaabaa` | rechaza | rechaza | rechaza |
| 7 | `babababbaba` | rechaza | rechaza | rechaza |

Nota sobre los casos: el lenguaje solo tiene 2 palabras.

<details><summary>Recorrido completo de cada cadena</summary>

1. `ab`: q0 -a→ q1 -b→ q3 — ✔
2. `ba`: q0 -b→ q2 -a→ q3 — ✔
3. λ: q0 — ✘
4. `aa`: q0 -a→ q1 -a→ (sin transición) — ✘
5. `baaa`: q0 -b→ q2 -a→ q3 -a→ (sin transición) — ✘
6. `bbaabaa`: q0 -b→ q2 -b→ (sin transición) — ✘
7. `babababbaba`: q0 -b→ q2 -a→ q3 -b→ (sin transición) — ✘

</details>

Simulación paso a paso en JFLAP con `ab`: [ver captura](../../evidencias/jflap/pasos/L3-262-AFND.png).

**Conversión.** AFND (4 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 4 estados, [`L3-262-AFND-AFD.jff`](../../automatas/conversiones/L3-262-AFND-AFD.jff) ([.json](../../automatas/conversiones/L3-262-AFND-AFD.json), [.xml](../../automatas/conversiones/L3-262-AFND-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 5 estados, y el AFD mínimo (Hopcroft), 5. La cota es 2^4 = 16. Se verificó que los tres autómatas aceptan el mismo lenguaje.

#### AFD que acepta {ab, ba}. — `L3-262-AFD`

Archivos: [`L3-262-AFD.jff`](../../automatas/lista3-afnd/L3-262-AFD.jff) · [`L3-262-AFD.json`](../../automatas/lista3-afnd/L3-262-AFD.json) · [`L3-262-AFD.xml`](../../automatas/lista3-afnd/L3-262-AFD.xml). Tipo según la definición: **AFD**, |Q| = 5, Σ = {a, b}, 10 transiciones.

**Diseño.** Construcción de subconjuntos: cada estado es el conjunto de estados del AFN alcanzables con el prefijo leído; acepta si contiene un estado final. ∅ es el estado de rechazo.

| Estado | a | b |
|---|---|---|
| →{q0} | {q1} | {q2} |
| {q1} | ∅ | {q3} |
| {q2} | {q3} | ∅ |
| ∅ | ∅ | ∅ |
| *{q3} | ∅ | ∅ |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `ab` | acepta | acepta | acepta |
| 2 | `ba` | acepta | acepta | acepta |
| 3 | λ | rechaza | rechaza | rechaza |
| 4 | `baa` | rechaza | rechaza | rechaza |
| 5 | `baaa` | rechaza | rechaza | rechaza |
| 6 | `babaaba` | rechaza | rechaza | rechaza |
| 7 | `bbbbbababab` | rechaza | rechaza | rechaza |

Nota sobre los casos: el lenguaje solo tiene 2 palabras.

<details><summary>Recorrido completo de cada cadena</summary>

1. `ab`: {q0} -a→ {q1} -b→ {q3} — ✔
2. `ba`: {q0} -b→ {q2} -a→ {q3} — ✔
3. λ: {q0} — ✘
4. `baa`: {q0} -b→ {q2} -a→ {q3} -a→ ∅ — ✘
5. `baaa`: {q0} -b→ {q2} -a→ {q3} -a→ ∅ -a→ ∅ — ✘
6. `babaaba`: {q0} -b→ {q2} -a→ {q3} -b→ ∅ -a→ ∅ -a→ ∅ -b→ ∅ -a→ ∅ — ✘
7. `bbbbbababab`: {q0} -b→ {q2} -b→ ∅ -b→ ∅ -b→ ∅ -b→ ∅ -a→ ∅ -b→ ∅ -a→ ∅ -b→ ∅ -a→ ∅ -b→ ∅ — ✘

</details>

Simulación paso a paso en JFLAP con `ab`: [ver captura](../../evidencias/jflap/pasos/L3-262-AFD.png).

<a id="problema-3-263"></a>

## Lista 3, problema 263

**Enunciado.** AFN de la figura 263.

**Clasificación: AFND.** El autómata de partida es un AFN (varios destinos por símbolo); el AFD es su conversión. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### AFN de la figura 263. — `L3-263-AFND`

Archivos: [`L3-263-AFND.jff`](../../automatas/lista3-afnd/L3-263-AFND.jff) · [`L3-263-AFND.json`](../../automatas/lista3-afnd/L3-263-AFND.json) · [`L3-263-AFND.xml`](../../automatas/lista3-afnd/L3-263-AFND.xml). Tipo según la definición: **AFND**, |Q| = 3, Σ = {0, 1}, 4 transiciones.

**Diseño.** q0 con lazo adivina el inicio de 01.

| Estado | 0 | 1 |
|---|---|---|
| →q0 | {q0, q1} | {q0} |
| q1 | ∅ | {q2} |
| *q2 | ∅ | ∅ |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `01` | acepta | acepta | acepta |
| 2 | `001` | acepta | acepta | acepta |
| 3 | `011101` | acepta | acepta | acepta |
| 4 | `1110001` | acepta | acepta | acepta |
| 5 | `110010110101` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `00` | rechaza | rechaza | rechaza |
| 8 | `0011` | rechaza | rechaza | rechaza |
| 9 | `1100011` | rechaza | rechaza | rechaza |
| 10 | `01001011010` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `01`: {q0} -0→ {q0, q1} -1→ {q0, q2} — ✔
  Árbol de cómputo: 2 caminos, 1 de aceptación:
    - q0 -0→ q1 -1→ q2 — ✔ acepta
    - q0 -0→ q0 -1→ q0 — ✘ termina fuera de F
2. `001`: {q0} -0→ {q0, q1} -0→ {q0, q1} -1→ {q0, q2} — ✔
  Árbol de cómputo: 3 caminos, 1 de aceptación:
    - q0 -0→ q0 -0→ q1 -1→ q2 — ✔ acepta
    - q0 -0→ q0 -0→ q0 -1→ q0 — ✘ termina fuera de F
    - q0 -0→ q1 — ✘ muere tras leer `0`
3. `011101`: {q0} -0→ {q0, q1} -1→ {q0, q2} -1→ {q0} -1→ {q0} -0→ {q0, q1} -1→ {q0, q2} — ✔
  Árbol de cómputo: 3 caminos, 1 de aceptación:
    - q0 -0→ q0 -1→ q0 -1→ q0 -1→ q0 -0→ q1 -1→ q2 — ✔ acepta
    - q0 -0→ q0 -1→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q0 — ✘ termina fuera de F
    - q0 -0→ q1 -1→ q2 — ✘ muere tras leer `01`
4. `1110001`: {q0} -1→ {q0} -1→ {q0} -1→ {q0} -0→ {q0, q1} -0→ {q0, q1} -0→ {q0, q1} -1→ {q0, q2} — ✔
  Árbol de cómputo: 4 caminos, 1 de aceptación:
    - q0 -1→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q1 -1→ q2 — ✔ acepta
    - q0 -1→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 — ✘ termina fuera de F
    - q0 -1→ q0 -1→ q0 -1→ q0 -0→ q0 -0→ q1 — ✘ muere tras leer `11100`
    - q0 -1→ q0 -1→ q0 -1→ q0 -0→ q1 — ✘ muere tras leer `1110`
5. `110010110101`: {q0} -1→ {q0} -1→ {q0} -0→ {q0, q1} -0→ {q0, q1} -1→ {q0, q2} -0→ {q0, q1} -1→ {q0, q2} -1→ {q0} -0→ {q0, q1} -1→ {q0, q2} -0→ {q0, q1} -1→ {q0, q2} — ✔
  Árbol de cómputo: 6 caminos, 1 de aceptación:
    - q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q1 -1→ q2 — ✔ acepta
    - q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q0 -1→ q0 — ✘ termina fuera de F
    - q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q1 -1→ q2 — ✘ muere tras leer `1100101101`
    - q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q1 -1→ q2 — ✘ muere tras leer `1100101`
    - q0 -1→ q0 -1→ q0 -0→ q0 -0→ q1 -1→ q2 — ✘ muere tras leer `11001`
    - q0 -1→ q0 -1→ q0 -0→ q1 — ✘ muere tras leer `110`
6. λ: {q0} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
7. `00`: {q0} -0→ {q0, q1} -0→ {q0, q1} — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - q0 -0→ q0 -0→ q0 — ✘ termina fuera de F
    - q0 -0→ q0 -0→ q1 — ✘ termina fuera de F
    - q0 -0→ q1 — ✘ muere tras leer `0`
8. `0011`: {q0} -0→ {q0, q1} -0→ {q0, q1} -1→ {q0, q2} -1→ {q0} — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - q0 -0→ q0 -0→ q0 -1→ q0 -1→ q0 — ✘ termina fuera de F
    - q0 -0→ q0 -0→ q1 -1→ q2 — ✘ muere tras leer `001`
    - q0 -0→ q1 — ✘ muere tras leer `0`
9. `1100011`: {q0} -1→ {q0} -1→ {q0} -0→ {q0, q1} -0→ {q0, q1} -0→ {q0, q1} -1→ {q0, q2} -1→ {q0} — ✘
  Árbol de cómputo: 4 caminos, 0 de aceptación:
    - q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -1→ q0 -1→ q0 — ✘ termina fuera de F
    - q0 -1→ q0 -1→ q0 -0→ q0 -0→ q0 -0→ q1 -1→ q2 — ✘ muere tras leer `110001`
    - q0 -1→ q0 -1→ q0 -0→ q0 -0→ q1 — ✘ muere tras leer `1100`
    - q0 -1→ q0 -1→ q0 -0→ q1 — ✘ muere tras leer `110`
10. `01001011010`: {q0} -0→ {q0, q1} -1→ {q0, q2} -0→ {q0, q1} -0→ {q0, q1} -1→ {q0, q2} -0→ {q0, q1} -1→ {q0, q2} -1→ {q0} -0→ {q0, q1} -1→ {q0, q2} -0→ {q0, q1} — ✘
  Árbol de cómputo: 7 caminos, 0 de aceptación (se muestran 6):
    - q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q0 — ✘ termina fuera de F
    - q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q0 -1→ q0 -0→ q1 — ✘ termina fuera de F
    - q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q0 -1→ q0 -1→ q0 -0→ q1 -1→ q2 — ✘ muere tras leer `0100101101`
    - q0 -0→ q0 -1→ q0 -0→ q0 -0→ q0 -1→ q0 -0→ q1 -1→ q2 — ✘ muere tras leer `0100101`
    - q0 -0→ q0 -1→ q0 -0→ q0 -0→ q1 -1→ q2 — ✘ muere tras leer `01001`
    - q0 -0→ q0 -1→ q0 -0→ q1 — ✘ muere tras leer `010`

</details>

Simulación paso a paso en JFLAP con `01`: [ver captura](../../evidencias/jflap/pasos/L3-263-AFND.png).

**Conversión.** AFND (3 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 3 estados, [`L3-263-AFND-AFD.jff`](../../automatas/conversiones/L3-263-AFND-AFD.jff) ([.json](../../automatas/conversiones/L3-263-AFND-AFD.json), [.xml](../../automatas/conversiones/L3-263-AFND-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 3 estados, y el AFD mínimo (Hopcroft), 3. La cota es 2^3 = 8. Se verificó que los tres autómatas aceptan el mismo lenguaje.

#### AFD equivalente al 263. — `L3-263-AFD`

Archivos: [`L3-263-AFD.jff`](../../automatas/lista3-afnd/L3-263-AFD.jff) · [`L3-263-AFD.json`](../../automatas/lista3-afnd/L3-263-AFD.json) · [`L3-263-AFD.xml`](../../automatas/lista3-afnd/L3-263-AFD.xml). Tipo según la definición: **AFD**, |Q| = 3, Σ = {0, 1}, 6 transiciones.

**Diseño.** Construcción de subconjuntos: cada estado es el conjunto de estados del AFN alcanzables con el prefijo leído; acepta si contiene un estado final.

| Estado | 0 | 1 |
|---|---|---|
| →{q0} | {q0,q1} | {q0} |
| {q0,q1} | {q0,q1} | {q0,q2} |
| *{q0,q2} | {q0,q1} | {q0} |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `01` | acepta | acepta | acepta |
| 2 | `1101` | acepta | acepta | acepta |
| 3 | `00101` | acepta | acepta | acepta |
| 4 | `00001101` | acepta | acepta | acepta |
| 5 | `100100100001` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `11` | rechaza | rechaza | rechaza |
| 8 | `0110` | rechaza | rechaza | rechaza |
| 9 | `0011010` | rechaza | rechaza | rechaza |
| 10 | `100101010010` | rechaza | rechaza | — |

<details><summary>Recorrido completo de cada cadena</summary>

1. `01`: {q0} -0→ {q0,q1} -1→ {q0,q2} — ✔
2. `1101`: {q0} -1→ {q0} -1→ {q0} -0→ {q0,q1} -1→ {q0,q2} — ✔
3. `00101`: {q0} -0→ {q0,q1} -0→ {q0,q1} -1→ {q0,q2} -0→ {q0,q1} -1→ {q0,q2} — ✔
4. `00001101`: {q0} -0→ {q0,q1} -0→ {q0,q1} -0→ {q0,q1} -0→ {q0,q1} -1→ {q0,q2} -1→ {q0} -0→ {q0,q1} -1→ {q0,q2} — ✔
5. `100100100001`: {q0} -1→ {q0} -0→ {q0,q1} -0→ {q0,q1} -1→ {q0,q2} -0→ {q0,q1} -0→ {q0,q1} -1→ {q0,q2} -0→ {q0,q1} -0→ {q0,q1} -0→ {q0,q1} -0→ {q0,q1} -1→ {q0,q2} — ✔
6. λ: {q0} — ✘
7. `11`: {q0} -1→ {q0} -1→ {q0} — ✘
8. `0110`: {q0} -0→ {q0,q1} -1→ {q0,q2} -1→ {q0} -0→ {q0,q1} — ✘
9. `0011010`: {q0} -0→ {q0,q1} -0→ {q0,q1} -1→ {q0,q2} -1→ {q0} -0→ {q0,q1} -1→ {q0,q2} -0→ {q0,q1} — ✘
10. `100101010010`: {q0} -1→ {q0} -0→ {q0,q1} -0→ {q0,q1} -1→ {q0,q2} -0→ {q0,q1} -1→ {q0,q2} -0→ {q0,q1} -1→ {q0,q2} -0→ {q0,q1} -0→ {q0,q1} -1→ {q0,q2} -0→ {q0,q1} — ✘

</details>

Simulación paso a paso en JFLAP con `01`: [ver captura](../../evidencias/jflap/pasos/L3-263-AFD.png).

