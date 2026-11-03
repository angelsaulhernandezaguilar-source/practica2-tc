# Ejercicio 2 — AFD — Lista 2

[← Ejercicio 2](../02-jflap.md) · [Índice](../../README.md)

Cada autómata indica su clasificación, el diseño, la tabla de transiciones, cinco cadenas válidas y cinco inválidas con el resultado esperado (oráculo escrito a partir del enunciado), el del simulador de este proyecto y el del motor de JFLAP 7.1, el recorrido de cada cadena (en los no deterministas, el conjunto de estados activos y el árbol de caminos) y la captura de la simulación paso a paso en JFLAP.

<a id="problema-2-94"></a>

## Lista 2, problema 94

**Enunciado.** Las palabras de Σ₁ = {0,1,2} que comienzan con 1 y terminan con 2.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Basta recordar si el primer símbolo fue 1 y si el último es 2.

#### AFD — `L2-094`

Archivos: [`L2-094.jff`](../../automatas/lista2-afd/L2-094.jff) · [`L2-094.json`](../../automatas/lista2-afd/L2-094.json) · [`L2-094.xml`](../../automatas/lista2-afd/L2-094.xml). Tipo según la definición: **AFD**, |Q| = 4, Σ = {0, 1, 2}, 12 transiciones.

**Diseño.** El estado guarda si el prefijo leído es válido (empezó con 1) y si el último símbolo es 2. Si el primer símbolo no es 1, el rechazo es definitivo.

| Estado | 0 | 1 | 2 | Significado |
|---|---|---|---|---|
| →q0 | q1 | q2 | q1 | no se ha leído nada |
| q1 | q1 | q1 | q1 | rechazo absorbente |
| q2 | q2 | q2 | q3 | empezó con 1 y el último símbolo no es 2 |
| *q3 | q2 | q2 | q3 | empezó con 1 y el último símbolo es 2 |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `12` | acepta | acepta | acepta |
| 2 | `112` | acepta | acepta | acepta |
| 3 | `11212` | acepta | acepta | acepta |
| 4 | `1111202` | acepta | acepta | acepta |
| 5 | `110021222012` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `02` | rechaza | rechaza | rechaza |
| 8 | `0211` | rechaza | rechaza | rechaza |
| 9 | `2011122` | rechaza | rechaza | rechaza |
| 10 | `02112102002` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `12`: q0 -1→ q2 -2→ q3 — ✔
2. `112`: q0 -1→ q2 -1→ q2 -2→ q3 — ✔
3. `11212`: q0 -1→ q2 -1→ q2 -2→ q3 -1→ q2 -2→ q3 — ✔
4. `1111202`: q0 -1→ q2 -1→ q2 -1→ q2 -1→ q2 -2→ q3 -0→ q2 -2→ q3 — ✔
5. `110021222012`: q0 -1→ q2 -1→ q2 -0→ q2 -0→ q2 -2→ q3 -1→ q2 -2→ q3 -2→ q3 -2→ q3 -0→ q2 -1→ q2 -2→ q3 — ✔
6. λ: q0 — ✘
7. `02`: q0 -0→ q1 -2→ q1 — ✘
8. `0211`: q0 -0→ q1 -2→ q1 -1→ q1 -1→ q1 — ✘
9. `2011122`: q0 -2→ q1 -0→ q1 -1→ q1 -1→ q1 -1→ q1 -2→ q1 -2→ q1 — ✘
10. `02112102002`: q0 -0→ q1 -2→ q1 -1→ q1 -1→ q1 -2→ q1 -1→ q1 -0→ q1 -2→ q1 -0→ q1 -0→ q1 -2→ q1 — ✘

</details>

Simulación paso a paso en JFLAP con `12`: [ver captura](../../evidencias/jflap/pasos/L2-094.png).

<a id="problema-2-95"></a>

## Lista 2, problema 95

**Enunciado.** Las palabras de Σ₁ que tienen longitud 4.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Solo se cuenta la longitud hasta 5.

#### AFD — `L2-095`

Archivos: [`L2-095.jff`](../../automatas/lista2-afd/L2-095.jff) · [`L2-095.json`](../../automatas/lista2-afd/L2-095.json) · [`L2-095.xml`](../../automatas/lista2-afd/L2-095.xml). Tipo según la definición: **AFD**, |Q| = 6, Σ = {0, 1, 2}, 18 transiciones.

**Diseño.** Contador de longitud saturado: qᵢ = se han leído i símbolos (i ≤ 4); a partir del quinto símbolo el estado de rechazo es absorbente. Solo q4 acepta.

| Estado | 0 | 1 | 2 | Significado |
|---|---|---|---|---|
| →q0 | q1 | q1 | q1 | se han leído 0 símbolos |
| q1 | q2 | q2 | q2 | se han leído 1 símbolos |
| q2 | q3 | q3 | q3 | se han leído 2 símbolos |
| q3 | q4 | q4 | q4 | se han leído 3 símbolos |
| *q4 | q5 | q5 | q5 | se han leído 4 símbolos |
| q5 | q5 | q5 | q5 | rechazo absorbente |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `0000` | acepta | acepta | acepta |
| 2 | `0010` | acepta | acepta | acepta |
| 3 | `0101` | acepta | acepta | acepta |
| 4 | `0200` | acepta | acepta | acepta |
| 5 | `1121` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `11` | rechaza | rechaza | rechaza |
| 8 | `20210` | rechaza | rechaza | rechaza |
| 9 | `1202010` | rechaza | rechaza | rechaza |
| 10 | `00220120120` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `0000`: q0 -0→ q1 -0→ q2 -0→ q3 -0→ q4 — ✔
2. `0010`: q0 -0→ q1 -0→ q2 -1→ q3 -0→ q4 — ✔
3. `0101`: q0 -0→ q1 -1→ q2 -0→ q3 -1→ q4 — ✔
4. `0200`: q0 -0→ q1 -2→ q2 -0→ q3 -0→ q4 — ✔
5. `1121`: q0 -1→ q1 -1→ q2 -2→ q3 -1→ q4 — ✔
6. λ: q0 — ✘
7. `11`: q0 -1→ q1 -1→ q2 — ✘
8. `20210`: q0 -2→ q1 -0→ q2 -2→ q3 -1→ q4 -0→ q5 — ✘
9. `1202010`: q0 -1→ q1 -2→ q2 -0→ q3 -2→ q4 -0→ q5 -1→ q5 -0→ q5 — ✘
10. `00220120120`: q0 -0→ q1 -0→ q2 -2→ q3 -2→ q4 -0→ q5 -1→ q5 -2→ q5 -0→ q5 -1→ q5 -2→ q5 -0→ q5 — ✘

</details>

Simulación paso a paso en JFLAP con `0000`: [ver captura](../../evidencias/jflap/pasos/L2-095.png).

<a id="problema-2-96"></a>

## Lista 2, problema 96

**Enunciado.** Las palabras de Σ₁ con prefijo 20 y longitud 4.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Combina la verificación del prefijo con un contador de longitud.

#### AFD — `L2-096`

Archivos: [`L2-096.jff`](../../automatas/lista2-afd/L2-096.jff) · [`L2-096.json`](../../automatas/lista2-afd/L2-096.json) · [`L2-096.xml`](../../automatas/lista2-afd/L2-096.xml). Tipo según la definición: **AFD**, |Q| = 6, Σ = {0, 1, 2}, 18 transiciones.

**Diseño.** Las dos primeras posiciones exigen 2 y luego 0 (cualquier otro símbolo lleva al rechazo); las posiciones 3 y 4 aceptan cualquier símbolo. Solo acepta el estado de longitud exacta 4.

| Estado | 0 | 1 | 2 | Significado |
|---|---|---|---|---|
| →q0 | q1 | q1 | q2 | inicio |
| q1 | q1 | q1 | q1 | rechazo absorbente |
| q2 | q3 | q1 | q1 | se leyó 2 |
| q3 | q4 | q4 | q4 | se leyó el prefijo 20 |
| q4 | q5 | q5 | q5 | 20 y un símbolo más |
| *q5 | q1 | q1 | q1 | 20 y dos símbolos más: longitud 4 |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `2000` | acepta | acepta | acepta |
| 2 | `2001` | acepta | acepta | acepta |
| 3 | `2002` | acepta | acepta | acepta |
| 4 | `2012` | acepta | acepta | acepta |
| 5 | `2020` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `00` | rechaza | rechaza | rechaza |
| 8 | `0000` | rechaza | rechaza | rechaza |
| 9 | `2011002` | rechaza | rechaza | rechaza |
| 10 | `02201200000` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `2000`: q0 -2→ q2 -0→ q3 -0→ q4 -0→ q5 — ✔
2. `2001`: q0 -2→ q2 -0→ q3 -0→ q4 -1→ q5 — ✔
3. `2002`: q0 -2→ q2 -0→ q3 -0→ q4 -2→ q5 — ✔
4. `2012`: q0 -2→ q2 -0→ q3 -1→ q4 -2→ q5 — ✔
5. `2020`: q0 -2→ q2 -0→ q3 -2→ q4 -0→ q5 — ✔
6. λ: q0 — ✘
7. `00`: q0 -0→ q1 -0→ q1 — ✘
8. `0000`: q0 -0→ q1 -0→ q1 -0→ q1 -0→ q1 — ✘
9. `2011002`: q0 -2→ q2 -0→ q3 -1→ q4 -1→ q5 -0→ q1 -0→ q1 -2→ q1 — ✘
10. `02201200000`: q0 -0→ q1 -2→ q1 -2→ q1 -0→ q1 -1→ q1 -2→ q1 -0→ q1 -0→ q1 -0→ q1 -0→ q1 -0→ q1 — ✘

</details>

Simulación paso a paso en JFLAP con `2000`: [ver captura](../../evidencias/jflap/pasos/L2-096.png).

<a id="problema-2-97"></a>

## Lista 2, problema 97

**Enunciado.** Palabras de Σ₁ cuya longitud es múltiplo de 3.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Contador módulo 3 de la longitud. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### Palabras de Σ₁ = {0,1,2} cuya longitud es múltiplo de 3. — `L2-097`

Archivos: [`L2-097.jff`](../../automatas/lista2-afd/L2-097.jff) · [`L2-097.json`](../../automatas/lista2-afd/L2-097.json) · [`L2-097.xml`](../../automatas/lista2-afd/L2-097.xml). Tipo según la definición: **AFD**, |Q| = 3, Σ = {0, 1, 2}, 9 transiciones.

**Diseño.** Solo importa la longitud: el estado guarda el residuo |prefijo| mod 3. q0 es inicial y de aceptación porque |λ| = 0.

| Estado | 0 | 1 | 2 |
|---|---|---|---|
| q1 | q2 | q2 | q2 |
| q2 | q0 | q0 | q0 |
| →*q0 | q1 | q1 | q1 |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | acepta | acepta | acepta |
| 2 | `020` | acepta | acepta | acepta |
| 3 | `201200` | acepta | acepta | acepta |
| 4 | `122020100` | acepta | acepta | acepta |
| 5 | `120021221120` | acepta | acepta | acepta |
| 6 | `0` | rechaza | rechaza | rechaza |
| 7 | `00` | rechaza | rechaza | rechaza |
| 8 | `2021` | rechaza | rechaza | rechaza |
| 9 | `2020020` | rechaza | rechaza | rechaza |
| 10 | `10112212112` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: q0 — ✔
2. `020`: q0 -0→ q1 -2→ q2 -0→ q0 — ✔
3. `201200`: q0 -2→ q1 -0→ q2 -1→ q0 -2→ q1 -0→ q2 -0→ q0 — ✔
4. `122020100`: q0 -1→ q1 -2→ q2 -2→ q0 -0→ q1 -2→ q2 -0→ q0 -1→ q1 -0→ q2 -0→ q0 — ✔
5. `120021221120`: q0 -1→ q1 -2→ q2 -0→ q0 -0→ q1 -2→ q2 -1→ q0 -2→ q1 -2→ q2 -1→ q0 -1→ q1 -2→ q2 -0→ q0 — ✔
6. `0`: q0 -0→ q1 — ✘
7. `00`: q0 -0→ q1 -0→ q2 — ✘
8. `2021`: q0 -2→ q1 -0→ q2 -2→ q0 -1→ q1 — ✘
9. `2020020`: q0 -2→ q1 -0→ q2 -2→ q0 -0→ q1 -0→ q2 -2→ q0 -0→ q1 — ✘
10. `10112212112`: q0 -1→ q1 -0→ q2 -1→ q0 -1→ q1 -2→ q2 -2→ q0 -1→ q1 -2→ q2 -1→ q0 -1→ q1 -2→ q2 — ✘

</details>

Simulación paso a paso en JFLAP con `020`: [ver captura](../../evidencias/jflap/pasos/L2-097.png).

<a id="problema-2-98"></a>

## Lista 2, problema 98

**Enunciado.** Las palabras de Σ₁ que terminan con la cadena 00102.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Búsqueda de sufijo con función de fallo.

#### AFD — `L2-098`

Archivos: [`L2-098.jff`](../../automatas/lista2-afd/L2-098.jff) · [`L2-098.json`](../../automatas/lista2-afd/L2-098.json) · [`L2-098.xml`](../../automatas/lista2-afd/L2-098.xml). Tipo según la definición: **AFD**, |Q| = 6, Σ = {0, 1, 2}, 18 transiciones.

**Diseño.** Autómata de búsqueda del sufijo 00102 (función de fallo, como en el algoritmo KMP): el estado qⱼ indica que los últimos j símbolos son el prefijo más largo de 00102 que es sufijo de lo leído. q5 acepta, pero no es absorbente: si llegan más símbolos se retrocede según la función de fallo.

| Estado | 0 | 1 | 2 | Significado |
|---|---|---|---|---|
| →q0 | q1 | q0 | q0 | ningún avance en el patrón |
| q1 | q2 | q0 | q0 | los últimos símbolos coinciden con «0» |
| q2 | q2 | q3 | q0 | los últimos símbolos coinciden con «00» |
| q3 | q4 | q0 | q0 | los últimos símbolos coinciden con «001» |
| q4 | q2 | q0 | q5 | los últimos símbolos coinciden con «0010» |
| *q5 | q1 | q0 | q0 | los últimos símbolos coinciden con «00102» |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `00102` | acepta | acepta | acepta |
| 2 | `0100102` | acepta | acepta | acepta |
| 3 | `021100102` | acepta | acepta | acepta |
| 4 | `000012100102` | acepta | acepta | acepta |
| 5 | `00221100100102` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `21` | rechaza | rechaza | rechaza |
| 8 | `1001` | rechaza | rechaza | rechaza |
| 9 | `1221021` | rechaza | rechaza | rechaza |
| 10 | `21200011021` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `00102`: q0 -0→ q1 -0→ q2 -1→ q3 -0→ q4 -2→ q5 — ✔
2. `0100102`: q0 -0→ q1 -1→ q0 -0→ q1 -0→ q2 -1→ q3 -0→ q4 -2→ q5 — ✔
3. `021100102`: q0 -0→ q1 -2→ q0 -1→ q0 -1→ q0 -0→ q1 -0→ q2 -1→ q3 -0→ q4 -2→ q5 — ✔
4. `000012100102`: q0 -0→ q1 -0→ q2 -0→ q2 -0→ q2 -1→ q3 -2→ q0 -1→ q0 -0→ q1 -0→ q2 -1→ q3 -0→ q4 -2→ q5 — ✔
5. `00221100100102`: q0 -0→ q1 -0→ q2 -2→ q0 -2→ q0 -1→ q0 -1→ q0 -0→ q1 -0→ q2 -1→ q3 -0→ q4 -0→ q2 -1→ q3 -0→ q4 -2→ q5 — ✔
6. λ: q0 — ✘
7. `21`: q0 -2→ q0 -1→ q0 — ✘
8. `1001`: q0 -1→ q0 -0→ q1 -0→ q2 -1→ q3 — ✘
9. `1221021`: q0 -1→ q0 -2→ q0 -2→ q0 -1→ q0 -0→ q1 -2→ q0 -1→ q0 — ✘
10. `21200011021`: q0 -2→ q0 -1→ q0 -2→ q0 -0→ q1 -0→ q2 -0→ q2 -1→ q3 -1→ q0 -0→ q1 -2→ q0 -1→ q0 — ✘

</details>

Simulación paso a paso en JFLAP con `00102`: [ver captura](../../evidencias/jflap/pasos/L2-098.png).

<a id="problema-2-99"></a>

## Lista 2, problema 99

**Enunciado.** Palabras de Σ₁ que terminan con 001001.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Búsqueda de sufijo con función de fallo. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### Palabras de Σ₁ que terminan con 001001. — `L2-099`

Archivos: [`L2-099.jff`](../../automatas/lista2-afd/L2-099.jff) · [`L2-099.json`](../../automatas/lista2-afd/L2-099.json) · [`L2-099.xml`](../../automatas/lista2-afd/L2-099.xml). Tipo según la definición: **AFD**, |Q| = 7, Σ = {0, 1, 2}, 21 transiciones.

**Diseño.** Autómata de búsqueda de sufijo (función de fallo tipo KMP): el estado qj indica que los últimos j símbolos leídos son el prefijo más largo de 001001 que es sufijo del prefijo leído. Un 2 regresa siempre a q0. Solo q6 acepta y puede abandonarse si llegan más símbolos.

| Estado | 0 | 1 | 2 |
|---|---|---|---|
| q1 | q2 | q0 | q0 |
| q3 | q4 | q0 | q0 |
| *q6 | q4 | q0 | q0 |
| q5 | q2 | q6 | q0 |
| q4 | q5 | q0 | q0 |
| q2 | q2 | q3 | q0 |
| →q0 | q1 | q0 | q0 |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `001001` | acepta | acepta | acepta |
| 2 | `21001001` | acepta | acepta | acepta |
| 3 | `2122001001` | acepta | acepta | acepta |
| 4 | `220102001001` | acepta | acepta | acepta |
| 5 | `001101202001001` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `20` | rechaza | rechaza | rechaza |
| 8 | `1101` | rechaza | rechaza | rechaza |
| 9 | `0002210` | rechaza | rechaza | rechaza |
| 10 | `00000001102` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `001001`: q0 -0→ q1 -0→ q2 -1→ q3 -0→ q4 -0→ q5 -1→ q6 — ✔
2. `21001001`: q0 -2→ q0 -1→ q0 -0→ q1 -0→ q2 -1→ q3 -0→ q4 -0→ q5 -1→ q6 — ✔
3. `2122001001`: q0 -2→ q0 -1→ q0 -2→ q0 -2→ q0 -0→ q1 -0→ q2 -1→ q3 -0→ q4 -0→ q5 -1→ q6 — ✔
4. `220102001001`: q0 -2→ q0 -2→ q0 -0→ q1 -1→ q0 -0→ q1 -2→ q0 -0→ q1 -0→ q2 -1→ q3 -0→ q4 -0→ q5 -1→ q6 — ✔
5. `001101202001001`: q0 -0→ q1 -0→ q2 -1→ q3 -1→ q0 -0→ q1 -1→ q0 -2→ q0 -0→ q1 -2→ q0 -0→ q1 -0→ q2 -1→ q3 -0→ q4 -0→ q5 -1→ q6 — ✔
6. λ: q0 — ✘
7. `20`: q0 -2→ q0 -0→ q1 — ✘
8. `1101`: q0 -1→ q0 -1→ q0 -0→ q1 -1→ q0 — ✘
9. `0002210`: q0 -0→ q1 -0→ q2 -0→ q2 -2→ q0 -2→ q0 -1→ q0 -0→ q1 — ✘
10. `00000001102`: q0 -0→ q1 -0→ q2 -0→ q2 -0→ q2 -0→ q2 -0→ q2 -0→ q2 -1→ q3 -1→ q0 -0→ q1 -2→ q0 — ✘

</details>

Simulación paso a paso en JFLAP con `001001`: [ver captura](../../evidencias/jflap/pasos/L2-099.png).

<a id="problema-2-100"></a>

## Lista 2, problema 100

**Enunciado.** Las palabras de Σ₂ = {a,b,c,0,1} tales que el primer símbolo es una letra y el segundo es un dígito.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Solo se revisan las dos primeras posiciones.

#### AFD — `L2-100`

Archivos: [`L2-100.jff`](../../automatas/lista2-afd/L2-100.jff) · [`L2-100.json`](../../automatas/lista2-afd/L2-100.json) · [`L2-100.xml`](../../automatas/lista2-afd/L2-100.xml). Tipo según la definición: **AFD**, |Q| = 4, Σ = {a, b, c, 0, 1}, 20 transiciones.

**Diseño.** q0 espera una letra; q1, un dígito; q2 confirma el prefijo y acepta todo lo que siga (absorbente). Un símbolo del tipo equivocado lleva al rechazo absorbente. Se exige longitud ≥ 2, porque una palabra de longitud 1 no tiene segundo símbolo.

| Estado | a | b | c | 0 | 1 | Significado |
|---|---|---|---|---|---|---|
| →q0 | q1 | q1 | q1 | q2 | q2 | inicio |
| q1 | q2 | q2 | q2 | q3 | q3 | primer símbolo: letra |
| q2 | q2 | q2 | q2 | q2 | q2 | rechazo absorbente |
| *q3 | q3 | q3 | q3 | q3 | q3 | letra seguida de dígito |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `a0` | acepta | acepta | acepta |
| 2 | `c0` | acepta | acepta | acepta |
| 3 | `b1aa` | acepta | acepta | acepta |
| 4 | `a1ccac0` | acepta | acepta | acepta |
| 5 | `a111ab11c1a` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `0c` | rechaza | rechaza | rechaza |
| 8 | `ab0c` | rechaza | rechaza | rechaza |
| 9 | `0abcaa1` | rechaza | rechaza | rechaza |
| 10 | `bcc0b111acb` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `a0`: q0 -a→ q1 -0→ q3 — ✔
2. `c0`: q0 -c→ q1 -0→ q3 — ✔
3. `b1aa`: q0 -b→ q1 -1→ q3 -a→ q3 -a→ q3 — ✔
4. `a1ccac0`: q0 -a→ q1 -1→ q3 -c→ q3 -c→ q3 -a→ q3 -c→ q3 -0→ q3 — ✔
5. `a111ab11c1a`: q0 -a→ q1 -1→ q3 -1→ q3 -1→ q3 -a→ q3 -b→ q3 -1→ q3 -1→ q3 -c→ q3 -1→ q3 -a→ q3 — ✔
6. λ: q0 — ✘
7. `0c`: q0 -0→ q2 -c→ q2 — ✘
8. `ab0c`: q0 -a→ q1 -b→ q2 -0→ q2 -c→ q2 — ✘
9. `0abcaa1`: q0 -0→ q2 -a→ q2 -b→ q2 -c→ q2 -a→ q2 -a→ q2 -1→ q2 — ✘
10. `bcc0b111acb`: q0 -b→ q1 -c→ q2 -c→ q2 -0→ q2 -b→ q2 -1→ q2 -1→ q2 -1→ q2 -a→ q2 -c→ q2 -b→ q2 — ✘

</details>

Simulación paso a paso en JFLAP con `a0`: [ver captura](../../evidencias/jflap/pasos/L2-100.png).

<a id="problema-2-101"></a>

## Lista 2, problema 101

**Enunciado.** Las palabras de Σ₃ = {a,b} que contienen la cadena aba.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Búsqueda de subcadena con estado final absorbente.

#### AFD — `L2-101`

Archivos: [`L2-101.jff`](../../automatas/lista2-afd/L2-101.jff) · [`L2-101.json`](../../automatas/lista2-afd/L2-101.json) · [`L2-101.xml`](../../automatas/lista2-afd/L2-101.xml). Tipo según la definición: **AFD**, |Q| = 4, Σ = {a, b}, 8 transiciones.

**Diseño.** Búsqueda de aba: qⱼ = j símbolos del patrón ya coinciden. Tras una a con ab (q2 → q3) se acepta y q3 es absorbente. En q2, una b regresa a q0 porque abb no tiene sufijo que sea prefijo de aba.

| Estado | a | b | Significado |
|---|---|---|---|
| →q0 | q1 | q0 | ningún avance en el patrón |
| q1 | q1 | q2 | los últimos símbolos coinciden con «a» |
| q2 | q3 | q0 | los últimos símbolos coinciden con «ab» |
| *q3 | q3 | q3 | «aba» ya apareció |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `aba` | acepta | acepta | acepta |
| 2 | `baba` | acepta | acepta | acepta |
| 3 | `baaaba` | acepta | acepta | acepta |
| 4 | `baaaabbaba` | acepta | acepta | acepta |
| 5 | `aaabaaaabaa` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `aa` | rechaza | rechaza | rechaza |
| 8 | `bbaa` | rechaza | rechaza | rechaza |
| 9 | `baaabba` | rechaza | rechaza | rechaza |
| 10 | `aabbbbbbbaa` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `aba`: q0 -a→ q1 -b→ q2 -a→ q3 — ✔
2. `baba`: q0 -b→ q0 -a→ q1 -b→ q2 -a→ q3 — ✔
3. `baaaba`: q0 -b→ q0 -a→ q1 -a→ q1 -a→ q1 -b→ q2 -a→ q3 — ✔
4. `baaaabbaba`: q0 -b→ q0 -a→ q1 -a→ q1 -a→ q1 -a→ q1 -b→ q2 -b→ q0 -a→ q1 -b→ q2 -a→ q3 — ✔
5. `aaabaaaabaa`: q0 -a→ q1 -a→ q1 -a→ q1 -b→ q2 -a→ q3 -a→ q3 -a→ q3 -a→ q3 -b→ q3 -a→ q3 -a→ q3 — ✔
6. λ: q0 — ✘
7. `aa`: q0 -a→ q1 -a→ q1 — ✘
8. `bbaa`: q0 -b→ q0 -b→ q0 -a→ q1 -a→ q1 — ✘
9. `baaabba`: q0 -b→ q0 -a→ q1 -a→ q1 -a→ q1 -b→ q2 -b→ q0 -a→ q1 — ✘
10. `aabbbbbbbaa`: q0 -a→ q1 -a→ q1 -b→ q2 -b→ q0 -b→ q0 -b→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q1 -a→ q1 — ✘

</details>

Simulación paso a paso en JFLAP con `aba`: [ver captura](../../evidencias/jflap/pasos/L2-101.png).

<a id="problema-2-102"></a>

## Lista 2, problema 102

**Enunciado.** Palabras de Σ₃ que contienen abbbab.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Búsqueda de subcadena. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### Palabras de Σ₃ = {a,b} que contienen abbbab. — `L2-102`

Archivos: [`L2-102.jff`](../../automatas/lista2-afd/L2-102.jff) · [`L2-102.json`](../../automatas/lista2-afd/L2-102.json) · [`L2-102.xml`](../../automatas/lista2-afd/L2-102.xml). Tipo según la definición: **AFD**, |Q| = 7, Σ = {a, b}, 14 transiciones.

**Diseño.** Mismo principio de búsqueda: qj = j símbolos de abbbab ya coinciden. q6 es de aceptación y absorbente: una vez hallada la subcadena, lo que siga no importa.

| Estado | a | b |
|---|---|---|
| q1 | q1 | q2 |
| q3 | q1 | q4 |
| *q6 | q6 | q6 |
| q5 | q1 | q6 |
| q4 | q5 | q0 |
| q2 | q1 | q3 |
| →q0 | q1 | q0 |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `abbbab` | acepta | acepta | acepta |
| 2 | `babbbab` | acepta | acepta | acepta |
| 3 | `aaaabbbab` | acepta | acepta | acepta |
| 4 | `aababbbab` | acepta | acepta | acepta |
| 5 | `bbababaabbbab` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `ba` | rechaza | rechaza | rechaza |
| 8 | `baab` | rechaza | rechaza | rechaza |
| 9 | `baabaab` | rechaza | rechaza | rechaza |
| 10 | `aaaabaabbbb` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `abbbab`: q0 -a→ q1 -b→ q2 -b→ q3 -b→ q4 -a→ q5 -b→ q6 — ✔
2. `babbbab`: q0 -b→ q0 -a→ q1 -b→ q2 -b→ q3 -b→ q4 -a→ q5 -b→ q6 — ✔
3. `aaaabbbab`: q0 -a→ q1 -a→ q1 -a→ q1 -a→ q1 -b→ q2 -b→ q3 -b→ q4 -a→ q5 -b→ q6 — ✔
4. `aababbbab`: q0 -a→ q1 -a→ q1 -b→ q2 -a→ q1 -b→ q2 -b→ q3 -b→ q4 -a→ q5 -b→ q6 — ✔
5. `bbababaabbbab`: q0 -b→ q0 -b→ q0 -a→ q1 -b→ q2 -a→ q1 -b→ q2 -a→ q1 -a→ q1 -b→ q2 -b→ q3 -b→ q4 -a→ q5 -b→ q6 — ✔
6. λ: q0 — ✘
7. `ba`: q0 -b→ q0 -a→ q1 — ✘
8. `baab`: q0 -b→ q0 -a→ q1 -a→ q1 -b→ q2 — ✘
9. `baabaab`: q0 -b→ q0 -a→ q1 -a→ q1 -b→ q2 -a→ q1 -a→ q1 -b→ q2 — ✘
10. `aaaabaabbbb`: q0 -a→ q1 -a→ q1 -a→ q1 -a→ q1 -b→ q2 -a→ q1 -a→ q1 -b→ q2 -b→ q3 -b→ q4 -b→ q0 — ✘

</details>

Simulación paso a paso en JFLAP con `abbbab`: [ver captura](../../evidencias/jflap/pasos/L2-102.png).

<a id="problema-2-103"></a>

## Lista 2, problema 103

**Enunciado.** Palabras de Σ₃ que contienen aabbba.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Búsqueda de subcadena. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### Palabras de Σ₃ que contienen aabbba. — `L2-103`

Archivos: [`L2-103.jff`](../../automatas/lista2-afd/L2-103.jff) · [`L2-103.json`](../../automatas/lista2-afd/L2-103.json) · [`L2-103.xml`](../../automatas/lista2-afd/L2-103.xml). Tipo según la definición: **AFD**, |Q| = 7, Σ = {a, b}, 14 transiciones.

**Diseño.** Búsqueda de aabbba: qj = longitud del mayor prefijo del patrón que es sufijo de lo leído; q6 absorbente de aceptación.

| Estado | a | b |
|---|---|---|
| q1 | q2 | q0 |
| q3 | q1 | q4 |
| *q6 | q6 | q6 |
| q5 | q6 | q0 |
| q4 | q1 | q5 |
| q2 | q2 | q3 |
| →q0 | q1 | q0 |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `aabbba` | acepta | acepta | acepta |
| 2 | `baaabbba` | acepta | acepta | acepta |
| 3 | `bbaabbba` | acepta | acepta | acepta |
| 4 | `bbababaabbba` | acepta | acepta | acepta |
| 5 | `bbaaaaaaabaabbba` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `ba` | rechaza | rechaza | rechaza |
| 8 | `abab` | rechaza | rechaza | rechaza |
| 9 | `abbbaaa` | rechaza | rechaza | rechaza |
| 10 | `babbaaabaaa` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `aabbba`: q0 -a→ q1 -a→ q2 -b→ q3 -b→ q4 -b→ q5 -a→ q6 — ✔
2. `baaabbba`: q0 -b→ q0 -a→ q1 -a→ q2 -a→ q2 -b→ q3 -b→ q4 -b→ q5 -a→ q6 — ✔
3. `bbaabbba`: q0 -b→ q0 -b→ q0 -a→ q1 -a→ q2 -b→ q3 -b→ q4 -b→ q5 -a→ q6 — ✔
4. `bbababaabbba`: q0 -b→ q0 -b→ q0 -a→ q1 -b→ q0 -a→ q1 -b→ q0 -a→ q1 -a→ q2 -b→ q3 -b→ q4 -b→ q5 -a→ q6 — ✔
5. `bbaaaaaaabaabbba`: q0 -b→ q0 -b→ q0 -a→ q1 -a→ q2 -a→ q2 -a→ q2 -a→ q2 -a→ q2 -a→ q2 -b→ q3 -a→ q1 -a→ q2 -b→ q3 -b→ q4 -b→ q5 -a→ q6 — ✔
6. λ: q0 — ✘
7. `ba`: q0 -b→ q0 -a→ q1 — ✘
8. `abab`: q0 -a→ q1 -b→ q0 -a→ q1 -b→ q0 — ✘
9. `abbbaaa`: q0 -a→ q1 -b→ q0 -b→ q0 -b→ q0 -a→ q1 -a→ q2 -a→ q2 — ✘
10. `babbaaabaaa`: q0 -b→ q0 -a→ q1 -b→ q0 -b→ q0 -a→ q1 -a→ q2 -a→ q2 -b→ q3 -a→ q1 -a→ q2 -a→ q2 — ✘

</details>

Simulación paso a paso en JFLAP con `aabbba`: [ver captura](../../evidencias/jflap/pasos/L2-103.png).

<a id="problema-2-104"></a>

## Lista 2, problema 104

**Enunciado.** Las palabras de Σ₃ que inician con la cadena abbab.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Verificación de prefijo.

#### AFD — `L2-104`

Archivos: [`L2-104.jff`](../../automatas/lista2-afd/L2-104.jff) · [`L2-104.json`](../../automatas/lista2-afd/L2-104.json) · [`L2-104.xml`](../../automatas/lista2-afd/L2-104.xml). Tipo según la definición: **AFD**, |Q| = 7, Σ = {a, b}, 14 transiciones.

**Diseño.** Cadena lineal que compara el prefijo símbolo por símbolo; el primer desacuerdo lleva al rechazo absorbente. Al completar abbab, el estado de aceptación es absorbente.

| Estado | a | b | Significado |
|---|---|---|---|
| →q0 | q1 | q2 | se ha leído el prefijo «» |
| q1 | q2 | q3 | se ha leído el prefijo «a» |
| q2 | q2 | q2 | rechazo absorbente |
| q3 | q2 | q4 | se ha leído el prefijo «ab» |
| q4 | q5 | q2 | se ha leído el prefijo «abb» |
| q5 | q2 | q6 | se ha leído el prefijo «abba» |
| *q6 | q6 | q6 | el prefijo «abbab» ya apareció |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `abbab` | acepta | acepta | acepta |
| 2 | `abbabbb` | acepta | acepta | acepta |
| 3 | `abbabbaaa` | acepta | acepta | acepta |
| 4 | `abbabbbbbbb` | acepta | acepta | acepta |
| 5 | `abbabbbabababbab` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `ab` | rechaza | rechaza | rechaza |
| 8 | `abab` | rechaza | rechaza | rechaza |
| 9 | `ababaaa` | rechaza | rechaza | rechaza |
| 10 | `bbbaaabaaba` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `abbab`: q0 -a→ q1 -b→ q3 -b→ q4 -a→ q5 -b→ q6 — ✔
2. `abbabbb`: q0 -a→ q1 -b→ q3 -b→ q4 -a→ q5 -b→ q6 -b→ q6 -b→ q6 — ✔
3. `abbabbaaa`: q0 -a→ q1 -b→ q3 -b→ q4 -a→ q5 -b→ q6 -b→ q6 -a→ q6 -a→ q6 -a→ q6 — ✔
4. `abbabbbbbbb`: q0 -a→ q1 -b→ q3 -b→ q4 -a→ q5 -b→ q6 -b→ q6 -b→ q6 -b→ q6 -b→ q6 -b→ q6 -b→ q6 — ✔
5. `abbabbbabababbab`: q0 -a→ q1 -b→ q3 -b→ q4 -a→ q5 -b→ q6 -b→ q6 -b→ q6 -a→ q6 -b→ q6 -a→ q6 -b→ q6 -a→ q6 -b→ q6 -b→ q6 -a→ q6 -b→ q6 — ✔
6. λ: q0 — ✘
7. `ab`: q0 -a→ q1 -b→ q3 — ✘
8. `abab`: q0 -a→ q1 -b→ q3 -a→ q2 -b→ q2 — ✘
9. `ababaaa`: q0 -a→ q1 -b→ q3 -a→ q2 -b→ q2 -a→ q2 -a→ q2 -a→ q2 — ✘
10. `bbbaaabaaba`: q0 -b→ q2 -b→ q2 -b→ q2 -a→ q2 -a→ q2 -a→ q2 -b→ q2 -a→ q2 -a→ q2 -b→ q2 -a→ q2 — ✘

</details>

Simulación paso a paso en JFLAP con `abbab`: [ver captura](../../evidencias/jflap/pasos/L2-104.png).

<a id="problema-2-105"></a>

## Lista 2, problema 105

**Enunciado.** Las palabras de Σ₃ que terminan con la cadena abaa.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Búsqueda de sufijo con función de fallo.

#### AFD — `L2-105`

Archivos: [`L2-105.jff`](../../automatas/lista2-afd/L2-105.jff) · [`L2-105.json`](../../automatas/lista2-afd/L2-105.json) · [`L2-105.xml`](../../automatas/lista2-afd/L2-105.xml). Tipo según la definición: **AFD**, |Q| = 5, Σ = {a, b}, 10 transiciones.

**Diseño.** Búsqueda del sufijo abaa con función de fallo; q4 acepta y, si llega otro símbolo, se retrocede (con a a q1, porque solo la última a sirve como inicio; con b a q2, porque ab es prefijo).

| Estado | a | b | Significado |
|---|---|---|---|
| →q0 | q1 | q0 | ningún avance en el patrón |
| q1 | q1 | q2 | los últimos símbolos coinciden con «a» |
| q2 | q3 | q0 | los últimos símbolos coinciden con «ab» |
| q3 | q4 | q2 | los últimos símbolos coinciden con «aba» |
| *q4 | q1 | q2 | los últimos símbolos coinciden con «abaa» |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `abaa` | acepta | acepta | acepta |
| 2 | `baabaa` | acepta | acepta | acepta |
| 3 | `bbabaa` | acepta | acepta | acepta |
| 4 | `aabbaaabaa` | acepta | acepta | acepta |
| 5 | `bbaaaaaaaabaa` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `bb` | rechaza | rechaza | rechaza |
| 8 | `aabb` | rechaza | rechaza | rechaza |
| 9 | `aabbbab` | rechaza | rechaza | rechaza |
| 10 | `babaaababba` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `abaa`: q0 -a→ q1 -b→ q2 -a→ q3 -a→ q4 — ✔
2. `baabaa`: q0 -b→ q0 -a→ q1 -a→ q1 -b→ q2 -a→ q3 -a→ q4 — ✔
3. `bbabaa`: q0 -b→ q0 -b→ q0 -a→ q1 -b→ q2 -a→ q3 -a→ q4 — ✔
4. `aabbaaabaa`: q0 -a→ q1 -a→ q1 -b→ q2 -b→ q0 -a→ q1 -a→ q1 -a→ q1 -b→ q2 -a→ q3 -a→ q4 — ✔
5. `bbaaaaaaaabaa`: q0 -b→ q0 -b→ q0 -a→ q1 -a→ q1 -a→ q1 -a→ q1 -a→ q1 -a→ q1 -a→ q1 -a→ q1 -b→ q2 -a→ q3 -a→ q4 — ✔
6. λ: q0 — ✘
7. `bb`: q0 -b→ q0 -b→ q0 — ✘
8. `aabb`: q0 -a→ q1 -a→ q1 -b→ q2 -b→ q0 — ✘
9. `aabbbab`: q0 -a→ q1 -a→ q1 -b→ q2 -b→ q0 -b→ q0 -a→ q1 -b→ q2 — ✘
10. `babaaababba`: q0 -b→ q0 -a→ q1 -b→ q2 -a→ q3 -a→ q4 -a→ q1 -b→ q2 -a→ q3 -b→ q2 -b→ q0 -a→ q1 — ✘

</details>

Simulación paso a paso en JFLAP con `abaa`: [ver captura](../../evidencias/jflap/pasos/L2-105.png).

<a id="problema-2-106"></a>

## Lista 2, problema 106

**Enunciado.** Palabras de Σ₁ que incluyen 1101001.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Búsqueda de subcadena. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### Palabras de Σ₁ que incluyen la subcadena 1101001. — `L2-106`

Archivos: [`L2-106.jff`](../../automatas/lista2-afd/L2-106.jff) · [`L2-106.json`](../../automatas/lista2-afd/L2-106.json) · [`L2-106.xml`](../../automatas/lista2-afd/L2-106.xml). Tipo según la definición: **AFD**, |Q| = 8, Σ = {0, 1, 2}, 24 transiciones.

**Diseño.** Búsqueda de 1101001: qj = j símbolos del patrón coinciden; el 2 no aparece en el patrón y reinicia la búsqueda; q7 absorbente de aceptación.

| Estado | 0 | 1 | 2 |
|---|---|---|---|
| q1 | q0 | q2 | q0 |
| q3 | q0 | q4 | q0 |
| q6 | q0 | q7 | q0 |
| *q7 | q7 | q7 | q7 |
| q5 | q6 | q1 | q0 |
| q4 | q5 | q2 | q0 |
| q2 | q3 | q2 | q0 |
| →q0 | q0 | q1 | q0 |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `1101001` | acepta | acepta | acepta |
| 2 | `221101001` | acepta | acepta | acepta |
| 3 | `2101101001` | acepta | acepta | acepta |
| 4 | `01112121101001` | acepta | acepta | acepta |
| 5 | `20202201101001` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `00` | rechaza | rechaza | rechaza |
| 8 | `2002` | rechaza | rechaza | rechaza |
| 9 | `2121000` | rechaza | rechaza | rechaza |
| 10 | `22001102102` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `1101001`: q0 -1→ q1 -1→ q2 -0→ q3 -1→ q4 -0→ q5 -0→ q6 -1→ q7 — ✔
2. `221101001`: q0 -2→ q0 -2→ q0 -1→ q1 -1→ q2 -0→ q3 -1→ q4 -0→ q5 -0→ q6 -1→ q7 — ✔
3. `2101101001`: q0 -2→ q0 -1→ q1 -0→ q0 -1→ q1 -1→ q2 -0→ q3 -1→ q4 -0→ q5 -0→ q6 -1→ q7 — ✔
4. `01112121101001`: q0 -0→ q0 -1→ q1 -1→ q2 -1→ q2 -2→ q0 -1→ q1 -2→ q0 -1→ q1 -1→ q2 -0→ q3 -1→ q4 -0→ q5 -0→ q6 -1→ q7 — ✔
5. `20202201101001`: q0 -2→ q0 -0→ q0 -2→ q0 -0→ q0 -2→ q0 -2→ q0 -0→ q0 -1→ q1 -1→ q2 -0→ q3 -1→ q4 -0→ q5 -0→ q6 -1→ q7 — ✔
6. λ: q0 — ✘
7. `00`: q0 -0→ q0 -0→ q0 — ✘
8. `2002`: q0 -2→ q0 -0→ q0 -0→ q0 -2→ q0 — ✘
9. `2121000`: q0 -2→ q0 -1→ q1 -2→ q0 -1→ q1 -0→ q0 -0→ q0 -0→ q0 — ✘
10. `22001102102`: q0 -2→ q0 -2→ q0 -0→ q0 -0→ q0 -1→ q1 -1→ q2 -0→ q3 -2→ q0 -1→ q1 -0→ q0 -2→ q0 — ✘

</details>

Simulación paso a paso en JFLAP con `00`: [ver captura](../../evidencias/jflap/pasos/L2-106.png).

<a id="problema-2-107"></a>

## Lista 2, problema 107

**Enunciado.** Palabras de Σ₁ con 0101 y con 021.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Producto de dos búsquedas. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### Palabras de Σ₁ que incluyen al menos una vez 0101 y al menos una vez 021. — `L2-107`

Archivos: [`L2-107.jff`](../../automatas/lista2-afd/L2-107.jff) · [`L2-107.json`](../../automatas/lista2-afd/L2-107.json) · [`L2-107.xml`](../../automatas/lista2-afd/L2-107.xml). Tipo según la definición: **AFD**, |Q| = 13, Σ = {0, 1, 2}, 39 transiciones.

**Diseño.** Intersección por autómata producto: cada estado es un par (avance en 0101, avance en 021), y acepta solo cuando ambos patrones ya aparecieron. Se minimizó por particiones a 13 estados.

<details><summary>Tabla de transiciones (13 estados)</summary>

| Estado | 0 | 1 | 2 |
|---|---|---|---|
| q9 | q11 | q5 | q5 |
| q1 | q1 | q2 | q3 |
| q10 | q8 | q12 | q6 |
| q7 | q7 | q9 | q5 |
| q3 | q1 | q5 | q0 |
| q6 | q8 | q6 | q6 |
| q11 | q7 | q12 | q5 |
| q5 | q7 | q5 | q5 |
| *q12 | q12 | q12 | q12 |
| q4 | q1 | q6 | q3 |
| q8 | q8 | q6 | q10 |
| q2 | q4 | q0 | q0 |
| →q0 | q1 | q0 | q0 |

</details>

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `0101021` | acepta | acepta | acepta |
| 2 | `110101021` | acepta | acepta | acepta |
| 3 | `220210101` | acepta | acepta | acepta |
| 4 | `0200220101021` | acepta | acepta | acepta |
| 5 | `002021010220101` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `01` | rechaza | rechaza | rechaza |
| 8 | `0011` | rechaza | rechaza | rechaza |
| 9 | `2101101` | rechaza | rechaza | rechaza |
| 10 | `22121121201` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `0101021`: q0 -0→ q1 -1→ q2 -0→ q4 -1→ q6 -0→ q8 -2→ q10 -1→ q12 — ✔
2. `110101021`: q0 -1→ q0 -1→ q0 -0→ q1 -1→ q2 -0→ q4 -1→ q6 -0→ q8 -2→ q10 -1→ q12 — ✔
3. `220210101`: q0 -2→ q0 -2→ q0 -0→ q1 -2→ q3 -1→ q5 -0→ q7 -1→ q9 -0→ q11 -1→ q12 — ✔
4. `0200220101021`: q0 -0→ q1 -2→ q3 -0→ q1 -0→ q1 -2→ q3 -2→ q0 -0→ q1 -1→ q2 -0→ q4 -1→ q6 -0→ q8 -2→ q10 -1→ q12 — ✔
5. `002021010220101`: q0 -0→ q1 -0→ q1 -2→ q3 -0→ q1 -2→ q3 -1→ q5 -0→ q7 -1→ q9 -0→ q11 -2→ q5 -2→ q5 -0→ q7 -1→ q9 -0→ q11 -1→ q12 — ✔
6. λ: q0 — ✘
7. `01`: q0 -0→ q1 -1→ q2 — ✘
8. `0011`: q0 -0→ q1 -0→ q1 -1→ q2 -1→ q0 — ✘
9. `2101101`: q0 -2→ q0 -1→ q0 -0→ q1 -1→ q2 -1→ q0 -0→ q1 -1→ q2 — ✘
10. `22121121201`: q0 -2→ q0 -2→ q0 -1→ q0 -2→ q0 -1→ q0 -1→ q0 -2→ q0 -1→ q0 -2→ q0 -0→ q1 -1→ q2 — ✘

</details>

Simulación paso a paso en JFLAP con `01`: [ver captura](../../evidencias/jflap/pasos/L2-107.png).

<a id="problema-2-108"></a>

## Lista 2, problema 108

**Enunciado.** Las palabras de Σ₂ que incluyen al menos una vez abbcb y al menos una vez cbaabb, sin traslape (abbcbaabb no pertenece).

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Producto de búsquedas que exige ocurrencias disjuntas.

#### AFD — `L2-108`

Archivos: [`L2-108.jff`](../../automatas/lista2-afd/L2-108.jff) · [`L2-108.json`](../../automatas/lista2-afd/L2-108.json) · [`L2-108.xml`](../../automatas/lista2-afd/L2-108.xml). Tipo según la definición: **AFD**, |Q| = 37, Σ = {a, b, c, 0, 1}, 185 transiciones.

**Diseño.** El lenguaje es la unión de Σ*·abbcb·Σ*·cbaabb·Σ* y Σ*·cbaabb·Σ*·abbcb·Σ*: una ocurrencia completa de un patrón seguida, sin compartir símbolos, de una del otro. Se construyó el AFND-λ de esa unión (el del problema 162-188 correspondiente), se determinizó por subconjuntos y se minimizó con Hopcroft. A diferencia del 109, al completar un patrón la búsqueda del otro recomienza desde cero en lugar de reutilizar el traslape.

<details><summary>Tabla de transiciones (37 estados)</summary>

| Estado | a | b | c | 0 | 1 |
|---|---|---|---|---|---|
| →q0 | q1 | q0 | q2 | q0 | q0 |
| q1 | q1 | q3 | q2 | q0 | q0 |
| q2 | q1 | q4 | q2 | q0 | q0 |
| q3 | q1 | q5 | q2 | q0 | q0 |
| q4 | q6 | q0 | q2 | q0 | q0 |
| q5 | q1 | q0 | q7 | q0 | q0 |
| q6 | q8 | q3 | q2 | q0 | q0 |
| q7 | q1 | q9 | q2 | q0 | q0 |
| q8 | q1 | q10 | q2 | q0 | q0 |
| q9 | q11 | q12 | q13 | q12 | q12 |
| q10 | q1 | q14 | q2 | q0 | q0 |
| q11 | q15 | q12 | q13 | q12 | q12 |
| q12 | q12 | q12 | q13 | q12 | q12 |
| q13 | q12 | q16 | q13 | q12 | q12 |
| q14 | q17 | q18 | q19 | q18 | q18 |
| q15 | q12 | q20 | q13 | q12 | q12 |
| q16 | q21 | q12 | q13 | q12 | q12 |
| q17 | q17 | q22 | q18 | q18 | q18 |
| q18 | q17 | q18 | q18 | q18 | q18 |
| q19 | q17 | q23 | q18 | q18 | q18 |
| q20 | q12 | q23 | q13 | q12 | q12 |
| q21 | q24 | q12 | q13 | q12 | q12 |
| q22 | q17 | q25 | q18 | q18 | q18 |
| q23 | q26 | q23 | q27 | q23 | q23 |
| q24 | q12 | q28 | q13 | q12 | q12 |
| q25 | q17 | q18 | q29 | q18 | q18 |
| q26 | q26 | q30 | q27 | q23 | q23 |
| q27 | q26 | q31 | q27 | q23 | q23 |
| q28 | q12 | q32 | q13 | q12 | q12 |
| q29 | q17 | q32 | q18 | q18 | q18 |
| q30 | q26 | q33 | q27 | q23 | q23 |
| q31 | q34 | q23 | q27 | q23 | q23 |
| *q32 | q32 | q32 | q32 | q32 | q32 |
| q33 | q26 | q23 | q35 | q23 | q23 |
| q34 | q36 | q30 | q27 | q23 | q23 |
| q35 | q26 | q32 | q27 | q23 | q23 |
| q36 | q26 | q35 | q27 | q23 | q23 |

</details>

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `abbcbcbaabb` | acepta | acepta | acepta |
| 2 | `a1abbcbcbaabb` | acepta | acepta | acepta |
| 3 | `1bccbaabbabbcb` | acepta | acepta | acepta |
| 4 | `ca0c000abbcbcbaabb` | acepta | acepta | acepta |
| 5 | `acbcccc1bb1abbcbcbaabb` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `cb` | rechaza | rechaza | rechaza |
| 8 | `aaa1` | rechaza | rechaza | rechaza |
| 9 | `caacb00` | rechaza | rechaza | rechaza |
| 10 | `101aa11cba0` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `abbcbcbaabb`: q0 -a→ q1 -b→ q3 -b→ q5 -c→ q7 -b→ q9 -c→ q13 -b→ q16 -a→ q21 -a→ q24 -b→ q28 -b→ q32 — ✔
2. `a1abbcbcbaabb`: q0 -a→ q1 -1→ q0 -a→ q1 -b→ q3 -b→ q5 -c→ q7 -b→ q9 -c→ q13 -b→ q16 -a→ q21 -a→ q24 -b→ q28 -b→ q32 — ✔
3. `1bccbaabbabbcb`: q0 -1→ q0 -b→ q0 -c→ q2 -c→ q2 -b→ q4 -a→ q6 -a→ q8 -b→ q10 -b→ q14 -a→ q17 -b→ q22 -b→ q25 -c→ q29 -b→ q32 — ✔
4. `ca0c000abbcbcbaabb`: q0 -c→ q2 -a→ q1 -0→ q0 -c→ q2 -0→ q0 -0→ q0 -0→ q0 -a→ q1 -b→ q3 -b→ q5 -c→ q7 -b→ q9 -c→ q13 -b→ q16 -a→ q21 -a→ q24 -b→ q28 -b→ q32 — ✔
5. `acbcccc1bb1abbcbcbaabb`: q0 -a→ q1 -c→ q2 -b→ q4 -c→ q2 -c→ q2 -c→ q2 -c→ q2 -1→ q0 -b→ q0 -b→ q0 -1→ q0 -a→ q1 -b→ q3 -b→ q5 -c→ q7 -b→ q9 -c→ q13 -b→ q16 -a→ q21 -a→ q24 -b→ q28 -b→ q32 — ✔
6. λ: q0 — ✘
7. `cb`: q0 -c→ q2 -b→ q4 — ✘
8. `aaa1`: q0 -a→ q1 -a→ q1 -a→ q1 -1→ q0 — ✘
9. `caacb00`: q0 -c→ q2 -a→ q1 -a→ q1 -c→ q2 -b→ q4 -0→ q0 -0→ q0 — ✘
10. `101aa11cba0`: q0 -1→ q0 -0→ q0 -1→ q0 -a→ q1 -a→ q1 -1→ q0 -1→ q0 -c→ q2 -b→ q4 -a→ q6 -0→ q0 — ✘

</details>

Simulación paso a paso en JFLAP con `cb`: [ver captura](../../evidencias/jflap/pasos/L2-108.png).

<a id="problema-2-109"></a>

## Lista 2, problema 109

**Enunciado.** Σ₂: abbcb y cbaabb, con traslape.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Producto de búsquedas con traslape. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### Palabras de Σ₂ = {a,b,c,0,1} que incluyen abbcb y cbaabb, pudiendo traslaparse. — `L2-109`

Archivos: [`L2-109.jff`](../../automatas/lista2-afd/L2-109.jff) · [`L2-109.json`](../../automatas/lista2-afd/L2-109.json) · [`L2-109.xml`](../../automatas/lista2-afd/L2-109.xml). Tipo según la definición: **AFD**, |Q| = 22, Σ = {0, 1, a, b, c}, 110 transiciones.

**Diseño.** Producto de dos búsquedas con función de fallo; esta detecta de forma natural los traslapes (abbcbaabb cuenta). Cada estado guarda el avance en cada patrón. Minimizado de 56 a 22 estados.

<details><summary>Tabla de transiciones (22 estados)</summary>

| Estado | 0 | 1 | a | b | c |
|---|---|---|---|---|---|
| q9 | q12 | q12 | q11 | q12 | q13 |
| q3 | q0 | q0 | q1 | q5 | q2 |
| q7 | q0 | q0 | q1 | q9 | q2 |
| q13 | q12 | q12 | q12 | q9 | q13 |
| q19 | q12 | q12 | q12 | q21 | q13 |
| q11 | q12 | q12 | q15 | q12 | q13 |
| q14 | q17 | q17 | q16 | q17 | q18 |
| q6 | q0 | q0 | q8 | q3 | q2 |
| →q0 | q0 | q0 | q1 | q0 | q2 |
| q18 | q17 | q17 | q16 | q21 | q17 |
| q10 | q0 | q0 | q1 | q14 | q2 |
| q5 | q0 | q0 | q1 | q0 | q7 |
| q8 | q0 | q0 | q1 | q10 | q2 |
| q2 | q0 | q0 | q1 | q4 | q2 |
| q15 | q12 | q12 | q12 | q19 | q13 |
| q20 | q17 | q17 | q16 | q14 | q17 |
| q1 | q0 | q0 | q1 | q3 | q2 |
| *q21 | q21 | q21 | q21 | q21 | q21 |
| q17 | q17 | q17 | q16 | q17 | q17 |
| q16 | q17 | q17 | q16 | q20 | q17 |
| q12 | q12 | q12 | q12 | q12 | q13 |
| q4 | q0 | q0 | q6 | q0 | q2 |

</details>

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `cbaabbcb` | acepta | acepta | acepta |
| 2 | `10cbaabbcb` | acepta | acepta | acepta |
| 3 | `c011cbaabbcb` | acepta | acepta | acepta |
| 4 | `001a10acbaabbcb` | acepta | acepta | acepta |
| 5 | `baabaa11aa1cbaabbcb` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `ac` | rechaza | rechaza | rechaza |
| 8 | `b1cb` | rechaza | rechaza | rechaza |
| 9 | `bb0bcab` | rechaza | rechaza | rechaza |
| 10 | `cabb0b011c1` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `cbaabbcb`: q0 -c→ q2 -b→ q4 -a→ q6 -a→ q8 -b→ q10 -b→ q14 -c→ q18 -b→ q21 — ✔
2. `10cbaabbcb`: q0 -1→ q0 -0→ q0 -c→ q2 -b→ q4 -a→ q6 -a→ q8 -b→ q10 -b→ q14 -c→ q18 -b→ q21 — ✔
3. `c011cbaabbcb`: q0 -c→ q2 -0→ q0 -1→ q0 -1→ q0 -c→ q2 -b→ q4 -a→ q6 -a→ q8 -b→ q10 -b→ q14 -c→ q18 -b→ q21 — ✔
4. `001a10acbaabbcb`: q0 -0→ q0 -0→ q0 -1→ q0 -a→ q1 -1→ q0 -0→ q0 -a→ q1 -c→ q2 -b→ q4 -a→ q6 -a→ q8 -b→ q10 -b→ q14 -c→ q18 -b→ q21 — ✔
5. `baabaa11aa1cbaabbcb`: q0 -b→ q0 -a→ q1 -a→ q1 -b→ q3 -a→ q1 -a→ q1 -1→ q0 -1→ q0 -a→ q1 -a→ q1 -1→ q0 -c→ q2 -b→ q4 -a→ q6 -a→ q8 -b→ q10 -b→ q14 -c→ q18 -b→ q21 — ✔
6. λ: q0 — ✘
7. `ac`: q0 -a→ q1 -c→ q2 — ✘
8. `b1cb`: q0 -b→ q0 -1→ q0 -c→ q2 -b→ q4 — ✘
9. `bb0bcab`: q0 -b→ q0 -b→ q0 -0→ q0 -b→ q0 -c→ q2 -a→ q1 -b→ q3 — ✘
10. `cabb0b011c1`: q0 -c→ q2 -a→ q1 -b→ q3 -b→ q5 -0→ q0 -b→ q0 -0→ q0 -1→ q0 -1→ q0 -c→ q2 -1→ q0 — ✘

</details>

Simulación paso a paso en JFLAP con `ac`: [ver captura](../../evidencias/jflap/pasos/L2-109.png).

<a id="problema-2-110"></a>

## Lista 2, problema 110

**Enunciado.** Las palabras de Σ₁ que contienen exactamente tres veces la subcadena 01.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Contador saturado de ocurrencias de 01.

#### AFD — `L2-110`

Archivos: [`L2-110.jff`](../../automatas/lista2-afd/L2-110.jff) · [`L2-110.json`](../../automatas/lista2-afd/L2-110.json) · [`L2-110.xml`](../../automatas/lista2-afd/L2-110.xml). Tipo según la definición: **AFD**, |Q| = 9, Σ = {0, 1, 2}, 27 transiciones.

**Diseño.** El estado es el par (¿el último símbolo fue 0?, ocurrencias de 01 vistas, saturadas en 4). 01 no puede traslaparse consigo mismo, así que cada 1 precedido de 0 cuenta una ocurrencia nueva. Acepta con contador 3; el contador 4 representa «más de tres» y es de rechazo.

| Estado | 0 | 1 | 2 | Significado |
|---|---|---|---|---|
| →q0 | q1 | q0 | q0 | 0 ocurrencias; último símbolo distinto de 0 |
| q1 | q1 | q2 | q0 | 0 ocurrencias; último símbolo 0 |
| q2 | q3 | q2 | q2 | 1 ocurrencias; último símbolo distinto de 0 |
| q3 | q3 | q4 | q2 | 1 ocurrencias; último símbolo 0 |
| q4 | q5 | q4 | q4 | 2 ocurrencias; último símbolo distinto de 0 |
| q5 | q5 | q6 | q4 | 2 ocurrencias; último símbolo 0 |
| *q6 | q7 | q6 | q6 | 3 ocurrencias; último símbolo distinto de 0 |
| *q7 | q7 | q8 | q6 | 3 ocurrencias; último símbolo 0 |
| q8 | q8 | q8 | q8 | más de 3 ocurrencias; último símbolo distinto de 0 o bien más de 3 ocurrencias; último símbolo 0 |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `010101` | acepta | acepta | acepta |
| 2 | `11010101` | acepta | acepta | acepta |
| 3 | `111010101` | acepta | acepta | acepta |
| 4 | `1012210101` | acepta | acepta | acepta |
| 5 | `200111202210101` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `00` | rechaza | rechaza | rechaza |
| 8 | `2100` | rechaza | rechaza | rechaza |
| 9 | `2220112` | rechaza | rechaza | rechaza |
| 10 | `22101111011` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `010101`: q0 -0→ q1 -1→ q2 -0→ q3 -1→ q4 -0→ q5 -1→ q6 — ✔
2. `11010101`: q0 -1→ q0 -1→ q0 -0→ q1 -1→ q2 -0→ q3 -1→ q4 -0→ q5 -1→ q6 — ✔
3. `111010101`: q0 -1→ q0 -1→ q0 -1→ q0 -0→ q1 -1→ q2 -0→ q3 -1→ q4 -0→ q5 -1→ q6 — ✔
4. `1012210101`: q0 -1→ q0 -0→ q1 -1→ q2 -2→ q2 -2→ q2 -1→ q2 -0→ q3 -1→ q4 -0→ q5 -1→ q6 — ✔
5. `200111202210101`: q0 -2→ q0 -0→ q1 -0→ q1 -1→ q2 -1→ q2 -1→ q2 -2→ q2 -0→ q3 -2→ q2 -2→ q2 -1→ q2 -0→ q3 -1→ q4 -0→ q5 -1→ q6 — ✔
6. λ: q0 — ✘
7. `00`: q0 -0→ q1 -0→ q1 — ✘
8. `2100`: q0 -2→ q0 -1→ q0 -0→ q1 -0→ q1 — ✘
9. `2220112`: q0 -2→ q0 -2→ q0 -2→ q0 -0→ q1 -1→ q2 -1→ q2 -2→ q2 — ✘
10. `22101111011`: q0 -2→ q0 -2→ q0 -1→ q0 -0→ q1 -1→ q2 -1→ q2 -1→ q2 -1→ q2 -0→ q3 -1→ q4 -1→ q4 — ✘

</details>

Simulación paso a paso en JFLAP con `010101`: [ver captura](../../evidencias/jflap/pasos/L2-110.png).

<a id="problema-2-111"></a>

## Lista 2, problema 111

**Enunciado.** Exactamente tres veces 01002.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Contador de ocurrencias. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### Palabras de Σ₁ que contienen exactamente tres veces 01002. — `L2-111`

Archivos: [`L2-111.jff`](../../automatas/lista2-afd/L2-111.jff) · [`L2-111.json`](../../automatas/lista2-afd/L2-111.json) · [`L2-111.xml`](../../automatas/lista2-afd/L2-111.xml). Tipo según la definición: **AFD**, |Q| = 21, Σ = {0, 1, 2}, 63 transiciones.

**Diseño.** El estado es el par (avance en la búsqueda de 01002, ocurrencias vistas, saturadas en 4). 01002 no se traslapa consigo mismo. Acepta si el contador vale 3 al terminar.

<details><summary>Tabla de transiciones (21 estados)</summary>

| Estado | 0 | 1 | 2 |
|---|---|---|---|
| q9 | q6 | q7 | q10 |
| q3 | q4 | q2 | q0 |
| q7 | q8 | q5 | q5 |
| q13 | q14 | q12 | q10 |
| *q19 | q16 | q17 | q20 |
| q11 | q11 | q12 | q10 |
| q14 | q11 | q12 | q15 |
| q6 | q6 | q7 | q5 |
| →q0 | q1 | q0 | q0 |
| *q18 | q19 | q17 | q15 |
| q10 | q11 | q10 | q10 |
| q5 | q6 | q5 | q5 |
| q8 | q9 | q7 | q5 |
| q2 | q3 | q0 | q0 |
| *q15 | q16 | q15 | q15 |
| q20 | q20 | q20 | q20 |
| q1 | q1 | q2 | q0 |
| *q17 | q18 | q15 | q15 |
| *q16 | q16 | q17 | q15 |
| q12 | q13 | q10 | q10 |
| q4 | q1 | q2 | q5 |

</details>

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `010020100201002` | acepta | acepta | acepta |
| 2 | `21010020100201002` | acepta | acepta | acepta |
| 3 | `111010020100201002` | acepta | acepta | acepta |
| 4 | `222210010020100201002` | acepta | acepta | acepta |
| 5 | `01211212221010020100201002` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `02` | rechaza | rechaza | rechaza |
| 8 | `0000` | rechaza | rechaza | rechaza |
| 9 | `2222012` | rechaza | rechaza | rechaza |
| 10 | `02201102122` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `010020100201002`: q0 -0→ q1 -1→ q2 -0→ q3 -0→ q4 -2→ q5 -0→ q6 -1→ q7 -0→ q8 -0→ q9 -2→ q10 -0→ q11 -1→ q12 -0→ q13 -0→ q14 -2→ q15 — ✔
2. `21010020100201002`: q0 -2→ q0 -1→ q0 -0→ q1 -1→ q2 -0→ q3 -0→ q4 -2→ q5 -0→ q6 -1→ q7 -0→ q8 -0→ q9 -2→ q10 -0→ q11 -1→ q12 -0→ q13 -0→ q14 -2→ q15 — ✔
3. `111010020100201002`: q0 -1→ q0 -1→ q0 -1→ q0 -0→ q1 -1→ q2 -0→ q3 -0→ q4 -2→ q5 -0→ q6 -1→ q7 -0→ q8 -0→ q9 -2→ q10 -0→ q11 -1→ q12 -0→ q13 -0→ q14 -2→ q15 — ✔
4. `222210010020100201002`: q0 -2→ q0 -2→ q0 -2→ q0 -2→ q0 -1→ q0 -0→ q1 -0→ q1 -1→ q2 -0→ q3 -0→ q4 -2→ q5 -0→ q6 -1→ q7 -0→ q8 -0→ q9 -2→ q10 -0→ q11 -1→ q12 -0→ q13 -0→ q14 -2→ q15 — ✔
5. `01211212221010020100201002`: q0 -0→ q1 -1→ q2 -2→ q0 -1→ q0 -1→ q0 -2→ q0 -1→ q0 -2→ q0 -2→ q0 -2→ q0 -1→ q0 -0→ q1 -1→ q2 -0→ q3 -0→ q4 -2→ q5 -0→ q6 -1→ q7 -0→ q8 -0→ q9 -2→ q10 -0→ q11 -1→ q12 -0→ q13 -0→ q14 -2→ q15 — ✔
6. λ: q0 — ✘
7. `02`: q0 -0→ q1 -2→ q0 — ✘
8. `0000`: q0 -0→ q1 -0→ q1 -0→ q1 -0→ q1 — ✘
9. `2222012`: q0 -2→ q0 -2→ q0 -2→ q0 -2→ q0 -0→ q1 -1→ q2 -2→ q0 — ✘
10. `02201102122`: q0 -0→ q1 -2→ q0 -2→ q0 -0→ q1 -1→ q2 -1→ q0 -0→ q1 -2→ q0 -1→ q0 -2→ q0 -2→ q0 — ✘

</details>

Simulación paso a paso en JFLAP con `02`: [ver captura](../../evidencias/jflap/pasos/L2-111.png).

<a id="problema-2-112"></a>

## Lista 2, problema 112

**Enunciado.** Dos veces 010 sin traslape.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Contador sin traslape. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### Palabras de Σ₁ que contienen dos veces 010 sin traslape (01010 no pertenece; 010010 sí). — `L2-112`

Archivos: [`L2-112.jff`](../../automatas/lista2-afd/L2-112.jff) · [`L2-112.json`](../../automatas/lista2-afd/L2-112.json) · [`L2-112.xml`](../../automatas/lista2-afd/L2-112.xml). Tipo según la definición: **AFD**, |Q| = 10, Σ = {0, 1, 2}, 30 transiciones.

**Diseño.** El estado es (avance en 010, ocurrencias contadas). Al completar una ocurrencia la búsqueda vuelve a cero, de modo que sus símbolos no se reutilizan. Acepta con contador exactamente 2.

| Estado | 0 | 1 | 2 |
|---|---|---|---|
| q9 | q9 | q9 | q9 |
| q1 | q1 | q2 | q0 |
| q3 | q4 | q3 | q3 |
| *q6 | q7 | q6 | q6 |
| *q7 | q7 | q8 | q6 |
| q5 | q6 | q3 | q3 |
| q4 | q4 | q5 | q3 |
| *q8 | q9 | q6 | q6 |
| q2 | q3 | q0 | q0 |
| →q0 | q1 | q0 | q0 |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `010010` | acepta | acepta | acepta |
| 2 | `0010010` | acepta | acepta | acepta |
| 3 | `211010010` | acepta | acepta | acepta |
| 4 | `0121011010010` | acepta | acepta | acepta |
| 5 | `1101201220010010` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `00` | rechaza | rechaza | rechaza |
| 8 | `0212` | rechaza | rechaza | rechaza |
| 9 | `2021021` | rechaza | rechaza | rechaza |
| 10 | `10110212122` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `010010`: q0 -0→ q1 -1→ q2 -0→ q3 -0→ q4 -1→ q5 -0→ q6 — ✔
2. `0010010`: q0 -0→ q1 -0→ q1 -1→ q2 -0→ q3 -0→ q4 -1→ q5 -0→ q6 — ✔
3. `211010010`: q0 -2→ q0 -1→ q0 -1→ q0 -0→ q1 -1→ q2 -0→ q3 -0→ q4 -1→ q5 -0→ q6 — ✔
4. `0121011010010`: q0 -0→ q1 -1→ q2 -2→ q0 -1→ q0 -0→ q1 -1→ q2 -1→ q0 -0→ q1 -1→ q2 -0→ q3 -0→ q4 -1→ q5 -0→ q6 — ✔
5. `1101201220010010`: q0 -1→ q0 -1→ q0 -0→ q1 -1→ q2 -2→ q0 -0→ q1 -1→ q2 -2→ q0 -2→ q0 -0→ q1 -0→ q1 -1→ q2 -0→ q3 -0→ q4 -1→ q5 -0→ q6 — ✔
6. λ: q0 — ✘
7. `00`: q0 -0→ q1 -0→ q1 — ✘
8. `0212`: q0 -0→ q1 -2→ q0 -1→ q0 -2→ q0 — ✘
9. `2021021`: q0 -2→ q0 -0→ q1 -2→ q0 -1→ q0 -0→ q1 -2→ q0 -1→ q0 — ✘
10. `10110212122`: q0 -1→ q0 -0→ q1 -1→ q2 -1→ q0 -0→ q1 -2→ q0 -1→ q0 -2→ q0 -1→ q0 -2→ q0 -2→ q0 — ✘

</details>

Simulación paso a paso en JFLAP con `010010`: [ver captura](../../evidencias/jflap/pasos/L2-112.png).

<a id="problema-2-113"></a>

## Lista 2, problema 113

**Enunciado.** Dos veces 010 con traslape.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Contador con traslape. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### Palabras de Σ₁ que contienen dos veces 010, pudiendo traslaparse. — `L2-113`

Archivos: [`L2-113.jff`](../../automatas/lista2-afd/L2-113.jff) · [`L2-113.json`](../../automatas/lista2-afd/L2-113.json) · [`L2-113.xml`](../../automatas/lista2-afd/L2-113.xml). Tipo según la definición: **AFD**, |Q| = 10, Σ = {0, 1, 2}, 30 transiciones.

**Diseño.** Igual que el 112, pero tras cada ocurrencia se sigue la función de fallo (el último 0 sirve de inicio de la siguiente), por lo que 01010 sí pertenece.

| Estado | 0 | 1 | 2 |
|---|---|---|---|
| q9 | q9 | q9 | q9 |
| q1 | q1 | q2 | q0 |
| q3 | q3 | q4 | q5 |
| *q6 | q6 | q7 | q8 |
| *q7 | q9 | q8 | q8 |
| q5 | q3 | q5 | q5 |
| q4 | q6 | q5 | q5 |
| *q8 | q6 | q8 | q8 |
| q2 | q3 | q0 | q0 |
| →q0 | q1 | q0 | q0 |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `01010` | acepta | acepta | acepta |
| 2 | `201010` | acepta | acepta | acepta |
| 3 | `20201010` | acepta | acepta | acepta |
| 4 | `112120201010` | acepta | acepta | acepta |
| 5 | `1011110110201010` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `20` | rechaza | rechaza | rechaza |
| 8 | `0002` | rechaza | rechaza | rechaza |
| 9 | `1120010` | rechaza | rechaza | rechaza |
| 10 | `02211121220` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `01010`: q0 -0→ q1 -1→ q2 -0→ q3 -1→ q4 -0→ q6 — ✔
2. `201010`: q0 -2→ q0 -0→ q1 -1→ q2 -0→ q3 -1→ q4 -0→ q6 — ✔
3. `20201010`: q0 -2→ q0 -0→ q1 -2→ q0 -0→ q1 -1→ q2 -0→ q3 -1→ q4 -0→ q6 — ✔
4. `112120201010`: q0 -1→ q0 -1→ q0 -2→ q0 -1→ q0 -2→ q0 -0→ q1 -2→ q0 -0→ q1 -1→ q2 -0→ q3 -1→ q4 -0→ q6 — ✔
5. `1011110110201010`: q0 -1→ q0 -0→ q1 -1→ q2 -1→ q0 -1→ q0 -1→ q0 -0→ q1 -1→ q2 -1→ q0 -0→ q1 -2→ q0 -0→ q1 -1→ q2 -0→ q3 -1→ q4 -0→ q6 — ✔
6. λ: q0 — ✘
7. `20`: q0 -2→ q0 -0→ q1 — ✘
8. `0002`: q0 -0→ q1 -0→ q1 -0→ q1 -2→ q0 — ✘
9. `1120010`: q0 -1→ q0 -1→ q0 -2→ q0 -0→ q1 -0→ q1 -1→ q2 -0→ q3 — ✘
10. `02211121220`: q0 -0→ q1 -2→ q0 -2→ q0 -1→ q0 -1→ q0 -1→ q0 -2→ q0 -1→ q0 -2→ q0 -2→ q0 -0→ q1 — ✘

</details>

Simulación paso a paso en JFLAP con `01010`: [ver captura](../../evidencias/jflap/pasos/L2-113.png).

<a id="problema-2-114"></a>

## Lista 2, problema 114

**Enunciado.** L = {w ∈ Σ₃* : w = aⁿbᵐ, m, n ∈ ℕ}.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Dos fases consecutivas: primero a, después b.

#### AFD — `L2-114`

Archivos: [`L2-114.jff`](../../automatas/lista2-afd/L2-114.jff) · [`L2-114.json`](../../automatas/lista2-afd/L2-114.json) · [`L2-114.xml`](../../automatas/lista2-afd/L2-114.xml). Tipo según la definición: **AFD**, |Q| = 4, Σ = {a, b}, 8 transiciones.

**Diseño.** q0: inicio; q1: se han leído a; q2: se leyó al menos una b después de las a (acepta). Una a después de una b, o una b al inicio, llevan al rechazo absorbente. Se toma ℕ = {1, 2, …}, la convención de la Tarea 2 y de la Práctica 1 (problema 121); con ℕ = {0, 1, …} bastaría con volver de aceptación los estados de los bloques que pueden ser vacíos.

| Estado | a | b | Significado |
|---|---|---|---|
| →q0 | q1 | q2 | inicio |
| q1 | q1 | q3 | bloque de a |
| q2 | q2 | q2 | rechazo absorbente |
| *q3 | q2 | q3 | bloque de b tras las a |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `ab` | acepta | acepta | acepta |
| 2 | `aab` | acepta | acepta | acepta |
| 3 | `abbb` | acepta | acepta | acepta |
| 4 | `abbbbbb` | acepta | acepta | acepta |
| 5 | `abbbbbbbbbb` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `aa` | rechaza | rechaza | rechaza |
| 8 | `aabba` | rechaza | rechaza | rechaza |
| 9 | `bbaaaba` | rechaza | rechaza | rechaza |
| 10 | `aaaabbabbab` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `ab`: q0 -a→ q1 -b→ q3 — ✔
2. `aab`: q0 -a→ q1 -a→ q1 -b→ q3 — ✔
3. `abbb`: q0 -a→ q1 -b→ q3 -b→ q3 -b→ q3 — ✔
4. `abbbbbb`: q0 -a→ q1 -b→ q3 -b→ q3 -b→ q3 -b→ q3 -b→ q3 -b→ q3 — ✔
5. `abbbbbbbbbb`: q0 -a→ q1 -b→ q3 -b→ q3 -b→ q3 -b→ q3 -b→ q3 -b→ q3 -b→ q3 -b→ q3 -b→ q3 -b→ q3 — ✔
6. λ: q0 — ✘
7. `aa`: q0 -a→ q1 -a→ q1 — ✘
8. `aabba`: q0 -a→ q1 -a→ q1 -b→ q3 -b→ q3 -a→ q2 — ✘
9. `bbaaaba`: q0 -b→ q2 -b→ q2 -a→ q2 -a→ q2 -a→ q2 -b→ q2 -a→ q2 — ✘
10. `aaaabbabbab`: q0 -a→ q1 -a→ q1 -a→ q1 -a→ q1 -b→ q3 -b→ q3 -a→ q2 -b→ q2 -b→ q2 -a→ q2 -b→ q2 — ✘

</details>

Simulación paso a paso en JFLAP con `ab`: [ver captura](../../evidencias/jflap/pasos/L2-114.png).

<a id="problema-2-115"></a>

## Lista 2, problema 115

**Enunciado.** L = {w ∈ Σ₂* : w = (abc)ⁿ, n ∈ ℕ}.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Ciclo de longitud 3 que reconoce abc.

#### AFD — `L2-115`

Archivos: [`L2-115.jff`](../../automatas/lista2-afd/L2-115.jff) · [`L2-115.json`](../../automatas/lista2-afd/L2-115.json) · [`L2-115.xml`](../../automatas/lista2-afd/L2-115.xml). Tipo según la definición: **AFD**, |Q| = 5, Σ = {a, b, c, 0, 1}, 25 transiciones.

**Diseño.** Ciclo q0 -a→ q1 -b→ q2 -c→ q3 -a→ q1: q3 indica que se cerró un bloque abc y es de aceptación. Cualquier otro símbolo lleva al rechazo absorbente. Se toma ℕ = {1, 2, …}, la convención de la Tarea 2 y de la Práctica 1 (problema 121); con ℕ = {0, 1, …} bastaría con volver de aceptación los estados de los bloques que pueden ser vacíos.

| Estado | a | b | c | 0 | 1 | Significado |
|---|---|---|---|---|---|---|
| →q0 | q1 | q2 | q2 | q2 | q2 | inicio |
| q1 | q2 | q3 | q2 | q2 | q2 | se leyó a |
| q2 | q2 | q2 | q2 | q2 | q2 | rechazo absorbente |
| q3 | q2 | q2 | q4 | q2 | q2 | se leyó ab |
| *q4 | q1 | q2 | q2 | q2 | q2 | se cerró un bloque abc |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `abc` | acepta | acepta | acepta |
| 2 | `abcabc` | acepta | acepta | acepta |
| 3 | `abcabcabc` | acepta | acepta | acepta |
| 4 | `abcabcabcabc` | acepta | acepta | acepta |
| 5 | `abcabcabcabcabcabc` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `0a` | rechaza | rechaza | rechaza |
| 8 | `cacc` | rechaza | rechaza | rechaza |
| 9 | `a0bb0ac` | rechaza | rechaza | rechaza |
| 10 | `bb0acb10abc` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `abc`: q0 -a→ q1 -b→ q3 -c→ q4 — ✔
2. `abcabc`: q0 -a→ q1 -b→ q3 -c→ q4 -a→ q1 -b→ q3 -c→ q4 — ✔
3. `abcabcabc`: q0 -a→ q1 -b→ q3 -c→ q4 -a→ q1 -b→ q3 -c→ q4 -a→ q1 -b→ q3 -c→ q4 — ✔
4. `abcabcabcabc`: q0 -a→ q1 -b→ q3 -c→ q4 -a→ q1 -b→ q3 -c→ q4 -a→ q1 -b→ q3 -c→ q4 -a→ q1 -b→ q3 -c→ q4 — ✔
5. `abcabcabcabcabcabc`: q0 -a→ q1 -b→ q3 -c→ q4 -a→ q1 -b→ q3 -c→ q4 -a→ q1 -b→ q3 -c→ q4 -a→ q1 -b→ q3 -c→ q4 -a→ q1 -b→ q3 -c→ q4 -a→ q1 -b→ q3 -c→ q4 — ✔
6. λ: q0 — ✘
7. `0a`: q0 -0→ q2 -a→ q2 — ✘
8. `cacc`: q0 -c→ q2 -a→ q2 -c→ q2 -c→ q2 — ✘
9. `a0bb0ac`: q0 -a→ q1 -0→ q2 -b→ q2 -b→ q2 -0→ q2 -a→ q2 -c→ q2 — ✘
10. `bb0acb10abc`: q0 -b→ q2 -b→ q2 -0→ q2 -a→ q2 -c→ q2 -b→ q2 -1→ q2 -0→ q2 -a→ q2 -b→ q2 -c→ q2 — ✘

</details>

Simulación paso a paso en JFLAP con `abc`: [ver captura](../../evidencias/jflap/pasos/L2-115.png).

<a id="problema-2-116"></a>

## Lista 2, problema 116

**Enunciado.** L = {w ∈ Σ₂* : w = aⁿbᵐcⁿ⁺¹, m, n ∈ ℕ}.

**Clasificación: Ninguna.** Ningún autómata finito lo reconoce: L no es regular (lema de bombeo), así que no cabe en ninguna de las tres secciones.

**L no es regular.** Supóngase que lo es y sea p la constante del lema de bombeo. La palabra
z = aᵖ b cᵖ⁺¹ pertenece a L y |z| ≥ p. Toda descomposición z = uvw con |uv| ≤ p y |v| ≥ 1 tiene
v = aᵏ con k ≥ 1, porque los primeros p símbolos son a. Entonces uv⁰w = aᵖ⁻ᵏ b cᵖ⁺¹ tiene p − k a
y p + 1 c, y p + 1 ≠ (p − k) + 1; luego uv⁰w ∉ L, lo que contradice el lema. Por lo tanto ningún
AFD, AFND ni AFND-λ reconoce L (los tres reconocen exactamente los lenguajes regulares).

La misma conclusión sale del teorema de Myhill-Nerode: las palabras a, a², a³, … son distinguibles
dos a dos (aⁱ b cⁱ⁺¹ ∈ L pero aʲ b cⁱ⁺¹ ∉ L si i ≠ j), así que la relación tiene índice infinito.
Reconocer L exige contar las a sin cota, lo que hace un autómata de pila (Unidad II): apila una
marca por cada a, ignora las b y desapila una por cada c, aceptando cuando sobra exactamente una c.

<a id="problema-2-117"></a>

## Lista 2, problema 117

**Enunciado.** L = {w ∈ Σ₃* : w = aⁿbᵐaᵖbᵠ, m, n, p, q ∈ ℕ}.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Cuatro fases consecutivas a, b, a, b.

#### AFD — `L2-117`

Archivos: [`L2-117.jff`](../../automatas/lista2-afd/L2-117.jff) · [`L2-117.json`](../../automatas/lista2-afd/L2-117.json) · [`L2-117.xml`](../../automatas/lista2-afd/L2-117.xml). Tipo según la definición: **AFD**, |Q| = 6, Σ = {a, b}, 12 transiciones.

**Diseño.** Una fase por bloque: q1 (a⁺), q2 (a⁺b⁺), q3 (a⁺b⁺a⁺), q4 (a⁺b⁺a⁺b⁺, acepta). Cada estado tiene un lazo con el símbolo de su bloque y pasa al siguiente con el otro símbolo; una quinta alternancia lleva al rechazo absorbente. Se toma ℕ = {1, 2, …}, la convención de la Tarea 2 y de la Práctica 1 (problema 121); con ℕ = {0, 1, …} bastaría con volver de aceptación los estados de los bloques que pueden ser vacíos.

| Estado | a | b | Significado |
|---|---|---|---|
| →q0 | q1 | q2 | inicio |
| q1 | q1 | q3 | bloque a⁺ |
| q2 | q2 | q2 | rechazo absorbente |
| q3 | q4 | q3 | a⁺b⁺ |
| q4 | q4 | q5 | a⁺b⁺a⁺ |
| *q5 | q2 | q5 | a⁺b⁺a⁺b⁺ |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `abab` | acepta | acepta | acepta |
| 2 | `aabab` | acepta | acepta | acepta |
| 3 | `abaab` | acepta | acepta | acepta |
| 4 | `aaababb` | acepta | acepta | acepta |
| 5 | `aaabbbaaaab` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `bb` | rechaza | rechaza | rechaza |
| 8 | `abba` | rechaza | rechaza | rechaza |
| 9 | `bbababa` | rechaza | rechaza | rechaza |
| 10 | `bbbbbabbbab` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `abab`: q0 -a→ q1 -b→ q3 -a→ q4 -b→ q5 — ✔
2. `aabab`: q0 -a→ q1 -a→ q1 -b→ q3 -a→ q4 -b→ q5 — ✔
3. `abaab`: q0 -a→ q1 -b→ q3 -a→ q4 -a→ q4 -b→ q5 — ✔
4. `aaababb`: q0 -a→ q1 -a→ q1 -a→ q1 -b→ q3 -a→ q4 -b→ q5 -b→ q5 — ✔
5. `aaabbbaaaab`: q0 -a→ q1 -a→ q1 -a→ q1 -b→ q3 -b→ q3 -b→ q3 -a→ q4 -a→ q4 -a→ q4 -a→ q4 -b→ q5 — ✔
6. λ: q0 — ✘
7. `bb`: q0 -b→ q2 -b→ q2 — ✘
8. `abba`: q0 -a→ q1 -b→ q3 -b→ q3 -a→ q4 — ✘
9. `bbababa`: q0 -b→ q2 -b→ q2 -a→ q2 -b→ q2 -a→ q2 -b→ q2 -a→ q2 — ✘
10. `bbbbbabbbab`: q0 -b→ q2 -b→ q2 -b→ q2 -b→ q2 -b→ q2 -a→ q2 -b→ q2 -b→ q2 -b→ q2 -a→ q2 -b→ q2 — ✘

</details>

Simulación paso a paso en JFLAP con `abab`: [ver captura](../../evidencias/jflap/pasos/L2-117.png).

<a id="problema-2-118"></a>

## Lista 2, problema 118

**Enunciado.** L = {w ∈ Σ₃ : w = a x ab y a}.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### L = {w ∈ Σ₃* : w = a x ab y a, con x, y ∈ Σ₃*}. — `L2-118`

Archivos: [`L2-118.jff`](../../automatas/lista2-afd/L2-118.jff) · [`L2-118.json`](../../automatas/lista2-afd/L2-118.json) · [`L2-118.xml`](../../automatas/lista2-afd/L2-118.xml). Tipo según la definición: **AFD**, |Q| = 6, Σ = {a, b}, 12 transiciones.

**Diseño.** Los estados recuerdan: si el primer símbolo fue a; si ya apareció ab después de esa a; y, una vez visto, si el último símbolo fue a. La palabra más corta es aaba.

| Estado | a | b |
|---|---|---|
| q1 | q3 | q1 |
| q3 | q3 | q4 |
| *q5 | q5 | q4 |
| q4 | q5 | q4 |
| q2 | q2 | q2 |
| →q0 | q1 | q2 |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `aaba` | acepta | acepta | acepta |
| 2 | `ababa` | acepta | acepta | acepta |
| 3 | `abbaba` | acepta | acepta | acepta |
| 4 | `abbaaba` | acepta | acepta | acepta |
| 5 | `aabbabbaaaba` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `aa` | rechaza | rechaza | rechaza |
| 8 | `bbbb` | rechaza | rechaza | rechaza |
| 9 | `ababbaab` | rechaza | rechaza | rechaza |
| 10 | `abaaaababbb` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `aaba`: q0 -a→ q1 -a→ q3 -b→ q4 -a→ q5 — ✔
2. `ababa`: q0 -a→ q1 -b→ q1 -a→ q3 -b→ q4 -a→ q5 — ✔
3. `abbaba`: q0 -a→ q1 -b→ q1 -b→ q1 -a→ q3 -b→ q4 -a→ q5 — ✔
4. `abbaaba`: q0 -a→ q1 -b→ q1 -b→ q1 -a→ q3 -a→ q3 -b→ q4 -a→ q5 — ✔
5. `aabbabbaaaba`: q0 -a→ q1 -a→ q3 -b→ q4 -b→ q4 -a→ q5 -b→ q4 -b→ q4 -a→ q5 -a→ q5 -a→ q5 -b→ q4 -a→ q5 — ✔
6. λ: q0 — ✘
7. `aa`: q0 -a→ q1 -a→ q3 — ✘
8. `bbbb`: q0 -b→ q2 -b→ q2 -b→ q2 -b→ q2 — ✘
9. `ababbaab`: q0 -a→ q1 -b→ q1 -a→ q3 -b→ q4 -b→ q4 -a→ q5 -a→ q5 -b→ q4 — ✘
10. `abaaaababbb`: q0 -a→ q1 -b→ q1 -a→ q3 -a→ q3 -a→ q3 -a→ q3 -b→ q4 -a→ q5 -b→ q4 -b→ q4 -b→ q4 — ✘

</details>

Simulación paso a paso en JFLAP con `aaba`: [ver captura](../../evidencias/jflap/pasos/L2-118.png).

<a id="problema-2-119"></a>

## Lista 2, problema 119

**Enunciado.** Las palabras de Σ₃ tales que después de cada subcadena aa aparece una b.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Se recuerda la racha final de a (0, 1 o 2).

#### AFD — `L2-119`

Archivos: [`L2-119.jff`](../../automatas/lista2-afd/L2-119.jff) · [`L2-119.json`](../../automatas/lista2-afd/L2-119.json) · [`L2-119.xml`](../../automatas/lista2-afd/L2-119.xml). Tipo según la definición: **AFD**, |Q| = 4, Σ = {a, b}, 8 transiciones.

**Diseño.** Se interpreta que el símbolo inmediato a cada aa debe ser b; así, aaa no pertenece (su primer aa va seguido de a) y una palabra no puede terminar en aa. q0: el último símbolo no es a; q1: una a suelta; q2: aa pendiente, que exige b. Leer a en q2 lleva al rechazo absorbente.

| Estado | a | b | Significado |
|---|---|---|---|
| →*q0 | q1 | q0 | sin a pendientes |
| *q1 | q2 | q0 | una a al final |
| q2 | q3 | q0 | aa al final: falta la b |
| q3 | q3 | q3 | rechazo absorbente |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | acepta | acepta | acepta |
| 2 | `ba` | acepta | acepta | acepta |
| 3 | `aaba` | acepta | acepta | acepta |
| 4 | `aababba` | acepta | acepta | acepta |
| 5 | `aabbbbababb` | acepta | acepta | acepta |
| 6 | `aa` | rechaza | rechaza | rechaza |
| 7 | `abaa` | rechaza | rechaza | rechaza |
| 8 | `aabbaa` | rechaza | rechaza | rechaza |
| 9 | `abaaabb` | rechaza | rechaza | rechaza |
| 10 | `bbaabaabbaa` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: q0 — ✔
2. `ba`: q0 -b→ q0 -a→ q1 — ✔
3. `aaba`: q0 -a→ q1 -a→ q2 -b→ q0 -a→ q1 — ✔
4. `aababba`: q0 -a→ q1 -a→ q2 -b→ q0 -a→ q1 -b→ q0 -b→ q0 -a→ q1 — ✔
5. `aabbbbababb`: q0 -a→ q1 -a→ q2 -b→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q1 -b→ q0 -a→ q1 -b→ q0 -b→ q0 — ✔
6. `aa`: q0 -a→ q1 -a→ q2 — ✘
7. `abaa`: q0 -a→ q1 -b→ q0 -a→ q1 -a→ q2 — ✘
8. `aabbaa`: q0 -a→ q1 -a→ q2 -b→ q0 -b→ q0 -a→ q1 -a→ q2 — ✘
9. `abaaabb`: q0 -a→ q1 -b→ q0 -a→ q1 -a→ q2 -a→ q3 -b→ q3 -b→ q3 — ✘
10. `bbaabaabbaa`: q0 -b→ q0 -b→ q0 -a→ q1 -a→ q2 -b→ q0 -a→ q1 -a→ q2 -b→ q0 -b→ q0 -a→ q1 -a→ q2 — ✘

</details>

Simulación paso a paso en JFLAP con `ba`: [ver captura](../../evidencias/jflap/pasos/L2-119.png).

<a id="problema-2-120"></a>

## Lista 2, problema 120

**Enunciado.** Palabras de Σ₁ cuyo primer y último carácter son distintos.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### Palabras de Σ₁ cuyo primer y último carácter son distintos. — `L2-120`

Archivos: [`L2-120.jff`](../../automatas/lista2-afd/L2-120.jff) · [`L2-120.json`](../../automatas/lista2-afd/L2-120.json) · [`L2-120.xml`](../../automatas/lista2-afd/L2-120.xml). Tipo según la definición: **AFD**, |Q| = 7, Σ = {0, 1, 2}, 21 transiciones.

**Diseño.** El estado es (primer símbolo, último símbolo). El primero queda fijo y el segundo se actualiza. λ se rechaza porque no tiene esos caracteres. Tras minimizar quedan 7 estados.

| Estado | 0 | 1 | 2 |
|---|---|---|---|
| q1 | q1 | q4 | q4 |
| q3 | q6 | q6 | q3 |
| *q5 | q5 | q2 | q5 |
| *q4 | q1 | q4 | q4 |
| *q6 | q6 | q6 | q3 |
| q2 | q5 | q2 | q5 |
| →q0 | q1 | q2 | q3 |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `01` | acepta | acepta | acepta |
| 2 | `10` | acepta | acepta | acepta |
| 3 | `2101` | acepta | acepta | — |
| 4 | `01210201` | acepta | acepta | — |
| 5 | `222022102120` | acepta | acepta | — |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `121` | rechaza | rechaza | rechaza |
| 8 | `0220` | rechaza | rechaza | — |
| 9 | `2211102` | rechaza | rechaza | — |
| 10 | `02100120220` | rechaza | rechaza | — |

<details><summary>Recorrido completo de cada cadena</summary>

1. `01`: q0 -0→ q1 -1→ q4 — ✔
2. `10`: q0 -1→ q2 -0→ q5 — ✔
3. `2101`: q0 -2→ q3 -1→ q6 -0→ q6 -1→ q6 — ✔
4. `01210201`: q0 -0→ q1 -1→ q4 -2→ q4 -1→ q4 -0→ q1 -2→ q4 -0→ q1 -1→ q4 — ✔
5. `222022102120`: q0 -2→ q3 -2→ q3 -2→ q3 -0→ q6 -2→ q3 -2→ q3 -1→ q6 -0→ q6 -2→ q3 -1→ q6 -2→ q3 -0→ q6 — ✔
6. λ: q0 — ✘
7. `121`: q0 -1→ q2 -2→ q5 -1→ q2 — ✘
8. `0220`: q0 -0→ q1 -2→ q4 -2→ q4 -0→ q1 — ✘
9. `2211102`: q0 -2→ q3 -2→ q3 -1→ q6 -1→ q6 -1→ q6 -0→ q6 -2→ q3 — ✘
10. `02100120220`: q0 -0→ q1 -2→ q4 -1→ q4 -0→ q1 -0→ q1 -1→ q4 -2→ q4 -0→ q1 -2→ q4 -2→ q4 -0→ q1 — ✘

</details>

Simulación paso a paso en JFLAP con `01`: [ver captura](../../evidencias/jflap/pasos/L2-120.png).

<a id="problema-2-121"></a>

## Lista 2, problema 121

**Enunciado.** Palabras de Σ₁ de longitud 3n, tales que cada bloque de 3 tiene al menos un 0 (se toma n ≥ 1).

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### Palabras de Σ₁ de longitud 3n, tales que cada bloque de 3 tiene al menos un 0 (se toma n ≥ 1). — `L2-121`

Archivos: [`L2-121.jff`](../../automatas/lista2-afd/L2-121.jff) · [`L2-121.json`](../../automatas/lista2-afd/L2-121.json) · [`L2-121.xml`](../../automatas/lista2-afd/L2-121.xml). Tipo según la definición: **AFD**, |Q| = 7, Σ = {0, 1, 2}, 21 transiciones.

**Diseño.** El estado guarda la posición dentro del bloque y si el bloque ya tiene 0; un bloque sin 0 lleva a un estado de rechazo absorbente. Se toma ℕ = {1, 2, …}, como en la Tarea 2, por lo que λ se rechaza.

| Estado | 0 | 1 | 2 |
|---|---|---|---|
| q1 | q3 | q3 | q3 |
| q4 | q5 | q6 | q6 |
| q3 | q5 | q5 | q5 |
| q6 | q6 | q6 | q6 |
| *q5 | q1 | q2 | q2 |
| q2 | q3 | q4 | q4 |
| →q0 | q1 | q2 | q2 |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `000` | acepta | acepta | acepta |
| 2 | `200` | acepta | acepta | acepta |
| 3 | `201200` | acepta | acepta | acepta |
| 4 | `200102200` | acepta | acepta | acepta |
| 5 | `220210210200` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `20` | rechaza | rechaza | rechaza |
| 8 | `0002` | rechaza | rechaza | rechaza |
| 9 | `1110200` | rechaza | rechaza | rechaza |
| 10 | `21220202012` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `000`: q0 -0→ q1 -0→ q3 -0→ q5 — ✔
2. `200`: q0 -2→ q2 -0→ q3 -0→ q5 — ✔
3. `201200`: q0 -2→ q2 -0→ q3 -1→ q5 -2→ q2 -0→ q3 -0→ q5 — ✔
4. `200102200`: q0 -2→ q2 -0→ q3 -0→ q5 -1→ q2 -0→ q3 -2→ q5 -2→ q2 -0→ q3 -0→ q5 — ✔
5. `220210210200`: q0 -2→ q2 -2→ q4 -0→ q5 -2→ q2 -1→ q4 -0→ q5 -2→ q2 -1→ q4 -0→ q5 -2→ q2 -0→ q3 -0→ q5 — ✔
6. λ: q0 — ✘
7. `20`: q0 -2→ q2 -0→ q3 — ✘
8. `0002`: q0 -0→ q1 -0→ q3 -0→ q5 -2→ q2 — ✘
9. `1110200`: q0 -1→ q2 -1→ q4 -1→ q6 -0→ q6 -2→ q6 -0→ q6 -0→ q6 — ✘
10. `21220202012`: q0 -2→ q2 -1→ q4 -2→ q6 -2→ q6 -0→ q6 -2→ q6 -0→ q6 -2→ q6 -0→ q6 -1→ q6 -2→ q6 — ✘

</details>

Simulación paso a paso en JFLAP con `000`: [ver captura](../../evidencias/jflap/pasos/L2-121.png).

<a id="problema-2-122"></a>

## Lista 2, problema 122

**Enunciado.** Palabras de Σ₁ en las que toda terna de símbolos consecutivos tiene un 0.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### Palabras de Σ₁ en las que toda terna de símbolos consecutivos tiene un 0. — `L2-122`

Archivos: [`L2-122.jff`](../../automatas/lista2-afd/L2-122.jff) · [`L2-122.json`](../../automatas/lista2-afd/L2-122.json) · [`L2-122.xml`](../../automatas/lista2-afd/L2-122.xml). Tipo según la definición: **AFD**, |Q| = 4, Σ = {0, 1, 2}, 12 transiciones.

**Diseño.** El estado es el tamaño de la racha actual sin ceros (0, 1 o 2). Con racha 3 se pasa al rechazo absorbente.

| Estado | 0 | 1 | 2 |
|---|---|---|---|
| *q1 | q0 | q2 | q2 |
| *q2 | q0 | q3 | q3 |
| q3 | q3 | q3 | q3 |
| →*q0 | q0 | q1 | q1 |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | acepta | acepta | acepta |
| 2 | `21` | acepta | acepta | acepta |
| 3 | `2100` | acepta | acepta | acepta |
| 4 | `0012011` | acepta | acepta | acepta |
| 5 | `10001022021` | acepta | acepta | acepta |
| 6 | `111` | rechaza | rechaza | rechaza |
| 7 | `121` | rechaza | rechaza | rechaza |
| 8 | `0211` | rechaza | rechaza | rechaza |
| 9 | `0211021` | rechaza | rechaza | rechaza |
| 10 | `22022001120` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: q0 — ✔
2. `21`: q0 -2→ q1 -1→ q2 — ✔
3. `2100`: q0 -2→ q1 -1→ q2 -0→ q0 -0→ q0 — ✔
4. `0012011`: q0 -0→ q0 -0→ q0 -1→ q1 -2→ q2 -0→ q0 -1→ q1 -1→ q2 — ✔
5. `10001022021`: q0 -1→ q1 -0→ q0 -0→ q0 -0→ q0 -1→ q1 -0→ q0 -2→ q1 -2→ q2 -0→ q0 -2→ q1 -1→ q2 — ✔
6. `111`: q0 -1→ q1 -1→ q2 -1→ q3 — ✘
7. `121`: q0 -1→ q1 -2→ q2 -1→ q3 — ✘
8. `0211`: q0 -0→ q0 -2→ q1 -1→ q2 -1→ q3 — ✘
9. `0211021`: q0 -0→ q0 -2→ q1 -1→ q2 -1→ q3 -0→ q3 -2→ q3 -1→ q3 — ✘
10. `22022001120`: q0 -2→ q1 -2→ q2 -0→ q0 -2→ q1 -2→ q2 -0→ q0 -0→ q0 -1→ q1 -1→ q2 -2→ q3 -0→ q3 — ✘

</details>

Simulación paso a paso en JFLAP con `21`: [ver captura](../../evidencias/jflap/pasos/L2-122.png).

<a id="problema-2-123"></a>

## Lista 2, problema 123

**Enunciado.** Palabras de Σ₃ de la forma w x w, con w ∈ Σ₃² y x ∈ Σ₃*.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### Palabras de Σ₃ de la forma w x w, con w ∈ Σ₃² y x ∈ Σ₃*. — `L2-123`

Archivos: [`L2-123.jff`](../../automatas/lista2-afd/L2-123.jff) · [`L2-123.json`](../../automatas/lista2-afd/L2-123.json) · [`L2-123.xml`](../../automatas/lista2-afd/L2-123.xml). Tipo según la definición: **AFD**, |Q| = 15, Σ = {a, b}, 30 transiciones.

**Diseño.** El estado memoriza los dos primeros símbolos, los dos últimos y si ya se leyeron al menos 4. Acepta si coinciden y |w x w| ≥ 4.

<details><summary>Tabla de transiciones (15 estados)</summary>

| Estado | a | b |
|---|---|---|
| *q12 | q8 | q4 |
| *q13 | q5 | q9 |
| q1 | q3 | q4 |
| q4 | q8 | q4 |
| q6 | q6 | q10 |
| q8 | q8 | q12 |
| q5 | q5 | q9 |
| q9 | q13 | q9 |
| q7 | q11 | q3 |
| *q14 | q6 | q14 |
| →q0 | q1 | q2 |
| q10 | q6 | q14 |
| q2 | q5 | q6 |
| q3 | q7 | q3 |
| *q11 | q11 | q3 |

</details>

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `aaaa` | acepta | acepta | acepta |
| 2 | `baba` | acepta | acepta | — |
| 3 | `aaabaa` | acepta | acepta | acepta |
| 4 | `baaabaaba` | acepta | acepta | acepta |
| 5 | `aaabaaabbaa` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `ba` | rechaza | rechaza | rechaza |
| 8 | `baaa` | rechaza | rechaza | rechaza |
| 9 | `bbababa` | rechaza | rechaza | rechaza |
| 10 | `abaabbbabbb` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `aaaa`: q0 -a→ q1 -a→ q3 -a→ q7 -a→ q11 — ✔
2. `baba`: q0 -b→ q2 -a→ q5 -b→ q9 -a→ q13 — ✔
3. `aaabaa`: q0 -a→ q1 -a→ q3 -a→ q7 -b→ q3 -a→ q7 -a→ q11 — ✔
4. `baaabaaba`: q0 -b→ q2 -a→ q5 -a→ q5 -a→ q5 -b→ q9 -a→ q13 -a→ q5 -b→ q9 -a→ q13 — ✔
5. `aaabaaabbaa`: q0 -a→ q1 -a→ q3 -a→ q7 -b→ q3 -a→ q7 -a→ q11 -a→ q11 -b→ q3 -b→ q3 -a→ q7 -a→ q11 — ✔
6. λ: q0 — ✘
7. `ba`: q0 -b→ q2 -a→ q5 — ✘
8. `baaa`: q0 -b→ q2 -a→ q5 -a→ q5 -a→ q5 — ✘
9. `bbababa`: q0 -b→ q2 -b→ q6 -a→ q6 -b→ q10 -a→ q6 -b→ q10 -a→ q6 — ✘
10. `abaabbbabbb`: q0 -a→ q1 -b→ q4 -a→ q8 -a→ q8 -b→ q12 -b→ q4 -b→ q4 -a→ q8 -b→ q12 -b→ q4 -b→ q4 — ✘

</details>

Simulación paso a paso en JFLAP con `aaaa`: [ver captura](../../evidencias/jflap/pasos/L2-123.png).

<a id="problema-2-124"></a>

## Lista 2, problema 124

**Enunciado.** Mecanismo de tres palancas: se acepta si la última canica sale por A.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### Mecanismo de tres palancas: se acepta si la última canica sale por A. — `L2-124`

Archivos: [`L2-124.jff`](../../automatas/lista2-afd/L2-124.jff) · [`L2-124.json`](../../automatas/lista2-afd/L2-124.json) · [`L2-124.xml`](../../automatas/lista2-afd/L2-124.xml). Tipo según la definición: **AFD**, |Q| = 13, Σ = {0, 1}, 26 transiciones.

**Diseño.** Las palancas tienen 2³ = 8 configuraciones. El AFD amplía el estado a (configuración, última salida), con 13 estados alcanzables; acepta los de salida A. Se toma la posición inicial con las tres palancas a la izquierda.

<details><summary>Tabla de transiciones (13 estados)</summary>

| Estado | 0 | 1 |
|---|---|---|
| →q0 | q1 | q2 |
| *q1 | q3 | q4 |
| *q2 | q4 | q5 |
| *q3 | q6 | q7 |
| *q4 | q7 | q8 |
| q5 | q6 | q7 |
| *q6 | q9 | q10 |
| q7 | q11 | q9 |
| q8 | q9 | q10 |
| q9 | q1 | q2 |
| q10 | q2 | q12 |
| *q11 | q2 | q12 |
| q12 | q3 | q4 |

</details>

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `0` | acepta | acepta | acepta |
| 2 | `01` | acepta | acepta | acepta |
| 3 | `10110` | acepta | acepta | acepta |
| 4 | `10001010` | acepta | acepta | acepta |
| 5 | `01110100110` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `11` | rechaza | rechaza | rechaza |
| 8 | `1011` | rechaza | rechaza | rechaza |
| 9 | `0111101` | rechaza | rechaza | rechaza |
| 10 | `01010101111` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `0`: q0 -0→ q1 — ✔
2. `01`: q0 -0→ q1 -1→ q4 — ✔
3. `10110`: q0 -1→ q2 -0→ q4 -1→ q8 -1→ q10 -0→ q2 — ✔
4. `10001010`: q0 -1→ q2 -0→ q4 -0→ q7 -0→ q11 -1→ q12 -0→ q3 -1→ q7 -0→ q11 — ✔
5. `01110100110`: q0 -0→ q1 -1→ q4 -1→ q8 -1→ q10 -0→ q2 -1→ q5 -0→ q6 -0→ q9 -1→ q2 -1→ q5 -0→ q6 — ✔
6. λ: q0 — ✘
7. `11`: q0 -1→ q2 -1→ q5 — ✘
8. `1011`: q0 -1→ q2 -0→ q4 -1→ q8 -1→ q10 — ✘
9. `0111101`: q0 -0→ q1 -1→ q4 -1→ q8 -1→ q10 -1→ q12 -0→ q3 -1→ q7 — ✘
10. `01010101111`: q0 -0→ q1 -1→ q4 -0→ q7 -1→ q9 -0→ q1 -1→ q4 -0→ q7 -1→ q9 -1→ q2 -1→ q5 -1→ q7 — ✘

</details>

Simulación paso a paso en JFLAP con `01`: [ver captura](../../evidencias/jflap/pasos/L2-124.png).

<a id="problema-2-125"></a>

## Lista 2, problema 125

**Enunciado.** Sea A = (Q, Σ, δ, A₀, F) un AFD. ¿Cuál es el lenguaje de A' = (Q, Σ, δ, A₀, Q \ F)?

**Clasificación: AFD.** Pregunta sobre un AFD (δ total); se ilustra con el AFD del 139 y su complemento.

**Respuesta.** L(A') = Σ* \ L(A), el complemento de L(A). Como δ es total, para cada w existe
exactamente un estado δ̂(A₀, w); w ∈ L(A') ⇔ δ̂(A₀, w) ∈ Q \ F ⇔ δ̂(A₀, w) ∉ F ⇔ w ∉ L(A).
La hipótesis de que δ sea total es indispensable: en un AFND (o en un autómata con δ parcial)
intercambiar F y Q \ F no da el complemento, porque una palabra puede tener caminos que terminan
dentro y fuera de F, o no tener ninguno. Por eso el ejemplo usa el AFD completo del problema 139:
el complemento de «número par de ceros» es «número impar de ceros».

#### AFD A del ejemplo (problema 139: par de ceros) — `L2-125-A`

Archivos: [`L2-125-A.jff`](../../automatas/lista2-afd/L2-125-A.jff) · [`L2-125-A.json`](../../automatas/lista2-afd/L2-125-A.json) · [`L2-125-A.xml`](../../automatas/lista2-afd/L2-125-A.xml). Tipo según la definición: **AFD**, |Q| = 2, Σ = {0, 1}, 4 transiciones.

**Diseño.** Ejemplo: el AFD del problema 139.

| Estado | 0 | 1 | Significado |
|---|---|---|---|
| →*q0 | q1 | q0 | número par de ceros |
| q1 | q0 | q1 | número impar de ceros |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | acepta | acepta | acepta |
| 2 | `100` | acepta | acepta | acepta |
| 3 | `0101` | acepta | acepta | acepta |
| 4 | `10010000` | acepta | acepta | acepta |
| 5 | `00110100110` | acepta | acepta | acepta |
| 6 | `0` | rechaza | rechaza | rechaza |
| 7 | `10` | rechaza | rechaza | rechaza |
| 8 | `1101` | rechaza | rechaza | rechaza |
| 9 | `11000100` | rechaza | rechaza | rechaza |
| 10 | `011001111100` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: q0 — ✔
2. `100`: q0 -1→ q0 -0→ q1 -0→ q0 — ✔
3. `0101`: q0 -0→ q1 -1→ q1 -0→ q0 -1→ q0 — ✔
4. `10010000`: q0 -1→ q0 -0→ q1 -0→ q0 -1→ q0 -0→ q1 -0→ q0 -0→ q1 -0→ q0 — ✔
5. `00110100110`: q0 -0→ q1 -0→ q0 -1→ q0 -1→ q0 -0→ q1 -1→ q1 -0→ q0 -0→ q1 -1→ q1 -1→ q1 -0→ q0 — ✔
6. `0`: q0 -0→ q1 — ✘
7. `10`: q0 -1→ q0 -0→ q1 — ✘
8. `1101`: q0 -1→ q0 -1→ q0 -0→ q1 -1→ q1 — ✘
9. `11000100`: q0 -1→ q0 -1→ q0 -0→ q1 -0→ q0 -0→ q1 -1→ q1 -0→ q0 -0→ q1 — ✘
10. `011001111100`: q0 -0→ q1 -1→ q1 -1→ q1 -0→ q0 -0→ q1 -1→ q1 -1→ q1 -1→ q1 -1→ q1 -1→ q1 -0→ q0 -0→ q1 — ✘

</details>

Simulación paso a paso en JFLAP con `100`: [ver captura](../../evidencias/jflap/pasos/L2-125-A.png).

#### A' = (Q, Σ, δ, A₀, Q \ F) — `L2-125-complemento`

Archivos: [`L2-125-complemento.jff`](../../automatas/lista2-afd/L2-125-complemento.jff) · [`L2-125-complemento.json`](../../automatas/lista2-afd/L2-125-complemento.json) · [`L2-125-complemento.xml`](../../automatas/lista2-afd/L2-125-complemento.xml). Tipo según la definición: **AFD**, |Q| = 2, Σ = {0, 1}, 4 transiciones.

**Diseño.** Mismos estados y transiciones; se intercambian los estados de aceptación y de no aceptación.

| Estado | 0 | 1 | Significado |
|---|---|---|---|
| →q0 | q1 | q0 | número par de ceros |
| *q1 | q0 | q1 | número impar de ceros |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `0` | acepta | acepta | acepta |
| 2 | `01` | acepta | acepta | acepta |
| 3 | `0100` | acepta | acepta | acepta |
| 4 | `0000000` | acepta | acepta | acepta |
| 5 | `00110000110` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `010` | rechaza | rechaza | rechaza |
| 8 | `1100` | rechaza | rechaza | rechaza |
| 9 | `01000100` | rechaza | rechaza | rechaza |
| 10 | `001001001100` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `0`: q0 -0→ q1 — ✔
2. `01`: q0 -0→ q1 -1→ q1 — ✔
3. `0100`: q0 -0→ q1 -1→ q1 -0→ q0 -0→ q1 — ✔
4. `0000000`: q0 -0→ q1 -0→ q0 -0→ q1 -0→ q0 -0→ q1 -0→ q0 -0→ q1 — ✔
5. `00110000110`: q0 -0→ q1 -0→ q0 -1→ q0 -1→ q0 -0→ q1 -0→ q0 -0→ q1 -0→ q0 -1→ q0 -1→ q0 -0→ q1 — ✔
6. λ: q0 — ✘
7. `010`: q0 -0→ q1 -1→ q1 -0→ q0 — ✘
8. `1100`: q0 -1→ q0 -1→ q0 -0→ q1 -0→ q0 — ✘
9. `01000100`: q0 -0→ q1 -1→ q1 -0→ q0 -0→ q1 -0→ q0 -1→ q0 -0→ q1 -0→ q0 — ✘
10. `001001001100`: q0 -0→ q1 -0→ q0 -1→ q0 -0→ q1 -0→ q0 -1→ q0 -0→ q1 -0→ q0 -1→ q0 -1→ q0 -0→ q1 -0→ q0 — ✘

</details>

Simulación paso a paso en JFLAP con `01`: [ver captura](../../evidencias/jflap/pasos/L2-125-complemento.png).

<a id="problema-2-126"></a>

## Lista 2, problema 126

**Enunciado.** Sea A = (Q, Σ, δ, A₀, F) un AFD. ¿Cuál es el lenguaje del autómata si F = ∅?

**Clasificación: AFD.** Pregunta sobre un AFD; con F = ∅ ninguna palabra llega a un estado de aceptación.

**Respuesta.** L(A) = ∅: w ∈ L(A) exige δ̂(A₀, w) ∈ F, y F no tiene elementos. No es lo mismo que {λ}: el lenguaje vacío no contiene ni siquiera la cadena vacía. Por eso este autómata no tiene casos válidos: no existe ninguna cadena que acepte.

#### AFD del 139 con F = ∅ — `L2-126`

Archivos: [`L2-126.jff`](../../automatas/lista2-afd/L2-126.jff) · [`L2-126.json`](../../automatas/lista2-afd/L2-126.json) · [`L2-126.xml`](../../automatas/lista2-afd/L2-126.xml). Tipo según la definición: **AFD**, |Q| = 2, Σ = {0, 1}, 4 transiciones.

**Diseño.** Mismo δ que el 139, sin estados de aceptación.

| Estado | 0 | 1 | Significado |
|---|---|---|---|
| →q0 | q1 | q0 | número par de ceros |
| q1 | q0 | q1 | número impar de ceros |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | rechaza | rechaza | rechaza |
| 2 | `00` | rechaza | rechaza | rechaza |
| 3 | `0101` | rechaza | rechaza | rechaza |
| 4 | `0001101` | rechaza | rechaza | rechaza |
| 5 | `10001010101` | rechaza | rechaza | rechaza |

Nota sobre los casos: el lenguaje solo tiene 0 palabras.

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: q0 — ✘
2. `00`: q0 -0→ q1 -0→ q0 — ✘
3. `0101`: q0 -0→ q1 -1→ q1 -0→ q0 -1→ q0 — ✘
4. `0001101`: q0 -0→ q1 -0→ q0 -0→ q1 -1→ q1 -1→ q1 -0→ q0 -1→ q0 — ✘
5. `10001010101`: q0 -1→ q0 -0→ q1 -0→ q0 -0→ q1 -1→ q1 -0→ q0 -1→ q0 -0→ q1 -1→ q1 -0→ q0 -1→ q0 — ✘

</details>

Simulación paso a paso en JFLAP con `00`: [ver captura](../../evidencias/jflap/pasos/L2-126.png).

<a id="problema-2-127"></a>

## Lista 2, problema 127

**Enunciado.** Sea A = (Q, Σ, δ, q₀, F) un AFD. ¿Cuál es el lenguaje del autómata si F = Q?

**Clasificación: AFD.** Pregunta sobre un AFD; con F = Q y δ total toda palabra termina en un estado de aceptación.

**Respuesta.** L(A) = Σ*: como δ es total, δ̂(q₀, w) existe para toda w ∈ Σ* y pertenece a Q = F. Si δ fuera parcial, L(A) sería el conjunto de palabras que no «se atoran», que puede ser menor que Σ*. Como el lenguaje es Σ*, las únicas cadenas inválidas posibles contienen símbolos fuera de Σ.

#### AFD del 139 con F = Q — `L2-127`

Archivos: [`L2-127.jff`](../../automatas/lista2-afd/L2-127.jff) · [`L2-127.json`](../../automatas/lista2-afd/L2-127.json) · [`L2-127.xml`](../../automatas/lista2-afd/L2-127.xml). Tipo según la definición: **AFD**, |Q| = 2, Σ = {0, 1}, 4 transiciones.

**Diseño.** Mismo δ que el 139; los dos estados son de aceptación.

| Estado | 0 | 1 | Significado |
|---|---|---|---|
| →*q0 | q1 | q0 | número par de ceros |
| *q1 | q0 | q1 | número impar de ceros |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | acepta | acepta | acepta |
| 2 | `00` | acepta | acepta | acepta |
| 3 | `1101` | acepta | acepta | acepta |
| 4 | `1110111` | acepta | acepta | acepta |
| 5 | `10111000110` | acepta | acepta | acepta |
| 6 | `#` (símbolo fuera de Σ) | rechaza | rechaza | rechaza |
| 7 | `0#` (símbolo fuera de Σ) | rechaza | rechaza | rechaza |
| 8 | `#11` (símbolo fuera de Σ) | rechaza | rechaza | rechaza |

Nota sobre los casos: todas las cadenas sobre Σ pertenecen al lenguaje, así que las inválidas usan un símbolo fuera de Σ (#).

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: q0 — ✔
2. `00`: q0 -0→ q1 -0→ q0 — ✔
3. `1101`: q0 -1→ q0 -1→ q0 -0→ q1 -1→ q1 — ✔
4. `1110111`: q0 -1→ q0 -1→ q0 -1→ q0 -0→ q1 -1→ q1 -1→ q1 -1→ q1 — ✔
5. `10111000110`: q0 -1→ q0 -0→ q1 -1→ q1 -1→ q1 -1→ q1 -0→ q0 -0→ q1 -0→ q0 -1→ q0 -1→ q0 -0→ q1 — ✔
6. `#`: q0 -#→ (sin transición) — ✘
7. `0#`: q0 -0→ q1 -#→ (sin transición) — ✘
8. `#11`: q0 -#→ (sin transición) — ✘

</details>

Simulación paso a paso en JFLAP con `00`: [ver captura](../../evidencias/jflap/pasos/L2-127.png).

<a id="problema-2-128"></a>

## Lista 2, problema 128

**Enunciado.** Autómata M del diagrama del ejercicio 128 (lenguaje L). Se pide un AFD para L₂.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Se cambia F de un AFD dado. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### Autómata M del diagrama del ejercicio 128 (lenguaje L). — `L2-128-M`

Archivos: [`L2-128-M.jff`](../../automatas/lista2-afd/L2-128-M.jff) · [`L2-128-M.json`](../../automatas/lista2-afd/L2-128-M.json) · [`L2-128-M.xml`](../../automatas/lista2-afd/L2-128-M.xml). Tipo según la definición: **AFD**, |Q| = 6, Σ = {0, 1}, 12 transiciones.

**Diseño.** Transcripción del diagrama: cada estado es uno de A a F del enunciado (q0 = A, …, q5 = F); F es de aceptación y regresa a D con 0 y con 1.

| Estado | 0 | 1 |
|---|---|---|
| →q0 | q1 | q2 |
| q1 | q2 | q3 |
| q2 | q3 | q4 |
| q3 | q5 | q4 |
| q4 | q4 | q5 |
| *q5 | q3 | q3 |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `010` | acepta | acepta | acepta |
| 2 | `100` | acepta | acepta | acepta |
| 3 | `0011` | acepta | acepta | acepta |
| 4 | `01110000` | acepta | acepta | acepta |
| 5 | `11000011010` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `11` | rechaza | rechaza | rechaza |
| 8 | `1100` | rechaza | rechaza | rechaza |
| 9 | `1001100` | rechaza | rechaza | rechaza |
| 10 | `001110100110` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `010`: q0 -0→ q1 -1→ q3 -0→ q5 — ✔
2. `100`: q0 -1→ q2 -0→ q3 -0→ q5 — ✔
3. `0011`: q0 -0→ q1 -0→ q2 -1→ q4 -1→ q5 — ✔
4. `01110000`: q0 -0→ q1 -1→ q3 -1→ q4 -1→ q5 -0→ q3 -0→ q5 -0→ q3 -0→ q5 — ✔
5. `11000011010`: q0 -1→ q2 -1→ q4 -0→ q4 -0→ q4 -0→ q4 -0→ q4 -1→ q5 -1→ q3 -0→ q5 -1→ q3 -0→ q5 — ✔
6. λ: q0 — ✘
7. `11`: q0 -1→ q2 -1→ q4 — ✘
8. `1100`: q0 -1→ q2 -1→ q4 -0→ q4 -0→ q4 — ✘
9. `1001100`: q0 -1→ q2 -0→ q3 -0→ q5 -1→ q3 -1→ q4 -0→ q4 -0→ q4 — ✘
10. `001110100110`: q0 -0→ q1 -0→ q2 -1→ q4 -1→ q5 -1→ q3 -0→ q5 -1→ q3 -0→ q5 -0→ q3 -1→ q4 -1→ q5 -0→ q3 — ✘

</details>

Simulación paso a paso en JFLAP con `010`: [ver captura](../../evidencias/jflap/pasos/L2-128-M.png).

#### L₂: palabras de L a las que se les quita el último símbolo. — `L2-128-L2`

Archivos: [`L2-128-L2.jff`](../../automatas/lista2-afd/L2-128-L2.jff) · [`L2-128-L2.json`](../../automatas/lista2-afd/L2-128-L2.json) · [`L2-128-L2.xml`](../../automatas/lista2-afd/L2-128-L2.xml). Tipo según la definición: **AFD**, |Q| = 6, Σ = {0, 1}, 12 transiciones.

**Diseño.** u ∈ L₂ ⇔ existe c con uc ∈ L. Se conservan estados y transiciones, y F' = {q : ∃c, δ(q,c) ∈ F} = {D, E}, pues D llega a F con 0 y E con 1, mientras que F va a D con ambos símbolos.

| Estado | 0 | 1 |
|---|---|---|
| →q0 | q1 | q2 |
| q1 | q2 | q3 |
| q2 | q3 | q4 |
| *q3 | q5 | q4 |
| *q4 | q4 | q5 |
| q5 | q3 | q3 |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `10` | acepta | acepta | acepta |
| 2 | `11` | acepta | acepta | acepta |
| 3 | `10110` | acepta | acepta | acepta |
| 4 | `1011010` | acepta | acepta | acepta |
| 5 | `00110110001` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `00` | rechaza | rechaza | rechaza |
| 8 | `10010` | rechaza | rechaza | rechaza |
| 9 | `1010001` | rechaza | rechaza | rechaza |
| 10 | `111101100110` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `10`: q0 -1→ q2 -0→ q3 — ✔
2. `11`: q0 -1→ q2 -1→ q4 — ✔
3. `10110`: q0 -1→ q2 -0→ q3 -1→ q4 -1→ q5 -0→ q3 — ✔
4. `1011010`: q0 -1→ q2 -0→ q3 -1→ q4 -1→ q5 -0→ q3 -1→ q4 -0→ q4 — ✔
5. `00110110001`: q0 -0→ q1 -0→ q2 -1→ q4 -1→ q5 -0→ q3 -1→ q4 -1→ q5 -0→ q3 -0→ q5 -0→ q3 -1→ q4 — ✔
6. λ: q0 — ✘
7. `00`: q0 -0→ q1 -0→ q2 — ✘
8. `10010`: q0 -1→ q2 -0→ q3 -0→ q5 -1→ q3 -0→ q5 — ✘
9. `1010001`: q0 -1→ q2 -0→ q3 -1→ q4 -0→ q4 -0→ q4 -0→ q4 -1→ q5 — ✘
10. `111101100110`: q0 -1→ q2 -1→ q4 -1→ q5 -1→ q3 -0→ q5 -1→ q3 -1→ q4 -0→ q4 -0→ q4 -1→ q5 -1→ q3 -0→ q5 — ✘

</details>

Simulación paso a paso en JFLAP con `10`: [ver captura](../../evidencias/jflap/pasos/L2-128-L2.png).

<a id="problema-2-129"></a>

## Lista 2, problema 129

**Enunciado.** AFD M que acepta LM = {w ∈ {a,b}* : w no contiene tres b consecutivas}, dado por su tabla.

**Clasificación: AFD.** El enunciado da el AFD completo (δ total, un destino por par); solo se transcribe y se verifica.

#### AFD dado en el enunciado — `L2-129`

Archivos: [`L2-129.jff`](../../automatas/lista2-afd/L2-129.jff) · [`L2-129.json`](../../automatas/lista2-afd/L2-129.json) · [`L2-129.xml`](../../automatas/lista2-afd/L2-129.xml). Tipo según la definición: **AFD**, |Q| = 4, Σ = {a, b}, 8 transiciones.

**Diseño.** Transcripción de la tabla. qᵢ = la racha actual de b tiene longitud i; q3 = ya hubo bbb (rechazo absorbente).

| Estado | a | b | Significado |
|---|---|---|---|
| →*q0 | q0 | q1 | racha de b de longitud 0 |
| *q1 | q0 | q2 | racha de longitud 1 |
| *q2 | q0 | q3 | racha de longitud 2 |
| q3 | q3 | q3 | ya apareció bbb |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | acepta | acepta | acepta |
| 2 | `ba` | acepta | acepta | acepta |
| 3 | `abaa` | acepta | acepta | acepta |
| 4 | `aabbaba` | acepta | acepta | acepta |
| 5 | `bbabbabaaba` | acepta | acepta | acepta |
| 6 | `bbb` | rechaza | rechaza | rechaza |
| 7 | `babbb` | rechaza | rechaza | rechaza |
| 8 | `bbaabbb` | rechaza | rechaza | rechaza |
| 9 | `bbaabbabbb` | rechaza | rechaza | rechaza |
| 10 | `bbaabbbaaba` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: q0 — ✔
2. `ba`: q0 -b→ q1 -a→ q0 — ✔
3. `abaa`: q0 -a→ q0 -b→ q1 -a→ q0 -a→ q0 — ✔
4. `aabbaba`: q0 -a→ q0 -a→ q0 -b→ q1 -b→ q2 -a→ q0 -b→ q1 -a→ q0 — ✔
5. `bbabbabaaba`: q0 -b→ q1 -b→ q2 -a→ q0 -b→ q1 -b→ q2 -a→ q0 -b→ q1 -a→ q0 -a→ q0 -b→ q1 -a→ q0 — ✔
6. `bbb`: q0 -b→ q1 -b→ q2 -b→ q3 — ✘
7. `babbb`: q0 -b→ q1 -a→ q0 -b→ q1 -b→ q2 -b→ q3 — ✘
8. `bbaabbb`: q0 -b→ q1 -b→ q2 -a→ q0 -a→ q0 -b→ q1 -b→ q2 -b→ q3 — ✘
9. `bbaabbabbb`: q0 -b→ q1 -b→ q2 -a→ q0 -a→ q0 -b→ q1 -b→ q2 -a→ q0 -b→ q1 -b→ q2 -b→ q3 — ✘
10. `bbaabbbaaba`: q0 -b→ q1 -b→ q2 -a→ q0 -a→ q0 -b→ q1 -b→ q2 -b→ q3 -a→ q3 -a→ q3 -b→ q3 -a→ q3 — ✘

</details>

Simulación paso a paso en JFLAP con `ba`: [ver captura](../../evidencias/jflap/pasos/L2-129.png).

<a id="problema-2-130"></a>

## Lista 2, problema 130

**Enunciado.** AFD M = ({q1,q2,q3}, {0,1}, δ, q1, {q2}) dado por su tabla; describir el lenguaje.

**Clasificación: AFD.** El enunciado da el AFD completo; se transcribe y se corrige la descripción de su lenguaje.

Comprobación: 100 ∈ L (dos 0 tras el último 1) y 10 ∉ L (uno); 1001 ∈ L porque cuenta el último 1, y 0110 ∉ L.

#### AFD dado en el enunciado — `L2-130`

Archivos: [`L2-130.jff`](../../automatas/lista2-afd/L2-130.jff) · [`L2-130.json`](../../automatas/lista2-afd/L2-130.json) · [`L2-130.xml`](../../automatas/lista2-afd/L2-130.xml). Tipo según la definición: **AFD**, |Q| = 3, Σ = {0, 1}, 6 transiciones.

**Diseño.** Transcripción de la tabla. La descripción del enunciado («alternan entre estados hasta llegar a q2») es imprecisa; el lenguaje exacto es: w tiene al menos un 1 y después del último 1 hay un número par de 0. q1: aún no hay 1; q2: después del último 1 hay un número par de 0; q3: hay un número impar.

| Estado | 0 | 1 | Significado |
|---|---|---|---|
| →q1 | q1 | q2 | todavía no aparece un 1 |
| *q2 | q3 | q2 | tras el último 1, número par de 0 |
| q3 | q2 | q2 | tras el último 1, número impar de 0 |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `1` | acepta | acepta | acepta |
| 2 | `001` | acepta | acepta | acepta |
| 3 | `1101` | acepta | acepta | acepta |
| 4 | `11110000` | acepta | acepta | acepta |
| 5 | `10111100100` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `010` | rechaza | rechaza | rechaza |
| 8 | `00010` | rechaza | rechaza | rechaza |
| 9 | `1000010` | rechaza | rechaza | rechaza |
| 10 | `101101001010` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `1`: q1 -1→ q2 — ✔
2. `001`: q1 -0→ q1 -0→ q1 -1→ q2 — ✔
3. `1101`: q1 -1→ q2 -1→ q2 -0→ q3 -1→ q2 — ✔
4. `11110000`: q1 -1→ q2 -1→ q2 -1→ q2 -1→ q2 -0→ q3 -0→ q2 -0→ q3 -0→ q2 — ✔
5. `10111100100`: q1 -1→ q2 -0→ q3 -1→ q2 -1→ q2 -1→ q2 -1→ q2 -0→ q3 -0→ q2 -1→ q2 -0→ q3 -0→ q2 — ✔
6. λ: q1 — ✘
7. `010`: q1 -0→ q1 -1→ q2 -0→ q3 — ✘
8. `00010`: q1 -0→ q1 -0→ q1 -0→ q1 -1→ q2 -0→ q3 — ✘
9. `1000010`: q1 -1→ q2 -0→ q3 -0→ q2 -0→ q3 -0→ q2 -1→ q2 -0→ q3 — ✘
10. `101101001010`: q1 -1→ q2 -0→ q3 -1→ q2 -1→ q2 -0→ q3 -1→ q2 -0→ q3 -0→ q2 -1→ q2 -0→ q3 -1→ q2 -0→ q3 — ✘

</details>

Simulación paso a paso en JFLAP con `001`: [ver captura](../../evidencias/jflap/pasos/L2-130.png).

<a id="problema-2-131"></a>

## Lista 2, problema 131

**Enunciado.** Dibujar M = ({q1,q2},{0,1},δ,q1,{q2}) y hallar L(M).

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### Dibujar M = ({q1,q2},{0,1},δ,q1,{q2}) y hallar L(M). — `L2-131`

Archivos: [`L2-131.jff`](../../automatas/lista2-afd/L2-131.jff) · [`L2-131.json`](../../automatas/lista2-afd/L2-131.json) · [`L2-131.xml`](../../automatas/lista2-afd/L2-131.xml). Tipo según la definición: **AFD**, |Q| = 2, Σ = {0, 1}, 4 transiciones.

**Diseño.** El estado solo recuerda el último símbolo: 1 lleva a q2 y 0 lleva a q1. L(M) = Σ*1, las cadenas que terminan en 1.

| Estado | 0 | 1 |
|---|---|---|
| →q0 | q0 | q1 |
| *q1 | q0 | q1 |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `1` | acepta | acepta | acepta |
| 2 | `11` | acepta | acepta | acepta |
| 3 | `0011` | acepta | acepta | acepta |
| 4 | `1001111` | acepta | acepta | acepta |
| 5 | `11100101001` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `10` | rechaza | rechaza | rechaza |
| 8 | `01010` | rechaza | rechaza | rechaza |
| 9 | `00100110` | rechaza | rechaza | rechaza |
| 10 | `01111110110` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `1`: q0 -1→ q1 — ✔
2. `11`: q0 -1→ q1 -1→ q1 — ✔
3. `0011`: q0 -0→ q0 -0→ q0 -1→ q1 -1→ q1 — ✔
4. `1001111`: q0 -1→ q1 -0→ q0 -0→ q0 -1→ q1 -1→ q1 -1→ q1 -1→ q1 — ✔
5. `11100101001`: q0 -1→ q1 -1→ q1 -1→ q1 -0→ q0 -0→ q0 -1→ q1 -0→ q0 -1→ q1 -0→ q0 -0→ q0 -1→ q1 — ✔
6. λ: q0 — ✘
7. `10`: q0 -1→ q1 -0→ q0 — ✘
8. `01010`: q0 -0→ q0 -1→ q1 -0→ q0 -1→ q1 -0→ q0 — ✘
9. `00100110`: q0 -0→ q0 -0→ q0 -1→ q1 -0→ q0 -0→ q0 -1→ q1 -1→ q1 -0→ q0 — ✘
10. `01111110110`: q0 -0→ q0 -1→ q1 -1→ q1 -1→ q1 -1→ q1 -1→ q1 -1→ q1 -0→ q0 -1→ q1 -1→ q1 -0→ q0 — ✘

</details>

Simulación paso a paso en JFLAP con `11`: [ver captura](../../evidencias/jflap/pasos/L2-131.png).

<a id="problema-2-132"></a>

## Lista 2, problema 132

**Enunciado.** Diseñar un AFD para L = {aⁿb : n ≥ 0}.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Un bloque de a y una sola b final.

#### AFD — `L2-132`

Archivos: [`L2-132.jff`](../../automatas/lista2-afd/L2-132.jff) · [`L2-132.json`](../../automatas/lista2-afd/L2-132.json) · [`L2-132.xml`](../../automatas/lista2-afd/L2-132.xml). Tipo según la definición: **AFD**, |Q| = 3, Σ = {a, b}, 6 transiciones.

**Diseño.** q0 tiene un lazo con a (n ≥ 0 permite cero a); la b lleva a q1, el único de aceptación. Cualquier símbolo después de la b lleva al rechazo absorbente.

| Estado | a | b | Significado |
|---|---|---|---|
| →q0 | q0 | q1 | bloque de a (posiblemente vacío) |
| *q1 | q2 | q2 | se leyó la b final |
| q2 | q2 | q2 | rechazo absorbente |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `b` | acepta | acepta | acepta |
| 2 | `ab` | acepta | acepta | acepta |
| 3 | `aab` | acepta | acepta | acepta |
| 4 | `aaab` | acepta | acepta | acepta |
| 5 | `aaaaab` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `bb` | rechaza | rechaza | rechaza |
| 8 | `aaaa` | rechaza | rechaza | rechaza |
| 9 | `abbbaaa` | rechaza | rechaza | rechaza |
| 10 | `aaaaaaabbbb` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `b`: q0 -b→ q1 — ✔
2. `ab`: q0 -a→ q0 -b→ q1 — ✔
3. `aab`: q0 -a→ q0 -a→ q0 -b→ q1 — ✔
4. `aaab`: q0 -a→ q0 -a→ q0 -a→ q0 -b→ q1 — ✔
5. `aaaaab`: q0 -a→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q0 -b→ q1 — ✔
6. λ: q0 — ✘
7. `bb`: q0 -b→ q1 -b→ q2 — ✘
8. `aaaa`: q0 -a→ q0 -a→ q0 -a→ q0 -a→ q0 — ✘
9. `abbbaaa`: q0 -a→ q0 -b→ q1 -b→ q2 -b→ q2 -a→ q2 -a→ q2 -a→ q2 — ✘
10. `aaaaaaabbbb`: q0 -a→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q0 -b→ q1 -b→ q2 -b→ q2 -b→ q2 — ✘

</details>

Simulación paso a paso en JFLAP con `ab`: [ver captura](../../evidencias/jflap/pasos/L2-132.png).

<a id="problema-2-133"></a>

## Lista 2, problema 133

**Enunciado.** Tabla y diagrama del autómata dado con Q = {q0,q1,q2,q3}, F = {q0}.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### Tabla y diagrama del autómata dado con Q = {q0,q1,q2,q3}, F = {q0}. — `L2-133`

Archivos: [`L2-133.jff`](../../automatas/lista2-afd/L2-133.jff) · [`L2-133.json`](../../automatas/lista2-afd/L2-133.json) · [`L2-133.xml`](../../automatas/lista2-afd/L2-133.xml). Tipo según la definición: **AFD**, |Q| = 4, Σ = {a, b}, 8 transiciones.

**Diseño.** Los estados codifican la paridad de a y de b: q0 (par, par), q1 (par, impar), q2 (impar, par), q3 (impar, impar). Acepta si ambas son pares.

| Estado | a | b |
|---|---|---|
| →*q0 | q1 | q2 |
| q2 | q3 | q0 |
| q1 | q0 | q3 |
| q3 | q2 | q1 |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | acepta | acepta | acepta |
| 2 | `baba` | acepta | acepta | acepta |
| 3 | `abaaba` | acepta | acepta | acepta |
| 4 | `bbbaaaab` | acepta | acepta | acepta |
| 5 | `baababbaabab` | acepta | acepta | acepta |
| 6 | `a` | rechaza | rechaza | — |
| 7 | `bba` | rechaza | rechaza | — |
| 8 | `aaba` | rechaza | rechaza | rechaza |
| 9 | `bbbaabb` | rechaza | rechaza | rechaza |
| 10 | `aaaaabbaaab` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: q0 — ✔
2. `baba`: q0 -b→ q2 -a→ q3 -b→ q1 -a→ q0 — ✔
3. `abaaba`: q0 -a→ q1 -b→ q3 -a→ q2 -a→ q3 -b→ q1 -a→ q0 — ✔
4. `bbbaaaab`: q0 -b→ q2 -b→ q0 -b→ q2 -a→ q3 -a→ q2 -a→ q3 -a→ q2 -b→ q0 — ✔
5. `baababbaabab`: q0 -b→ q2 -a→ q3 -a→ q2 -b→ q0 -a→ q1 -b→ q3 -b→ q1 -a→ q0 -a→ q1 -b→ q3 -a→ q2 -b→ q0 — ✔
6. `a`: q0 -a→ q1 — ✘
7. `bba`: q0 -b→ q2 -b→ q0 -a→ q1 — ✘
8. `aaba`: q0 -a→ q1 -a→ q0 -b→ q2 -a→ q3 — ✘
9. `bbbaabb`: q0 -b→ q2 -b→ q0 -b→ q2 -a→ q3 -a→ q2 -b→ q0 -b→ q2 — ✘
10. `aaaaabbaaab`: q0 -a→ q1 -a→ q0 -a→ q1 -a→ q0 -a→ q1 -b→ q3 -b→ q1 -a→ q0 -a→ q1 -a→ q0 -b→ q2 — ✘

</details>

Simulación paso a paso en JFLAP con `baba`: [ver captura](../../evidencias/jflap/pasos/L2-133.png).

<a id="problema-2-134"></a>

## Lista 2, problema 134

**Enunciado.** L(M) = {w | w ∈ {a,b,c}* y w contiene el patrón abac}.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Búsqueda de subcadena (aplicación a búsqueda de texto).

#### AFD — `L2-134`

Archivos: [`L2-134.jff`](../../automatas/lista2-afd/L2-134.jff) · [`L2-134.json`](../../automatas/lista2-afd/L2-134.json) · [`L2-134.xml`](../../automatas/lista2-afd/L2-134.xml). Tipo según la definición: **AFD**, |Q| = 5, Σ = {a, b, c}, 15 transiciones.

**Diseño.** Búsqueda de abac con función de fallo: en q3 (aba) una b regresa a q2 porque ab es prefijo del patrón; una a regresa a q1. q4 es de aceptación y absorbente.

| Estado | a | b | c | Significado |
|---|---|---|---|---|
| →q0 | q1 | q0 | q0 | ningún avance en el patrón |
| q1 | q1 | q2 | q0 | los últimos símbolos coinciden con «a» |
| q2 | q3 | q0 | q0 | los últimos símbolos coinciden con «ab» |
| q3 | q1 | q2 | q4 | los últimos símbolos coinciden con «aba» |
| *q4 | q4 | q4 | q4 | «abac» ya apareció |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `abac` | acepta | acepta | acepta |
| 2 | `bbabac` | acepta | acepta | acepta |
| 3 | `aabcabac` | acepta | acepta | acepta |
| 4 | `cbcbbccabac` | acepta | acepta | acepta |
| 5 | `aacabaacbabac` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `cc` | rechaza | rechaza | rechaza |
| 8 | `ccaa` | rechaza | rechaza | rechaza |
| 9 | `cabbcaa` | rechaza | rechaza | rechaza |
| 10 | `cbcbaccaaaa` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `abac`: q0 -a→ q1 -b→ q2 -a→ q3 -c→ q4 — ✔
2. `bbabac`: q0 -b→ q0 -b→ q0 -a→ q1 -b→ q2 -a→ q3 -c→ q4 — ✔
3. `aabcabac`: q0 -a→ q1 -a→ q1 -b→ q2 -c→ q0 -a→ q1 -b→ q2 -a→ q3 -c→ q4 — ✔
4. `cbcbbccabac`: q0 -c→ q0 -b→ q0 -c→ q0 -b→ q0 -b→ q0 -c→ q0 -c→ q0 -a→ q1 -b→ q2 -a→ q3 -c→ q4 — ✔
5. `aacabaacbabac`: q0 -a→ q1 -a→ q1 -c→ q0 -a→ q1 -b→ q2 -a→ q3 -a→ q1 -c→ q0 -b→ q0 -a→ q1 -b→ q2 -a→ q3 -c→ q4 — ✔
6. λ: q0 — ✘
7. `cc`: q0 -c→ q0 -c→ q0 — ✘
8. `ccaa`: q0 -c→ q0 -c→ q0 -a→ q1 -a→ q1 — ✘
9. `cabbcaa`: q0 -c→ q0 -a→ q1 -b→ q2 -b→ q0 -c→ q0 -a→ q1 -a→ q1 — ✘
10. `cbcbaccaaaa`: q0 -c→ q0 -b→ q0 -c→ q0 -b→ q0 -a→ q1 -c→ q0 -c→ q0 -a→ q1 -a→ q1 -a→ q1 -a→ q1 — ✘

</details>

Simulación paso a paso en JFLAP con `abac`: [ver captura](../../evidencias/jflap/pasos/L2-134.png).

<a id="problema-2-135"></a>

## Lista 2, problema 135

**Enunciado.** L = {bᵐ a bⁿ : m, n > 0}.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### L = {bᵐ a bⁿ : m, n > 0}. — `L2-135`

Archivos: [`L2-135.jff`](../../automatas/lista2-afd/L2-135.jff) · [`L2-135.json`](../../automatas/lista2-afd/L2-135.json) · [`L2-135.xml`](../../automatas/lista2-afd/L2-135.xml). Tipo según la definición: **AFD**, |Q| = 5, Σ = {a, b}, 10 transiciones.

**Diseño.** Etapas: inicio; ya hay b; ya se leyó la única a; ya hay b tras la a (acepta). Cualquier violación va al rechazo absorbente.

| Estado | a | b |
|---|---|---|
| q1 | q1 | q1 |
| q3 | q1 | q4 |
| *q4 | q1 | q4 |
| q2 | q3 | q2 |
| →q0 | q1 | q2 |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `bab` | acepta | acepta | acepta |
| 2 | `babb` | acepta | acepta | acepta |
| 3 | `bbab` | acepta | acepta | acepta |
| 4 | `babbbbb` | acepta | acepta | acepta |
| 5 | `bbbbabbbbbb` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `aa` | rechaza | rechaza | rechaza |
| 8 | `aaba` | rechaza | rechaza | rechaza |
| 9 | `aabbbba` | rechaza | rechaza | rechaza |
| 10 | `bbabaaaabbb` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `bab`: q0 -b→ q2 -a→ q3 -b→ q4 — ✔
2. `babb`: q0 -b→ q2 -a→ q3 -b→ q4 -b→ q4 — ✔
3. `bbab`: q0 -b→ q2 -b→ q2 -a→ q3 -b→ q4 — ✔
4. `babbbbb`: q0 -b→ q2 -a→ q3 -b→ q4 -b→ q4 -b→ q4 -b→ q4 -b→ q4 — ✔
5. `bbbbabbbbbb`: q0 -b→ q2 -b→ q2 -b→ q2 -b→ q2 -a→ q3 -b→ q4 -b→ q4 -b→ q4 -b→ q4 -b→ q4 -b→ q4 — ✔
6. λ: q0 — ✘
7. `aa`: q0 -a→ q1 -a→ q1 — ✘
8. `aaba`: q0 -a→ q1 -a→ q1 -b→ q1 -a→ q1 — ✘
9. `aabbbba`: q0 -a→ q1 -a→ q1 -b→ q1 -b→ q1 -b→ q1 -b→ q1 -a→ q1 — ✘
10. `bbabaaaabbb`: q0 -b→ q2 -b→ q2 -a→ q3 -b→ q4 -a→ q1 -a→ q1 -a→ q1 -a→ q1 -b→ q1 -b→ q1 -b→ q1 — ✘

</details>

Simulación paso a paso en JFLAP con `bab`: [ver captura](../../evidencias/jflap/pasos/L2-135.png).

<a id="problema-2-136"></a>

## Lista 2, problema 136

**Enunciado.** Dado Σ = {a,b}, construir un AFD para L = {aᵐbⁿ : m, n > 0}.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Dos fases, cada una con al menos un símbolo.

#### AFD — `L2-136`

Archivos: [`L2-136.jff`](../../automatas/lista2-afd/L2-136.jff) · [`L2-136.json`](../../automatas/lista2-afd/L2-136.json) · [`L2-136.xml`](../../automatas/lista2-afd/L2-136.xml). Tipo según la definición: **AFD**, |Q| = 4, Σ = {a, b}, 8 transiciones.

**Diseño.** Igual que el 114 (allí ℕ empieza en 1): q1 = al menos una a; q2 = al menos una b tras ellas (acepta); el orden inverso lleva al rechazo absorbente.

| Estado | a | b | Significado |
|---|---|---|---|
| →q0 | q1 | q2 | inicio |
| q1 | q1 | q3 | bloque de a |
| q2 | q2 | q2 | rechazo absorbente |
| *q3 | q2 | q3 | bloque de b tras las a |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `ab` | acepta | acepta | acepta |
| 2 | `aab` | acepta | acepta | acepta |
| 3 | `abbb` | acepta | acepta | acepta |
| 4 | `abbbbbb` | acepta | acepta | acepta |
| 5 | `aaaabbbbbbb` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `aa` | rechaza | rechaza | rechaza |
| 8 | `aaaba` | rechaza | rechaza | rechaza |
| 9 | `baaaabb` | rechaza | rechaza | rechaza |
| 10 | `bbaaababbaa` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `ab`: q0 -a→ q1 -b→ q3 — ✔
2. `aab`: q0 -a→ q1 -a→ q1 -b→ q3 — ✔
3. `abbb`: q0 -a→ q1 -b→ q3 -b→ q3 -b→ q3 — ✔
4. `abbbbbb`: q0 -a→ q1 -b→ q3 -b→ q3 -b→ q3 -b→ q3 -b→ q3 -b→ q3 — ✔
5. `aaaabbbbbbb`: q0 -a→ q1 -a→ q1 -a→ q1 -a→ q1 -b→ q3 -b→ q3 -b→ q3 -b→ q3 -b→ q3 -b→ q3 -b→ q3 — ✔
6. λ: q0 — ✘
7. `aa`: q0 -a→ q1 -a→ q1 — ✘
8. `aaaba`: q0 -a→ q1 -a→ q1 -a→ q1 -b→ q3 -a→ q2 — ✘
9. `baaaabb`: q0 -b→ q2 -a→ q2 -a→ q2 -a→ q2 -a→ q2 -b→ q2 -b→ q2 — ✘
10. `bbaaababbaa`: q0 -b→ q2 -b→ q2 -a→ q2 -a→ q2 -a→ q2 -b→ q2 -a→ q2 -b→ q2 -b→ q2 -a→ q2 -a→ q2 — ✘

</details>

Simulación paso a paso en JFLAP con `ab`: [ver captura](../../evidencias/jflap/pasos/L2-136.png).

<a id="problema-2-137"></a>

## Lista 2, problema 137

**Enunciado.** Cadenas sobre {a,b} con prefijo ab.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### Cadenas sobre {a,b} con prefijo ab. — `L2-137`

Archivos: [`L2-137.jff`](../../automatas/lista2-afd/L2-137.jff) · [`L2-137.json`](../../automatas/lista2-afd/L2-137.json) · [`L2-137.xml`](../../automatas/lista2-afd/L2-137.xml). Tipo según la definición: **AFD**, |Q| = 4, Σ = {a, b}, 8 transiciones.

**Diseño.** Estados: nada leído; leí a; prefijo ab confirmado (aceptación absorbente); rechazo absorbente.

| Estado | a | b |
|---|---|---|
| q1 | q2 | q3 |
| q2 | q2 | q2 |
| *q3 | q3 | q3 |
| →q0 | q1 | q2 |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `ab` | acepta | acepta | acepta |
| 2 | `abab` | acepta | acepta | acepta |
| 3 | `abaabab` | acepta | acepta | acepta |
| 4 | `abaababaabb` | acepta | acepta | acepta |
| 5 | `ababbbabbabbbbbb` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `ba` | rechaza | rechaza | rechaza |
| 8 | `bbaa` | rechaza | rechaza | rechaza |
| 9 | `aabbbba` | rechaza | rechaza | rechaza |
| 10 | `babbaaababb` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `ab`: q0 -a→ q1 -b→ q3 — ✔
2. `abab`: q0 -a→ q1 -b→ q3 -a→ q3 -b→ q3 — ✔
3. `abaabab`: q0 -a→ q1 -b→ q3 -a→ q3 -a→ q3 -b→ q3 -a→ q3 -b→ q3 — ✔
4. `abaababaabb`: q0 -a→ q1 -b→ q3 -a→ q3 -a→ q3 -b→ q3 -a→ q3 -b→ q3 -a→ q3 -a→ q3 -b→ q3 -b→ q3 — ✔
5. `ababbbabbabbbbbb`: q0 -a→ q1 -b→ q3 -a→ q3 -b→ q3 -b→ q3 -b→ q3 -a→ q3 -b→ q3 -b→ q3 -a→ q3 -b→ q3 -b→ q3 -b→ q3 -b→ q3 -b→ q3 -b→ q3 — ✔
6. λ: q0 — ✘
7. `ba`: q0 -b→ q2 -a→ q2 — ✘
8. `bbaa`: q0 -b→ q2 -b→ q2 -a→ q2 -a→ q2 — ✘
9. `aabbbba`: q0 -a→ q1 -a→ q2 -b→ q2 -b→ q2 -b→ q2 -b→ q2 -a→ q2 — ✘
10. `babbaaababb`: q0 -b→ q2 -a→ q2 -b→ q2 -b→ q2 -a→ q2 -a→ q2 -a→ q2 -b→ q2 -a→ q2 -b→ q2 -b→ q2 — ✘

</details>

Simulación paso a paso en JFLAP con `ab`: [ver captura](../../evidencias/jflap/pasos/L2-137.png).

<a id="problema-2-138"></a>

## Lista 2, problema 138

**Enunciado.** AFD sobre {a,b} que acepta las palabras cuyo número de b es divisible entre tres.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Contador módulo 3 de las b.

#### AFD — `L2-138`

Archivos: [`L2-138.jff`](../../automatas/lista2-afd/L2-138.jff) · [`L2-138.json`](../../automatas/lista2-afd/L2-138.json) · [`L2-138.xml`](../../automatas/lista2-afd/L2-138.xml). Tipo según la definición: **AFD**, |Q| = 3, Σ = {a, b}, 6 transiciones.

**Diseño.** qᵢ = el número de b leídas es ≡ i (mód 3). La a no cambia el estado (lazo) y la b avanza el contador. q0 es inicial y de aceptación porque 0 es divisible entre 3.

| Estado | a | b | Significado |
|---|---|---|---|
| →*q0 | q0 | q1 | #b ≡ 0 (mód 3) |
| q1 | q1 | q2 | #b ≡ 1 (mód 3) |
| q2 | q2 | q0 | #b ≡ 2 (mód 3) |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | acepta | acepta | acepta |
| 2 | `bbb` | acepta | acepta | acepta |
| 3 | `bbab` | acepta | acepta | acepta |
| 4 | `baabaab` | acepta | acepta | acepta |
| 5 | `abaaabaababbb` | acepta | acepta | acepta |
| 6 | `b` | rechaza | rechaza | rechaza |
| 7 | `aab` | rechaza | rechaza | rechaza |
| 8 | `aabb` | rechaza | rechaza | rechaza |
| 9 | `bbabaab` | rechaza | rechaza | rechaza |
| 10 | `bbbabbabaaab` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: q0 — ✔
2. `bbb`: q0 -b→ q1 -b→ q2 -b→ q0 — ✔
3. `bbab`: q0 -b→ q1 -b→ q2 -a→ q2 -b→ q0 — ✔
4. `baabaab`: q0 -b→ q1 -a→ q1 -a→ q1 -b→ q2 -a→ q2 -a→ q2 -b→ q0 — ✔
5. `abaaabaababbb`: q0 -a→ q0 -b→ q1 -a→ q1 -a→ q1 -a→ q1 -b→ q2 -a→ q2 -a→ q2 -b→ q0 -a→ q0 -b→ q1 -b→ q2 -b→ q0 — ✔
6. `b`: q0 -b→ q1 — ✘
7. `aab`: q0 -a→ q0 -a→ q0 -b→ q1 — ✘
8. `aabb`: q0 -a→ q0 -a→ q0 -b→ q1 -b→ q2 — ✘
9. `bbabaab`: q0 -b→ q1 -b→ q2 -a→ q2 -b→ q0 -a→ q0 -a→ q0 -b→ q1 — ✘
10. `bbbabbabaaab`: q0 -b→ q1 -b→ q2 -b→ q0 -a→ q0 -b→ q1 -b→ q2 -a→ q2 -b→ q0 -a→ q0 -a→ q0 -a→ q0 -b→ q1 — ✘

</details>

Simulación paso a paso en JFLAP con `bbb`: [ver captura](../../evidencias/jflap/pasos/L2-138.png).

<a id="problema-2-139"></a>

## Lista 2, problema 139

**Enunciado.** Cadenas en {0,1}* con número par de ceros.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### Cadenas en {0,1}* con número par de ceros. — `L2-139`

Archivos: [`L2-139.jff`](../../automatas/lista2-afd/L2-139.jff) · [`L2-139.json`](../../automatas/lista2-afd/L2-139.json) · [`L2-139.xml`](../../automatas/lista2-afd/L2-139.xml). Tipo según la definición: **AFD**, |Q| = 2, Σ = {0, 1}, 4 transiciones.

**Diseño.** El estado guarda la paridad de los ceros leídos; 0 la invierte y 1 no la cambia.

| Estado | 0 | 1 |
|---|---|---|
| q1 | q0 | q1 |
| →*q0 | q1 | q0 |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | acepta | acepta | acepta |
| 2 | `010` | acepta | acepta | acepta |
| 3 | `0000` | acepta | acepta | acepta |
| 4 | `00100010` | acepta | acepta | acepta |
| 5 | `10111011010` | acepta | acepta | acepta |
| 6 | `0` | rechaza | rechaza | rechaza |
| 7 | `10` | rechaza | rechaza | rechaza |
| 8 | `1110` | rechaza | rechaza | rechaza |
| 9 | `0101110` | rechaza | rechaza | rechaza |
| 10 | `11100010101` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: q0 — ✔
2. `010`: q0 -0→ q1 -1→ q1 -0→ q0 — ✔
3. `0000`: q0 -0→ q1 -0→ q0 -0→ q1 -0→ q0 — ✔
4. `00100010`: q0 -0→ q1 -0→ q0 -1→ q0 -0→ q1 -0→ q0 -0→ q1 -1→ q1 -0→ q0 — ✔
5. `10111011010`: q0 -1→ q0 -0→ q1 -1→ q1 -1→ q1 -1→ q1 -0→ q0 -1→ q0 -1→ q0 -0→ q1 -1→ q1 -0→ q0 — ✔
6. `0`: q0 -0→ q1 — ✘
7. `10`: q0 -1→ q0 -0→ q1 — ✘
8. `1110`: q0 -1→ q0 -1→ q0 -1→ q0 -0→ q1 — ✘
9. `0101110`: q0 -0→ q1 -1→ q1 -0→ q0 -1→ q0 -1→ q0 -1→ q0 -0→ q1 — ✘
10. `11100010101`: q0 -1→ q0 -1→ q0 -1→ q0 -0→ q1 -0→ q0 -0→ q1 -1→ q1 -0→ q0 -1→ q0 -0→ q1 -1→ q1 — ✘

</details>

Simulación paso a paso en JFLAP con `010`: [ver captura](../../evidencias/jflap/pasos/L2-139.png).

<a id="problema-2-140"></a>

## Lista 2, problema 140

**Enunciado.** Autómata finito sobre {0,1} para: a) un número impar de ceros; b) un número par de ceros y un número par de unos.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Contadores de paridad (uno para a; un par para b).

#### a) Número impar de ceros — `L2-140a`

Archivos: [`L2-140a.jff`](../../automatas/lista2-afd/L2-140a.jff) · [`L2-140a.json`](../../automatas/lista2-afd/L2-140a.json) · [`L2-140a.xml`](../../automatas/lista2-afd/L2-140a.xml). Tipo según la definición: **AFD**, |Q| = 2, Σ = {0, 1}, 4 transiciones.

**Diseño.** q0 = par de ceros, q1 = impar (acepta); el 0 cambia de estado y el 1 no.

| Estado | 0 | 1 | Significado |
|---|---|---|---|
| →q0 | q1 | q0 | par de ceros |
| *q1 | q0 | q1 | impar de ceros |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `0` | acepta | acepta | acepta |
| 2 | `10` | acepta | acepta | acepta |
| 3 | `11110` | acepta | acepta | acepta |
| 4 | `11010000` | acepta | acepta | acepta |
| 5 | `11011001100` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `11` | rechaza | rechaza | rechaza |
| 8 | `10000` | rechaza | rechaza | rechaza |
| 9 | `01011100` | rechaza | rechaza | rechaza |
| 10 | `01010111011` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `0`: q0 -0→ q1 — ✔
2. `10`: q0 -1→ q0 -0→ q1 — ✔
3. `11110`: q0 -1→ q0 -1→ q0 -1→ q0 -1→ q0 -0→ q1 — ✔
4. `11010000`: q0 -1→ q0 -1→ q0 -0→ q1 -1→ q1 -0→ q0 -0→ q1 -0→ q0 -0→ q1 — ✔
5. `11011001100`: q0 -1→ q0 -1→ q0 -0→ q1 -1→ q1 -1→ q1 -0→ q0 -0→ q1 -1→ q1 -1→ q1 -0→ q0 -0→ q1 — ✔
6. λ: q0 — ✘
7. `11`: q0 -1→ q0 -1→ q0 — ✘
8. `10000`: q0 -1→ q0 -0→ q1 -0→ q0 -0→ q1 -0→ q0 — ✘
9. `01011100`: q0 -0→ q1 -1→ q1 -0→ q0 -1→ q0 -1→ q0 -1→ q0 -0→ q1 -0→ q0 — ✘
10. `01010111011`: q0 -0→ q1 -1→ q1 -0→ q0 -1→ q0 -0→ q1 -1→ q1 -1→ q1 -1→ q1 -0→ q0 -1→ q0 -1→ q0 — ✘

</details>

Simulación paso a paso en JFLAP con `10`: [ver captura](../../evidencias/jflap/pasos/L2-140a.png).

#### b) Par de ceros y par de unos — `L2-140b`

Archivos: [`L2-140b.jff`](../../automatas/lista2-afd/L2-140b.jff) · [`L2-140b.json`](../../automatas/lista2-afd/L2-140b.json) · [`L2-140b.xml`](../../automatas/lista2-afd/L2-140b.xml). Tipo según la definición: **AFD**, |Q| = 4, Σ = {0, 1}, 8 transiciones.

**Diseño.** El estado es el par (paridad de ceros, paridad de unos); el 0 cambia la primera componente y el 1 la segunda. Solo (par, par) acepta. Es el mismo autómata del problema 133.

| Estado | 0 | 1 | Significado |
|---|---|---|---|
| →*q0 | q1 | q2 | par de ceros, par de unos |
| q1 | q0 | q3 | impar de ceros, par de unos |
| q2 | q3 | q0 | par de ceros, impar de unos |
| q3 | q2 | q1 | impar de ceros, impar de unos |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | acepta | acepta | acepta |
| 2 | `1010` | acepta | acepta | acepta |
| 3 | `001010` | acepta | acepta | acepta |
| 4 | `00100010` | acepta | acepta | acepta |
| 5 | `001000111000` | acepta | acepta | acepta |
| 6 | `0` | rechaza | rechaza | — |
| 7 | `110` | rechaza | rechaza | — |
| 8 | `01010` | rechaza | rechaza | — |
| 9 | `1001101` | rechaza | rechaza | rechaza |
| 10 | `01110000111` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: q0 — ✔
2. `1010`: q0 -1→ q2 -0→ q3 -1→ q1 -0→ q0 — ✔
3. `001010`: q0 -0→ q1 -0→ q0 -1→ q2 -0→ q3 -1→ q1 -0→ q0 — ✔
4. `00100010`: q0 -0→ q1 -0→ q0 -1→ q2 -0→ q3 -0→ q2 -0→ q3 -1→ q1 -0→ q0 — ✔
5. `001000111000`: q0 -0→ q1 -0→ q0 -1→ q2 -0→ q3 -0→ q2 -0→ q3 -1→ q1 -1→ q3 -1→ q1 -0→ q0 -0→ q1 -0→ q0 — ✔
6. `0`: q0 -0→ q1 — ✘
7. `110`: q0 -1→ q2 -1→ q0 -0→ q1 — ✘
8. `01010`: q0 -0→ q1 -1→ q3 -0→ q2 -1→ q0 -0→ q1 — ✘
9. `1001101`: q0 -1→ q2 -0→ q3 -0→ q2 -1→ q0 -1→ q2 -0→ q3 -1→ q1 — ✘
10. `01110000111`: q0 -0→ q1 -1→ q3 -1→ q1 -1→ q3 -0→ q2 -0→ q3 -0→ q2 -0→ q3 -1→ q1 -1→ q3 -1→ q1 — ✘

</details>

Simulación paso a paso en JFLAP con `1010`: [ver captura](../../evidencias/jflap/pasos/L2-140b.png).

<a id="problema-2-141"></a>

## Lista 2, problema 141

**Enunciado.** Cadenas en {0,1}* donde cada 0 tiene un 1 inmediatamente a su derecha.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### Cadenas en {0,1}* donde cada 0 tiene un 1 inmediatamente a su derecha. — `L2-141`

Archivos: [`L2-141.jff`](../../automatas/lista2-afd/L2-141.jff) · [`L2-141.json`](../../automatas/lista2-afd/L2-141.json) · [`L2-141.xml`](../../automatas/lista2-afd/L2-141.xml). Tipo según la definición: **AFD**, |Q| = 3, Σ = {0, 1}, 6 transiciones.

**Diseño.** Estados: correcto (sin 0 pendiente), pendiente (último símbolo 0 aún sin su 1) y rechazo absorbente (00).

| Estado | 0 | 1 |
|---|---|---|
| q1 | q2 | q0 |
| q2 | q2 | q2 |
| →*q0 | q1 | q0 |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | acepta | acepta | acepta |
| 2 | `01` | acepta | acepta | acepta |
| 3 | `10101` | acepta | acepta | acepta |
| 4 | `0101011` | acepta | acepta | acepta |
| 5 | `11010111111` | acepta | acepta | acepta |
| 6 | `0` | rechaza | rechaza | rechaza |
| 7 | `10` | rechaza | rechaza | rechaza |
| 8 | `1001` | rechaza | rechaza | rechaza |
| 9 | `10101110` | rechaza | rechaza | rechaza |
| 10 | `11110000010` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: q0 — ✔
2. `01`: q0 -0→ q1 -1→ q0 — ✔
3. `10101`: q0 -1→ q0 -0→ q1 -1→ q0 -0→ q1 -1→ q0 — ✔
4. `0101011`: q0 -0→ q1 -1→ q0 -0→ q1 -1→ q0 -0→ q1 -1→ q0 -1→ q0 — ✔
5. `11010111111`: q0 -1→ q0 -1→ q0 -0→ q1 -1→ q0 -0→ q1 -1→ q0 -1→ q0 -1→ q0 -1→ q0 -1→ q0 -1→ q0 — ✔
6. `0`: q0 -0→ q1 — ✘
7. `10`: q0 -1→ q0 -0→ q1 — ✘
8. `1001`: q0 -1→ q0 -0→ q1 -0→ q2 -1→ q2 — ✘
9. `10101110`: q0 -1→ q0 -0→ q1 -1→ q0 -0→ q1 -1→ q0 -1→ q0 -1→ q0 -0→ q1 — ✘
10. `11110000010`: q0 -1→ q0 -1→ q0 -1→ q0 -1→ q0 -0→ q1 -0→ q2 -0→ q2 -0→ q2 -0→ q2 -1→ q2 -0→ q2 — ✘

</details>

Simulación paso a paso en JFLAP con `01`: [ver captura](../../evidencias/jflap/pasos/L2-141.png).

<a id="problema-2-142"></a>

## Lista 2, problema 142

**Enunciado.** Autómata finito sobre {a,b} para: a) LA = (ab)* = {(ab)ⁿ : n ≥ 0}; b) LB = {(ab)ⁿ : n ≥ 1}.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Ciclo de longitud 2 que reconoce ab.

#### a) (ab)* — `L2-142a`

Archivos: [`L2-142a.jff`](../../automatas/lista2-afd/L2-142a.jff) · [`L2-142a.json`](../../automatas/lista2-afd/L2-142a.json) · [`L2-142a.xml`](../../automatas/lista2-afd/L2-142a.xml). Tipo según la definición: **AFD**, |Q| = 3, Σ = {a, b}, 6 transiciones.

**Diseño.** El enunciado añade «la cadena vacía no es aceptada», lo que contradice n ≥ 0: (ab)⁰ = λ. Se sigue la definición formal, así que λ se acepta: q0 es inicial y de aceptación; q0 -a→ q1 -b→ q0.

| Estado | a | b | Significado |
|---|---|---|---|
| →*q0 | q1 | q2 | se han cerrado bloques ab completos |
| q1 | q2 | q0 | falta la b del bloque |
| q2 | q2 | q2 | rechazo absorbente |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | acepta | acepta | acepta |
| 2 | `ab` | acepta | acepta | acepta |
| 3 | `abab` | acepta | acepta | acepta |
| 4 | `abababab` | acepta | acepta | acepta |
| 5 | `abababababab` | acepta | acepta | acepta |
| 6 | `a` | rechaza | rechaza | — |
| 7 | `aa` | rechaza | rechaza | rechaza |
| 8 | `bbba` | rechaza | rechaza | rechaza |
| 9 | `abbbaba` | rechaza | rechaza | rechaza |
| 10 | `ababbabbaba` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: q0 — ✔
2. `ab`: q0 -a→ q1 -b→ q0 — ✔
3. `abab`: q0 -a→ q1 -b→ q0 -a→ q1 -b→ q0 — ✔
4. `abababab`: q0 -a→ q1 -b→ q0 -a→ q1 -b→ q0 -a→ q1 -b→ q0 -a→ q1 -b→ q0 — ✔
5. `abababababab`: q0 -a→ q1 -b→ q0 -a→ q1 -b→ q0 -a→ q1 -b→ q0 -a→ q1 -b→ q0 -a→ q1 -b→ q0 -a→ q1 -b→ q0 — ✔
6. `a`: q0 -a→ q1 — ✘
7. `aa`: q0 -a→ q1 -a→ q2 — ✘
8. `bbba`: q0 -b→ q2 -b→ q2 -b→ q2 -a→ q2 — ✘
9. `abbbaba`: q0 -a→ q1 -b→ q0 -b→ q2 -b→ q2 -a→ q2 -b→ q2 -a→ q2 — ✘
10. `ababbabbaba`: q0 -a→ q1 -b→ q0 -a→ q1 -b→ q0 -b→ q2 -a→ q2 -b→ q2 -b→ q2 -a→ q2 -b→ q2 -a→ q2 — ✘

</details>

Simulación paso a paso en JFLAP con `ab`: [ver captura](../../evidencias/jflap/pasos/L2-142a.png).

#### b) (ab)⁺ — `L2-142b`

Archivos: [`L2-142b.jff`](../../automatas/lista2-afd/L2-142b.jff) · [`L2-142b.json`](../../automatas/lista2-afd/L2-142b.json) · [`L2-142b.xml`](../../automatas/lista2-afd/L2-142b.xml). Tipo según la definición: **AFD**, |Q| = 4, Σ = {a, b}, 8 transiciones.

**Diseño.** Con n ≥ 1, λ queda fuera: q0 inicial no acepta; q2 = se cerró al menos un bloque ab.

| Estado | a | b | Significado |
|---|---|---|---|
| →q0 | q1 | q2 | inicio |
| q1 | q2 | q3 | falta la b del bloque |
| q2 | q2 | q2 | rechazo absorbente |
| *q3 | q1 | q2 | se cerró al menos un bloque ab |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `ab` | acepta | acepta | acepta |
| 2 | `abab` | acepta | acepta | acepta |
| 3 | `abababab` | acepta | acepta | acepta |
| 4 | `abababababab` | acepta | acepta | acepta |
| 5 | `abababababababab` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `bb` | rechaza | rechaza | rechaza |
| 8 | `bbba` | rechaza | rechaza | rechaza |
| 9 | `aababba` | rechaza | rechaza | rechaza |
| 10 | `bbabababbab` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `ab`: q0 -a→ q1 -b→ q3 — ✔
2. `abab`: q0 -a→ q1 -b→ q3 -a→ q1 -b→ q3 — ✔
3. `abababab`: q0 -a→ q1 -b→ q3 -a→ q1 -b→ q3 -a→ q1 -b→ q3 -a→ q1 -b→ q3 — ✔
4. `abababababab`: q0 -a→ q1 -b→ q3 -a→ q1 -b→ q3 -a→ q1 -b→ q3 -a→ q1 -b→ q3 -a→ q1 -b→ q3 -a→ q1 -b→ q3 — ✔
5. `abababababababab`: q0 -a→ q1 -b→ q3 -a→ q1 -b→ q3 -a→ q1 -b→ q3 -a→ q1 -b→ q3 -a→ q1 -b→ q3 -a→ q1 -b→ q3 -a→ q1 -b→ q3 -a→ q1 -b→ q3 — ✔
6. λ: q0 — ✘
7. `bb`: q0 -b→ q2 -b→ q2 — ✘
8. `bbba`: q0 -b→ q2 -b→ q2 -b→ q2 -a→ q2 — ✘
9. `aababba`: q0 -a→ q1 -a→ q2 -b→ q2 -a→ q2 -b→ q2 -b→ q2 -a→ q2 — ✘
10. `bbabababbab`: q0 -b→ q2 -b→ q2 -a→ q2 -b→ q2 -a→ q2 -b→ q2 -a→ q2 -b→ q2 -b→ q2 -a→ q2 -b→ q2 — ✘

</details>

Simulación paso a paso en JFLAP con `ab`: [ver captura](../../evidencias/jflap/pasos/L2-142b.png).

<a id="problema-2-143"></a>

## Lista 2, problema 143

**Enunciado.** Lenguaje del autómata de la figura (a). / Lenguaje del autómata de la figura (b).

**Clasificación: AFD.** La figura (a) es un AFD; la (b) es un AFND (dos destinos con b en q1) y se clasifica en esa sección. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### Lenguaje del autómata de la figura (a). — `L2-143a`

Archivos: [`L2-143a.jff`](../../automatas/lista2-afd/L2-143a.jff) · [`L2-143a.json`](../../automatas/lista2-afd/L2-143a.json) · [`L2-143a.xml`](../../automatas/lista2-afd/L2-143a.xml). Tipo según la definición: **AFD**, |Q| = 1, Σ = {a, b}, 2 transiciones.

**Diseño.** Un solo estado, inicial y de aceptación, con lazos a y b: L = Σ*.

| Estado | a | b |
|---|---|---|
| →*q0 | q0 | q0 |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | acepta | acepta | acepta |
| 2 | `ba` | acepta | acepta | acepta |
| 3 | `bbba` | acepta | acepta | acepta |
| 4 | `aababba` | acepta | acepta | acepta |
| 5 | `abbaaaaabab` | acepta | acepta | acepta |
| 6 | `#` (símbolo fuera de Σ) | rechaza | rechaza | rechaza |
| 7 | `a#` (símbolo fuera de Σ) | rechaza | rechaza | rechaza |
| 8 | `#bb` (símbolo fuera de Σ) | rechaza | rechaza | rechaza |

Nota sobre los casos: todas las cadenas sobre Σ pertenecen al lenguaje, así que las inválidas usan un símbolo fuera de Σ (#).

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: q0 — ✔
2. `ba`: q0 -b→ q0 -a→ q0 — ✔
3. `bbba`: q0 -b→ q0 -b→ q0 -b→ q0 -a→ q0 — ✔
4. `aababba`: q0 -a→ q0 -a→ q0 -b→ q0 -a→ q0 -b→ q0 -b→ q0 -a→ q0 — ✔
5. `abbaaaaabab`: q0 -a→ q0 -b→ q0 -b→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q0 -a→ q0 -b→ q0 -a→ q0 -b→ q0 — ✔
6. `#`: q0 -#→ (sin transición) — ✘
7. `a#`: q0 -a→ q0 -#→ (sin transición) — ✘
8. `#bb`: q0 -#→ (sin transición) — ✘

</details>

Simulación paso a paso en JFLAP con `ba`: [ver captura](../../evidencias/jflap/pasos/L2-143a.png).

<a id="problema-2-144"></a>

## Lista 2, problema 144

**Enunciado.** Autómata finito para: a) cadenas que comienzan con a; b) comienzan con a y terminan con b; c) contienen aaa; d) el conjunto de números enteros; e) el conjunto de números enteros con signo.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Cinco lenguajes de prefijo, sufijo, subcadena y formato numérico.

#### a) Comienzan con a — `L2-144a`

Archivos: [`L2-144a.jff`](../../automatas/lista2-afd/L2-144a.jff) · [`L2-144a.json`](../../automatas/lista2-afd/L2-144a.json) · [`L2-144a.xml`](../../automatas/lista2-afd/L2-144a.xml). Tipo según la definición: **AFD**, |Q| = 3, Σ = {a, b}, 6 transiciones.

**Diseño.** El primer símbolo decide: a lleva a un estado de aceptación absorbente y b al rechazo absorbente.

| Estado | a | b | Significado |
|---|---|---|---|
| →q0 | q1 | q2 | se ha leído el prefijo «» |
| *q1 | q1 | q1 | el prefijo «a» ya apareció |
| q2 | q2 | q2 | rechazo absorbente |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `a` | acepta | acepta | acepta |
| 2 | `ab` | acepta | acepta | acepta |
| 3 | `abbb` | acepta | acepta | acepta |
| 4 | `abbbaaa` | acepta | acepta | acepta |
| 5 | `ababbbbaabb` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `ba` | rechaza | rechaza | rechaza |
| 8 | `babb` | rechaza | rechaza | rechaza |
| 9 | `baaaaba` | rechaza | rechaza | rechaza |
| 10 | `babbabaaaba` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `a`: q0 -a→ q1 — ✔
2. `ab`: q0 -a→ q1 -b→ q1 — ✔
3. `abbb`: q0 -a→ q1 -b→ q1 -b→ q1 -b→ q1 — ✔
4. `abbbaaa`: q0 -a→ q1 -b→ q1 -b→ q1 -b→ q1 -a→ q1 -a→ q1 -a→ q1 — ✔
5. `ababbbbaabb`: q0 -a→ q1 -b→ q1 -a→ q1 -b→ q1 -b→ q1 -b→ q1 -b→ q1 -a→ q1 -a→ q1 -b→ q1 -b→ q1 — ✔
6. λ: q0 — ✘
7. `ba`: q0 -b→ q2 -a→ q2 — ✘
8. `babb`: q0 -b→ q2 -a→ q2 -b→ q2 -b→ q2 — ✘
9. `baaaaba`: q0 -b→ q2 -a→ q2 -a→ q2 -a→ q2 -a→ q2 -b→ q2 -a→ q2 — ✘
10. `babbabaaaba`: q0 -b→ q2 -a→ q2 -b→ q2 -b→ q2 -a→ q2 -b→ q2 -a→ q2 -a→ q2 -a→ q2 -b→ q2 -a→ q2 — ✘

</details>

Simulación paso a paso en JFLAP con `ab`: [ver captura](../../evidencias/jflap/pasos/L2-144a.png).

#### b) Comienzan con a y terminan con b — `L2-144b`

Archivos: [`L2-144b.jff`](../../automatas/lista2-afd/L2-144b.jff) · [`L2-144b.json`](../../automatas/lista2-afd/L2-144b.json) · [`L2-144b.xml`](../../automatas/lista2-afd/L2-144b.xml). Tipo según la definición: **AFD**, |Q| = 4, Σ = {a, b}, 8 transiciones.

**Diseño.** Tras una a inicial, el estado recuerda el último símbolo; acepta si es b. Una b inicial lleva al rechazo absorbente.

| Estado | a | b | Significado |
|---|---|---|---|
| →q0 | q1 | q2 | inicio |
| q1 | q1 | q3 | empezó con a; último símbolo a |
| q2 | q2 | q2 | rechazo absorbente |
| *q3 | q1 | q3 | empezó con a; último símbolo b |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `ab` | acepta | acepta | acepta |
| 2 | `aab` | acepta | acepta | acepta |
| 3 | `abaab` | acepta | acepta | acepta |
| 4 | `aabbbbb` | acepta | acepta | acepta |
| 5 | `ababaaabaab` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `aa` | rechaza | rechaza | rechaza |
| 8 | `baaa` | rechaza | rechaza | rechaza |
| 9 | `babbaab` | rechaza | rechaza | rechaza |
| 10 | `bbbaabaaaba` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `ab`: q0 -a→ q1 -b→ q3 — ✔
2. `aab`: q0 -a→ q1 -a→ q1 -b→ q3 — ✔
3. `abaab`: q0 -a→ q1 -b→ q3 -a→ q1 -a→ q1 -b→ q3 — ✔
4. `aabbbbb`: q0 -a→ q1 -a→ q1 -b→ q3 -b→ q3 -b→ q3 -b→ q3 -b→ q3 — ✔
5. `ababaaabaab`: q0 -a→ q1 -b→ q3 -a→ q1 -b→ q3 -a→ q1 -a→ q1 -a→ q1 -b→ q3 -a→ q1 -a→ q1 -b→ q3 — ✔
6. λ: q0 — ✘
7. `aa`: q0 -a→ q1 -a→ q1 — ✘
8. `baaa`: q0 -b→ q2 -a→ q2 -a→ q2 -a→ q2 — ✘
9. `babbaab`: q0 -b→ q2 -a→ q2 -b→ q2 -b→ q2 -a→ q2 -a→ q2 -b→ q2 — ✘
10. `bbbaabaaaba`: q0 -b→ q2 -b→ q2 -b→ q2 -a→ q2 -a→ q2 -b→ q2 -a→ q2 -a→ q2 -a→ q2 -b→ q2 -a→ q2 — ✘

</details>

Simulación paso a paso en JFLAP con `ab`: [ver captura](../../evidencias/jflap/pasos/L2-144b.png).

#### c) Contienen aaa — `L2-144c`

Archivos: [`L2-144c.jff`](../../automatas/lista2-afd/L2-144c.jff) · [`L2-144c.json`](../../automatas/lista2-afd/L2-144c.json) · [`L2-144c.xml`](../../automatas/lista2-afd/L2-144c.xml). Tipo según la definición: **AFD**, |Q| = 4, Σ = {a, b}, 8 transiciones.

**Diseño.** Búsqueda de aaa: qᵢ = racha actual de a (i < 3); q3 absorbente de aceptación.

| Estado | a | b | Significado |
|---|---|---|---|
| →q0 | q1 | q0 | ningún avance en el patrón |
| q1 | q2 | q0 | los últimos símbolos coinciden con «a» |
| q2 | q3 | q0 | los últimos símbolos coinciden con «aa» |
| *q3 | q3 | q3 | «aaa» ya apareció |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `aaa` | acepta | acepta | acepta |
| 2 | `abaaa` | acepta | acepta | acepta |
| 3 | `bbaaa` | acepta | acepta | acepta |
| 4 | `babbaaa` | acepta | acepta | acepta |
| 5 | `aabaabaaaaa` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `ba` | rechaza | rechaza | rechaza |
| 8 | `baab` | rechaza | rechaza | rechaza |
| 9 | `aababba` | rechaza | rechaza | rechaza |
| 10 | `abaabbbbbba` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `aaa`: q0 -a→ q1 -a→ q2 -a→ q3 — ✔
2. `abaaa`: q0 -a→ q1 -b→ q0 -a→ q1 -a→ q2 -a→ q3 — ✔
3. `bbaaa`: q0 -b→ q0 -b→ q0 -a→ q1 -a→ q2 -a→ q3 — ✔
4. `babbaaa`: q0 -b→ q0 -a→ q1 -b→ q0 -b→ q0 -a→ q1 -a→ q2 -a→ q3 — ✔
5. `aabaabaaaaa`: q0 -a→ q1 -a→ q2 -b→ q0 -a→ q1 -a→ q2 -b→ q0 -a→ q1 -a→ q2 -a→ q3 -a→ q3 -a→ q3 — ✔
6. λ: q0 — ✘
7. `ba`: q0 -b→ q0 -a→ q1 — ✘
8. `baab`: q0 -b→ q0 -a→ q1 -a→ q2 -b→ q0 — ✘
9. `aababba`: q0 -a→ q1 -a→ q2 -b→ q0 -a→ q1 -b→ q0 -b→ q0 -a→ q1 — ✘
10. `abaabbbbbba`: q0 -a→ q1 -b→ q0 -a→ q1 -a→ q2 -b→ q0 -b→ q0 -b→ q0 -b→ q0 -b→ q0 -b→ q0 -a→ q1 — ✘

</details>

Simulación paso a paso en JFLAP con `aaa`: [ver captura](../../evidencias/jflap/pasos/L2-144c.png).

#### d) Números enteros (Σ = {0,…,9}) — `L2-144d`

Archivos: [`L2-144d.jff`](../../automatas/lista2-afd/L2-144d.jff) · [`L2-144d.json`](../../automatas/lista2-afd/L2-144d.json) · [`L2-144d.xml`](../../automatas/lista2-afd/L2-144d.xml). Tipo según la definición: **AFD**, |Q| = 4, Σ = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 40 transiciones.

**Diseño.** Se toma la representación decimal sin ceros a la izquierda: 0, o un dígito de 1 a 9 seguido de cualquier cantidad de dígitos. q1 = se leyó «0» (otro dígito lo invalida); q2 = número que empieza con 1-9 (absorbe dígitos). λ no es un número.

| Estado | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | Significado |
|---|---|---|---|---|---|---|---|---|---|---|---|
| →q0 | q1 | q2 | q2 | q2 | q2 | q2 | q2 | q2 | q2 | q2 | nada leído |
| *q1 | q3 | q3 | q3 | q3 | q3 | q3 | q3 | q3 | q3 | q3 | se leyó el número 0 |
| *q2 | q2 | q2 | q2 | q2 | q2 | q2 | q2 | q2 | q2 | q2 | número sin ceros a la izquierda |
| q3 | q3 | q3 | q3 | q3 | q3 | q3 | q3 | q3 | q3 | q3 | rechazo absorbente |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `0` | acepta | acepta | acepta |
| 2 | `59` | acepta | acepta | — |
| 3 | `9038` | acepta | acepta | — |
| 4 | `5746602` | acepta | acepta | — |
| 5 | `89566197849` | acepta | acepta | — |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `09` | rechaza | rechaza | rechaza |
| 8 | `0268` | rechaza | rechaza | rechaza |
| 9 | `0968296` | rechaza | rechaza | rechaza |
| 10 | `09883346367` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `0`: q0 -0→ q1 — ✔
2. `59`: q0 -5→ q2 -9→ q2 — ✔
3. `9038`: q0 -9→ q2 -0→ q2 -3→ q2 -8→ q2 — ✔
4. `5746602`: q0 -5→ q2 -7→ q2 -4→ q2 -6→ q2 -6→ q2 -0→ q2 -2→ q2 — ✔
5. `89566197849`: q0 -8→ q2 -9→ q2 -5→ q2 -6→ q2 -6→ q2 -1→ q2 -9→ q2 -7→ q2 -8→ q2 -4→ q2 -9→ q2 — ✔
6. λ: q0 — ✘
7. `09`: q0 -0→ q1 -9→ q3 — ✘
8. `0268`: q0 -0→ q1 -2→ q3 -6→ q3 -8→ q3 — ✘
9. `0968296`: q0 -0→ q1 -9→ q3 -6→ q3 -8→ q3 -2→ q3 -9→ q3 -6→ q3 — ✘
10. `09883346367`: q0 -0→ q1 -9→ q3 -8→ q3 -8→ q3 -3→ q3 -3→ q3 -4→ q3 -6→ q3 -3→ q3 -6→ q3 -7→ q3 — ✘

</details>

Simulación paso a paso en JFLAP con `5990`: [ver captura](../../evidencias/jflap/pasos/L2-144d.png).

#### e) Enteros con signo (Σ = {0,…,9,+,−}) — `L2-144e`

Archivos: [`L2-144e.jff`](../../automatas/lista2-afd/L2-144e.jff) · [`L2-144e.json`](../../automatas/lista2-afd/L2-144e.json) · [`L2-144e.xml`](../../automatas/lista2-afd/L2-144e.xml). Tipo según la definición: **AFD**, |Q| = 5, Σ = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, +, -}, 60 transiciones.

**Diseño.** Como d), con un signo opcional al principio: q1 = se leyó el signo y falta al menos un dígito. Un signo en otra posición lleva al rechazo absorbente.

| Estado | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | + | - | Significado |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| →q0 | q1 | q2 | q2 | q2 | q2 | q2 | q2 | q2 | q2 | q2 | q3 | q3 | nada leído |
| *q1 | q4 | q4 | q4 | q4 | q4 | q4 | q4 | q4 | q4 | q4 | q4 | q4 | el número 0 (con o sin signo) |
| *q2 | q2 | q2 | q2 | q2 | q2 | q2 | q2 | q2 | q2 | q2 | q4 | q4 | número sin ceros a la izquierda |
| q3 | q1 | q2 | q2 | q2 | q2 | q2 | q2 | q2 | q2 | q2 | q4 | q4 | se leyó el signo |
| q4 | q4 | q4 | q4 | q4 | q4 | q4 | q4 | q4 | q4 | q4 | q4 | q4 | rechazo absorbente |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `0` | acepta | acepta | — |
| 2 | `93` | acepta | acepta | acepta |
| 3 | `3303` | acepta | acepta | acepta |
| 4 | `7654479` | acepta | acepta | acepta |
| 5 | `64910737178` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `+6+` | rechaza | rechaza | rechaza |
| 8 | `+501+` | rechaza | rechaza | rechaza |
| 9 | `+240244+` | rechaza | rechaza | rechaza |
| 10 | `299-3+12372` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `0`: q0 -0→ q1 — ✔
2. `93`: q0 -9→ q2 -3→ q2 — ✔
3. `3303`: q0 -3→ q2 -3→ q2 -0→ q2 -3→ q2 — ✔
4. `7654479`: q0 -7→ q2 -6→ q2 -5→ q2 -4→ q2 -4→ q2 -7→ q2 -9→ q2 — ✔
5. `64910737178`: q0 -6→ q2 -4→ q2 -9→ q2 -1→ q2 -0→ q2 -7→ q2 -3→ q2 -7→ q2 -1→ q2 -7→ q2 -8→ q2 — ✔
6. λ: q0 — ✘
7. `+6+`: q0 -+→ q3 -6→ q2 -+→ q4 — ✘
8. `+501+`: q0 -+→ q3 -5→ q2 -0→ q2 -1→ q2 -+→ q4 — ✘
9. `+240244+`: q0 -+→ q3 -2→ q2 -4→ q2 -0→ q2 -2→ q2 -4→ q2 -4→ q2 -+→ q4 — ✘
10. `299-3+12372`: q0 -2→ q2 -9→ q2 -9→ q2 --→ q4 -3→ q4 -+→ q4 -1→ q4 -2→ q4 -3→ q4 -7→ q4 -2→ q4 — ✘

</details>

Simulación paso a paso en JFLAP con `93`: [ver captura](../../evidencias/jflap/pasos/L2-144e.png).

<a id="problema-2-145"></a>

## Lista 2, problema 145

**Enunciado.** Número binario leído de derecha a izquierda que es múltiplo de 5.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### Número binario leído de derecha a izquierda que es múltiplo de 5. — `L2-145`

Archivos: [`L2-145.jff`](../../automatas/lista2-afd/L2-145.jff) · [`L2-145.json`](../../automatas/lista2-afd/L2-145.json) · [`L2-145.xml`](../../automatas/lista2-afd/L2-145.xml). Tipo según la definición: **AFD**, |Q| = 5, Σ = {0, 1}, 10 transiciones.

**Diseño.** Un bit nuevo pesa 2ⁱ mod 5, y 2 tiene orden 4 módulo 5, de modo que basta guardar (residuo, posición mod 4). Tras minimizar quedan 5 estados. λ representa el 0 y se acepta.

| Estado | 0 | 1 |
|---|---|---|
| q3 | q4 | q2 |
| q2 | q3 | q0 |
| q4 | q1 | q4 |
| q1 | q2 | q3 |
| →*q0 | q0 | q1 |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | acepta | acepta | acepta |
| 2 | `00` | acepta | acepta | acepta |
| 3 | `10011` | acepta | acepta | acepta |
| 4 | `0011110` | acepta | acepta | acepta |
| 5 | `1000101100001` | acepta | acepta | acepta |
| 6 | `1` | rechaza | rechaza | rechaza |
| 7 | `001` | rechaza | rechaza | rechaza |
| 8 | `1100` | rechaza | rechaza | rechaza |
| 9 | `1010011` | rechaza | rechaza | rechaza |
| 10 | `01110011111` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: q0 — ✔
2. `00`: q0 -0→ q0 -0→ q0 — ✔
3. `10011`: q0 -1→ q1 -0→ q2 -0→ q3 -1→ q2 -1→ q0 — ✔
4. `0011110`: q0 -0→ q0 -0→ q0 -1→ q1 -1→ q3 -1→ q2 -1→ q0 -0→ q0 — ✔
5. `1000101100001`: q0 -1→ q1 -0→ q2 -0→ q3 -0→ q4 -1→ q4 -0→ q1 -1→ q3 -1→ q2 -0→ q3 -0→ q4 -0→ q1 -0→ q2 -1→ q0 — ✔
6. `1`: q0 -1→ q1 — ✘
7. `001`: q0 -0→ q0 -0→ q0 -1→ q1 — ✘
8. `1100`: q0 -1→ q1 -1→ q3 -0→ q4 -0→ q1 — ✘
9. `1010011`: q0 -1→ q1 -0→ q2 -1→ q0 -0→ q0 -0→ q0 -1→ q1 -1→ q3 — ✘
10. `01110011111`: q0 -0→ q0 -1→ q1 -1→ q3 -1→ q2 -0→ q3 -0→ q4 -1→ q4 -1→ q4 -1→ q4 -1→ q4 -1→ q4 — ✘

</details>

Simulación paso a paso en JFLAP con `00`: [ver captura](../../evidencias/jflap/pasos/L2-145.png).

<a id="problema-2-146"></a>

## Lista 2, problema 146

**Enunciado.** AFD que lee un número binario de izquierda a derecha e identifica los múltiplos de 5.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. El estado guarda el residuo módulo 5 del valor leído.

#### AFD — `L2-146`

Archivos: [`L2-146.jff`](../../automatas/lista2-afd/L2-146.jff) · [`L2-146.json`](../../automatas/lista2-afd/L2-146.json) · [`L2-146.xml`](../../automatas/lista2-afd/L2-146.xml). Tipo según la definición: **AFD**, |Q| = 5, Σ = {0, 1}, 10 transiciones.

**Diseño.** Al leer el bit b el valor pasa de v a 2v + b, así que basta el residuo: r' = (2r + b) mod 5. q0 (residuo 0) es inicial y de aceptación; λ representa el 0, igual que en el problema 145 de la Práctica 1.

| Estado | 0 | 1 | Significado |
|---|---|---|---|
| →*q0 | q0 | q1 | valor ≡ 0 (mód 5) |
| q1 | q2 | q3 | valor ≡ 1 (mód 5) |
| q2 | q4 | q0 | valor ≡ 2 (mód 5) |
| q3 | q1 | q2 | valor ≡ 3 (mód 5) |
| q4 | q3 | q4 | valor ≡ 4 (mód 5) |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | acepta | acepta | acepta |
| 2 | `0101` | acepta | acepta | acepta |
| 3 | `1111` | acepta | acepta | acepta |
| 4 | `11000011` | acepta | acepta | acepta |
| 5 | `00010010001` | acepta | acepta | acepta |
| 6 | `1` | rechaza | rechaza | rechaza |
| 7 | `001` | rechaza | rechaza | rechaza |
| 8 | `01011` | rechaza | rechaza | rechaza |
| 9 | `0001000` | rechaza | rechaza | rechaza |
| 10 | `111100000001` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: q0 — ✔
2. `0101`: q0 -0→ q0 -1→ q1 -0→ q2 -1→ q0 — ✔
3. `1111`: q0 -1→ q1 -1→ q3 -1→ q2 -1→ q0 — ✔
4. `11000011`: q0 -1→ q1 -1→ q3 -0→ q1 -0→ q2 -0→ q4 -0→ q3 -1→ q2 -1→ q0 — ✔
5. `00010010001`: q0 -0→ q0 -0→ q0 -0→ q0 -1→ q1 -0→ q2 -0→ q4 -1→ q4 -0→ q3 -0→ q1 -0→ q2 -1→ q0 — ✔
6. `1`: q0 -1→ q1 — ✘
7. `001`: q0 -0→ q0 -0→ q0 -1→ q1 — ✘
8. `01011`: q0 -0→ q0 -1→ q1 -0→ q2 -1→ q0 -1→ q1 — ✘
9. `0001000`: q0 -0→ q0 -0→ q0 -0→ q0 -1→ q1 -0→ q2 -0→ q4 -0→ q3 — ✘
10. `111100000001`: q0 -1→ q1 -1→ q3 -1→ q2 -1→ q0 -0→ q0 -0→ q0 -0→ q0 -0→ q0 -0→ q0 -0→ q0 -0→ q0 -1→ q1 — ✘

</details>

Simulación paso a paso en JFLAP con `0101`: [ver captura](../../evidencias/jflap/pasos/L2-146.png).

<a id="problema-2-147"></a>

## Lista 2, problema 147

**Enunciado.** Número binario leído de izquierda a derecha que es múltiplo de 6.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### Número binario leído de izquierda a derecha que es múltiplo de 6. — `L2-147`

Archivos: [`L2-147.jff`](../../automatas/lista2-afd/L2-147.jff) · [`L2-147.json`](../../automatas/lista2-afd/L2-147.json) · [`L2-147.xml`](../../automatas/lista2-afd/L2-147.xml). Tipo según la definición: **AFD**, |Q| = 4, Σ = {0, 1}, 8 transiciones.

**Diseño.** El estado guarda el residuo del valor leído: r' = (2r + b) mod 6. De los 6 residuos quedan 4 estados distinguibles.

| Estado | 0 | 1 |
|---|---|---|
| q1 | q2 | q3 |
| q2 | q1 | q2 |
| q3 | q0 | q1 |
| →*q0 | q0 | q1 |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | acepta | acepta | acepta |
| 2 | `10010` | acepta | acepta | acepta |
| 3 | `011110` | acepta | acepta | acepta |
| 4 | `0111011010` | acepta | acepta | acepta |
| 5 | `1010001010010` | acepta | acepta | acepta |
| 6 | `1` | rechaza | rechaza | rechaza |
| 7 | `11` | rechaza | rechaza | rechaza |
| 8 | `1111` | rechaza | rechaza | rechaza |
| 9 | `1011100` | rechaza | rechaza | rechaza |
| 10 | `001101010101` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: q0 — ✔
2. `10010`: q0 -1→ q1 -0→ q2 -0→ q1 -1→ q3 -0→ q0 — ✔
3. `011110`: q0 -0→ q0 -1→ q1 -1→ q3 -1→ q1 -1→ q3 -0→ q0 — ✔
4. `0111011010`: q0 -0→ q0 -1→ q1 -1→ q3 -1→ q1 -0→ q2 -1→ q2 -1→ q2 -0→ q1 -1→ q3 -0→ q0 — ✔
5. `1010001010010`: q0 -1→ q1 -0→ q2 -1→ q2 -0→ q1 -0→ q2 -0→ q1 -1→ q3 -0→ q0 -1→ q1 -0→ q2 -0→ q1 -1→ q3 -0→ q0 — ✔
6. `1`: q0 -1→ q1 — ✘
7. `11`: q0 -1→ q1 -1→ q3 — ✘
8. `1111`: q0 -1→ q1 -1→ q3 -1→ q1 -1→ q3 — ✘
9. `1011100`: q0 -1→ q1 -0→ q2 -1→ q2 -1→ q2 -1→ q2 -0→ q1 -0→ q2 — ✘
10. `001101010101`: q0 -0→ q0 -0→ q0 -1→ q1 -1→ q3 -0→ q0 -1→ q1 -0→ q2 -1→ q2 -0→ q1 -1→ q3 -0→ q0 -1→ q1 — ✘

</details>

Simulación paso a paso en JFLAP con `10010`: [ver captura](../../evidencias/jflap/pasos/L2-147.png).

<a id="problema-2-148"></a>

## Lista 2, problema 148

**Enunciado.** Progreso de un alumno con Σ = {P,N,A,S}: máximo dos convocatorias por año; termina al aprobar.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### Progreso de un alumno con Σ = {P,N,A,S}: máximo dos convocatorias por año; termina al aprobar. — `L2-148`

Archivos: [`L2-148.jff`](../../automatas/lista2-afd/L2-148.jff) · [`L2-148.json`](../../automatas/lista2-afd/L2-148.json) · [`L2-148.xml`](../../automatas/lista2-afd/L2-148.xml). Tipo según la definición: **AFD**, |Q| = 6, Σ = {A, N, P, S}, 24 transiciones.

**Diseño.** q0: inicio de año, 0 presentaciones. q1: se presentó y espera resultado. q4: ya aplazó una vez. q5: segunda presentación. q3: aprobó (aceptación absorbente). q2: secuencia sin sentido (rechazo). N no consume oportunidad; dos S reinician el año.

| Estado | A | N | P | S |
|---|---|---|---|---|
| →q0 | q2 | q0 | q1 | q2 |
| q1 | q3 | q2 | q2 | q4 |
| q4 | q2 | q4 | q5 | q2 |
| q5 | q3 | q2 | q2 | q0 |
| *q3 | q3 | q3 | q3 | q3 |
| q2 | q2 | q2 | q2 | q2 |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `PA` | acepta | acepta | acepta |
| 2 | `NNPA` | acepta | acepta | acepta |
| 3 | `NPSPA` | acepta | acepta | acepta |
| 4 | `NNNNPAA` | acepta | acepta | acepta |
| 5 | `NPSNPANAPSA` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `SP` | rechaza | rechaza | rechaza |
| 8 | `PPSA` | rechaza | rechaza | rechaza |
| 9 | `PPSNPNN` | rechaza | rechaza | rechaza |
| 10 | `ANANNNAPSSP` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `PA`: q0 -P→ q1 -A→ q3 — ✔
2. `NNPA`: q0 -N→ q0 -N→ q0 -P→ q1 -A→ q3 — ✔
3. `NPSPA`: q0 -N→ q0 -P→ q1 -S→ q4 -P→ q5 -A→ q3 — ✔
4. `NNNNPAA`: q0 -N→ q0 -N→ q0 -N→ q0 -N→ q0 -P→ q1 -A→ q3 -A→ q3 — ✔
5. `NPSNPANAPSA`: q0 -N→ q0 -P→ q1 -S→ q4 -N→ q4 -P→ q5 -A→ q3 -N→ q3 -A→ q3 -P→ q3 -S→ q3 -A→ q3 — ✔
6. λ: q0 — ✘
7. `SP`: q0 -S→ q2 -P→ q2 — ✘
8. `PPSA`: q0 -P→ q1 -P→ q2 -S→ q2 -A→ q2 — ✘
9. `PPSNPNN`: q0 -P→ q1 -P→ q2 -S→ q2 -N→ q2 -P→ q2 -N→ q2 -N→ q2 — ✘
10. `ANANNNAPSSP`: q0 -A→ q2 -N→ q2 -A→ q2 -N→ q2 -N→ q2 -N→ q2 -A→ q2 -P→ q2 -S→ q2 -S→ q2 -P→ q2 — ✘

</details>

Simulación paso a paso en JFLAP con `PA`: [ver captura](../../evidencias/jflap/pasos/L2-148.png).

<a id="problema-2-149"></a>

## Lista 2, problema 149

**Enunciado.** Autómata dado por tabla; hallar Q, Σ, A₀, F y valores de δ̂.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

**Valores pedidos** (con los nombres de estado de la tabla):

- δ̂({B}, 0) = {A}: {B} -0→ {A}
- δ̂({C}, 1) = {A}: {C} -1→ {A}
- δ̂({A}, 1101) = {C}: {A} -1→ {C} -1→ {A} -0→ {B} -1→ {C}
- δ̂({A}, 01001) = {A}: {A} -0→ {B} -1→ {C} -0→ {C} -0→ {C} -1→ {A}

#### Autómata dado por tabla; hallar Q, Σ, A₀, F y valores de δ̂. — `L2-149`

Archivos: [`L2-149.jff`](../../automatas/lista2-afd/L2-149.jff) · [`L2-149.json`](../../automatas/lista2-afd/L2-149.json) · [`L2-149.xml`](../../automatas/lista2-afd/L2-149.xml). Tipo según la definición: **AFD**, |Q| = 3, Σ = {0, 1}, 6 transiciones.

**Diseño.** Transcripción de la tabla: q0 = A, q1 = B, q2 = C.

| Estado | 0 | 1 |
|---|---|---|
| →q0 | q1 | q2 |
| q1 | q0 | q2 |
| *q2 | q2 | q0 |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `1` | acepta | acepta | acepta |
| 2 | `111` | acepta | acepta | acepta |
| 3 | `1110` | acepta | acepta | acepta |
| 4 | `1000101` | acepta | acepta | acepta |
| 5 | `00010100001` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `11` | rechaza | rechaza | rechaza |
| 8 | `10001` | rechaza | rechaza | rechaza |
| 9 | `0110000` | rechaza | rechaza | rechaza |
| 10 | `110101011011` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `1`: q0 -1→ q2 — ✔
2. `111`: q0 -1→ q2 -1→ q0 -1→ q2 — ✔
3. `1110`: q0 -1→ q2 -1→ q0 -1→ q2 -0→ q2 — ✔
4. `1000101`: q0 -1→ q2 -0→ q2 -0→ q2 -0→ q2 -1→ q0 -0→ q1 -1→ q2 — ✔
5. `00010100001`: q0 -0→ q1 -0→ q0 -0→ q1 -1→ q2 -0→ q2 -1→ q0 -0→ q1 -0→ q0 -0→ q1 -0→ q0 -1→ q2 — ✔
6. λ: q0 — ✘
7. `11`: q0 -1→ q2 -1→ q0 — ✘
8. `10001`: q0 -1→ q2 -0→ q2 -0→ q2 -0→ q2 -1→ q0 — ✘
9. `0110000`: q0 -0→ q1 -1→ q2 -1→ q0 -0→ q1 -0→ q0 -0→ q1 -0→ q0 — ✘
10. `110101011011`: q0 -1→ q2 -1→ q0 -0→ q1 -1→ q2 -0→ q2 -1→ q0 -0→ q1 -1→ q2 -1→ q0 -0→ q1 -1→ q2 -1→ q0 — ✘

</details>

Simulación paso a paso en JFLAP con `111`: [ver captura](../../evidencias/jflap/pasos/L2-149.png).

<a id="problema-2-150"></a>

## Lista 2, problema 150

**Enunciado.** Autómata dado por tabla con Σ = {0,1,a}; hallar Q, Σ, A₀, F y valores de δ̂.

**Clasificación: AFD.** El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

**Valores pedidos** (con los nombres de estado de la tabla):

- δ̂({B}, 10a11) = {C}: {B} -1→ {C} -0→ {A} -a→ {D} -1→ {B} -1→ {C}
- δ̂({B}, aa1100) = {B}: {B} -a→ {C} -a→ {D} -1→ {B} -1→ {C} -0→ {A} -0→ {B}
- δ̂({A}, a01a01) = {C}: {A} -a→ {D} -0→ {B} -1→ {C} -a→ {D} -0→ {B} -1→ {C}
- δ̂({C}, a11a00) = {B}: {C} -a→ {D} -1→ {B} -1→ {C} -a→ {D} -0→ {B} -0→ {B}

#### Autómata dado por tabla con Σ = {0,1,a}; hallar Q, Σ, A₀, F y valores de δ̂. — `L2-150`

Archivos: [`L2-150.jff`](../../automatas/lista2-afd/L2-150.jff) · [`L2-150.json`](../../automatas/lista2-afd/L2-150.json) · [`L2-150.xml`](../../automatas/lista2-afd/L2-150.xml). Tipo según la definición: **AFD**, |Q| = 4, Σ = {0, 1, a}, 12 transiciones.

**Diseño.** Transcripción de la tabla: q0 = A, q1 = B, q2 = C, q3 = D.

| Estado | 0 | 1 | a |
|---|---|---|---|
| →q0 | q1 | q2 | q3 |
| *q1 | q1 | q2 | q2 |
| *q2 | q0 | q0 | q3 |
| *q3 | q1 | q1 | q1 |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `0` | acepta | acepta | — |
| 2 | `100` | acepta | acepta | — |
| 3 | `aa1a` | acepta | acepta | acepta |
| 4 | `a001aa0` | acepta | acepta | acepta |
| 5 | `aa00110a001` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `a010` | rechaza | rechaza | rechaza |
| 8 | `000a0` | rechaza | rechaza | rechaza |
| 9 | `0a10a0010` | rechaza | rechaza | rechaza |
| 10 | `01101a0a11a010` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `0`: q0 -0→ q1 — ✔
2. `100`: q0 -1→ q2 -0→ q0 -0→ q1 — ✔
3. `aa1a`: q0 -a→ q3 -a→ q1 -1→ q2 -a→ q3 — ✔
4. `a001aa0`: q0 -a→ q3 -0→ q1 -0→ q1 -1→ q2 -a→ q3 -a→ q1 -0→ q1 — ✔
5. `aa00110a001`: q0 -a→ q3 -a→ q1 -0→ q1 -0→ q1 -1→ q2 -1→ q0 -0→ q1 -a→ q2 -0→ q0 -0→ q1 -1→ q2 — ✔
6. λ: q0 — ✘
7. `a010`: q0 -a→ q3 -0→ q1 -1→ q2 -0→ q0 — ✘
8. `000a0`: q0 -0→ q1 -0→ q1 -0→ q1 -a→ q2 -0→ q0 — ✘
9. `0a10a0010`: q0 -0→ q1 -a→ q2 -1→ q0 -0→ q1 -a→ q2 -0→ q0 -0→ q1 -1→ q2 -0→ q0 — ✘
10. `01101a0a11a010`: q0 -0→ q1 -1→ q2 -1→ q0 -0→ q1 -1→ q2 -a→ q3 -0→ q1 -a→ q2 -1→ q0 -1→ q2 -a→ q3 -0→ q1 -1→ q2 -0→ q0 — ✘

</details>

Simulación paso a paso en JFLAP con `101`: [ver captura](../../evidencias/jflap/pasos/L2-150.png).

