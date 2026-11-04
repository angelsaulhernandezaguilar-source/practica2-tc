# Práctica 3 · Ejercicio 1. Conversión de AFD a expresiones regulares

[← Volver al índice](../../README.md)

## 1.1 Conversión con JFLAP

Se eligieron cinco AFD (δ total) de las Listas 2 y 3, todos ya entregados y verificados en la Práctica 2:

| AFD | Lista y problema | Lenguaje | Archivo |
|---|---|---|---|
| L2-130 | Lista 2, 130 | M = ({q1, q2, q3}, {0, 1}, δ, q1, {q2}) dado por tabla | [`L2-130.jff`](../../automatas/practica3/afd-a-er/L2-130.jff) |
| L2-138 | Lista 2, 138 | Palabras sobre {a, b} cuyo número de b es múltiplo de 3 | [`L2-138.jff`](../../automatas/practica3/afd-a-er/L2-138.jff) |
| L2-141 | Lista 2, 141 | Palabras sobre {0, 1} en las que cada 0 va seguido inmediatamente de un 1 | [`L2-141.jff`](../../automatas/practica3/afd-a-er/L2-141.jff) |
| L3-257 | Lista 3, 257 | AFD de la tabla 257 | [`L3-257.jff`](../../automatas/practica3/afd-a-er/L3-257.jff) |
| L3-258 | Lista 3, 258 | AFD de la tabla 258 | [`L3-258.jff`](../../automatas/practica3/afd-a-er/L3-258.jff) |

### Cómo se obtuvo cada conversión

Cada conversión se hizo en la ventana real de JFLAP 7.1 con
[`herramientas/JflapER.java`](../../herramientas/JflapER.java), lanzada por
[`herramientas/practica3_er.py`](../../herramientas/practica3_er.py). El programa abre el `.jff`, elige
**Convert → Convert FA to RE** y aplica las mismas acciones que haría una persona con las herramientas de esa
ventana, usando los métodos del controlador de JFLAP (`FSAToREController`):

1. *Make Single Noninitial Final State*: si hace falta, crea un estado final nuevo y une con λ los finales
   viejos a él (`stateCreate`, `transitionCreate`).
2. *Reform Transitions*: combina en una sola etiqueta las transiciones paralelas (`transitionCollapse`) y
   pone una transición ∅ entre cada par de estados sin transición (`transitionCreate`).
3. *Remove States*: elimina, uno por uno, los estados que no son ni el inicial ni el final
   (`stateCollapse` y `finalizeStateRemove`; es la herramienta *State Collapser*). Se eliminan en orden
   alfabético.
4. *Export* abre la expresión en una ventana nueva; ahí **Convert → Convert to NFA**, *Do All* y *Export*
   construyen su AFN-λ.
5. El AFN se compara con el AFD original con `FSAEqualityChecker`, la clase que ejecuta
   **Test → Compare Equivalence**, y se simulan seis cadenas (las tres aceptadas y las tres rechazadas más
   cortas) en ambos autómatas con el simulador de JFLAP.

Tras cada acción se guardó una captura de la ventana (`paso-NN.png`) y un renglón en `pasos.tsv` con la etapa
que muestra JFLAP, la acción hecha y todas las transiciones del grafo generalizado. Todo está en
[`evidencias/practica3/jflap/`](../../evidencias/practica3/jflap/). Las expresiones se guardaron como
expresiones de JFLAP (`<type>re</type>`) en `automatas/practica3/afd-a-er/<AFD>-ER.jff`.

**Resumen**

| AFD | Expresión de JFLAP | Estados eliminados | AFN de *Convert to NFA* | *Compare Equivalence* | 6 cadenas |
|---|---|---|---|---|---|
| L2-130 | `0*1(1+0(0+1))*` | q3 | 24 estados | equivalentes | coinciden |
| L2-138 | `(a+ba*ba*b)*` | q1, q2 | 22 estados | equivalentes | coinciden |
| L2-141 | `(1+01)*` | q1, q2 | 12 estados | **no equivalentes** (ver la nota); sin el sumidero q2: equivalentes | coinciden |
| L3-257 | `((1+01*0)(0+1))*(01*+1+01*0)` | B, C | 48 estados | equivalentes | coinciden |
| L3-258 | `((0+1)(01)*(1+00))*(0+1)(01)*` | B | 44 estados | equivalentes | coinciden |

Además, el núcleo del proyecto confirma cada resultado: la expresión de JFLAP y la simplificada se convierten
con Thompson y se comparan con el AFD buscando la cadena más corta en la diferencia simétrica
(`Automata.contraejemplo`); en los diez casos no existe.

> **Nota sobre el AFD 141 y *Compare Equivalence*.** El AFD 141 tiene un estado sumidero explícito, q2 (si un 0
> va seguido de otro 0, la cadena ya no puede aceptarse). Comparado con el AFN de su propia expresión,
> `FSAEqualityChecker` responde *false*, aunque las seis cadenas coinciden y el núcleo no encuentra
> contraejemplo. `JflapER` repite la comparación con el mismo AFD sin los estados desde los que no se llega a
> F (sólo q2) y la respuesta es *true*. Es decir, el resultado negativo es un defecto de la comprobación de
> JFLAP 7.1 con estados sumidero, no una diferencia de lenguajes: quitar q2 no cambia el lenguaje, porque
> ninguna cadena que lo visite se acepta. Los otros cuatro AFD no tienen sumidero y dan *true* en las dos
> comparaciones.

### Leyes algebraicas que se usan

Todas son de Hopcroft, Motwani y Ullman (2007), sección 3.4 (*Algebraic Laws for Regular Expressions*); las
secciones 3.4.6 y 3.4.7 dan además el método para descubrir y comprobar una ley nueva (sustituir las variables
por símbolos distintos y comparar los lenguajes de las dos expresiones concretas), que es lo que hace el núcleo
al comparar cada par de expresiones.

| Ley | Forma | Sección |
|---|---|---|
| Conmutatividad de la unión | r + s = s + r | 3.4.1 |
| Identidad de la concatenación | λr = rλ = r | 3.4.2 |
| Distributiva por la izquierda | r(s + t) = rs + rt | 3.4.3 |
| Distributiva por la derecha | (s + t)r = sr + tr | 3.4.3 |
| Idempotencia de la unión | r + r = r | 3.4.4 |
| Cerraduras | (λ + r)* = r*, r* = λ + r*r, ∅* = λ | 3.4.5 |
| Desplazamiento | (rs)*r = r(sr)* | Se comprueba con la prueba de 3.4.7 |
| Unión bajo estrella | (r + s)* = (r*s)*r* | Se comprueba con la prueba de 3.4.7 |

---

### AFD 130

| δ | 0 | 1 |
|---|---|---|
| → q1 | q1 | q2 |
| \* q2 | q3 | q2 |
| q3 | q2 | q2 |

**Análisis previo.** q1 tiene un lazo con 0 y sólo sale de él con 1, así que la expresión empieza con `0*1`. Desde
q2, el AFD sólo puede quedarse en {q2, q3}: hay un lazo q2 -1→ q2 y un ciclo q2 -0→ q3 -(0+1)→ q2, que es
la rama que leerá una palabra de dos símbolos `0(0+1)`. Como q2 es el único final, lo anterior se repite:
se espera `0*1(1 + 0(0+1))*`. Hay un solo estado que eliminar (q3).

**Estados eliminados en JFLAP.** Como q2 ya es el único final y no es inicial, JFLAP omite la primera etapa.

| Paso | Acción | Captura |
|---|---|---|
| 0 | Autómata inicial en *Convert FA to RE* | [paso-00](../../evidencias/practica3/jflap/L2-130/paso-00.png) |
| 1 | Se combinan q3 -0→ q2 y q3 -1→ q2 en q3 -(0+1)→ q2 | [paso-01](../../evidencias/practica3/jflap/L2-130/paso-01.png) |
| 2-5 | Transiciones ∅ en los pares sin transición (q1→q3, q2→q1, q3→q1, q3→q3) | [paso-05](../../evidencias/practica3/jflap/L2-130/paso-05.png) |
| 6 | **Se elimina q3**: q2 -0→ q3 -(0+1)→ q2 se suma al lazo de q2: `1 + 0(0+1)`; los caminos con ∅ desaparecen | [paso-06](../../evidencias/practica3/jflap/L2-130/paso-06.png) |

Expresión final: `0*1(1+0(0+1))*`, que es la anticipada. Verificación: [expresión](../../evidencias/practica3/jflap/L2-130/expresion.png),
[Convert to NFA](../../evidencias/practica3/jflap/L2-130/re-a-afn.png),
[AFN exportado](../../evidencias/practica3/jflap/L2-130/afn.png); Compare Equivalence: equivalentes.

| Cadena | AFD | AFN de la expresión |
|---|---|---|
| 1 | aceptada | aceptada |
| 01 | aceptada | aceptada |
| 11 | aceptada | aceptada |
| λ | rechazada | rechazada |
| 0 | rechazada | rechazada |
| 00 | rechazada | rechazada |

**Simplificación.** No hay una forma más corta: el único cambio posible es la distributiva por la izquierda,
`0(0+1) = 00 + 01`, que da `0*1(1+00+01)*`, con el mismo número de símbolos. Se conserva la de JFLAP.

---

### AFD 138

| δ | a | b |
|---|---|---|
| → \* q0 | q0 | q1 |
| q1 | q1 | q2 |
| q2 | q2 | q0 |

**Análisis previo.** Cada estado tiene un lazo con a (las a no cambian la cuenta) y las b forman un ciclo
q0 → q1 → q2 → q0. El inicial también es el final, así que toda la expresión será una estrella: se repiten
«una a» o «una vuelta completa al ciclo», que lee `b a* b a* b`. Se espera `(a + ba*ba*b)*`.

**Estados eliminados en JFLAP.** El inicial q0 también es final, así que JFLAP crea un final nuevo, q3, con
q0 -λ→ q3.

| Paso | Acción | Captura |
|---|---|---|
| 1-2 | Se crea q3 y la transición λ desde q0 | [paso-02](../../evidencias/practica3/jflap/L2-138/paso-02.png) |
| 3-11 | Transiciones ∅ en los 9 pares sin transición | [paso-11](../../evidencias/practica3/jflap/L2-138/paso-11.png) |
| 12 | **Se elimina q1**: q0 -b→ q1 -a*→ q1 -b→ q2 da q0 -`ba*b`→ q2 | [paso-12](../../evidencias/practica3/jflap/L2-138/paso-12.png) |
| 13 | **Se elimina q2**: q0 -`ba*b`→ q2 -a*→ q2 -b→ q0 se suma al lazo de q0: `a + ba*ba*b` | [paso-13](../../evidencias/practica3/jflap/L2-138/paso-13.png) |

Expresión final: `(a+ba*ba*b)*` (el λ hacia q3 desaparece por la identidad rλ = r).
[Convert to NFA](../../evidencias/practica3/jflap/L2-138/re-a-afn.png); Compare Equivalence: equivalentes.

| Cadena | AFD | AFN de la expresión |
|---|---|---|
| λ | aceptada | aceptada |
| a | aceptada | aceptada |
| aa | aceptada | aceptada |
| b | rechazada | rechazada |
| ab | rechazada | rechazada |
| ba | rechazada | rechazada |

**Simplificación.** La expresión ya es la mínima natural. Una forma equivalente que separa las a sueltas es
`(a*ba*ba*b)*a*`, por la ley de unión bajo estrella (r + s)* = (r*s)*r* con r = a y s = ba*ba*b, seguida de
es más larga, así que se conserva `(a+ba*ba*b)*`.

---

### AFD 141

| δ | 0 | 1 |
|---|---|---|
| → \* q0 | q1 | q0 |
| q1 | q2 | q0 |
| q2 | q2 | q2 |

**Análisis previo.** Desde q0 hay dos ciclos que regresan a q0: el lazo `1` y la rama q0 -0→ q1 -1→ q0, que
lee `01`. La rama q1 -0→ q2 lleva al sumidero q2, que no aporta nada a la expresión (todo camino que lo
visita tiene etiqueta ∅). El inicial es el final: se espera `(1 + 01)*`.

**Estados eliminados en JFLAP.**

| Paso | Acción | Captura |
|---|---|---|
| 1-2 | Final nuevo q3 y q0 -λ→ q3 | [paso-02](../../evidencias/practica3/jflap/L2-141/paso-02.png) |
| 3 | Se combinan los lazos de q2: `0+1` | [paso-03](../../evidencias/practica3/jflap/L2-141/paso-03.png) |
| 4-13 | Transiciones ∅ en los 10 pares sin transición | [paso-13](../../evidencias/practica3/jflap/L2-141/paso-13.png) |
| 14 | **Se elimina q1**: q0 -0→ q1 -1→ q0 se suma al lazo de q0 (`1+01`) y q0 -0→ q1 -0→ q2 da q0 -`00`→ q2 | [paso-14](../../evidencias/practica3/jflap/L2-141/paso-14.png) |
| 15 | **Se elimina q2**: todos sus caminos de salida son ∅, así que no cambia ninguna etiqueta | [paso-15](../../evidencias/practica3/jflap/L2-141/paso-15.png) |

Expresión final: `(1+01)*`. [Convert to NFA](../../evidencias/practica3/jflap/L2-141/re-a-afn.png). Compare
Equivalence contra el AFD completo: *false*; contra el AFD sin el sumidero q2: *true* (ver la nota de arriba).

| Cadena | AFD | AFN de la expresión |
|---|---|---|
| λ | aceptada | aceptada |
| 1 | aceptada | aceptada |
| 01 | aceptada | aceptada |
| 0 | rechazada | rechazada |
| 00 | rechazada | rechazada |
| 10 | rechazada | rechazada |

**Simplificación.** Ninguna; `(1+01)*` tiene cinco símbolos y no admite una forma más corta.

---

### AFD 257

| δ | 0 | 1 |
|---|---|---|
| → A | B | C |
| \* B | C | B |
| \* C | A | A |

**Análisis previo.** Hay dos finales, así que JFLAP creará un final nuevo y la expresión tendrá una unión de
dos «salidas». Toda vuelta a A pasa por C (C -0+1→ A), y a C se llega directo (`1`) o por B (`01*0`, con el
lazo `1` de B en medio): la parte que se repite es `(1 + 01*0)(0+1)`. Para terminar se sale hacia B (`01*`)
o hacia C (`1` o `01*0`). Se espera `((1+01*0)(0+1))*(01* + 1 + 01*0)`.

**Estados eliminados en JFLAP.**

| Paso | Acción | Captura |
|---|---|---|
| 1-3 | Final nuevo q3, con λ desde C y desde B | [paso-03](../../evidencias/practica3/jflap/L3-257/paso-03.png) |
| 4 | Se combinan C -0→ A y C -1→ A: `0+1` | [paso-04](../../evidencias/practica3/jflap/L3-257/paso-04.png) |
| 5-13 | Transiciones ∅ en los 9 pares sin transición | [paso-13](../../evidencias/practica3/jflap/L3-257/paso-13.png) |
| 14 | **Se elimina B**: A -0→ B -1*→ B -0→ C da A -`1+01*0`→ C; A -0→ B -1*→ B -λ→ q3 da A -`01*`→ q3 | [paso-14](../../evidencias/practica3/jflap/L3-257/paso-14.png) |
| 15 | **Se elimina C**: A -`1+01*0`→ C -`0+1`→ A da el lazo `(1+01*0)(0+1)`; A -`1+01*0`→ C -λ→ q3 se suma a A → q3 | [paso-15](../../evidencias/practica3/jflap/L3-257/paso-15.png) |

Expresión final: `((1+01*0)(0+1))*(01*+1+01*0)`.
[Convert to NFA](../../evidencias/practica3/jflap/L3-257/re-a-afn.png); Compare Equivalence: equivalentes.

| Cadena | AFD | AFN de la expresión |
|---|---|---|
| 0 | aceptada | aceptada |
| 1 | aceptada | aceptada |
| 00 | aceptada | aceptada |
| λ | rechazada | rechazada |
| 10 | rechazada | rechazada |
| 11 | rechazada | rechazada |

**Simplificación.**

| Paso | Expresión | Ley |
|---|---|---|
| 0 | `((1+01*0)(0+1))*(01* + 1 + 01*0)` | (JFLAP) |
| 1 | `((1+01*0)(0+1))*(01* + 01*0 + 1)` | Conmutatividad de la unión (3.4.1) |
| 2 | `((1+01*0)(0+1))*(01*λ + 01*0 + 1)` | Identidad rλ = r (3.4.2) |
| 3 | `((1+01*0)(0+1))*(01*(λ+0) + 1)` | Distributiva por la izquierda (3.4.3) |

El resultado coincide con la expresión que se entregó en la Práctica 1 para este problema
([`L3-257-ER.jff`](../../automatas/lista2-afd/L3-257-ER.jff)), obtenida allá con el lema de Arden.

---

### AFD 258

| δ | 0 | 1 |
|---|---|---|
| → A | C | C |
| B | A | C |
| \* C | B | A |

**Análisis previo.** A sólo sale hacia C (con 0 o 1) y C es el final. Desde C hay un ciclo corto
C -0→ B -1→ C (`01`) y dos formas de volver a A: directo (`1`) o por B (`00`). Se espera
`((0+1)(01)*(1+00))*(0+1)(01)*`: cada vuelta completa A → C → A, y al final A → C con ciclos `01`.

**Estados eliminados en JFLAP.** C ya es el único final y no es inicial.

| Paso | Acción | Captura |
|---|---|---|
| 1 | Se combinan A -0→ C y A -1→ C: `0+1` | [paso-01](../../evidencias/practica3/jflap/L3-258/paso-01.png) |
| 2-5 | Transiciones ∅ en los 4 pares sin transición | [paso-05](../../evidencias/practica3/jflap/L3-258/paso-05.png) |
| 6 | **Se elimina B**: C -0→ B -1→ C da el lazo `01` en C; C -0→ B -0→ A se suma a C -1→ A: `1+00` | [paso-06](../../evidencias/practica3/jflap/L3-258/paso-06.png) |

Con dos estados (A inicial, C final) JFLAP aplica la fórmula del grafo de dos estados,
(r + s u* t)* s u* con r = ∅ (lazo de A), s = `0+1`, u = `01`, t = `1+00`. Expresión final:
`((0+1)(01)*(1+00))*(0+1)(01)*`. [Convert to NFA](../../evidencias/practica3/jflap/L3-258/re-a-afn.png);
Compare Equivalence: equivalentes.

| Cadena | AFD | AFN de la expresión |
|---|---|---|
| 0 | aceptada | aceptada |
| 1 | aceptada | aceptada |
| 001 | aceptada | aceptada |
| λ | rechazada | rechazada |
| 00 | rechazada | rechazada |
| 01 | rechazada | rechazada |

**Simplificación.** Con la ley de desplazamiento (rs)*r = r(sr)*, tomando r = `(0+1)(01)*` y s = `1+00`,
se obtiene `(0+1)(01)*((1+00)(0+1)(01)*)*`, que tiene la misma longitud. La de JFLAP ya es irreducible en
longitud y se conserva.

---

## 1.2 Comparación de métodos

Se resolvieron a mano los AFD **130** y **257** por los tres métodos. Cada expresión intermedia y final se
comprobó después con el núcleo (Thompson y búsqueda de contraejemplo): las tres son equivalentes al AFD.

### AFD 130

**a) Eliminación de estados** (Hopcroft et al., 2007, sección 3.2.2). Igual que en JFLAP: q1 es inicial y q2 es
el único final, así que sólo se elimina q3. Para cada par (p, r) con p → q3 → r se agrega
R_pq3 (R_q3q3)* R_q3r a R_pr; aquí sólo hay q2 -0→ q3 -(0+1)→ q2 y R_q3q3 = ∅, con ∅* = λ:

R_q2q2 = 1 + 0 λ (0+1) = 1 + 0(0+1).

Con dos estados, la fórmula de la sección 3.2.2 para inicial ≠ final es (R + S U* T)* S U*, con R = 0 (lazo
de q1), S = 1, U = 1 + 0(0+1), T = ∅: (0 + ∅)* 1 (1+0(0+1))* = **0\*1(1+0(0+1))\***.

**b) Construcción Rᵢⱼ⁽ᵏ⁾** (Hopcroft et al., 2007, sección 3.2.1, teorema 3.4; Kleene, 1956). Numeración
1 = q1, 2 = q2, 3 = q3; L = R₁₂⁽³⁾. Recurrencia: Rᵢⱼ⁽ᵏ⁾ = Rᵢⱼ⁽ᵏ⁻¹⁾ + Rᵢₖ⁽ᵏ⁻¹⁾ (Rₖₖ⁽ᵏ⁻¹⁾)* Rₖⱼ⁽ᵏ⁻¹⁾.

| | k = 0 | k = 1 (por q1) | k = 2 (por q2) |
|---|---|---|---|
| R₁₁ | λ + 0 | 0\* | 0\* |
| R₁₂ | 1 | 0\*1 | 0\*11\* |
| R₁₃ | ∅ | ∅ | 0\*11\*0 |
| R₂₂ | λ + 1 | λ + 1 | 1\* |
| R₂₃ | 0 | 0 | 1\*0 |
| R₃₂ | 0 + 1 | 0 + 1 | (0+1)1\* |
| R₃₃ | λ | λ | λ + (0+1)1\*0 |

Simplificaciones usadas en la tabla: (λ + 0)* = 0* y (λ + 0) + (λ + 0)0*(λ + 0) = 0* (cerraduras, 3.4.5);
0*1 + 0*1·1*(λ+1) = 0*11* porque 1*(λ+1) = 1* (ídem). R₂₁ y R₃₁ son ∅ en todas las k, porque ningún estado
regresa a q1.

R₁₂⁽³⁾ = R₁₂⁽²⁾ + R₁₃⁽²⁾ (R₃₃⁽²⁾)* R₃₂⁽²⁾ = 0\*11\* + 0\*11\*0 (λ + (0+1)1\*0)\* (0+1)1\*

y como (λ + r)* = r*: **0\*11\* + 0\*11\*0((0+1)1\*0)\*(0+1)1\***. Se calcularon 21 expresiones (7 por ronda;
las de R₂₁ y R₃₁ son triviales).

**c) Ecuaciones y lema de Arden** (apunte del curso, unidad 1.2.6; la forma X = Xa + b ⇒ X = ba*, con λ ∉ L(a)).
Para cada estado, X_q es el conjunto de cadenas que llevan de q1 a q: se suman las transiciones de llegada y
λ en el inicial.

| Ecuación | Resolución |
|---|---|
| X₁ = λ + X₁0 | Arden: X₁ = λ0\* = 0\* |
| X₃ = X₂0 | Sustitución |
| X₂ = X₁1 + X₂1 + X₃(0+1) = X₁1 + X₂(1 + 0(0+1)) | Arden: X₂ = X₁1(1+0(0+1))\* |

L = X₂ = **0\*1(1+0(0+1))\***.

### AFD 257

**a) Eliminación de estados.** Hay dos finales; se agrega un final f con B -λ→ f y C -λ→ f (como JFLAP).

1. Eliminar B (lazo `1`): A -0→ B -1*→ B -0→ C da A → C: `1 + 01*0`; A -0→ B -1*→ B -λ→ f da A → f: `01*`.
2. Eliminar C (sin lazo, ∅* = λ): A → C → A da el lazo de A: `(1+01*0)(0+1)`; A → C -λ→ f se suma a
   A → f: `01* + (1+01*0)λ = 01* + 1 + 01*0` (distributiva por la derecha e identidad).
3. Grafo de dos estados con lazo sólo en A: **((1+01\*0)(0+1))\*(01\* + 1 + 01\*0)**.

**b) Construcción Rᵢⱼ⁽ᵏ⁾.** 1 = A, 2 = B, 3 = C; L = R₁₂⁽³⁾ + R₁₃⁽³⁾. Se abrevia u = 1 + 01*0 y v = 0 + 1.

| | k = 0 | k = 1 (por A) | k = 2 (por B) |
|---|---|---|---|
| R₁₁ | λ | λ | λ |
| R₁₂ | 0 | 0 | 01\* |
| R₁₃ | 1 | 1 | 1 + 01\*0 = u |
| R₂₂ | λ + 1 | λ + 1 | 1\* |
| R₂₃ | 0 | 0 | 1\*0 |
| R₃₁ | 0 + 1 | 0 + 1 | 0 + 1 = v |
| R₃₂ | ∅ | (0+1)0 | (0+1)01\* = v01\* |
| R₃₃ | λ | λ + (0+1)1 | λ + (0+1)(1 + 01\*0) = λ + vu |

(R₂₁ = ∅ en todas las k.) Con k = 3, y (λ + vu)* = (vu)*:

- R₁₂⁽³⁾ = 01\* + u(vu)\*v01\*
- R₁₃⁽³⁾ = u + u(vu)\*(λ + vu) = u(vu)\*  (porque λ + vu ⊆ (vu)* y r + r s* = r s* cuando λ ∈ s*)

L = 01\* + u(vu)\*v01\* + u(vu)\*. Simplificación: por desplazamiento, u(vu)\* = (uv)\*u, así que
u(vu)\*v = (uv)\*uv; entonces 01\* + (uv)\*uv01\* = (λ + (uv)\*uv)01\* = (uv)\*01\* (cerraduras: r\* = λ + r\*r).
L = (uv)\*01\* + (uv)\*u = (uv)\*(01\* + u) = **((1+01\*0)(0+1))\*(01\* + 1 + 01\*0)** (distributiva).
Se calcularon 27 expresiones (9 por ronda) más la simplificación final, que fue la parte difícil.

**c) Ecuaciones y lema de Arden.**

| Ecuación | Resolución |
|---|---|
| X_B = X_A0 + X_B1 | Arden: X_B = X_A01\* |
| X_C = X_A1 + X_B0 = X_A1 + X_A01\*0 | Distributiva: X_C = X_A(1 + 01\*0) |
| X_A = λ + X_C(0+1) = λ + X_A(1+01\*0)(0+1) | Arden: X_A = ((1+01\*0)(0+1))\* |

L = X_B + X_C = X_A(01\* + 1 + 01\*0) = **((1+01\*0)(0+1))\*(01\* + 1 + 01\*0)**.

### Comparación

| | Eliminación de estados | Rᵢⱼ⁽ᵏ⁾ | Ecuaciones y Arden |
|---|---|---|---|
| Base bibliográfica | Hopcroft et al. (2007), sección 3.2.2 | Hopcroft et al. (2007), sección 3.2.1, teorema 3.4; Kleene (1956) | Apunte del curso (1.2.6); lema de Arden |
| AFD 130: longitud (apariciones de símbolos de Σ) | 6 | 14 | 6 |
| AFD 130: pasos | 1 eliminación + fórmula final | 21 expresiones en 3 rondas | 3 ecuaciones, 2 aplicaciones de Arden |
| AFD 257: longitud (apariciones de símbolos de Σ) | 12 | 26 sin simplificar, 12 después | 12 |
| AFD 257: pasos | 2 eliminaciones + fórmula | 27 expresiones + simplificación con 3 leyes | 3 ecuaciones, 2 aplicaciones de Arden |
| Facilidad | Alta: se trabaja sobre el diagrama y cada paso reduce el grafo | Baja a mano: el número de expresiones crece como n³ y crecen rápido | Alta para n pequeño; hay que elegir el orden de sustitución |
| Ventaja | Es el que implementa JFLAP; resultados cortos | Totalmente mecánico, sin decisiones; es la demostración del teorema de Kleene | Algebraico, se verifica cada igualdad; da el resultado más corto con poco trabajo |
| Desventaja | El resultado depende del orden de eliminación | Expresiones muy largas que obligan a simplificar | Requiere cuidado con λ ∈ L(a) (Arden no da solución única) |

En los dos AFD, la eliminación de estados y Arden llegaron a la **misma expresión** que JFLAP, y Rᵢⱼ⁽ᵏ⁾ a
una expresión equivalente pero mucho más larga, que sólo coincide con las otras después de simplificar
con las leyes de la sección 3.4. Esto concuerda con la observación de Hopcroft et al. (2007, sección 3.2.2) de
que la eliminación de estados evita repetir el trabajo que la construcción Rᵢⱼ⁽ᵏ⁾ hace para cada par (i, j)
en cada ronda, y de que el método de Kleene produce expresiones de tamaño hasta 4ⁿ.

Fuentes: Hopcroft, Motwani y Ullman (2007); Kleene (1956); Rodger (s.f.), JFLAP. Ver [bibliografía](../bibliografia.md).
