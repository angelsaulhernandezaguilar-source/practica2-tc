# Teoría de la Computación — Práctica 2: AFND y simulación de autómatas con interfaz gráfica

**Nombre completo:** Ángel Saúl Hernández Aguilar  
**Boleta:** 2025630123  
**Grupo:** 4CM4  
**Carrera:** Ingeniería en Sistemas Computacionales (plan 2020)  
**Unidad de aprendizaje:** Teoría de la Computación — Escuela Superior de Cómputo, IPN  
**Profesor:** M. en C. Gabriel Hurtado Avilés  
**Fecha de entrega:** martes 6 de octubre de 2026, según el enunciado (la fecha efectiva es la de la última confirmación en `main`)

**Repositorio:** https://github.com/angelsaulhernandezaguilar-source/practica2-tc

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

## Uso de inteligencia artificial en este trabajo

En cumplimiento del principio de transparencia académica, se documenta el uso de un asistente de
inteligencia artificial, como en la Práctica 1:

- Se usó para **escribir el código** (`src/`, `tests/`, `herramientas/`) y para **redactar los documentos** de
  `docs/` a partir de las fuentes de la [bibliografía](docs/bibliografia.md). Ningún texto generado se cita
  como fuente: toda afirmación remite a un libro con ISBN, un artículo con DOI o documentación oficial.
- Se usó para **verificar las fuentes en línea** en vez de citarlas de memoria: los DOI se resolvieron en
  doi.org, los ISBN en Open Library, y la sección 5 del artículo de Rabin y Scott, la figura 5 de la RFC 9293
  y los resúmenes de los dos artículos nuevos se leyeron en su texto original.
- Los resultados no se escribieron a mano: cada autómata se comparó con un oráculo escrito a partir de su
  enunciado, cada cadena de prueba se corrió en el motor de JFLAP 7.1 y cada conversión se hizo con la clase
  `NFAToDFA` de JFLAP; las tablas de los documentos se generan con esos resultados.
- Las decisiones de interpretación (ℕ = {1, 2, …}, el sentido de «después de cada aa aparece una b», la
  contradicción del problema 142 a), la división de SYN-RECEIVED en el modelo de TCP) están señaladas en el
  documento correspondiente para que el autor las revise y las defienda.

## Licencia y autoría

Trabajo académico individual para la Unidad de Aprendizaje de Teoría de la Computación, ESCOM–IPN, periodo 2027-1.
