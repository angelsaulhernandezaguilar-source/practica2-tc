"""Ejercicio 5: el diagrama de estados de una conexión TCP (RFC 9293, figura 5) como AFD.

Uso:  python herramientas/aplicacion.py
Escribe automatas/aplicacion/tcp.{jff,json,xml} y evidencias/jflap/aplicacion-casos.tsv.
"""

import pathlib
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
sys.path[:0] = [str(RAIZ / "src")]

from automata import Automata  # noqa: E402
from formatos import guardar_tres  # noqa: E402

# Alfabeto: los eventos que percibe el TCP local. Un carácter por evento para que JFLAP lo simule.
ALFABETO = {
    "p": "llamada OPEN pasiva del usuario",
    "o": "llamada OPEN activa del usuario",
    "e": "llamada SEND del usuario",
    "c": "llamada CLOSE del usuario",
    "a": "llamada ABORT del usuario",
    "s": "llega un segmento con SYN (sin ACK)",
    "y": "llega un segmento con SYN y ACK de nuestro SYN",
    "k": "llega un ACK que confirma nuestro SYN o nuestro FIN",
    "f": "llega un segmento con FIN",
    "g": "llega un FIN que además confirma nuestro FIN (nota 2 de la figura 5)",
    "r": "llega un segmento con RST",
    "t": "vence el temporizador de 2·MSL",
}

ESTADOS = {
    "CLOSED": "no hay conexión ni TCB",
    "LISTEN": "espera solicitudes de conexión (tras OPEN pasiva)",
    "SYN-SENT": "se envió SYN; espera la respuesta",
    "SYN-RCVD-P": "se recibió SYN y se respondió SYN,ACK; se llegó desde LISTEN",
    "SYN-RCVD-A": "igual, pero se llegó desde SYN-SENT (apertura simultánea)",
    "ESTAB": "conexión establecida; se transfieren datos",
    "FIN-WAIT-1": "el usuario cerró; se envió FIN y se espera su ACK",
    "FIN-WAIT-2": "nuestro FIN fue confirmado; se espera el FIN remoto",
    "CLOSE-WAIT": "llegó el FIN remoto; se espera que el usuario cierre",
    "CLOSING": "ambos lados enviaron FIN a la vez; se espera el ACK del nuestro",
    "LAST-ACK": "se envió nuestro FIN tras el remoto; se espera su ACK",
    "TIME-WAIT": "se espera 2·MSL para que no queden segmentos retrasados",
}

CAMBIOS = """
CLOSED p LISTEN; CLOSED o SYN-SENT;
LISTEN s SYN-RCVD-P; LISTEN e SYN-SENT; LISTEN o SYN-SENT; LISTEN c CLOSED; LISTEN a CLOSED;
SYN-SENT y ESTAB; SYN-SENT s SYN-RCVD-A; SYN-SENT c CLOSED; SYN-SENT a CLOSED; SYN-SENT r CLOSED;
SYN-RCVD-P k ESTAB; SYN-RCVD-P c FIN-WAIT-1; SYN-RCVD-P r LISTEN; SYN-RCVD-P a CLOSED;
SYN-RCVD-A k ESTAB; SYN-RCVD-A c FIN-WAIT-1; SYN-RCVD-A r CLOSED; SYN-RCVD-A a CLOSED;
ESTAB c FIN-WAIT-1; ESTAB f CLOSE-WAIT; ESTAB r CLOSED; ESTAB a CLOSED;
FIN-WAIT-1 k FIN-WAIT-2; FIN-WAIT-1 f CLOSING; FIN-WAIT-1 g TIME-WAIT; FIN-WAIT-1 r CLOSED; FIN-WAIT-1 a CLOSED;
FIN-WAIT-2 f TIME-WAIT; FIN-WAIT-2 r CLOSED; FIN-WAIT-2 a CLOSED;
CLOSE-WAIT c LAST-ACK; CLOSE-WAIT r CLOSED; CLOSE-WAIT a CLOSED;
CLOSING k TIME-WAIT; CLOSING r CLOSED; CLOSING a CLOSED;
LAST-ACK k CLOSED; LAST-ACK r CLOSED; LAST-ACK a CLOSED;
TIME-WAIT t CLOSED; TIME-WAIT r CLOSED; TIME-WAIT a CLOSED
"""

# (cadena, ¿se espera aceptación?, qué representa)
CASOS = [
    ("", True, "Ningún evento: la conexión nunca existió"),
    ("pc", True, "El servidor escucha y el usuario cancela"),
    ("oyckft", True, "Cliente: apertura activa, cierre activo y TIME-WAIT completo"),
    ("pskfck", True, "Servidor: apertura pasiva y cierre pasivo (CLOSE-WAIT → LAST-ACK)"),
    ("oycfkt", True, "Cierre simultáneo: FIN-WAIT-1 → CLOSING → TIME-WAIT"),
    ("oycgt", True, "Nota 2: el FIN remoto confirma el nuestro (FIN-WAIT-1 → TIME-WAIT)"),
    ("oskr", True, "Apertura simultánea y RST en ESTAB"),
    ("psrc", True, "RST en SYN-RCVD desde LISTEN regresa a LISTEN; luego CLOSE"),
    ("osr", True, "RST en SYN-RCVD por apertura simultánea va a CLOSED"),
    ("peyckft", True, "SEND en LISTEN convierte la apertura en activa"),
    ("oya", True, "ABORT en ESTAB"),
    ("psr", False, "Tras el RST se vuelve a LISTEN: la conexión sigue abierta"),
    ("oyc", False, "Se envió FIN y no llega el ACK: queda en FIN-WAIT-1"),
    ("oyckf", False, "Falta el temporizador: queda en TIME-WAIT"),
    ("pskf", False, "El usuario no ha cerrado: queda en CLOSE-WAIT"),
    ("oyftc", False, "t no cambia CLOSE-WAIT; CLOSE lleva a LAST-ACK y falta el ACK"),
    ("o", False, "SYN enviado sin respuesta"),
]


def tcp() -> Automata:
    trans = {}
    for item in CAMBIOS.replace("\n", " ").split(";"):
        if item.strip():
            q, a, p = item.split()
            trans[q, a] = p
    # Eventos que no aparecen en la figura no cambian de estado (la figura solo muestra cambios).
    lista = [(q, a, trans.get((q, a), q)) for q in ESTADOS for a in ALFABETO]
    return Automata(list(ALFABETO), list(ESTADOS), "CLOSED", {"CLOSED"}, lista, "tcp").validar()


if __name__ == "__main__":
    m = tcp()
    destino = RAIZ / "automatas" / "aplicacion"
    destino.mkdir(parents=True, exist_ok=True)
    guardar_tres(m, destino / "tcp")
    for w, esperado, _ in CASOS:
        assert m.acepta(w) == esperado, w
    (RAIZ / "evidencias" / "jflap" / "aplicacion-casos.tsv").write_text(
        "".join(f"automatas/aplicacion/tcp.jff\t{w}\n" for w, _, _ in CASOS), encoding="utf-8", newline="\n")
    print(m, m.tipo, "minimo:", len(m.minimizar().estados))
