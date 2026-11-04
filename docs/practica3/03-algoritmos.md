# Práctica 3 · Ejercicio 3. Documentación de los algoritmos

[← Volver al índice](../../README.md)

Notación: n = |Q|, k = |Σ|, m_λ = número de transiciones λ, Cl(q) es la cerradura λ (ECLOSE en Hopcroft,
Motwani y Ullman, 2007). Las referencias de libro son a la tercera edición de Hopcroft et al. (2007) y de
Sipser (2013), la bibliografía oficial usada desde la Práctica 2. Todas las funciones están en
[`src/algoritmos.py`](../../src/algoritmos.py). Cada resultado guarda en `operaciones` el número de consultas
a δ que hizo el algoritmo; la última sección las compara con las estimaciones.

## 1. Cerradura λ y simulación directa (apartado 2.1)

**Problema.** Dado un AFN-λ M = (Q, Σ, δ, q₀, F) con δ: Q × (Σ ∪ {λ}) → 𝒫(Q), calcular para cada q el conjunto
Cl(q) de estados alcanzables desde q con cero o más transiciones λ, y decidir si w ∈ L(M) sin convertir M.

**Resultado teórico.** Hopcroft et al. (2007), sección 2.5.3 (*Epsilon-Closures*), definen ECLOSE(q)
recursivamente: q ∈ ECLOSE(q), y si p ∈ ECLOSE(q) y r ∈ δ(p, λ), entonces r ∈ ECLOSE(q). La sección 2.5.4
(*Extended Transitions and Languages for ε-NFA's*) define δ̂(q, λ) = ECLOSE(q) y
δ̂(q, xa) = ECLOSE(⋃_{p ∈ δ̂(q, x)} δ(p, a)), y L(M) = {w : δ̂(q₀, w) ∩ F ≠ ∅}. La simulación directa calcula
exactamente esa recurrencia. Sipser (2013), demostración del teorema 1.39, usa la misma cerradura E(R).

**Pseudocódigo y funciones.**

```
CERRADURA(S):                          ← _cerrar(aut, S); clausura_lambda(aut, q)
  vistos ← S;  pila ← S
  mientras pila ≠ ∅:
    q ← sacar(pila)                    (un renglón de Clausura.pasos)
    para p en δ(q, λ):
      si p ∉ vistos: agregar p a vistos y a pila   (arco (q, p) en Clausura.arcos)
  devolver vistos

SIMULAR(w = a₁…aₙ):                    ← simular_directo(aut, w)
  S ← CERRADURA({q₀})                  (PasoDirecto 0: antes = {q₀}, despues = S)
  para i = 1..n:
    T ← ⋃_{q ∈ S} δ(q, aᵢ)             (PasoDirecto.antes: antes de la cerradura)
    S ← CERRADURA(T)                   (PasoDirecto.despues)
  aceptar si S ∩ F ≠ ∅                 (SimulacionDirecta.acepta)
```

**Ejemplo a mano: Lista 3, problema 197 (Cl(A)) y 196 a) (δ̂(A, 110)).**

Tabla del 197 (q₀ = A, F = {D}): A -λ→ C; B -λ→ D; C -λ→ B. A mano: Cl(A) contiene a A; por A -λ→ C entra C;
por C -λ→ B entra B; por B -λ→ D entra D; D no tiene transiciones λ. **Cl(A) = {A, B, C, D}.** El software
(`clausura_lambda(L3-197, "A")`, captura [cerradura-final](../../evidencias/practica3/app/cerradura-final.png)):

```
Se parte de {A}: todo estado está en su propia cerradura (cero transiciones λ).
Se saca A de la pila: δ(A, λ) = {C}; se agrega C.
Se saca C de la pila: δ(C, λ) = {B}; se agrega B.
Se saca B de la pila: δ(B, λ) = {D}; se agrega D.
Se saca D de la pila: δ(D, λ) = ∅, no agrega nada.
La pila quedó vacía: Cl = {A, B, C, D}.
```

Tabla del 196 (q₀ = A, F = {C}): A -0→ A, A -λ→ B; B -0→ {A, B}, B -1→ C; C sin transiciones. A mano:
δ̂(A, λ) = Cl(A) = {A, B}. Al leer 1: δ({A, B}, 1) = {C}, Cl({C}) = {C}. Al leer 1: δ({C}, 1) = ∅. Al leer 0:
∅. **δ̂(A, 110) = ∅, 110 se rechaza.** El software da lo mismo (`simular_directo(L3-196, "110")`):

```
Paso 0 (antes de leer): activos {A}; tras la cerradura λ: {A, B}. λ seguidas: A -λ→ B.
Paso 1: se lee 1 desde {A, B}. Transiciones: δ(B, 1) ∋ C. Antes de la cerradura: {C}; después de la cerradura λ: {C}.
Paso 2: se lee 1 desde {C}. Transiciones: ninguna. Antes de la cerradura: ∅; después de la cerradura λ: ∅.
Paso 3: se lee 0 desde ∅. Transiciones: ninguna. Antes de la cerradura: ∅; después de la cerradura λ: ∅.
```

Comparación: coinciden el orden en que se agregan los estados a la cerradura y cada conjunto de la
simulación. La prueba `test_simulacion_directa_muestra_antes_y_despues` fija este ejemplo.

**Número de pasos.** Cl(q): cada estado entra a la pila a lo más una vez y cada transición λ se revisa una vez:
O(n + m_λ) ⊆ O(n²). Todas las cerraduras: O(n(n + m_λ)) ⊆ O(n³). Simulación de w: por símbolo, a lo más n
consultas a δ (uniones de hasta n estados) y una cerradura: O(n²) por símbolo y **O(|w| · n²)** en total, sin
preparación previa.

## 2. Eliminación de transiciones λ (apartado 2.2)

**Problema.** Dado un AFN-λ M, construir un AFN M' = (Q, Σ, δ', q₀, F') sin transiciones λ con L(M') = L(M).

**Resultado teórico.** Hopcroft et al. (2007), sección 2.5.5 (*Eliminating ε-Transitions*), teorema 2.22: un
lenguaje es aceptado por un ε-NFA si y sólo si es aceptado por un AFD. Su construcción aplica ECLOSE dentro de
la construcción de subconjuntos; aquí se separa en dos etapas, primero un AFN sin λ con los mismos estados y
después los subconjuntos (sección 3 de este documento). Para la primera se define
δ'(q, a) = ECLOSE(δ(ECLOSE(q), a)) y F' = {q : ECLOSE(q) ∩ F ≠ ∅}. La corrección se demuestra con el mismo
argumento inductivo del teorema 2.22: para |w| ≥ 1, δ̂'(q, w) = δ̂(q, w) (para w = a es la definición; el paso
inductivo usa que ECLOSE(ECLOSE(S)) = ECLOSE(S)); para w = λ, q₀ ∈ F' si y sólo si ECLOSE(q₀) ∩ F ≠ ∅, que es
la condición de aceptar λ en M.

**Pseudocódigo y funciones.**

```
ELIMINAR-λ(M):                           ← eliminar_lambda(aut)
  para cada q: C[q] ← CERRADURA({q})     (FilaSinLambda.clausura)
  para cada q y cada a ∈ Σ:
    T ← ⋃_{r ∈ C[q]} δ(r, a)             (FilaSinLambda.movidos[a])
    δ'(q, a) ← ⋃_{p ∈ T} C[p]            (FilaSinLambda.destinos[a])
  F' ← {q : C[q] ∩ F ≠ ∅}                (FilaSinLambda.aceptacion)
  añadidas ← δ' − δ;  nuevas_finales ← F' − F
                                         (ResultadoSinLambda.agregadas, .nuevas_aceptacion)
```

**Ejemplo a mano: Lista 3, problema 199.** q₀ = A, F = {D, E}; A -0→ E, A -λ→ {B, C}; B -0→ E, B -1→ B;
C -1→ {A, C}, C -λ→ E; D -1→ D; E -1→ D.

| q | Cl(q) | δ(Cl(q), 0) → δ'(q, 0) | δ(Cl(q), 1) → δ'(q, 1) | ¿F'? |
|---|---|---|---|---|
| A | {A, B, C, E} | {E} → {E} | {B} ∪ {A, C} ∪ {D} → Cl({A, B, C, D}) = {A, B, C, D, E} | sí (E ∈ Cl(A)) |
| B | {B} | {E} → {E} | {B} → {B} | no |
| C | {C, E} | ∅ → ∅ | {A, C} ∪ {D} → Cl({A, C, D}) = {A, B, C, D, E} | sí (E ∈ Cl(C)) |
| D | {D} | ∅ | {D} | sí |
| E | {E} | ∅ | {D} | sí |

Transiciones añadidas: A -1→ A, B, C, D, E (5) y C -1→ B, D, E (3); se quitan las tres λ; **A y C pasan a ser
de aceptación**. El software da la misma tabla (captura
[eliminar-lambda-final](../../evidencias/practica3/app/eliminar-lambda-final.png)):

```
Cl(A) = {A, B, C, E}. δ'(A, 0) = Cl(δ({A, B, C, E}, 0)) = Cl({E}) = {E}; δ'(A, 1) = Cl(δ({A, B, C, E}, 1)) = Cl({A, B, C, D}) = {A, B, C, D, E}.
Cl(B) = {B}. δ'(B, 0) = Cl(δ({B}, 0)) = Cl({E}) = {E}; δ'(B, 1) = Cl(δ({B}, 1)) = Cl({B}) = {B}.
Cl(C) = {C, E}. δ'(C, 0) = Cl(δ({C, E}, 0)) = Cl(∅) = ∅; δ'(C, 1) = Cl(δ({C, E}, 1)) = Cl({A, C, D}) = {A, B, C, D, E}.
Cl(D) = {D}. δ'(D, 0) = Cl(δ({D}, 0)) = Cl(∅) = ∅; δ'(D, 1) = Cl(δ({D}, 1)) = Cl({D}) = {D}.
Cl(E) = {E}. δ'(E, 0) = Cl(δ({E}, 0)) = Cl(∅) = ∅; δ'(E, 1) = Cl(δ({E}, 1)) = Cl({D}) = {D}.
agregadas = 8 transiciones; nuevas_aceptacion = [A, C]
```

Comparación: coinciden las cinco cerraduras, las diez celdas de δ' y F' = {A, C, D, E}. Lo que el cálculo a mano
suele olvidar, y el software no, es cerrar también el conjunto de llegada: δ({A, B, C, E}, 1) = {A, B, C, D}, y E
sólo entra al cerrarlo (por C -λ→ E); sin esa segunda cerradura, δ'(A, 1) quedaría sin E.

**Número de pasos.** n cerraduras: O(n³). Para cada uno de los n·k pares (q, a): a lo más n consultas a δ con
uniones de hasta n estados, y una unión de hasta n cerraduras de tamaño n: O(n²) por par. Total
**O(k · n³)**. El autómata resultante puede tener hasta k · n² transiciones (en el 199, A pasa de 2 a 6).

## 3. Construcción de subconjuntos (apartado 2.3)

**Problema.** Dado un AFN N = (Q, Σ, δ, q₀, F), construir un AFD D con L(D) = L(N).

**Resultado teórico.** Rabin y Scott (1959), teorema 11; Hopcroft et al. (2007), sección 2.3.5 (*Equivalence of
Deterministic and Nondeterministic Finite Automata*), teorema 2.11 (si D se construye a partir de N por
subconjuntos, L(D) = L(N)) y teorema 2.12; Sipser (2013), teorema 1.39. D tiene por estados subconjuntos de
Q, estado inicial {q₀}, δ_D(S, a) = ⋃_{p ∈ S} δ(p, a) y F_D = {S : S ∩ F ≠ ∅}. Hopcroft et al. (2007, sección
2.3.5) señalan que basta construir los subconjuntos accesibles desde {q₀} (*lazy evaluation*), que es lo que
hace el algoritmo con su cola.

**Pseudocódigo y funciones.**

```
SUBCONJUNTOS(N):                          ← construir_subconjuntos(aut)
  S₀ ← {q₀}  (CERRADURA({q₀}) si N tiene λ)
  orden ← [S₀];  cola ← [S₀]
  mientras cola ≠ ∅:
    S ← sacar(cola)                       (un FilaSubconjunto, en el orden de la tabla)
    para a ∈ Σ:
      T ← ⋃_{p ∈ S} δ(p, a)               (FilaSubconjunto.destinos[a])
      si T ∉ orden: agregar T a orden y a cola   (FilaSubconjunto.nuevos)
    S es de aceptación ⇔ S ∩ F ≠ ∅        (FilaSubconjunto.aceptacion, .razon)
  ∅, si aparece, es el estado sumidero (δ_D total)
```

**Ejemplo a mano: Lista 3, problema 192.** q₀ = A, F = {C}; A -0→ B, A -1→ {B, C}; B -0→ {A, B}; C -0→ {A, C}.

| Renglón | S | δ_D(S, 0) | δ_D(S, 1) | Nuevos | ¿Aceptación? |
|---|---|---|---|---|---|
| 1 | → {A} | {B} | {B, C} | {B}, {B, C} | no: {A} ∩ F = ∅ |
| 2 | {B} | {A, B} | ∅ | {A, B}, ∅ | no |
| 3 | {B, C} | {A, B} ∪ {A, C} = {A, B, C} | ∅ | {A, B, C} | sí: {B, C} ∩ F = {C} |
| 4 | {A, B} | {B} ∪ {A, B} = {A, B} | {B, C} | — | no |
| 5 | ∅ | ∅ | ∅ | — | no |
| 6 | {A, B, C} | {A, B, C} | {B, C} | — | sí: contiene C |

Seis estados alcanzables de los 2³ = 8 posibles ({C} y {A, C} nunca aparecen). El software produce los mismos
seis renglones en el mismo orden:

```
Renglón 1: δ_D({A}, 0) = {B}; δ_D({A}, 1) = {B, C}. Nuevos: {B}, {B, C}.
Renglón 2: δ_D({B}, 0) = {A, B}; δ_D({B}, 1) = ∅. Nuevos: {A, B}, ∅.
Renglón 3: δ_D({B, C}, 0) = {A, B, C}; δ_D({B, C}, 1) = ∅. Nuevos: {A, B, C}. Es de aceptación porque S ∩ F = {C} ≠ ∅.
Renglón 4: δ_D({A, B}, 0) = {A, B}; δ_D({A, B}, 1) = {B, C}.
Renglón 5: δ_D(∅, 0) = ∅; δ_D(∅, 1) = ∅.
Renglón 6: δ_D({A, B, C}, 0) = {A, B, C}; δ_D({A, B, C}, 1) = {B, C}. Es de aceptación porque S ∩ F = {C} ≠ ∅.
```

Comparación: coinciden. La única diferencia con *Convert to DFA* de JFLAP es que JFLAP no dibuja ∅; la
captura de la [equivalencia](../../evidencias/practica3/app/equivalencia.png) muestra que el mínimo del AFN y
el del AFD de JFLAP son isomorfos.

**Número de pasos.** A lo más 2ⁿ subconjuntos alcanzables; para cada uno y cada símbolo, |S| ≤ n consultas a
δ con uniones de hasta n estados, más la búsqueda de T entre los ya vistos. **O(2ⁿ · k · n²)** en el peor caso
(la familia Lₙ de la Práctica 2 lo alcanza) y O(|Q_D| · k · n²) en general, donde |Q_D| es el número de
subconjuntos alcanzables, que en los siete casos de la lista es a lo más 2n.

## 4. Minimización de AFD y equivalencia (apartado 2.4)

**Problema.** Dado un AFD A, construir un AFD con el menor número posible de estados que acepte L(A), y
decidir si dos AFD aceptan el mismo lenguaje.

**Resultado teórico.** Hopcroft et al. (2007), sección 4.4: dos estados p, q son equivalentes si para toda w,
δ̂(p, w) ∈ F ⇔ δ̂(q, w) ∈ F (4.4.1, *Testing Equivalence of States*); el algoritmo de llenado de tabla encuentra
todos los pares distinguibles (teorema 4.20). La minimización (4.4.3, *Minimization of DFA's*) elimina los
estados inaccesibles y agrupa los equivalentes en bloques, que forman una partición porque la equivalencia de
estados es transitiva; el AFD de bloques es mínimo (4.4.4, *Why the Minimized DFA Can't Be Beaten*): ningún
AFD equivalente tiene menos estados, y **todo AFD mínimo de L es igual al de bloques salvo el nombre de los estados**. Por eso dos AFD son
equivalentes si y sólo si sus AFD mínimos son isomorfos (y 4.4.2, *Testing Equivalence of Regular
Languages*, da la misma decisión con la tabla). El refinamiento de particiones que se programó calcula la
misma relación que la tabla: la ronda k separa exactamente los pares distinguibles por una cadena de longitud
≤ k; es la versión por rondas del algoritmo que Hopcroft (1971) acelera a O(k · n log n), ya implementada en
la Práctica 2 (`Automata.minimizar`). La base es el teorema de Myhill-Nerode (Nerode, 1958).

**Pseudocódigo y funciones.**

```
MINIMIZAR(A):                                  ← minimizar_afd(aut)
  Q ← estados accesibles desde q₀ (BFS)        (ResultadoMinimo.inaccesibles)
  si δ es parcial: agregar sumidero ∅          (ResultadoMinimo.sumidero)
  Π₀ ← {F, Q − F}                              (Ronda 0)
  repetir:
    para cada bloque B de Πᵢ:
      firma(q) ← (bloque de δ(q, a) en Πᵢ, para cada a ∈ Σ)
      dividir B por firmas iguales             (Ronda.divisiones)
    hasta que Πᵢ₊₁ = Πᵢ                         (Ronda i + 1)
  cada bloque es un estado; δ([q], a) = [δ(q, a)]

ISOMORFOS(M₁, M₂):                             ← isomorfismo(m1, m2)
  φ(q0₁) ← q0₂;  recorrer M₁ en anchura:
    para a ∈ Σ: p₁ ← δ₁(q, a), p₂ ← δ₂(φ(q), a)
      si φ(p₁) existe y ≠ p₂: no son isomorfos; si no, φ(p₁) ← p₂
    q ∈ F₁ ⇔ φ(q) ∈ F₂
  φ debe ser biyectiva

EQUIVALENTES(A₁, A₂) ⇔ ISOMORFOS(MINIMIZAR(A₁), MINIMIZAR(A₂))   ← equivalentes_por_minimizacion
```

**Ejemplo a mano: Lista 3, problema 156.** q₀ = A, F = {E}; A -0→ B, A -1→ C; B -0→ C, B -1→ E; C -0→ D,
C -1→ C; D -0→ C, D -1→ E; E -0→ B, E -1→ E. Todos los estados son accesibles (A → B, C → D, E).

- Π₀ = {[E], [A, B, C, D]}.
- Ronda 1, firmas en Π₀ (bloque de δ(q, 0), bloque de δ(q, 1)): A → (ABCD, ABCD); B → (ABCD, E);
  C → (ABCD, ABCD); D → (ABCD, E). Π₁ = {[E], [A, C], [B, D]}.
- Ronda 2: A → (BD, AC); C → (BD, AC): siguen juntos. B → (AC, E); D → (AC, E): siguen juntos.
  Π₂ = Π₁: estable.

AFD mínimo de 3 estados: [A, C] -0→ [B, D], [A, C] -1→ [A, C]; [B, D] -0→ [A, C], [B, D] -1→ E;
E -0→ [B, D], E -1→ E. El software:

```
No hay estados inaccesibles.
Π0 = { [E], [A, B, C, D] }  (F y Q − F)
Π1 = { [E], [A, C], [B, D] }
   [A, B, C, D] se divide: [A, C] van a 0→[A, B, C, D], 1→[A, B, C, D]; [B, D] van a 0→[A, B, C, D], 1→[E]
Π2 = { [E], [A, C], [B, D] }
Π2 = Π1: la partición es estable.
```

con la tabla `→[A, C]: [B, D], [A, C]; [B, D]: [A, C], E; *E: [B, D], E`. Comparación: coinciden las
particiones de cada ronda y el autómata; además es isomorfo al `L3-156-simplificado.jff` entregado en la
Práctica 1 (`test_minimo_contra_el_simplificado_de_la_lista`).

**Número de pasos.** Inaccesibles: O(n · k). Cada ronda calcula n firmas de k componentes: O(n · k). Como cada
ronda que no termina aumenta el número de bloques y nunca hay más de n, hay a lo más n − 1 rondas de
refinamiento: **O(k · n²)** (Hopcroft, 1971, lo baja a O(k · n log n)). El isomorfismo recorre cada
transición una vez: O(n · k). Decidir la equivalencia de dos AFN cuesta, por tanto, lo que cuesten los
subconjuntos más O(k · N²), con N el tamaño del AFD de subconjuntos.

## 5. Validación de varias cadenas (apartado 2.5)

**Problema.** Dado M y un archivo con una cadena por línea, decidir cada una y escribir un informe.

**Resultado teórico.** El de la sección 1: L(M) = {w : δ̂(q₀, w) ∩ F ≠ ∅} (Hopcroft et al., 2007, 2.5.4).

**Pseudocódigo y funciones.** `leer_cadenas` (línea vacía o `λ` = cadena vacía, `#` = comentario) →
para cada cadena, `simular_directo` → `ResultadoCadena` → `informe_lote`. Ejemplo: el informe del 196 con
`cadenas-ejemplo.txt` ([`informe-L3-196.txt`](../../evidencias/practica3/informe-L3-196.txt)) acepta sólo `1` y `01`.
A mano: desde Cl(A) = {A, B} cada 0 regresa a {A, B} y un 1 lleva a C, que no tiene salidas, así que
L(196) = 0\*1; de las doce cadenas del archivo, sólo `1` y `01` tienen esa forma (`0012` además tiene un símbolo
fuera de Σ). Coincide con el informe.

**Número de pasos.** O(Σ |wᵢ| · n²).

## 6. Conteo de operaciones en los casos de prueba

Consultas a δ que registró cada algoritmo (`operaciones`), contra las cotas de arriba. n = estados del autómata
de entrada de cada etapa (para la minimización, el AFD de subconjuntos).

| Caso | n | k | Cerraduras (≤ n²) | Quitar λ (≤ n² + k·n²) | Subconjuntos: estados / consultas (≤ k·n·2ⁿ) | Minimización: rondas / consultas (≤ k·n²) | Mínimo |
|---|---|---|---|---|---|---|---|
| 196 | 3 | 2 | 4 | 12 | 4 / 8 | 2 / 16 | 3 |
| 197 | 4 | 2 | 10 | 30 | 2 / 10 | 1 / 4 | 1 |
| 198 | 4 | 2 | 7 | 21 | 3 / 12 | 1 / 6 | 2 |
| 199 | 5 | 2 | 9 | 27 | 5 / 16 | 2 / 20 | 3 |
| 200 | 6 | 2 | 11 | 33 | 6 / 50 | 1 / 12 | 2 |
| 192 | 3 | 2 | 3 | 9 | 6 / 18 | 3 / 36 | 6 |
| 193 | 4 | 2 | 4 | 12 | 8 / 32 | 5 / 80 | 7 |
| 194 | 4 | 3 | 4 | 16 | 4 / 27 | 1 / 12 | 2 |
| 260 | 5 | 2 | 5 | 15 | 8 / 46 | 4 / 64 | 7 |
| 261 | 5 | 2 | 5 | 15 | 5 / 22 | 2 / 20 | 3 |
| 262 | 4 | 2 | 4 | 12 | 5 / 8 | 3 / 30 | 5 |
| 263 | 3 | 2 | 3 | 9 | 3 / 10 | 2 / 12 | 3 |
| 151 | 10 | 2 | 10 | 30 | 10 / 20 | 3 / 60 | 5 |
| 155 | 12 | 2 | 12 | 36 | 10 / 20 | 3 / 60 | 5 |

(«Rondas» cuenta aquí las rondas de refinamiento, sin Π₀.) En todos los casos el conteo queda muy por debajo
de la cota del peor caso: las cerraduras tienen pocos estados, el AFD de subconjuntos nunca pasa de 2n
estados y la partición se estabiliza en pocas rondas. El 193 (8 subconjuntos con n = 4) y el 260 (8 con n = 5) son
los que más crecen; la familia Lₙ de la Práctica 2 es la que alcanza 2ⁿ.

Fuentes: Hopcroft, Motwani y Ullman (2007); Sipser (2013); Rabin y Scott (1959); Hopcroft (1971); Nerode
(1958). Ver [bibliografía](../bibliografia.md).
