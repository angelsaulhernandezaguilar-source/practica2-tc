# Ejercicio 2. AFND y AFND-λ en JFLAP

[← Volver al índice](../README.md)

Este documento resume el ejercicio. El detalle de cada autómata (diseño, tabla, diez cadenas con su recorrido, λ-clausuras, captura de JFLAP y conversión) está en seis documentos, uno por sección:

| Documento | Contenido |
|---|---|
| [AFD — Lista 2](jflap/afd-lista2.md) | Problemas 94-150 |
| [AFD — Lista 3](jflap/afd-lista3.md) | Problemas 151-157 y 254-259 |
| [AFND estándar](jflap/afnd.md) | 143(b), 158-161, 162-188, 189-195 y 260-263 |
| [AFND-λ, parte 1](jflap/afnd-lambda-1.md) | 162-188 resueltos con λ, y 196-200 |
| [AFND-λ, parte 2](jflap/afnd-lambda-2.md) | 201-235 (verdadero o falso) y 236-240 |
| [AFND-λ, parte 3](jflap/afnd-lambda-3.md) | 241-253 (de expresión regular a AFND-λ) |

## Cómo se construyó y se verificó

- **166 ejercicios** (todos los números del 94 al 263; los de verdadero o falso que comparten expresión se agrupan) y **190 autómatas**, cada uno en `.jff`, `.json` y `.xml` dentro de `automatas/`. Los 101 archivos `.jff` de la Práctica 1 se copiaron sin cambios con `herramientas/importar_p1.py`; los nuevos los escribe `herramientas/generar.py` con `src/formatos.py`.
- **Oráculo independiente.** Cada autómata se comparó con una definición del lenguaje escrita a partir del enunciado (`herramientas/catalogo.py`), sobre todas las cadenas cortas y cientos de cadenas al azar. Las pruebas `tests/test_catalogo.py` repiten esa comparación en cada ejecución de pytest.
- **JFLAP.** Las 1831 cadenas de prueba se corrieron en el motor de simulación de JFLAP 7.1 (`herramientas/JflapLote.java`); JFLAP coincidió con el resultado esperado en todas. Los resultados están en [`evidencias/jflap/resultados-jflap.tsv`](../evidencias/jflap/resultados-jflap.tsv).
- **Paso a paso.** Para cada autómata se ejecutó *Input → Step with Closure* en la ventana de JFLAP y se guardó cada paso (`herramientas/JflapPasos.java`); las capturas están en [`evidencias/jflap/pasos/`](../evidencias/jflap/pasos/) y se enlazan desde cada autómata.
- **Conversiones.** Los AFND se convirtieron con *Convert → Convert to DFA* de JFLAP (la clase `NFAToDFA`, `herramientas/JflapConvertir.java`). Los AFND-λ se convirtieron primero a AFND estándar con `Automata.sin_lambda()` y después a AFD con JFLAP. Todos los resultados están en [`automatas/conversiones/`](../automatas/conversiones/) y se verificó que cada uno acepta el mismo lenguaje que el autómata original.

Convención: Σ₁ = {0, 1, 2}, Σ₂ = {a, b, c, 0, 1}, Σ₃ = {a, b}; λ es la cadena vacía. Siguiendo la definición del curso, un **AFD** tiene δ total (δ: Q × Σ → Q). Un autómata determinista con alguna celda vacía es, formalmente, un AFND con δ(q, a) = ∅; JFLAP lo llamaría DFA.

## 2.1 Clasificación y cobertura

| Sección | Carpeta | Ejercicios |
|---|---|---|
| AFD | [`automatas/lista2-afd/`](../automatas/lista2-afd/) | 69 |
| AFND | [`automatas/lista3-afnd/`](../automatas/lista3-afnd/) | 43 |
| AFND-λ | [`automatas/lista3-afnd-lambda/`](../automatas/lista3-afnd-lambda/) | 52 |
| Ninguna | — | 2 |

Las carpetas llevan el nombre que sugiere el enunciado, pero cada una es una **sección por tipo de autómata**: `lista2-afd/` contiene todos los AFD (los de la Lista 2 y los AFD dados por tabla en la Lista 3, como 151-157 y 254-259), `lista3-afnd/` los AFND estándar (incluido el 143(b) de la Lista 2) y `lista3-afnd-lambda/` los AFND-λ. El prefijo del archivo (`L2-` o `L3-`) indica la lista.

El criterio de clasificación es la forma del autómata que resuelve el ejercicio: **AFD** si el enunciado pide o da un autómata con δ total y un solo estado activo; **AFND** si hay celdas con varios destinos o con ∅ y no hay λ; **AFND-λ** si la solución usa transiciones que no consumen símbolos. Los ejercicios de expresiones regulares (201-253) caen en AFND-λ porque la manera de simular una expresión es su autómata de Thompson. El problema 116 no cabe en ninguna: su lenguaje no es regular.

| Lista | Problema | Sección | Justificación (una línea) |
|---|---|---|---|
| 2 | [94](jflap/afd-lista2.md#problema-2-94) | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Basta recordar si el primer símbolo fue 1 y si el último es 2. |
| 2 | [95](jflap/afd-lista2.md#problema-2-95) | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Solo se cuenta la longitud hasta 5. |
| 2 | [96](jflap/afd-lista2.md#problema-2-96) | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Combina la verificación del prefijo con un contador de longitud. |
| 2 | [97](jflap/afd-lista2.md#problema-2-97) ★ | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Contador módulo 3 de la longitud. |
| 2 | [98](jflap/afd-lista2.md#problema-2-98) | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Búsqueda de sufijo con función de fallo. |
| 2 | [99](jflap/afd-lista2.md#problema-2-99) ★ | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Búsqueda de sufijo con función de fallo. |
| 2 | [100](jflap/afd-lista2.md#problema-2-100) | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Solo se revisan las dos primeras posiciones. |
| 2 | [101](jflap/afd-lista2.md#problema-2-101) | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Búsqueda de subcadena con estado final absorbente. |
| 2 | [102](jflap/afd-lista2.md#problema-2-102) ★ | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Búsqueda de subcadena. |
| 2 | [103](jflap/afd-lista2.md#problema-2-103) ★ | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Búsqueda de subcadena. |
| 2 | [104](jflap/afd-lista2.md#problema-2-104) | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Verificación de prefijo. |
| 2 | [105](jflap/afd-lista2.md#problema-2-105) | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Búsqueda de sufijo con función de fallo. |
| 2 | [106](jflap/afd-lista2.md#problema-2-106) ★ | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Búsqueda de subcadena. |
| 2 | [107](jflap/afd-lista2.md#problema-2-107) ★ | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Producto de dos búsquedas. |
| 2 | [108](jflap/afd-lista2.md#problema-2-108) | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Producto de búsquedas que exige ocurrencias disjuntas. |
| 2 | [109](jflap/afd-lista2.md#problema-2-109) ★ | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Producto de búsquedas con traslape. |
| 2 | [110](jflap/afd-lista2.md#problema-2-110) | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Contador saturado de ocurrencias de 01. |
| 2 | [111](jflap/afd-lista2.md#problema-2-111) ★ | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Contador de ocurrencias. |
| 2 | [112](jflap/afd-lista2.md#problema-2-112) ★ | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Contador sin traslape. |
| 2 | [113](jflap/afd-lista2.md#problema-2-113) ★ | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Contador con traslape. |
| 2 | [114](jflap/afd-lista2.md#problema-2-114) | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Dos fases consecutivas: primero a, después b. |
| 2 | [115](jflap/afd-lista2.md#problema-2-115) | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Ciclo de longitud 3 que reconoce abc. |
| 2 | [116](jflap/afd-lista2.md#problema-2-116) | Ninguna | Ningún autómata finito lo reconoce: L no es regular (lema de bombeo), así que no cabe en ninguna de las tres secciones. |
| 2 | [117](jflap/afd-lista2.md#problema-2-117) | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Cuatro fases consecutivas a, b, a, b. |
| 2 | [118](jflap/afd-lista2.md#problema-2-118) ★ | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. |
| 2 | [119](jflap/afd-lista2.md#problema-2-119) | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Se recuerda la racha final de a (0, 1 o 2). |
| 2 | [120](jflap/afd-lista2.md#problema-2-120) ★ | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. |
| 2 | [121](jflap/afd-lista2.md#problema-2-121) ★ | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. |
| 2 | [122](jflap/afd-lista2.md#problema-2-122) ★ | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. |
| 2 | [123](jflap/afd-lista2.md#problema-2-123) ★ | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. |
| 2 | [124](jflap/afd-lista2.md#problema-2-124) ★ | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. |
| 2 | [125](jflap/afd-lista2.md#problema-2-125) | AFD | Pregunta sobre un AFD (δ total); se ilustra con el AFD del 139 y su complemento. |
| 2 | [126](jflap/afd-lista2.md#problema-2-126) | AFD | Pregunta sobre un AFD; con F = ∅ ninguna palabra llega a un estado de aceptación. |
| 2 | [127](jflap/afd-lista2.md#problema-2-127) | AFD | Pregunta sobre un AFD; con F = Q y δ total toda palabra termina en un estado de aceptación. |
| 2 | [128](jflap/afd-lista2.md#problema-2-128) ★ | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Se cambia F de un AFD dado. |
| 2 | [129](jflap/afd-lista2.md#problema-2-129) | AFD | El enunciado da el AFD completo (δ total, un destino por par); solo se transcribe y se verifica. |
| 2 | [130](jflap/afd-lista2.md#problema-2-130) | AFD | El enunciado da el AFD completo; se transcribe y se corrige la descripción de su lenguaje. |
| 2 | [131](jflap/afd-lista2.md#problema-2-131) ★ | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. |
| 2 | [132](jflap/afd-lista2.md#problema-2-132) | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Un bloque de a y una sola b final. |
| 2 | [133](jflap/afd-lista2.md#problema-2-133) ★ | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. |
| 2 | [134](jflap/afd-lista2.md#problema-2-134) | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Búsqueda de subcadena (aplicación a búsqueda de texto). |
| 2 | [135](jflap/afd-lista2.md#problema-2-135) ★ | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. |
| 2 | [136](jflap/afd-lista2.md#problema-2-136) | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Dos fases, cada una con al menos un símbolo. |
| 2 | [137](jflap/afd-lista2.md#problema-2-137) ★ | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. |
| 2 | [138](jflap/afd-lista2.md#problema-2-138) | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Contador módulo 3 de las b. |
| 2 | [139](jflap/afd-lista2.md#problema-2-139) ★ | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. |
| 2 | [140](jflap/afd-lista2.md#problema-2-140) | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Contadores de paridad (uno para a; un par para b). |
| 2 | [141](jflap/afd-lista2.md#problema-2-141) ★ | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. |
| 2 | [142](jflap/afd-lista2.md#problema-2-142) | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Ciclo de longitud 2 que reconoce ab. |
| 2 | [143](jflap/afd-lista2.md#problema-2-143) ★ | AFD | La figura (a) es un AFD; la (b) es un AFND (dos destinos con b en q1) y se clasifica en esa sección. |
| 2 | [143b](jflap/afnd.md#problema-2-143b) ★ | AFND | La figura (b) tiene dos transiciones con b desde q1 y ninguna con b desde q0: es no determinista. |
| 2 | [144](jflap/afd-lista2.md#problema-2-144) | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. Cinco lenguajes de prefijo, sufijo, subcadena y formato numérico. |
| 2 | [145](jflap/afd-lista2.md#problema-2-145) ★ | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. |
| 2 | [146](jflap/afd-lista2.md#problema-2-146) | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. El estado guarda el residuo módulo 5 del valor leído. |
| 2 | [147](jflap/afd-lista2.md#problema-2-147) ★ | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. |
| 2 | [148](jflap/afd-lista2.md#problema-2-148) ★ | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. |
| 2 | [149](jflap/afd-lista2.md#problema-2-149) ★ | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. |
| 2 | [150](jflap/afd-lista2.md#problema-2-150) ★ | AFD | El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ. |
| 3 | [151](jflap/afd-lista3.md#problema-3-151) ★ | AFD | AFD dado por tabla (δ total) que se simplifica; la sección AFD es la que corresponde. |
| 3 | [152](jflap/afd-lista3.md#problema-3-152) ★ | AFD | AFD dado por tabla (δ total) que se simplifica; la sección AFD es la que corresponde. |
| 3 | [153](jflap/afd-lista3.md#problema-3-153) ★ | AFD | AFD dado por tabla (δ total) que se simplifica; la sección AFD es la que corresponde. |
| 3 | [154](jflap/afd-lista3.md#problema-3-154) ★ | AFD | AFD dado por tabla (δ total) que se simplifica; la sección AFD es la que corresponde. |
| 3 | [155](jflap/afd-lista3.md#problema-3-155) ★ | AFD | AFD dado por tabla (δ total) que se simplifica; la sección AFD es la que corresponde. |
| 3 | [156](jflap/afd-lista3.md#problema-3-156) ★ | AFD | AFD dado por tabla (δ total) que se simplifica; la sección AFD es la que corresponde. |
| 3 | [157](jflap/afd-lista3.md#problema-3-157) ★ | AFD | AFD dado por tabla (δ total) que se simplifica; la sección AFD es la que corresponde. |
| 3 | [158](jflap/afnd.md#problema-3-158) ★ | AFND | Los diagramas dejan transiciones indefinidas (δ(q, a) = ∅); la lista los presenta como AFN. |
| 3 | [159](jflap/afnd.md#problema-3-159) ★ | AFND | Los diagramas dejan transiciones indefinidas (δ(q, a) = ∅); la lista los presenta como AFN. |
| 3 | [160](jflap/afnd.md#problema-3-160) ★ | AFND | Los diagramas dejan transiciones indefinidas (δ(q, a) = ∅); la lista los presenta como AFN. |
| 3 | [161](jflap/afnd.md#problema-3-161) ★ | AFND | Los diagramas dejan transiciones indefinidas (δ(q, a) = ∅); la lista los presenta como AFN. |
| 3 | [162-188 (p. 100)](jflap/afnd.md#problema-3-162-188-p-100) | AFND | El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. |
| 3 | [162-188 (p. 101)](jflap/afnd.md#problema-3-162-188-p-101) | AFND | El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. |
| 3 | [162-188 (p. 102)](jflap/afnd.md#problema-3-162-188-p-102) ★ | AFND | El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. |
| 3 | [162-188 (p. 103)](jflap/afnd.md#problema-3-162-188-p-103) ★ | AFND | El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. |
| 3 | [162-188 (p. 104)](jflap/afnd.md#problema-3-162-188-p-104) | AFND | El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. |
| 3 | [162-188 (p. 105)](jflap/afnd.md#problema-3-162-188-p-105) | AFND | El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. |
| 3 | [162-188 (p. 106)](jflap/afnd.md#problema-3-162-188-p-106) ★ | AFND | El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. |
| 3 | [162-188 (p. 107)](jflap/afnd.md#problema-3-162-188-p-107) ★ | AFND | El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. |
| 3 | [162-188 (p. 108)](jflap/afnd-lambda-1.md#problema-3-162-188-p-108) | AFND-λ | Se resolvió con transiciones λ: componen el autómata a partir de piezas (unión o concatenación) sin consumir símbolos. |
| 3 | [162-188 (p. 109)](jflap/afnd.md#problema-3-162-188-p-109) ★ | AFND | El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. |
| 3 | [162-188 (p. 110)](jflap/afnd.md#problema-3-162-188-p-110) | AFND | El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. |
| 3 | [162-188 (p. 111)](jflap/afnd.md#problema-3-162-188-p-111) ★ | AFND | El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. |
| 3 | [162-188 (p. 112)](jflap/afnd.md#problema-3-162-188-p-112) ★ | AFND | El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. |
| 3 | [162-188 (p. 113)](jflap/afnd.md#problema-3-162-188-p-113) ★ | AFND | El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. |
| 3 | [162-188 (p. 114)](jflap/afnd.md#problema-3-162-188-p-114) | AFND | El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. |
| 3 | [162-188 (p. 115)](jflap/afnd.md#problema-3-162-188-p-115) | AFND | El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. |
| 3 | [162-188 (p. 116)](jflap/afnd.md#problema-3-162-188-p-116) | Ninguna | El lenguaje del 116 no es regular: tampoco existe un AFN (ver el problema 116). |
| 3 | [162-188 (p. 117)](jflap/afnd-lambda-1.md#problema-3-162-188-p-117) | AFND-λ | Se resolvió con transiciones λ: componen el autómata a partir de piezas (unión o concatenación) sin consumir símbolos. |
| 3 | [162-188 (p. 118)](jflap/afnd.md#problema-3-162-188-p-118) ★ | AFND | El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. |
| 3 | [162-188 (p. 119)](jflap/afnd.md#problema-3-162-188-p-119) | AFND | El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. |
| 3 | [162-188 (p. 120)](jflap/afnd.md#problema-3-162-188-p-120) ★ | AFND | El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. |
| 3 | [162-188 (p. 121)](jflap/afnd.md#problema-3-162-188-p-121) ★ | AFND | El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. |
| 3 | [162-188 (p. 122)](jflap/afnd.md#problema-3-162-188-p-122) ★ | AFND | El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. |
| 3 | [162-188 (p. 123)](jflap/afnd.md#problema-3-162-188-p-123) ★ | AFND | El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. |
| 3 | [162-188 (p. 94)](jflap/afnd.md#problema-3-162-188-p-94) | AFND | El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. |
| 3 | [162-188 (p. 95)](jflap/afnd.md#problema-3-162-188-p-95) | AFND | El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. |
| 3 | [162-188 (p. 96)](jflap/afnd.md#problema-3-162-188-p-96) | AFND | El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. |
| 3 | [162-188 (p. 97)](jflap/afnd.md#problema-3-162-188-p-97) ★ | AFND | El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. |
| 3 | [162-188 (p. 98)](jflap/afnd.md#problema-3-162-188-p-98) | AFND | El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. |
| 3 | [162-188 (p. 99)](jflap/afnd.md#problema-3-162-188-p-99) ★ | AFND | El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD. |
| 3 | [189](jflap/afnd.md#problema-3-189) ★ | AFND | Se pide un AFN: un lazo inicial adivina dónde empieza cada patrón. |
| 3 | [190](jflap/afnd.md#problema-3-190) ★ | AFND | Se pide un AFN: un lazo inicial adivina dónde empieza cada patrón. |
| 3 | [191](jflap/afnd.md#problema-3-191) | AFND | Es el planteamiento común de los problemas 192-194: dado un AFN, hallar el AFD por subconjuntos. |
| 3 | [192](jflap/afnd.md#problema-3-192) ★ | AFND | El autómata dado tiene celdas con dos o más estados y celdas ∅: es un AFN; el AFD es su conversión. |
| 3 | [193](jflap/afnd.md#problema-3-193) ★ | AFND | El autómata dado tiene celdas con dos o más estados y celdas ∅: es un AFN; el AFD es su conversión. |
| 3 | [194](jflap/afnd.md#problema-3-194) ★ | AFND | El autómata dado tiene celdas con dos o más estados y celdas ∅: es un AFN; el AFD es su conversión. |
| 3 | [195](jflap/afnd.md#problema-3-195) ★ | AFND | El autómata dado tiene celdas con dos o más estados y celdas ∅: es un AFN; el AFD es su conversión. |
| 3 | [196](jflap/afnd-lambda-1.md#problema-3-196) | AFND-λ | La tabla tiene una columna λ con entradas no vacías: es un AFND con transiciones λ. |
| 3 | [197](jflap/afnd-lambda-1.md#problema-3-197) | AFND-λ | La tabla tiene una columna λ con entradas no vacías: es un AFND con transiciones λ. |
| 3 | [198](jflap/afnd-lambda-1.md#problema-3-198) | AFND-λ | La tabla tiene una columna λ con entradas no vacías: es un AFND con transiciones λ. |
| 3 | [199](jflap/afnd-lambda-1.md#problema-3-199) | AFND-λ | La tabla tiene una columna λ con entradas no vacías: es un AFND con transiciones λ. |
| 3 | [200](jflap/afnd-lambda-1.md#problema-3-200) | AFND-λ | La tabla tiene una columna λ con entradas no vacías: es un AFND con transiciones λ. |
| 3 | [201, 206, 221](jflap/afnd-lambda-2.md#problema-3-201-206-221) ★ | AFND-λ | Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. |
| 3 | [202, 207](jflap/afnd-lambda-2.md#problema-3-202-207) ★ | AFND-λ | Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. |
| 3 | [203, 222](jflap/afnd-lambda-2.md#problema-3-203-222) ★ | AFND-λ | Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. |
| 3 | [204, 233](jflap/afnd-lambda-2.md#problema-3-204-233) ★ | AFND-λ | Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. |
| 3 | [205](jflap/afnd-lambda-2.md#problema-3-205) ★ | AFND-λ | Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. |
| 3 | [208](jflap/afnd-lambda-2.md#problema-3-208) ★ | AFND-λ | Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. |
| 3 | [209](jflap/afnd-lambda-2.md#problema-3-209) ★ | AFND-λ | Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. |
| 3 | [210, 224, 227](jflap/afnd-lambda-2.md#problema-3-210-224-227) ★ | AFND-λ | Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. |
| 3 | [211](jflap/afnd-lambda-2.md#problema-3-211) ★ | AFND-λ | Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. |
| 3 | [212](jflap/afnd-lambda-2.md#problema-3-212) ★ | AFND-λ | Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. |
| 3 | [213](jflap/afnd-lambda-2.md#problema-3-213) ★ | AFND-λ | Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. |
| 3 | [214](jflap/afnd-lambda-2.md#problema-3-214) ★ | AFND-λ | Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. |
| 3 | [215](jflap/afnd-lambda-2.md#problema-3-215) ★ | AFND-λ | Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. |
| 3 | [216](jflap/afnd-lambda-2.md#problema-3-216) ★ | AFND-λ | Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. |
| 3 | [217](jflap/afnd-lambda-2.md#problema-3-217) ★ | AFND-λ | Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. |
| 3 | [218](jflap/afnd-lambda-2.md#problema-3-218) ★ | AFND-λ | Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. |
| 3 | [219](jflap/afnd-lambda-2.md#problema-3-219) ★ | AFND-λ | Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. |
| 3 | [220](jflap/afnd-lambda-2.md#problema-3-220) ★ | AFND-λ | Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. |
| 3 | [223](jflap/afnd-lambda-2.md#problema-3-223) ★ | AFND-λ | Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. |
| 3 | [225](jflap/afnd-lambda-2.md#problema-3-225) ★ | AFND-λ | Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. |
| 3 | [226](jflap/afnd-lambda-2.md#problema-3-226) ★ | AFND-λ | Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. |
| 3 | [228](jflap/afnd-lambda-2.md#problema-3-228) ★ | AFND-λ | Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. |
| 3 | [229, 235](jflap/afnd-lambda-2.md#problema-3-229-235) | AFND-λ | Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. |
| 3 | [230](jflap/afnd-lambda-2.md#problema-3-230) ★ | AFND-λ | Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. |
| 3 | [231](jflap/afnd-lambda-2.md#problema-3-231) ★ | AFND-λ | Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. |
| 3 | [232](jflap/afnd-lambda-2.md#problema-3-232) ★ | AFND-λ | Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. |
| 3 | [234](jflap/afnd-lambda-2.md#problema-3-234) ★ | AFND-λ | Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena. |
| 3 | [236](jflap/afnd-lambda-2.md#problema-3-236) ★ | AFND-λ | La respuesta es una expresión regular; su AFND-λ de Thompson es la forma de simularla. |
| 3 | [237](jflap/afnd-lambda-2.md#problema-3-237) ★ | AFND-λ | La respuesta es una expresión regular; su AFND-λ de Thompson es la forma de simularla. |
| 3 | [238](jflap/afnd-lambda-2.md#problema-3-238) ★ | AFND-λ | La respuesta es una expresión regular; su AFND-λ de Thompson es la forma de simularla. |
| 3 | [239](jflap/afnd-lambda-2.md#problema-3-239) ★ | AFND-λ | La respuesta es una expresión regular; su AFND-λ de Thompson es la forma de simularla. |
| 3 | [240](jflap/afnd-lambda-2.md#problema-3-240) ★ | AFND-λ | La respuesta es una expresión regular; su AFND-λ de Thompson es la forma de simularla. |
| 3 | [241](jflap/afnd-lambda-3.md#problema-3-241) | AFND-λ | Se pide explícitamente un AFND-λ equivalente a la expresión regular. |
| 3 | [242](jflap/afnd-lambda-3.md#problema-3-242) | AFND-λ | Se pide explícitamente un AFND-λ equivalente a la expresión regular. |
| 3 | [243](jflap/afnd-lambda-3.md#problema-3-243) | AFND-λ | Se pide explícitamente un AFND-λ equivalente a la expresión regular. |
| 3 | [244](jflap/afnd-lambda-3.md#problema-3-244) | AFND-λ | Se pide explícitamente un AFND-λ equivalente a la expresión regular. |
| 3 | [245](jflap/afnd-lambda-3.md#problema-3-245) | AFND-λ | Se pide explícitamente un AFND-λ equivalente a la expresión regular. |
| 3 | [246](jflap/afnd-lambda-3.md#problema-3-246) | AFND-λ | Se pide explícitamente un AFND-λ equivalente a la expresión regular. |
| 3 | [247](jflap/afnd-lambda-3.md#problema-3-247) | AFND-λ | Se pide explícitamente un AFND-λ equivalente a la expresión regular. |
| 3 | [248](jflap/afnd-lambda-3.md#problema-3-248) | AFND-λ | Se pide explícitamente un AFND-λ equivalente a la expresión regular. |
| 3 | [249](jflap/afnd-lambda-3.md#problema-3-249) | AFND-λ | Se pide explícitamente un AFND-λ equivalente a la expresión regular. |
| 3 | [250](jflap/afnd-lambda-3.md#problema-3-250) | AFND-λ | Se pide explícitamente un AFND-λ equivalente a la expresión regular. |
| 3 | [251](jflap/afnd-lambda-3.md#problema-3-251) | AFND-λ | Se pide explícitamente un AFND-λ equivalente a la expresión regular. |
| 3 | [252](jflap/afnd-lambda-3.md#problema-3-252) | AFND-λ | Se pide explícitamente un AFND-λ equivalente a la expresión regular. |
| 3 | [253](jflap/afnd-lambda-3.md#problema-3-253) | AFND-λ | Se pide explícitamente un AFND-λ equivalente a la expresión regular. |
| 3 | [254](jflap/afd-lista3.md#problema-3-254) ★ | AFD | El autómata dado es un AFD (δ total); la expresión se obtiene con el lema de Arden. |
| 3 | [255](jflap/afd-lista3.md#problema-3-255) ★ | AFD | El autómata dado es un AFD (δ total); la expresión se obtiene con el lema de Arden. |
| 3 | [256](jflap/afd-lista3.md#problema-3-256) ★ | AFD | El autómata dado es un AFD (δ total); la expresión se obtiene con el lema de Arden. |
| 3 | [257](jflap/afd-lista3.md#problema-3-257) ★ | AFD | El autómata dado es un AFD (δ total); la expresión se obtiene con el lema de Arden. |
| 3 | [258](jflap/afd-lista3.md#problema-3-258) ★ | AFD | El autómata dado es un AFD (δ total); la expresión se obtiene con el lema de Arden. |
| 3 | [259](jflap/afd-lista3.md#problema-3-259) | AFD | El autómata dado es un AFD (δ total); se aplica el algoritmo Rᵢⱼ⁽ᵏ⁾ de Kleene. |
| 3 | [260](jflap/afnd.md#problema-3-260) ★ | AFND | El autómata de partida es un AFN (varios destinos por símbolo); el AFD es su conversión. |
| 3 | [261](jflap/afnd.md#problema-3-261) ★ | AFND | El autómata de partida es un AFN (varios destinos por símbolo); el AFD es su conversión. |
| 3 | [262](jflap/afnd.md#problema-3-262) ★ | AFND | El autómata de partida es un AFN (varios destinos por símbolo); el AFD es su conversión. |
| 3 | [263](jflap/afnd.md#problema-3-263) ★ | AFND | El autómata de partida es un AFN (varios destinos por símbolo); el AFD es su conversión. |

★ = entregado en la Práctica 1 (se conservan sus `.jff`; aquí se agregan `.json`, `.xml`, pruebas y recorridos).

## 2.2 Diseño y validación

En cada documento de sección, cada autómata trae:

1. **Diseño y justificación**: qué recuerda cada estado (columna *Significado* de la tabla en los autómatas nuevos) y por qué la construcción reconoce exactamente el lenguaje.
2. **Cinco cadenas válidas y cinco inválidas** de longitudes crecientes: la más corta, y otras obtenidas caminando al azar por el AFD mínimo sin salir de los estados desde los que aún se puede aceptar (o rechazar). Para cada una se muestra lo esperado según el oráculo, lo que da el simulador y lo que da JFLAP.
3. **Recorrido completo**: en un AFD, la sucesión de estados; en un AFND o AFND-λ, el conjunto de estados activos tras cada símbolo y el **árbol de cómputo** con cada camino: los que aceptan, los que mueren porque no hay transición y los que terminan fuera de F. Ahí se ven las bifurcaciones.
4. **Captura de JFLAP** con la simulación paso a paso de una de las cadenas.

Cuando no existen cinco cadenas de un tipo, se indica: por ejemplo, L(126) = ∅ no tiene ninguna válida, {ab, ba} (262) tiene dos, y L(127) = Σ* solo tiene inválidas con símbolos fuera de Σ.

## 2.3 Transiciones λ

Una transición λ cambia de estado sin consumir símbolos. En los autómatas de esta práctica aparecen por tres motivos: (1) **unión**: desde un estado se elige, sin leer nada, cuál de varias alternativas seguir (108, uniones de Thompson); (2) **concatenación**: al terminar un bloque se pasa al siguiente (117, concatenaciones de Thompson); (3) **repetición**: en una estrella, regresar al inicio del bloque o saltarlo (Thompson). En los problemas 196-200 las λ vienen dadas en la tabla.

La **λ-clausura** Cl(q) es el conjunto de estados alcanzables desde q con cero o más transiciones λ; se calcula con un recorrido en profundidad que agrega cada estado nuevo alcanzado por λ hasta que no hay cambios (`Automata.clausura`). Su papel en el reconocimiento es doble: el cómputo empieza en Cl(q₀) y no en {q₀}, y después de leer cada símbolo el conjunto alcanzado se vuelve a cerrar: δ̂(S, wa) = Cl(⋃_{q ∈ δ̂(S, w)} δ(q, a)). Una cadena se acepta si el conjunto final contiene un estado de F, aunque solo se llegue a él por λ.

Ejemplo, problema 196 (tabla completa en [AFND-λ, parte 1](jflap/afnd-lambda-1.md)):

| q | Cl(q) |
|---|---|
| A | {A, B} |
| B | {B} |
| C | {C} |

δ̂(A, 110): {A, B} (Cl(A)) → {C} (lee 1) → ∅ (lee 1) → ∅ (lee 0). Sin la clausura inicial, el 1 no tendría transición desde A (δ(A, 1) = ∅) y la cadena moriría; con ella, B ∈ Cl(A) lee el 1 hacia C.

Hay 50 autómatas con transiciones λ. Para cada uno, su documento presenta la justificación de las λ y la tabla de λ-clausuras de **todos** sus estados:

| Problema | Archivo | Estados | Transiciones λ | Estados con Cl(q) ≠ {q} |
|---|---|---|---|---|
| [162-188 (p. 108)](jflap/afnd-lambda-1.md#problema-3-162-188-p-108) | `L3-AFNDL-p108` | 26 | 4 | 3 |
| [162-188 (p. 117)](jflap/afnd-lambda-1.md#problema-3-162-188-p-117) | `L3-AFNDL-p117` | 8 | 3 | 3 |
| [196](jflap/afnd-lambda-1.md#problema-3-196) | `L3-196` | 3 | 1 | 1 |
| [197](jflap/afnd-lambda-1.md#problema-3-197) | `L3-197` | 4 | 3 | 3 |
| [198](jflap/afnd-lambda-1.md#problema-3-198) | `L3-198` | 4 | 2 | 2 |
| [199](jflap/afnd-lambda-1.md#problema-3-199) | `L3-199` | 5 | 3 | 2 |
| [200](jflap/afnd-lambda-1.md#problema-3-200) | `L3-200` | 6 | 5 | 4 |
| [201, 206, 221](jflap/afnd-lambda-2.md#problema-3-201-206-221) | `L3-VF-201` | 6 | 4 | 3 |
| [202, 207](jflap/afnd-lambda-2.md#problema-3-202-207) | `L3-VF-202` | 4 | 1 | 1 |
| [203, 222](jflap/afnd-lambda-2.md#problema-3-203-222) | `L3-VF-203` | 10 | 12 | 7 |
| [204, 233](jflap/afnd-lambda-2.md#problema-3-204-233) | `L3-VF-204` | 6 | 5 | 3 |
| [205](jflap/afnd-lambda-2.md#problema-3-205) | `L3-VF-205` | 6 | 5 | 3 |
| [208](jflap/afnd-lambda-2.md#problema-3-208) | `L3-VF-208` | 8 | 7 | 5 |
| [209](jflap/afnd-lambda-2.md#problema-3-209) | `L3-VF-209` | 8 | 6 | 4 |
| [210, 224, 227](jflap/afnd-lambda-2.md#problema-3-210-224-227) | `L3-VF-210` | 8 | 8 | 5 |
| [211](jflap/afnd-lambda-2.md#problema-3-211) | `L3-VF-211` | 8 | 6 | 4 |
| [212](jflap/afnd-lambda-2.md#problema-3-212) | `L3-VF-212` | 8 | 6 | 4 |
| [213](jflap/afnd-lambda-2.md#problema-3-213) | `L3-VF-213` | 10 | 10 | 6 |
| [214](jflap/afnd-lambda-2.md#problema-3-214) | `L3-VF-214` | 10 | 10 | 6 |
| [215](jflap/afnd-lambda-2.md#problema-3-215) | `L3-VF-215` | 8 | 6 | 4 |
| [216](jflap/afnd-lambda-2.md#problema-3-216) | `L3-VF-216` | 8 | 6 | 4 |
| [217](jflap/afnd-lambda-2.md#problema-3-217) | `L3-VF-217` | 8 | 6 | 4 |
| [218](jflap/afnd-lambda-2.md#problema-3-218) | `L3-VF-218` | 10 | 9 | 6 |
| [219](jflap/afnd-lambda-2.md#problema-3-219) | `L3-VF-219` | 10 | 9 | 6 |
| [220](jflap/afnd-lambda-2.md#problema-3-220) | `L3-VF-220` | 12 | 13 | 8 |
| [223](jflap/afnd-lambda-2.md#problema-3-223) | `L3-VF-223` | 8 | 9 | 5 |
| [225](jflap/afnd-lambda-2.md#problema-3-225) | `L3-VF-225` | 10 | 9 | 6 |
| [228](jflap/afnd-lambda-2.md#problema-3-228) | `L3-VF-228` | 12 | 12 | 8 |
| [230](jflap/afnd-lambda-2.md#problema-3-230) | `L3-VF-230` | 2 | 1 | 1 |
| [231](jflap/afnd-lambda-2.md#problema-3-231) | `L3-VF-231` | 6 | 5 | 4 |
| [232](jflap/afnd-lambda-2.md#problema-3-232) | `L3-VF-232` | 4 | 2 | 2 |
| [234](jflap/afnd-lambda-2.md#problema-3-234) | `L3-VF-234` | 6 | 5 | 3 |
| [236](jflap/afnd-lambda-2.md#problema-3-236) | `L3-236` | 22 | 20 | 14 |
| [237](jflap/afnd-lambda-2.md#problema-3-237) | `L3-237` | 14 | 11 | 8 |
| [238](jflap/afnd-lambda-2.md#problema-3-238) | `L3-238` | 34 | 29 | 23 |
| [239](jflap/afnd-lambda-2.md#problema-3-239) | `L3-239` | 26 | 24 | 17 |
| [240](jflap/afnd-lambda-2.md#problema-3-240) | `L3-240` | 78 | 72 | 53 |
| [241](jflap/afnd-lambda-3.md#problema-3-241) | `L3-241` | 6 | 4 | 3 |
| [242](jflap/afnd-lambda-3.md#problema-3-242) | `L3-242` | 8 | 8 | 5 |
| [243](jflap/afnd-lambda-3.md#problema-3-243) | `L3-243` | 8 | 8 | 5 |
| [244](jflap/afnd-lambda-3.md#problema-3-244) | `L3-244` | 8 | 5 | 4 |
| [245](jflap/afnd-lambda-3.md#problema-3-245) | `L3-245` | 10 | 9 | 6 |
| [246](jflap/afnd-lambda-3.md#problema-3-246) | `L3-246` | 10 | 9 | 6 |
| [247](jflap/afnd-lambda-3.md#problema-3-247) | `L3-247` | 12 | 13 | 8 |
| [248](jflap/afnd-lambda-3.md#problema-3-248) | `L3-248` | 10 | 9 | 6 |
| [249](jflap/afnd-lambda-3.md#problema-3-249) | `L3-249` | 12 | 13 | 8 |
| [250](jflap/afnd-lambda-3.md#problema-3-250) | `L3-250` | 16 | 18 | 11 |
| [251](jflap/afnd-lambda-3.md#problema-3-251) | `L3-251` | 18 | 18 | 12 |
| [252](jflap/afnd-lambda-3.md#problema-3-252) | `L3-252` | 38 | 34 | 25 |
| [253](jflap/afnd-lambda-3.md#problema-3-253) | `L3-253` | 42 | 36 | 27 |

## 2.4 Conversiones y análisis comparativo

### Casos destacados

n = estados del AFND convertido (para un AFND-λ, el AFND ya sin λ y sin inaccesibles). «AFD de JFLAP» es el resultado de *Convert to DFA*, que no dibuja el conjunto vacío; «completo» lo incluye cuando hace falta para que δ sea total; «mínimo» es el AFD de Hopcroft.

| Problema | Archivo | AFND-λ | n (AFND) | Trans. AFND | AFD de JFLAP | Trans. AFD | AFD completo | AFD mínimo | Cota 2ⁿ |
|---|---|---|---|---|---|---|---|---|---|
| 192 | `L3-192-AFND` | — | 3 | 7 | 5 | 8 | 6 | 6 | 8 |
| 193 | `L3-193-AFND` | — | 4 | 12 | 7 | 13 | 8 | 7 | 16 |
| 195 | `L3-195-AFND` | — | 5 | 12 | 12 | 24 | 12 | 7 | 32 |
| 260 | `L3-260-AFND` | — | 5 | 15 | 7 | 13 | 8 | 7 | 32 |
| 190 | `L3-190` | — | 32 | 42 | 44 | 88 | 44 | 19 | 2^32 |
| 162-188 (p. 99) | `L3-AFND-p099` | — | 7 | 9 | 7 | 21 | 7 | 7 | 128 |
| 196 | `L3-196` | 3 | 3 | 6 | 3 | 4 | 3 | 3 | 8 |
| 200 | `L3-200` | 6 | 6 | 37 | 6 | 12 | 6 | 2 | 64 |
| 252 | `L3-252` | 38 | 34 | 310 | 13 | 26 | 13 | 8 | 2^34 |

<details><summary>Las 89 conversiones</summary>

| Problema | Archivo | n | AFD de JFLAP | AFD completo | AFD mínimo | 2ⁿ |
|---|---|---|---|---|---|---|
| 143b | `L2-143b` | 2 | 3 | 4 | 3 | 4 |
| 158 | `L3-158` | 3 | 3 | 4 | 4 | 8 |
| 159 | `L3-159` | 3 | 3 | 4 | 4 | 8 |
| 160 | `L3-160` | 3 | 3 | 4 | 4 | 8 |
| 161 | `L3-161` | 3 | 3 | 4 | 4 | 8 |
| 162-188 (p. 100) | `L3-AFND-p100` | 3 | 3 | 4 | 4 | 8 |
| 162-188 (p. 101) | `L3-AFND-p101` | 4 | 6 | 6 | 4 | 16 |
| 162-188 (p. 102) | `L3-AFND-p102` | 7 | 12 | 12 | 7 | 128 |
| 162-188 (p. 103) | `L3-AFND-p103` | 7 | 12 | 12 | 7 | 128 |
| 162-188 (p. 104) | `L3-AFND-p104` | 6 | 6 | 7 | 7 | 64 |
| 162-188 (p. 105) | `L3-AFND-p105` | 5 | 5 | 5 | 5 | 32 |
| 162-188 (p. 106) | `L3-AFND-p106` | 8 | 14 | 14 | 8 | 256 |
| 162-188 (p. 107) | `L3-AFND-p107` | 14 | 20 | 20 | 13 | 16,384 |
| 162-188 (p. 108) | `L3-AFNDL-p108` | 26 | 89 | 89 | 37 | 2^26 |
| 162-188 (p. 109) | `L3-AFND-p109` | 37 | 64 | 64 | 22 | 2^37 |
| 162-188 (p. 114) | `L3-AFND-p114` | 3 | 3 | 4 | 4 | 8 |
| 162-188 (p. 115) | `L3-AFND-p115` | 4 | 4 | 5 | 5 | 16 |
| 162-188 (p. 117) | `L3-AFNDL-p117` | 8 | 5 | 6 | 6 | 256 |
| 162-188 (p. 118) | `L3-AFND-p118` | 5 | 5 | 6 | 6 | 32 |
| 162-188 (p. 119) | `L3-AFND-p119` | 3 | 3 | 4 | 4 | 8 |
| 162-188 (p. 120) | `L3-AFND-p120` | 5 | 7 | 7 | 7 | 32 |
| 162-188 (p. 121) | `L3-AFND-p121` | 7 | 6 | 7 | 7 | 128 |
| 162-188 (p. 122) | `L3-AFND-p122` | 3 | 3 | 4 | 4 | 8 |
| 162-188 (p. 123) | `L3-AFND-p123` | 12 | 15 | 15 | 15 | 4,096 |
| 162-188 (p. 94) | `L3-AFND-p094` | 3 | 3 | 4 | 4 | 8 |
| 162-188 (p. 95) | `L3-AFND-p095` | 5 | 5 | 6 | 6 | 32 |
| 162-188 (p. 96) | `L3-AFND-p096` | 5 | 5 | 6 | 6 | 32 |
| 162-188 (p. 98) | `L3-AFND-p098` | 6 | 6 | 6 | 6 | 64 |
| 162-188 (p. 99) | `L3-AFND-p099` | 7 | 7 | 7 | 7 | 128 |
| 189 | `L3-189` | 7 | 12 | 12 | 7 | 128 |
| 190 | `L3-190` | 32 | 44 | 44 | 19 | 2^32 |
| 192 | `L3-192-AFND` | 3 | 5 | 6 | 6 | 8 |
| 193 | `L3-193-AFND` | 4 | 7 | 8 | 7 | 16 |
| 194 | `L3-194-AFND` | 4 | 4 | 4 | 2 | 16 |
| 195 | `L3-195-AFND` | 5 | 12 | 12 | 7 | 32 |
| 196 | `L3-196` | 3 | 3 | 3 | 3 | 8 |
| 197 | `L3-197` | 4 | 2 | 1 | 1 | 16 |
| 198 | `L3-198` | 4 | 3 | 3 | 2 | 16 |
| 199 | `L3-199` | 5 | 4 | 5 | 3 | 32 |
| 200 | `L3-200` | 6 | 6 | 6 | 2 | 64 |
| 201, 206, 221 | `L3-VF-201` | 4 | 3 | 4 | 3 | 16 |
| 202, 207 | `L3-VF-202` | 4 | 3 | 4 | 4 | 16 |
| 203, 222 | `L3-VF-203` | 8 | 3 | 4 | 4 | 256 |
| 204, 233 | `L3-VF-204` | 6 | 3 | 4 | 3 | 64 |
| 205 | `L3-VF-205` | 6 | 3 | 4 | 3 | 64 |
| 208 | `L3-VF-208` | 6 | 3 | 4 | 3 | 64 |
| 209 | `L3-VF-209` | 1 | 1 | 2 | 1 | 2 |
| 210, 224, 227 | `L3-VF-210` | 8 | 3 | 4 | 2 | 256 |
| 211 | `L3-VF-211` | 8 | 4 | 5 | 4 | 256 |
| 212 | `L3-VF-212` | 8 | 4 | 5 | 4 | 256 |
| 213 | `L3-VF-213` | 10 | 4 | 5 | 4 | 1,024 |
| 214 | `L3-VF-214` | 10 | 4 | 4 | 1 | 1,024 |
| 215 | `L3-VF-215` | 8 | 4 | 5 | 4 | 256 |
| 216 | `L3-VF-216` | 8 | 4 | 5 | 4 | 256 |
| 217 | `L3-VF-217` | 8 | 4 | 5 | 4 | 256 |
| 218 | `L3-VF-218` | 10 | 4 | 5 | 3 | 1,024 |
| 219 | `L3-VF-219` | 10 | 4 | 5 | 3 | 1,024 |
| 220 | `L3-VF-220` | 12 | 4 | 5 | 3 | 4,096 |
| 223 | `L3-VF-223` | 8 | 3 | 4 | 3 | 256 |
| 225 | `L3-VF-225` | 10 | 4 | 5 | 3 | 1,024 |
| 226 | `L3-VF-226` | 2 | 2 | 3 | 3 | 4 |
| 228 | `L3-VF-228` | 10 | 4 | 5 | 2 | 1,024 |
| 229, 235 | `L3-VF-229` | 2 | 2 | 2 | 1 | 4 |
| 230 | `L3-VF-230` | 1 | 1 | 2 | 2 | 2 |
| 231 | `L3-VF-231` | 3 | 2 | 3 | 3 | 8 |
| 232 | `L3-VF-232` | 2 | 2 | 3 | 3 | 4 |
| 234 | `L3-VF-234` | 6 | 3 | 4 | 3 | 64 |
| 236 | `L3-236` | 22 | 9 | 9 | 4 | 2^22 |
| 237 | `L3-237` | 14 | 5 | 5 | 4 | 16,384 |
| 238 | `L3-238` | 32 | 11 | 12 | 7 | 2^32 |
| 239 | `L3-239` | 24 | 9 | 9 | 6 | 2^24 |
| 240 | `L3-240` | 76 | 33 | 33 | 6 | 2^76 |
| 241 | `L3-241` | 4 | 3 | 4 | 3 | 16 |
| 242 | `L3-242` | 6 | 3 | 4 | 4 | 64 |
| 243 | `L3-243` | 8 | 3 | 3 | 1 | 256 |
| 244 | `L3-244` | 8 | 4 | 5 | 4 | 256 |
| 245 | `L3-245` | 10 | 4 | 5 | 3 | 1,024 |
| 246 | `L3-246` | 10 | 3 | 4 | 4 | 1,024 |
| 247 | `L3-247` | 10 | 4 | 5 | 5 | 1,024 |
| 248 | `L3-248` | 8 | 4 | 5 | 5 | 256 |
| 249 | `L3-249` | 10 | 4 | 5 | 3 | 1,024 |
| 250 | `L3-250` | 14 | 6 | 7 | 6 | 16,384 |
| 251 | `L3-251` | 14 | 4 | 5 | 5 | 16,384 |
| 252 | `L3-252` | 34 | 13 | 13 | 8 | 2^34 |
| 253 | `L3-253` | 40 | 22 | 23 | 18 | 2^40 |
| 260 | `L3-260-AFND` | 5 | 7 | 8 | 7 | 32 |
| 261 | `L3-261-AFND` | 5 | 5 | 5 | 3 | 32 |
| 262 | `L3-262-AFND` | 4 | 4 | 5 | 5 | 16 |
| 263 | `L3-263-AFND` | 3 | 3 | 3 | 3 | 8 |

</details>

### Comparación

**Número de estados.** En las 89 conversiones, el AFD completo nunca pasó de 89 estados, mientras que la cota 2ⁿ llega a 2^76. La proporción más alta entre estados obtenidos y cota fue 4/4 (`L2-143b`, un AFND de dos estados cuyo AFD usa los cuatro subconjuntos, incluido ∅), y en 87 de los 89 casos el AFD tuvo a lo sumo el doble de estados que el AFND. En los AFND de búsqueda de patrones (lazo inicial que «adivina» dónde empieza el patrón) el AFD tiene casi los mismos estados que el AFND: la construcción de subconjuntos reproduce la función de fallo del algoritmo KMP. En cambio, en los AFND-λ de Thompson el AFND de partida tiene muchos estados redundantes y el AFD mínimo es mucho menor.

**Complejidad de las transiciones.** El AFND tiene menos transiciones pero cada celda es un conjunto; el AFD tiene exactamente |Q|·|Σ| transiciones (una por celda) y cada una es un solo estado. En los AFND-λ, además, una parte de las transiciones no consume símbolos y obliga a calcular clausuras.

**Facilidad de diseño e interpretación.** El AFND y el AFND-λ son más fáciles de diseñar: se describen con la estructura del enunciado (un lazo que adivina, ramas para una unión, bloques concatenados por λ) y cada estado tiene un significado local. El AFD resultante es más difícil de leer: cada estado es un conjunto como {A, C, D}, cuyo significado es «el autómata podría estar en A, en C o en D». Esa es la razón por la que la lista pide AFN «más simples» en 162-188.

**Eficiencia en el reconocimiento.** Un AFD procesa cada símbolo con una consulta a la tabla: tiempo O(|w|) y memoria constante. Simular un AFND sin convertirlo exige mantener el conjunto de estados activos: cada símbolo cuesta O(n²) en el peor caso (para cada estado activo, unir sus destinos) más el cálculo de clausuras en un AFND-λ. Convertir de antemano cuesta hasta O(2ⁿ·|Σ|·n) en tiempo y 2ⁿ estados en memoria, pero se paga una sola vez; conviene cuando el autómata se usa con muchas cadenas.

### Por qué la cota 2ⁿ rara vez se alcanza

La construcción de subconjuntos solo crea los subconjuntos **alcanzables** desde Cl(q₀), y en la mayoría de los autómatas muchos de los 2ⁿ subconjuntos no lo son: si q₀ tiene un lazo con todo Σ, q₀ está en todos los conjuntos alcanzables, lo que ya divide la cota entre dos; si el AFND es casi determinista, los conjuntos tienen uno o dos elementos; y si varios estados solo se alcanzan en un orden fijo (una cadena lineal), sus combinaciones posibles son pocas. Además, varios subconjuntos alcanzables pueden ser equivalentes y fundirse al minimizar. Hopcroft, Motwani y Ullman (2007, sección 2.3.5) observan que en la práctica el AFD suele tener aproximadamente tantos estados como el AFN, aunque el peor caso sea exponencial.

### Una familia en la que sí se alcanza

Hopcroft, Motwani y Ullman (2007, sección 2.3.6) presentan el «caso malo» de la construcción: Lₙ = {w ∈ {0,1}* : el n-ésimo símbolo desde el final es 1}. Su AFND tiene n + 1 estados (q₀ con lazo que adivina cuál 1 está a n posiciones del final, seguido de una cadena de n estados), y todo AFD que lo reconozca necesita al menos 2ⁿ estados, porque debe recordar los últimos n símbolos: dos cadenas que difieren en la posición i desde el final son distinguibles por la cadena 0ⁱ⁻¹. Se construyeron los AFND de L₁ a L₆ y se convirtieron con JFLAP:

| n | Estados del AFND (n + 1) | AFD de JFLAP | AFD mínimo | 2ⁿ | Cota 2^(n+1) |
|---|---|---|---|---|---|
| 1 | 2 | 2 | 2 | 2 | 4 |
| 2 | 3 | 4 | 4 | 4 | 8 |
| 3 | 4 | 8 | 8 | 8 | 16 |
| 4 | 5 | 16 | 16 | 16 | 32 |
| 5 | 6 | 32 | 32 | 32 | 64 |
| 6 | 7 | 64 | 64 | 64 | 128 |

El AFD mínimo tiene exactamente 2ⁿ estados para cada n (archivos `familia-L*` en [`automatas/conversiones/`](../automatas/conversiones/)): el crecimiento exponencial es inevitable, no un defecto de la construcción. Respecto de los n + 1 estados del AFND queda a un factor 2 de la cota. Moore (1971) dio una familia de AFND de n estados cuyo AFD mínimo tiene exactamente 2ⁿ estados, con lo que la cota de la construcción de subconjuntos es justa.

Fuentes: Hopcroft, Motwani y Ullman (2007); Moore (1971); Rabin y Scott (1959). Ver [bibliografía](bibliografia.md).
