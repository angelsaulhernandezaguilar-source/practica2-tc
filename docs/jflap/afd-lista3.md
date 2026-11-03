# Ejercicio 2 — AFD — Lista 3

[← Ejercicio 2](../02-jflap.md) · [Índice](../../README.md)

Cada autómata indica su clasificación, el diseño, la tabla de transiciones, cinco cadenas válidas y cinco inválidas con el resultado esperado (oráculo escrito a partir del enunciado), el del simulador de este proyecto y el del motor de JFLAP 7.1, el recorrido de cada cadena (en los no deterministas, el conjunto de estados activos y el árbol de caminos) y la captura de la simulación paso a paso en JFLAP.

<a id="problema-3-151"></a>

## Lista 3, problema 151

**Enunciado.** Diagrama del autómata de la tabla 151.

**Clasificación: AFD.** AFD dado por tabla (δ total) que se simplifica; la sección AFD es la que corresponde. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### Diagrama del autómata de la tabla 151. — `L3-151-original`

Archivos: [`L3-151-original.jff`](../../automatas/lista2-afd/L3-151-original.jff) · [`L3-151-original.json`](../../automatas/lista2-afd/L3-151-original.json) · [`L3-151-original.xml`](../../automatas/lista2-afd/L3-151-original.xml). Tipo según la definición: **AFD**, |Q| = 10, Σ = {0, 1}, 20 transiciones.

**Diseño.** Transcripción de la tabla. Los estados inaccesibles se hallan con un recorrido en anchura desde el inicial. No hay inaccesibles.

| Estado | 0 | 1 |
|---|---|---|
| →A | C | E |
| B | F | E |
| *C | A | G |
| D | C | E |
| *E | I | B |
| *F | D | H |
| G | F | I |
| H | C | J |
| I | J | E |
| J | I | E |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `1` | acepta | acepta | acepta |
| 2 | `111` | acepta | acepta | acepta |
| 3 | `10111` | acepta | acepta | acepta |
| 4 | `11100111` | acepta | acepta | acepta |
| 5 | `010100000111` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `10` | rechaza | rechaza | rechaza |
| 8 | `01111` | rechaza | rechaza | — |
| 9 | `0001111` | rechaza | rechaza | rechaza |
| 10 | `001010001100` | rechaza | rechaza | — |

<details><summary>Recorrido completo de cada cadena</summary>

1. `1`: A -1→ E — ✔
2. `111`: A -1→ E -1→ B -1→ E — ✔
3. `10111`: A -1→ E -0→ I -1→ E -1→ B -1→ E — ✔
4. `11100111`: A -1→ E -1→ B -1→ E -0→ I -0→ J -1→ E -1→ B -1→ E — ✔
5. `010100000111`: A -0→ C -1→ G -0→ F -1→ H -0→ C -0→ A -0→ C -0→ A -0→ C -1→ G -1→ I -1→ E — ✔
6. λ: A — ✘
7. `10`: A -1→ E -0→ I — ✘
8. `01111`: A -0→ C -1→ G -1→ I -1→ E -1→ B — ✘
9. `0001111`: A -0→ C -0→ A -0→ C -1→ G -1→ I -1→ E -1→ B — ✘
10. `001010001100`: A -0→ C -0→ A -1→ E -0→ I -1→ E -0→ I -0→ J -0→ I -1→ E -1→ B -0→ F -0→ D — ✘

</details>

Simulación paso a paso en JFLAP con `111`: [ver captura](../../evidencias/jflap/pasos/L3-151-original.png).

#### Autómata 151 simplificado. — `L3-151-simplificado`

Archivos: [`L3-151-simplificado.jff`](../../automatas/lista2-afd/L3-151-simplificado.jff) · [`L3-151-simplificado.json`](../../automatas/lista2-afd/L3-151-simplificado.json) · [`L3-151-simplificado.xml`](../../automatas/lista2-afd/L3-151-simplificado.xml). Tipo según la definición: **AFD**, |Q| = 5, Σ = {0, 1}, 10 transiciones.

**Diseño.** Partición: se inicia con {no finales, finales} y se separan los estados que van a bloques distintos con algún símbolo, hasta estabilizar; cada estado del resultado representa un bloque de estados equivalentes.

| Estado | 0 | 1 |
|---|---|---|
| →ABD | CF | E |
| *CF | ABD | GH |
| *E | IJ | ABD |
| GH | CF | IJ |
| IJ | IJ | E |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `1` | acepta | acepta | acepta |
| 2 | `010` | acepta | acepta | acepta |
| 3 | `10111` | acepta | acepta | acepta |
| 4 | `10101001` | acepta | acepta | acepta |
| 5 | `101100101001` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `01` | rechaza | rechaza | rechaza |
| 8 | `01111` | rechaza | rechaza | rechaza |
| 9 | `01001111` | rechaza | rechaza | rechaza |
| 10 | `01011001110` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `1`: ABD -1→ E — ✔
2. `010`: ABD -0→ CF -1→ GH -0→ CF — ✔
3. `10111`: ABD -1→ E -0→ IJ -1→ E -1→ ABD -1→ E — ✔
4. `10101001`: ABD -1→ E -0→ IJ -1→ E -0→ IJ -1→ E -0→ IJ -0→ IJ -1→ E — ✔
5. `101100101001`: ABD -1→ E -0→ IJ -1→ E -1→ ABD -0→ CF -0→ ABD -1→ E -0→ IJ -1→ E -0→ IJ -0→ IJ -1→ E — ✔
6. λ: ABD — ✘
7. `01`: ABD -0→ CF -1→ GH — ✘
8. `01111`: ABD -0→ CF -1→ GH -1→ IJ -1→ E -1→ ABD — ✘
9. `01001111`: ABD -0→ CF -1→ GH -0→ CF -0→ ABD -1→ E -1→ ABD -1→ E -1→ ABD — ✘
10. `01011001110`: ABD -0→ CF -1→ GH -0→ CF -1→ GH -1→ IJ -0→ IJ -0→ IJ -1→ E -1→ ABD -1→ E -0→ IJ — ✘

</details>

Simulación paso a paso en JFLAP con `010`: [ver captura](../../evidencias/jflap/pasos/L3-151-simplificado.png).

<a id="problema-3-152"></a>

## Lista 3, problema 152

**Enunciado.** Diagrama del autómata de la tabla 152.

**Clasificación: AFD.** AFD dado por tabla (δ total) que se simplifica; la sección AFD es la que corresponde. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### Diagrama del autómata de la tabla 152. — `L3-152-original`

Archivos: [`L3-152-original.jff`](../../automatas/lista2-afd/L3-152-original.jff) · [`L3-152-original.json`](../../automatas/lista2-afd/L3-152-original.json) · [`L3-152-original.xml`](../../automatas/lista2-afd/L3-152-original.xml). Tipo según la definición: **AFD**, |Q| = 6, Σ = {0, 1, 2}, 18 transiciones.

**Diseño.** Transcripción de la tabla. Los estados inaccesibles se hallan con un recorrido en anchura desde el inicial. No hay inaccesibles.

| Estado | 0 | 1 | 2 |
|---|---|---|---|
| →A | C | E | B |
| B | D | E | B |
| C | A | D | F |
| *D | F | B | C |
| *E | F | B | A |
| *F | D | B | C |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `1` | acepta | acepta | acepta |
| 2 | `001` | acepta | acepta | acepta |
| 3 | `11110` | acepta | acepta | acepta |
| 4 | `21121021` | acepta | acepta | acepta |
| 5 | `020100100201` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `11` | rechaza | rechaza | rechaza |
| 8 | `01222` | rechaza | rechaza | rechaza |
| 9 | `01222202` | rechaza | rechaza | rechaza |
| 10 | `012021202222` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `1`: A -1→ E — ✔
2. `001`: A -0→ C -0→ A -1→ E — ✔
3. `11110`: A -1→ E -1→ B -1→ E -1→ B -0→ D — ✔
4. `21121021`: A -2→ B -1→ E -1→ B -2→ B -1→ E -0→ F -2→ C -1→ D — ✔
5. `020100100201`: A -0→ C -2→ F -0→ D -1→ B -0→ D -0→ F -1→ B -0→ D -0→ F -2→ C -0→ A -1→ E — ✔
6. λ: A — ✘
7. `11`: A -1→ E -1→ B — ✘
8. `01222`: A -0→ C -1→ D -2→ C -2→ F -2→ C — ✘
9. `01222202`: A -0→ C -1→ D -2→ C -2→ F -2→ C -2→ F -0→ D -2→ C — ✘
10. `012021202222`: A -0→ C -1→ D -2→ C -0→ A -2→ B -1→ E -2→ A -0→ C -2→ F -2→ C -2→ F -2→ C — ✘

</details>

Simulación paso a paso en JFLAP con `001`: [ver captura](../../evidencias/jflap/pasos/L3-152-original.png).

#### Autómata 152 simplificado. — `L3-152-simplificado`

Archivos: [`L3-152-simplificado.jff`](../../automatas/lista2-afd/L3-152-simplificado.jff) · [`L3-152-simplificado.json`](../../automatas/lista2-afd/L3-152-simplificado.json) · [`L3-152-simplificado.xml`](../../automatas/lista2-afd/L3-152-simplificado.xml). Tipo según la definición: **AFD**, |Q| = 5, Σ = {0, 1, 2}, 15 transiciones.

**Diseño.** Partición: se inicia con {no finales, finales} y se separan los estados que van a bloques distintos con algún símbolo, hasta estabilizar; cada estado del resultado representa un bloque de estados equivalentes.

| Estado | 0 | 1 | 2 |
|---|---|---|---|
| →A | C | E | B |
| B | DF | E | B |
| C | A | DF | DF |
| *DF | DF | B | C |
| *E | DF | B | A |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `1` | acepta | acepta | acepta |
| 2 | `21` | acepta | acepta | acepta |
| 3 | `2220` | acepta | acepta | acepta |
| 4 | `22011120` | acepta | acepta | acepta |
| 5 | `211210220021` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `211` | rechaza | rechaza | — |
| 8 | `01002` | rechaza | rechaza | rechaza |
| 9 | `20000212` | rechaza | rechaza | rechaza |
| 10 | `121202220222` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `1`: A -1→ E — ✔
2. `21`: A -2→ B -1→ E — ✔
3. `2220`: A -2→ B -2→ B -2→ B -0→ DF — ✔
4. `22011120`: A -2→ B -2→ B -0→ DF -1→ B -1→ E -1→ B -2→ B -0→ DF — ✔
5. `211210220021`: A -2→ B -1→ E -1→ B -2→ B -1→ E -0→ DF -2→ C -2→ DF -0→ DF -0→ DF -2→ C -1→ DF — ✔
6. λ: A — ✘
7. `211`: A -2→ B -1→ E -1→ B — ✘
8. `01002`: A -0→ C -1→ DF -0→ DF -0→ DF -2→ C — ✘
9. `20000212`: A -2→ B -0→ DF -0→ DF -0→ DF -0→ DF -2→ C -1→ DF -2→ C — ✘
10. `121202220222`: A -1→ E -2→ A -1→ E -2→ A -0→ C -2→ DF -2→ C -2→ DF -0→ DF -2→ C -2→ DF -2→ C — ✘

</details>

Simulación paso a paso en JFLAP con `21`: [ver captura](../../evidencias/jflap/pasos/L3-152-simplificado.png).

<a id="problema-3-153"></a>

## Lista 3, problema 153

**Enunciado.** Diagrama del autómata de la tabla 153.

**Clasificación: AFD.** AFD dado por tabla (δ total) que se simplifica; la sección AFD es la que corresponde. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### Diagrama del autómata de la tabla 153. — `L3-153-original`

Archivos: [`L3-153-original.jff`](../../automatas/lista2-afd/L3-153-original.jff) · [`L3-153-original.json`](../../automatas/lista2-afd/L3-153-original.json) · [`L3-153-original.xml`](../../automatas/lista2-afd/L3-153-original.xml). Tipo según la definición: **AFD**, |Q| = 7, Σ = {0, 1}, 14 transiciones.

**Diseño.** Transcripción de la tabla. Los estados inaccesibles se hallan con un recorrido en anchura desde el inicial. No hay inaccesibles.

| Estado | 0 | 1 |
|---|---|---|
| →A | B | C |
| B | D | E |
| C | F | G |
| *D | D | E |
| E | F | G |
| *F | E | D |
| *G | F | G |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `00` | acepta | acepta | acepta |
| 2 | `11` | acepta | acepta | acepta |
| 3 | `1111` | acepta | acepta | — |
| 4 | `1101101` | acepta | acepta | — |
| 5 | `10001000010` | acepta | acepta | — |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `1100` | rechaza | rechaza | — |
| 8 | `00001` | rechaza | rechaza | — |
| 9 | `00001011` | rechaza | rechaza | — |
| 10 | `0111010011100` | rechaza | rechaza | — |

<details><summary>Recorrido completo de cada cadena</summary>

1. `00`: A -0→ B -0→ D — ✔
2. `11`: A -1→ C -1→ G — ✔
3. `1111`: A -1→ C -1→ G -1→ G -1→ G — ✔
4. `1101101`: A -1→ C -1→ G -0→ F -1→ D -1→ E -0→ F -1→ D — ✔
5. `10001000010`: A -1→ C -0→ F -0→ E -0→ F -1→ D -0→ D -0→ D -0→ D -0→ D -1→ E -0→ F — ✔
6. λ: A — ✘
7. `1100`: A -1→ C -1→ G -0→ F -0→ E — ✘
8. `00001`: A -0→ B -0→ D -0→ D -0→ D -1→ E — ✘
9. `00001011`: A -0→ B -0→ D -0→ D -0→ D -1→ E -0→ F -1→ D -1→ E — ✘
10. `0111010011100`: A -0→ B -1→ E -1→ G -1→ G -0→ F -1→ D -0→ D -0→ D -1→ E -1→ G -1→ G -0→ F -0→ E — ✘

</details>

Simulación paso a paso en JFLAP con `00`: [ver captura](../../evidencias/jflap/pasos/L3-153-original.png).

#### Autómata 153 simplificado. — `L3-153-simplificado`

Archivos: [`L3-153-simplificado.jff`](../../automatas/lista2-afd/L3-153-simplificado.jff) · [`L3-153-simplificado.json`](../../automatas/lista2-afd/L3-153-simplificado.json) · [`L3-153-simplificado.xml`](../../automatas/lista2-afd/L3-153-simplificado.xml). Tipo según la definición: **AFD**, |Q| = 6, Σ = {0, 1}, 12 transiciones.

**Diseño.** Partición: se inicia con {no finales, finales} y se separan los estados que van a bloques distintos con algún símbolo, hasta estabilizar; cada estado del resultado representa un bloque de estados equivalentes.

| Estado | 0 | 1 |
|---|---|---|
| →A | B | CE |
| B | D | CE |
| CE | F | G |
| *D | D | CE |
| *F | CE | D |
| *G | F | G |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `00` | acepta | acepta | — |
| 2 | `010` | acepta | acepta | — |
| 3 | `1101` | acepta | acepta | acepta |
| 4 | `0001101` | acepta | acepta | acepta |
| 5 | `01111000111` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `001` | rechaza | rechaza | rechaza |
| 8 | `11011` | rechaza | rechaza | rechaza |
| 9 | `00100011` | rechaza | rechaza | rechaza |
| 10 | `010100001100` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `00`: A -0→ B -0→ D — ✔
2. `010`: A -0→ B -1→ CE -0→ F — ✔
3. `1101`: A -1→ CE -1→ G -0→ F -1→ D — ✔
4. `0001101`: A -0→ B -0→ D -0→ D -1→ CE -1→ G -0→ F -1→ D — ✔
5. `01111000111`: A -0→ B -1→ CE -1→ G -1→ G -1→ G -0→ F -0→ CE -0→ F -1→ D -1→ CE -1→ G — ✔
6. λ: A — ✘
7. `001`: A -0→ B -0→ D -1→ CE — ✘
8. `11011`: A -1→ CE -1→ G -0→ F -1→ D -1→ CE — ✘
9. `00100011`: A -0→ B -0→ D -1→ CE -0→ F -0→ CE -0→ F -1→ D -1→ CE — ✘
10. `010100001100`: A -0→ B -1→ CE -0→ F -1→ D -0→ D -0→ D -0→ D -0→ D -1→ CE -1→ G -0→ F -0→ CE — ✘

</details>

Simulación paso a paso en JFLAP con `11`: [ver captura](../../evidencias/jflap/pasos/L3-153-simplificado.png).

<a id="problema-3-154"></a>

## Lista 3, problema 154

**Enunciado.** Diagrama del autómata de la tabla 154.

**Clasificación: AFD.** AFD dado por tabla (δ total) que se simplifica; la sección AFD es la que corresponde. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### Diagrama del autómata de la tabla 154. — `L3-154-original`

Archivos: [`L3-154-original.jff`](../../automatas/lista2-afd/L3-154-original.jff) · [`L3-154-original.json`](../../automatas/lista2-afd/L3-154-original.json) · [`L3-154-original.xml`](../../automatas/lista2-afd/L3-154-original.xml). Tipo según la definición: **AFD**, |Q| = 11, Σ = {0, 1}, 22 transiciones.

**Diseño.** Transcripción de la tabla. Los estados inaccesibles se hallan con un recorrido en anchura desde el inicial.

| Estado | 0 | 1 |
|---|---|---|
| →A | D | K |
| B | H | K |
| C | I | E |
| D | C | G |
| *E | K | I |
| F | B | E |
| *G | C | I |
| *H | C | B |
| I | G | K |
| *J | F | B |
| K | C | F |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `01` | acepta | acepta | acepta |
| 2 | `101` | acepta | acepta | acepta |
| 3 | `100101` | acepta | acepta | acepta |
| 4 | `00000110` | acepta | acepta | acepta |
| 5 | `010010100110` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `10` | rechaza | rechaza | rechaza |
| 8 | `00000` | rechaza | rechaza | — |
| 9 | `0110110` | rechaza | rechaza | rechaza |
| 10 | `10000010111` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `01`: A -0→ D -1→ G — ✔
2. `101`: A -1→ K -0→ C -1→ E — ✔
3. `100101`: A -1→ K -0→ C -0→ I -1→ K -0→ C -1→ E — ✔
4. `00000110`: A -0→ D -0→ C -0→ I -0→ G -0→ C -1→ E -1→ I -0→ G — ✔
5. `010010100110`: A -0→ D -1→ G -0→ C -0→ I -1→ K -0→ C -1→ E -0→ K -0→ C -1→ E -1→ I -0→ G — ✔
6. λ: A — ✘
7. `10`: A -1→ K -0→ C — ✘
8. `00000`: A -0→ D -0→ C -0→ I -0→ G -0→ C — ✘
9. `0110110`: A -0→ D -1→ G -1→ I -0→ G -1→ I -1→ K -0→ C — ✘
10. `10000010111`: A -1→ K -0→ C -0→ I -0→ G -0→ C -0→ I -1→ K -0→ C -1→ E -1→ I -1→ K — ✘

</details>

Simulación paso a paso en JFLAP con `01`: [ver captura](../../evidencias/jflap/pasos/L3-154-original.png).

#### Autómata 154 sin el estado inaccesible J. — `L3-154-accesibles`

Archivos: [`L3-154-accesibles.jff`](../../automatas/lista2-afd/L3-154-accesibles.jff) · [`L3-154-accesibles.json`](../../automatas/lista2-afd/L3-154-accesibles.json) · [`L3-154-accesibles.xml`](../../automatas/lista2-afd/L3-154-accesibles.xml). Tipo según la definición: **AFD**, |Q| = 10, Σ = {0, 1}, 20 transiciones.

**Diseño.** El recorrido desde A nunca alcanza J; se elimina con sus transiciones.

| Estado | 0 | 1 |
|---|---|---|
| →A | D | K |
| B | H | K |
| C | I | E |
| D | C | G |
| *E | K | I |
| F | B | E |
| *G | C | I |
| *H | C | B |
| I | G | K |
| K | C | F |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `01` | acepta | acepta | acepta |
| 2 | `001` | acepta | acepta | acepta |
| 3 | `111001` | acepta | acepta | acepta |
| 4 | `101000101` | acepta | acepta | acepta |
| 5 | `010101011110` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `10` | rechaza | rechaza | rechaza |
| 8 | `1101` | rechaza | rechaza | rechaza |
| 9 | `10111010` | rechaza | rechaza | rechaza |
| 10 | `00011010010` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `01`: A -0→ D -1→ G — ✔
2. `001`: A -0→ D -0→ C -1→ E — ✔
3. `111001`: A -1→ K -1→ F -1→ E -0→ K -0→ C -1→ E — ✔
4. `101000101`: A -1→ K -0→ C -1→ E -0→ K -0→ C -0→ I -1→ K -0→ C -1→ E — ✔
5. `010101011110`: A -0→ D -1→ G -0→ C -1→ E -0→ K -1→ F -0→ B -1→ K -1→ F -1→ E -1→ I -0→ G — ✔
6. λ: A — ✘
7. `10`: A -1→ K -0→ C — ✘
8. `1101`: A -1→ K -1→ F -0→ B -1→ K — ✘
9. `10111010`: A -1→ K -0→ C -1→ E -1→ I -1→ K -0→ C -1→ E -0→ K — ✘
10. `00011010010`: A -0→ D -0→ C -0→ I -1→ K -1→ F -0→ B -1→ K -0→ C -0→ I -1→ K -0→ C — ✘

</details>

Simulación paso a paso en JFLAP con `01`: [ver captura](../../evidencias/jflap/pasos/L3-154-accesibles.png).

#### Autómata 154 simplificado. — `L3-154-simplificado`

Archivos: [`L3-154-simplificado.jff`](../../automatas/lista2-afd/L3-154-simplificado.jff) · [`L3-154-simplificado.json`](../../automatas/lista2-afd/L3-154-simplificado.json) · [`L3-154-simplificado.xml`](../../automatas/lista2-afd/L3-154-simplificado.xml). Tipo según la definición: **AFD**, |Q| = 7, Σ = {0, 1}, 14 transiciones.

**Diseño.** Partición: se inicia con {no finales, finales} y se separan los estados que van a bloques distintos con algún símbolo, hasta estabilizar; cada estado del resultado representa un bloque de estados equivalentes.

| Estado | 0 | 1 |
|---|---|---|
| →A | D | K |
| BI | GH | K |
| CF | BI | E |
| D | CF | GH |
| *E | K | BI |
| *GH | CF | BI |
| K | CF | CF |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `01` | acepta | acepta | acepta |
| 2 | `101` | acepta | acepta | acepta |
| 3 | `10110` | acepta | acepta | acepta |
| 4 | `01101001` | acepta | acepta | acepta |
| 5 | `1101111100101` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `00` | rechaza | rechaza | rechaza |
| 8 | `1110` | rechaza | rechaza | rechaza |
| 9 | `00011001` | rechaza | rechaza | — |
| 10 | `01000000111` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `01`: A -0→ D -1→ GH — ✔
2. `101`: A -1→ K -0→ CF -1→ E — ✔
3. `10110`: A -1→ K -0→ CF -1→ E -1→ BI -0→ GH — ✔
4. `01101001`: A -0→ D -1→ GH -1→ BI -0→ GH -1→ BI -0→ GH -0→ CF -1→ E — ✔
5. `1101111100101`: A -1→ K -1→ CF -0→ BI -1→ K -1→ CF -1→ E -1→ BI -1→ K -0→ CF -0→ BI -1→ K -0→ CF -1→ E — ✔
6. λ: A — ✘
7. `00`: A -0→ D -0→ CF — ✘
8. `1110`: A -1→ K -1→ CF -1→ E -0→ K — ✘
9. `00011001`: A -0→ D -0→ CF -0→ BI -1→ K -1→ CF -0→ BI -0→ GH -1→ BI — ✘
10. `01000000111`: A -0→ D -1→ GH -0→ CF -0→ BI -0→ GH -0→ CF -0→ BI -0→ GH -1→ BI -1→ K -1→ CF — ✘

</details>

Simulación paso a paso en JFLAP con `01`: [ver captura](../../evidencias/jflap/pasos/L3-154-simplificado.png).

<a id="problema-3-155"></a>

## Lista 3, problema 155

**Enunciado.** Diagrama del autómata de la tabla 155.

**Clasificación: AFD.** AFD dado por tabla (δ total) que se simplifica; la sección AFD es la que corresponde. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### Diagrama del autómata de la tabla 155. — `L3-155-original`

Archivos: [`L3-155-original.jff`](../../automatas/lista2-afd/L3-155-original.jff) · [`L3-155-original.json`](../../automatas/lista2-afd/L3-155-original.json) · [`L3-155-original.xml`](../../automatas/lista2-afd/L3-155-original.xml). Tipo según la definición: **AFD**, |Q| = 12, Σ = {0, 1}, 24 transiciones.

**Diseño.** Transcripción de la tabla. Los estados inaccesibles se hallan con un recorrido en anchura desde el inicial.

| Estado | 0 | 1 |
|---|---|---|
| →A | B | C |
| B | D | E |
| C | K | G |
| D | H | E |
| E | F | D |
| *F | J | G |
| G | E | G |
| H | B | K |
| I | C | A |
| J | D | G |
| K | F | D |
| L | C | J |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `010` | acepta | acepta | acepta |
| 2 | `0010` | acepta | acepta | acepta |
| 3 | `10110` | acepta | acepta | acepta |
| 4 | `1101100010` | acepta | acepta | acepta |
| 5 | `0010101110010` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `00` | rechaza | rechaza | rechaza |
| 8 | `0100` | rechaza | rechaza | rechaza |
| 9 | `0011100` | rechaza | rechaza | rechaza |
| 10 | `01111000011` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `010`: A -0→ B -1→ E -0→ F — ✔
2. `0010`: A -0→ B -0→ D -1→ E -0→ F — ✔
3. `10110`: A -1→ C -0→ K -1→ D -1→ E -0→ F — ✔
4. `1101100010`: A -1→ C -1→ G -0→ E -1→ D -1→ E -0→ F -0→ J -0→ D -1→ E -0→ F — ✔
5. `0010101110010`: A -0→ B -0→ D -1→ E -0→ F -1→ G -0→ E -1→ D -1→ E -1→ D -0→ H -0→ B -1→ E -0→ F — ✔
6. λ: A — ✘
7. `00`: A -0→ B -0→ D — ✘
8. `0100`: A -0→ B -1→ E -0→ F -0→ J — ✘
9. `0011100`: A -0→ B -0→ D -1→ E -1→ D -1→ E -0→ F -0→ J — ✘
10. `01111000011`: A -0→ B -1→ E -1→ D -1→ E -1→ D -0→ H -0→ B -0→ D -0→ H -1→ K -1→ D — ✘

</details>

Simulación paso a paso en JFLAP con `010`: [ver captura](../../evidencias/jflap/pasos/L3-155-original.png).

#### Autómata 155 sin los estados inaccesibles I y L. — `L3-155-accesibles`

Archivos: [`L3-155-accesibles.jff`](../../automatas/lista2-afd/L3-155-accesibles.jff) · [`L3-155-accesibles.json`](../../automatas/lista2-afd/L3-155-accesibles.json) · [`L3-155-accesibles.xml`](../../automatas/lista2-afd/L3-155-accesibles.xml). Tipo según la definición: **AFD**, |Q| = 10, Σ = {0, 1}, 20 transiciones.

**Diseño.** El recorrido desde A no alcanza I ni L; se eliminan.

| Estado | 0 | 1 |
|---|---|---|
| →A | B | C |
| B | D | E |
| C | K | G |
| D | H | E |
| E | F | D |
| *F | J | G |
| G | E | G |
| H | B | K |
| J | D | G |
| K | F | D |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `010` | acepta | acepta | acepta |
| 2 | `1100` | acepta | acepta | acepta |
| 3 | `10110` | acepta | acepta | acepta |
| 4 | `010111100` | acepta | acepta | acepta |
| 5 | `111011000010` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `10` | rechaza | rechaza | rechaza |
| 8 | `1010` | rechaza | rechaza | rechaza |
| 9 | `0011000` | rechaza | rechaza | rechaza |
| 10 | `10110111001` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `010`: A -0→ B -1→ E -0→ F — ✔
2. `1100`: A -1→ C -1→ G -0→ E -0→ F — ✔
3. `10110`: A -1→ C -0→ K -1→ D -1→ E -0→ F — ✔
4. `010111100`: A -0→ B -1→ E -0→ F -1→ G -1→ G -1→ G -1→ G -0→ E -0→ F — ✔
5. `111011000010`: A -1→ C -1→ G -1→ G -0→ E -1→ D -1→ E -0→ F -0→ J -0→ D -0→ H -1→ K -0→ F — ✔
6. λ: A — ✘
7. `10`: A -1→ C -0→ K — ✘
8. `1010`: A -1→ C -0→ K -1→ D -0→ H — ✘
9. `0011000`: A -0→ B -0→ D -1→ E -1→ D -0→ H -0→ B -0→ D — ✘
10. `10110111001`: A -1→ C -0→ K -1→ D -1→ E -0→ F -1→ G -1→ G -1→ G -0→ E -0→ F -1→ G — ✘

</details>

Simulación paso a paso en JFLAP con `010`: [ver captura](../../evidencias/jflap/pasos/L3-155-accesibles.png).

#### Autómata 155 simplificado. — `L3-155-simplificado`

Archivos: [`L3-155-simplificado.jff`](../../automatas/lista2-afd/L3-155-simplificado.jff) · [`L3-155-simplificado.json`](../../automatas/lista2-afd/L3-155-simplificado.json) · [`L3-155-simplificado.xml`](../../automatas/lista2-afd/L3-155-simplificado.xml). Tipo según la definición: **AFD**, |Q| = 5, Σ = {0, 1}, 10 transiciones.

**Diseño.** Partición: se inicia con {no finales, finales} y se separan los estados que van a bloques distintos con algún símbolo, hasta estabilizar; cada estado del resultado representa un bloque de estados equivalentes.

| Estado | 0 | 1 |
|---|---|---|
| →AJ | BDH | CG |
| BDH | BDH | EK |
| CG | EK | CG |
| EK | F | BDH |
| *F | AJ | CG |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `010` | acepta | acepta | acepta |
| 2 | `1100` | acepta | acepta | acepta |
| 3 | `101010` | acepta | acepta | acepta |
| 4 | `1011110` | acepta | acepta | acepta |
| 5 | `0110100110110` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `10` | rechaza | rechaza | rechaza |
| 8 | `0100` | rechaza | rechaza | rechaza |
| 9 | `0010000` | rechaza | rechaza | rechaza |
| 10 | `01101110011` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `010`: AJ -0→ BDH -1→ EK -0→ F — ✔
2. `1100`: AJ -1→ CG -1→ CG -0→ EK -0→ F — ✔
3. `101010`: AJ -1→ CG -0→ EK -1→ BDH -0→ BDH -1→ EK -0→ F — ✔
4. `1011110`: AJ -1→ CG -0→ EK -1→ BDH -1→ EK -1→ BDH -1→ EK -0→ F — ✔
5. `0110100110110`: AJ -0→ BDH -1→ EK -1→ BDH -0→ BDH -1→ EK -0→ F -0→ AJ -1→ CG -1→ CG -0→ EK -1→ BDH -1→ EK -0→ F — ✔
6. λ: AJ — ✘
7. `10`: AJ -1→ CG -0→ EK — ✘
8. `0100`: AJ -0→ BDH -1→ EK -0→ F -0→ AJ — ✘
9. `0010000`: AJ -0→ BDH -0→ BDH -1→ EK -0→ F -0→ AJ -0→ BDH -0→ BDH — ✘
10. `01101110011`: AJ -0→ BDH -1→ EK -1→ BDH -0→ BDH -1→ EK -1→ BDH -1→ EK -0→ F -0→ AJ -1→ CG -1→ CG — ✘

</details>

Simulación paso a paso en JFLAP con `010`: [ver captura](../../evidencias/jflap/pasos/L3-155-simplificado.png).

<a id="problema-3-156"></a>

## Lista 3, problema 156

**Enunciado.** Tabla del autómata del diagrama 156.

**Clasificación: AFD.** AFD dado por tabla (δ total) que se simplifica; la sección AFD es la que corresponde. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### Tabla del autómata del diagrama 156. — `L3-156-original`

Archivos: [`L3-156-original.jff`](../../automatas/lista2-afd/L3-156-original.jff) · [`L3-156-original.json`](../../automatas/lista2-afd/L3-156-original.json) · [`L3-156-original.xml`](../../automatas/lista2-afd/L3-156-original.xml). Tipo según la definición: **AFD**, |Q| = 5, Σ = {0, 1}, 10 transiciones.

**Diseño.** Transcripción del diagrama de la lista.

| Estado | 0 | 1 |
|---|---|---|
| →A | B | C |
| B | C | E |
| C | D | C |
| D | C | E |
| *E | B | E |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `01` | acepta | acepta | acepta |
| 2 | `1101` | acepta | acepta | acepta |
| 3 | `000001` | acepta | acepta | acepta |
| 4 | `11000101` | acepta | acepta | acepta |
| 5 | `1001011001101` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `00` | rechaza | rechaza | rechaza |
| 8 | `0000` | rechaza | rechaza | rechaza |
| 9 | `1000100` | rechaza | rechaza | rechaza |
| 10 | `10011010100` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `01`: A -0→ B -1→ E — ✔
2. `1101`: A -1→ C -1→ C -0→ D -1→ E — ✔
3. `000001`: A -0→ B -0→ C -0→ D -0→ C -0→ D -1→ E — ✔
4. `11000101`: A -1→ C -1→ C -0→ D -0→ C -0→ D -1→ E -0→ B -1→ E — ✔
5. `1001011001101`: A -1→ C -0→ D -0→ C -1→ C -0→ D -1→ E -1→ E -0→ B -0→ C -1→ C -1→ C -0→ D -1→ E — ✔
6. λ: A — ✘
7. `00`: A -0→ B -0→ C — ✘
8. `0000`: A -0→ B -0→ C -0→ D -0→ C — ✘
9. `1000100`: A -1→ C -0→ D -0→ C -0→ D -1→ E -0→ B -0→ C — ✘
10. `10011010100`: A -1→ C -0→ D -0→ C -1→ C -1→ C -0→ D -1→ E -0→ B -1→ E -0→ B -0→ C — ✘

</details>

Simulación paso a paso en JFLAP con `01`: [ver captura](../../evidencias/jflap/pasos/L3-156-original.png).

#### Autómata 156 simplificado. — `L3-156-simplificado`

Archivos: [`L3-156-simplificado.jff`](../../automatas/lista2-afd/L3-156-simplificado.jff) · [`L3-156-simplificado.json`](../../automatas/lista2-afd/L3-156-simplificado.json) · [`L3-156-simplificado.xml`](../../automatas/lista2-afd/L3-156-simplificado.xml). Tipo según la definición: **AFD**, |Q| = 3, Σ = {0, 1}, 6 transiciones.

**Diseño.** Partición: se inicia con {no finales, finales} y se separan los estados que van a bloques distintos con algún símbolo, hasta estabilizar; cada estado del resultado representa un bloque de estados equivalentes.

| Estado | 0 | 1 |
|---|---|---|
| →AC | BD | AC |
| BD | AC | E |
| *E | BD | E |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `01` | acepta | acepta | acepta |
| 2 | `0001` | acepta | acepta | acepta |
| 3 | `11101` | acepta | acepta | acepta |
| 4 | `010110001` | acepta | acepta | acepta |
| 5 | `0111100110001` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `00` | rechaza | rechaza | rechaza |
| 8 | `0110` | rechaza | rechaza | rechaza |
| 9 | `10100010` | rechaza | rechaza | rechaza |
| 10 | `101011000110` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `01`: AC -0→ BD -1→ E — ✔
2. `0001`: AC -0→ BD -0→ AC -0→ BD -1→ E — ✔
3. `11101`: AC -1→ AC -1→ AC -1→ AC -0→ BD -1→ E — ✔
4. `010110001`: AC -0→ BD -1→ E -0→ BD -1→ E -1→ E -0→ BD -0→ AC -0→ BD -1→ E — ✔
5. `0111100110001`: AC -0→ BD -1→ E -1→ E -1→ E -1→ E -0→ BD -0→ AC -1→ AC -1→ AC -0→ BD -0→ AC -0→ BD -1→ E — ✔
6. λ: AC — ✘
7. `00`: AC -0→ BD -0→ AC — ✘
8. `0110`: AC -0→ BD -1→ E -1→ E -0→ BD — ✘
9. `10100010`: AC -1→ AC -0→ BD -1→ E -0→ BD -0→ AC -0→ BD -1→ E -0→ BD — ✘
10. `101011000110`: AC -1→ AC -0→ BD -1→ E -0→ BD -1→ E -1→ E -0→ BD -0→ AC -0→ BD -1→ E -1→ E -0→ BD — ✘

</details>

Simulación paso a paso en JFLAP con `01`: [ver captura](../../evidencias/jflap/pasos/L3-156-simplificado.png).

<a id="problema-3-157"></a>

## Lista 3, problema 157

**Enunciado.** Tabla del autómata del diagrama 157.

**Clasificación: AFD.** AFD dado por tabla (δ total) que se simplifica; la sección AFD es la que corresponde. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

#### Tabla del autómata del diagrama 157. — `L3-157-original`

Archivos: [`L3-157-original.jff`](../../automatas/lista2-afd/L3-157-original.jff) · [`L3-157-original.json`](../../automatas/lista2-afd/L3-157-original.json) · [`L3-157-original.xml`](../../automatas/lista2-afd/L3-157-original.xml). Tipo según la definición: **AFD**, |Q| = 6, Σ = {0, 1}, 12 transiciones.

**Diseño.** Transcripción del diagrama de la lista.

| Estado | 0 | 1 |
|---|---|---|
| →A | B | F |
| B | C | E |
| C | D | E |
| D | B | E |
| E | F | D |
| *F | F | B |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `1` | acepta | acepta | acepta |
| 2 | `010` | acepta | acepta | acepta |
| 3 | `1000` | acepta | acepta | acepta |
| 4 | `100100010` | acepta | acepta | acepta |
| 5 | `1101110101110` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `01` | rechaza | rechaza | rechaza |
| 8 | `1001` | rechaza | rechaza | rechaza |
| 9 | `0000111` | rechaza | rechaza | rechaza |
| 10 | `01110001001` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `1`: A -1→ F — ✔
2. `010`: A -0→ B -1→ E -0→ F — ✔
3. `1000`: A -1→ F -0→ F -0→ F -0→ F — ✔
4. `100100010`: A -1→ F -0→ F -0→ F -1→ B -0→ C -0→ D -0→ B -1→ E -0→ F — ✔
5. `1101110101110`: A -1→ F -1→ B -0→ C -1→ E -1→ D -1→ E -0→ F -1→ B -0→ C -1→ E -1→ D -1→ E -0→ F — ✔
6. λ: A — ✘
7. `01`: A -0→ B -1→ E — ✘
8. `1001`: A -1→ F -0→ F -0→ F -1→ B — ✘
9. `0000111`: A -0→ B -0→ C -0→ D -0→ B -1→ E -1→ D -1→ E — ✘
10. `01110001001`: A -0→ B -1→ E -1→ D -1→ E -0→ F -0→ F -0→ F -1→ B -0→ C -0→ D -1→ E — ✘

</details>

Simulación paso a paso en JFLAP con `010`: [ver captura](../../evidencias/jflap/pasos/L3-157-original.png).

#### Autómata 157 simplificado. — `L3-157-simplificado`

Archivos: [`L3-157-simplificado.jff`](../../automatas/lista2-afd/L3-157-simplificado.jff) · [`L3-157-simplificado.json`](../../automatas/lista2-afd/L3-157-simplificado.json) · [`L3-157-simplificado.xml`](../../automatas/lista2-afd/L3-157-simplificado.xml). Tipo según la definición: **AFD**, |Q| = 4, Σ = {0, 1}, 8 transiciones.

**Diseño.** Partición: se inicia con {no finales, finales} y se separan los estados que van a bloques distintos con algún símbolo, hasta estabilizar; cada estado del resultado representa un bloque de estados equivalentes.

| Estado | 0 | 1 |
|---|---|---|
| →A | BCD | F |
| BCD | BCD | E |
| E | F | BCD |
| *F | F | BCD |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `1` | acepta | acepta | acepta |
| 2 | `1110` | acepta | acepta | acepta |
| 3 | `111110` | acepta | acepta | acepta |
| 4 | `1010010` | acepta | acepta | acepta |
| 5 | `00010001100` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `11` | rechaza | rechaza | rechaza |
| 8 | `01001` | rechaza | rechaza | rechaza |
| 9 | `0011101` | rechaza | rechaza | rechaza |
| 10 | `10011010111` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `1`: A -1→ F — ✔
2. `1110`: A -1→ F -1→ BCD -1→ E -0→ F — ✔
3. `111110`: A -1→ F -1→ BCD -1→ E -1→ BCD -1→ E -0→ F — ✔
4. `1010010`: A -1→ F -0→ F -1→ BCD -0→ BCD -0→ BCD -1→ E -0→ F — ✔
5. `00010001100`: A -0→ BCD -0→ BCD -0→ BCD -1→ E -0→ F -0→ F -0→ F -1→ BCD -1→ E -0→ F -0→ F — ✔
6. λ: A — ✘
7. `11`: A -1→ F -1→ BCD — ✘
8. `01001`: A -0→ BCD -1→ E -0→ F -0→ F -1→ BCD — ✘
9. `0011101`: A -0→ BCD -0→ BCD -1→ E -1→ BCD -1→ E -0→ F -1→ BCD — ✘
10. `10011010111`: A -1→ F -0→ F -0→ F -1→ BCD -1→ E -0→ F -1→ BCD -0→ BCD -1→ E -1→ BCD -1→ E — ✘

</details>

Simulación paso a paso en JFLAP con `1110`: [ver captura](../../evidencias/jflap/pasos/L3-157-simplificado.png).

<a id="problema-3-254"></a>

## Lista 3, problema 254

**Enunciado.** Autómata de la tabla 254. Encontrar una expresión regular.

**Clasificación: AFD.** El autómata dado es un AFD (δ total); la expresión se obtiene con el lema de Arden. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

**Expresión regular** (archivo de JFLAP [`L3-254-ER.jff`](../../automatas/lista2-afd/L3-254-ER.jff)): `(0+1)*1` (en JFLAP, `+` es la unión y `!` es λ).

**Obtención.** Lema de Arden sobre las ecuaciones del autómata.

#### AFD dado en la tabla — `L3-254`

Archivos: [`L3-254.jff`](../../automatas/lista2-afd/L3-254.jff) · [`L3-254.json`](../../automatas/lista2-afd/L3-254.json) · [`L3-254.xml`](../../automatas/lista2-afd/L3-254.xml). Tipo según la definición: **AFD**, |Q| = 2, Σ = {0, 1}, 4 transiciones.

**Diseño.** Transcripción. El estado recuerda si el último símbolo fue 1.

| Estado | 0 | 1 |
|---|---|---|
| →A | A | B |
| *B | A | B |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `1` | acepta | acepta | acepta |
| 2 | `01` | acepta | acepta | acepta |
| 3 | `01101` | acepta | acepta | acepta |
| 4 | `00011101` | acepta | acepta | acepta |
| 5 | `11110001111` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `010` | rechaza | rechaza | rechaza |
| 8 | `11010` | rechaza | rechaza | rechaza |
| 9 | `0000010` | rechaza | rechaza | rechaza |
| 10 | `11001010000` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `1`: A -1→ B — ✔
2. `01`: A -0→ A -1→ B — ✔
3. `01101`: A -0→ A -1→ B -1→ B -0→ A -1→ B — ✔
4. `00011101`: A -0→ A -0→ A -0→ A -1→ B -1→ B -1→ B -0→ A -1→ B — ✔
5. `11110001111`: A -1→ B -1→ B -1→ B -1→ B -0→ A -0→ A -0→ A -1→ B -1→ B -1→ B -1→ B — ✔
6. λ: A — ✘
7. `010`: A -0→ A -1→ B -0→ A — ✘
8. `11010`: A -1→ B -1→ B -0→ A -1→ B -0→ A — ✘
9. `0000010`: A -0→ A -0→ A -0→ A -0→ A -0→ A -1→ B -0→ A — ✘
10. `11001010000`: A -1→ B -1→ B -0→ A -0→ A -1→ B -0→ A -1→ B -0→ A -0→ A -0→ A -0→ A — ✘

</details>

Simulación paso a paso en JFLAP con `01`: [ver captura](../../evidencias/jflap/pasos/L3-254.png).

<a id="problema-3-255"></a>

## Lista 3, problema 255

**Enunciado.** Autómata de la tabla 255. Encontrar una expresión regular.

**Clasificación: AFD.** El autómata dado es un AFD (δ total); la expresión se obtiene con el lema de Arden. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

**Expresión regular** (archivo de JFLAP [`L3-255-ER.jff`](../../automatas/lista2-afd/L3-255-ER.jff)): `((0+1)1*0)*` (en JFLAP, `+` es la unión y `!` es λ).

**Obtención.** Lema de Arden.

#### AFD dado en la tabla — `L3-255`

Archivos: [`L3-255.jff`](../../automatas/lista2-afd/L3-255.jff) · [`L3-255.json`](../../automatas/lista2-afd/L3-255.json) · [`L3-255.xml`](../../automatas/lista2-afd/L3-255.xml). Tipo según la definición: **AFD**, |Q| = 2, Σ = {0, 1}, 4 transiciones.

**Diseño.** Transcripción de la tabla.

| Estado | 0 | 1 |
|---|---|---|
| →*A | B | B |
| B | A | B |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | acepta | acepta | acepta |
| 2 | `10` | acepta | acepta | acepta |
| 3 | `0010` | acepta | acepta | acepta |
| 4 | `11101010` | acepta | acepta | acepta |
| 5 | `01111011110` | acepta | acepta | acepta |
| 6 | `0` | rechaza | rechaza | rechaza |
| 7 | `000` | rechaza | rechaza | rechaza |
| 8 | `10000` | rechaza | rechaza | rechaza |
| 9 | `11111100` | rechaza | rechaza | rechaza |
| 10 | `101100010100` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: A — ✔
2. `10`: A -1→ B -0→ A — ✔
3. `0010`: A -0→ B -0→ A -1→ B -0→ A — ✔
4. `11101010`: A -1→ B -1→ B -1→ B -0→ A -1→ B -0→ A -1→ B -0→ A — ✔
5. `01111011110`: A -0→ B -1→ B -1→ B -1→ B -1→ B -0→ A -1→ B -1→ B -1→ B -1→ B -0→ A — ✔
6. `0`: A -0→ B — ✘
7. `000`: A -0→ B -0→ A -0→ B — ✘
8. `10000`: A -1→ B -0→ A -0→ B -0→ A -0→ B — ✘
9. `11111100`: A -1→ B -1→ B -1→ B -1→ B -1→ B -1→ B -0→ A -0→ B — ✘
10. `101100010100`: A -1→ B -0→ A -1→ B -1→ B -0→ A -0→ B -0→ A -1→ B -0→ A -1→ B -0→ A -0→ B — ✘

</details>

Simulación paso a paso en JFLAP con `10`: [ver captura](../../evidencias/jflap/pasos/L3-255.png).

<a id="problema-3-256"></a>

## Lista 3, problema 256

**Enunciado.** Autómata de la tabla 256. Encontrar una expresión regular.

**Clasificación: AFD.** El autómata dado es un AFD (δ total); la expresión se obtiene con el lema de Arden. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

**Expresión regular** (archivo de JFLAP [`L3-256-ER.jff`](../../automatas/lista2-afd/L3-256-ER.jff)): `(1+2+0(0+1)*2)*0(0+1)*` (en JFLAP, `+` es la unión y `!` es λ).

**Obtención.** Lema de Arden.

#### AFD dado en la tabla — `L3-256`

Archivos: [`L3-256.jff`](../../automatas/lista2-afd/L3-256.jff) · [`L3-256.json`](../../automatas/lista2-afd/L3-256.json) · [`L3-256.xml`](../../automatas/lista2-afd/L3-256.xml). Tipo según la definición: **AFD**, |Q| = 2, Σ = {0, 1, 2}, 6 transiciones.

**Diseño.** Transcripción de la tabla.

| Estado | 0 | 1 | 2 |
|---|---|---|---|
| →A | B | A | A |
| *B | B | B | A |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `0` | acepta | acepta | acepta |
| 2 | `00` | acepta | acepta | acepta |
| 3 | `00120` | acepta | acepta | acepta |
| 4 | `1222100` | acepta | acepta | acepta |
| 5 | `012111111220` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `11` | rechaza | rechaza | rechaza |
| 8 | `20012` | rechaza | rechaza | rechaza |
| 9 | `02210012` | rechaza | rechaza | rechaza |
| 10 | `112112111012` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `0`: A -0→ B — ✔
2. `00`: A -0→ B -0→ B — ✔
3. `00120`: A -0→ B -0→ B -1→ B -2→ A -0→ B — ✔
4. `1222100`: A -1→ A -2→ A -2→ A -2→ A -1→ A -0→ B -0→ B — ✔
5. `012111111220`: A -0→ B -1→ B -2→ A -1→ A -1→ A -1→ A -1→ A -1→ A -1→ A -2→ A -2→ A -0→ B — ✔
6. λ: A — ✘
7. `11`: A -1→ A -1→ A — ✘
8. `20012`: A -2→ A -0→ B -0→ B -1→ B -2→ A — ✘
9. `02210012`: A -0→ B -2→ A -2→ A -1→ A -0→ B -0→ B -1→ B -2→ A — ✘
10. `112112111012`: A -1→ A -1→ A -2→ A -1→ A -1→ A -2→ A -1→ A -1→ A -1→ A -0→ B -1→ B -2→ A — ✘

</details>

Simulación paso a paso en JFLAP con `00`: [ver captura](../../evidencias/jflap/pasos/L3-256.png).

<a id="problema-3-257"></a>

## Lista 3, problema 257

**Enunciado.** Autómata de la tabla 257. Encontrar una expresión regular.

**Clasificación: AFD.** El autómata dado es un AFD (δ total); la expresión se obtiene con el lema de Arden. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

**Expresión regular** (archivo de JFLAP [`L3-257-ER.jff`](../../automatas/lista2-afd/L3-257-ER.jff)): `((1+01*0)(0+1))*(01*(λ+0)+1)` (en JFLAP, `+` es la unión y `!` es λ).

**Obtención.** Lema de Arden.

#### AFD dado en la tabla — `L3-257`

Archivos: [`L3-257.jff`](../../automatas/lista2-afd/L3-257.jff) · [`L3-257.json`](../../automatas/lista2-afd/L3-257.json) · [`L3-257.xml`](../../automatas/lista2-afd/L3-257.xml). Tipo según la definición: **AFD**, |Q| = 3, Σ = {0, 1}, 6 transiciones.

**Diseño.** Transcripción de la tabla.

| Estado | 0 | 1 |
|---|---|---|
| →A | B | C |
| *B | C | B |
| *C | A | A |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `1` | acepta | acepta | acepta |
| 2 | `01` | acepta | acepta | acepta |
| 3 | `10101` | acepta | acepta | acepta |
| 4 | `11100011` | acepta | acepta | acepta |
| 5 | `111100010101` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `000` | rechaza | rechaza | rechaza |
| 8 | `1011` | rechaza | rechaza | rechaza |
| 9 | `1110001` | rechaza | rechaza | rechaza |
| 10 | `0100101110000` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `1`: A -1→ C — ✔
2. `01`: A -0→ B -1→ B — ✔
3. `10101`: A -1→ C -0→ A -1→ C -0→ A -1→ C — ✔
4. `11100011`: A -1→ C -1→ A -1→ C -0→ A -0→ B -0→ C -1→ A -1→ C — ✔
5. `111100010101`: A -1→ C -1→ A -1→ C -1→ A -0→ B -0→ C -0→ A -1→ C -0→ A -1→ C -0→ A -1→ C — ✔
6. λ: A — ✘
7. `000`: A -0→ B -0→ C -0→ A — ✘
8. `1011`: A -1→ C -0→ A -1→ C -1→ A — ✘
9. `1110001`: A -1→ C -1→ A -1→ C -0→ A -0→ B -0→ C -1→ A — ✘
10. `0100101110000`: A -0→ B -1→ B -0→ C -0→ A -1→ C -0→ A -1→ C -1→ A -1→ C -0→ A -0→ B -0→ C -0→ A — ✘

</details>

Simulación paso a paso en JFLAP con `01`: [ver captura](../../evidencias/jflap/pasos/L3-257.png).

<a id="problema-3-258"></a>

## Lista 3, problema 258

**Enunciado.** Autómata de la tabla 258. Encontrar una expresión regular.

**Clasificación: AFD.** El autómata dado es un AFD (δ total); la expresión se obtiene con el lema de Arden. *(Entregado en la Práctica 1; aquí se agregan los formatos .json y .xml, las pruebas y los recorridos.)*

**Expresión regular** (archivo de JFLAP [`L3-258-ER.jff`](../../automatas/lista2-afd/L3-258-ER.jff)): `((0+1)(01)*(00+1))*(0+1)(01)*` (en JFLAP, `+` es la unión y `!` es λ).

**Obtención.** Lema de Arden.

#### AFD dado en la tabla — `L3-258`

Archivos: [`L3-258.jff`](../../automatas/lista2-afd/L3-258.jff) · [`L3-258.json`](../../automatas/lista2-afd/L3-258.json) · [`L3-258.xml`](../../automatas/lista2-afd/L3-258.xml). Tipo según la definición: **AFD**, |Q| = 3, Σ = {0, 1}, 6 transiciones.

**Diseño.** Transcripción de la tabla.

| Estado | 0 | 1 |
|---|---|---|
| →A | C | C |
| B | A | C |
| *C | B | A |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `0` | acepta | acepta | acepta |
| 2 | `010` | acepta | acepta | acepta |
| 3 | `01110` | acepta | acepta | acepta |
| 4 | `00100110` | acepta | acepta | acepta |
| 5 | `001100001110` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `00` | rechaza | rechaza | rechaza |
| 8 | `1110` | rechaza | rechaza | rechaza |
| 9 | `0000110` | rechaza | rechaza | rechaza |
| 10 | `010101011010` | rechaza | rechaza | — |

<details><summary>Recorrido completo de cada cadena</summary>

1. `0`: A -0→ C — ✔
2. `010`: A -0→ C -1→ A -0→ C — ✔
3. `01110`: A -0→ C -1→ A -1→ C -1→ A -0→ C — ✔
4. `00100110`: A -0→ C -0→ B -1→ C -0→ B -0→ A -1→ C -1→ A -0→ C — ✔
5. `001100001110`: A -0→ C -0→ B -1→ C -1→ A -0→ C -0→ B -0→ A -0→ C -1→ A -1→ C -1→ A -0→ C — ✔
6. λ: A — ✘
7. `00`: A -0→ C -0→ B — ✘
8. `1110`: A -1→ C -1→ A -1→ C -0→ B — ✘
9. `0000110`: A -0→ C -0→ B -0→ A -0→ C -1→ A -1→ C -0→ B — ✘
10. `010101011010`: A -0→ C -1→ A -0→ C -1→ A -0→ C -1→ A -0→ C -1→ A -1→ C -0→ B -1→ C -0→ B — ✘

</details>

Simulación paso a paso en JFLAP con `010`: [ver captura](../../evidencias/jflap/pasos/L3-258.png).

<a id="problema-3-259"></a>

## Lista 3, problema 259

**Enunciado.** Para el autómata de la tabla, ¿qué valores Rᵢⱼ⁽ᵏ⁾ (k = 0,…,4) son necesarios para encontrar R₁₄⁽⁴⁾? Encontrar una expresión regular equivalente.

**Clasificación: AFD.** El autómata dado es un AFD (δ total); se aplica el algoritmo Rᵢⱼ⁽ᵏ⁾ de Kleene.

Con los estados numerados 1-4, R₁₄⁽⁴⁾ = R₁₄⁽³⁾ + R₁₄⁽³⁾ (R₄₄⁽³⁾)* R₄₄⁽³⁾, y cada Rᵢⱼ⁽ᵏ⁾ se obtiene de Rᵢⱼ⁽ᵏ⁻¹⁾ + Rᵢₖ⁽ᵏ⁻¹⁾ (Rₖₖ⁽ᵏ⁻¹⁾)* Rₖⱼ⁽ᵏ⁻¹⁾. Desarrollando la recursión desde R₁₄⁽⁴⁾, los valores necesarios son:

| k | Pares (i, j) necesarios | Valores |
|---|---|---|
| 4 | (1,4) | R14⁽4⁾ = `∅` |
| 3 | (1,4), (4,4) | R14⁽3⁾ = `∅`; R44⁽3⁾ = `b+λ` |
| 2 | (1,3), (1,4), (3,3), (3,4), (4,3), (4,4) | R13⁽2⁾ = `a+b((λ+ab)*)(b+aa)`; R14⁽2⁾ = `∅`; R33⁽2⁾ = `b+λ+a((λ+ab)*)(b+aa)`; R34⁽2⁾ = `∅`; R43⁽2⁾ = `aa+ab((λ+ab)*)(b+aa)`; R44⁽2⁾ = `b+λ` |
| 1 | (1,2), (1,3), (1,4), (2,2), (2,3), (2,4), (3,2), (3,3), (3,4), (4,2), (4,3), (4,4) | R12⁽1⁾ = `b`; R13⁽1⁾ = `a`; R14⁽1⁾ = `∅`; R22⁽1⁾ = `λ+ab`; R23⁽1⁾ = `b+aa`; R24⁽1⁾ = `∅`; R32⁽1⁾ = `a`; R33⁽1⁾ = `b+λ`; R34⁽1⁾ = `∅`; R42⁽1⁾ = `ab`; R43⁽1⁾ = `aa`; R44⁽1⁾ = `b+λ` |
| 0 | (1,1), (1,2), (1,3), (1,4), (2,1), (2,2), (2,3), (2,4), (3,1), (3,2), (3,3), (3,4), (4,1), (4,2), (4,3), (4,4) | R11⁽0⁾ = `λ`; R12⁽0⁾ = `b`; R13⁽0⁾ = `a`; R14⁽0⁾ = `∅`; R21⁽0⁾ = `a`; R22⁽0⁾ = `λ`; R23⁽0⁾ = `b`; R24⁽0⁾ = `∅`; R31⁽0⁾ = `∅`; R32⁽0⁾ = `a`; R33⁽0⁾ = `b+λ`; R34⁽0⁾ = `∅`; R41⁽0⁾ = `a`; R42⁽0⁾ = `∅`; R43⁽0⁾ = `∅`; R44⁽0⁾ = `b+λ` |

**Resultado:** R₁₄⁽⁴⁾ = `∅`. El estado 4 no es alcanzable desde 1 (de 1, 2 y 3 solo se llega a 1, 2 y 3), así que todos los Rᵢ₄⁽ᵏ⁾ con i ≤ 3 valen ∅ y la expresión equivalente al autómata es **∅**: el lenguaje es vacío.

#### AFD dado en la tabla — `L3-259`

Archivos: [`L3-259.jff`](../../automatas/lista2-afd/L3-259.jff) · [`L3-259.json`](../../automatas/lista2-afd/L3-259.json) · [`L3-259.xml`](../../automatas/lista2-afd/L3-259.xml). Tipo según la definición: **AFD**, |Q| = 4, Σ = {a, b}, 8 transiciones.

**Diseño.** Transcripción: 1 -a→ 3, 1 -b→ 2; 2 -a→ 1, 2 -b→ 3; 3 -a→ 2, 3 -b→ 3; 4 -a→ 1, 4 -b→ 4. El estado de aceptación 4 no tiene transiciones de entrada desde 1, 2 o 3.

| Estado | a | b |
|---|---|---|
| →1 | 3 | 2 |
| 2 | 1 | 3 |
| 3 | 2 | 3 |
| *4 | 1 | 4 |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | rechaza | rechaza | rechaza |
| 2 | `aa` | rechaza | rechaza | rechaza |
| 3 | `aabb` | rechaza | rechaza | rechaza |
| 4 | `abaabbb` | rechaza | rechaza | rechaza |
| 5 | `ababaaaabaa` | rechaza | rechaza | rechaza |

Nota sobre los casos: el lenguaje solo tiene 0 palabras.

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: 1 — ✘
2. `aa`: 1 -a→ 3 -a→ 2 — ✘
3. `aabb`: 1 -a→ 3 -a→ 2 -b→ 3 -b→ 3 — ✘
4. `abaabbb`: 1 -a→ 3 -b→ 3 -a→ 2 -a→ 1 -b→ 2 -b→ 3 -b→ 3 — ✘
5. `ababaaaabaa`: 1 -a→ 3 -b→ 3 -a→ 2 -b→ 3 -a→ 2 -a→ 1 -a→ 3 -a→ 2 -b→ 3 -a→ 2 -a→ 1 — ✘

</details>

Simulación paso a paso en JFLAP con `aa`: [ver captura](../../evidencias/jflap/pasos/L3-259.png).

