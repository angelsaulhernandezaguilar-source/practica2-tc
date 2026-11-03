# Ejercicio 2 — AFND-λ (problemas 241-253)

[← Ejercicio 2](../02-jflap.md) · [Índice](../../README.md)

Cada autómata indica su clasificación, el diseño, la tabla de transiciones, cinco cadenas válidas y cinco inválidas con el resultado esperado (oráculo escrito a partir del enunciado), el del simulador de este proyecto y el del motor de JFLAP 7.1, el recorrido de cada cadena (en los no deterministas, el conjunto de estados activos y el árbol de caminos) y la captura de la simulación paso a paso en JFLAP.

<a id="problema-3-241"></a>

## Lista 3, problema 241

**Enunciado.** Encontrar un AFND-λ equivalente a la expresión regular 0+1.

**Clasificación: AFND-λ.** Se pide explícitamente un AFND-λ equivalente a la expresión regular.

**Expresión:** `0+1`.

#### AFND-λ de Thompson de 0+1 — `L3-241`

Archivos: [`L3-241.jff`](../../automatas/lista3-afnd-lambda/L3-241.jff) · [`L3-241.json`](../../automatas/lista3-afnd-lambda/L3-241.json) · [`L3-241.xml`](../../automatas/lista3-afnd-lambda/L3-241.xml). Tipo según la definición: **AFND-lambda**, |Q| = 6, Σ = {0, 1}, 6 transiciones.

**Diseño.** Construcción de Thompson: el árbol de la expresión se recorre de abajo hacia arriba y cada operador combina los fragmentos de sus operandos (ver la tabla de reglas en este documento).

| Estado | 0 | 1 | λ |
|---|---|---|---|
| →q0 | ∅ | ∅ | {q1, q2} |
| q1 | {q3} | ∅ | ∅ |
| q3 | ∅ | ∅ | {q5} |
| q2 | ∅ | {q4} | ∅ |
| q4 | ∅ | ∅ | {q5} |
| *q5 | ∅ | ∅ | ∅ |

**Transiciones λ.** Thompson usa λ en tres lugares: dos de salida en cada unión (elegir alternativa), cuatro en cada estrella (entrar, repetir, salir, saltar) y una entre los fragmentos de cada concatenación. Ninguna consume símbolos, por eso la construcción es composicional.

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
| 1 | `0` | acepta | acepta | acepta |
| 2 | `1` | acepta | acepta | acepta |
| 3 | λ | rechaza | rechaza | rechaza |
| 4 | `10` | rechaza | rechaza | rechaza |
| 5 | `0110` | rechaza | rechaza | rechaza |
| 6 | `0000010` | rechaza | rechaza | rechaza |
| 7 | `11010111010` | rechaza | rechaza | rechaza |

Nota sobre los casos: el lenguaje solo tiene 2 palabras.

<details><summary>Recorrido completo de cada cadena</summary>

1. `0`: {q0, q1, q2} -0→ {q3, q5} — ✔
  Árbol de cómputo: 3 caminos, 1 de aceptación:
    - q0 -λ→ q1 -0→ q3 -λ→ q5 — ✔ acepta
    - q0 -λ→ q1 -0→ q3 — ✘ termina fuera de F
    - q0 -λ→ q2 — ✘ muere tras leer λ
2. `1`: {q0, q1, q2} -1→ {q4, q5} — ✔
  Árbol de cómputo: 3 caminos, 1 de aceptación:
    - q0 -λ→ q2 -1→ q4 -λ→ q5 — ✔ acepta
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 -1→ q4 — ✘ termina fuera de F
3. λ: {q0, q1, q2} — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
    - q0 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q2 — ✘ termina fuera de F
4. `10`: {q0, q1, q2} -1→ {q4, q5} -0→ ∅ — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 -1→ q4 -λ→ q5 — ✘ muere tras leer `1`
5. `0110`: {q0, q1, q2} -0→ {q3, q5} -1→ ∅ -1→ ∅ -0→ ∅ — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -λ→ q1 -0→ q3 -λ→ q5 — ✘ muere tras leer `0`
    - q0 -λ→ q2 — ✘ muere tras leer λ
6. `0000010`: {q0, q1, q2} -0→ {q3, q5} -0→ ∅ -0→ ∅ -0→ ∅ -0→ ∅ -1→ ∅ -0→ ∅ — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -λ→ q1 -0→ q3 -λ→ q5 — ✘ muere tras leer `0`
    - q0 -λ→ q2 — ✘ muere tras leer λ
7. `11010111010`: {q0, q1, q2} -1→ {q4, q5} -1→ ∅ -0→ ∅ -1→ ∅ -0→ ∅ -1→ ∅ -1→ ∅ -1→ ∅ -0→ ∅ -1→ ∅ -0→ ∅ — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 -1→ q4 -λ→ q5 — ✘ muere tras leer `1`

</details>

Simulación paso a paso en JFLAP con `0`: [ver captura](../../evidencias/jflap/pasos/L3-241.png).

**Conversión.** AFND-λ (6 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 4 estados, [`L3-241-AFND.jff`](../../automatas/conversiones/L3-241-AFND.jff). AFND (4 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 3 estados, [`L3-241-AFD.jff`](../../automatas/conversiones/L3-241-AFD.jff) ([.json](../../automatas/conversiones/L3-241-AFD.json), [.xml](../../automatas/conversiones/L3-241-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 4 estados, y el AFD mínimo (Hopcroft), 3. La cota es 2^4 = 16. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-242"></a>

## Lista 3, problema 242

**Enunciado.** Encontrar un AFND-λ equivalente a la expresión regular 0*+1.

**Clasificación: AFND-λ.** Se pide explícitamente un AFND-λ equivalente a la expresión regular.

**Expresión:** `0*+1`.

#### AFND-λ de Thompson de 0*+1 — `L3-242`

Archivos: [`L3-242.jff`](../../automatas/lista3-afnd-lambda/L3-242.jff) · [`L3-242.json`](../../automatas/lista3-afnd-lambda/L3-242.json) · [`L3-242.xml`](../../automatas/lista3-afnd-lambda/L3-242.xml). Tipo según la definición: **AFND-lambda**, |Q| = 8, Σ = {0, 1}, 10 transiciones.

**Diseño.** Construcción de Thompson: el árbol de la expresión se recorre de abajo hacia arriba y cada operador combina los fragmentos de sus operandos (ver la tabla de reglas en este documento).

| Estado | 0 | 1 | λ |
|---|---|---|---|
| →q0 | ∅ | ∅ | {q1, q2} |
| q1 | ∅ | ∅ | {q3, q4} |
| q3 | {q6} | ∅ | ∅ |
| q6 | ∅ | ∅ | {q3, q4} |
| q4 | ∅ | ∅ | {q7} |
| q2 | ∅ | {q5} | ∅ |
| q5 | ∅ | ∅ | {q7} |
| *q7 | ∅ | ∅ | ∅ |

**Transiciones λ.** Thompson usa λ en tres lugares: dos de salida en cada unión (elegir alternativa), cuatro en cada estrella (entrar, repetir, salir, saltar) y una entre los fragmentos de cada concatenación. Ninguna consume símbolos, por eso la construcción es composicional.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0, q1, q2, q3, q4, q7} | sí |
| q1 | {q1, q3, q4, q7} | sí |
| q3 | {q3} | no |
| q6 | {q3, q4, q6, q7} | sí |
| q4 | {q4, q7} | sí |
| q2 | {q2} | no |
| q5 | {q5, q7} | sí |
| q7 | {q7} | sí |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | acepta | acepta | acepta |
| 2 | `1` | acepta | acepta | acepta |
| 3 | `00` | acepta | acepta | acepta |
| 4 | `0000` | acepta | acepta | acepta |
| 5 | `00000000000` | acepta | acepta | acepta |
| 6 | `01` | rechaza | rechaza | rechaza |
| 7 | `11` | rechaza | rechaza | rechaza |
| 8 | `00001` | rechaza | rechaza | rechaza |
| 9 | `0011010` | rechaza | rechaza | rechaza |
| 10 | `10110100100` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: {q0, q1, q2, q3, q4, q7} — ✔
  Árbol de cómputo: 6 caminos, 1 de aceptación:
    - q0 -λ→ q1 -λ→ q4 -λ→ q7 — ✔ acepta
    - q0 — ✘ termina fuera de F
    - q0 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 — ✘ termina fuera de F
    - q0 -λ→ q2 — ✘ termina fuera de F
2. `1`: {q0, q1, q2, q3, q4, q7} -1→ {q5, q7} — ✔
  Árbol de cómputo: 4 caminos, 1 de aceptación:
    - q0 -λ→ q2 -1→ q5 -λ→ q7 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q7 — ✘ muere tras leer λ
    - q0 -λ→ q2 -1→ q5 — ✘ termina fuera de F
3. `00`: {q0, q1, q2, q3, q4, q7} -0→ {q3, q4, q6, q7} -0→ {q3, q4, q6, q7} — ✔
  Árbol de cómputo: 7 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q4 -λ→ q7 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q4 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q4 -λ→ q7 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q4 -λ→ q7 — ✘ muere tras leer λ
4. `0000`: {q0, q1, q2, q3, q4, q7} -0→ {q3, q4, q6, q7} -0→ {q3, q4, q6, q7} -0→ {q3, q4, q6, q7} -0→ {q3, q4, q6, q7} — ✔
  Árbol de cómputo: 9 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q4 -λ→ q7 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q4 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q4 -λ→ q7 — ✘ muere tras leer `000`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q4 -λ→ q7 — ✘ muere tras leer `00`
5. `00000000000`: {q0, q1, q2, q3, q4, q7} -0→ {q3, q4, q6, q7} -0→ {q3, q4, q6, q7} -0→ {q3, q4, q6, q7} -0→ {q3, q4, q6, q7} -0→ {q3, q4, q6, q7} -0→ {q3, q4, q6, q7} -0→ {q3, q4, q6, q7} -0→ {q3, q4, q6, q7} -0→ {q3, q4, q6, q7} -0→ {q3, q4, q6, q7} -0→ {q3, q4, q6, q7} — ✔
  Árbol de cómputo: 16 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q4 -λ→ q7 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q4 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q4 -λ→ q7 — ✘ muere tras leer `0000000000`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q4 -λ→ q7 — ✘ muere tras leer `000000000`
6. `01`: {q0, q1, q2, q3, q4, q7} -0→ {q3, q4, q6, q7} -1→ ∅ — ✘
  Árbol de cómputo: 4 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q4 -λ→ q7 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q4 -λ→ q7 — ✘ muere tras leer λ
    - q0 -λ→ q2 — ✘ muere tras leer λ
7. `11`: {q0, q1, q2, q3, q4, q7} -1→ {q5, q7} -1→ ∅ — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q7 — ✘ muere tras leer λ
    - q0 -λ→ q2 -1→ q5 -λ→ q7 — ✘ muere tras leer `1`
8. `00001`: {q0, q1, q2, q3, q4, q7} -0→ {q3, q4, q6, q7} -0→ {q3, q4, q6, q7} -0→ {q3, q4, q6, q7} -0→ {q3, q4, q6, q7} -1→ ∅ — ✘
  Árbol de cómputo: 7 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 — ✘ muere tras leer `0000`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q4 -λ→ q7 — ✘ muere tras leer `0000`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q4 -λ→ q7 — ✘ muere tras leer `000`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q4 -λ→ q7 — ✘ muere tras leer `00`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q4 -λ→ q7 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q4 -λ→ q7 — ✘ muere tras leer λ
9. `0011010`: {q0, q1, q2, q3, q4, q7} -0→ {q3, q4, q6, q7} -0→ {q3, q4, q6, q7} -1→ ∅ -1→ ∅ -0→ ∅ -1→ ∅ -0→ ∅ — ✘
  Árbol de cómputo: 5 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 — ✘ muere tras leer `00`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q4 -λ→ q7 — ✘ muere tras leer `00`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q4 -λ→ q7 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q4 -λ→ q7 — ✘ muere tras leer λ
    - q0 -λ→ q2 — ✘ muere tras leer λ
10. `10110100100`: {q0, q1, q2, q3, q4, q7} -1→ {q5, q7} -0→ ∅ -1→ ∅ -1→ ∅ -0→ ∅ -1→ ∅ -0→ ∅ -0→ ∅ -1→ ∅ -0→ ∅ -0→ ∅ — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q7 — ✘ muere tras leer λ
    - q0 -λ→ q2 -1→ q5 -λ→ q7 — ✘ muere tras leer `1`

</details>

Simulación paso a paso en JFLAP con `00`: [ver captura](../../evidencias/jflap/pasos/L3-242.png).

**Conversión.** AFND-λ (8 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 6 estados, [`L3-242-AFND.jff`](../../automatas/conversiones/L3-242-AFND.jff). AFND (6 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 3 estados, [`L3-242-AFD.jff`](../../automatas/conversiones/L3-242-AFD.jff) ([.json](../../automatas/conversiones/L3-242-AFD.json), [.xml](../../automatas/conversiones/L3-242-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 4 estados, y el AFD mínimo (Hopcroft), 4. La cota es 2^6 = 64. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-243"></a>

## Lista 3, problema 243

**Enunciado.** Encontrar un AFND-λ equivalente a la expresión regular (0+1)*.

**Clasificación: AFND-λ.** Se pide explícitamente un AFND-λ equivalente a la expresión regular.

**Expresión:** `(0+1)*`.

#### AFND-λ de Thompson de (0+1)* — `L3-243`

Archivos: [`L3-243.jff`](../../automatas/lista3-afnd-lambda/L3-243.jff) · [`L3-243.json`](../../automatas/lista3-afnd-lambda/L3-243.json) · [`L3-243.xml`](../../automatas/lista3-afnd-lambda/L3-243.xml). Tipo según la definición: **AFND-lambda**, |Q| = 8, Σ = {0, 1}, 10 transiciones.

**Diseño.** Construcción de Thompson: el árbol de la expresión se recorre de abajo hacia arriba y cada operador combina los fragmentos de sus operandos (ver la tabla de reglas en este documento).

| Estado | 0 | 1 | λ |
|---|---|---|---|
| →q0 | ∅ | ∅ | {q1, q2} |
| q1 | ∅ | ∅ | {q3, q4} |
| q3 | {q5} | ∅ | ∅ |
| q5 | ∅ | ∅ | {q7} |
| q4 | ∅ | {q6} | ∅ |
| q6 | ∅ | ∅ | {q7} |
| q7 | ∅ | ∅ | {q1, q2} |
| *q2 | ∅ | ∅ | ∅ |

**Transiciones λ.** Thompson usa λ en tres lugares: dos de salida en cada unión (elegir alternativa), cuatro en cada estrella (entrar, repetir, salir, saltar) y una entre los fragmentos de cada concatenación. Ninguna consume símbolos, por eso la construcción es composicional.

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
| 2 | `10` | acepta | acepta | acepta |
| 3 | `1101` | acepta | acepta | acepta |
| 4 | `0100000` | acepta | acepta | acepta |
| 5 | `10001011010` | acepta | acepta | acepta |
| 6 | `#` (símbolo fuera de Σ) | rechaza | rechaza | rechaza |
| 7 | `0#` (símbolo fuera de Σ) | rechaza | rechaza | rechaza |
| 8 | `#11` (símbolo fuera de Σ) | rechaza | rechaza | rechaza |

Nota sobre los casos: todas las cadenas sobre Σ pertenecen al lenguaje, así que las inválidas usan un símbolo fuera de Σ (#).

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: {q0, q1, q2, q3, q4} — ✔
  Árbol de cómputo: 5 caminos, 1 de aceptación:
    - q0 -λ→ q2 — ✔ acepta
    - q0 — ✘ termina fuera de F
    - q0 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 — ✘ termina fuera de F
2. `10`: {q0, q1, q2, q3, q4} -1→ {q1, q2, q3, q4, q6, q7} -0→ {q1, q2, q3, q4, q5, q7} — ✔
  Árbol de cómputo: 10 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q4 -1→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q2 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -1→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -1→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -1→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -1→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q3 — ✘ termina fuera de F
3. `1101`: {q0, q1, q2, q3, q4} -1→ {q1, q2, q3, q4, q6, q7} -1→ {q1, q2, q3, q4, q6, q7} -0→ {q1, q2, q3, q4, q5, q7} -1→ {q1, q2, q3, q4, q6, q7} — ✔
  Árbol de cómputo: 14 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q4 -1→ q6 -λ→ q7 -λ→ q1 -λ→ q4 -1→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q4 -1→ q6 -λ→ q7 -λ→ q2 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -1→ q6 -λ→ q7 -λ→ q1 -λ→ q3 — ✘ muere tras leer `1`
    - q0 -λ→ q1 -λ→ q4 -1→ q6 -λ→ q7 -λ→ q1 -λ→ q4 -1→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q3 — ✘ muere tras leer `110`
    - q0 -λ→ q1 -λ→ q4 -1→ q6 -λ→ q7 -λ→ q1 -λ→ q4 -1→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q4 -1→ q6 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -1→ q6 -λ→ q7 -λ→ q1 -λ→ q4 -1→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q4 -1→ q6 -λ→ q7 — ✘ termina fuera de F
4. `0100000`: {q0, q1, q2, q3, q4} -0→ {q1, q2, q3, q4, q5, q7} -1→ {q1, q2, q3, q4, q6, q7} -0→ {q1, q2, q3, q4, q5, q7} -0→ {q1, q2, q3, q4, q5, q7} -0→ {q1, q2, q3, q4, q5, q7} -0→ {q1, q2, q3, q4, q5, q7} -0→ {q1, q2, q3, q4, q5, q7} — ✔
  Árbol de cómputo: 20 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q4 -1→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q2 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q3 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q4 -1→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q4 -1→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q4 -1→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q4 -1→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q3 — ✘ termina fuera de F
5. `10001011010`: {q0, q1, q2, q3, q4} -1→ {q1, q2, q3, q4, q6, q7} -0→ {q1, q2, q3, q4, q5, q7} -0→ {q1, q2, q3, q4, q5, q7} -0→ {q1, q2, q3, q4, q5, q7} -1→ {q1, q2, q3, q4, q6, q7} -0→ {q1, q2, q3, q4, q5, q7} -1→ {q1, q2, q3, q4, q6, q7} -1→ {q1, q2, q3, q4, q6, q7} -0→ {q1, q2, q3, q4, q5, q7} -1→ {q1, q2, q3, q4, q6, q7} -0→ {q1, q2, q3, q4, q5, q7} — ✔
  Árbol de cómputo: 28 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q4 -1→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q4 -1→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q4 -1→ q6 -λ→ q7 -λ→ q1 -λ→ q4 -1→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q4 -1→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q2 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -1→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q3 — ✘ muere tras leer `1000`
    - q0 -λ→ q1 -λ→ q4 -1→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q4 -1→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q3 — ✘ muere tras leer `100010`
    - q0 -λ→ q1 -λ→ q4 -1→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q4 -1→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q4 -1→ q6 -λ→ q7 -λ→ q1 -λ→ q3 — ✘ muere tras leer `1000101`
    - q0 -λ→ q1 -λ→ q4 -1→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q4 -1→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q4 -1→ q6 -λ→ q7 -λ→ q1 -λ→ q4 -1→ q6 -λ→ q7 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q3 — ✘ muere tras leer `100010110`
6. `#`: {q0, q1, q2, q3, q4} -#→ ∅ — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 — ✘ muere tras leer λ
    - q0 -λ→ q2 — ✘ muere tras leer λ
7. `0#`: {q0, q1, q2, q3, q4} -0→ {q1, q2, q3, q4, q5, q7} -#→ ∅ — ✘
  Árbol de cómputo: 5 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q3 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q1 -λ→ q4 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q3 -0→ q5 -λ→ q7 -λ→ q2 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q4 — ✘ muere tras leer λ
    - q0 -λ→ q2 — ✘ muere tras leer λ
8. `#11`: {q0, q1, q2, q3, q4} -#→ ∅ -1→ ∅ -1→ ∅ — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 — ✘ muere tras leer λ
    - q0 -λ→ q2 — ✘ muere tras leer λ

</details>

Simulación paso a paso en JFLAP con `10`: [ver captura](../../evidencias/jflap/pasos/L3-243.png).

**Conversión.** AFND-λ (8 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 8 estados, [`L3-243-AFND.jff`](../../automatas/conversiones/L3-243-AFND.jff). AFND (8 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 3 estados, [`L3-243-AFD.jff`](../../automatas/conversiones/L3-243-AFD.jff) ([.json](../../automatas/conversiones/L3-243-AFD.json), [.xml](../../automatas/conversiones/L3-243-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 3 estados, y el AFD mínimo (Hopcroft), 1. La cota es 2^8 = 256. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-244"></a>

## Lista 3, problema 244

**Enunciado.** Encontrar un AFND-λ equivalente a la expresión regular 0(0+1).

**Clasificación: AFND-λ.** Se pide explícitamente un AFND-λ equivalente a la expresión regular.

**Expresión:** `0(0+1)`.

#### AFND-λ de Thompson de 0(0+1) — `L3-244`

Archivos: [`L3-244.jff`](../../automatas/lista3-afnd-lambda/L3-244.jff) · [`L3-244.json`](../../automatas/lista3-afnd-lambda/L3-244.json) · [`L3-244.xml`](../../automatas/lista3-afnd-lambda/L3-244.xml). Tipo según la definición: **AFND-lambda**, |Q| = 8, Σ = {0, 1}, 8 transiciones.

**Diseño.** Construcción de Thompson: el árbol de la expresión se recorre de abajo hacia arriba y cada operador combina los fragmentos de sus operandos (ver la tabla de reglas en este documento).

| Estado | 0 | 1 | λ |
|---|---|---|---|
| →q0 | {q1} | ∅ | ∅ |
| q1 | ∅ | ∅ | {q2} |
| q2 | ∅ | ∅ | {q3, q4} |
| q3 | {q5} | ∅ | ∅ |
| q5 | ∅ | ∅ | {q7} |
| q4 | ∅ | {q6} | ∅ |
| q6 | ∅ | ∅ | {q7} |
| *q7 | ∅ | ∅ | ∅ |

**Transiciones λ.** Thompson usa λ en tres lugares: dos de salida en cada unión (elegir alternativa), cuatro en cada estrella (entrar, repetir, salir, saltar) y una entre los fragmentos de cada concatenación. Ninguna consume símbolos, por eso la construcción es composicional.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0} | no |
| q1 | {q1, q2, q3, q4} | no |
| q2 | {q2, q3, q4} | no |
| q3 | {q3} | no |
| q5 | {q5, q7} | sí |
| q4 | {q4} | no |
| q6 | {q6, q7} | sí |
| q7 | {q7} | sí |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `00` | acepta | acepta | acepta |
| 2 | `01` | acepta | acepta | acepta |
| 3 | λ | rechaza | rechaza | rechaza |
| 4 | `000` | rechaza | rechaza | rechaza |
| 5 | `1110` | rechaza | rechaza | rechaza |
| 6 | `0111100` | rechaza | rechaza | rechaza |
| 7 | `01001110110` | rechaza | rechaza | rechaza |

Nota sobre los casos: el lenguaje solo tiene 2 palabras.

<details><summary>Recorrido completo de cada cadena</summary>

1. `00`: {q0} -0→ {q1, q2, q3, q4} -0→ {q5, q7} — ✔
  Árbol de cómputo: 3 caminos, 1 de aceptación:
    - q0 -0→ q1 -λ→ q2 -λ→ q3 -0→ q5 -λ→ q7 — ✔ acepta
    - q0 -0→ q1 -λ→ q2 -λ→ q3 -0→ q5 — ✘ termina fuera de F
    - q0 -0→ q1 -λ→ q2 -λ→ q4 — ✘ muere tras leer `0`
2. `01`: {q0} -0→ {q1, q2, q3, q4} -1→ {q6, q7} — ✔
  Árbol de cómputo: 3 caminos, 1 de aceptación:
    - q0 -0→ q1 -λ→ q2 -λ→ q4 -1→ q6 -λ→ q7 — ✔ acepta
    - q0 -0→ q1 -λ→ q2 -λ→ q3 — ✘ muere tras leer `0`
    - q0 -0→ q1 -λ→ q2 -λ→ q4 -1→ q6 — ✘ termina fuera de F
3. λ: {q0} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
4. `000`: {q0} -0→ {q1, q2, q3, q4} -0→ {q5, q7} -0→ ∅ — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -0→ q1 -λ→ q2 -λ→ q3 -0→ q5 -λ→ q7 — ✘ muere tras leer `00`
    - q0 -0→ q1 -λ→ q2 -λ→ q4 — ✘ muere tras leer `0`
5. `1110`: {q0} -1→ ∅ -1→ ∅ -1→ ∅ -0→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ
6. `0111100`: {q0} -0→ {q1, q2, q3, q4} -1→ {q6, q7} -1→ ∅ -1→ ∅ -1→ ∅ -0→ ∅ -0→ ∅ — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -0→ q1 -λ→ q2 -λ→ q3 — ✘ muere tras leer `0`
    - q0 -0→ q1 -λ→ q2 -λ→ q4 -1→ q6 -λ→ q7 — ✘ muere tras leer `01`
7. `01001110110`: {q0} -0→ {q1, q2, q3, q4} -1→ {q6, q7} -0→ ∅ -0→ ∅ -1→ ∅ -1→ ∅ -1→ ∅ -0→ ∅ -1→ ∅ -1→ ∅ -0→ ∅ — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - q0 -0→ q1 -λ→ q2 -λ→ q3 — ✘ muere tras leer `0`
    - q0 -0→ q1 -λ→ q2 -λ→ q4 -1→ q6 -λ→ q7 — ✘ muere tras leer `01`

</details>

Simulación paso a paso en JFLAP con `00`: [ver captura](../../evidencias/jflap/pasos/L3-244.png).

**Conversión.** AFND-λ (8 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 8 estados, [`L3-244-AFND.jff`](../../automatas/conversiones/L3-244-AFND.jff). AFND (8 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 4 estados, [`L3-244-AFD.jff`](../../automatas/conversiones/L3-244-AFD.jff) ([.json](../../automatas/conversiones/L3-244-AFD.json), [.xml](../../automatas/conversiones/L3-244-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 5 estados, y el AFD mínimo (Hopcroft), 4. La cota es 2^8 = 256. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-245"></a>

## Lista 3, problema 245

**Enunciado.** Encontrar un AFND-λ equivalente a la expresión regular 0(0+1)*.

**Clasificación: AFND-λ.** Se pide explícitamente un AFND-λ equivalente a la expresión regular.

**Expresión:** `0(0+1)*`.

#### AFND-λ de Thompson de 0(0+1)* — `L3-245`

Archivos: [`L3-245.jff`](../../automatas/lista3-afnd-lambda/L3-245.jff) · [`L3-245.json`](../../automatas/lista3-afnd-lambda/L3-245.json) · [`L3-245.xml`](../../automatas/lista3-afnd-lambda/L3-245.xml). Tipo según la definición: **AFND-lambda**, |Q| = 10, Σ = {0, 1}, 12 transiciones.

**Diseño.** Construcción de Thompson: el árbol de la expresión se recorre de abajo hacia arriba y cada operador combina los fragmentos de sus operandos (ver la tabla de reglas en este documento).

| Estado | 0 | 1 | λ |
|---|---|---|---|
| →q0 | {q1} | ∅ | ∅ |
| q1 | ∅ | ∅ | {q2} |
| q2 | ∅ | ∅ | {q3, q4} |
| q3 | ∅ | ∅ | {q5, q6} |
| q5 | {q7} | ∅ | ∅ |
| q7 | ∅ | ∅ | {q9} |
| q6 | ∅ | {q8} | ∅ |
| q8 | ∅ | ∅ | {q9} |
| q9 | ∅ | ∅ | {q3, q4} |
| *q4 | ∅ | ∅ | ∅ |

**Transiciones λ.** Thompson usa λ en tres lugares: dos de salida en cada unión (elegir alternativa), cuatro en cada estrella (entrar, repetir, salir, saltar) y una entre los fragmentos de cada concatenación. Ninguna consume símbolos, por eso la construcción es composicional.

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
| 1 | `0` | acepta | acepta | acepta |
| 2 | `00` | acepta | acepta | acepta |
| 3 | `0010` | acepta | acepta | acepta |
| 4 | `0111000` | acepta | acepta | acepta |
| 5 | `00101100111` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `10` | rechaza | rechaza | rechaza |
| 8 | `1001` | rechaza | rechaza | rechaza |
| 9 | `1010011` | rechaza | rechaza | rechaza |
| 10 | `11001001100` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `0`: {q0} -0→ {q1, q2, q3, q4, q5, q6} — ✔
  Árbol de cómputo: 6 caminos, 1 de aceptación:
    - q0 -0→ q1 -λ→ q2 -λ→ q4 — ✔ acepta
    - q0 -0→ q1 — ✘ termina fuera de F
    - q0 -0→ q1 -λ→ q2 — ✘ termina fuera de F
    - q0 -0→ q1 -λ→ q2 -λ→ q3 — ✘ termina fuera de F
    - q0 -0→ q1 -λ→ q2 -λ→ q3 -λ→ q5 — ✘ termina fuera de F
    - q0 -0→ q1 -λ→ q2 -λ→ q3 -λ→ q6 — ✘ termina fuera de F
2. `00`: {q0} -0→ {q1, q2, q3, q4, q5, q6} -0→ {q3, q4, q5, q6, q7, q9} — ✔
  Árbol de cómputo: 8 caminos, 1 de aceptación (se muestran 6):
    - q0 -0→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -0→ q7 -λ→ q9 -λ→ q4 — ✔ acepta
    - q0 -0→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -0→ q7 — ✘ termina fuera de F
    - q0 -0→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -0→ q7 -λ→ q9 — ✘ termina fuera de F
    - q0 -0→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -0→ q7 -λ→ q9 -λ→ q3 — ✘ termina fuera de F
    - q0 -0→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -0→ q7 -λ→ q9 -λ→ q3 -λ→ q5 — ✘ termina fuera de F
    - q0 -0→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -0→ q7 -λ→ q9 -λ→ q3 -λ→ q6 — ✘ termina fuera de F
3. `0010`: {q0} -0→ {q1, q2, q3, q4, q5, q6} -0→ {q3, q4, q5, q6, q7, q9} -1→ {q3, q4, q5, q6, q8, q9} -0→ {q3, q4, q5, q6, q7, q9} — ✔
  Árbol de cómputo: 12 caminos, 1 de aceptación (se muestran 6):
    - q0 -0→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -0→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -1→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -0→ q7 -λ→ q9 -λ→ q4 — ✔ acepta
    - q0 -0→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -0→ q7 -λ→ q9 -λ→ q3 -λ→ q5 — ✘ muere tras leer `00`
    - q0 -0→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -0→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -1→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -0→ q7 — ✘ termina fuera de F
    - q0 -0→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -0→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -1→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -0→ q7 -λ→ q9 — ✘ termina fuera de F
    - q0 -0→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -0→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -1→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -0→ q7 -λ→ q9 -λ→ q3 — ✘ termina fuera de F
    - q0 -0→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -0→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -1→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -0→ q7 -λ→ q9 -λ→ q3 -λ→ q5 — ✘ termina fuera de F
4. `0111000`: {q0} -0→ {q1, q2, q3, q4, q5, q6} -1→ {q3, q4, q5, q6, q8, q9} -1→ {q3, q4, q5, q6, q8, q9} -1→ {q3, q4, q5, q6, q8, q9} -0→ {q3, q4, q5, q6, q7, q9} -0→ {q3, q4, q5, q6, q7, q9} -0→ {q3, q4, q5, q6, q7, q9} — ✔
  Árbol de cómputo: 18 caminos, 1 de aceptación (se muestran 6):
    - q0 -0→ q1 -λ→ q2 -λ→ q3 -λ→ q6 -1→ q8 -λ→ q9 -λ→ q3 -λ→ q6 -1→ q8 -λ→ q9 -λ→ q3 -λ→ q6 -1→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -0→ q7 -λ→ q9 -λ→ q3 -λ→ q5 -0→ q7 -λ→ q9 -λ→ q3 -λ→ q5 -0→ q7 -λ→ q9 -λ→ q4 — ✔ acepta
    - q0 -0→ q1 -λ→ q2 -λ→ q3 -λ→ q5 — ✘ muere tras leer `0`
    - q0 -0→ q1 -λ→ q2 -λ→ q3 -λ→ q6 -1→ q8 -λ→ q9 -λ→ q3 -λ→ q5 — ✘ muere tras leer `01`
    - q0 -0→ q1 -λ→ q2 -λ→ q3 -λ→ q6 -1→ q8 -λ→ q9 -λ→ q3 -λ→ q6 -1→ q8 -λ→ q9 -λ→ q3 -λ→ q5 — ✘ muere tras leer `011`
    - q0 -0→ q1 -λ→ q2 -λ→ q3 -λ→ q6 -1→ q8 -λ→ q9 -λ→ q3 -λ→ q6 -1→ q8 -λ→ q9 -λ→ q3 -λ→ q6 -1→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -0→ q7 -λ→ q9 -λ→ q3 -λ→ q5 -0→ q7 -λ→ q9 -λ→ q3 -λ→ q5 -0→ q7 — ✘ termina fuera de F
    - q0 -0→ q1 -λ→ q2 -λ→ q3 -λ→ q6 -1→ q8 -λ→ q9 -λ→ q3 -λ→ q6 -1→ q8 -λ→ q9 -λ→ q3 -λ→ q6 -1→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -0→ q7 -λ→ q9 -λ→ q3 -λ→ q5 -0→ q7 -λ→ q9 -λ→ q3 -λ→ q5 -0→ q7 -λ→ q9 — ✘ termina fuera de F
5. `00101100111`: {q0} -0→ {q1, q2, q3, q4, q5, q6} -0→ {q3, q4, q5, q6, q7, q9} -1→ {q3, q4, q5, q6, q8, q9} -0→ {q3, q4, q5, q6, q7, q9} -1→ {q3, q4, q5, q6, q8, q9} -1→ {q3, q4, q5, q6, q8, q9} -0→ {q3, q4, q5, q6, q7, q9} -0→ {q3, q4, q5, q6, q7, q9} -1→ {q3, q4, q5, q6, q8, q9} -1→ {q3, q4, q5, q6, q8, q9} -1→ {q3, q4, q5, q6, q8, q9} — ✔
  Árbol de cómputo: 26 caminos, 1 de aceptación (se muestran 6):
    - q0 -0→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -0→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -1→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -0→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -1→ q8 -λ→ q9 -λ→ q3 -λ→ q6 -1→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -0→ q7 -λ→ q9 -λ→ q3 -λ→ q5 -0→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -1→ q8 -λ→ q9 -λ→ q3 -λ→ q6 -1→ q8 -λ→ q9 -λ→ q3 -λ→ q6 -1→ q8 -λ→ q9 -λ→ q4 — ✔ acepta
    - q0 -0→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -0→ q7 -λ→ q9 -λ→ q3 -λ→ q5 — ✘ muere tras leer `00`
    - q0 -0→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -0→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -1→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -0→ q7 -λ→ q9 -λ→ q3 -λ→ q5 — ✘ muere tras leer `0010`
    - q0 -0→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -0→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -1→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -0→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -1→ q8 -λ→ q9 -λ→ q3 -λ→ q5 — ✘ muere tras leer `00101`
    - q0 -0→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -0→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -1→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -0→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -1→ q8 -λ→ q9 -λ→ q3 -λ→ q6 -1→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -0→ q7 -λ→ q9 -λ→ q3 -λ→ q5 -0→ q7 -λ→ q9 -λ→ q3 -λ→ q5 — ✘ muere tras leer `00101100`
    - q0 -0→ q1 -λ→ q2 -λ→ q3 -λ→ q5 -0→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -1→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -0→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -1→ q8 -λ→ q9 -λ→ q3 -λ→ q6 -1→ q8 -λ→ q9 -λ→ q3 -λ→ q5 -0→ q7 -λ→ q9 -λ→ q3 -λ→ q5 -0→ q7 -λ→ q9 -λ→ q3 -λ→ q6 -1→ q8 -λ→ q9 -λ→ q3 -λ→ q5 — ✘ muere tras leer `001011001`
6. λ: {q0} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
7. `10`: {q0} -1→ ∅ -0→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ
8. `1001`: {q0} -1→ ∅ -0→ ∅ -0→ ∅ -1→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ
9. `1010011`: {q0} -1→ ∅ -0→ ∅ -1→ ∅ -0→ ∅ -0→ ∅ -1→ ∅ -1→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ
10. `11001001100`: {q0} -1→ ∅ -1→ ∅ -0→ ∅ -0→ ∅ -1→ ∅ -0→ ∅ -0→ ∅ -1→ ∅ -1→ ∅ -0→ ∅ -0→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ

</details>

Simulación paso a paso en JFLAP con `00`: [ver captura](../../evidencias/jflap/pasos/L3-245.png).

**Conversión.** AFND-λ (10 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 10 estados, [`L3-245-AFND.jff`](../../automatas/conversiones/L3-245-AFND.jff). AFND (10 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 4 estados, [`L3-245-AFD.jff`](../../automatas/conversiones/L3-245-AFD.jff) ([.json](../../automatas/conversiones/L3-245-AFD.json), [.xml](../../automatas/conversiones/L3-245-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 5 estados, y el AFD mínimo (Hopcroft), 3. La cota es 2^10 = 1024. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-246"></a>

## Lista 3, problema 246

**Enunciado.** Encontrar un AFND-λ equivalente a la expresión regular 0*(0+1).

**Clasificación: AFND-λ.** Se pide explícitamente un AFND-λ equivalente a la expresión regular.

**Expresión:** `0*(0+1)`.

#### AFND-λ de Thompson de 0*(0+1) — `L3-246`

Archivos: [`L3-246.jff`](../../automatas/lista3-afnd-lambda/L3-246.jff) · [`L3-246.json`](../../automatas/lista3-afnd-lambda/L3-246.json) · [`L3-246.xml`](../../automatas/lista3-afnd-lambda/L3-246.xml). Tipo según la definición: **AFND-lambda**, |Q| = 10, Σ = {0, 1}, 12 transiciones.

**Diseño.** Construcción de Thompson: el árbol de la expresión se recorre de abajo hacia arriba y cada operador combina los fragmentos de sus operandos (ver la tabla de reglas en este documento).

| Estado | 0 | 1 | λ |
|---|---|---|---|
| →q0 | ∅ | ∅ | {q1, q2} |
| q1 | {q3} | ∅ | ∅ |
| q3 | ∅ | ∅ | {q1, q2} |
| q2 | ∅ | ∅ | {q4} |
| q4 | ∅ | ∅ | {q5, q6} |
| q5 | {q7} | ∅ | ∅ |
| q7 | ∅ | ∅ | {q9} |
| q6 | ∅ | {q8} | ∅ |
| q8 | ∅ | ∅ | {q9} |
| *q9 | ∅ | ∅ | ∅ |

**Transiciones λ.** Thompson usa λ en tres lugares: dos de salida en cada unión (elegir alternativa), cuatro en cada estrella (entrar, repetir, salir, saltar) y una entre los fragmentos de cada concatenación. Ninguna consume símbolos, por eso la construcción es composicional.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0, q1, q2, q4, q5, q6} | no |
| q1 | {q1} | no |
| q3 | {q1, q2, q3, q4, q5, q6} | no |
| q2 | {q2, q4, q5, q6} | no |
| q4 | {q4, q5, q6} | no |
| q5 | {q5} | no |
| q7 | {q7, q9} | sí |
| q6 | {q6} | no |
| q8 | {q8, q9} | sí |
| q9 | {q9} | sí |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `1` | acepta | acepta | acepta |
| 2 | `01` | acepta | acepta | acepta |
| 3 | `001` | acepta | acepta | acepta |
| 4 | `0001` | acepta | acepta | acepta |
| 5 | `00001` | acepta | acepta | — |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `10` | rechaza | rechaza | — |
| 8 | `1010` | rechaza | rechaza | — |
| 9 | `0110100` | rechaza | rechaza | — |
| 10 | `00110101001` | rechaza | rechaza | — |

<details><summary>Recorrido completo de cada cadena</summary>

1. `1`: {q0, q1, q2, q4, q5, q6} -1→ {q8, q9} — ✔
  Árbol de cómputo: 4 caminos, 1 de aceptación:
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 -1→ q8 -λ→ q9 — ✔ acepta
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q4 -λ→ q5 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 -1→ q8 — ✘ termina fuera de F
2. `01`: {q0, q1, q2, q4, q5, q6} -0→ {q1, q2, q3, q4, q5, q6, q7, q9} -1→ {q8, q9} — ✔
  Árbol de cómputo: 6 caminos, 1 de aceptación:
    - q0 -λ→ q1 -0→ q3 -λ→ q2 -λ→ q4 -λ→ q6 -1→ q8 -λ→ q9 — ✔ acepta
    - q0 -λ→ q1 -0→ q3 -λ→ q1 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -0→ q3 -λ→ q2 -λ→ q4 -λ→ q5 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -0→ q3 -λ→ q2 -λ→ q4 -λ→ q6 -1→ q8 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q4 -λ→ q5 -0→ q7 -λ→ q9 — ✘ muere tras leer `0`
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 — ✘ muere tras leer λ
3. `001`: {q0, q1, q2, q4, q5, q6} -0→ {q1, q2, q3, q4, q5, q6, q7, q9} -0→ {q1, q2, q3, q4, q5, q6, q7, q9} -1→ {q8, q9} — ✔
  Árbol de cómputo: 8 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -0→ q3 -λ→ q1 -0→ q3 -λ→ q2 -λ→ q4 -λ→ q6 -1→ q8 -λ→ q9 — ✔ acepta
    - q0 -λ→ q1 -0→ q3 -λ→ q1 -0→ q3 -λ→ q1 — ✘ muere tras leer `00`
    - q0 -λ→ q1 -0→ q3 -λ→ q1 -0→ q3 -λ→ q2 -λ→ q4 -λ→ q5 — ✘ muere tras leer `00`
    - q0 -λ→ q1 -0→ q3 -λ→ q1 -0→ q3 -λ→ q2 -λ→ q4 -λ→ q6 -1→ q8 — ✘ termina fuera de F
    - q0 -λ→ q1 -0→ q3 -λ→ q2 -λ→ q4 -λ→ q5 -0→ q7 -λ→ q9 — ✘ muere tras leer `00`
    - q0 -λ→ q1 -0→ q3 -λ→ q2 -λ→ q4 -λ→ q6 — ✘ muere tras leer `0`
4. `0001`: {q0, q1, q2, q4, q5, q6} -0→ {q1, q2, q3, q4, q5, q6, q7, q9} -0→ {q1, q2, q3, q4, q5, q6, q7, q9} -0→ {q1, q2, q3, q4, q5, q6, q7, q9} -1→ {q8, q9} — ✔
  Árbol de cómputo: 10 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -0→ q3 -λ→ q1 -0→ q3 -λ→ q1 -0→ q3 -λ→ q2 -λ→ q4 -λ→ q6 -1→ q8 -λ→ q9 — ✔ acepta
    - q0 -λ→ q1 -0→ q3 -λ→ q1 -0→ q3 -λ→ q1 -0→ q3 -λ→ q1 — ✘ muere tras leer `000`
    - q0 -λ→ q1 -0→ q3 -λ→ q1 -0→ q3 -λ→ q1 -0→ q3 -λ→ q2 -λ→ q4 -λ→ q5 — ✘ muere tras leer `000`
    - q0 -λ→ q1 -0→ q3 -λ→ q1 -0→ q3 -λ→ q1 -0→ q3 -λ→ q2 -λ→ q4 -λ→ q6 -1→ q8 — ✘ termina fuera de F
    - q0 -λ→ q1 -0→ q3 -λ→ q1 -0→ q3 -λ→ q2 -λ→ q4 -λ→ q5 -0→ q7 -λ→ q9 — ✘ muere tras leer `000`
    - q0 -λ→ q1 -0→ q3 -λ→ q1 -0→ q3 -λ→ q2 -λ→ q4 -λ→ q6 — ✘ muere tras leer `00`
5. `00001`: {q0, q1, q2, q4, q5, q6} -0→ {q1, q2, q3, q4, q5, q6, q7, q9} -0→ {q1, q2, q3, q4, q5, q6, q7, q9} -0→ {q1, q2, q3, q4, q5, q6, q7, q9} -0→ {q1, q2, q3, q4, q5, q6, q7, q9} -1→ {q8, q9} — ✔
  Árbol de cómputo: 12 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -0→ q3 -λ→ q1 -0→ q3 -λ→ q1 -0→ q3 -λ→ q1 -0→ q3 -λ→ q2 -λ→ q4 -λ→ q6 -1→ q8 -λ→ q9 — ✔ acepta
    - q0 -λ→ q1 -0→ q3 -λ→ q1 -0→ q3 -λ→ q1 -0→ q3 -λ→ q1 -0→ q3 -λ→ q1 — ✘ muere tras leer `0000`
    - q0 -λ→ q1 -0→ q3 -λ→ q1 -0→ q3 -λ→ q1 -0→ q3 -λ→ q1 -0→ q3 -λ→ q2 -λ→ q4 -λ→ q5 — ✘ muere tras leer `0000`
    - q0 -λ→ q1 -0→ q3 -λ→ q1 -0→ q3 -λ→ q1 -0→ q3 -λ→ q1 -0→ q3 -λ→ q2 -λ→ q4 -λ→ q6 -1→ q8 — ✘ termina fuera de F
    - q0 -λ→ q1 -0→ q3 -λ→ q1 -0→ q3 -λ→ q1 -0→ q3 -λ→ q2 -λ→ q4 -λ→ q5 -0→ q7 -λ→ q9 — ✘ muere tras leer `0000`
    - q0 -λ→ q1 -0→ q3 -λ→ q1 -0→ q3 -λ→ q1 -0→ q3 -λ→ q2 -λ→ q4 -λ→ q6 — ✘ muere tras leer `000`
6. λ: {q0, q1, q2, q4, q5, q6} — ✘
  Árbol de cómputo: 6 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
    - q0 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q2 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q4 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q4 -λ→ q5 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 — ✘ termina fuera de F
7. `10`: {q0, q1, q2, q4, q5, q6} -1→ {q8, q9} -0→ ∅ — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q4 -λ→ q5 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 -1→ q8 -λ→ q9 — ✘ muere tras leer `1`
8. `1010`: {q0, q1, q2, q4, q5, q6} -1→ {q8, q9} -0→ ∅ -1→ ∅ -0→ ∅ — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q4 -λ→ q5 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 -1→ q8 -λ→ q9 — ✘ muere tras leer `1`
9. `0110100`: {q0, q1, q2, q4, q5, q6} -0→ {q1, q2, q3, q4, q5, q6, q7, q9} -1→ {q8, q9} -1→ ∅ -0→ ∅ -1→ ∅ -0→ ∅ -0→ ∅ — ✘
  Árbol de cómputo: 5 caminos, 0 de aceptación:
    - q0 -λ→ q1 -0→ q3 -λ→ q1 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -0→ q3 -λ→ q2 -λ→ q4 -λ→ q5 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -0→ q3 -λ→ q2 -λ→ q4 -λ→ q6 -1→ q8 -λ→ q9 — ✘ muere tras leer `01`
    - q0 -λ→ q2 -λ→ q4 -λ→ q5 -0→ q7 -λ→ q9 — ✘ muere tras leer `0`
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 — ✘ muere tras leer λ
10. `00110101001`: {q0, q1, q2, q4, q5, q6} -0→ {q1, q2, q3, q4, q5, q6, q7, q9} -0→ {q1, q2, q3, q4, q5, q6, q7, q9} -1→ {q8, q9} -1→ ∅ -0→ ∅ -1→ ∅ -0→ ∅ -1→ ∅ -0→ ∅ -0→ ∅ -1→ ∅ — ✘
  Árbol de cómputo: 7 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -0→ q3 -λ→ q1 -0→ q3 -λ→ q1 — ✘ muere tras leer `00`
    - q0 -λ→ q1 -0→ q3 -λ→ q1 -0→ q3 -λ→ q2 -λ→ q4 -λ→ q5 — ✘ muere tras leer `00`
    - q0 -λ→ q1 -0→ q3 -λ→ q1 -0→ q3 -λ→ q2 -λ→ q4 -λ→ q6 -1→ q8 -λ→ q9 — ✘ muere tras leer `001`
    - q0 -λ→ q1 -0→ q3 -λ→ q2 -λ→ q4 -λ→ q5 -0→ q7 -λ→ q9 — ✘ muere tras leer `00`
    - q0 -λ→ q1 -0→ q3 -λ→ q2 -λ→ q4 -λ→ q6 — ✘ muere tras leer `0`
    - q0 -λ→ q2 -λ→ q4 -λ→ q5 -0→ q7 -λ→ q9 — ✘ muere tras leer `0`

</details>

Simulación paso a paso en JFLAP con `01`: [ver captura](../../evidencias/jflap/pasos/L3-246.png).

**Conversión.** AFND-λ (10 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 10 estados, [`L3-246-AFND.jff`](../../automatas/conversiones/L3-246-AFND.jff). AFND (10 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 3 estados, [`L3-246-AFD.jff`](../../automatas/conversiones/L3-246-AFD.jff) ([.json](../../automatas/conversiones/L3-246-AFD.json), [.xml](../../automatas/conversiones/L3-246-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 4 estados, y el AFD mínimo (Hopcroft), 4. La cota es 2^10 = 1024. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-247"></a>

## Lista 3, problema 247

**Enunciado.** Encontrar un AFND-λ equivalente a la expresión regular (01)*+1*.

**Clasificación: AFND-λ.** Se pide explícitamente un AFND-λ equivalente a la expresión regular.

**Expresión:** `(01)*+1*`.

#### AFND-λ de Thompson de (01)*+1* — `L3-247`

Archivos: [`L3-247.jff`](../../automatas/lista3-afnd-lambda/L3-247.jff) · [`L3-247.json`](../../automatas/lista3-afnd-lambda/L3-247.json) · [`L3-247.xml`](../../automatas/lista3-afnd-lambda/L3-247.xml). Tipo según la definición: **AFND-lambda**, |Q| = 12, Σ = {0, 1}, 16 transiciones.

**Diseño.** Construcción de Thompson: el árbol de la expresión se recorre de abajo hacia arriba y cada operador combina los fragmentos de sus operandos (ver la tabla de reglas en este documento).

| Estado | 0 | 1 | λ |
|---|---|---|---|
| →q0 | ∅ | ∅ | {q1, q2} |
| q1 | ∅ | ∅ | {q3, q4} |
| q3 | {q7} | ∅ | ∅ |
| q7 | ∅ | ∅ | {q10} |
| q10 | ∅ | {q11} | ∅ |
| q11 | ∅ | ∅ | {q3, q4} |
| q4 | ∅ | ∅ | {q8} |
| q2 | ∅ | ∅ | {q5, q6} |
| q6 | ∅ | {q9} | ∅ |
| q9 | ∅ | ∅ | {q5, q6} |
| q5 | ∅ | ∅ | {q8} |
| *q8 | ∅ | ∅ | ∅ |

**Transiciones λ.** Thompson usa λ en tres lugares: dos de salida en cada unión (elegir alternativa), cuatro en cada estrella (entrar, repetir, salir, saltar) y una entre los fragmentos de cada concatenación. Ninguna consume símbolos, por eso la construcción es composicional.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0, q1, q2, q3, q4, q5, q6, q8} | sí |
| q1 | {q1, q3, q4, q8} | sí |
| q3 | {q3} | no |
| q7 | {q10, q7} | no |
| q10 | {q10} | no |
| q11 | {q11, q3, q4, q8} | sí |
| q4 | {q4, q8} | sí |
| q2 | {q2, q5, q6, q8} | sí |
| q6 | {q6} | no |
| q9 | {q5, q6, q8, q9} | sí |
| q5 | {q5, q8} | sí |
| q8 | {q8} | sí |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | acepta | acepta | acepta |
| 2 | `01` | acepta | acepta | acepta |
| 3 | `1111` | acepta | acepta | acepta |
| 4 | `01010101` | acepta | acepta | acepta |
| 5 | `010101010101` | acepta | acepta | acepta |
| 6 | `0` | rechaza | rechaza | rechaza |
| 7 | `00` | rechaza | rechaza | rechaza |
| 8 | `1110` | rechaza | rechaza | rechaza |
| 9 | `1101001` | rechaza | rechaza | rechaza |
| 10 | `11010000101` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: {q0, q1, q2, q3, q4, q5, q6, q8} — ✔
  Árbol de cómputo: 9 caminos, 2 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 — ✔ acepta
    - q0 -λ→ q2 -λ→ q5 -λ→ q8 — ✔ acepta
    - q0 — ✘ termina fuera de F
    - q0 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 — ✘ termina fuera de F
2. `01`: {q0, q1, q2, q3, q4, q5, q6, q8} -0→ {q10, q7} -1→ {q11, q3, q4, q8} — ✔
  Árbol de cómputo: 7 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q4 -λ→ q8 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q4 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q5 -λ→ q8 — ✘ muere tras leer λ
3. `1111`: {q0, q1, q2, q3, q4, q5, q6, q8} -1→ {q5, q6, q8, q9} -1→ {q5, q6, q8, q9} -1→ {q5, q6, q8, q9} -1→ {q5, q6, q8, q9} — ✔
  Árbol de cómputo: 10 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q2 -λ→ q6 -1→ q9 -λ→ q6 -1→ q9 -λ→ q6 -1→ q9 -λ→ q6 -1→ q9 -λ→ q5 -λ→ q8 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q5 -λ→ q8 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q6 -1→ q9 -λ→ q5 -λ→ q8 — ✘ muere tras leer `1`
    - q0 -λ→ q2 -λ→ q6 -1→ q9 -λ→ q6 -1→ q9 -λ→ q5 -λ→ q8 — ✘ muere tras leer `11`
4. `01010101`: {q0, q1, q2, q3, q4, q5, q6, q8} -0→ {q10, q7} -1→ {q11, q3, q4, q8} -0→ {q10, q7} -1→ {q11, q3, q4, q8} -0→ {q10, q7} -1→ {q11, q3, q4, q8} -0→ {q10, q7} -1→ {q11, q3, q4, q8} — ✔
  Árbol de cómputo: 10 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q4 -λ→ q8 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q4 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q4 -λ→ q8 — ✘ muere tras leer `010101`
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q4 -λ→ q8 — ✘ muere tras leer `0101`
5. `010101010101`: {q0, q1, q2, q3, q4, q5, q6, q8} -0→ {q10, q7} -1→ {q11, q3, q4, q8} -0→ {q10, q7} -1→ {q11, q3, q4, q8} -0→ {q10, q7} -1→ {q11, q3, q4, q8} -0→ {q10, q7} -1→ {q11, q3, q4, q8} -0→ {q10, q7} -1→ {q11, q3, q4, q8} -0→ {q10, q7} -1→ {q11, q3, q4, q8} — ✔
  Árbol de cómputo: 12 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q4 -λ→ q8 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q4 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q4 -λ→ q8 — ✘ muere tras leer `0101010101`
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q3 -0→ q7 -λ→ q10 -1→ q11 -λ→ q4 -λ→ q8 — ✘ muere tras leer `01010101`
6. `0`: {q0, q1, q2, q3, q4, q5, q6, q8} -0→ {q10, q7} — ✘
  Árbol de cómputo: 5 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q3 -0→ q7 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q10 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q5 -λ→ q8 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q6 — ✘ muere tras leer λ
7. `00`: {q0, q1, q2, q3, q4, q5, q6, q8} -0→ {q10, q7} -0→ ∅ — ✘
  Árbol de cómputo: 4 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q10 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q5 -λ→ q8 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q6 — ✘ muere tras leer λ
8. `1110`: {q0, q1, q2, q3, q4, q5, q6, q8} -1→ {q5, q6, q8, q9} -1→ {q5, q6, q8, q9} -1→ {q5, q6, q8, q9} -0→ ∅ — ✘
  Árbol de cómputo: 7 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q5 -λ→ q8 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q6 -1→ q9 -λ→ q5 -λ→ q8 — ✘ muere tras leer `1`
    - q0 -λ→ q2 -λ→ q6 -1→ q9 -λ→ q6 -1→ q9 -λ→ q5 -λ→ q8 — ✘ muere tras leer `11`
    - q0 -λ→ q2 -λ→ q6 -1→ q9 -λ→ q6 -1→ q9 -λ→ q6 -1→ q9 -λ→ q5 -λ→ q8 — ✘ muere tras leer `111`
9. `1101001`: {q0, q1, q2, q3, q4, q5, q6, q8} -1→ {q5, q6, q8, q9} -1→ {q5, q6, q8, q9} -0→ ∅ -1→ ∅ -0→ ∅ -0→ ∅ -1→ ∅ — ✘
  Árbol de cómputo: 6 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q5 -λ→ q8 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q6 -1→ q9 -λ→ q5 -λ→ q8 — ✘ muere tras leer `1`
    - q0 -λ→ q2 -λ→ q6 -1→ q9 -λ→ q6 -1→ q9 -λ→ q5 -λ→ q8 — ✘ muere tras leer `11`
    - q0 -λ→ q2 -λ→ q6 -1→ q9 -λ→ q6 -1→ q9 -λ→ q6 — ✘ muere tras leer `11`
10. `11010000101`: {q0, q1, q2, q3, q4, q5, q6, q8} -1→ {q5, q6, q8, q9} -1→ {q5, q6, q8, q9} -0→ ∅ -1→ ∅ -0→ ∅ -0→ ∅ -0→ ∅ -0→ ∅ -1→ ∅ -0→ ∅ -1→ ∅ — ✘
  Árbol de cómputo: 6 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q5 -λ→ q8 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q6 -1→ q9 -λ→ q5 -λ→ q8 — ✘ muere tras leer `1`
    - q0 -λ→ q2 -λ→ q6 -1→ q9 -λ→ q6 -1→ q9 -λ→ q5 -λ→ q8 — ✘ muere tras leer `11`
    - q0 -λ→ q2 -λ→ q6 -1→ q9 -λ→ q6 -1→ q9 -λ→ q6 — ✘ muere tras leer `11`

</details>

Simulación paso a paso en JFLAP con `01`: [ver captura](../../evidencias/jflap/pasos/L3-247.png).

**Conversión.** AFND-λ (12 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 10 estados, [`L3-247-AFND.jff`](../../automatas/conversiones/L3-247-AFND.jff). AFND (10 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 4 estados, [`L3-247-AFD.jff`](../../automatas/conversiones/L3-247-AFD.jff) ([.json](../../automatas/conversiones/L3-247-AFD.json), [.xml](../../automatas/conversiones/L3-247-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 5 estados, y el AFD mínimo (Hopcroft), 5. La cota es 2^10 = 1024. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-248"></a>

## Lista 3, problema 248

**Enunciado.** Encontrar un AFND-λ equivalente a la expresión regular (0*+1)0.

**Clasificación: AFND-λ.** Se pide explícitamente un AFND-λ equivalente a la expresión regular.

**Expresión:** `(0*+1)0`.

#### AFND-λ de Thompson de (0*+1)0 — `L3-248`

Archivos: [`L3-248.jff`](../../automatas/lista3-afnd-lambda/L3-248.jff) · [`L3-248.json`](../../automatas/lista3-afnd-lambda/L3-248.json) · [`L3-248.xml`](../../automatas/lista3-afnd-lambda/L3-248.xml). Tipo según la definición: **AFND-lambda**, |Q| = 10, Σ = {0, 1}, 12 transiciones.

**Diseño.** Construcción de Thompson: el árbol de la expresión se recorre de abajo hacia arriba y cada operador combina los fragmentos de sus operandos (ver la tabla de reglas en este documento).

| Estado | 0 | 1 | λ |
|---|---|---|---|
| →q0 | ∅ | ∅ | {q1, q2} |
| q1 | ∅ | ∅ | {q3, q4} |
| q3 | {q6} | ∅ | ∅ |
| q6 | ∅ | ∅ | {q3, q4} |
| q4 | ∅ | ∅ | {q7} |
| q2 | ∅ | {q5} | ∅ |
| q5 | ∅ | ∅ | {q7} |
| q7 | ∅ | ∅ | {q8} |
| q8 | {q9} | ∅ | ∅ |
| *q9 | ∅ | ∅ | ∅ |

**Transiciones λ.** Thompson usa λ en tres lugares: dos de salida en cada unión (elegir alternativa), cuatro en cada estrella (entrar, repetir, salir, saltar) y una entre los fragmentos de cada concatenación. Ninguna consume símbolos, por eso la construcción es composicional.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0, q1, q2, q3, q4, q7, q8} | no |
| q1 | {q1, q3, q4, q7, q8} | no |
| q3 | {q3} | no |
| q6 | {q3, q4, q6, q7, q8} | no |
| q4 | {q4, q7, q8} | no |
| q2 | {q2} | no |
| q5 | {q5, q7, q8} | no |
| q7 | {q7, q8} | no |
| q8 | {q8} | no |
| q9 | {q9} | sí |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `0` | acepta | acepta | acepta |
| 2 | `00` | acepta | acepta | acepta |
| 3 | `10` | acepta | acepta | acepta |
| 4 | `0000000` | acepta | acepta | acepta |
| 5 | `00000000000` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `01` | rechaza | rechaza | rechaza |
| 8 | `0011` | rechaza | rechaza | rechaza |
| 9 | `0111101` | rechaza | rechaza | rechaza |
| 10 | `10000001110` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `0`: {q0, q1, q2, q3, q4, q7, q8} -0→ {q3, q4, q6, q7, q8, q9} — ✔
  Árbol de cómputo: 7 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q4 -λ→ q7 -λ→ q8 -0→ q9 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -0→ q6 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q4 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q4 -λ→ q7 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q4 -λ→ q7 -λ→ q8 — ✘ termina fuera de F
2. `00`: {q0, q1, q2, q3, q4, q7, q8} -0→ {q3, q4, q6, q7, q8, q9} -0→ {q3, q4, q6, q7, q8, q9} — ✔
  Árbol de cómputo: 8 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q4 -λ→ q7 -λ→ q8 -0→ q9 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q4 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q4 -λ→ q7 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q4 -λ→ q7 -λ→ q8 — ✘ termina fuera de F
3. `10`: {q0, q1, q2, q3, q4, q7, q8} -1→ {q5, q7, q8} -0→ {q9} — ✔
  Árbol de cómputo: 3 caminos, 1 de aceptación:
    - q0 -λ→ q2 -1→ q5 -λ→ q7 -λ→ q8 -0→ q9 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q7 -λ→ q8 — ✘ muere tras leer λ
4. `0000000`: {q0, q1, q2, q3, q4, q7, q8} -0→ {q3, q4, q6, q7, q8, q9} -0→ {q3, q4, q6, q7, q8, q9} -0→ {q3, q4, q6, q7, q8, q9} -0→ {q3, q4, q6, q7, q8, q9} -0→ {q3, q4, q6, q7, q8, q9} -0→ {q3, q4, q6, q7, q8, q9} -0→ {q3, q4, q6, q7, q8, q9} — ✔
  Árbol de cómputo: 13 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q4 -λ→ q7 -λ→ q8 -0→ q9 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q4 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q4 -λ→ q7 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q4 -λ→ q7 -λ→ q8 — ✘ termina fuera de F
5. `00000000000`: {q0, q1, q2, q3, q4, q7, q8} -0→ {q3, q4, q6, q7, q8, q9} -0→ {q3, q4, q6, q7, q8, q9} -0→ {q3, q4, q6, q7, q8, q9} -0→ {q3, q4, q6, q7, q8, q9} -0→ {q3, q4, q6, q7, q8, q9} -0→ {q3, q4, q6, q7, q8, q9} -0→ {q3, q4, q6, q7, q8, q9} -0→ {q3, q4, q6, q7, q8, q9} -0→ {q3, q4, q6, q7, q8, q9} -0→ {q3, q4, q6, q7, q8, q9} -0→ {q3, q4, q6, q7, q8, q9} — ✔
  Árbol de cómputo: 17 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q4 -λ→ q7 -λ→ q8 -0→ q9 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q4 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q4 -λ→ q7 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q4 -λ→ q7 -λ→ q8 — ✘ termina fuera de F
6. λ: {q0, q1, q2, q3, q4, q7, q8} — ✘
  Árbol de cómputo: 7 caminos, 0 de aceptación (se muestran 6):
    - q0 — ✘ termina fuera de F
    - q0 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -λ→ q7 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -λ→ q7 -λ→ q8 — ✘ termina fuera de F
7. `01`: {q0, q1, q2, q3, q4, q7, q8} -0→ {q3, q4, q6, q7, q8, q9} -1→ ∅ — ✘
  Árbol de cómputo: 4 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q4 -λ→ q7 -λ→ q8 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q4 -λ→ q7 -λ→ q8 -0→ q9 — ✘ muere tras leer `0`
    - q0 -λ→ q2 — ✘ muere tras leer λ
8. `0011`: {q0, q1, q2, q3, q4, q7, q8} -0→ {q3, q4, q6, q7, q8, q9} -0→ {q3, q4, q6, q7, q8, q9} -1→ ∅ -1→ ∅ — ✘
  Árbol de cómputo: 5 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 — ✘ muere tras leer `00`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q4 -λ→ q7 -λ→ q8 — ✘ muere tras leer `00`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q4 -λ→ q7 -λ→ q8 -0→ q9 — ✘ muere tras leer `00`
    - q0 -λ→ q1 -λ→ q4 -λ→ q7 -λ→ q8 -0→ q9 — ✘ muere tras leer `0`
    - q0 -λ→ q2 — ✘ muere tras leer λ
9. `0111101`: {q0, q1, q2, q3, q4, q7, q8} -0→ {q3, q4, q6, q7, q8, q9} -1→ ∅ -1→ ∅ -1→ ∅ -1→ ∅ -0→ ∅ -1→ ∅ — ✘
  Árbol de cómputo: 4 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q4 -λ→ q7 -λ→ q8 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q4 -λ→ q7 -λ→ q8 -0→ q9 — ✘ muere tras leer `0`
    - q0 -λ→ q2 — ✘ muere tras leer λ
10. `10000001110`: {q0, q1, q2, q3, q4, q7, q8} -1→ {q5, q7, q8} -0→ {q9} -0→ ∅ -0→ ∅ -0→ ∅ -0→ ∅ -0→ ∅ -1→ ∅ -1→ ∅ -1→ ∅ -0→ ∅ — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q7 -λ→ q8 — ✘ muere tras leer λ
    - q0 -λ→ q2 -1→ q5 -λ→ q7 -λ→ q8 -0→ q9 — ✘ muere tras leer `10`

</details>

Simulación paso a paso en JFLAP con `00`: [ver captura](../../evidencias/jflap/pasos/L3-248.png).

**Conversión.** AFND-λ (10 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 8 estados, [`L3-248-AFND.jff`](../../automatas/conversiones/L3-248-AFND.jff). AFND (8 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 4 estados, [`L3-248-AFD.jff`](../../automatas/conversiones/L3-248-AFD.jff) ([.json](../../automatas/conversiones/L3-248-AFD.json), [.xml](../../automatas/conversiones/L3-248-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 5 estados, y el AFD mínimo (Hopcroft), 5. La cota es 2^8 = 256. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-249"></a>

## Lista 3, problema 249

**Enunciado.** Encontrar un AFND-λ equivalente a la expresión regular (0*+1)0*.

**Clasificación: AFND-λ.** Se pide explícitamente un AFND-λ equivalente a la expresión regular.

**Expresión:** `(0*+1)0*`.

#### AFND-λ de Thompson de (0*+1)0* — `L3-249`

Archivos: [`L3-249.jff`](../../automatas/lista3-afnd-lambda/L3-249.jff) · [`L3-249.json`](../../automatas/lista3-afnd-lambda/L3-249.json) · [`L3-249.xml`](../../automatas/lista3-afnd-lambda/L3-249.xml). Tipo según la definición: **AFND-lambda**, |Q| = 12, Σ = {0, 1}, 16 transiciones.

**Diseño.** Construcción de Thompson: el árbol de la expresión se recorre de abajo hacia arriba y cada operador combina los fragmentos de sus operandos (ver la tabla de reglas en este documento).

| Estado | 0 | 1 | λ |
|---|---|---|---|
| →q0 | ∅ | ∅ | {q1, q2} |
| q1 | ∅ | ∅ | {q3, q4} |
| q3 | {q6} | ∅ | ∅ |
| q6 | ∅ | ∅ | {q3, q4} |
| q4 | ∅ | ∅ | {q7} |
| q2 | ∅ | {q5} | ∅ |
| q5 | ∅ | ∅ | {q7} |
| q7 | ∅ | ∅ | {q8} |
| q8 | ∅ | ∅ | {q10, q9} |
| q10 | {q11} | ∅ | ∅ |
| q11 | ∅ | ∅ | {q10, q9} |
| *q9 | ∅ | ∅ | ∅ |

**Transiciones λ.** Thompson usa λ en tres lugares: dos de salida en cada unión (elegir alternativa), cuatro en cada estrella (entrar, repetir, salir, saltar) y una entre los fragmentos de cada concatenación. Ninguna consume símbolos, por eso la construcción es composicional.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0, q1, q10, q2, q3, q4, q7, q8, q9} | sí |
| q1 | {q1, q10, q3, q4, q7, q8, q9} | sí |
| q3 | {q3} | no |
| q6 | {q10, q3, q4, q6, q7, q8, q9} | sí |
| q4 | {q10, q4, q7, q8, q9} | sí |
| q2 | {q2} | no |
| q5 | {q10, q5, q7, q8, q9} | sí |
| q7 | {q10, q7, q8, q9} | sí |
| q8 | {q10, q8, q9} | sí |
| q10 | {q10} | no |
| q11 | {q10, q11, q9} | sí |
| q9 | {q9} | sí |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | acepta | acepta | acepta |
| 2 | `10` | acepta | acepta | acepta |
| 3 | `0000` | acepta | acepta | acepta |
| 4 | `0000000` | acepta | acepta | acepta |
| 5 | `10000000000` | acepta | acepta | acepta |
| 6 | `01` | rechaza | rechaza | rechaza |
| 7 | `11` | rechaza | rechaza | rechaza |
| 8 | `1101` | rechaza | rechaza | rechaza |
| 9 | `0100000` | rechaza | rechaza | rechaza |
| 10 | `11111011000` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: {q0, q1, q10, q2, q3, q4, q7, q8, q9} — ✔
  Árbol de cómputo: 9 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q4 -λ→ q7 -λ→ q8 -λ→ q9 — ✔ acepta
    - q0 — ✘ termina fuera de F
    - q0 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -λ→ q7 — ✘ termina fuera de F
2. `10`: {q0, q1, q10, q2, q3, q4, q7, q8, q9} -1→ {q10, q5, q7, q8, q9} -0→ {q10, q11, q9} — ✔
  Árbol de cómputo: 7 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q2 -1→ q5 -λ→ q7 -λ→ q8 -λ→ q10 -0→ q11 -λ→ q9 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q7 -λ→ q8 -λ→ q10 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q7 -λ→ q8 -λ→ q9 — ✘ muere tras leer λ
    - q0 -λ→ q2 -1→ q5 -λ→ q7 -λ→ q8 -λ→ q10 -0→ q11 — ✘ termina fuera de F
    - q0 -λ→ q2 -1→ q5 -λ→ q7 -λ→ q8 -λ→ q10 -0→ q11 -λ→ q10 — ✘ termina fuera de F
3. `0000`: {q0, q1, q10, q2, q3, q4, q7, q8, q9} -0→ {q10, q11, q3, q4, q6, q7, q8, q9} -0→ {q10, q11, q3, q4, q6, q7, q8, q9} -0→ {q10, q11, q3, q4, q6, q7, q8, q9} -0→ {q10, q11, q3, q4, q6, q7, q8, q9} — ✔
  Árbol de cómputo: 30 caminos, 5 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q4 -λ→ q7 -λ→ q8 -λ→ q9 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q4 -λ→ q7 -λ→ q8 -λ→ q10 -0→ q11 -λ→ q9 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q4 -λ→ q7 -λ→ q8 -λ→ q10 -0→ q11 -λ→ q10 -0→ q11 -λ→ q9 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q4 — ✘ termina fuera de F
4. `0000000`: {q0, q1, q10, q2, q3, q4, q7, q8, q9} -0→ {q10, q11, q3, q4, q6, q7, q8, q9} -0→ {q10, q11, q3, q4, q6, q7, q8, q9} -0→ {q10, q11, q3, q4, q6, q7, q8, q9} -0→ {q10, q11, q3, q4, q6, q7, q8, q9} -0→ {q10, q11, q3, q4, q6, q7, q8, q9} -0→ {q10, q11, q3, q4, q6, q7, q8, q9} -0→ {q10, q11, q3, q4, q6, q7, q8, q9} — ✔
  Árbol de cómputo: 57 caminos, 8 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q4 -λ→ q7 -λ→ q8 -λ→ q9 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q4 -λ→ q7 -λ→ q8 -λ→ q10 -0→ q11 -λ→ q9 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q4 -λ→ q7 -λ→ q8 -λ→ q10 -0→ q11 -λ→ q10 -0→ q11 -λ→ q9 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q3 -0→ q6 -λ→ q4 — ✘ termina fuera de F
5. `10000000000`: {q0, q1, q10, q2, q3, q4, q7, q8, q9} -1→ {q10, q5, q7, q8, q9} -0→ {q10, q11, q9} -0→ {q10, q11, q9} -0→ {q10, q11, q9} -0→ {q10, q11, q9} -0→ {q10, q11, q9} -0→ {q10, q11, q9} -0→ {q10, q11, q9} -0→ {q10, q11, q9} -0→ {q10, q11, q9} -0→ {q10, q11, q9} — ✔
  Árbol de cómputo: 16 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q2 -1→ q5 -λ→ q7 -λ→ q8 -λ→ q10 -0→ q11 -λ→ q10 -0→ q11 -λ→ q10 -0→ q11 -λ→ q10 -0→ q11 -λ→ q10 -0→ q11 -λ→ q10 -0→ q11 -λ→ q10 -0→ q11 -λ→ q10 -0→ q11 -λ→ q10 -0→ q11 -λ→ q10 -0→ q11 -λ→ q9 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q7 -λ→ q8 -λ→ q10 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q7 -λ→ q8 -λ→ q9 — ✘ muere tras leer λ
    - q0 -λ→ q2 -1→ q5 -λ→ q7 -λ→ q8 -λ→ q10 -0→ q11 -λ→ q10 -0→ q11 -λ→ q10 -0→ q11 -λ→ q10 -0→ q11 -λ→ q10 -0→ q11 -λ→ q10 -0→ q11 -λ→ q10 -0→ q11 -λ→ q10 -0→ q11 -λ→ q10 -0→ q11 -λ→ q10 -0→ q11 — ✘ termina fuera de F
    - q0 -λ→ q2 -1→ q5 -λ→ q7 -λ→ q8 -λ→ q10 -0→ q11 -λ→ q10 -0→ q11 -λ→ q10 -0→ q11 -λ→ q10 -0→ q11 -λ→ q10 -0→ q11 -λ→ q10 -0→ q11 -λ→ q10 -0→ q11 -λ→ q10 -0→ q11 -λ→ q10 -0→ q11 -λ→ q10 -0→ q11 -λ→ q10 — ✘ termina fuera de F
6. `01`: {q0, q1, q10, q2, q3, q4, q7, q8, q9} -0→ {q10, q11, q3, q4, q6, q7, q8, q9} -1→ ∅ — ✘
  Árbol de cómputo: 7 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q4 -λ→ q7 -λ→ q8 -λ→ q10 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q4 -λ→ q7 -λ→ q8 -λ→ q9 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q4 -λ→ q7 -λ→ q8 -λ→ q10 -0→ q11 -λ→ q10 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q4 -λ→ q7 -λ→ q8 -λ→ q10 -0→ q11 -λ→ q9 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q4 -λ→ q7 -λ→ q8 -λ→ q9 — ✘ muere tras leer λ
7. `11`: {q0, q1, q10, q2, q3, q4, q7, q8, q9} -1→ {q10, q5, q7, q8, q9} -1→ ∅ — ✘
  Árbol de cómputo: 5 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q7 -λ→ q8 -λ→ q10 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q7 -λ→ q8 -λ→ q9 — ✘ muere tras leer λ
    - q0 -λ→ q2 -1→ q5 -λ→ q7 -λ→ q8 -λ→ q10 — ✘ muere tras leer `1`
    - q0 -λ→ q2 -1→ q5 -λ→ q7 -λ→ q8 -λ→ q9 — ✘ muere tras leer `1`
8. `1101`: {q0, q1, q10, q2, q3, q4, q7, q8, q9} -1→ {q10, q5, q7, q8, q9} -1→ ∅ -0→ ∅ -1→ ∅ — ✘
  Árbol de cómputo: 5 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q7 -λ→ q8 -λ→ q10 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q7 -λ→ q8 -λ→ q9 — ✘ muere tras leer λ
    - q0 -λ→ q2 -1→ q5 -λ→ q7 -λ→ q8 -λ→ q10 — ✘ muere tras leer `1`
    - q0 -λ→ q2 -1→ q5 -λ→ q7 -λ→ q8 -λ→ q9 — ✘ muere tras leer `1`
9. `0100000`: {q0, q1, q10, q2, q3, q4, q7, q8, q9} -0→ {q10, q11, q3, q4, q6, q7, q8, q9} -1→ ∅ -0→ ∅ -0→ ∅ -0→ ∅ -0→ ∅ -0→ ∅ — ✘
  Árbol de cómputo: 7 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q3 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q4 -λ→ q7 -λ→ q8 -λ→ q10 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q3 -0→ q6 -λ→ q4 -λ→ q7 -λ→ q8 -λ→ q9 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q4 -λ→ q7 -λ→ q8 -λ→ q10 -0→ q11 -λ→ q10 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q4 -λ→ q7 -λ→ q8 -λ→ q10 -0→ q11 -λ→ q9 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q4 -λ→ q7 -λ→ q8 -λ→ q9 — ✘ muere tras leer λ
10. `11111011000`: {q0, q1, q10, q2, q3, q4, q7, q8, q9} -1→ {q10, q5, q7, q8, q9} -1→ ∅ -1→ ∅ -1→ ∅ -1→ ∅ -0→ ∅ -1→ ∅ -1→ ∅ -0→ ∅ -0→ ∅ -0→ ∅ — ✘
  Árbol de cómputo: 5 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q7 -λ→ q8 -λ→ q10 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q7 -λ→ q8 -λ→ q9 — ✘ muere tras leer λ
    - q0 -λ→ q2 -1→ q5 -λ→ q7 -λ→ q8 -λ→ q10 — ✘ muere tras leer `1`
    - q0 -λ→ q2 -1→ q5 -λ→ q7 -λ→ q8 -λ→ q9 — ✘ muere tras leer `1`

</details>

Simulación paso a paso en JFLAP con `10`: [ver captura](../../evidencias/jflap/pasos/L3-249.png).

**Conversión.** AFND-λ (12 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 10 estados, [`L3-249-AFND.jff`](../../automatas/conversiones/L3-249-AFND.jff). AFND (10 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 4 estados, [`L3-249-AFD.jff`](../../automatas/conversiones/L3-249-AFD.jff) ([.json](../../automatas/conversiones/L3-249-AFD.json), [.xml](../../automatas/conversiones/L3-249-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 5 estados, y el AFD mínimo (Hopcroft), 3. La cota es 2^10 = 1024. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-250"></a>

## Lista 3, problema 250

**Enunciado.** Encontrar un AFND-λ equivalente a la expresión regular 0*1*+1*0.

**Clasificación: AFND-λ.** Se pide explícitamente un AFND-λ equivalente a la expresión regular.

**Expresión:** `0*1*+1*0`.

#### AFND-λ de Thompson de 0*1*+1*0 — `L3-250`

Archivos: [`L3-250.jff`](../../automatas/lista3-afnd-lambda/L3-250.jff) · [`L3-250.json`](../../automatas/lista3-afnd-lambda/L3-250.json) · [`L3-250.xml`](../../automatas/lista3-afnd-lambda/L3-250.xml). Tipo según la definición: **AFND-lambda**, |Q| = 16, Σ = {0, 1}, 22 transiciones.

**Diseño.** Construcción de Thompson: el árbol de la expresión se recorre de abajo hacia arriba y cada operador combina los fragmentos de sus operandos (ver la tabla de reglas en este documento).

<details><summary>Tabla de transiciones (16 estados)</summary>

| Estado | 0 | 1 | λ |
|---|---|---|---|
| →q0 | ∅ | ∅ | {q1, q2} |
| q1 | ∅ | ∅ | {q3, q4} |
| q3 | {q7} | ∅ | ∅ |
| q7 | ∅ | ∅ | {q3, q4} |
| q4 | ∅ | ∅ | {q8} |
| q8 | ∅ | ∅ | {q11, q12} |
| q11 | ∅ | {q14} | ∅ |
| q14 | ∅ | ∅ | {q11, q12} |
| q12 | ∅ | ∅ | {q15} |
| q2 | ∅ | ∅ | {q5, q6} |
| q5 | ∅ | {q9} | ∅ |
| q9 | ∅ | ∅ | {q5, q6} |
| q6 | ∅ | ∅ | {q10} |
| q10 | {q13} | ∅ | ∅ |
| q13 | ∅ | ∅ | {q15} |
| *q15 | ∅ | ∅ | ∅ |

</details>

**Transiciones λ.** Thompson usa λ en tres lugares: dos de salida en cada unión (elegir alternativa), cuatro en cada estrella (entrar, repetir, salir, saltar) y una entre los fragmentos de cada concatenación. Ninguna consume símbolos, por eso la construcción es composicional.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

<details><summary>λ-clausuras de los 16 estados</summary>

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0, q1, q10, q11, q12, q15, q2, q3, q4, q5, q6, q8} | sí |
| q1 | {q1, q11, q12, q15, q3, q4, q8} | sí |
| q3 | {q3} | no |
| q7 | {q11, q12, q15, q3, q4, q7, q8} | sí |
| q4 | {q11, q12, q15, q4, q8} | sí |
| q8 | {q11, q12, q15, q8} | sí |
| q11 | {q11} | no |
| q14 | {q11, q12, q14, q15} | sí |
| q12 | {q12, q15} | sí |
| q2 | {q10, q2, q5, q6} | no |
| q5 | {q5} | no |
| q9 | {q10, q5, q6, q9} | no |
| q6 | {q10, q6} | no |
| q10 | {q10} | no |
| q13 | {q13, q15} | sí |
| q15 | {q15} | sí |

</details>

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | acepta | acepta | acepta |
| 2 | `10` | acepta | acepta | acepta |
| 3 | `11` | acepta | acepta | acepta |
| 4 | `110` | acepta | acepta | acepta |
| 5 | `0111111` | acepta | acepta | acepta |
| 6 | `010` | rechaza | rechaza | rechaza |
| 7 | `100` | rechaza | rechaza | rechaza |
| 8 | `00110` | rechaza | rechaza | rechaza |
| 9 | `0100101` | rechaza | rechaza | rechaza |
| 10 | `01010001110` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: {q0, q1, q10, q11, q12, q15, q2, q3, q4, q5, q6, q8} — ✔
  Árbol de cómputo: 12 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -λ→ q12 -λ→ q15 — ✔ acepta
    - q0 — ✘ termina fuera de F
    - q0 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 — ✘ termina fuera de F
2. `10`: {q0, q1, q10, q11, q12, q15, q2, q3, q4, q5, q6, q8} -1→ {q10, q11, q12, q14, q15, q5, q6, q9} -0→ {q13, q15} — ✔
  Árbol de cómputo: 8 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q2 -λ→ q5 -1→ q9 -λ→ q6 -λ→ q10 -0→ q13 -λ→ q15 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -λ→ q11 -1→ q14 -λ→ q11 — ✘ muere tras leer `1`
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -λ→ q11 -1→ q14 -λ→ q12 -λ→ q15 — ✘ muere tras leer `1`
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -λ→ q12 -λ→ q15 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q5 -1→ q9 -λ→ q5 — ✘ muere tras leer `1`
3. `11`: {q0, q1, q10, q11, q12, q15, q2, q3, q4, q5, q6, q8} -1→ {q10, q11, q12, q14, q15, q5, q6, q9} -1→ {q10, q11, q12, q14, q15, q5, q6, q9} — ✔
  Árbol de cómputo: 13 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -λ→ q11 -1→ q14 -λ→ q11 -1→ q14 -λ→ q12 -λ→ q15 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -λ→ q11 -1→ q14 -λ→ q11 -1→ q14 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -λ→ q11 -1→ q14 -λ→ q11 -1→ q14 -λ→ q11 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -λ→ q11 -1→ q14 -λ→ q11 -1→ q14 -λ→ q12 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -λ→ q11 -1→ q14 -λ→ q12 -λ→ q15 — ✘ muere tras leer `1`
4. `110`: {q0, q1, q10, q11, q12, q15, q2, q3, q4, q5, q6, q8} -1→ {q10, q11, q12, q14, q15, q5, q6, q9} -1→ {q10, q11, q12, q14, q15, q5, q6, q9} -0→ {q13, q15} — ✔
  Árbol de cómputo: 10 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q2 -λ→ q5 -1→ q9 -λ→ q5 -1→ q9 -λ→ q6 -λ→ q10 -0→ q13 -λ→ q15 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -λ→ q11 -1→ q14 -λ→ q11 -1→ q14 -λ→ q11 — ✘ muere tras leer `11`
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -λ→ q11 -1→ q14 -λ→ q11 -1→ q14 -λ→ q12 -λ→ q15 — ✘ muere tras leer `11`
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -λ→ q11 -1→ q14 -λ→ q12 -λ→ q15 — ✘ muere tras leer `1`
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -λ→ q12 -λ→ q15 — ✘ muere tras leer λ
5. `0111111`: {q0, q1, q10, q11, q12, q15, q2, q3, q4, q5, q6, q8} -0→ {q11, q12, q13, q15, q3, q4, q7, q8} -1→ {q11, q12, q14, q15} -1→ {q11, q12, q14, q15} -1→ {q11, q12, q14, q15} -1→ {q11, q12, q14, q15} -1→ {q11, q12, q14, q15} -1→ {q11, q12, q14, q15} — ✔
  Árbol de cómputo: 15 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q4 -λ→ q8 -λ→ q11 -1→ q14 -λ→ q11 -1→ q14 -λ→ q11 -1→ q14 -λ→ q11 -1→ q14 -λ→ q11 -1→ q14 -λ→ q11 -1→ q14 -λ→ q12 -λ→ q15 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q3 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q4 -λ→ q8 -λ→ q11 -1→ q14 -λ→ q11 -1→ q14 -λ→ q11 -1→ q14 -λ→ q11 -1→ q14 -λ→ q11 -1→ q14 -λ→ q11 -1→ q14 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q4 -λ→ q8 -λ→ q11 -1→ q14 -λ→ q11 -1→ q14 -λ→ q11 -1→ q14 -λ→ q11 -1→ q14 -λ→ q11 -1→ q14 -λ→ q11 -1→ q14 -λ→ q11 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q4 -λ→ q8 -λ→ q11 -1→ q14 -λ→ q11 -1→ q14 -λ→ q11 -1→ q14 -λ→ q11 -1→ q14 -λ→ q11 -1→ q14 -λ→ q11 -1→ q14 -λ→ q12 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q4 -λ→ q8 -λ→ q11 -1→ q14 -λ→ q11 -1→ q14 -λ→ q11 -1→ q14 -λ→ q11 -1→ q14 -λ→ q11 -1→ q14 -λ→ q12 -λ→ q15 — ✘ muere tras leer `011111`
6. `010`: {q0, q1, q10, q11, q12, q15, q2, q3, q4, q5, q6, q8} -0→ {q11, q12, q13, q15, q3, q4, q7, q8} -1→ {q11, q12, q14, q15} -0→ ∅ — ✘
  Árbol de cómputo: 8 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q3 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q4 -λ→ q8 -λ→ q11 -1→ q14 -λ→ q11 — ✘ muere tras leer `01`
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q4 -λ→ q8 -λ→ q11 -1→ q14 -λ→ q12 -λ→ q15 — ✘ muere tras leer `01`
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q4 -λ→ q8 -λ→ q12 -λ→ q15 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -λ→ q11 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -λ→ q12 -λ→ q15 — ✘ muere tras leer λ
7. `100`: {q0, q1, q10, q11, q12, q15, q2, q3, q4, q5, q6, q8} -1→ {q10, q11, q12, q14, q15, q5, q6, q9} -0→ {q13, q15} -0→ ∅ — ✘
  Árbol de cómputo: 7 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -λ→ q11 -1→ q14 -λ→ q11 — ✘ muere tras leer `1`
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -λ→ q11 -1→ q14 -λ→ q12 -λ→ q15 — ✘ muere tras leer `1`
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -λ→ q12 -λ→ q15 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q5 -1→ q9 -λ→ q5 — ✘ muere tras leer `1`
    - q0 -λ→ q2 -λ→ q5 -1→ q9 -λ→ q6 -λ→ q10 -0→ q13 -λ→ q15 — ✘ muere tras leer `10`
8. `00110`: {q0, q1, q10, q11, q12, q15, q2, q3, q4, q5, q6, q8} -0→ {q11, q12, q13, q15, q3, q4, q7, q8} -0→ {q11, q12, q15, q3, q4, q7, q8} -1→ {q11, q12, q14, q15} -1→ {q11, q12, q14, q15} -0→ ∅ — ✘
  Árbol de cómputo: 11 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q3 -0→ q7 -λ→ q3 — ✘ muere tras leer `00`
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q3 -0→ q7 -λ→ q4 -λ→ q8 -λ→ q11 -1→ q14 -λ→ q11 -1→ q14 -λ→ q11 — ✘ muere tras leer `0011`
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q3 -0→ q7 -λ→ q4 -λ→ q8 -λ→ q11 -1→ q14 -λ→ q11 -1→ q14 -λ→ q12 -λ→ q15 — ✘ muere tras leer `0011`
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q3 -0→ q7 -λ→ q4 -λ→ q8 -λ→ q11 -1→ q14 -λ→ q12 -λ→ q15 — ✘ muere tras leer `001`
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q3 -0→ q7 -λ→ q4 -λ→ q8 -λ→ q12 -λ→ q15 — ✘ muere tras leer `00`
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q4 -λ→ q8 -λ→ q11 — ✘ muere tras leer `0`
9. `0100101`: {q0, q1, q10, q11, q12, q15, q2, q3, q4, q5, q6, q8} -0→ {q11, q12, q13, q15, q3, q4, q7, q8} -1→ {q11, q12, q14, q15} -0→ ∅ -0→ ∅ -1→ ∅ -0→ ∅ -1→ ∅ — ✘
  Árbol de cómputo: 8 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q3 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q4 -λ→ q8 -λ→ q11 -1→ q14 -λ→ q11 — ✘ muere tras leer `01`
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q4 -λ→ q8 -λ→ q11 -1→ q14 -λ→ q12 -λ→ q15 — ✘ muere tras leer `01`
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q4 -λ→ q8 -λ→ q12 -λ→ q15 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -λ→ q11 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -λ→ q12 -λ→ q15 — ✘ muere tras leer λ
10. `01010001110`: {q0, q1, q10, q11, q12, q15, q2, q3, q4, q5, q6, q8} -0→ {q11, q12, q13, q15, q3, q4, q7, q8} -1→ {q11, q12, q14, q15} -0→ ∅ -1→ ∅ -0→ ∅ -0→ ∅ -0→ ∅ -1→ ∅ -1→ ∅ -1→ ∅ -0→ ∅ — ✘
  Árbol de cómputo: 8 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q3 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q4 -λ→ q8 -λ→ q11 -1→ q14 -λ→ q11 — ✘ muere tras leer `01`
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q4 -λ→ q8 -λ→ q11 -1→ q14 -λ→ q12 -λ→ q15 — ✘ muere tras leer `01`
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q4 -λ→ q8 -λ→ q12 -λ→ q15 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -λ→ q11 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -λ→ q12 -λ→ q15 — ✘ muere tras leer λ

</details>

Simulación paso a paso en JFLAP con `10`: [ver captura](../../evidencias/jflap/pasos/L3-250.png).

**Conversión.** AFND-λ (16 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 14 estados, [`L3-250-AFND.jff`](../../automatas/conversiones/L3-250-AFND.jff). AFND (14 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 6 estados, [`L3-250-AFD.jff`](../../automatas/conversiones/L3-250-AFD.jff) ([.json](../../automatas/conversiones/L3-250-AFD.json), [.xml](../../automatas/conversiones/L3-250-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 7 estados, y el AFD mínimo (Hopcroft), 6. La cota es 2^14 = 16384. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-251"></a>

## Lista 3, problema 251

**Enunciado.** Encontrar un AFND-λ equivalente a la expresión regular (0+1*)0+1*1.

**Clasificación: AFND-λ.** Se pide explícitamente un AFND-λ equivalente a la expresión regular.

**Expresión:** `(0+1*)0+1*1`.

#### AFND-λ de Thompson de (0+1*)0+1*1 — `L3-251`

Archivos: [`L3-251.jff`](../../automatas/lista3-afnd-lambda/L3-251.jff) · [`L3-251.json`](../../automatas/lista3-afnd-lambda/L3-251.json) · [`L3-251.xml`](../../automatas/lista3-afnd-lambda/L3-251.xml). Tipo según la definición: **AFND-lambda**, |Q| = 18, Σ = {0, 1}, 23 transiciones.

**Diseño.** Construcción de Thompson: el árbol de la expresión se recorre de abajo hacia arriba y cada operador combina los fragmentos de sus operandos (ver la tabla de reglas en este documento).

<details><summary>Tabla de transiciones (18 estados)</summary>

| Estado | 0 | 1 | λ |
|---|---|---|---|
| →q0 | ∅ | ∅ | {q1, q2} |
| q1 | ∅ | ∅ | {q3, q4} |
| q3 | {q7} | ∅ | ∅ |
| q7 | ∅ | ∅ | {q12} |
| q4 | ∅ | ∅ | {q8, q9} |
| q8 | ∅ | {q13} | ∅ |
| q13 | ∅ | ∅ | {q8, q9} |
| q9 | ∅ | ∅ | {q12} |
| q12 | ∅ | ∅ | {q15} |
| q15 | {q17} | ∅ | ∅ |
| q17 | ∅ | ∅ | {q16} |
| q2 | ∅ | ∅ | {q5, q6} |
| q5 | ∅ | {q10} | ∅ |
| q10 | ∅ | ∅ | {q5, q6} |
| q6 | ∅ | ∅ | {q11} |
| q11 | ∅ | {q14} | ∅ |
| q14 | ∅ | ∅ | {q16} |
| *q16 | ∅ | ∅ | ∅ |

</details>

**Transiciones λ.** Thompson usa λ en tres lugares: dos de salida en cada unión (elegir alternativa), cuatro en cada estrella (entrar, repetir, salir, saltar) y una entre los fragmentos de cada concatenación. Ninguna consume símbolos, por eso la construcción es composicional.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

<details><summary>λ-clausuras de los 18 estados</summary>

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0, q1, q11, q12, q15, q2, q3, q4, q5, q6, q8, q9} | no |
| q1 | {q1, q12, q15, q3, q4, q8, q9} | no |
| q3 | {q3} | no |
| q7 | {q12, q15, q7} | no |
| q4 | {q12, q15, q4, q8, q9} | no |
| q8 | {q8} | no |
| q13 | {q12, q13, q15, q8, q9} | no |
| q9 | {q12, q15, q9} | no |
| q12 | {q12, q15} | no |
| q15 | {q15} | no |
| q17 | {q16, q17} | sí |
| q2 | {q11, q2, q5, q6} | no |
| q5 | {q5} | no |
| q10 | {q10, q11, q5, q6} | no |
| q6 | {q11, q6} | no |
| q11 | {q11} | no |
| q14 | {q14, q16} | sí |
| q16 | {q16} | sí |

</details>

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `0` | acepta | acepta | — |
| 2 | `00` | acepta | acepta | acepta |
| 3 | `10` | acepta | acepta | acepta |
| 4 | `11` | acepta | acepta | acepta |
| 5 | `110` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `0100` | rechaza | rechaza | rechaza |
| 8 | `1100` | rechaza | rechaza | rechaza |
| 9 | `1101000` | rechaza | rechaza | rechaza |
| 10 | `11100101111` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `0`: {q0, q1, q11, q12, q15, q2, q3, q4, q5, q6, q8, q9} -0→ {q12, q15, q16, q17, q7} — ✔
  Árbol de cómputo: 8 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q4 -λ→ q9 -λ→ q12 -λ→ q15 -0→ q17 -λ→ q16 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -0→ q7 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q12 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q12 -λ→ q15 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q9 -λ→ q12 -λ→ q15 -0→ q17 — ✘ termina fuera de F
2. `00`: {q0, q1, q11, q12, q15, q2, q3, q4, q5, q6, q8, q9} -0→ {q12, q15, q16, q17, q7} -0→ {q16, q17} — ✔
  Árbol de cómputo: 6 caminos, 1 de aceptación:
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q12 -λ→ q15 -0→ q17 -λ→ q16 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q12 -λ→ q15 -0→ q17 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q9 -λ→ q12 -λ→ q15 -0→ q17 -λ→ q16 — ✘ muere tras leer `0`
    - q0 -λ→ q2 -λ→ q5 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q6 -λ→ q11 — ✘ muere tras leer λ
3. `10`: {q0, q1, q11, q12, q15, q2, q3, q4, q5, q6, q8, q9} -1→ {q10, q11, q12, q13, q14, q15, q16, q5, q6, q8, q9} -0→ {q16, q17} — ✔
  Árbol de cómputo: 8 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -1→ q13 -λ→ q9 -λ→ q12 -λ→ q15 -0→ q17 -λ→ q16 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -1→ q13 -λ→ q8 — ✘ muere tras leer `1`
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -1→ q13 -λ→ q9 -λ→ q12 -λ→ q15 -0→ q17 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -λ→ q9 -λ→ q12 -λ→ q15 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q5 -1→ q10 -λ→ q5 — ✘ muere tras leer `1`
4. `11`: {q0, q1, q11, q12, q15, q2, q3, q4, q5, q6, q8, q9} -1→ {q10, q11, q12, q13, q14, q15, q16, q5, q6, q8, q9} -1→ {q10, q11, q12, q13, q14, q15, q16, q5, q6, q8, q9} — ✔
  Árbol de cómputo: 15 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q2 -λ→ q5 -1→ q10 -λ→ q6 -λ→ q11 -1→ q14 -λ→ q16 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -1→ q13 -λ→ q8 -1→ q13 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -1→ q13 -λ→ q8 -1→ q13 -λ→ q8 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -1→ q13 -λ→ q8 -1→ q13 -λ→ q9 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -1→ q13 -λ→ q8 -1→ q13 -λ→ q9 -λ→ q12 — ✘ termina fuera de F
5. `110`: {q0, q1, q11, q12, q15, q2, q3, q4, q5, q6, q8, q9} -1→ {q10, q11, q12, q13, q14, q15, q16, q5, q6, q8, q9} -1→ {q10, q11, q12, q13, q14, q15, q16, q5, q6, q8, q9} -0→ {q16, q17} — ✔
  Árbol de cómputo: 10 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -1→ q13 -λ→ q8 -1→ q13 -λ→ q9 -λ→ q12 -λ→ q15 -0→ q17 -λ→ q16 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -1→ q13 -λ→ q8 -1→ q13 -λ→ q8 — ✘ muere tras leer `11`
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -1→ q13 -λ→ q8 -1→ q13 -λ→ q9 -λ→ q12 -λ→ q15 -0→ q17 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -1→ q13 -λ→ q9 -λ→ q12 -λ→ q15 — ✘ muere tras leer `1`
    - q0 -λ→ q1 -λ→ q4 -λ→ q9 -λ→ q12 -λ→ q15 — ✘ muere tras leer λ
6. λ: {q0, q1, q11, q12, q15, q2, q3, q4, q5, q6, q8, q9} — ✘
  Árbol de cómputo: 12 caminos, 0 de aceptación (se muestran 6):
    - q0 — ✘ termina fuera de F
    - q0 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 -λ→ q9 — ✘ termina fuera de F
7. `0100`: {q0, q1, q11, q12, q15, q2, q3, q4, q5, q6, q8, q9} -0→ {q12, q15, q16, q17, q7} -1→ ∅ -0→ ∅ -0→ ∅ — ✘
  Árbol de cómputo: 5 caminos, 0 de aceptación:
    - q0 -λ→ q1 -λ→ q3 -0→ q7 -λ→ q12 -λ→ q15 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q9 -λ→ q12 -λ→ q15 -0→ q17 -λ→ q16 — ✘ muere tras leer `0`
    - q0 -λ→ q2 -λ→ q5 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q6 -λ→ q11 — ✘ muere tras leer λ
8. `1100`: {q0, q1, q11, q12, q15, q2, q3, q4, q5, q6, q8, q9} -1→ {q10, q11, q12, q13, q14, q15, q16, q5, q6, q8, q9} -1→ {q10, q11, q12, q13, q14, q15, q16, q5, q6, q8, q9} -0→ {q16, q17} -0→ ∅ — ✘
  Árbol de cómputo: 9 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -1→ q13 -λ→ q8 -1→ q13 -λ→ q8 — ✘ muere tras leer `11`
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -1→ q13 -λ→ q8 -1→ q13 -λ→ q9 -λ→ q12 -λ→ q15 -0→ q17 -λ→ q16 — ✘ muere tras leer `110`
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -1→ q13 -λ→ q9 -λ→ q12 -λ→ q15 — ✘ muere tras leer `1`
    - q0 -λ→ q1 -λ→ q4 -λ→ q9 -λ→ q12 -λ→ q15 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q5 -1→ q10 -λ→ q5 -1→ q10 -λ→ q5 — ✘ muere tras leer `11`
9. `1101000`: {q0, q1, q11, q12, q15, q2, q3, q4, q5, q6, q8, q9} -1→ {q10, q11, q12, q13, q14, q15, q16, q5, q6, q8, q9} -1→ {q10, q11, q12, q13, q14, q15, q16, q5, q6, q8, q9} -0→ {q16, q17} -1→ ∅ -0→ ∅ -0→ ∅ -0→ ∅ — ✘
  Árbol de cómputo: 9 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -1→ q13 -λ→ q8 -1→ q13 -λ→ q8 — ✘ muere tras leer `11`
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -1→ q13 -λ→ q8 -1→ q13 -λ→ q9 -λ→ q12 -λ→ q15 -0→ q17 -λ→ q16 — ✘ muere tras leer `110`
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -1→ q13 -λ→ q9 -λ→ q12 -λ→ q15 — ✘ muere tras leer `1`
    - q0 -λ→ q1 -λ→ q4 -λ→ q9 -λ→ q12 -λ→ q15 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q5 -1→ q10 -λ→ q5 -1→ q10 -λ→ q5 — ✘ muere tras leer `11`
10. `11100101111`: {q0, q1, q11, q12, q15, q2, q3, q4, q5, q6, q8, q9} -1→ {q10, q11, q12, q13, q14, q15, q16, q5, q6, q8, q9} -1→ {q10, q11, q12, q13, q14, q15, q16, q5, q6, q8, q9} -1→ {q10, q11, q12, q13, q14, q15, q16, q5, q6, q8, q9} -0→ {q16, q17} -0→ ∅ -1→ ∅ -0→ ∅ -1→ ∅ -1→ ∅ -1→ ∅ -1→ ∅ — ✘
  Árbol de cómputo: 11 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -1→ q13 -λ→ q8 -1→ q13 -λ→ q8 -1→ q13 -λ→ q8 — ✘ muere tras leer `111`
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -1→ q13 -λ→ q8 -1→ q13 -λ→ q8 -1→ q13 -λ→ q9 -λ→ q12 -λ→ q15 -0→ q17 -λ→ q16 — ✘ muere tras leer `1110`
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -1→ q13 -λ→ q8 -1→ q13 -λ→ q9 -λ→ q12 -λ→ q15 — ✘ muere tras leer `11`
    - q0 -λ→ q1 -λ→ q4 -λ→ q8 -1→ q13 -λ→ q9 -λ→ q12 -λ→ q15 — ✘ muere tras leer `1`
    - q0 -λ→ q1 -λ→ q4 -λ→ q9 -λ→ q12 -λ→ q15 — ✘ muere tras leer λ

</details>

Simulación paso a paso en JFLAP con `00`: [ver captura](../../evidencias/jflap/pasos/L3-251.png).

**Conversión.** AFND-λ (18 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 14 estados, [`L3-251-AFND.jff`](../../automatas/conversiones/L3-251-AFND.jff). AFND (14 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 4 estados, [`L3-251-AFD.jff`](../../automatas/conversiones/L3-251-AFD.jff) ([.json](../../automatas/conversiones/L3-251-AFD.json), [.xml](../../automatas/conversiones/L3-251-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 5 estados, y el AFD mínimo (Hopcroft), 5. La cota es 2^14 = 16384. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-252"></a>

## Lista 3, problema 252

**Enunciado.** Encontrar un AFND-λ equivalente a la expresión regular (0+1)*(00+11)+(00+11)(0+1)*.

**Clasificación: AFND-λ.** Se pide explícitamente un AFND-λ equivalente a la expresión regular.

**Expresión:** `(0+1)*(00+11)+(00+11)(0+1)*`.

#### AFND-λ de Thompson de (0+1)*(00+11)+(00+11)(0+1)* — `L3-252`

Archivos: [`L3-252.jff`](../../automatas/lista3-afnd-lambda/L3-252.jff) · [`L3-252.json`](../../automatas/lista3-afnd-lambda/L3-252.json) · [`L3-252.xml`](../../automatas/lista3-afnd-lambda/L3-252.xml). Tipo según la definición: **AFND-lambda**, |Q| = 38, Σ = {0, 1}, 46 transiciones.

**Diseño.** Construcción de Thompson: el árbol de la expresión se recorre de abajo hacia arriba y cada operador combina los fragmentos de sus operandos (ver la tabla de reglas en este documento).

<details><summary>Tabla de transiciones (38 estados)</summary>

| Estado | 0 | 1 | λ |
|---|---|---|---|
| →q0 | ∅ | ∅ | {q1, q2} |
| q1 | ∅ | ∅ | {q3, q4} |
| q3 | ∅ | ∅ | {q7, q8} |
| q7 | {q12} | ∅ | ∅ |
| q12 | ∅ | ∅ | {q18} |
| q8 | ∅ | {q13} | ∅ |
| q13 | ∅ | ∅ | {q18} |
| q18 | ∅ | ∅ | {q3, q4} |
| q4 | ∅ | ∅ | {q9} |
| q9 | ∅ | ∅ | {q14, q15} |
| q14 | {q19} | ∅ | ∅ |
| q19 | ∅ | ∅ | {q23} |
| q23 | {q26} | ∅ | ∅ |
| q26 | ∅ | ∅ | {q29} |
| q15 | ∅ | {q20} | ∅ |
| q20 | ∅ | ∅ | {q24} |
| q24 | ∅ | {q27} | ∅ |
| q27 | ∅ | ∅ | {q29} |
| q29 | ∅ | ∅ | {q32} |
| q2 | ∅ | ∅ | {q5, q6} |
| q5 | {q10} | ∅ | ∅ |
| q10 | ∅ | ∅ | {q16} |
| q16 | {q21} | ∅ | ∅ |
| q21 | ∅ | ∅ | {q25} |
| q6 | ∅ | {q11} | ∅ |
| q11 | ∅ | ∅ | {q17} |
| q17 | ∅ | {q22} | ∅ |
| q22 | ∅ | ∅ | {q25} |
| q25 | ∅ | ∅ | {q28} |
| q28 | ∅ | ∅ | {q30, q31} |
| q30 | ∅ | ∅ | {q33, q34} |
| q33 | {q35} | ∅ | ∅ |
| q35 | ∅ | ∅ | {q37} |
| q34 | ∅ | {q36} | ∅ |
| q36 | ∅ | ∅ | {q37} |
| q37 | ∅ | ∅ | {q30, q31} |
| q31 | ∅ | ∅ | {q32} |
| *q32 | ∅ | ∅ | ∅ |

</details>

**Transiciones λ.** Thompson usa λ en tres lugares: dos de salida en cada unión (elegir alternativa), cuatro en cada estrella (entrar, repetir, salir, saltar) y una entre los fragmentos de cada concatenación. Ninguna consume símbolos, por eso la construcción es composicional.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

<details><summary>λ-clausuras de los 38 estados</summary>

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0, q1, q14, q15, q2, q3, q4, q5, q6, q7, q8, q9} | no |
| q1 | {q1, q14, q15, q3, q4, q7, q8, q9} | no |
| q3 | {q3, q7, q8} | no |
| q7 | {q7} | no |
| q12 | {q12, q14, q15, q18, q3, q4, q7, q8, q9} | no |
| q8 | {q8} | no |
| q13 | {q13, q14, q15, q18, q3, q4, q7, q8, q9} | no |
| q18 | {q14, q15, q18, q3, q4, q7, q8, q9} | no |
| q4 | {q14, q15, q4, q9} | no |
| q9 | {q14, q15, q9} | no |
| q14 | {q14} | no |
| q19 | {q19, q23} | no |
| q23 | {q23} | no |
| q26 | {q26, q29, q32} | sí |
| q15 | {q15} | no |
| q20 | {q20, q24} | no |
| q24 | {q24} | no |
| q27 | {q27, q29, q32} | sí |
| q29 | {q29, q32} | sí |
| q2 | {q2, q5, q6} | no |
| q5 | {q5} | no |
| q10 | {q10, q16} | no |
| q16 | {q16} | no |
| q21 | {q21, q25, q28, q30, q31, q32, q33, q34} | sí |
| q6 | {q6} | no |
| q11 | {q11, q17} | no |
| q17 | {q17} | no |
| q22 | {q22, q25, q28, q30, q31, q32, q33, q34} | sí |
| q25 | {q25, q28, q30, q31, q32, q33, q34} | sí |
| q28 | {q28, q30, q31, q32, q33, q34} | sí |
| q30 | {q30, q33, q34} | no |
| q33 | {q33} | no |
| q35 | {q30, q31, q32, q33, q34, q35, q37} | sí |
| q34 | {q34} | no |
| q36 | {q30, q31, q32, q33, q34, q36, q37} | sí |
| q37 | {q30, q31, q32, q33, q34, q37} | sí |
| q31 | {q31, q32} | sí |
| q32 | {q32} | sí |

</details>

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `00` | acepta | acepta | acepta |
| 2 | `100` | acepta | acepta | acepta |
| 3 | `01100` | acepta | acepta | acepta |
| 4 | `1110011` | acepta | acepta | acepta |
| 5 | `01000111100` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `10` | rechaza | rechaza | rechaza |
| 8 | `10110` | rechaza | rechaza | rechaza |
| 9 | `10010110` | rechaza | rechaza | rechaza |
| 10 | `100110111001` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `00`: {q0, q1, q14, q15, q2, q3, q4, q5, q6, q7, q8, q9} -0→ {q10, q12, q14, q15, q16, q18, q19, q23, q3, q4, q7, q8, q9} -0→ {q12, q14, q15, q18, q19, q21, q23, q25, q26, q28, q29, q3, q30, q31, q32, q33, q34, q4, q7, q8, q9} — ✔
  Árbol de cómputo: 27 caminos, 2 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q4 -λ→ q9 -λ→ q14 -0→ q19 -λ→ q23 -0→ q26 -λ→ q29 -λ→ q32 — ✔ acepta
    - q0 -λ→ q2 -λ→ q5 -0→ q10 -λ→ q16 -0→ q21 -λ→ q25 -λ→ q28 -λ→ q31 -λ→ q32 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 — ✘ termina fuera de F
2. `100`: {q0, q1, q14, q15, q2, q3, q4, q5, q6, q7, q8, q9} -1→ {q11, q13, q14, q15, q17, q18, q20, q24, q3, q4, q7, q8, q9} -0→ {q12, q14, q15, q18, q19, q23, q3, q4, q7, q8, q9} -0→ {q12, q14, q15, q18, q19, q23, q26, q29, q3, q32, q4, q7, q8, q9} — ✔
  Árbol de cómputo: 23 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q4 -λ→ q9 -λ→ q14 -0→ q19 -λ→ q23 -0→ q26 -λ→ q29 -λ→ q32 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 — ✘ termina fuera de F
3. `01100`: {q0, q1, q14, q15, q2, q3, q4, q5, q6, q7, q8, q9} -0→ {q10, q12, q14, q15, q16, q18, q19, q23, q3, q4, q7, q8, q9} -1→ {q13, q14, q15, q18, q20, q24, q3, q4, q7, q8, q9} -1→ {q13, q14, q15, q18, q20, q24, q27, q29, q3, q32, q4, q7, q8, q9} -0→ {q12, q14, q15, q18, q19, q23, q3, q4, q7, q8, q9} -0→ {q12, q14, q15, q18, q19, q23, q26, q29, q3, q32, q4, q7, q8, q9} — ✔
  Árbol de cómputo: 29 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q4 -λ→ q9 -λ→ q14 -0→ q19 -λ→ q23 -0→ q26 -λ→ q29 -λ→ q32 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 — ✘ muere tras leer `01`
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 — ✘ termina fuera de F
4. `1110011`: {q0, q1, q14, q15, q2, q3, q4, q5, q6, q7, q8, q9} -1→ {q11, q13, q14, q15, q17, q18, q20, q24, q3, q4, q7, q8, q9} -1→ {q13, q14, q15, q18, q20, q22, q24, q25, q27, q28, q29, q3, q30, q31, q32, q33, q34, q4, q7, q8, q9} -1→ {q13, q14, q15, q18, q20, q24, q27, q29, q3, q30, q31, q32, q33, q34, q36, q37, q4, q7, q8, q9} -0→ {q12, q14, q15, q18, q19, q23, q3, q30, q31, q32, q33, q34, q35, q37, q4, q7, q8, q9} -0→ {q12, q14, q15, q18, q19, q23, q26, q29, q3, q30, q31, q32, q33, q34, q35, q37, q4, q7, q8, q9} -1→ {q13, q14, q15, q18, q20, q24, q3, q30, q31, q32, q33, q34, q36, q37, q4, q7, q8, q9} -1→ {q13, q14, q15, q18, q20, q24, q27, q29, q3, q30, q31, q32, q33, q34, q36, q37, q4, q7, q8, q9} — ✔
  Árbol de cómputo: 51 caminos, 2 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q4 -λ→ q9 -λ→ q15 -1→ q20 -λ→ q24 -1→ q27 -λ→ q29 -λ→ q32 — ✔ acepta
    - q0 -λ→ q2 -λ→ q6 -1→ q11 -λ→ q17 -1→ q22 -λ→ q25 -λ→ q28 -λ→ q30 -λ→ q34 -1→ q36 -λ→ q37 -λ→ q30 -λ→ q33 -0→ q35 -λ→ q37 -λ→ q30 -λ→ q33 -0→ q35 -λ→ q37 -λ→ q30 -λ→ q34 -1→ q36 -λ→ q37 -λ→ q30 -λ→ q34 -1→ q36 -λ→ q37 -λ→ q31 -λ→ q32 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 — ✘ muere tras leer `1`
    - q0 -λ→ q1 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 — ✘ muere tras leer `11`
    - q0 -λ→ q1 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 — ✘ muere tras leer `11100`
5. `01000111100`: {q0, q1, q14, q15, q2, q3, q4, q5, q6, q7, q8, q9} -0→ {q10, q12, q14, q15, q16, q18, q19, q23, q3, q4, q7, q8, q9} -1→ {q13, q14, q15, q18, q20, q24, q3, q4, q7, q8, q9} -0→ {q12, q14, q15, q18, q19, q23, q3, q4, q7, q8, q9} -0→ {q12, q14, q15, q18, q19, q23, q26, q29, q3, q32, q4, q7, q8, q9} -0→ {q12, q14, q15, q18, q19, q23, q26, q29, q3, q32, q4, q7, q8, q9} -1→ {q13, q14, q15, q18, q20, q24, q3, q4, q7, q8, q9} -1→ {q13, q14, q15, q18, q20, q24, q27, q29, q3, q32, q4, q7, q8, q9} -1→ {q13, q14, q15, q18, q20, q24, q27, q29, q3, q32, q4, q7, q8, q9} -1→ {q13, q14, q15, q18, q20, q24, q27, q29, q3, q32, q4, q7, q8, q9} -0→ {q12, q14, q15, q18, q19, q23, q3, q4, q7, q8, q9} -0→ {q12, q14, q15, q18, q19, q23, q26, q29, q3, q32, q4, q7, q8, q9} — ✔
  Árbol de cómputo: 47 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q4 -λ→ q9 -λ→ q14 -0→ q19 -λ→ q23 -0→ q26 -λ→ q29 -λ→ q32 — ✔ acepta
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 — ✘ muere tras leer `01000`
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 — ✘ muere tras leer `010001`
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 — ✘ muere tras leer `0100011`
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 — ✘ muere tras leer `01000111`
6. λ: {q0, q1, q14, q15, q2, q3, q4, q5, q6, q7, q8, q9} — ✘
  Árbol de cómputo: 12 caminos, 0 de aceptación (se muestran 6):
    - q0 — ✘ termina fuera de F
    - q0 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -λ→ q8 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q4 — ✘ termina fuera de F
7. `10`: {q0, q1, q14, q15, q2, q3, q4, q5, q6, q7, q8, q9} -1→ {q11, q13, q14, q15, q17, q18, q20, q24, q3, q4, q7, q8, q9} -0→ {q12, q14, q15, q18, q19, q23, q3, q4, q7, q8, q9} — ✘
  Árbol de cómputo: 18 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q8 — ✘ termina fuera de F
8. `10110`: {q0, q1, q14, q15, q2, q3, q4, q5, q6, q7, q8, q9} -1→ {q11, q13, q14, q15, q17, q18, q20, q24, q3, q4, q7, q8, q9} -0→ {q12, q14, q15, q18, q19, q23, q3, q4, q7, q8, q9} -1→ {q13, q14, q15, q18, q20, q24, q3, q4, q7, q8, q9} -1→ {q13, q14, q15, q18, q20, q24, q27, q29, q3, q32, q4, q7, q8, q9} -0→ {q12, q14, q15, q18, q19, q23, q3, q4, q7, q8, q9} — ✘
  Árbol de cómputo: 27 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 — ✘ muere tras leer `10`
    - q0 -λ→ q1 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 — ✘ muere tras leer `101`
    - q0 -λ→ q1 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 — ✘ termina fuera de F
9. `10010110`: {q0, q1, q14, q15, q2, q3, q4, q5, q6, q7, q8, q9} -1→ {q11, q13, q14, q15, q17, q18, q20, q24, q3, q4, q7, q8, q9} -0→ {q12, q14, q15, q18, q19, q23, q3, q4, q7, q8, q9} -0→ {q12, q14, q15, q18, q19, q23, q26, q29, q3, q32, q4, q7, q8, q9} -1→ {q13, q14, q15, q18, q20, q24, q3, q4, q7, q8, q9} -0→ {q12, q14, q15, q18, q19, q23, q3, q4, q7, q8, q9} -1→ {q13, q14, q15, q18, q20, q24, q3, q4, q7, q8, q9} -1→ {q13, q14, q15, q18, q20, q24, q27, q29, q3, q32, q4, q7, q8, q9} -0→ {q12, q14, q15, q18, q19, q23, q3, q4, q7, q8, q9} — ✘
  Árbol de cómputo: 36 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 — ✘ muere tras leer `100`
    - q0 -λ→ q1 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 — ✘ muere tras leer `10010`
    - q0 -λ→ q1 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 — ✘ muere tras leer `100101`
    - q0 -λ→ q1 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 — ✘ termina fuera de F
    - q0 -λ→ q1 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 — ✘ termina fuera de F
10. `100110111001`: {q0, q1, q14, q15, q2, q3, q4, q5, q6, q7, q8, q9} -1→ {q11, q13, q14, q15, q17, q18, q20, q24, q3, q4, q7, q8, q9} -0→ {q12, q14, q15, q18, q19, q23, q3, q4, q7, q8, q9} -0→ {q12, q14, q15, q18, q19, q23, q26, q29, q3, q32, q4, q7, q8, q9} -1→ {q13, q14, q15, q18, q20, q24, q3, q4, q7, q8, q9} -1→ {q13, q14, q15, q18, q20, q24, q27, q29, q3, q32, q4, q7, q8, q9} -0→ {q12, q14, q15, q18, q19, q23, q3, q4, q7, q8, q9} -1→ {q13, q14, q15, q18, q20, q24, q3, q4, q7, q8, q9} -1→ {q13, q14, q15, q18, q20, q24, q27, q29, q3, q32, q4, q7, q8, q9} -1→ {q13, q14, q15, q18, q20, q24, q27, q29, q3, q32, q4, q7, q8, q9} -0→ {q12, q14, q15, q18, q19, q23, q3, q4, q7, q8, q9} -0→ {q12, q14, q15, q18, q19, q23, q26, q29, q3, q32, q4, q7, q8, q9} -1→ {q13, q14, q15, q18, q20, q24, q3, q4, q7, q8, q9} — ✘
  Árbol de cómputo: 48 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -λ→ q3 -λ→ q7 — ✘ muere tras leer λ
    - q0 -λ→ q1 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 — ✘ muere tras leer `100`
    - q0 -λ→ q1 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 — ✘ muere tras leer `1001`
    - q0 -λ→ q1 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 — ✘ muere tras leer `100110`
    - q0 -λ→ q1 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 — ✘ muere tras leer `1001101`
    - q0 -λ→ q1 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 -0→ q12 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q8 -1→ q13 -λ→ q18 -λ→ q3 -λ→ q7 — ✘ muere tras leer `10011011`

</details>

Simulación paso a paso en JFLAP con `00`: [ver captura](../../evidencias/jflap/pasos/L3-252.png).

**Conversión.** AFND-λ (38 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 34 estados, [`L3-252-AFND.jff`](../../automatas/conversiones/L3-252-AFND.jff). AFND (34 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 13 estados, [`L3-252-AFD.jff`](../../automatas/conversiones/L3-252-AFD.jff) ([.json](../../automatas/conversiones/L3-252-AFD.json), [.xml](../../automatas/conversiones/L3-252-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 13 estados, y el AFD mínimo (Hopcroft), 8. La cota es 2^34 = 17179869184. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-253"></a>

## Lista 3, problema 253

**Enunciado.** Encontrar un AFND-λ equivalente a la expresión regular (0+(11+00)*)(11+10+01)*(λ+110).

**Clasificación: AFND-λ.** Se pide explícitamente un AFND-λ equivalente a la expresión regular.

**Expresión:** `(0+(11+00)*)(11+10+01)*(λ+110)`.

#### AFND-λ de Thompson de (0+(11+00)*)(11+10+01)*(λ+110) — `L3-253`

Archivos: [`L3-253.jff`](../../automatas/lista3-afnd-lambda/L3-253.jff) · [`L3-253.json`](../../automatas/lista3-afnd-lambda/L3-253.json) · [`L3-253.xml`](../../automatas/lista3-afnd-lambda/L3-253.xml). Tipo según la definición: **AFND-lambda**, |Q| = 42, Σ = {0, 1}, 50 transiciones.

**Diseño.** Construcción de Thompson: el árbol de la expresión se recorre de abajo hacia arriba y cada operador combina los fragmentos de sus operandos (ver la tabla de reglas en este documento).

<details><summary>Tabla de transiciones (42 estados)</summary>

| Estado | 0 | 1 | λ |
|---|---|---|---|
| →q0 | ∅ | ∅ | {q1, q2} |
| q1 | {q3} | ∅ | ∅ |
| q3 | ∅ | ∅ | {q6} |
| q2 | ∅ | ∅ | {q4, q5} |
| q5 | ∅ | ∅ | {q7, q8} |
| q7 | ∅ | {q10} | ∅ |
| q10 | ∅ | ∅ | {q14} |
| q14 | ∅ | {q20} | ∅ |
| q20 | ∅ | ∅ | {q27} |
| q8 | {q11} | ∅ | ∅ |
| q11 | ∅ | ∅ | {q15} |
| q15 | {q21} | ∅ | ∅ |
| q21 | ∅ | ∅ | {q27} |
| q27 | ∅ | ∅ | {q4, q5} |
| q4 | ∅ | ∅ | {q6} |
| q6 | ∅ | ∅ | {q9} |
| q9 | ∅ | ∅ | {q12, q13} |
| q12 | ∅ | ∅ | {q16, q17, q18} |
| q16 | ∅ | {q22} | ∅ |
| q22 | ∅ | ∅ | {q28} |
| q28 | ∅ | {q33} | ∅ |
| q33 | ∅ | ∅ | {q38} |
| q17 | ∅ | {q23} | ∅ |
| q23 | ∅ | ∅ | {q29} |
| q29 | {q34} | ∅ | ∅ |
| q34 | ∅ | ∅ | {q38} |
| q18 | {q24} | ∅ | ∅ |
| q24 | ∅ | ∅ | {q30} |
| q30 | ∅ | {q35} | ∅ |
| q35 | ∅ | ∅ | {q38} |
| q38 | ∅ | ∅ | {q12, q13} |
| q13 | ∅ | ∅ | {q19} |
| q19 | ∅ | ∅ | {q25, q26} |
| q25 | ∅ | ∅ | {q31} |
| q31 | ∅ | ∅ | {q36} |
| q26 | ∅ | {q32} | ∅ |
| q32 | ∅ | ∅ | {q37} |
| q37 | ∅ | {q39} | ∅ |
| q39 | ∅ | ∅ | {q40} |
| q40 | {q41} | ∅ | ∅ |
| q41 | ∅ | ∅ | {q36} |
| *q36 | ∅ | ∅ | ∅ |

</details>

**Transiciones λ.** Thompson usa λ en tres lugares: dos de salida en cada unión (elegir alternativa), cuatro en cada estrella (entrar, repetir, salir, saltar) y una entre los fragmentos de cada concatenación. Ninguna consume símbolos, por eso la construcción es composicional.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

<details><summary>λ-clausuras de los 42 estados</summary>

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0, q1, q12, q13, q16, q17, q18, q19, q2, q25, q26, q31, q36, q4, q5, q6, q7, q8, q9} | sí |
| q1 | {q1} | no |
| q3 | {q12, q13, q16, q17, q18, q19, q25, q26, q3, q31, q36, q6, q9} | sí |
| q2 | {q12, q13, q16, q17, q18, q19, q2, q25, q26, q31, q36, q4, q5, q6, q7, q8, q9} | sí |
| q5 | {q5, q7, q8} | no |
| q7 | {q7} | no |
| q10 | {q10, q14} | no |
| q14 | {q14} | no |
| q20 | {q12, q13, q16, q17, q18, q19, q20, q25, q26, q27, q31, q36, q4, q5, q6, q7, q8, q9} | sí |
| q8 | {q8} | no |
| q11 | {q11, q15} | no |
| q15 | {q15} | no |
| q21 | {q12, q13, q16, q17, q18, q19, q21, q25, q26, q27, q31, q36, q4, q5, q6, q7, q8, q9} | sí |
| q27 | {q12, q13, q16, q17, q18, q19, q25, q26, q27, q31, q36, q4, q5, q6, q7, q8, q9} | sí |
| q4 | {q12, q13, q16, q17, q18, q19, q25, q26, q31, q36, q4, q6, q9} | sí |
| q6 | {q12, q13, q16, q17, q18, q19, q25, q26, q31, q36, q6, q9} | sí |
| q9 | {q12, q13, q16, q17, q18, q19, q25, q26, q31, q36, q9} | sí |
| q12 | {q12, q16, q17, q18} | no |
| q16 | {q16} | no |
| q22 | {q22, q28} | no |
| q28 | {q28} | no |
| q33 | {q12, q13, q16, q17, q18, q19, q25, q26, q31, q33, q36, q38} | sí |
| q17 | {q17} | no |
| q23 | {q23, q29} | no |
| q29 | {q29} | no |
| q34 | {q12, q13, q16, q17, q18, q19, q25, q26, q31, q34, q36, q38} | sí |
| q18 | {q18} | no |
| q24 | {q24, q30} | no |
| q30 | {q30} | no |
| q35 | {q12, q13, q16, q17, q18, q19, q25, q26, q31, q35, q36, q38} | sí |
| q38 | {q12, q13, q16, q17, q18, q19, q25, q26, q31, q36, q38} | sí |
| q13 | {q13, q19, q25, q26, q31, q36} | sí |
| q19 | {q19, q25, q26, q31, q36} | sí |
| q25 | {q25, q31, q36} | sí |
| q31 | {q31, q36} | sí |
| q26 | {q26} | no |
| q32 | {q32, q37} | no |
| q37 | {q37} | no |
| q39 | {q39, q40} | no |
| q40 | {q40} | no |
| q41 | {q36, q41} | sí |
| q36 | {q36} | sí |

</details>

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | acepta | acepta | acepta |
| 2 | `11` | acepta | acepta | acepta |
| 3 | `1010` | acepta | acepta | acepta |
| 4 | `10010101` | acepta | acepta | acepta |
| 5 | `000101101011` | acepta | acepta | acepta |
| 6 | `1` | rechaza | rechaza | rechaza |
| 7 | `0100` | rechaza | rechaza | rechaza |
| 8 | `11000` | rechaza | rechaza | — |
| 9 | `1100010` | rechaza | rechaza | rechaza |
| 10 | `11011110011` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: {q0, q1, q12, q13, q16, q17, q18, q19, q2, q25, q26, q31, q36, q4, q5, q6, q7, q8, q9} — ✔
  Árbol de cómputo: 19 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q9 -λ→ q13 -λ→ q19 -λ→ q25 -λ→ q31 -λ→ q36 — ✔ acepta
    - q0 — ✘ termina fuera de F
    - q0 -λ→ q1 — ✘ termina fuera de F
    - q0 -λ→ q2 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q4 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 — ✘ termina fuera de F
2. `11`: {q0, q1, q12, q13, q16, q17, q18, q19, q2, q25, q26, q31, q36, q4, q5, q6, q7, q8, q9} -1→ {q10, q14, q22, q23, q28, q29, q32, q37} -1→ {q12, q13, q16, q17, q18, q19, q20, q25, q26, q27, q31, q33, q36, q38, q39, q4, q40, q5, q6, q7, q8, q9} — ✔
  Árbol de cómputo: 37 caminos, 2 de aceptación (se muestran 6):
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q16 -1→ q22 -λ→ q28 -1→ q33 -λ→ q38 -λ→ q13 -λ→ q19 -λ→ q25 -λ→ q31 -λ→ q36 — ✔ acepta
    - q0 -λ→ q2 -λ→ q5 -λ→ q7 -1→ q10 -λ→ q14 -1→ q20 -λ→ q27 -λ→ q4 -λ→ q6 -λ→ q9 -λ→ q13 -λ→ q19 -λ→ q25 -λ→ q31 -λ→ q36 — ✔ acepta
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q16 -1→ q22 -λ→ q28 -1→ q33 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q16 -1→ q22 -λ→ q28 -1→ q33 -λ→ q38 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q16 -1→ q22 -λ→ q28 -1→ q33 -λ→ q38 -λ→ q12 — ✘ termina fuera de F
3. `1010`: {q0, q1, q12, q13, q16, q17, q18, q19, q2, q25, q26, q31, q36, q4, q5, q6, q7, q8, q9} -1→ {q10, q14, q22, q23, q28, q29, q32, q37} -0→ {q12, q13, q16, q17, q18, q19, q25, q26, q31, q34, q36, q38} -1→ {q22, q23, q28, q29, q32, q37} -0→ {q12, q13, q16, q17, q18, q19, q25, q26, q31, q34, q36, q38} — ✔
  Árbol de cómputo: 23 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q17 -1→ q23 -λ→ q29 -0→ q34 -λ→ q38 -λ→ q12 -λ→ q17 -1→ q23 -λ→ q29 -0→ q34 -λ→ q38 -λ→ q13 -λ→ q19 -λ→ q25 -λ→ q31 -λ→ q36 — ✔ acepta
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q16 -1→ q22 -λ→ q28 — ✘ muere tras leer `1`
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q17 -1→ q23 -λ→ q29 -0→ q34 -λ→ q38 -λ→ q12 -λ→ q16 -1→ q22 -λ→ q28 — ✘ muere tras leer `101`
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q17 -1→ q23 -λ→ q29 -0→ q34 -λ→ q38 -λ→ q12 -λ→ q17 -1→ q23 -λ→ q29 -0→ q34 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q17 -1→ q23 -λ→ q29 -0→ q34 -λ→ q38 -λ→ q12 -λ→ q17 -1→ q23 -λ→ q29 -0→ q34 -λ→ q38 — ✘ termina fuera de F
4. `10010101`: {q0, q1, q12, q13, q16, q17, q18, q19, q2, q25, q26, q31, q36, q4, q5, q6, q7, q8, q9} -1→ {q10, q14, q22, q23, q28, q29, q32, q37} -0→ {q12, q13, q16, q17, q18, q19, q25, q26, q31, q34, q36, q38} -0→ {q24, q30} -1→ {q12, q13, q16, q17, q18, q19, q25, q26, q31, q35, q36, q38} -0→ {q24, q30} -1→ {q12, q13, q16, q17, q18, q19, q25, q26, q31, q35, q36, q38} -0→ {q24, q30} -1→ {q12, q13, q16, q17, q18, q19, q25, q26, q31, q35, q36, q38} — ✔
  Árbol de cómputo: 31 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q17 -1→ q23 -λ→ q29 -0→ q34 -λ→ q38 -λ→ q12 -λ→ q18 -0→ q24 -λ→ q30 -1→ q35 -λ→ q38 -λ→ q12 -λ→ q18 -0→ q24 -λ→ q30 -1→ q35 -λ→ q38 -λ→ q12 -λ→ q18 -0→ q24 -λ→ q30 -1→ q35 -λ→ q38 -λ→ q13 -λ→ q19 -λ→ q25 -λ→ q31 -λ→ q36 — ✔ acepta
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q16 -1→ q22 -λ→ q28 — ✘ muere tras leer `1`
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q17 -1→ q23 -λ→ q29 -0→ q34 -λ→ q38 -λ→ q12 -λ→ q16 — ✘ muere tras leer `10`
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q17 -1→ q23 -λ→ q29 -0→ q34 -λ→ q38 -λ→ q12 -λ→ q17 — ✘ muere tras leer `10`
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q17 -1→ q23 -λ→ q29 -0→ q34 -λ→ q38 -λ→ q12 -λ→ q18 -0→ q24 -λ→ q30 -1→ q35 -λ→ q38 -λ→ q12 -λ→ q16 — ✘ muere tras leer `1001`
5. `000101101011`: {q0, q1, q12, q13, q16, q17, q18, q19, q2, q25, q26, q31, q36, q4, q5, q6, q7, q8, q9} -0→ {q11, q12, q13, q15, q16, q17, q18, q19, q24, q25, q26, q3, q30, q31, q36, q6, q9} -0→ {q12, q13, q16, q17, q18, q19, q21, q24, q25, q26, q27, q30, q31, q36, q4, q5, q6, q7, q8, q9} -0→ {q11, q15, q24, q30} -1→ {q12, q13, q16, q17, q18, q19, q25, q26, q31, q35, q36, q38} -0→ {q24, q30} -1→ {q12, q13, q16, q17, q18, q19, q25, q26, q31, q35, q36, q38} -1→ {q22, q23, q28, q29, q32, q37} -0→ {q12, q13, q16, q17, q18, q19, q25, q26, q31, q34, q36, q38} -1→ {q22, q23, q28, q29, q32, q37} -0→ {q12, q13, q16, q17, q18, q19, q25, q26, q31, q34, q36, q38} -1→ {q22, q23, q28, q29, q32, q37} -1→ {q12, q13, q16, q17, q18, q19, q25, q26, q31, q33, q36, q38, q39, q40} — ✔
  Árbol de cómputo: 46 caminos, 1 de aceptación (se muestran 6):
    - q0 -λ→ q2 -λ→ q5 -λ→ q8 -0→ q11 -λ→ q15 -0→ q21 -λ→ q27 -λ→ q4 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q18 -0→ q24 -λ→ q30 -1→ q35 -λ→ q38 -λ→ q12 -λ→ q18 -0→ q24 -λ→ q30 -1→ q35 -λ→ q38 -λ→ q12 -λ→ q17 -1→ q23 -λ→ q29 -0→ q34 -λ→ q38 -λ→ q12 -λ→ q17 -1→ q23 -λ→ q29 -0→ q34 -λ→ q38 -λ→ q12 -λ→ q16 -1→ q22 -λ→ q28 -1→ q33 -λ→ q38 -λ→ q13 -λ→ q19 -λ→ q25 -λ→ q31 -λ→ q36 — ✔ acepta
    - q0 -λ→ q1 -0→ q3 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q16 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -0→ q3 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q17 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -0→ q3 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q18 -0→ q24 -λ→ q30 — ✘ muere tras leer `00`
    - q0 -λ→ q1 -0→ q3 -λ→ q6 -λ→ q9 -λ→ q13 -λ→ q19 -λ→ q25 -λ→ q31 -λ→ q36 — ✘ muere tras leer `0`
    - q0 -λ→ q1 -0→ q3 -λ→ q6 -λ→ q9 -λ→ q13 -λ→ q19 -λ→ q26 — ✘ muere tras leer `0`
6. `1`: {q0, q1, q12, q13, q16, q17, q18, q19, q2, q25, q26, q31, q36, q4, q5, q6, q7, q8, q9} -1→ {q10, q14, q22, q23, q28, q29, q32, q37} — ✘
  Árbol de cómputo: 12 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q16 -1→ q22 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q16 -1→ q22 -λ→ q28 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q17 -1→ q23 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q17 -1→ q23 -λ→ q29 — ✘ termina fuera de F
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q18 — ✘ muere tras leer λ
7. `0100`: {q0, q1, q12, q13, q16, q17, q18, q19, q2, q25, q26, q31, q36, q4, q5, q6, q7, q8, q9} -0→ {q11, q12, q13, q15, q16, q17, q18, q19, q24, q25, q26, q3, q30, q31, q36, q6, q9} -1→ {q12, q13, q16, q17, q18, q19, q22, q23, q25, q26, q28, q29, q31, q32, q35, q36, q37, q38} -0→ {q12, q13, q16, q17, q18, q19, q24, q25, q26, q30, q31, q34, q36, q38} -0→ {q24, q30} — ✘
  Árbol de cómputo: 21 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 -0→ q3 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q16 -1→ q22 -λ→ q28 — ✘ muere tras leer `01`
    - q0 -λ→ q1 -0→ q3 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q17 -1→ q23 -λ→ q29 -0→ q34 -λ→ q38 -λ→ q12 -λ→ q16 — ✘ muere tras leer `010`
    - q0 -λ→ q1 -0→ q3 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q17 -1→ q23 -λ→ q29 -0→ q34 -λ→ q38 -λ→ q12 -λ→ q17 — ✘ muere tras leer `010`
    - q0 -λ→ q1 -0→ q3 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q17 -1→ q23 -λ→ q29 -0→ q34 -λ→ q38 -λ→ q12 -λ→ q18 -0→ q24 — ✘ termina fuera de F
    - q0 -λ→ q1 -0→ q3 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q17 -1→ q23 -λ→ q29 -0→ q34 -λ→ q38 -λ→ q12 -λ→ q18 -0→ q24 -λ→ q30 — ✘ termina fuera de F
    - q0 -λ→ q1 -0→ q3 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q17 -1→ q23 -λ→ q29 -0→ q34 -λ→ q38 -λ→ q13 -λ→ q19 -λ→ q25 -λ→ q31 -λ→ q36 — ✘ muere tras leer `010`
8. `11000`: {q0, q1, q12, q13, q16, q17, q18, q19, q2, q25, q26, q31, q36, q4, q5, q6, q7, q8, q9} -1→ {q10, q14, q22, q23, q28, q29, q32, q37} -1→ {q12, q13, q16, q17, q18, q19, q20, q25, q26, q27, q31, q33, q36, q38, q39, q4, q40, q5, q6, q7, q8, q9} -0→ {q11, q15, q24, q30, q36, q41} -0→ {q12, q13, q16, q17, q18, q19, q21, q25, q26, q27, q31, q36, q4, q5, q6, q7, q8, q9} -0→ {q11, q15, q24, q30} — ✘
  Árbol de cómputo: 26 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q16 -1→ q22 -λ→ q28 -1→ q33 -λ→ q38 -λ→ q12 -λ→ q16 — ✘ muere tras leer `11`
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q16 -1→ q22 -λ→ q28 -1→ q33 -λ→ q38 -λ→ q12 -λ→ q17 — ✘ muere tras leer `11`
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q16 -1→ q22 -λ→ q28 -1→ q33 -λ→ q38 -λ→ q12 -λ→ q18 -0→ q24 -λ→ q30 — ✘ muere tras leer `110`
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q16 -1→ q22 -λ→ q28 -1→ q33 -λ→ q38 -λ→ q13 -λ→ q19 -λ→ q25 -λ→ q31 -λ→ q36 — ✘ muere tras leer `11`
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q16 -1→ q22 -λ→ q28 -1→ q33 -λ→ q38 -λ→ q13 -λ→ q19 -λ→ q26 — ✘ muere tras leer `11`
9. `1100010`: {q0, q1, q12, q13, q16, q17, q18, q19, q2, q25, q26, q31, q36, q4, q5, q6, q7, q8, q9} -1→ {q10, q14, q22, q23, q28, q29, q32, q37} -1→ {q12, q13, q16, q17, q18, q19, q20, q25, q26, q27, q31, q33, q36, q38, q39, q4, q40, q5, q6, q7, q8, q9} -0→ {q11, q15, q24, q30, q36, q41} -0→ {q12, q13, q16, q17, q18, q19, q21, q25, q26, q27, q31, q36, q4, q5, q6, q7, q8, q9} -0→ {q11, q15, q24, q30} -1→ {q12, q13, q16, q17, q18, q19, q25, q26, q31, q35, q36, q38} -0→ {q24, q30} — ✘
  Árbol de cómputo: 29 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q16 -1→ q22 -λ→ q28 -1→ q33 -λ→ q38 -λ→ q12 -λ→ q16 — ✘ muere tras leer `11`
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q16 -1→ q22 -λ→ q28 -1→ q33 -λ→ q38 -λ→ q12 -λ→ q17 — ✘ muere tras leer `11`
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q16 -1→ q22 -λ→ q28 -1→ q33 -λ→ q38 -λ→ q12 -λ→ q18 -0→ q24 -λ→ q30 — ✘ muere tras leer `110`
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q16 -1→ q22 -λ→ q28 -1→ q33 -λ→ q38 -λ→ q13 -λ→ q19 -λ→ q25 -λ→ q31 -λ→ q36 — ✘ muere tras leer `11`
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q16 -1→ q22 -λ→ q28 -1→ q33 -λ→ q38 -λ→ q13 -λ→ q19 -λ→ q26 — ✘ muere tras leer `11`
10. `11011110011`: {q0, q1, q12, q13, q16, q17, q18, q19, q2, q25, q26, q31, q36, q4, q5, q6, q7, q8, q9} -1→ {q10, q14, q22, q23, q28, q29, q32, q37} -1→ {q12, q13, q16, q17, q18, q19, q20, q25, q26, q27, q31, q33, q36, q38, q39, q4, q40, q5, q6, q7, q8, q9} -0→ {q11, q15, q24, q30, q36, q41} -1→ {q12, q13, q16, q17, q18, q19, q25, q26, q31, q35, q36, q38} -1→ {q22, q23, q28, q29, q32, q37} -1→ {q12, q13, q16, q17, q18, q19, q25, q26, q31, q33, q36, q38, q39, q40} -1→ {q22, q23, q28, q29, q32, q37} -0→ {q12, q13, q16, q17, q18, q19, q25, q26, q31, q34, q36, q38} -0→ {q24, q30} -1→ {q12, q13, q16, q17, q18, q19, q25, q26, q31, q35, q36, q38} -1→ {q22, q23, q28, q29, q32, q37} — ✘
  Árbol de cómputo: 56 caminos, 0 de aceptación (se muestran 6):
    - q0 -λ→ q1 — ✘ muere tras leer λ
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q16 -1→ q22 -λ→ q28 -1→ q33 -λ→ q38 -λ→ q12 -λ→ q16 — ✘ muere tras leer `11`
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q16 -1→ q22 -λ→ q28 -1→ q33 -λ→ q38 -λ→ q12 -λ→ q17 — ✘ muere tras leer `11`
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q16 -1→ q22 -λ→ q28 -1→ q33 -λ→ q38 -λ→ q12 -λ→ q18 -0→ q24 -λ→ q30 -1→ q35 -λ→ q38 -λ→ q12 -λ→ q16 -1→ q22 -λ→ q28 -1→ q33 -λ→ q38 -λ→ q12 -λ→ q16 -1→ q22 -λ→ q28 — ✘ muere tras leer `1101111`
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q16 -1→ q22 -λ→ q28 -1→ q33 -λ→ q38 -λ→ q12 -λ→ q18 -0→ q24 -λ→ q30 -1→ q35 -λ→ q38 -λ→ q12 -λ→ q16 -1→ q22 -λ→ q28 -1→ q33 -λ→ q38 -λ→ q12 -λ→ q17 -1→ q23 -λ→ q29 -0→ q34 -λ→ q38 -λ→ q12 -λ→ q16 — ✘ muere tras leer `11011110`
    - q0 -λ→ q2 -λ→ q4 -λ→ q6 -λ→ q9 -λ→ q12 -λ→ q16 -1→ q22 -λ→ q28 -1→ q33 -λ→ q38 -λ→ q12 -λ→ q18 -0→ q24 -λ→ q30 -1→ q35 -λ→ q38 -λ→ q12 -λ→ q16 -1→ q22 -λ→ q28 -1→ q33 -λ→ q38 -λ→ q12 -λ→ q17 -1→ q23 -λ→ q29 -0→ q34 -λ→ q38 -λ→ q12 -λ→ q17 — ✘ muere tras leer `11011110`

</details>

Simulación paso a paso en JFLAP con `11`: [ver captura](../../evidencias/jflap/pasos/L3-253.png).

**Conversión.** AFND-λ (42 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 40 estados, [`L3-253-AFND.jff`](../../automatas/conversiones/L3-253-AFND.jff). AFND (40 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 22 estados, [`L3-253-AFD.jff`](../../automatas/conversiones/L3-253-AFD.jff) ([.json](../../automatas/conversiones/L3-253-AFD.json), [.xml](../../automatas/conversiones/L3-253-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 23 estados, y el AFD mínimo (Hopcroft), 18. La cota es 2^40 = 1099511627776. Se verificó que los tres autómatas aceptan el mismo lenguaje.

