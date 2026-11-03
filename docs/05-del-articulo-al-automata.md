# Ejercicio 5. Del artículo al autómata: el diagrama de estados de TCP

[← Volver al índice](../README.md)

## Elección

Se eligió la opción **«el diagrama de estados del protocolo TCP»**, que Gribkoff (2013, figura 4) presenta
como aplicación de los autómatas finitos deterministas. Gribkoff reproduce el diagrama sin definir el
alfabeto; por eso el modelo se construyó directamente sobre la especificación normativa vigente, la
**RFC 9293** (Eddy, 2022, sección 3.3.2, figura 5 y sus tres notas), que sustituye a la RFC 793 de 1981.
La RFC advierte que el diagrama «es solo un resumen y no debe tomarse como la especificación total».

## 5.1 Alfabeto

Según la RFC, una conexión cambia de estado en respuesta a **eventos**: llamadas del usuario, segmentos
entrantes y vencimientos de temporizadores. El alfabeto es el conjunto de esos eventos tal como los percibe
el TCP local; las *acciones* que el diagrama escribe debajo de cada flecha (snd SYN, snd ACK, delete TCB) son
salidas y no forman parte de Σ. Cada evento se representa con una letra para que JFLAP lo simule:

| Símbolo | Evento | Origen |
|---|---|---|
| `p` | OPEN pasiva | llamada del usuario |
| `o` | OPEN activa | llamada del usuario |
| `e` | SEND (solo cambia de estado en LISTEN, sección 3.10.2) | llamada del usuario |
| `c` | CLOSE | llamada del usuario |
| `a` | ABORT (RFC 9293, sección 3.10.5) | llamada del usuario |
| `s` | segmento con SYN, sin ACK | red |
| `y` | segmento con SYN y ACK de nuestro SYN | red |
| `k` | ACK que confirma nuestro SYN o nuestro FIN | red |
| `f` | segmento con FIN | red |
| `g` | FIN que además confirma nuestro FIN (nota 2 de la figura 5) | red |
| `r` | segmento con RST | red |
| `t` | vence el temporizador de 2·MSL | temporizador |

Σ = {p, o, e, c, a, s, y, k, f, g, r, t}. La RFC menciona además RECEIVE y STATUS, que nunca cambian de
estado; se omiten porque en el modelo serían lazos en todos los estados y no alteran el lenguaje.

## 5.2 Definición formal

M = (Q, Σ, δ, q₀, F) con:

- **Q** = {CLOSED, LISTEN, SYN-SENT, SYN-RCVD-P, SYN-RCVD-A, ESTAB, FIN-WAIT-1, FIN-WAIT-2, CLOSE-WAIT,
  CLOSING, LAST-ACK, TIME-WAIT} (12 estados).
- **Σ** = {p, o, e, c, a, s, y, k, f, g, r, t}.
- **q₀** = CLOSED: antes del primer evento no existe conexión.
- **F** = {CLOSED}: el modelo acepta las secuencias de eventos **después de las cuales la conexión quedó
  completamente liberada** (sin TCB). Así, L(M) es el conjunto de historias «limpias» de una conexión, que es
  lo que interesa verificar en una traza: una secuencia rechazada deja recursos asignados.
- **δ** es la tabla siguiente; «·» significa que el evento no cambia de estado.

| Estado | p | o | e | c | a | s | y | k | f | g | r | t |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| →*CLOSED | LISTEN | SYN-SENT | · | · | · | · | · | · | · | · | · | · |
| LISTEN | · | SYN-SENT | SYN-SENT | CLOSED | CLOSED | SYN-RCVD-P | · | · | · | · | · | · |
| SYN-SENT | · | · | · | CLOSED | CLOSED | SYN-RCVD-A | ESTAB | · | · | · | CLOSED | · |
| SYN-RCVD-P | · | · | · | FIN-WAIT-1 | CLOSED | · | · | ESTAB | · | · | LISTEN | · |
| SYN-RCVD-A | · | · | · | FIN-WAIT-1 | CLOSED | · | · | ESTAB | · | · | CLOSED | · |
| ESTAB | · | · | · | FIN-WAIT-1 | CLOSED | · | · | · | CLOSE-WAIT | · | CLOSED | · |
| FIN-WAIT-1 | · | · | · | · | CLOSED | · | · | FIN-WAIT-2 | CLOSING | TIME-WAIT | CLOSED | · |
| FIN-WAIT-2 | · | · | · | · | CLOSED | · | · | · | TIME-WAIT | · | CLOSED | · |
| CLOSE-WAIT | · | · | · | LAST-ACK | CLOSED | · | · | · | · | · | CLOSED | · |
| CLOSING | · | · | · | · | CLOSED | · | · | TIME-WAIT | · | · | CLOSED | · |
| LAST-ACK | · | · | · | · | CLOSED | · | · | CLOSED | · | · | CLOSED | · |
| TIME-WAIT | · | · | · | · | CLOSED | · | · | · | · | · | CLOSED | CLOSED |

### Qué representa cada estado

| Estado | Significado (RFC 9293, sección 3.3.2) |
|---|---|
| CLOSED | No hay conexión ni bloque de control (TCB). |
| LISTEN | Se espera una solicitud de conexión (después de un OPEN pasivo). |
| SYN-SENT | Se envió SYN y se espera la respuesta. |
| SYN-RCVD-P | Se recibió SYN y se respondió SYN,ACK; **se llegó desde LISTEN**. |
| SYN-RCVD-A | Igual, pero **se llegó desde SYN-SENT** (apertura simultánea). |
| ESTAB | Conexión establecida; es el estado de transferencia de datos. |
| FIN-WAIT-1 | El usuario cerró; se envió FIN y se espera su ACK (o el FIN remoto). |
| FIN-WAIT-2 | Nuestro FIN fue confirmado; se espera el FIN remoto. |
| CLOSE-WAIT | Llegó el FIN remoto; se espera que el usuario cierre. |
| CLOSING | Ambos lados enviaron FIN; se espera el ACK del nuestro. |
| LAST-ACK | Se envió nuestro FIN después del remoto; se espera su ACK. |
| TIME-WAIT | Se espera 2·MSL para que los segmentos retrasados no afecten conexiones nuevas. |

### Decisiones de modelado

1. **SYN-RECEIVED se divide en dos estados.** La nota 1 de la figura dice que la transición de SYN-RECEIVED a
   LISTEN al recibir RST solo ocurre si se llegó por un OPEN pasivo; si se llegó por apertura simultánea, el
   RST cierra la conexión (nota 3). Un AFD no recuerda de dónde viene salvo en su estado, así que el
   diagrama de la RFC, leído literalmente, *no es determinista* en ese punto: necesita dos copias del
   estado. La prueba `test_syn_rcvd_necesita_dos_estados` comprueba que fusionarlas cambiaría el lenguaje
   (`psr` termina en LISTEN y `osr` en CLOSED), y el algoritmo de Hopcroft confirma que los 12 estados son
   distinguibles: el AFD es mínimo.
2. **Las notas 2 y 3 se incorporan.** El símbolo `g` modela la nota 2 (FIN-WAIT-1 → TIME-WAIT cuando el FIN
   remoto ya confirma el nuestro). El RST recibido lleva a CLOSED desde los estados sincronizados (nota 3);
   en LISTEN y en CLOSED se ignora, como indica la sección 3.10.7 de la RFC.
3. **Los eventos que no aparecen en la figura no cambian de estado.** La RFC aclara que la figura muestra
   solo cambios de estado; un evento sin flecha produce, como mucho, un mensaje de error o el envío de un
   segmento, pero el estado se conserva. Por eso δ es total con lazos, y M es un **AFD** en el sentido del
   curso. Se agregaron dos cambios que la figura no dibuja pero el texto de la RFC sí especifica: un OPEN
   activo o un SEND en LISTEN convierten la conexión en activa y pasan a SYN-SENT (sección 3.10.1).

## 5.3 Archivo y validación en el simulador

Archivos: [`automatas/aplicacion/tcp.jff`](../automatas/aplicacion/tcp.jff),
[`tcp.json`](../automatas/aplicacion/tcp.json) y [`tcp.xml`](../automatas/aplicacion/tcp.xml), generados con
[`herramientas/aplicacion.py`](../herramientas/aplicacion.py). El `.jff` se cargó en el simulador de este
proyecto, que reconoció la quíntupla completa (AFD, 12 estados, 12 símbolos, δ total) y simuló las cadenas
paso a paso (captura: [`evidencias/app/tcp-simulacion.png`](../evidencias/app/tcp-simulacion.png)). Las
mismas cadenas se corrieron en JFLAP 7.1
([`evidencias/jflap/aplicacion-jflap.tsv`](../evidencias/jflap/aplicacion-jflap.tsv)) y la prueba
[`tests/test_aplicacion.py`](../tests/test_aplicacion.py) las verifica desde los tres formatos.

| # | Cadena | Escenario | Estado final | Esperado | Simulador | JFLAP |
|---|---|---|---|---|---|---|
| 1 | λ | Ningún evento | CLOSED | acepta | acepta | acepta |
| 2 | `pc` | El servidor escucha y el usuario cancela | CLOSED | acepta | acepta | acepta |
| 3 | `oyckft` | Cliente: apertura y cierre activos, TIME-WAIT completo | CLOSED | acepta | acepta | acepta |
| 4 | `pskfck` | Servidor: apertura pasiva, cierre pasivo | CLOSED | acepta | acepta | acepta |
| 5 | `oycfkt` | Cierre simultáneo (pasa por CLOSING) | CLOSED | acepta | acepta | acepta |
| 6 | `oycgt` | Nota 2: FIN que confirma nuestro FIN | CLOSED | acepta | acepta | acepta |
| 7 | `oskr` | Apertura simultánea y RST en ESTAB | CLOSED | acepta | acepta | acepta |
| 8 | `psrc` | RST en SYN-RCVD-P regresa a LISTEN; luego CLOSE | CLOSED | acepta | acepta | acepta |
| 9 | `osr` | RST en SYN-RCVD-A cierra | CLOSED | acepta | acepta | acepta |
| 10 | `peyckft` | SEND en LISTEN convierte la apertura en activa | CLOSED | acepta | acepta | acepta |
| 11 | `oya` | ABORT en ESTAB | CLOSED | acepta | acepta | acepta |
| 12 | `psr` | Tras el RST se vuelve a escuchar | LISTEN | rechaza | rechaza | rechaza |
| 13 | `oyc` | Se envió FIN y no llega su ACK | FIN-WAIT-1 | rechaza | rechaza | rechaza |
| 14 | `oyckf` | Falta que venza el temporizador | TIME-WAIT | rechaza | rechaza | rechaza |
| 15 | `pskf` | El usuario no ha cerrado | CLOSE-WAIT | rechaza | rechaza | rechaza |
| 16 | `oyftc` | `t` no afecta CLOSE-WAIT; falta el último ACK | LAST-ACK | rechaza | rechaza | rechaza |
| 17 | `o` | SYN enviado sin respuesta | SYN-SENT | rechaza | rechaza | rechaza |

Recorrido de la cadena 3, en la que se ve el ciclo de vida típico de un cliente:
CLOSED -o→ SYN-SENT -y→ ESTAB -c→ FIN-WAIT-1 -k→ FIN-WAIT-2 -f→ TIME-WAIT -t→ CLOSED.

## 5.4 La abstracción: qué captura el modelo y qué deja fuera

El autómata captura la **dimensión de control** de una conexión TCP: en qué fase del ciclo de vida está
(apertura, transferencia, cierre, espera) y qué órdenes de eventos son posibles. Con eso responde preguntas
útiles con solo leer una traza: si una conexión quedó abierta (la cadena se rechaza), por qué estado pasó, si
un cierre fue activo, pasivo o simultáneo, o si un RST la cerró. También pone de relieve algo que el
diagrama de la RFC deja en una nota: SYN-RECEIVED no es un estado sino dos, porque su comportamiento ante un
RST depende de la historia; un modelo finito solo puede recordar esa historia multiplicando estados.

Lo que deja fuera es casi todo lo que hace que TCP funcione. Primero, los **datos y los números de
secuencia**: en ESTAB se pueden enviar millones de bytes y el modelo no cambia de estado; saber si un ACK
confirma *nuestro* FIN exige comparar números de secuencia de 32 bits, y el modelo lo resuelve dando al
evento un símbolo distinto (`k` frente a otros ACK), es decir, empuja ese cálculo fuera del autómata.
Segundo, las **salidas**: el diagrama dice qué se envía en cada transición (SYN, SYN-ACK, ACK, FIN) y un AFD
no produce salidas; un transductor de Mealy las conservaría, como en el autocompletado de Lucene que
describe Gribkoff (2013). Tercero, el **tiempo**: 2·MSL, la retransmisión y los temporizadores de
mantenimiento son eventos abstractos (`t`) sin duración. Cuarto, las **condiciones de validez**: ventanas,
segmentos fuera de orden, RST que deben ignorarse por no estar en la ventana o la protección contra
ataques ciegos de la RFC 5961, que la RFC 9293 incorpora. Por último, el modelo describe **una** conexión
y un solo extremo; el comportamiento conjunto de cliente y servidor sería el producto de dos autómatas
comunicados por la red, que puede perder o reordenar segmentos. Esa es la frontera de la abstracción:
el AFD es correcto para el orden de los eventos de control, y no dice nada de si los bytes llegan.

## Fuentes

Eddy (2022); Gribkoff (2013); Hopcroft et al. (2007). Ver la [bibliografía](bibliografia.md).
