# Propuesta de trabajo (apartado 5.3, opcional)

[← Volver al índice](../README.md)

## Detección de expresiones regulares vulnerables a ReDoS mediante autómatas

**Problema.** Los motores de expresiones regulares de JavaScript, Python y Java deciden la pertenencia
explorando los caminos de un AFN uno por uno, con retroceso. Para algunas expresiones, como `(a+)+$` o
`\s*#?\s*$`, existe una familia de entradas en la que el número de caminos que se exploran crece de forma
polinomial o exponencial con la longitud de la cadena; un atacante puede aprovecharlo para agotar el
procesador de un servidor (ReDoS). Davis et al. (2018) encontraron más de 4 000 expresiones de este tipo en
más de 10 000 módulos de npm y pypi, y mostraron que las heurísticas que usan los desarrolladores (evitar
cuantificadores anidados) producen muchos falsos positivos. Interesa una prueba que distinga con precisión
las expresiones peligrosas de las inofensivas.

**Por qué admite un modelo de lenguajes formales.** El costo del retroceso no depende de *qué* lenguaje
denota la expresión sino de *cuántas formas* tiene su AFN de aceptar o rechazar una cadena, es decir, de su
**ambigüedad**. Esa es una propiedad del autómata que se puede analizar con las herramientas del curso:
la construcción de Thompson (Thompson, 1968) da el AFN-λ; la eliminación de λ da el AFN; y el autómata
producto N × N (Rabin y Scott, 1959) permite buscar dos caminos distintos con la misma etiqueta. Si desde un
estado p salen dos ciclos distintos que leen la misma cadena, el número de caminos crece exponencialmente;
si hay dos estados distintos p ≠ q con ciclos sobre la misma cadena y un camino de p a q, crece de forma
polinomial. La tarea se reduce, entonces, a problemas de alcanzabilidad en grafos finitos.

**Clase de máquina.** Para expresiones regulares en sentido estricto (unión, concatenación, estrella y
repeticiones acotadas), bastan **autómatas finitos**: el análisis trabaja sobre el AFN y su producto, y la
salida es un autómata finito que genera las entradas maliciosas (prefijo · bombeo* · sufijo). Las
repeticiones acotadas como `a{1,1000}` hacen crecer el AFN; ahí conviene una representación con contadores
como la de Turoňová et al. (2020) en lugar de desplegarlas. Las **referencias hacia atrás** (`(a*)b\1`) ya no
describen lenguajes regulares (el lenguaje {wbw} no es regular por el lema de bombeo), y analizar
expresiones con ellas requerirá, conforme avance el curso, al menos **autómatas de pila** o un modelo más
general; para esas expresiones se prevé limitar la propuesta a detectar la construcción y advertir.

**Artículos que la sustentan.**

1. Davis, J. C., Coghlan, C. A., Servant, F., & Lee, D. (2018). The impact of regular expression denial of
   service (ReDoS) in practice: An empirical study at the ecosystem scale. En *Proceedings of the 2018 26th
   ACM ESEC/FSE* (pp. 246–256). https://doi.org/10.1145/3236024.3236027 — da el problema, la magnitud y un
   conjunto de expresiones reales para evaluar.
2. Turoňová, L., Holík, L., Lengál, O., Saarikivi, O., Veanes, M., & Vojnar, T. (2020). Regex matching with
   counting-set automata. *Proceedings of the ACM on Programming Languages, 4*(OOPSLA), 1–30.
   https://doi.org/10.1145/3428286 — da el tratamiento de la repetición acotada y muestra la conexión entre
   no determinismo, explosión de estados y desempeño de los motores.

**Qué se construiría.** Una extensión del núcleo de este repositorio (`src/automata.py`):

1. Un analizador de expresiones con la sintaxis común de Python (clases de caracteres, `?`, `+`, `{m,n}`),
   traducido a la construcción de Thompson que ya existe en `herramientas/construir.py`.
2. La eliminación de λ y el producto N × N, con una búsqueda de los patrones de ciclo descritos arriba; si se
   encuentra uno, la herramienta construye una entrada maliciosa concreta: un prefijo que lleva a p, la
   cadena del ciclo repetida k veces y un sufijo que fuerza el rechazo.
3. Una opción en la interfaz Flet para mostrar el AFN, resaltar los ciclos ambiguos y simular la entrada.

**Cómo se comprobaría que funciona.**

- **Pruebas unitarias** con expresiones de clasificación conocida (`a*`, `(a|a)*`, `(a+)+`, `a*a*`) y con la
  verificación de que cada entrada generada sí está en la familia predicha.
- **Validación empírica:** para cada expresión marcada como exponencial o polinomial, medir con el módulo
  `re` de Python el tiempo de búsqueda en entradas de longitud creciente (10, 20, 40, …) y ajustar la curva;
  la predicción es correcta si el crecimiento observado coincide con el de la clase (exponencial, cuadrático,
  lineal). Las expresiones marcadas como seguras deben mantenerse lineales.
- **Comparación con el estudio de Davis et al. (2018):** sobre una muestra de sus expresiones, medir la
  proporción de falsos positivos de la heurística de cuantificadores anidados frente a la del análisis con
  autómatas.
