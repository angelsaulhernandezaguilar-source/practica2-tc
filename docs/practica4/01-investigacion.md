# Práctica 4 · Ejercicio 1. Investigación sobre expresiones regulares

[← Volver al índice](../../README.md)

Las referencias de libro son a Hopcroft, Motwani y Ullman (2007, tercera edición) y a Sipser (2013, tercera
edición), la bibliografía oficial usada desde la Práctica 2; las demás fuentes están en la
[bibliografía](../bibliografia.md). La notación es la del curso: `+` unión, yuxtaposición concatenación,
`*` cerradura de Kleene, `λ` palabra vacía y `∅` lenguaje vacío.

## 1. Lenguajes regulares, expresiones regulares y sus operaciones

**Operaciones sobre lenguajes.** Sean L y M lenguajes sobre un alfabeto Σ. Sipser (2013, definición 1.23)
define las tres *operaciones regulares*:

* **Unión:** L + M = {w : w ∈ L o w ∈ M}.
* **Concatenación:** LM = {xy : x ∈ L, y ∈ M}.
* **Cerradura de Kleene (estrella):** L* = {x₁x₂…xₖ : k ≥ 0, cada xᵢ ∈ L}; por convención λ ∈ L* siempre,
  porque k = 0 da la palabra vacía. Hopcroft et al. (2007, § 3.1.1) la escriben como L* = L⁰ ∪ L¹ ∪ L² ∪ …,
  con L⁰ = {λ}.

**Expresión regular.** Es un objeto sintáctico: una fórmula finita. Hopcroft et al. (2007, § 3.1.2) la definen
por inducción, junto con el lenguaje L(E) que denota:

| | Expresión E | Lenguaje L(E) |
|---|---|---|
| Base | `λ` | {λ} |
| Base | `∅` | ∅ (ninguna palabra) |
| Base | `a`, con a ∈ Σ | {a} |
| Inducción | `E + F` | L(E) ∪ L(F) |
| Inducción | `EF` | L(E)L(F) |
| Inducción | `E*` | (L(E))* |
| Inducción | `(E)` | L(E) |

No hay otras expresiones regulares. La precedencia (Hopcroft et al., 2007, § 3.1.3) es la misma que la del
enunciado: la cerradura liga más fuerte, después la concatenación y al final la unión; `0+10*` es
`0 + (1(0*))`. Sipser (2013, definición 1.52) da la misma definición con ∪ y ∘ en lugar de `+` y la
yuxtaposición. Es el analizador del Ejercicio 2 el que aplica exactamente esta gramática.

**Lenguaje regular.** Es un objeto semántico: un conjunto de palabras. Sipser (2013, definición 1.16) llama
regular a un lenguaje si algún autómata finito lo reconoce; Hopcroft et al. (2007, § 3.1) lo caracterizan
como un lenguaje denotado por alguna expresión regular. Las dos definiciones coinciden por el teorema de
Kleene (§ 3 de este documento). La relación entre expresión y lenguaje no es uno a uno: `(0+1)*1`,
`0*1(0*1)*` y `(0+11*0)*11*` son tres expresiones distintas del mismo lenguaje (las dos últimas salieron en el
problema 277 de la Lista 4, por el método Rᵢⱼ⁽ᵏ⁾ y por el lema de Arden). Además, la clase de los lenguajes
regulares es cerrada bajo las tres operaciones (Sipser, 2013, teoremas 1.25, 1.47 y 1.49), lo que es justo lo
que hace válida la definición inductiva de las expresiones.

## 2. Los lenguajes regulares en la jerarquía de Chomsky

Chomsky (1956, 1959) clasificó las gramáticas según la forma de sus producciones, y cada clase de gramáticas
genera una clase de lenguajes que coincide con la de alguna máquina abstracta:

| Tipo | Gramática | Lenguajes | Máquina | Ejemplo que la separa del tipo siguiente |
|---|---|---|---|---|
| 3 | Regular (lineal por la derecha: A → aB, A → a, A → λ) | Regulares | Autómata finito | — |
| 2 | Libre de contexto (A → α) | Libres de contexto | Autómata de pila | {aⁿbⁿ : n ≥ 0} es de tipo 2 y no de tipo 3 |
| 1 | Sensible al contexto (αAβ → αγβ, γ ≠ λ) | Sensibles al contexto | Autómata linealmente acotado | {aⁿbⁿcⁿ : n ≥ 0} es de tipo 1 y no de tipo 2 |
| 0 | Sin restricción (α → β) | Recursivamente enumerables | Máquina de Turing | El lenguaje de la máquina universal es de tipo 0 y no de tipo 1 |

Las inclusiones son estrictas: regulares ⊂ libres de contexto ⊂ sensibles al contexto ⊂ recursivamente
enumerables. Los lenguajes regulares son el nivel más bajo, el de **memoria finita**: un autómata finito solo
recuerda en qué estado está, por eso no puede contar sin cota (no reconoce aⁿbⁿ), lo que se demuestra con el
lema de bombeo (Hopcroft et al., 2007, § 4.1; Sipser, 2013, § 1.4). A cambio, todo problema sobre ellos es
decidible y eficiente: pertenencia en tiempo lineal con un AFD, vacuidad, finitud y equivalencia (Hopcroft
et al., 2007, § 4.3), y tienen tres descripciones intercambiables: autómatas, expresiones regulares y gramáticas
regulares (Hopcroft et al., 2007, § 5.1 y § 3.2; Sipser, 2013, § 1.3). Las gramáticas regulares equivalen a los
autómatas finitos: cada producción A → aB es una transición A -a→ B (Hopcroft et al., 2007, ejercicio 5.1.4;
Chomsky, 1959, teorema 7).

## 3. El teorema de Kleene

El resultado se debe a Kleene (1956), que demostró que los «eventos regulares» describibles con sus
expresiones son exactamente los que representa una red de neuronas finita (un autómata finito). En la
bibliografía oficial aparece dividido en las dos direcciones que implementa esta práctica:

**Parte I (de la expresión al autómata).** *Toda lengua definida por una expresión regular es también
definida por un autómata finito.* Hopcroft et al. (2007), **teorema 3.7**, § 3.2.3 (*Converting Regular
Expressions to Automata*): la demostración construye por inducción estructural un AFN-λ con un solo estado
inicial sin entradas y un solo estado final sin salidas para cada una de las formas base y para la unión, la
concatenación y la cerradura (figuras 3.16 y 3.17). Sipser (2013), **lema 1.55**: «si un lenguaje es descrito
por una expresión regular, entonces es regular», con la misma construcción (figuras 1.48 a 1.50 y ejemplo
1.56 con la expresión `(ab ∪ a)*`). Es la construcción del Ejercicio 2 y de la Lista 4, problemas 272 y 278.

**Parte II (del autómata a la expresión).** *Si L = L(A) para algún AFD A, entonces existe una expresión
regular R con L = L(R).* Hopcroft et al. (2007), **teorema 3.4**, § 3.2.1 (*From DFA's to Regular
Expressions*), demostrado con las expresiones Rᵢⱼ⁽ᵏ⁾ (los caminos de i a j que solo pasan por estados numerados
≤ k); la § 3.2.2 (*Converting DFA's to Regular Expressions by Eliminating States*) da el método de
eliminación de estados, que es el que implementa el Ejercicio 3 y el que usa JFLAP. Sipser (2013),
**lema 1.60**: «si un lenguaje es regular, entonces es descrito por una expresión regular», demostrado con
autómatas finitos no deterministas generalizados (GNFA), cuyas transiciones llevan expresiones regulares y
cuyos estados se eliminan uno por uno (procedimiento CONVERT, figura 1.63).

Las dos partes juntas son el **teorema 1.54** de Sipser (2013): *un lenguaje es regular si y solo si alguna
expresión regular lo describe*. Hopcroft et al. (2007) resumen la equivalencia en la figura 3.1: AFD, AFN,
AFN-λ y expresiones regulares definen la misma clase de lenguajes.

## 4. Leyes algebraicas usadas en la Práctica 3

Todas están en Hopcroft et al. (2007, § 3.4, *Algebraic Laws for Regular Expressions*). En la Práctica 3
sirvieron para simplificar las expresiones de JFLAP y para comprobar que la expresión larga del método
Rᵢⱼ⁽ᵏ⁾ era la misma que la corta de Arden ([Ejercicio 1 de la Práctica 3](../practica3/01-afd-a-er-jflap.md));
en esta práctica el software las aplica automáticamente al construir las etiquetas del autómata generalizado:

| Ley | Forma | Sección | Dónde se usó |
|---|---|---|---|
| Conmutatividad y asociatividad de la unión | r + s = s + r; (r + s) + t = r + (s + t) | 3.4.1 | 257: reordenar `01* + 1 + 01*0` |
| Identidades | ∅ + r = r; λr = rλ = r | 3.4.2 | 257: `01*λ = 01*`; eliminación de estados: las transiciones ∅ desaparecen |
| Aniquilador | ∅r = r∅ = ∅ | 3.4.2 | Eliminación de estados: un camino que pasa por una transición ∅ no aporta nada |
| Distributivas | r(s + t) = rs + rt; (s + t)r = sr + tr | 3.4.3 | 257: `01*λ + 01*0 = 01*(λ + 0)`; 130: `0(0+1) = 00 + 01` |
| Idempotencia | r + r = r | 3.4.4 | Rᵢⱼ⁽ᵏ⁾ del 130 |
| Cerraduras | (r*)* = r*; ∅* = λ; λ* = λ; (λ + r)* = r*; r* = λ + r*r = λ + rr* | 3.4.5 | 130 y 257 (Rᵢⱼ⁽ᵏ⁾: (λ + 0)* = 0*); eliminación de estados: un estado sin lazo tiene ∅* = λ |
| Desplazamiento | (rs)*r = r(sr)* | comprobada con el método de 3.4.7 | 258 y 257 (Rᵢⱼ⁽ᵏ⁾) |
| Unión bajo estrella | (r + s)* = (r*s)*r* | comprobada con el método de 3.4.7 | 138; Lista 4, 277 |

Las secciones 3.4.6 y 3.4.7 enseñan a **descubrir y comprobar** una ley: se sustituye cada variable por un
símbolo distinto y se comparan los dos lenguajes concretos (teorema 3.13). Es exactamente lo que hace la
pestaña 7 del software con *Comparar*: convierte las dos expresiones a AFD mínimos y decide si son
isomorfos.

## 5. Expresiones regulares de la teoría y de los lenguajes de programación

Las «regex» de Python (módulo `re`), Perl, Java o JavaScript nacen de las expresiones de Kleene, pero son
otra cosa en tres sentidos:

1. **Azúcar sintáctica que no cambia el poder expresivo.** Las clases `[a-z]` y `\d`, el punto `.`, los
   cuantificadores `?`, `+` y `{m,n}`, las anclas `^` y `$` y los grupos `(?:…)` se traducen a unión,
   concatenación y estrella: `r?` es `λ + r`, `r+` es `rr*`, `r{2,4}` es `rr(λ + r(λ + r))`. El Ejercicio 4 hace
   la traducción inversa: cada validador se escribe en la notación del curso y `a_python` lo convierte a `re`.
2. **Semántica de búsqueda, no de pertenencia.** `re.search` encuentra una subcadena que casa y devuelve dónde;
   la pregunta de la teoría es si *toda* la cadena pertenece a L(r), que en Python es `re.fullmatch`. Por eso las
   pruebas del Ejercicio 4 comparan el autómata con `fullmatch`.
3. **Extensiones que sí salen de los lenguajes regulares.** Las *referencias hacia atrás* `\1`, `\2`, … exigen
   que un trozo de la cadena se repita literalmente. Un motor como el de Python las resuelve por retroceso
   (*backtracking*), probando todas las maneras de partir la cadena, lo que puede costar tiempo exponencial;
   es la causa de los ataques de denegación de servicio por expresiones regulares (ReDoS) que Davis et al.
   (2018) midieron en más de 10 000 expresiones reales. Los motores basados en autómatas (grep, RE2) siguen el
   algoritmo de Thompson (1968) —construir el AFN y simularlo por conjuntos, como la pestaña 3— y por eso
   garantizan tiempo lineal, pero no pueden ofrecer referencias hacia atrás.

**Por qué `(a*)b\1` no es regular.** El patrón casa una cadena si y solo si tiene la forma `aⁿ b aⁿ`: el grupo
captura aⁿ y `\1` exige exactamente la misma cadena después de la b. Sea L = {aⁿbaⁿ : n ≥ 0} y supóngase
que es regular. Por el lema de bombeo (Hopcroft et al., 2007, teorema 4.1; Sipser, 2013, teorema 1.70) existe
una constante p ≥ 1 tal que toda w ∈ L con |w| ≥ p se descompone como w = xyz con |xy| ≤ p, |y| ≥ 1 y
xyⁱz ∈ L para todo i ≥ 0. Tómese w = aᵖbaᵖ ∈ L, que cumple |w| = 2p + 1 ≥ p. Como |xy| ≤ p, los
primeros p símbolos son todos a, así que x = aʲ, y = aᵏ con k ≥ 1 y j + k ≤ p, y z = aᵖ⁻ʲ⁻ᵏbaᵖ. Bombeando con
i = 2: xy²z = aʲa²ᵏaᵖ⁻ʲ⁻ᵏbaᵖ = aᵖ⁺ᵏbaᵖ. Como k ≥ 1, hay más a antes de la b que después, así que
xy²z ∉ L, contradiciendo el lema. Por lo tanto L no es regular, y ningún autómata finito ni expresión regular
de la teoría puede reconocer lo que ese patrón de Python reconoce. (Con i = 0 se obtiene aᵖ⁻ᵏbaᵖ ∉ L, que
también sirve.) El argumento es el mismo que el de {aⁿbⁿ} (Sipser, 2013, ejemplo 1.73): un autómata con un
número fijo de estados no puede recordar cuántas a leyó.

## 6. Cinco aplicaciones actuales

**a) Análisis léxico en compiladores.** El primer paso de un compilador parte el programa en *tokens*, y cada
token se especifica con una expresión regular (Aho, Lam, Sethi y Ullman, 2007, § 3.3); generadores como
`lex`/`flex` convierten las expresiones en un AFD que se ejecuta en tiempo lineal (§ 3.6 a 3.8, la misma
cadena ER → AFN-λ → AFD → mínimo de esta práctica). Identificador de C en la notación del curso, con
L = a+…+z+A+…+Z y D = 0+…+9:

```
(L + _)(L + D + _)*          en re:  [A-Za-z_][A-Za-z0-9_]*
```

El primer símbolo no puede ser un dígito (para no confundirlo con un número) y después se admite cualquier
mezcla. Un número real: `DD*(λ + .DD*)`, en `re` `[0-9]+(\.[0-9]+)?`. El analizador léxico aplica la regla de la
coincidencia más larga: ante `x1 = 3.14`, reconoce `x1`, `=`, `3.14`.

**b) Búsqueda de patrones en texto.** `grep` nació del algoritmo de Thompson (1968), y sus expresiones
extendidas están normalizadas por POSIX (IEEE, 2018, capítulo 9). Para encontrar en un registro las líneas de
error que mencionan un tiempo de espera agotado:

```
grep -E '^(ERROR|FATAL)\b.*\btimeout\b' servidor.log
```

`^` ancla al inicio de la línea, `(ERROR|FATAL)` es la unión, `\b` exige frontera de palabra (para no casar
`ERRORES`), `.*` es `Σ*` y la palabra `timeout` debe aparecer completa. grep prueba el patrón sobre cada línea
y conserva las que casan; con `-c` cuenta, con `-v` invierte.

**c) Validación de datos.** Formularios y API comprueban el formato de un campo antes de procesarlo. El
validador de correo del Ejercicio 4, aproximación al `addr-spec` del RFC 5322 (Resnick, 2008), con
A = letras, dígitos, `_`, `-`, `+` y X = letras y dígitos:

```
AA*(.AA*)*@(X(X+-)*X+X)(.(X(X+-)*X+X))*.YYY*
```

La parte local son átomos separados por puntos (sin puntos seguidos ni en los extremos), el dominio son
etiquetas alfanuméricas que no empiezan ni terminan con guion (RFC 1035) y el dominio superior tiene al menos
dos letras. El [Ejercicio 4](04-validadores.md) detalla qué deja fuera: una expresión para correos siempre es
una aproximación al estándar.

**d) Filtrado de registros.** Las herramientas de monitoreo y los filtros de intrusos leen bitácoras línea por
línea y las clasifican con expresiones. Para extraer de un registro de acceso en formato común de Apache las
peticiones que terminaron en error del servidor (código 5xx) y quedarse con la dirección y el recurso:

```
^(\d{1,3}(\.\d{1,3}){3}) \S+ \S+ \[[^\]]+\] "(GET|POST) (\S+) [^"]*" 5\d\d
```

El primer grupo captura la dirección IPv4 (cuatro grupos de uno a tres dígitos separados por punto), los
campos de identidad y usuario son `\S+`, la fecha va entre corchetes, la petición entre comillas con el
método y el recurso capturados, y el estado debe empezar con 5. Con `re.finditer` sobre el archivo se obtienen
los pares (dirección, recurso) para agruparlos. Es un uso de búsqueda con grupos de captura, no de pertenencia.

**e) Automatización en sistemas operativos.** Los intérpretes de órdenes usan expresiones para renombrar,
filtrar y transformar en lote. En PowerShell (Microsoft, 2024), para mover los informes mensuales cuyo nombre
sigue el patrón `informe-AAAA-MM.pdf` a una carpeta por año:

```powershell
Get-ChildItem *.pdf | Where-Object { $_.Name -match '^informe-(\d{4})-(0[1-9]|1[0-2])\.pdf$' } |
    ForEach-Object { Move-Item $_ (Join-Path $Matches[1] $_.Name) }
```

`-match` aplica la expresión al nombre y deja los grupos en `$Matches`; `(\d{4})` captura el año y
`(0[1-9]|1[0-2])` restringe el mes a 01-12 (la misma subexpresión `0P + 1(0+1+2)` del validador de fechas).
En Unix, `sed -E 's/^informe-([0-9]{4})-.*/\1/'` hace la extracción equivalente, también normalizada por POSIX.

En las cinco aplicaciones el patrón es el mismo: una expresión corta describe un conjunto infinito de cadenas,
y una máquina (AFD, AFN simulado o motor con retroceso) decide la pertenencia o localiza las coincidencias.
La diferencia práctica está en qué motor se usa: los basados en autómatas garantizan tiempo lineal (a y b);
los basados en retroceso ofrecen capturas y referencias hacia atrás (c, d y e) a costa de poder ser lentos
con patrones mal diseñados.
