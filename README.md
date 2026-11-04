# Teoría de la Computación — Prácticas 2 y 3: simulador de autómatas finitos con interfaz gráfica

**Nombre completo:** Ángel Saúl Hernández Aguilar  
**Boleta:** 2025630123  
**Grupo:** 4CM4  
**Carrera:** Ingeniería en Sistemas Computacionales (plan 2020)  
**Unidad de aprendizaje:** Teoría de la Computación — Escuela Superior de Cómputo, IPN  
**Profesor:** M. en C. Gabriel Hurtado Avilés  
**Fecha de entrega de la Práctica 2:** martes 6 de octubre de 2026, según el enunciado; la confirmación entregada quedó marcada con la etiqueta `practica2` (la última de `main` antes de la Práctica 3)

**Repositorio:** https://github.com/angelsaulhernandezaguilar-source/practica2-tc

## Práctica 3: de AFD a expresiones regulares con JFLAP, y de AFN-λ a AFD mínimo en el software

**Fecha de entrega:** miércoles 4 de noviembre de 2026. La entrega es la confirmación que señala la etiqueta
**`practica3`**; la Práctica 2 quedó fija en la etiqueta `practica2`. El software interactivo es el de la
Práctica 2, ampliado en este mismo repositorio, como pide el enunciado.

| Documento | Contenido |
|---|---|
| [Ejercicio 1](docs/practica3/01-afd-a-er-jflap.md) | Cinco AFD convertidos con *Convert FA to RE* (cada estado eliminado, con capturas), verificación con *Convert to NFA* y *Compare Equivalence*, simplificación con leyes algebraicas, y los tres métodos a mano para dos AFD |
| [Ejercicio 2](docs/practica3/02-software.md) | Cerradura λ, simulación directa, eliminación de λ, subconjuntos, minimización, equivalencia y validación por lotes, con capturas; pruebas automatizadas y la justificación de la longitud de comparación |
| [Ejercicio 3](docs/practica3/03-algoritmos.md) | Para cada algoritmo: problema, resultado teórico con su referencia, pseudocódigo y sus funciones, ejemplo a mano contra el software y número de pasos |

| Carpeta | Contenido |
|---|---|
| `automatas/practica3/afd-a-er/` | Los cinco AFD (`.jff`) y sus expresiones de JFLAP (`*-ER.jff`) |
| `automatas/practica3/casos-de-prueba/` | Los `.jff` de la Lista 3 usados en las pruebas: 151-157, 192-194, 196-200 y 260-263 |
| `src/algoritmos.py` | Los algoritmos nuevos, con su registro paso a paso (núcleo, sin Flet) |
| `tests/test_practica3.py` | Pruebas del apartado 2.6 |
| `evidencias/practica3/` | Capturas de JFLAP (`jflap/`, una por paso), del simulador (`app/`), un informe de validación y la integración continua (`ci/`) |
| `herramientas/` | `JflapER.java` y `practica3_er.py` (Ejercicio 1 en JFLAP), `capturas_p3.py` (capturas del simulador) |

### Uso de las funciones nuevas

1. Cargue un autómata en la pestaña **1. Definir** (*Abrir .jff* o la lista *Autómatas del repositorio*; los
   casos de prueba están en `practica3/casos-de-prueba/`).
2. Pestaña **5. Paso a paso**: elija el algoritmo (*2.1 Cerradura λ*, *2.2 Eliminación de transiciones λ*,
   *2.3 Construcción de subconjuntos*, *2.4 Minimización de AFD* o *2.4 Equivalencia de dos autómatas*), pulse
   *Calcular* y avance con *Siguiente paso* / *Paso anterior* / *Hasta el final*. Para la cerradura elija el
   estado en *Estado para Cl(q)*; para la equivalencia, el segundo autómata en su lista. *Usar el resultado*
   reemplaza el autómata actual por el obtenido (para encadenar AFN-λ → AFN → AFD → mínimo o guardarlo).
3. Pestaña **3. Simular**: la *Simulación directa* muestra en cada paso los activos antes y después de la
   cerradura λ. En *Validación de varias cadenas*, *Cargar archivo de cadenas (.txt)* lee una cadena por línea
   (línea vacía o `λ` = cadena vacía, `#` = comentario) y *Guardar informe* escribe el resultado de cada una.
4. Desde Python, sin interfaz (con `PYTHONPATH=src`, como en las pruebas):

   ```python
   from formatos import cargar
   from algoritmos import de_afn_lambda_a_minimo, validar_lote, informe_lote
   c = de_afn_lambda_a_minimo(cargar("automatas/practica3/casos-de-prueba/L3-199.jff"))
   print("\n".join(c.sin_lambda.describir() + c.subconjuntos.describir() + c.minimo.describir()))
   ```

Regenerar el Ejercicio 1 (requiere Java y JFLAP 7.1): `set JFLAP_JAR=C:\ruta\JFLAP7.1.jar` y
`python herramientas/practica3_er.py`.

## Práctica 2

## Índice

| Documento | Contenido |
|---|---|
| [Ejercicio 1](docs/01-entorno.md) | Entorno reutilizado, flujo de ramas con *Pull Requests* e integración continua |
| [Ejercicio 2](docs/02-jflap.md) | Los problemas 94-263 clasificados en AFD, AFND y AFND-λ; λ-clausuras; conversiones y análisis comparativo |
| [Ejercicio 3](docs/03-simulador.md) | Simulador con interfaz gráfica: definición, importación, simulación paso a paso, exportación y pruebas |
| [Ejercicio 4](docs/04-investigacion.md) | Investigación, el artículo de Rabin y Scott (1959) y dos artículos nuevos |
| [Ejercicio 5](docs/05-del-articulo-al-automata.md) | El diagrama de estados de TCP modelado como AFD |
| [Propuesta](docs/propuesta.md) | Propuesta de artículo (apartado 5.3, opcional) |
| [Bibliografía](docs/bibliografia.md) | Referencias en formato APA 7 |

| Carpeta | Contenido |
|---|---|
| `automatas/lista2-afd/` | Sección **AFD**: todos los AFD de las Listas 2 y 3, en `.jff`, `.json` y `.xml` |
| `automatas/lista3-afnd/` | Sección **AFND** estándar |
| `automatas/lista3-afnd-lambda/` | Sección **AFND-λ** |
| `automatas/conversiones/` | AFND sin λ y AFD obtenidos con JFLAP; familia Lₙ |
| `automatas/aplicacion/` | El autómata de TCP del Ejercicio 5 |
| `src/` | `automata.py` y `formatos.py` (núcleo), `lenguajes.py` (Práctica 1) y `app.py` (interfaz) |
| `tests/` | Pruebas con pytest |
| `herramientas/` | Catálogo de ejercicios, generación de archivos y documentos, y herramientas Java que usan JFLAP |
| `evidencias/` | Capturas de Git, de la integración continua, de JFLAP y del simulador |

## Procedencia: Práctica 1

El entorno (`entorno/Dockerfile`, `entorno/compose.yml`, `requirements.txt`, `pytest.ini`), el módulo
`src/lenguajes.py` y sus pruebas `tests/test_lenguajes.py` proceden **sin cambios de código** de la Práctica 1:
[angelsaulhernandezaguilar-source/Teoria-computcion-4CM4](https://github.com/angelsaulhernandezaguilar-source/Teoria-computcion-4CM4).
También proceden de ella los 101 archivos `.jff` de los problemas con asterisco, copiados con
`herramientas/importar_p1.py`, y su catálogo (`herramientas/practica1.py`). El detalle está en el
[Ejercicio 1](docs/01-entorno.md).

## Cómo se ejecuta

Con Docker Desktop encendido, desde la carpeta `entorno/`:

```bash
docker compose build
docker compose run --rm py311 pytest -q
docker compose run --rm py312 pytest -q
docker compose run --rm py313 pytest -q
docker compose up py312      # simulador en http://localhost:8550
docker compose down
```

Sin Docker, con un entorno virtual:

```bash
py -3.12 -m venv venv
venv\Scripts\activate            # macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
pytest -q
python src/app.py                # abre el simulador en una ventana
```

### Uso del simulador

1. **Definir** (pestaña 1): escriba Σ y Q separados por comas, pulse *Generar o actualizar la tabla*, elija q₀,
   marque F y llene las celdas de δ con los destinos separados por comas (la columna λ es para las
   transiciones λ). *Aplicar definición* valida la quíntupla. O bien abra un `.jff`, `.json` o `.xml`, o elija
   uno de la lista de autómatas del repositorio.
2. **Autómata** (pestaña 2): diagrama, tabla de transiciones, quíntupla y λ-clausuras; botones para quitar λ,
   convertir a AFD y minimizar.
3. **Simular** (pestaña 3): escriba la cadena (vacía = λ) y pulse *Validar*, o avance con *Siguiente paso*.
4. **Lenguajes** (pestaña 4): las operaciones de la Práctica 1.
5. *Guardar .jff / .json / .xml* (pestaña 1) exporta el autómata actual.

### Regenerar los autómatas y los documentos del Ejercicio 2

Requiere Java y JFLAP 7.1:

```bash
set JFLAP_JAR=C:\ruta\JFLAP7.1.jar          # bash: export JFLAP_JAR=/ruta/JFLAP7.1.jar
python herramientas/generar.py todo
python herramientas/aplicacion.py
```

## Convención para λ

En los tres formatos de archivo, **λ es la cadena vacía como símbolo leído**: `<read/>` en `.jff`,
`"lee": ""` en `.json` y `lee=""` en `.xml`. Es la convención de JFLAP y la del Anexo 3; por eso el alfabeto
nunca puede contener la cadena vacía. JFLAP no guarda el alfabeto en el `.jff`; este proyecto lo escribe en un
comentario `<!--alfabeto: [...]-->` que JFLAP ignora, y si falta lo deduce de las transiciones. Más detalles en
el [Ejercicio 3](docs/03-simulador.md#32-importación).

## Licencia y autoría

Trabajo académico individual para la Unidad de Aprendizaje de Teoría de la Computación, ESCOM–IPN, periodo 2027-1.
