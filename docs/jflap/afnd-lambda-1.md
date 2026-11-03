# Ejercicio 2 — AFND-λ (problemas 162-200)

[← Ejercicio 2](../02-jflap.md) · [Índice](../../README.md)

Cada autómata indica su clasificación, el diseño, la tabla de transiciones, cinco cadenas válidas y cinco inválidas con el resultado esperado (oráculo escrito a partir del enunciado), el del simulador de este proyecto y el del motor de JFLAP 7.1, el recorrido de cada cadena (en los no deterministas, el conjunto de estados activos y el árbol de caminos) y la captura de la simulación paso a paso en JFLAP.

<a id="problema-3-162-188-p-108"></a>

## Lista 3, problema 162-188 (p. 108)

**Enunciado.** AFN para el problema 108 de la Lista 2: Las palabras de Σ₂ que incluyen al menos una vez abbcb y al menos una vez cbaabb, sin traslape (abbcbaabb no pertenece).

**Clasificación: AFND-λ.** Se resolvió con transiciones λ: componen el autómata a partir de piezas (unión o concatenación) sin consumir símbolos.

#### AFND-λ — `L3-AFNDL-p108`

Archivos: [`L3-AFNDL-p108.jff`](../../automatas/lista3-afnd-lambda/L3-AFNDL-p108.jff) · [`L3-AFNDL-p108.json`](../../automatas/lista3-afnd-lambda/L3-AFNDL-p108.json) · [`L3-AFNDL-p108.xml`](../../automatas/lista3-afnd-lambda/L3-AFNDL-p108.xml). Tipo según la definición: **AFND-lambda**, |Q| = 26, Σ = {a, b, c, 0, 1}, 56 transiciones.

**Diseño.** Unión de dos órdenes: desde i, una transición λ elige la rama x (primero abbcb, luego cbaabb) y otra la rama y (al revés). En cada rama, los lazos con Σ₂ adivinan dónde empieza cada patrón; los patrones son cadenas lineales separadas, así que no pueden traslaparse. Las ramas se reúnen en f con otra λ.

<details><summary>Tabla de transiciones (26 estados)</summary>

| Estado | a | b | c | 0 | 1 | λ |
|---|---|---|---|---|---|---|
| →i | ∅ | ∅ | ∅ | ∅ | ∅ | {x0, y0} |
| x0 | {x0, x1} | {x0} | {x0} | {x0} | {x0} | ∅ |
| x1 | ∅ | {x2} | ∅ | ∅ | ∅ | ∅ |
| x2 | ∅ | {x3} | ∅ | ∅ | ∅ | ∅ |
| x3 | ∅ | ∅ | {x4} | ∅ | ∅ | ∅ |
| x4 | ∅ | {x5} | ∅ | ∅ | ∅ | ∅ |
| x5 | {x5} | {x5} | {x5, x6} | {x5} | {x5} | ∅ |
| x6 | ∅ | {x7} | ∅ | ∅ | ∅ | ∅ |
| x7 | {x8} | ∅ | ∅ | ∅ | ∅ | ∅ |
| x8 | {x9} | ∅ | ∅ | ∅ | ∅ | ∅ |
| x9 | ∅ | {x10} | ∅ | ∅ | ∅ | ∅ |
| x10 | ∅ | {x11} | ∅ | ∅ | ∅ | ∅ |
| x11 | {x11} | {x11} | {x11} | {x11} | {x11} | {f} |
| y0 | {y0} | {y0} | {y0, y1} | {y0} | {y0} | ∅ |
| y1 | ∅ | {y2} | ∅ | ∅ | ∅ | ∅ |
| y2 | {y3} | ∅ | ∅ | ∅ | ∅ | ∅ |
| y3 | {y4} | ∅ | ∅ | ∅ | ∅ | ∅ |
| y4 | ∅ | {y5} | ∅ | ∅ | ∅ | ∅ |
| y5 | ∅ | {y6} | ∅ | ∅ | ∅ | ∅ |
| y6 | {y6, y7} | {y6} | {y6} | {y6} | {y6} | ∅ |
| y7 | ∅ | {y8} | ∅ | ∅ | ∅ | ∅ |
| y8 | ∅ | {y9} | ∅ | ∅ | ∅ | ∅ |
| y9 | ∅ | ∅ | {y10} | ∅ | ∅ | ∅ |
| y10 | ∅ | {y11} | ∅ | ∅ | ∅ | ∅ |
| y11 | {y11} | {y11} | {y11} | {y11} | {y11} | {f} |
| *f | ∅ | ∅ | ∅ | ∅ | ∅ | ∅ |

</details>

**Transiciones λ.** Las dos λ de salida de i implementan la unión (el autómata «elige» el orden sin consumir símbolos) y las dos λ de llegada a f la cierran en un único estado de aceptación. Sin ellas habría que duplicar el lazo de q0 en cada rama o tener dos estados iniciales, que la definición no permite.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

<details><summary>λ-clausuras de los 26 estados</summary>

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| i | {i, x0, y0} | no |
| x0 | {x0} | no |
| x1 | {x1} | no |
| x2 | {x2} | no |
| x3 | {x3} | no |
| x4 | {x4} | no |
| x5 | {x5} | no |
| x6 | {x6} | no |
| x7 | {x7} | no |
| x8 | {x8} | no |
| x9 | {x9} | no |
| x10 | {x10} | no |
| x11 | {f, x11} | sí |
| y0 | {y0} | no |
| y1 | {y1} | no |
| y2 | {y2} | no |
| y3 | {y3} | no |
| y4 | {y4} | no |
| y5 | {y5} | no |
| y6 | {y6} | no |
| y7 | {y7} | no |
| y8 | {y8} | no |
| y9 | {y9} | no |
| y10 | {y10} | no |
| y11 | {f, y11} | sí |
| f | {f} | sí |

</details>

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `abbcbcbaabb` | acepta | acepta | acepta |
| 2 | `01abbcbcbaabb` | acepta | acepta | acepta |
| 3 | `caacbaabbabbcb` | acepta | acepta | acepta |
| 4 | `bb0ab1abbcbcbaabb` | acepta | acepta | acepta |
| 5 | `11a1c0aabb0abbcbcbaabb` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `b1` | rechaza | rechaza | rechaza |
| 8 | `c1cc` | rechaza | rechaza | rechaza |
| 9 | `b0aaab1` | rechaza | rechaza | rechaza |
| 10 | `aaacab1b10b` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `abbcbcbaabb`: {i, x0, y0} -a→ {x0, x1, y0} -b→ {x0, x2, y0} -b→ {x0, x3, y0} -c→ {x0, x4, y0, y1} -b→ {x0, x5, y0, y2} -c→ {x0, x5, x6, y0, y1} -b→ {x0, x5, x7, y0, y2} -a→ {x0, x1, x5, x8, y0, y3} -a→ {x0, x1, x5, x9, y0, y4} -b→ {x0, x10, x2, x5, y0, y5} -b→ {f, x0, x11, x3, x5, y0, y6} — ✔
  Árbol de cómputo: 9 caminos, 1 de aceptación (se muestran 6):
    - i -λ→ x0 -a→ x1 -b→ x2 -b→ x3 -c→ x4 -b→ x5 -c→ x6 -b→ x7 -a→ x8 -a→ x9 -b→ x10 -b→ x11 -λ→ f — ✔ acepta
    - i -λ→ x0 -a→ x0 -b→ x0 -b→ x0 -c→ x0 -b→ x0 -c→ x0 -b→ x0 -a→ x0 -a→ x0 -b→ x0 -b→ x0 — ✘ termina fuera de F
    - i -λ→ x0 -a→ x0 -b→ x0 -b→ x0 -c→ x0 -b→ x0 -c→ x0 -b→ x0 -a→ x0 -a→ x1 -b→ x2 -b→ x3 — ✘ termina fuera de F
    - i -λ→ x0 -a→ x0 -b→ x0 -b→ x0 -c→ x0 -b→ x0 -c→ x0 -b→ x0 -a→ x1 — ✘ muere tras leer `abbcbcba`
    - i -λ→ x0 -a→ x1 -b→ x2 -b→ x3 -c→ x4 -b→ x5 -c→ x5 -b→ x5 -a→ x5 -a→ x5 -b→ x5 -b→ x5 — ✘ termina fuera de F
    - i -λ→ x0 -a→ x1 -b→ x2 -b→ x3 -c→ x4 -b→ x5 -c→ x6 -b→ x7 -a→ x8 -a→ x9 -b→ x10 -b→ x11 — ✘ termina fuera de F
2. `01abbcbcbaabb`: {i, x0, y0} -0→ {x0, y0} -1→ {x0, y0} -a→ {x0, x1, y0} -b→ {x0, x2, y0} -b→ {x0, x3, y0} -c→ {x0, x4, y0, y1} -b→ {x0, x5, y0, y2} -c→ {x0, x5, x6, y0, y1} -b→ {x0, x5, x7, y0, y2} -a→ {x0, x1, x5, x8, y0, y3} -a→ {x0, x1, x5, x9, y0, y4} -b→ {x0, x10, x2, x5, y0, y5} -b→ {f, x0, x11, x3, x5, y0, y6} — ✔
  Árbol de cómputo: 9 caminos, 1 de aceptación (se muestran 6):
    - i -λ→ x0 -0→ x0 -1→ x0 -a→ x1 -b→ x2 -b→ x3 -c→ x4 -b→ x5 -c→ x6 -b→ x7 -a→ x8 -a→ x9 -b→ x10 -b→ x11 -λ→ f — ✔ acepta
    - i -λ→ x0 -0→ x0 -1→ x0 -a→ x0 -b→ x0 -b→ x0 -c→ x0 -b→ x0 -c→ x0 -b→ x0 -a→ x0 -a→ x0 -b→ x0 -b→ x0 — ✘ termina fuera de F
    - i -λ→ x0 -0→ x0 -1→ x0 -a→ x0 -b→ x0 -b→ x0 -c→ x0 -b→ x0 -c→ x0 -b→ x0 -a→ x0 -a→ x1 -b→ x2 -b→ x3 — ✘ termina fuera de F
    - i -λ→ x0 -0→ x0 -1→ x0 -a→ x0 -b→ x0 -b→ x0 -c→ x0 -b→ x0 -c→ x0 -b→ x0 -a→ x1 — ✘ muere tras leer `01abbcbcba`
    - i -λ→ x0 -0→ x0 -1→ x0 -a→ x1 -b→ x2 -b→ x3 -c→ x4 -b→ x5 -c→ x5 -b→ x5 -a→ x5 -a→ x5 -b→ x5 -b→ x5 — ✘ termina fuera de F
    - i -λ→ x0 -0→ x0 -1→ x0 -a→ x1 -b→ x2 -b→ x3 -c→ x4 -b→ x5 -c→ x6 -b→ x7 -a→ x8 -a→ x9 -b→ x10 -b→ x11 — ✘ termina fuera de F
3. `caacbaabbabbcb`: {i, x0, y0} -c→ {x0, y0, y1} -a→ {x0, x1, y0} -a→ {x0, x1, y0} -c→ {x0, y0, y1} -b→ {x0, y0, y2} -a→ {x0, x1, y0, y3} -a→ {x0, x1, y0, y4} -b→ {x0, x2, y0, y5} -b→ {x0, x3, y0, y6} -a→ {x0, x1, y0, y6, y7} -b→ {x0, x2, y0, y6, y8} -b→ {x0, x3, y0, y6, y9} -c→ {x0, x4, y0, y1, y10, y6} -b→ {f, x0, x5, y0, y11, y2, y6} — ✔
  Árbol de cómputo: 12 caminos, 1 de aceptación (se muestran 6):
    - i -λ→ y0 -c→ y0 -a→ y0 -a→ y0 -c→ y1 -b→ y2 -a→ y3 -a→ y4 -b→ y5 -b→ y6 -a→ y7 -b→ y8 -b→ y9 -c→ y10 -b→ y11 -λ→ f — ✔ acepta
    - i -λ→ x0 -c→ x0 -a→ x0 -a→ x0 -c→ x0 -b→ x0 -a→ x0 -a→ x0 -b→ x0 -b→ x0 -a→ x0 -b→ x0 -b→ x0 -c→ x0 -b→ x0 — ✘ termina fuera de F
    - i -λ→ x0 -c→ x0 -a→ x0 -a→ x0 -c→ x0 -b→ x0 -a→ x0 -a→ x0 -b→ x0 -b→ x0 -a→ x1 -b→ x2 -b→ x3 -c→ x4 -b→ x5 — ✘ termina fuera de F
    - i -λ→ x0 -c→ x0 -a→ x0 -a→ x0 -c→ x0 -b→ x0 -a→ x0 -a→ x1 -b→ x2 -b→ x3 — ✘ muere tras leer `caacbaabb`
    - i -λ→ x0 -c→ x0 -a→ x0 -a→ x0 -c→ x0 -b→ x0 -a→ x1 — ✘ muere tras leer `caacba`
    - i -λ→ x0 -c→ x0 -a→ x0 -a→ x1 — ✘ muere tras leer `caa`
4. `bb0ab1abbcbcbaabb`: {i, x0, y0} -b→ {x0, y0} -b→ {x0, y0} -0→ {x0, y0} -a→ {x0, x1, y0} -b→ {x0, x2, y0} -1→ {x0, y0} -a→ {x0, x1, y0} -b→ {x0, x2, y0} -b→ {x0, x3, y0} -c→ {x0, x4, y0, y1} -b→ {x0, x5, y0, y2} -c→ {x0, x5, x6, y0, y1} -b→ {x0, x5, x7, y0, y2} -a→ {x0, x1, x5, x8, y0, y3} -a→ {x0, x1, x5, x9, y0, y4} -b→ {x0, x10, x2, x5, y0, y5} -b→ {f, x0, x11, x3, x5, y0, y6} — ✔
  Árbol de cómputo: 10 caminos, 1 de aceptación (se muestran 6):
    - i -λ→ x0 -b→ x0 -b→ x0 -0→ x0 -a→ x0 -b→ x0 -1→ x0 -a→ x1 -b→ x2 -b→ x3 -c→ x4 -b→ x5 -c→ x6 -b→ x7 -a→ x8 -a→ x9 -b→ x10 -b→ x11 -λ→ f — ✔ acepta
    - i -λ→ x0 -b→ x0 -b→ x0 -0→ x0 -a→ x0 -b→ x0 -1→ x0 -a→ x0 -b→ x0 -b→ x0 -c→ x0 -b→ x0 -c→ x0 -b→ x0 -a→ x0 -a→ x0 -b→ x0 -b→ x0 — ✘ termina fuera de F
    - i -λ→ x0 -b→ x0 -b→ x0 -0→ x0 -a→ x0 -b→ x0 -1→ x0 -a→ x0 -b→ x0 -b→ x0 -c→ x0 -b→ x0 -c→ x0 -b→ x0 -a→ x0 -a→ x1 -b→ x2 -b→ x3 — ✘ termina fuera de F
    - i -λ→ x0 -b→ x0 -b→ x0 -0→ x0 -a→ x0 -b→ x0 -1→ x0 -a→ x0 -b→ x0 -b→ x0 -c→ x0 -b→ x0 -c→ x0 -b→ x0 -a→ x1 — ✘ muere tras leer `bb0ab1abbcbcba`
    - i -λ→ x0 -b→ x0 -b→ x0 -0→ x0 -a→ x0 -b→ x0 -1→ x0 -a→ x1 -b→ x2 -b→ x3 -c→ x4 -b→ x5 -c→ x5 -b→ x5 -a→ x5 -a→ x5 -b→ x5 -b→ x5 — ✘ termina fuera de F
    - i -λ→ x0 -b→ x0 -b→ x0 -0→ x0 -a→ x0 -b→ x0 -1→ x0 -a→ x1 -b→ x2 -b→ x3 -c→ x4 -b→ x5 -c→ x6 -b→ x7 -a→ x8 -a→ x9 -b→ x10 -b→ x11 — ✘ termina fuera de F
5. `11a1c0aabb0abbcbcbaabb`: {i, x0, y0} -1→ {x0, y0} -1→ {x0, y0} -a→ {x0, x1, y0} -1→ {x0, y0} -c→ {x0, y0, y1} -0→ {x0, y0} -a→ {x0, x1, y0} -a→ {x0, x1, y0} -b→ {x0, x2, y0} -b→ {x0, x3, y0} -0→ {x0, y0} -a→ {x0, x1, y0} -b→ {x0, x2, y0} -b→ {x0, x3, y0} -c→ {x0, x4, y0, y1} -b→ {x0, x5, y0, y2} -c→ {x0, x5, x6, y0, y1} -b→ {x0, x5, x7, y0, y2} -a→ {x0, x1, x5, x8, y0, y3} -a→ {x0, x1, x5, x9, y0, y4} -b→ {x0, x10, x2, x5, y0, y5} -b→ {f, x0, x11, x3, x5, y0, y6} — ✔
  Árbol de cómputo: 13 caminos, 1 de aceptación (se muestran 6):
    - i -λ→ x0 -1→ x0 -1→ x0 -a→ x0 -1→ x0 -c→ x0 -0→ x0 -a→ x0 -a→ x0 -b→ x0 -b→ x0 -0→ x0 -a→ x1 -b→ x2 -b→ x3 -c→ x4 -b→ x5 -c→ x6 -b→ x7 -a→ x8 -a→ x9 -b→ x10 -b→ x11 -λ→ f — ✔ acepta
    - i -λ→ x0 -1→ x0 -1→ x0 -a→ x0 -1→ x0 -c→ x0 -0→ x0 -a→ x0 -a→ x0 -b→ x0 -b→ x0 -0→ x0 -a→ x0 -b→ x0 -b→ x0 -c→ x0 -b→ x0 -c→ x0 -b→ x0 -a→ x0 -a→ x0 -b→ x0 -b→ x0 — ✘ termina fuera de F
    - i -λ→ x0 -1→ x0 -1→ x0 -a→ x0 -1→ x0 -c→ x0 -0→ x0 -a→ x0 -a→ x0 -b→ x0 -b→ x0 -0→ x0 -a→ x0 -b→ x0 -b→ x0 -c→ x0 -b→ x0 -c→ x0 -b→ x0 -a→ x0 -a→ x1 -b→ x2 -b→ x3 — ✘ termina fuera de F
    - i -λ→ x0 -1→ x0 -1→ x0 -a→ x0 -1→ x0 -c→ x0 -0→ x0 -a→ x0 -a→ x0 -b→ x0 -b→ x0 -0→ x0 -a→ x0 -b→ x0 -b→ x0 -c→ x0 -b→ x0 -c→ x0 -b→ x0 -a→ x1 — ✘ muere tras leer `11a1c0aabb0abbcbcba`
    - i -λ→ x0 -1→ x0 -1→ x0 -a→ x0 -1→ x0 -c→ x0 -0→ x0 -a→ x0 -a→ x0 -b→ x0 -b→ x0 -0→ x0 -a→ x1 -b→ x2 -b→ x3 -c→ x4 -b→ x5 -c→ x5 -b→ x5 -a→ x5 -a→ x5 -b→ x5 -b→ x5 — ✘ termina fuera de F
    - i -λ→ x0 -1→ x0 -1→ x0 -a→ x0 -1→ x0 -c→ x0 -0→ x0 -a→ x0 -a→ x0 -b→ x0 -b→ x0 -0→ x0 -a→ x1 -b→ x2 -b→ x3 -c→ x4 -b→ x5 -c→ x6 -b→ x7 -a→ x8 -a→ x9 -b→ x10 -b→ x11 — ✘ termina fuera de F
6. λ: {i, x0, y0} — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - i — ✘ termina fuera de F
    - i -λ→ x0 — ✘ termina fuera de F
    - i -λ→ y0 — ✘ termina fuera de F
7. `b1`: {i, x0, y0} -b→ {x0, y0} -1→ {x0, y0} — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - i -λ→ x0 -b→ x0 -1→ x0 — ✘ termina fuera de F
    - i -λ→ y0 -b→ y0 -1→ y0 — ✘ termina fuera de F
8. `c1cc`: {i, x0, y0} -c→ {x0, y0, y1} -1→ {x0, y0} -c→ {x0, y0, y1} -c→ {x0, y0, y1} — ✘
  Árbol de cómputo: 5 caminos, 0 de aceptación:
    - i -λ→ x0 -c→ x0 -1→ x0 -c→ x0 -c→ x0 — ✘ termina fuera de F
    - i -λ→ y0 -c→ y0 -1→ y0 -c→ y0 -c→ y0 — ✘ termina fuera de F
    - i -λ→ y0 -c→ y0 -1→ y0 -c→ y0 -c→ y1 — ✘ termina fuera de F
    - i -λ→ y0 -c→ y0 -1→ y0 -c→ y1 — ✘ muere tras leer `c1c`
    - i -λ→ y0 -c→ y1 — ✘ muere tras leer `c`
9. `b0aaab1`: {i, x0, y0} -b→ {x0, y0} -0→ {x0, y0} -a→ {x0, x1, y0} -a→ {x0, x1, y0} -a→ {x0, x1, y0} -b→ {x0, x2, y0} -1→ {x0, y0} — ✘
  Árbol de cómputo: 5 caminos, 0 de aceptación:
    - i -λ→ x0 -b→ x0 -0→ x0 -a→ x0 -a→ x0 -a→ x0 -b→ x0 -1→ x0 — ✘ termina fuera de F
    - i -λ→ x0 -b→ x0 -0→ x0 -a→ x0 -a→ x0 -a→ x1 -b→ x2 — ✘ muere tras leer `b0aaab`
    - i -λ→ x0 -b→ x0 -0→ x0 -a→ x0 -a→ x1 — ✘ muere tras leer `b0aa`
    - i -λ→ x0 -b→ x0 -0→ x0 -a→ x1 — ✘ muere tras leer `b0a`
    - i -λ→ y0 -b→ y0 -0→ y0 -a→ y0 -a→ y0 -a→ y0 -b→ y0 -1→ y0 — ✘ termina fuera de F
10. `aaacab1b10b`: {i, x0, y0} -a→ {x0, x1, y0} -a→ {x0, x1, y0} -a→ {x0, x1, y0} -c→ {x0, y0, y1} -a→ {x0, x1, y0} -b→ {x0, x2, y0} -1→ {x0, y0} -b→ {x0, y0} -1→ {x0, y0} -0→ {x0, y0} -b→ {x0, y0} — ✘
  Árbol de cómputo: 7 caminos, 0 de aceptación (se muestran 6):
    - i -λ→ x0 -a→ x0 -a→ x0 -a→ x0 -c→ x0 -a→ x0 -b→ x0 -1→ x0 -b→ x0 -1→ x0 -0→ x0 -b→ x0 — ✘ termina fuera de F
    - i -λ→ x0 -a→ x0 -a→ x0 -a→ x0 -c→ x0 -a→ x1 -b→ x2 — ✘ muere tras leer `aaacab`
    - i -λ→ x0 -a→ x0 -a→ x0 -a→ x1 — ✘ muere tras leer `aaa`
    - i -λ→ x0 -a→ x0 -a→ x1 — ✘ muere tras leer `aa`
    - i -λ→ x0 -a→ x1 — ✘ muere tras leer `a`
    - i -λ→ y0 -a→ y0 -a→ y0 -a→ y0 -c→ y0 -a→ y0 -b→ y0 -1→ y0 -b→ y0 -1→ y0 -0→ y0 -b→ y0 — ✘ termina fuera de F

</details>

Simulación paso a paso en JFLAP con `b1`: [ver captura](../../evidencias/jflap/pasos/L3-AFNDL-p108.png).

**Conversión.** AFND-λ (26 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 26 estados, [`L3-AFNDL-p108-AFND.jff`](../../automatas/conversiones/L3-AFNDL-p108-AFND.jff). AFND (26 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 89 estados, [`L3-AFNDL-p108-AFD.jff`](../../automatas/conversiones/L3-AFNDL-p108-AFD.jff) ([.json](../../automatas/conversiones/L3-AFNDL-p108-AFD.json), [.xml](../../automatas/conversiones/L3-AFNDL-p108-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 89 estados, y el AFD mínimo (Hopcroft), 37. La cota es 2^26 = 67108864. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-162-188-p-117"></a>

## Lista 3, problema 162-188 (p. 117)

**Enunciado.** AFN para el problema 117 de la Lista 2: L = {w ∈ Σ₃* : w = aⁿbᵐaᵖbᵠ, m, n, p, q ∈ ℕ}.

**Clasificación: AFND-λ.** Se resolvió con transiciones λ: componen el autómata a partir de piezas (unión o concatenación) sin consumir símbolos.

#### AFND-λ — `L3-AFNDL-p117`

Archivos: [`L3-AFNDL-p117.jff`](../../automatas/lista3-afnd-lambda/L3-AFNDL-p117.jff) · [`L3-AFNDL-p117.json`](../../automatas/lista3-afnd-lambda/L3-AFNDL-p117.json) · [`L3-AFNDL-p117.xml`](../../automatas/lista3-afnd-lambda/L3-AFNDL-p117.xml). Tipo según la definición: **AFND-lambda**, |Q| = 8, Σ = {a, b}, 11 transiciones.

**Diseño.** Concatenación de cuatro bloques x⁺: cada bloque es un estado de entrada y un estado con lazo; una transición λ pasa al bloque siguiente cuando el autómata adivina que el bloque terminó.

| Estado | a | b | λ |
|---|---|---|---|
| →q0 | {q1} | ∅ | ∅ |
| q1 | {q1} | ∅ | {q2} |
| q2 | ∅ | {q3} | ∅ |
| q3 | ∅ | {q3} | {q4} |
| q4 | {q5} | ∅ | ∅ |
| q5 | {q5} | ∅ | {q6} |
| q6 | ∅ | {q7} | ∅ |
| *q7 | ∅ | {q7} | ∅ |

**Transiciones λ.** Las λ (q1→q2, q3→q4, q5→q6) unen los bloques a⁺, b⁺, a⁺, b⁺ sin consumir símbolos: así cada bloque se diseña por separado y se concatena, que es como se construye el autómata de una concatenación de expresiones. No son indispensables (el AFD del 117 tiene 5 estados más el de rechazo), pero hacen visible la estructura aⁿ·bᵐ·aᵖ·bᵠ del enunciado.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| q0 | {q0} | no |
| q1 | {q1, q2} | no |
| q2 | {q2} | no |
| q3 | {q3, q4} | no |
| q4 | {q4} | no |
| q5 | {q5, q6} | no |
| q6 | {q6} | no |
| q7 | {q7} | sí |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `abab` | acepta | acepta | acepta |
| 2 | `aabab` | acepta | acepta | acepta |
| 3 | `aabbab` | acepta | acepta | acepta |
| 4 | `abbabbb` | acepta | acepta | acepta |
| 5 | `abbabbbbbbb` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `bb` | rechaza | rechaza | rechaza |
| 8 | `baab` | rechaza | rechaza | rechaza |
| 9 | `bbbabab` | rechaza | rechaza | rechaza |
| 10 | `babaababbab` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `abab`: {q0} -a→ {q1, q2} -b→ {q3, q4} -a→ {q5, q6} -b→ {q7} — ✔
  Árbol de cómputo: 1 caminos, 1 de aceptación:
    - q0 -a→ q1 -λ→ q2 -b→ q3 -λ→ q4 -a→ q5 -λ→ q6 -b→ q7 — ✔ acepta
2. `aabab`: {q0} -a→ {q1, q2} -a→ {q1, q2} -b→ {q3, q4} -a→ {q5, q6} -b→ {q7} — ✔
  Árbol de cómputo: 2 caminos, 1 de aceptación:
    - q0 -a→ q1 -a→ q1 -λ→ q2 -b→ q3 -λ→ q4 -a→ q5 -λ→ q6 -b→ q7 — ✔ acepta
    - q0 -a→ q1 -λ→ q2 — ✘ muere tras leer `a`
3. `aabbab`: {q0} -a→ {q1, q2} -a→ {q1, q2} -b→ {q3, q4} -b→ {q3, q4} -a→ {q5, q6} -b→ {q7} — ✔
  Árbol de cómputo: 3 caminos, 1 de aceptación:
    - q0 -a→ q1 -a→ q1 -λ→ q2 -b→ q3 -b→ q3 -λ→ q4 -a→ q5 -λ→ q6 -b→ q7 — ✔ acepta
    - q0 -a→ q1 -λ→ q2 — ✘ muere tras leer `a`
    - q0 -a→ q1 -a→ q1 -λ→ q2 -b→ q3 -λ→ q4 — ✘ muere tras leer `aab`
4. `abbabbb`: {q0} -a→ {q1, q2} -b→ {q3, q4} -b→ {q3, q4} -a→ {q5, q6} -b→ {q7} -b→ {q7} -b→ {q7} — ✔
  Árbol de cómputo: 2 caminos, 1 de aceptación:
    - q0 -a→ q1 -λ→ q2 -b→ q3 -b→ q3 -λ→ q4 -a→ q5 -λ→ q6 -b→ q7 -b→ q7 -b→ q7 — ✔ acepta
    - q0 -a→ q1 -λ→ q2 -b→ q3 -λ→ q4 — ✘ muere tras leer `ab`
5. `abbabbbbbbb`: {q0} -a→ {q1, q2} -b→ {q3, q4} -b→ {q3, q4} -a→ {q5, q6} -b→ {q7} -b→ {q7} -b→ {q7} -b→ {q7} -b→ {q7} -b→ {q7} -b→ {q7} — ✔
  Árbol de cómputo: 2 caminos, 1 de aceptación:
    - q0 -a→ q1 -λ→ q2 -b→ q3 -b→ q3 -λ→ q4 -a→ q5 -λ→ q6 -b→ q7 -b→ q7 -b→ q7 -b→ q7 -b→ q7 -b→ q7 -b→ q7 — ✔ acepta
    - q0 -a→ q1 -λ→ q2 -b→ q3 -λ→ q4 — ✘ muere tras leer `ab`
6. λ: {q0} — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ termina fuera de F
7. `bb`: {q0} -b→ ∅ -b→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ
8. `baab`: {q0} -b→ ∅ -a→ ∅ -a→ ∅ -b→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ
9. `bbbabab`: {q0} -b→ ∅ -b→ ∅ -b→ ∅ -a→ ∅ -b→ ∅ -a→ ∅ -b→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ
10. `babaababbab`: {q0} -b→ ∅ -a→ ∅ -b→ ∅ -a→ ∅ -a→ ∅ -b→ ∅ -a→ ∅ -b→ ∅ -b→ ∅ -a→ ∅ -b→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - q0 — ✘ muere tras leer λ

</details>

Simulación paso a paso en JFLAP con `abab`: [ver captura](../../evidencias/jflap/pasos/L3-AFNDL-p117.png).

**Conversión.** AFND-λ (8 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 8 estados, [`L3-AFNDL-p117-AFND.jff`](../../automatas/conversiones/L3-AFNDL-p117-AFND.jff). AFND (8 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 5 estados, [`L3-AFNDL-p117-AFD.jff`](../../automatas/conversiones/L3-AFNDL-p117-AFD.jff) ([.json](../../automatas/conversiones/L3-AFNDL-p117-AFD.json), [.xml](../../automatas/conversiones/L3-AFNDL-p117-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 6 estados, y el AFD mínimo (Hopcroft), 6. La cota es 2^8 = 256. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-196"></a>

## Lista 3, problema 196

**Enunciado.** Dibujar el AFND-λ de la tabla 196, hallar un AFD equivalente y calcular los incisos.

**Clasificación: AFND-λ.** La tabla tiene una columna λ con entradas no vacías: es un AFND con transiciones λ.

**Incisos** (δ es la función del autómata original):

- a) δ̂(A, 110) = ∅: {A, B} -1→ {C} -1→ ∅ -0→ ∅
- b) Cl({A}) = {A, B}
- c) Cl({B}) = {B}
- d) Cl({A, B}) = {A, B}
- e) δ(A, 0) = {A} (sin clausura; con ella, δ̂(A, 0) = {A, B})

#### AFND-λ dado en la tabla — `L3-196`

Archivos: [`L3-196.jff`](../../automatas/lista3-afnd-lambda/L3-196.jff) · [`L3-196.json`](../../automatas/lista3-afnd-lambda/L3-196.json) · [`L3-196.xml`](../../automatas/lista3-afnd-lambda/L3-196.xml). Tipo según la definición: **AFND-lambda**, |Q| = 3, Σ = {0, 1}, 5 transiciones.

**Diseño.** Transcripción de la tabla (columnas λ, 0, 1).

| Estado | 0 | 1 | λ |
|---|---|---|---|
| →A | {A} | ∅ | {B} |
| B | {A, B} | {C} | ∅ |
| *C | ∅ | ∅ | ∅ |

**Transiciones λ.** Las transiciones λ vienen dadas por la tabla; su papel se lee en las λ-clausuras.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| A | {A, B} | no |
| B | {B} | no |
| C | {C} | sí |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `1` | acepta | acepta | acepta |
| 2 | `01` | acepta | acepta | acepta |
| 3 | `001` | acepta | acepta | acepta |
| 4 | `00001` | acepta | acepta | acepta |
| 5 | `00000001` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `11` | rechaza | rechaza | rechaza |
| 8 | `0101` | rechaza | rechaza | rechaza |
| 9 | `0100011` | rechaza | rechaza | rechaza |
| 10 | `11011100110` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `1`: {A, B} -1→ {C} — ✔
  Árbol de cómputo: 1 caminos, 1 de aceptación:
    - A -λ→ B -1→ C — ✔ acepta
2. `01`: {A, B} -0→ {A, B} -1→ {C} — ✔
  Árbol de cómputo: 3 caminos, 3 de aceptación:
    - A -λ→ B -0→ A -λ→ B -1→ C — ✔ acepta
    - A -λ→ B -0→ B -1→ C — ✔ acepta
    - A -0→ A -λ→ B -1→ C — ✔ acepta
3. `001`: {A, B} -0→ {A, B} -0→ {A, B} -1→ {C} — ✔
  Árbol de cómputo: 8 caminos, 8 de aceptación (se muestran 3):
    - A -λ→ B -0→ A -λ→ B -0→ A -λ→ B -1→ C — ✔ acepta
    - A -λ→ B -0→ A -λ→ B -0→ B -1→ C — ✔ acepta
    - A -λ→ B -0→ A -0→ A -λ→ B -1→ C — ✔ acepta
4. `00001`: {A, B} -0→ {A, B} -0→ {A, B} -0→ {A, B} -0→ {A, B} -1→ {C} — ✔
  Árbol de cómputo: 55 caminos, 55 de aceptación (se muestran 3):
    - A -λ→ B -0→ A -λ→ B -0→ A -λ→ B -0→ A -λ→ B -0→ A -λ→ B -1→ C — ✔ acepta
    - A -λ→ B -0→ A -λ→ B -0→ A -λ→ B -0→ A -λ→ B -0→ B -1→ C — ✔ acepta
    - A -λ→ B -0→ A -λ→ B -0→ A -λ→ B -0→ A -0→ A -λ→ B -1→ C — ✔ acepta
5. `00000001`: {A, B} -0→ {A, B} -0→ {A, B} -0→ {A, B} -0→ {A, B} -0→ {A, B} -0→ {A, B} -0→ {A, B} -1→ {C} — ✔
  Árbol de cómputo: 200+ caminos, 200 de aceptación (se muestran 3):
    - A -λ→ B -0→ A -λ→ B -0→ A -λ→ B -0→ A -λ→ B -0→ A -λ→ B -0→ A -λ→ B -0→ A -λ→ B -0→ A -λ→ B -1→ C — ✔ acepta
    - A -λ→ B -0→ A -λ→ B -0→ A -λ→ B -0→ A -λ→ B -0→ A -λ→ B -0→ A -λ→ B -0→ A -λ→ B -0→ B -1→ C — ✔ acepta
    - A -λ→ B -0→ A -λ→ B -0→ A -λ→ B -0→ A -λ→ B -0→ A -λ→ B -0→ A -λ→ B -0→ A -0→ A -λ→ B -1→ C — ✔ acepta
6. λ: {A, B} — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - A — ✘ termina fuera de F
    - A -λ→ B — ✘ termina fuera de F
7. `11`: {A, B} -1→ {C} -1→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - A -λ→ B -1→ C — ✘ muere tras leer `1`
8. `0101`: {A, B} -0→ {A, B} -1→ {C} -0→ ∅ -1→ ∅ — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - A -λ→ B -0→ A -λ→ B -1→ C — ✘ muere tras leer `01`
    - A -λ→ B -0→ B -1→ C — ✘ muere tras leer `01`
    - A -0→ A -λ→ B -1→ C — ✘ muere tras leer `01`
9. `0100011`: {A, B} -0→ {A, B} -1→ {C} -0→ ∅ -0→ ∅ -0→ ∅ -1→ ∅ -1→ ∅ — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - A -λ→ B -0→ A -λ→ B -1→ C — ✘ muere tras leer `01`
    - A -λ→ B -0→ B -1→ C — ✘ muere tras leer `01`
    - A -0→ A -λ→ B -1→ C — ✘ muere tras leer `01`
10. `11011100110`: {A, B} -1→ {C} -1→ ∅ -0→ ∅ -1→ ∅ -1→ ∅ -1→ ∅ -0→ ∅ -0→ ∅ -1→ ∅ -1→ ∅ -0→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - A -λ→ B -1→ C — ✘ muere tras leer `1`

</details>

Simulación paso a paso en JFLAP con `01`: [ver captura](../../evidencias/jflap/pasos/L3-196.png).

**Conversión.** AFND-λ (3 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 3 estados, [`L3-196-AFND.jff`](../../automatas/conversiones/L3-196-AFND.jff). AFND (3 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 3 estados, [`L3-196-AFD.jff`](../../automatas/conversiones/L3-196-AFD.jff) ([.json](../../automatas/conversiones/L3-196-AFD.json), [.xml](../../automatas/conversiones/L3-196-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 3 estados, y el AFD mínimo (Hopcroft), 3. La cota es 2^3 = 8. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-197"></a>

## Lista 3, problema 197

**Enunciado.** Dibujar el AFND-λ de la tabla 197, hallar un AFD equivalente y calcular los incisos.

**Clasificación: AFND-λ.** La tabla tiene una columna λ con entradas no vacías: es un AFND con transiciones λ.

**Incisos** (δ es la función del autómata original):

- a) Cl({A}) = {A, B, C, D}
- b) Cl({B, D}) = {B, D}
- c) Cl({A, B, C}) = {A, B, C, D}
- d) δ(A, 0) = {B, D} (sin clausura; con ella, δ̂(A, 0) = {A, B, C, D})
- e) δ̂(A, 010) = {A, B, C, D}: {A, B, C, D} -0→ {A, B, C, D} -1→ {A, B, C, D} -0→ {A, B, C, D}

#### AFND-λ dado en la tabla — `L3-197`

Archivos: [`L3-197.jff`](../../automatas/lista3-afnd-lambda/L3-197.jff) · [`L3-197.json`](../../automatas/lista3-afnd-lambda/L3-197.json) · [`L3-197.xml`](../../automatas/lista3-afnd-lambda/L3-197.xml). Tipo según la definición: **AFND-lambda**, |Q| = 4, Σ = {0, 1}, 11 transiciones.

**Diseño.** Transcripción de la tabla (columnas λ, 0, 1).

| Estado | 0 | 1 | λ |
|---|---|---|---|
| →A | {B, D} | ∅ | {C} |
| B | {A, C} | {D} | {D} |
| C | ∅ | {A, C} | {B} |
| *D | ∅ | {D} | ∅ |

**Transiciones λ.** Las transiciones λ vienen dadas por la tabla; su papel se lee en las λ-clausuras.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| A | {A, B, C, D} | sí |
| B | {B, D} | sí |
| C | {B, C, D} | sí |
| D | {D} | sí |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | acepta | acepta | acepta |
| 2 | `00` | acepta | acepta | acepta |
| 3 | `1010` | acepta | acepta | acepta |
| 4 | `1000110` | acepta | acepta | acepta |
| 5 | `11010100110` | acepta | acepta | acepta |
| 6 | `#` (símbolo fuera de Σ) | rechaza | rechaza | rechaza |
| 7 | `0#` (símbolo fuera de Σ) | rechaza | rechaza | rechaza |
| 8 | `#11` (símbolo fuera de Σ) | rechaza | rechaza | rechaza |

Nota sobre los casos: todas las cadenas sobre Σ pertenecen al lenguaje, así que las inválidas usan un símbolo fuera de Σ (#).

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: {A, B, C, D} — ✔
  Árbol de cómputo: 4 caminos, 1 de aceptación:
    - A -λ→ C -λ→ B -λ→ D — ✔ acepta
    - A — ✘ termina fuera de F
    - A -λ→ C — ✘ termina fuera de F
    - A -λ→ C -λ→ B — ✘ termina fuera de F
2. `00`: {A, B, C, D} -0→ {A, B, C, D} -0→ {A, B, C, D} — ✔
  Árbol de cómputo: 29 caminos, 8 de aceptación (se muestran 6):
    - A -λ→ C -λ→ B -0→ A -λ→ C -λ→ B -0→ A -λ→ C -λ→ B -λ→ D — ✔ acepta
    - A -λ→ C -λ→ B -0→ A -λ→ C -λ→ B -0→ C -λ→ B -λ→ D — ✔ acepta
    - A -λ→ C -λ→ B -0→ A -0→ B -λ→ D — ✔ acepta
    - A -λ→ C -λ→ B -λ→ D — ✘ muere tras leer λ
    - A -λ→ C -λ→ B -0→ A -λ→ C -λ→ B -λ→ D — ✘ muere tras leer `0`
    - A -λ→ C -λ→ B -0→ A -λ→ C -λ→ B -0→ A — ✘ termina fuera de F
3. `1010`: {A, B, C, D} -1→ {A, B, C, D} -0→ {A, B, C, D} -1→ {A, B, C, D} -0→ {A, B, C, D} — ✔
  Árbol de cómputo: 91 caminos, 24 de aceptación (se muestran 6):
    - A -λ→ C -1→ A -λ→ C -λ→ B -0→ A -λ→ C -1→ A -λ→ C -λ→ B -0→ A -λ→ C -λ→ B -λ→ D — ✔ acepta
    - A -λ→ C -1→ A -λ→ C -λ→ B -0→ A -λ→ C -1→ A -λ→ C -λ→ B -0→ C -λ→ B -λ→ D — ✔ acepta
    - A -λ→ C -1→ A -λ→ C -λ→ B -0→ A -λ→ C -1→ A -0→ B -λ→ D — ✔ acepta
    - A -λ→ C -λ→ B -λ→ D -1→ D — ✘ muere tras leer `1`
    - A -λ→ C -λ→ B -1→ D — ✘ muere tras leer `1`
    - A -λ→ C -1→ A -λ→ C -λ→ B -λ→ D — ✘ muere tras leer `1`
4. `1000110`: {A, B, C, D} -1→ {A, B, C, D} -0→ {A, B, C, D} -0→ {A, B, C, D} -0→ {A, B, C, D} -1→ {A, B, C, D} -1→ {A, B, C, D} -0→ {A, B, C, D} — ✔
  Árbol de cómputo: 200+ caminos, 51 de aceptación (se muestran 6):
    - A -λ→ C -1→ A -λ→ C -λ→ B -0→ A -λ→ C -λ→ B -0→ A -λ→ C -λ→ B -0→ A -λ→ C -1→ A -λ→ C -1→ A -λ→ C -λ→ B -0→ A -λ→ C -λ→ B -λ→ D — ✔ acepta
    - A -λ→ C -1→ A -λ→ C -λ→ B -0→ A -λ→ C -λ→ B -0→ A -λ→ C -λ→ B -0→ A -λ→ C -1→ A -λ→ C -1→ A -λ→ C -λ→ B -0→ C -λ→ B -λ→ D — ✔ acepta
    - A -λ→ C -1→ A -λ→ C -λ→ B -0→ A -λ→ C -λ→ B -0→ A -λ→ C -λ→ B -0→ A -λ→ C -1→ A -λ→ C -1→ A -0→ B -λ→ D — ✔ acepta
    - A -λ→ C -λ→ B -λ→ D -1→ D — ✘ muere tras leer `1`
    - A -λ→ C -λ→ B -1→ D — ✘ muere tras leer `1`
    - A -λ→ C -1→ A -λ→ C -λ→ B -λ→ D — ✘ muere tras leer `1`
5. `11010100110`: {A, B, C, D} -1→ {A, B, C, D} -1→ {A, B, C, D} -0→ {A, B, C, D} -1→ {A, B, C, D} -0→ {A, B, C, D} -1→ {A, B, C, D} -0→ {A, B, C, D} -0→ {A, B, C, D} -1→ {A, B, C, D} -1→ {A, B, C, D} -0→ {A, B, C, D} — ✔
  Árbol de cómputo: 200+ caminos, 48 de aceptación (se muestran 6):
    - A -λ→ C -1→ A -λ→ C -1→ A -λ→ C -λ→ B -0→ A -λ→ C -1→ A -λ→ C -λ→ B -0→ A -λ→ C -1→ A -λ→ C -λ→ B -0→ A -λ→ C -λ→ B -0→ A -λ→ C -1→ A -λ→ C -1→ A -λ→ C -λ→ B -0→ A -λ→ C -λ→ B -λ→ D — ✔ acepta
    - A -λ→ C -1→ A -λ→ C -1→ A -λ→ C -λ→ B -0→ A -λ→ C -1→ A -λ→ C -λ→ B -0→ A -λ→ C -1→ A -λ→ C -λ→ B -0→ A -λ→ C -λ→ B -0→ A -λ→ C -1→ A -λ→ C -1→ A -λ→ C -λ→ B -0→ C -λ→ B -λ→ D — ✔ acepta
    - A -λ→ C -1→ A -λ→ C -1→ A -λ→ C -λ→ B -0→ A -λ→ C -1→ A -λ→ C -λ→ B -0→ A -λ→ C -1→ A -λ→ C -λ→ B -0→ A -λ→ C -λ→ B -0→ A -λ→ C -1→ A -λ→ C -1→ A -0→ B -λ→ D — ✔ acepta
    - A -λ→ C -λ→ B -λ→ D -1→ D -1→ D — ✘ muere tras leer `11`
    - A -λ→ C -λ→ B -1→ D -1→ D — ✘ muere tras leer `11`
    - A -λ→ C -1→ A -λ→ C -λ→ B -λ→ D -1→ D — ✘ muere tras leer `11`
6. `#`: {A, B, C, D} -#→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - A -λ→ C -λ→ B -λ→ D — ✘ muere tras leer λ
7. `0#`: {A, B, C, D} -0→ {A, B, C, D} -#→ ∅ — ✘
  Árbol de cómputo: 5 caminos, 0 de aceptación:
    - A -λ→ C -λ→ B -λ→ D — ✘ muere tras leer λ
    - A -λ→ C -λ→ B -0→ A -λ→ C -λ→ B -λ→ D — ✘ muere tras leer `0`
    - A -λ→ C -λ→ B -0→ C -λ→ B -λ→ D — ✘ muere tras leer `0`
    - A -0→ B -λ→ D — ✘ muere tras leer `0`
    - A -0→ D — ✘ muere tras leer `0`
8. `#11`: {A, B, C, D} -#→ ∅ -1→ ∅ -1→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - A -λ→ C -λ→ B -λ→ D — ✘ muere tras leer λ

</details>

Simulación paso a paso en JFLAP con `00`: [ver captura](../../evidencias/jflap/pasos/L3-197.png).

**Conversión.** AFND-λ (4 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 4 estados, [`L3-197-AFND.jff`](../../automatas/conversiones/L3-197-AFND.jff). AFND (4 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 2 estados, [`L3-197-AFD.jff`](../../automatas/conversiones/L3-197-AFD.jff) ([.json](../../automatas/conversiones/L3-197-AFD.json), [.xml](../../automatas/conversiones/L3-197-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 1 estados, y el AFD mínimo (Hopcroft), 1. La cota es 2^4 = 16. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-198"></a>

## Lista 3, problema 198

**Enunciado.** Dibujar el AFND-λ de la tabla 198, hallar un AFD equivalente y calcular los incisos.

**Clasificación: AFND-λ.** La tabla tiene una columna λ con entradas no vacías: es un AFND con transiciones λ.

**Incisos** (δ es la función del autómata original):

- a) Cl({A}) = {A, B, C}
- b) Cl({C, D}) = {B, C, D}
- c) Cl({A, C, D}) = {A, B, C, D}
- d) δ̂(B, 0111) = {B, C, D}: {B} -0→ {B, C} -1→ {B, C, D} -1→ {B, C, D} -1→ {B, C, D}

#### AFND-λ dado en la tabla — `L3-198`

Archivos: [`L3-198.jff`](../../automatas/lista3-afnd-lambda/L3-198.jff) · [`L3-198.json`](../../automatas/lista3-afnd-lambda/L3-198.json) · [`L3-198.xml`](../../automatas/lista3-afnd-lambda/L3-198.xml). Tipo según la definición: **AFND-lambda**, |Q| = 4, Σ = {0, 1}, 7 transiciones.

**Diseño.** Transcripción de la tabla (columnas λ, 0, 1).

| Estado | 0 | 1 | λ |
|---|---|---|---|
| →A | {B} | ∅ | {C} |
| B | {C} | ∅ | ∅ |
| C | ∅ | {C, D} | {B} |
| *D | ∅ | {B} | ∅ |

**Transiciones λ.** Las transiciones λ vienen dadas por la tabla; su papel se lee en las λ-clausuras.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| A | {A, B, C} | no |
| B | {B} | no |
| C | {B, C} | no |
| D | {D} | sí |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `1` | acepta | acepta | acepta |
| 2 | `01` | acepta | acepta | acepta |
| 3 | `0011` | acepta | acepta | acepta |
| 4 | `00010101` | acepta | acepta | acepta |
| 5 | `101101111101` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `010` | rechaza | rechaza | rechaza |
| 8 | `00010` | rechaza | rechaza | rechaza |
| 9 | `1010010` | rechaza | rechaza | rechaza |
| 10 | `000010100110` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. `1`: {A, B, C} -1→ {B, C, D} — ✔
  Árbol de cómputo: 4 caminos, 1 de aceptación:
    - A -λ→ C -1→ D — ✔ acepta
    - A -λ→ C -λ→ B — ✘ muere tras leer λ
    - A -λ→ C -1→ C — ✘ termina fuera de F
    - A -λ→ C -1→ C -λ→ B — ✘ termina fuera de F
2. `01`: {A, B, C} -0→ {B, C} -1→ {B, C, D} — ✔
  Árbol de cómputo: 5 caminos, 1 de aceptación:
    - A -λ→ C -λ→ B -0→ C -1→ D — ✔ acepta
    - A -λ→ C -λ→ B -0→ C -λ→ B — ✘ muere tras leer `0`
    - A -λ→ C -λ→ B -0→ C -1→ C — ✘ termina fuera de F
    - A -λ→ C -λ→ B -0→ C -1→ C -λ→ B — ✘ termina fuera de F
    - A -0→ B — ✘ muere tras leer `0`
3. `0011`: {A, B, C} -0→ {B, C} -0→ {B, C} -1→ {B, C, D} -1→ {B, C, D} — ✔
  Árbol de cómputo: 12 caminos, 2 de aceptación (se muestran 6):
    - A -λ→ C -λ→ B -0→ C -λ→ B -0→ C -1→ C -1→ D — ✔ acepta
    - A -0→ B -0→ C -1→ C -1→ D — ✔ acepta
    - A -λ→ C -λ→ B -0→ C -λ→ B -0→ C -λ→ B — ✘ muere tras leer `00`
    - A -λ→ C -λ→ B -0→ C -λ→ B -0→ C -1→ C -λ→ B — ✘ muere tras leer `001`
    - A -λ→ C -λ→ B -0→ C -λ→ B -0→ C -1→ C -1→ C — ✘ termina fuera de F
    - A -λ→ C -λ→ B -0→ C -λ→ B -0→ C -1→ C -1→ C -λ→ B — ✘ termina fuera de F
4. `00010101`: {A, B, C} -0→ {B, C} -0→ {B, C} -0→ {B, C} -1→ {B, C, D} -0→ {B, C} -1→ {B, C, D} -0→ {B, C} -1→ {B, C, D} — ✔
  Árbol de cómputo: 16 caminos, 2 de aceptación (se muestran 6):
    - A -λ→ C -λ→ B -0→ C -λ→ B -0→ C -λ→ B -0→ C -1→ C -λ→ B -0→ C -1→ C -λ→ B -0→ C -1→ D — ✔ acepta
    - A -0→ B -0→ C -λ→ B -0→ C -1→ C -λ→ B -0→ C -1→ C -λ→ B -0→ C -1→ D — ✔ acepta
    - A -λ→ C -λ→ B -0→ C -λ→ B -0→ C -λ→ B -0→ C -λ→ B — ✘ muere tras leer `000`
    - A -λ→ C -λ→ B -0→ C -λ→ B -0→ C -λ→ B -0→ C -1→ C -λ→ B -0→ C -λ→ B — ✘ muere tras leer `00010`
    - A -λ→ C -λ→ B -0→ C -λ→ B -0→ C -λ→ B -0→ C -1→ C -λ→ B -0→ C -1→ C -λ→ B -0→ C -λ→ B — ✘ muere tras leer `0001010`
    - A -λ→ C -λ→ B -0→ C -λ→ B -0→ C -λ→ B -0→ C -1→ C -λ→ B -0→ C -1→ C -λ→ B -0→ C -1→ C — ✘ termina fuera de F
5. `101101111101`: {A, B, C} -1→ {B, C, D} -0→ {B, C} -1→ {B, C, D} -1→ {B, C, D} -0→ {B, C} -1→ {B, C, D} -1→ {B, C, D} -1→ {B, C, D} -1→ {B, C, D} -1→ {B, C, D} -0→ {B, C} -1→ {B, C, D} — ✔
  Árbol de cómputo: 39 caminos, 4 de aceptación (se muestran 6):
    - A -λ→ C -1→ C -λ→ B -0→ C -1→ C -1→ C -λ→ B -0→ C -1→ C -1→ C -1→ C -1→ C -1→ C -λ→ B -0→ C -1→ D — ✔ acepta
    - A -λ→ C -1→ C -λ→ B -0→ C -1→ C -1→ C -λ→ B -0→ C -1→ C -1→ C -1→ C -1→ D -1→ B -0→ C -1→ D — ✔ acepta
    - A -λ→ C -1→ C -λ→ B -0→ C -1→ D -1→ B -0→ C -1→ C -1→ C -1→ C -1→ C -1→ C -λ→ B -0→ C -1→ D — ✔ acepta
    - A -λ→ C -λ→ B — ✘ muere tras leer λ
    - A -λ→ C -1→ C -λ→ B -0→ C -λ→ B — ✘ muere tras leer `10`
    - A -λ→ C -1→ C -λ→ B -0→ C -1→ C -λ→ B — ✘ muere tras leer `101`
6. λ: {A, B, C} — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - A — ✘ termina fuera de F
    - A -λ→ C — ✘ termina fuera de F
    - A -λ→ C -λ→ B — ✘ termina fuera de F
7. `010`: {A, B, C} -0→ {B, C} -1→ {B, C, D} -0→ {B, C} — ✘
  Árbol de cómputo: 5 caminos, 0 de aceptación:
    - A -λ→ C -λ→ B -0→ C -λ→ B — ✘ muere tras leer `0`
    - A -λ→ C -λ→ B -0→ C -1→ C -λ→ B -0→ C — ✘ termina fuera de F
    - A -λ→ C -λ→ B -0→ C -1→ C -λ→ B -0→ C -λ→ B — ✘ termina fuera de F
    - A -λ→ C -λ→ B -0→ C -1→ D — ✘ muere tras leer `01`
    - A -0→ B — ✘ muere tras leer `0`
8. `00010`: {A, B, C} -0→ {B, C} -0→ {B, C} -0→ {B, C} -1→ {B, C, D} -0→ {B, C} — ✘
  Árbol de cómputo: 8 caminos, 0 de aceptación (se muestran 6):
    - A -λ→ C -λ→ B -0→ C -λ→ B -0→ C -λ→ B -0→ C -λ→ B — ✘ muere tras leer `000`
    - A -λ→ C -λ→ B -0→ C -λ→ B -0→ C -λ→ B -0→ C -1→ C -λ→ B -0→ C — ✘ termina fuera de F
    - A -λ→ C -λ→ B -0→ C -λ→ B -0→ C -λ→ B -0→ C -1→ C -λ→ B -0→ C -λ→ B — ✘ termina fuera de F
    - A -λ→ C -λ→ B -0→ C -λ→ B -0→ C -λ→ B -0→ C -1→ D — ✘ muere tras leer `0001`
    - A -0→ B -0→ C -λ→ B -0→ C -λ→ B — ✘ muere tras leer `000`
    - A -0→ B -0→ C -λ→ B -0→ C -1→ C -λ→ B -0→ C — ✘ termina fuera de F
9. `1010010`: {A, B, C} -1→ {B, C, D} -0→ {B, C} -1→ {B, C, D} -0→ {B, C} -0→ {B, C} -1→ {B, C, D} -0→ {B, C} — ✘
  Árbol de cómputo: 8 caminos, 0 de aceptación (se muestran 6):
    - A -λ→ C -λ→ B — ✘ muere tras leer λ
    - A -λ→ C -1→ C -λ→ B -0→ C -λ→ B — ✘ muere tras leer `10`
    - A -λ→ C -1→ C -λ→ B -0→ C -1→ C -λ→ B -0→ C -λ→ B -0→ C -λ→ B — ✘ muere tras leer `10100`
    - A -λ→ C -1→ C -λ→ B -0→ C -1→ C -λ→ B -0→ C -λ→ B -0→ C -1→ C -λ→ B -0→ C — ✘ termina fuera de F
    - A -λ→ C -1→ C -λ→ B -0→ C -1→ C -λ→ B -0→ C -λ→ B -0→ C -1→ C -λ→ B -0→ C -λ→ B — ✘ termina fuera de F
    - A -λ→ C -1→ C -λ→ B -0→ C -1→ C -λ→ B -0→ C -λ→ B -0→ C -1→ D — ✘ muere tras leer `101001`
10. `000010100110`: {A, B, C} -0→ {B, C} -0→ {B, C} -0→ {B, C} -0→ {B, C} -1→ {B, C, D} -0→ {B, C} -1→ {B, C, D} -0→ {B, C} -0→ {B, C} -1→ {B, C, D} -1→ {B, C, D} -0→ {B, C} — ✘
  Árbol de cómputo: 22 caminos, 0 de aceptación (se muestran 6):
    - A -λ→ C -λ→ B -0→ C -λ→ B -0→ C -λ→ B -0→ C -λ→ B -0→ C -λ→ B — ✘ muere tras leer `0000`
    - A -λ→ C -λ→ B -0→ C -λ→ B -0→ C -λ→ B -0→ C -λ→ B -0→ C -1→ C -λ→ B -0→ C -λ→ B — ✘ muere tras leer `000010`
    - A -λ→ C -λ→ B -0→ C -λ→ B -0→ C -λ→ B -0→ C -λ→ B -0→ C -1→ C -λ→ B -0→ C -1→ C -λ→ B -0→ C -λ→ B -0→ C -λ→ B — ✘ muere tras leer `000010100`
    - A -λ→ C -λ→ B -0→ C -λ→ B -0→ C -λ→ B -0→ C -λ→ B -0→ C -1→ C -λ→ B -0→ C -1→ C -λ→ B -0→ C -λ→ B -0→ C -1→ C -λ→ B — ✘ muere tras leer `0000101001`
    - A -λ→ C -λ→ B -0→ C -λ→ B -0→ C -λ→ B -0→ C -λ→ B -0→ C -1→ C -λ→ B -0→ C -1→ C -λ→ B -0→ C -λ→ B -0→ C -1→ C -1→ C -λ→ B -0→ C — ✘ termina fuera de F
    - A -λ→ C -λ→ B -0→ C -λ→ B -0→ C -λ→ B -0→ C -λ→ B -0→ C -1→ C -λ→ B -0→ C -1→ C -λ→ B -0→ C -λ→ B -0→ C -1→ C -1→ C -λ→ B -0→ C -λ→ B — ✘ termina fuera de F

</details>

Simulación paso a paso en JFLAP con `01`: [ver captura](../../evidencias/jflap/pasos/L3-198.png).

**Conversión.** AFND-λ (4 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 4 estados, [`L3-198-AFND.jff`](../../automatas/conversiones/L3-198-AFND.jff). AFND (4 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 3 estados, [`L3-198-AFD.jff`](../../automatas/conversiones/L3-198-AFD.jff) ([.json](../../automatas/conversiones/L3-198-AFD.json), [.xml](../../automatas/conversiones/L3-198-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 3 estados, y el AFD mínimo (Hopcroft), 2. La cota es 2^4 = 16. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-199"></a>

## Lista 3, problema 199

**Enunciado.** Dibujar el AFND-λ de la tabla 199, hallar un AFD equivalente y calcular los incisos.

**Clasificación: AFND-λ.** La tabla tiene una columna λ con entradas no vacías: es un AFND con transiciones λ.

**Incisos** (δ es la función del autómata original):

- a) Cl({A}) = {A, B, C, E}
- b) Cl({C}) = {C, E}
- c) δ̂(A, 011) = {D}: {A, B, C, E} -0→ {E} -1→ {D} -1→ {D}

#### AFND-λ dado en la tabla — `L3-199`

Archivos: [`L3-199.jff`](../../automatas/lista3-afnd-lambda/L3-199.jff) · [`L3-199.json`](../../automatas/lista3-afnd-lambda/L3-199.json) · [`L3-199.xml`](../../automatas/lista3-afnd-lambda/L3-199.xml). Tipo según la definición: **AFND-lambda**, |Q| = 5, Σ = {0, 1}, 10 transiciones.

**Diseño.** Transcripción de la tabla (columnas λ, 0, 1).

| Estado | 0 | 1 | λ |
|---|---|---|---|
| →A | {E} | ∅ | {B, C} |
| B | {E} | {B} | ∅ |
| C | ∅ | {A, C} | {E} |
| *D | ∅ | {D} | ∅ |
| *E | ∅ | {D} | ∅ |

**Transiciones λ.** Las transiciones λ vienen dadas por la tabla; su papel se lee en las λ-clausuras.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| A | {A, B, C, E} | sí |
| B | {B} | no |
| C | {C, E} | sí |
| D | {D} | sí |
| E | {E} | sí |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | λ | acepta | acepta | acepta |
| 2 | `01` | acepta | acepta | acepta |
| 3 | `0111` | acepta | acepta | acepta |
| 4 | `1011111` | acepta | acepta | acepta |
| 5 | `10111111111` | acepta | acepta | acepta |
| 6 | `00` | rechaza | rechaza | rechaza |
| 7 | `0010` | rechaza | rechaza | rechaza |
| 8 | `1100` | rechaza | rechaza | rechaza |
| 9 | `1101011` | rechaza | rechaza | rechaza |
| 10 | `10010001010` | rechaza | rechaza | rechaza |

<details><summary>Recorrido completo de cada cadena</summary>

1. λ: {A, B, C, E} — ✔
  Árbol de cómputo: 4 caminos, 1 de aceptación:
    - A -λ→ C -λ→ E — ✔ acepta
    - A — ✘ termina fuera de F
    - A -λ→ B — ✘ termina fuera de F
    - A -λ→ C — ✘ termina fuera de F
2. `01`: {A, B, C, E} -0→ {E} -1→ {D} — ✔
  Árbol de cómputo: 3 caminos, 2 de aceptación:
    - A -λ→ B -0→ E -1→ D — ✔ acepta
    - A -0→ E -1→ D — ✔ acepta
    - A -λ→ C -λ→ E — ✘ muere tras leer λ
3. `0111`: {A, B, C, E} -0→ {E} -1→ {D} -1→ {D} -1→ {D} — ✔
  Árbol de cómputo: 3 caminos, 2 de aceptación:
    - A -λ→ B -0→ E -1→ D -1→ D -1→ D — ✔ acepta
    - A -0→ E -1→ D -1→ D -1→ D — ✔ acepta
    - A -λ→ C -λ→ E — ✘ muere tras leer λ
4. `1011111`: {A, B, C, E} -1→ {A, B, C, D, E} -0→ {E} -1→ {D} -1→ {D} -1→ {D} -1→ {D} -1→ {D} — ✔
  Árbol de cómputo: 6 caminos, 3 de aceptación:
    - A -λ→ B -1→ B -0→ E -1→ D -1→ D -1→ D -1→ D -1→ D — ✔ acepta
    - A -λ→ C -1→ A -λ→ B -0→ E -1→ D -1→ D -1→ D -1→ D -1→ D — ✔ acepta
    - A -λ→ C -1→ A -0→ E -1→ D -1→ D -1→ D -1→ D -1→ D — ✔ acepta
    - A -λ→ C -λ→ E -1→ D — ✘ muere tras leer `1`
    - A -λ→ C -1→ A -λ→ C -λ→ E — ✘ muere tras leer `1`
    - A -λ→ C -1→ C -λ→ E — ✘ muere tras leer `1`
5. `10111111111`: {A, B, C, E} -1→ {A, B, C, D, E} -0→ {E} -1→ {D} -1→ {D} -1→ {D} -1→ {D} -1→ {D} -1→ {D} -1→ {D} -1→ {D} -1→ {D} — ✔
  Árbol de cómputo: 6 caminos, 3 de aceptación:
    - A -λ→ B -1→ B -0→ E -1→ D -1→ D -1→ D -1→ D -1→ D -1→ D -1→ D -1→ D -1→ D — ✔ acepta
    - A -λ→ C -1→ A -λ→ B -0→ E -1→ D -1→ D -1→ D -1→ D -1→ D -1→ D -1→ D -1→ D -1→ D — ✔ acepta
    - A -λ→ C -1→ A -0→ E -1→ D -1→ D -1→ D -1→ D -1→ D -1→ D -1→ D -1→ D -1→ D — ✔ acepta
    - A -λ→ C -λ→ E -1→ D — ✘ muere tras leer `1`
    - A -λ→ C -1→ A -λ→ C -λ→ E — ✘ muere tras leer `1`
    - A -λ→ C -1→ C -λ→ E — ✘ muere tras leer `1`
6. `00`: {A, B, C, E} -0→ {E} -0→ ∅ — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - A -λ→ B -0→ E — ✘ muere tras leer `0`
    - A -λ→ C -λ→ E — ✘ muere tras leer λ
    - A -0→ E — ✘ muere tras leer `0`
7. `0010`: {A, B, C, E} -0→ {E} -0→ ∅ -1→ ∅ -0→ ∅ — ✘
  Árbol de cómputo: 3 caminos, 0 de aceptación:
    - A -λ→ B -0→ E — ✘ muere tras leer `0`
    - A -λ→ C -λ→ E — ✘ muere tras leer λ
    - A -0→ E — ✘ muere tras leer `0`
8. `1100`: {A, B, C, E} -1→ {A, B, C, D, E} -1→ {A, B, C, D, E} -0→ {E} -0→ ∅ — ✘
  Árbol de cómputo: 13 caminos, 0 de aceptación (se muestran 6):
    - A -λ→ B -1→ B -1→ B -0→ E — ✘ muere tras leer `110`
    - A -λ→ C -λ→ E -1→ D -1→ D — ✘ muere tras leer `11`
    - A -λ→ C -1→ A -λ→ B -1→ B -0→ E — ✘ muere tras leer `110`
    - A -λ→ C -1→ A -λ→ C -λ→ E -1→ D — ✘ muere tras leer `11`
    - A -λ→ C -1→ A -λ→ C -1→ A -λ→ B -0→ E — ✘ muere tras leer `110`
    - A -λ→ C -1→ A -λ→ C -1→ A -λ→ C -λ→ E — ✘ muere tras leer `11`
9. `1101011`: {A, B, C, E} -1→ {A, B, C, D, E} -1→ {A, B, C, D, E} -0→ {E} -1→ {D} -0→ ∅ -1→ ∅ -1→ ∅ — ✘
  Árbol de cómputo: 13 caminos, 0 de aceptación (se muestran 6):
    - A -λ→ B -1→ B -1→ B -0→ E -1→ D — ✘ muere tras leer `1101`
    - A -λ→ C -λ→ E -1→ D -1→ D — ✘ muere tras leer `11`
    - A -λ→ C -1→ A -λ→ B -1→ B -0→ E -1→ D — ✘ muere tras leer `1101`
    - A -λ→ C -1→ A -λ→ C -λ→ E -1→ D — ✘ muere tras leer `11`
    - A -λ→ C -1→ A -λ→ C -1→ A -λ→ B -0→ E -1→ D — ✘ muere tras leer `1101`
    - A -λ→ C -1→ A -λ→ C -1→ A -λ→ C -λ→ E — ✘ muere tras leer `11`
10. `10010001010`: {A, B, C, E} -1→ {A, B, C, D, E} -0→ {E} -0→ ∅ -1→ ∅ -0→ ∅ -0→ ∅ -0→ ∅ -1→ ∅ -0→ ∅ -1→ ∅ -0→ ∅ — ✘
  Árbol de cómputo: 6 caminos, 0 de aceptación:
    - A -λ→ B -1→ B -0→ E — ✘ muere tras leer `10`
    - A -λ→ C -λ→ E -1→ D — ✘ muere tras leer `1`
    - A -λ→ C -1→ A -λ→ B -0→ E — ✘ muere tras leer `10`
    - A -λ→ C -1→ A -λ→ C -λ→ E — ✘ muere tras leer `1`
    - A -λ→ C -1→ A -0→ E — ✘ muere tras leer `10`
    - A -λ→ C -1→ C -λ→ E — ✘ muere tras leer `1`

</details>

Simulación paso a paso en JFLAP con `01`: [ver captura](../../evidencias/jflap/pasos/L3-199.png).

**Conversión.** AFND-λ (5 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 5 estados, [`L3-199-AFND.jff`](../../automatas/conversiones/L3-199-AFND.jff). AFND (5 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 4 estados, [`L3-199-AFD.jff`](../../automatas/conversiones/L3-199-AFD.jff) ([.json](../../automatas/conversiones/L3-199-AFD.json), [.xml](../../automatas/conversiones/L3-199-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 5 estados, y el AFD mínimo (Hopcroft), 3. La cota es 2^5 = 32. Se verificó que los tres autómatas aceptan el mismo lenguaje.

<a id="problema-3-200"></a>

## Lista 3, problema 200

**Enunciado.** Dibujar el AFND-λ de la tabla 200, hallar un AFD equivalente y calcular los incisos.

**Clasificación: AFND-λ.** La tabla tiene una columna λ con entradas no vacías: es un AFND con transiciones λ.

**Incisos** (δ es la función del autómata original):

- a) Cl({A}) = {A, B}
- b) Cl({C, D}) = {C, D, E, F}
- c) δ̂(C, 1011) = {A, B, C, D, E, F}: {C, E} -1→ {A, B, C, D, E, F} -0→ {A, B, C, D, E, F} -1→ {A, B, C, D, E, F} -1→ {A, B, C, D, E, F}

#### AFND-λ dado en la tabla — `L3-200`

Archivos: [`L3-200.jff`](../../automatas/lista3-afnd-lambda/L3-200.jff) · [`L3-200.json`](../../automatas/lista3-afnd-lambda/L3-200.json) · [`L3-200.xml`](../../automatas/lista3-afnd-lambda/L3-200.xml). Tipo según la definición: **AFND-lambda**, |Q| = 6, Σ = {0, 1}, 22 transiciones.

**Diseño.** Transcripción de la tabla (columnas λ, 0, 1).

| Estado | 0 | 1 | λ |
|---|---|---|---|
| →A | {F} | {A, C, F} | {B} |
| B | {C, D} | {B, E} | ∅ |
| C | ∅ | {A, C} | {E} |
| *D | {A, C} | {B, E} | {E, F} |
| *E | ∅ | {D} | ∅ |
| F | {B, E} | ∅ | {E} |

**Transiciones λ.** Las transiciones λ vienen dadas por la tabla; su papel se lee en las λ-clausuras.

**λ-clausuras.** Cl(q) son los estados a los que se llega desde q sin leer símbolos. El simulador empieza en Cl(q₀) y, después de cada símbolo, cierra el conjunto alcanzado; una cadena se acepta si el conjunto final contiene un estado de F.

| Estado | Cl(q) | ¿Contiene un estado de F? |
|---|---|---|
| A | {A, B} | no |
| B | {B} | no |
| C | {C, E} | sí |
| D | {D, E, F} | sí |
| E | {E} | sí |
| F | {E, F} | sí |

| # | Cadena | Se espera | Simulador | JFLAP |
|---|---|---|---|---|
| 1 | `0` | acepta | acepta | acepta |
| 2 | `01` | acepta | acepta | acepta |
| 3 | `1010` | acepta | acepta | acepta |
| 4 | `0111000` | acepta | acepta | acepta |
| 5 | `11010111111` | acepta | acepta | acepta |
| 6 | λ | rechaza | rechaza | rechaza |
| 7 | `#` (símbolo fuera de Σ) | rechaza | rechaza | rechaza |
| 8 | `0#` (símbolo fuera de Σ) | rechaza | rechaza | rechaza |
| 9 | `#11` (símbolo fuera de Σ) | rechaza | rechaza | rechaza |

Nota sobre los casos: todas las cadenas sobre Σ pertenecen al lenguaje, así que las inválidas usan un símbolo fuera de Σ (#).

<details><summary>Recorrido completo de cada cadena</summary>

1. `0`: {A, B} -0→ {C, D, E, F} — ✔
  Árbol de cómputo: 8 caminos, 5 de aceptación (se muestran 6):
    - A -λ→ B -0→ C -λ→ E — ✔ acepta
    - A -λ→ B -0→ D — ✔ acepta
    - A -λ→ B -0→ D -λ→ E — ✔ acepta
    - A -λ→ B -0→ C — ✘ termina fuera de F
    - A -λ→ B -0→ D -λ→ F — ✘ termina fuera de F
    - A -0→ F — ✘ termina fuera de F
2. `01`: {A, B} -0→ {C, D, E, F} -1→ {A, B, C, D, E, F} — ✔
  Árbol de cómputo: 22 caminos, 14 de aceptación (se muestran 6):
    - A -λ→ B -0→ C -λ→ E -1→ D — ✔ acepta
    - A -λ→ B -0→ C -λ→ E -1→ D -λ→ E — ✔ acepta
    - A -λ→ B -0→ C -λ→ E -1→ D -λ→ F -λ→ E — ✔ acepta
    - A -λ→ B -0→ C -λ→ E -1→ D -λ→ F — ✘ termina fuera de F
    - A -λ→ B -0→ C -1→ A — ✘ termina fuera de F
    - A -λ→ B -0→ C -1→ A -λ→ B — ✘ termina fuera de F
3. `1010`: {A, B} -1→ {A, B, C, E, F} -0→ {B, C, D, E, F} -1→ {A, B, C, D, E, F} -0→ {A, B, C, D, E, F} — ✔
  Árbol de cómputo: 106 caminos, 38 de aceptación (se muestran 6):
    - A -λ→ B -1→ B -0→ C -λ→ E -1→ D -λ→ F -0→ E — ✔ acepta
    - A -λ→ B -1→ B -0→ C -λ→ E -1→ D -0→ C -λ→ E — ✔ acepta
    - A -λ→ B -1→ B -0→ C -1→ A -λ→ B -0→ C -λ→ E — ✔ acepta
    - A -λ→ B -1→ B -0→ C -λ→ E -1→ D -λ→ E — ✘ muere tras leer `101`
    - A -λ→ B -1→ B -0→ C -λ→ E -1→ D -λ→ F -λ→ E — ✘ muere tras leer `101`
    - A -λ→ B -1→ B -0→ C -λ→ E -1→ D -λ→ F -0→ B — ✘ termina fuera de F
4. `0111000`: {A, B} -0→ {C, D, E, F} -1→ {A, B, C, D, E, F} -1→ {A, B, C, D, E, F} -1→ {A, B, C, D, E, F} -0→ {A, B, C, D, E, F} -0→ {A, B, C, D, E, F} -0→ {A, B, C, D, E, F} — ✔
  Árbol de cómputo: 200+ caminos, 59 de aceptación (se muestran 6):
    - A -λ→ B -0→ C -λ→ E -1→ D -λ→ E -1→ D -λ→ E -1→ D -λ→ F -0→ B -0→ D -λ→ F -0→ E — ✔ acepta
    - A -λ→ B -0→ C -λ→ E -1→ D -λ→ E -1→ D -λ→ E -1→ D -λ→ F -0→ B -0→ D -0→ C -λ→ E — ✔ acepta
    - A -λ→ B -0→ C -λ→ E -1→ D -λ→ E -1→ D -λ→ E -1→ D -0→ A -λ→ B -0→ D -λ→ F -0→ E — ✔ acepta
    - A -λ→ B -0→ C -λ→ E -1→ D -λ→ E -1→ D -λ→ E -1→ D -λ→ E — ✘ muere tras leer `0111`
    - A -λ→ B -0→ C -λ→ E -1→ D -λ→ E -1→ D -λ→ E -1→ D -λ→ F -λ→ E — ✘ muere tras leer `0111`
    - A -λ→ B -0→ C -λ→ E -1→ D -λ→ E -1→ D -λ→ E -1→ D -λ→ F -0→ B -0→ C -λ→ E — ✘ muere tras leer `011100`
5. `11010111111`: {A, B} -1→ {A, B, C, E, F} -1→ {A, B, C, D, E, F} -0→ {A, B, C, D, E, F} -1→ {A, B, C, D, E, F} -0→ {A, B, C, D, E, F} -1→ {A, B, C, D, E, F} -1→ {A, B, C, D, E, F} -1→ {A, B, C, D, E, F} -1→ {A, B, C, D, E, F} -1→ {A, B, C, D, E, F} -1→ {A, B, C, D, E, F} — ✔
  Árbol de cómputo: 200+ caminos, 137 de aceptación (se muestran 6):
    - A -λ→ B -1→ B -1→ B -0→ C -λ→ E -1→ D -λ→ F -0→ B -1→ B -1→ B -1→ B -1→ B -1→ B -1→ E — ✔ acepta
    - A -λ→ B -1→ B -1→ B -0→ C -λ→ E -1→ D -λ→ F -0→ B -1→ B -1→ B -1→ B -1→ B -1→ E -1→ D — ✔ acepta
    - A -λ→ B -1→ B -1→ B -0→ C -λ→ E -1→ D -λ→ F -0→ B -1→ B -1→ B -1→ B -1→ B -1→ E -1→ D -λ→ E — ✔ acepta
    - A -λ→ B -1→ B -1→ B -0→ C -λ→ E -1→ D -λ→ E — ✘ muere tras leer `1101`
    - A -λ→ B -1→ B -1→ B -0→ C -λ→ E -1→ D -λ→ F -λ→ E — ✘ muere tras leer `1101`
    - A -λ→ B -1→ B -1→ B -0→ C -λ→ E -1→ D -λ→ F -0→ B -1→ B -1→ B -1→ B -1→ B -1→ B -1→ B — ✘ termina fuera de F
6. λ: {A, B} — ✘
  Árbol de cómputo: 2 caminos, 0 de aceptación:
    - A — ✘ termina fuera de F
    - A -λ→ B — ✘ termina fuera de F
7. `#`: {A, B} -#→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - A -λ→ B — ✘ muere tras leer λ
8. `0#`: {A, B} -0→ {C, D, E, F} -#→ ∅ — ✘
  Árbol de cómputo: 4 caminos, 0 de aceptación:
    - A -λ→ B -0→ C -λ→ E — ✘ muere tras leer `0`
    - A -λ→ B -0→ D -λ→ E — ✘ muere tras leer `0`
    - A -λ→ B -0→ D -λ→ F -λ→ E — ✘ muere tras leer `0`
    - A -0→ F -λ→ E — ✘ muere tras leer `0`
9. `#11`: {A, B} -#→ ∅ -1→ ∅ -1→ ∅ — ✘
  Árbol de cómputo: 1 caminos, 0 de aceptación:
    - A -λ→ B — ✘ muere tras leer λ

</details>

Simulación paso a paso en JFLAP con `01`: [ver captura](../../evidencias/jflap/pasos/L3-200.png).

**Conversión.** AFND-λ (6 estados) → AFND sin λ con δ'(q, a) = Cl(δ(Cl(q), a)) y F' = {q : Cl(q) ∩ F ≠ ∅}, quitando los inaccesibles: 6 estados, [`L3-200-AFND.jff`](../../automatas/conversiones/L3-200-AFND.jff). AFND (6 estados) → AFD con *Convert to DFA* de JFLAP (clase `NFAToDFA`): 6 estados, [`L3-200-AFD.jff`](../../automatas/conversiones/L3-200-AFD.jff) ([.json](../../automatas/conversiones/L3-200-AFD.json), [.xml](../../automatas/conversiones/L3-200-AFD.xml)). JFLAP omite el conjunto vacío; con él, el AFD completo tiene 6 estados, y el AFD mínimo (Hopcroft), 2. La cota es 2^6 = 64. Se verificó que los tres autómatas aceptan el mismo lenguaje.

