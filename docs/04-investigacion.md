# Ejercicio 4. Investigación y estado del arte

[← Volver al índice](../README.md)

Notación: Σ es un alfabeto finito, Σ* el conjunto de cadenas sobre Σ y λ la cadena vacía. Las referencias
completas, en formato APA 7, están en la [bibliografía](bibliografia.md).

## 4.1 Investigación

### El no determinismo: AFN y AFN-λ

Un **autómata finito no determinista** (AFN) es una quíntupla M = (Q, Σ, δ, q₀, F), donde Q es un conjunto
finito de estados, q₀ ∈ Q es el estado inicial, F ⊆ Q es el conjunto de estados de aceptación y la función
de transición es δ: Q × Σ → 𝒫(Q) (Hopcroft et al., 2007, sección 2.3.2). La diferencia con el AFD es el
codominio: en lugar de un estado, δ(q, a) es un *conjunto* de estados, que puede ser vacío (no hay
movimiento) o tener varios elementos (hay varias opciones).

La función se extiende a cadenas de forma inductiva: δ̂(q, λ) = {q} y
δ̂(q, wa) = ⋃_{p ∈ δ̂(q, w)} δ(p, a). El lenguaje del autómata es
L(M) = {w ∈ Σ* : δ̂(q₀, w) ∩ F ≠ ∅}. Es decir, **una cadena es aceptada si existe al menos un camino**
desde q₀ que la consuma completa y termine en un estado de F; los caminos que se bloquean o que terminan
fuera de F no cuentan en contra. La cadena se rechaza solo si *ningún* camino acepta.

Un **AFN-λ** (o AFN-ε) permite además transiciones que no consumen símbolos:
δ: Q × (Σ ∪ {λ}) → 𝒫(Q) (Hopcroft et al., 2007, sección 2.5; Sipser, 2013, definición 1.37, que ya incluye
ε en la definición de AFN). La aceptación se define igual, pero cada camino puede intercalar transiciones λ
en cualquier punto, por lo que la función extendida necesita la λ-clausura.

### La λ-clausura

La λ-clausura de un estado q, Cl(q) (ECLOSE en Hopcroft et al.), es el menor conjunto que contiene a q y
que es cerrado bajo transiciones λ: si p ∈ Cl(q) y r ∈ δ(p, λ), entonces r ∈ Cl(q). Para un conjunto S,
Cl(S) = ⋃_{q ∈ S} Cl(q). Se calcula como un recorrido de grafo restringido a las aristas λ:

```text
Clausura(S):
    resultado ← S;  pila ← elementos de S
    mientras pila no esté vacía:
        q ← sacar(pila)
        para cada r en δ(q, λ):
            si r ∉ resultado: agregar r a resultado y a pila
    devolver resultado
```

Cada estado entra a la pila una sola vez, así que el costo es O(|Q| + número de transiciones λ). Con ella
se define δ̂(q, λ) = Cl(q) y δ̂(q, wa) = Cl(⋃_{p ∈ δ̂(q, w)} δ(p, a)). Su papel en el reconocimiento es
doble: el cómputo comienza en Cl(q₀), no en {q₀}, y tras cada símbolo el conjunto alcanzado se vuelve a
cerrar. Así, un estado de aceptación al que solo se llega por λ cuenta para aceptar la cadena (Hopcroft et
al., 2007, sección 2.5.3). Es exactamente lo que hacen `Automata.clausura` y `Automata.delta_gorro` en
[`src/automata.py`](../src/automata.py).

### La construcción de subconjuntos y la equivalencia entre AFD y AFN

**Teorema** (Rabin y Scott, 1959, teorema 11; Hopcroft et al., 2007, teorema 2.12). Para todo AFN
N = (Q, Σ, δ, q₀, F) existe un AFD D tal que L(D) = L(N). Como todo AFD es un AFN (con |δ(q, a)| = 1), las
dos clases reconocen exactamente los mismos lenguajes.

**Construcción.** D = (𝒫(Q), Σ, δ_D, {q₀}, F_D) con δ_D(S, a) = ⋃_{q ∈ S} δ(q, a) y
F_D = {S ⊆ Q : S ∩ F ≠ ∅}. En la práctica solo se construyen los subconjuntos alcanzables desde {q₀}.
Para un AFN-λ se usa Cl(q₀) como estado inicial y δ_D(S, a) = Cl(⋃_{q ∈ S} δ(q, a)).

**Esbozo de la demostración.** Se prueba por inducción sobre |w| que δ̂_D({q₀}, w) = δ̂_N(q₀, w). Para
w = λ ambos lados valen {q₀}. Si vale para w, entonces
δ̂_D({q₀}, wa) = δ_D(δ̂_D({q₀}, w), a) = δ_D(δ̂_N(q₀, w), a) = ⋃_{p ∈ δ̂_N(q₀, w)} δ(p, a) = δ̂_N(q₀, wa).
Por lo tanto w ∈ L(D) ⇔ δ̂_D({q₀}, w) ∈ F_D ⇔ δ̂_N(q₀, w) ∩ F ≠ ∅ ⇔ w ∈ L(N). El estado del AFD después de
leer w es, literalmente, el conjunto de estados en los que *podría* estar el AFN.

### El costo de la conversión y la cota 2ⁿ

Si |Q| = n, el AFD tiene a lo sumo 2ⁿ estados, uno por subconjunto de Q, y el tiempo de construcción es
O(2ⁿ · |Σ| · n²) en el peor caso. La cota es justa: el lenguaje
Lₙ = {w ∈ {0,1}* : el n-ésimo símbolo desde el final es 1} tiene un AFN de n + 1 estados y ningún AFD con
menos de 2ⁿ estados, porque el AFD debe recordar los últimos n símbolos (Hopcroft et al., 2007, sección
2.3.6); Moore (1971) dio familias de AFN de n estados cuyo AFD mínimo tiene exactamente 2ⁿ estados. Sin
embargo, en los autómatas que aparecen en la práctica la cota casi nunca se alcanza, porque solo se generan
los subconjuntos alcanzables. Los datos del [Ejercicio 2](02-jflap.md#24-conversiones-y-análisis-comparativo)
lo confirman: en las 89 conversiones el AFD completo más grande tuvo 89 estados, frente a cotas que llegan
a 2⁷⁶, mientras que la familia Lₙ, construida y convertida con JFLAP, produjo exactamente 2, 4, 8, 16, 32 y 64 estados.

### El teorema de Kleene: autómatas finitos y expresiones regulares

**Teorema** (Kleene, 1956). Un lenguaje es reconocido por un autómata finito si y solo si es denotado por
una expresión regular. Las dos direcciones son constructivas (Hopcroft et al., 2007, sección 3.2):

- **De expresión regular a AFN-λ.** Por inducción sobre la expresión: ∅, λ y cada símbolo tienen autómatas
  de dos estados; para r + s, rs y r* se combinan los autómatas de r y s con transiciones λ. Es la
  construcción de Thompson (1968), usada en los problemas 201-253 del Ejercicio 2.
- **De AFD a expresión regular.** Con los estados numerados 1, …, n, Rᵢⱼ⁽ᵏ⁾ denota las cadenas que llevan
  de i a j sin pasar por estados intermedios mayores que k:
  Rᵢⱼ⁽ᵏ⁾ = Rᵢⱼ⁽ᵏ⁻¹⁾ + Rᵢₖ⁽ᵏ⁻¹⁾ (Rₖₖ⁽ᵏ⁻¹⁾)* Rₖⱼ⁽ᵏ⁻¹⁾, y L(M) es la unión de R₁ⱼ⁽ⁿ⁾ con j ∈ F. Es el
  método del problema 259; el lema de Arden y la eliminación de estados son variantes del mismo cálculo.

Junto con el teorema de subconjuntos, esto da la equivalencia de cuatro formalismos: AFD, AFN, AFN-λ y
expresiones regulares definen la misma clase, los lenguajes regulares.

### Minimización: Myhill-Nerode y el algoritmo de Hopcroft

Para L ⊆ Σ*, dos cadenas x, y son **indistinguibles** respecto de L (x ≡_L y) si para toda z ∈ Σ*,
xz ∈ L ⇔ yz ∈ L. **Teorema de Myhill-Nerode** (Nerode, 1958): L es
regular si y solo si ≡_L tiene un número finito de clases de equivalencia, y en ese caso el número de
clases es el número de estados del AFD mínimo, que es único salvo el nombre de los estados. El teorema da
a la vez un criterio de no regularidad (el problema 116 lo usa: aⁱ y aʲ son distinguibles para i ≠ j) y la
justificación de la minimización: un AFD es mínimo cuando no tiene estados inaccesibles ni dos estados
equivalentes (Hopcroft et al., 2007, sección 4.4, desarrollan la minimización con esta idea de estados
distinguibles).

**Algoritmo de Hopcroft** (Hopcroft, 1971). Tras quitar los estados inaccesibles y completar δ, se parte
de la partición P = {F, Q − F} y se refina: un bloque B se divide respecto de un «divisor» (C, a) en los
estados que con a van a C y los que no. Se mantiene una lista W de divisores pendientes; al dividir un
bloque Y en Y₁ y Y₂, si Y estaba en W se reemplaza por ambos, y si no, basta agregar el menor de los dos.
Esta regla de «procesar la mitad menor» hace que cada estado entre en W O(log n) veces, y el algoritmo
corre en O(|Σ| · n log n), frente al O(|Σ| · n²) del método de llenado de tabla. Cuando la partición se
estabiliza, cada bloque es un estado del AFD mínimo. Es el método de `Automata.minimizar` y de la columna
«AFD mínimo» del Ejercicio 2.

### Qué significa que el no determinismo no aumente el poder

En términos prácticos, el teorema de Rabin y Scott significa que el no determinismo es una herramienta de
**diseño y descripción**, no de capacidad: todo lo que se puede reconocer «adivinando» se puede reconocer
sin adivinar, con memoria finita fija y leyendo cada símbolo una vez. El precio no está en *qué* se puede
reconocer sino en *cuánto cuesta* describirlo o ejecutarlo:

- Un AFN puede ser exponencialmente más pequeño que cualquier AFD equivalente (familia Lₙ), así que el no
  determinismo es una forma de compresión.
- Un AFN se puede ejecutar sin convertirlo, simulando todos los caminos a la vez (el conjunto de estados
  activos), con costo O(n²) por símbolo y sin construir 2ⁿ estados. Es lo que hacen el simulador de este
  proyecto y los motores tipo Thompson; los motores con retroceso (*backtracking*), en cambio, exploran los
  caminos uno por uno y pueden tardar un tiempo exponencial, que es el origen del ReDoS estudiado por
  Davis et al. (2018).
- Para demostrar que un lenguaje es regular basta exhibir un AFN o un AFN-λ, que suelen ser mucho más
  sencillos; la equivalencia garantiza que existe el AFD.

La situación cambia en otros modelos: para autómatas de pila el no determinismo sí aumenta el poder
(Unidad II), y para máquinas de Turing con tiempo polinomial la pregunta es el problema P vs NP, cuyo
origen es precisamente esta noción de máquina no determinista.

## 4.2 Artículo asignado: Rabin y Scott (1959)

> Rabin, M. O., & Scott, D. (1959). Finite automata and their decision problems. *IBM Journal of Research
> and Development, 3*(2), 114–125. https://doi.org/10.1147/rd.32.0114

### Dónde se prueba la determinización

En la **sección 5, «Nondeterministic operation»** (p. 120 de la revista). La **definición 9** introduce el
autómata no determinista como un sistema 𝔄 = (S, M, S₀, F), donde M asigna a cada par (estado, símbolo)
un *subconjunto* de S, y S₀ y F son subconjuntos de S. La **definición 10** fija la aceptación: la cinta
x = σ₀σ₁…σₙ₋₁ pertenece a T(𝔄) si existe una sucesión de estados s₀, s₁, …, sₙ con s₀ ∈ S₀,
sᵢ ∈ M(sᵢ₋₁, σᵢ₋₁) y sₙ ∈ F. La **definición 11** construye el autómata 𝔇(𝔄) = (T, N, t₀, G): T es el
conjunto de **todos** los subconjuntos de S; N(t, σ) es la unión de los M(s, σ) con s ∈ t; t₀ = S₀; y G
son los subconjuntos que contienen al menos un elemento de F. El **teorema 11** afirma T(𝔄) = T(𝔇(𝔄)), y
su demostración tiene dos partes: si x es aceptada por 𝔄 mediante s₀, …, sₙ, se prueba por inducción que
cada sₖ pertenece a N(t₀, σ₀…σₖ₋₁), así que el último conjunto está en G; en el otro sentido, partiendo de
un conjunto final en G, se reconstruye una sucesión de estados de 𝔄 «hacia atrás».

Con la notación del curso: el AFN es M = (Q, Σ, δ, q₀, F); el AFD es
M_D = (𝒫(Q), Σ, δ_D, {q₀}, F_D) con δ_D(S, a) = ⋃_{q ∈ S} δ(q, a) y F_D = {S ⊆ Q : S ∩ F ≠ ∅}; el
teorema dice L(M) = L(M_D), y la inducción del artículo es la prueba de δ̂_D({q₀}, w) = δ̂(q₀, w) esbozada
arriba. Es exactamente la operación que JFLAP hizo en las conversiones del Ejercicio 2.

### Diferencias de notación

| Rabin y Scott (1959) | Libro del curso (Hopcroft et al., 2007) |
|---|---|
| Autómata 𝔄 = (S, M, S₀, F), cuádrupla; el alfabeto Σ es fijo y externo | Quíntupla (Q, Σ, δ, q₀, F), con Σ como componente |
| *Tapes* (cintas) y T(𝔄), «el conjunto de cintas definido por 𝔄» | *Strings* (cadenas) y L(M), «el lenguaje de M» |
| M para la función de movimientos | δ para la función de transición |
| S₀ ⊆ S: un **conjunto** de estados iniciales | Un único estado inicial q₀ |
| 𝒫(S) completo en la construcción (definición 11) | Solo los subconjuntos alcanzables («evaluación perezosa») |
| Sin transiciones λ | AFN-λ con ECLOSE (sección 2.5) |

La notación del libro resulta más clara para trabajar con ella, por tres razones: incluir Σ en la quíntupla
hace explícito sobre qué símbolos está definida δ; el nombre L(M) conecta directamente con «lenguaje» y con
las operaciones sobre lenguajes de la Práctica 1; y construir solo los subconjuntos alcanzables es lo que
se hace en la práctica (JFLAP, el simulador). La del artículo, en cambio, es más general en un punto: al
permitir un conjunto S₀ de estados iniciales evita tener que agregar un estado nuevo con transiciones λ
para expresar una unión, lo que hace más corta la definición del producto y de la unión de autómatas.

### Por qué recibieron el Premio Turing

Rabin y Scott recibieron el Premio A. M. Turing de 1976. La mención oficial de la ACM dice: «For their
joint paper "Finite Automata and Their Decision Problem," which introduced the idea of nondeterministic
machines, which has proved to be an enormously valuable concept. Their (Scott & Rabin) classic paper has
been a continuous source of inspiration for subsequent work in this field» (Association for Computing
Machinery, s.f.).

La distinción se justifica, entonces, por haber **introducido la máquina no determinista** como concepto
formal, más que por un resultado aislado. Su valor quedó probado en tres frentes: en la teoría de autómatas,
porque el no determinismo simplificó las demostraciones (el propio artículo lo usa para dar pruebas
directas de cerraduras y de la equivalencia con los conjuntos regulares de Kleene); en las decisiones
algorítmicas que el artículo también resuelve (si un autómata acepta alguna cinta, si acepta una cantidad infinita y si dos autómatas son equivalentes; el
teorema 10 acota la longitud del contraejemplo por el producto de los números de estados);
y, sobre todo, en la teoría de la complejidad, donde la máquina de Turing no determinista define la clase
NP. De ahí la expresión «fuente continua de inspiración» de la mención.

## 4.3 Dos artículos localizados

Ambos tienen DOI, están publicados en foros con revisión por pares (ESEC/FSE 2018 y OOPSLA 2020, de la ACM) y
son distintos de los cinco de la Práctica 1. Los dos describen sistemas construidos y medidos.

### Ficha 1. Davis et al. (2018)

| Punto | Contenido |
|---|---|
| **Cita** | Davis, J. C., Coghlan, C. A., Servant, F., & Lee, D. (2018). The impact of regular expression denial of service (ReDoS) in practice: An empirical study at the ecosystem scale. En *Proceedings of the 2018 26th ACM Joint Meeting on European Software Engineering Conference and Symposium on the Foundations of Software Engineering* (pp. 246–256). ACM. https://doi.org/10.1145/3236024.3236027 |
| **Problema** | Los motores de expresiones regulares de JavaScript y Python resuelven la pertenencia con retroceso (*backtracking*) sobre un AFN: prueban los caminos uno por uno. Con ciertas expresiones (*super-linear*, SL) y entradas maliciosas el tiempo crece de forma polinomial o exponencial con la longitud de la cadena, lo que permite un ataque de denegación de servicio (ReDoS). No se sabía qué tan frecuente es el problema en el software real ni cómo lo corrigen los desarrolladores. |
| **Método** | Estudio empírico a escala de ecosistema: extrajeron las expresiones de las bibliotecas centrales de Node.js y Python y de 448 402 módulos de npm y pypi (más del 50 % de los registros), detectaron las SL con herramientas de análisis existentes, validaron cada una construyendo una entrada maliciosa y midiendo el tiempo de respuesta, evaluaron las heurísticas de «anti-patrones» y analizaron las correcciones de 284 módulos a cuyos mantenedores notificaron. |
| **Resultado principal** | Encontraron más de 4 000 expresiones SL únicas que afectan a más de 10 000 módulos, incluidas las bibliotecas centrales de Node.js y Python; cerca de 300 tienen complejidad exponencial. Las heurísticas de anti-patrones (cuantificadores anidados) tienen pocos falsos negativos pero muchos falsos positivos. Al corregir, los desarrolladores prefieren reescribir la expresión antes que truncar la entrada o usar otro analizador. |
| **Relación con el temario** | Es una consecuencia práctica de la diferencia entre **simular un AFN con todos los caminos a la vez** (conjunto de estados activos, lineal en la cadena) y **explorarlo camino por camino**. El artículo menciona como alternativa los motores lineales basados en el algoritmo de Thompson (1968), que es la simulación por conjuntos y la construcción ER → AFN-λ usadas en este repositorio. |
| **Aportación a mi trabajo** | Justifica la decisión de diseño del simulador (apartado 3.3): simular el no determinismo siguiendo todos los caminos como conjunto de estados, nunca por retroceso. También aporta un caso de estudio para la propuesta de trabajo: decidir con autómatas si una expresión puede tener comportamiento super-lineal. |

### Ficha 2. Turoňová et al. (2020)

| Punto | Contenido |
|---|---|
| **Cita** | Turoňová, L., Holík, L., Lengál, O., Saarikivi, O., Veanes, M., & Vojnar, T. (2020). Regex matching with counting-set automata. *Proceedings of the ACM on Programming Languages, 4*(OOPSLA), 1–30. https://doi.org/10.1145/3428286 |
| **Problema** | Las expresiones con repetición acotada, como `(ab){1,100}`, son comunes (filtros de red, esquemas XML), pero su AFD crece exponencialmente con la cota: para `.*a.{k}` el AFD mínimo necesita 2ᵏ⁺¹ estados porque debe recordar en qué posiciones de los últimos k + 1 símbolos apareció una a. Los motores con caché de estados (RE2, grep) también fallan en esos casos. |
| **Método** | Proponen los *counting-set automata* (CsA): autómatas deterministas con registros que guardan conjuntos de enteros acotados y que se actualizan con operaciones de tiempo constante. El algoritmo traduce la expresión a un autómata con contadores no determinista (al estilo de las derivadas de Antimirov, sin transiciones ε) y lo **determiniza con una construcción de subconjuntos generalizada** cuyo tamaño no depende de las cotas. Implementaron un comparador basado en CsA y lo midieron frente a grep, RE2, SRM y el motor de .NET. |
| **Resultado principal** | El método trata más del 90 % de las expresiones con conteo recolectadas; los CsA resultan mucho más pequeños y rápidos de construir que los AFD equivalentes. En la expresión `(_a){64999}_a`, los motores existentes exceden cualquier límite razonable; con la cota reducida a 1 000 tardan de 6 a 34 s sobre 500 KiB de texto, mientras que el CsA tarda alrededor de 1 s con la cota original. |
| **Relación con el temario** | Es la construcción de subconjuntos (Rabin y Scott, 1959) llevada a un modelo con memoria adicional, y ataca directamente la explosión 2ⁿ: su ejemplo `.*a.{k}` es la misma familia Lₙ («el n-ésimo símbolo desde el final») que se construyó y midió en el Ejercicio 2. |
| **Aportación a mi trabajo** | Confirma con datos externos el resultado de la tabla de la familia Lₙ y muestra una salida práctica a la cota 2ⁿ que no es «convertir todo»: agregar al estado del AFD una estructura que represente de forma compacta muchos subconjuntos. Es la base de la segunda línea de la propuesta de trabajo. |

## Uso de fuentes

Todas las afirmaciones de este documento se apoyan en los libros con ISBN, los artículos con DOI y la
documentación oficial listados en la [bibliografía](bibliografia.md). Los datos del artículo de Rabin y
Scott se tomaron del texto original (sección 5, definiciones 9-11 y teorema 11); los de las fichas, de los
resúmenes y las secciones de introducción y resultados de cada artículo.
