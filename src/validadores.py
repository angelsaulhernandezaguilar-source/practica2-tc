"""
Práctica 4, Ejercicio 4: validadores de formatos reales con expresiones regulares.

Cada validador se define una sola vez, en la notación del curso con clases de
símbolos declaradas; de ahí salen el AFD (por el Ejercicio 2) y el patrón del
módulo ``re`` (por ``expresiones.a_python``). Los dos deben coincidir en toda
cadena; ``ejemplos`` genera el conjunto de prueba con el que se comprueba.

Los cuatro validadores: correo electrónico, teléfono nacional (México, diez
dígitos), fecha en tres formatos y URL. Las aproximaciones y lo que queda
fuera de cada expresión están en docs/practica4/04-validadores.md.
"""

from __future__ import annotations

import random
import re
from dataclasses import dataclass, field
from functools import lru_cache

from expresiones import CadenaExpresion, a_python, analizar, de_expresion_a_minimo

DIGITOS = "0123456789"
MINUSCULAS = "abcdefghijklmnopqrstuvwxyz"
MAYUSCULAS = MINUSCULAS.upper()
LETRAS = MINUSCULAS + MAYUSCULAS
ALFANUMERICOS = LETRAS + DIGITOS


@dataclass
class Validador:
    clave: str
    nombre: str
    expresion: str  # notación del curso
    clases: dict  # abreviaturas de clases de símbolos
    descripcion: str
    fuente: str  # norma o documento que se aproxima
    fuera: list = field(default_factory=list)  # casos válidos o inválidos que la expresión no distingue
    validas: list = field(default_factory=list)  # ejemplos fijos
    invalidas: list = field(default_factory=list)

    @property
    def patron(self) -> str:
        return a_python(analizar(self.expresion, self.clases))

    @property
    def re(self):
        return re.compile(self.patron)

    def cadena(self) -> CadenaExpresion:
        return _cadena(self.clave)

    def alfabeto(self) -> list[str]:
        return sorted(analizar(self.expresion, self.clases).simbolos())

    def valida_con_re(self, w: str) -> bool:
        return self.re.fullmatch(w) is not None

    def valida_con_automata(self, w: str) -> bool:
        return self.cadena().acepta(w)

    def clases_texto(self) -> list[str]:
        return [f"{n} = {_mostrar_clase(m)}" for n, m in self.clases.items()]


def _mostrar_clase(miembros: str) -> str:
    m = "".join(miembros)
    for nombre, bloque in (("0+1+…+9", DIGITOS), ("a+b+…+z", MINUSCULAS), ("A+B+…+Z", MAYUSCULAS)):
        if bloque in m:
            m = m.replace(bloque, f" {nombre} ")
    partes = []
    for trozo in m.split(" "):
        if not trozo:
            continue
        partes.append(trozo if "…" in trozo else "+".join("␣" if c == " " else c for c in trozo))
    return "+".join(partes)


# ----------------------------------------------------------------------
# Definiciones
# ----------------------------------------------------------------------

_ETIQUETA = "(X(X+-)*X+X)"  # etiqueta de dominio: alfanumérica, puede llevar guiones interiores

CORREO = Validador(
    "correo", "Correo electrónico",
    f"AA*(.AA*)*@{_ETIQUETA}(.{_ETIQUETA})*.YYY*",
    {"A": ALFANUMERICOS + "_-+", "X": ALFANUMERICOS, "Y": LETRAS},
    "parte local como dot-atom (átomos de letras, dígitos, _, - y + separados por puntos), @, "
    "etiquetas de dominio alfanuméricas con guiones interiores separadas por puntos y un dominio superior "
    "de al menos dos letras.",
    "RFC 5322, § 3.4.1 (addr-spec = local-part \"@\" domain, con la forma dot-atom) y RFC 1035, § 2.3.1 "
    "(etiquetas de dominio: letras, dígitos y guiones, sin guion al inicio ni al final).",
    [
        "Quedan fuera (válidos según la norma): partes locales entre comillas (\"juan perez\"@x.mx), "
        "comentarios entre paréntesis, dominios literales ([192.168.0.1]), caracteres como ! # $ % & ' * / = ? "
        "^ ` { | } ~ en la parte local y los dominios internacionalizados (RFC 6531).",
        "Se aceptan (inválidos en la práctica): etiquetas de más de 63 caracteres y direcciones de más de 254, "
        "porque los límites de longitud no son parte de la expresión; dominios superiores que no existen.",
    ],
    ["juan.perez@escom.ipn.mx", "a@b.co", "usuario_1+listas@correo-x.com", "A.B-C@sub.dominio.org"],
    ["juan..perez@escom.ipn.mx", ".juan@x.mx", "juan@-x.mx", "juan@x", "juan@x.m", "@x.mx", "juan@@x.mx",
     "juan perez@x.mx", "juan@x..mx", "juan@x.mx."],
)

TELEFONO = Validador(
    "telefono", "Teléfono nacional (México, 10 dígitos)",
    "NDDDDDDDDD+ND(S+-)DDDD(S+-)DDDD+\\(ND\\)SDDDDSDDDD+NDD(S+-)DDD(S+-)DDDD+\\(NDD\\)SDDDSDDDD",
    {"D": DIGITOS, "N": "23456789", "S": " "},
    "diez dígitos que empiezan por 2-9, escritos seguidos, o agrupados 2-4-4 o 3-3-4 con espacios o guiones, "
    "o con la clave de larga distancia entre paréntesis.",
    "Plan Técnico Fundamental de Numeración (IFT, DOF 11-05-2018): marcación nacional uniforme a diez dígitos "
    "desde agosto de 2019, sin prefijos 01, 044 ni 045.",
    [
        "Quedan fuera: el prefijo internacional +52, los números con prefijos antiguos (01, 044, 045), las "
        "extensiones (ext. 123) y los números de servicios (911, 089, 01 800).",
        "Se aceptan (inválidos en la práctica): claves de larga distancia que no están asignadas (el plan "
        "sólo fija la forma del número, no la lista de claves) y mezclas de espacio y guion (55 1234-5678).",
    ],
    ["5512345678", "55 1234 5678", "55-1234-5678", "(55) 1234 5678", "331 234 5678", "(331) 234 5678",
     "331-234-5678"],
    ["1512345678", "0512345678", "551234567", "55123456789", "+52 55 1234 5678", "55 1234 56789",
     "(55)1234 5678", "55/1234/5678", "55 12 34 56 78", "5512 3456 78"],
)

_DIA = "(0P+(1+2)D+3(0+1))"
_MES = "(0P+1(0+1+2))"
_ANIO = "DDDD"

FECHA = Validador(
    "fecha", "Fecha (DD/MM/AAAA, DD-MM-AAAA o AAAA-MM-DD)",
    f"{_DIA}/{_MES}/{_ANIO}+{_DIA}-{_MES}-{_ANIO}+{_ANIO}-{_MES}-{_DIA}",
    {"D": DIGITOS, "P": "123456789"},
    "día de 01 a 31 y mes de 01 a 12, siempre con dos dígitos, y año de cuatro dígitos; en orden "
    "día-mes-año con / o con -, o en orden año-mes-día con - (ISO 8601).",
    "ISO 8601-1:2019, § 5.2.2.1 (fecha de calendario completa, formato extendido AAAA-MM-DD); el orden "
    "día/mes/año es el uso en México.",
    [
        "Se aceptan (inválidas en el calendario): 31/04/2026, 30/02/2026 y 29/02/2025, porque la expresión "
        "no relaciona el día con la longitud del mes ni con los años bisiestos. El lenguaje de las fechas "
        "válidas sí es regular (hay un número finito de combinaciones día-mes y la regla de los bisiestos "
        "depende de los dos últimos dígitos del año salvo en los siglos), pero su expresión es mucho más larga.",
        "Quedan fuera (válidas en ISO 8601): el formato básico 20261106, las fechas con hora "
        "(2026-11-06T10:00) y las semanas o días ordinales (2026-W45-5, 2026-310); también 6/11/2026 sin ceros.",
    ],
    ["06/11/2026", "31/12/1999", "01-01-2000", "2026-11-06", "2000-02-29", "29/02/2025"],
    ["6/11/2026", "32/01/2026", "00/01/2026", "06/13/2026", "06/00/2026", "06/11/26", "2026/11/06",
     "06-11/2026", "2026-11-6", "20261106", "06.11.2026", "2026-13-01"],
)

URL = Validador(
    "url", "URL (http o https)",
    f"http(λ+s)://{_ETIQUETA}(.{_ETIQUETA})*(λ+:DD*)(/P*)*(λ+?Q*)(λ+#Q*)",
    {"D": DIGITOS, "X": ALFANUMERICOS, "P": ALFANUMERICOS + "-_.~", "Q": ALFANUMERICOS + "-_.~=&/"},
    "esquema http o https, ://, un nombre de host de etiquetas alfanuméricas con guiones interiores, un "
    "puerto opcional, una ruta de segmentos con caracteres no reservados, una consulta opcional tras ? y un "
    "fragmento opcional tras #.",
    "RFC 3986, § 3 (componentes scheme, authority, path, query y fragment) y § 2.3 (caracteres no reservados "
    "ALPHA, DIGIT, -, ., _ y ~).",
    [
        "Quedan fuera (válidas según la norma): otros esquemas (ftp, mailto), la información de usuario "
        "(usuario:clave@), los hosts numéricos y IPv6 ([::1]), la codificación con porcentaje (%20) y los "
        "subdelimitadores ! $ ' ( ) * + , ; en la ruta o la consulta.",
        "Se aceptan (inválidas en la práctica): puertos mayores que 65535 (:99999), hosts sin dominio superior "
        "(http://localhost sí es válido, pero http://x-y también pasa) y segmentos de ruta vacíos consecutivos.",
    ],
    ["http://escom.ipn.mx", "https://www.escom.ipn.mx/", "https://x.mx:8080/a/b.html?q=1&r=2#top",
     "http://localhost:8550", "https://a-b.c/~u/", "http://x.mx/?#"],
    ["escom.ipn.mx", "htp://x.mx", "http:/x.mx", "http://", "http://-x.mx", "http://x.mx:p", "http://x mx",
     "https://x.mx/a b", "http://x.mx#f?q", "ftp://x.mx", "http://x.mx/%20", "http://x.mx?q=1?r"],
)

VALIDADORES = {v.clave: v for v in (CORREO, TELEFONO, FECHA, URL)}


@lru_cache(maxsize=None)
def _cadena(clave: str) -> CadenaExpresion:
    v = VALIDADORES[clave]
    return de_expresion_a_minimo(v.expresion, v.clases, nombre=v.clave)


# ----------------------------------------------------------------------
# Generación de cadenas de prueba
# ----------------------------------------------------------------------

def _etiqueta(r: random.Random) -> str:
    n = r.randint(1, 8)
    if n == 1:
        return r.choice(ALFANUMERICOS)
    medio = "".join(r.choice(ALFANUMERICOS + "-") for _ in range(n - 2))
    return r.choice(ALFANUMERICOS) + medio + r.choice(ALFANUMERICOS)


def _generar_valida(clave: str, r: random.Random) -> str:
    if clave == "correo":
        atomos = ["".join(r.choice(ALFANUMERICOS + "_-+") for _ in range(r.randint(1, 6)))
                  for _ in range(r.randint(1, 3))]
        dominio = ".".join(_etiqueta(r) for _ in range(r.randint(1, 3)))
        tld = "".join(r.choice(LETRAS) for _ in range(r.randint(2, 4)))
        return ".".join(atomos) + "@" + dominio + "." + tld
    if clave == "telefono":
        d = r.choice("23456789") + "".join(r.choice(DIGITOS) for _ in range(9))
        s = r.choice(" -")
        return r.choice([
            d, f"{d[:2]}{s}{d[2:6]}{s}{d[6:]}", f"({d[:2]}) {d[2:6]} {d[6:]}",
            f"{d[:3]}{s}{d[3:6]}{s}{d[6:]}", f"({d[:3]}) {d[3:6]} {d[6:]}",
        ])
    if clave == "fecha":
        dia, mes = r.randint(1, 31), r.randint(1, 12)
        anio = r.randint(0, 9999)
        return r.choice([f"{dia:02}/{mes:02}/{anio:04}", f"{dia:02}-{mes:02}-{anio:04}", f"{anio:04}-{mes:02}-{dia:02}"])
    if clave == "url":
        host = ".".join(_etiqueta(r) for _ in range(r.randint(1, 3)))
        puerto = f":{r.randint(0, 65535)}" if r.random() < 0.3 else ""
        ruta = "".join("/" + "".join(r.choice(ALFANUMERICOS + "-_.~") for _ in range(r.randint(0, 6)))
                       for _ in range(r.randint(0, 3)))
        consulta = "?" + "".join(r.choice(ALFANUMERICOS + "-_.~=&/") for _ in range(r.randint(0, 8))) if r.random() < 0.4 else ""
        frag = "#" + "".join(r.choice(ALFANUMERICOS + "-_.~=&/") for _ in range(r.randint(0, 5))) if r.random() < 0.3 else ""
        return "http" + r.choice(["", "s"]) + "://" + host + puerto + ruta + consulta + frag
    raise KeyError(clave)


_RUIDO = " .@/:-_()+#?=&~%!,;'\"[]{}áéíñ\t"


def _mutar(w: str, r: random.Random, alfabeto: list[str]) -> str:
    """Una alteración al azar: borrar, insertar, cambiar o duplicar un carácter, recortar o pegar ruido."""
    tipo = r.randint(0, 6)
    i = r.randrange(len(w) + 1)
    extra = r.choice(alfabeto + list(_RUIDO))
    if tipo == 0 and w:
        return w[:i] + w[i + 1:]
    if tipo == 1:
        return w[:i] + extra + w[i:]
    if tipo == 2 and w:
        return w[:i] + extra + w[i + 1:]
    if tipo == 3 and w:
        return w[:i] + w[i:i + 1] + w[i:]
    if tipo == 4 and w:
        return w[: r.randint(0, len(w) - 1)]
    if tipo == 5:
        return w + extra
    if w:
        j = r.randrange(len(w))
        return w[:j] + w[j:j + 1] + w[j:]
    return extra


def ejemplos(clave: str, cuantas_validas=300, cuantas_invalidas=300, semilla=2026) -> tuple[list[str], list[str]]:
    """Conjunto de prueba reproducible: cadenas válidas construidas pieza por pieza según la definición del
    formato, y cadenas inválidas obtenidas mutando válidas (una o dos alteraciones) o con ruido aleatorio,
    hasta reunir las que re.fullmatch rechaza. Siempre incluye los ejemplos fijos del validador."""
    v = VALIDADORES[clave]
    r = random.Random(f"{semilla}-{clave}")
    alfabeto = v.alfabeto()
    validas = list(v.validas)
    while len(validas) < cuantas_validas:
        w = _generar_valida(clave, r)
        if w not in validas:
            validas.append(w)
    invalidas = list(v.invalidas)
    while len(invalidas) < cuantas_invalidas:
        if r.random() < 0.8:
            w = _mutar(r.choice(validas), r, alfabeto)
            if r.random() < 0.3:
                w = _mutar(w, r, alfabeto)
        else:
            w = "".join(r.choice(alfabeto + list(_RUIDO)) for _ in range(r.randint(0, 25)))
        if not v.valida_con_re(w) and w not in invalidas:
            invalidas.append(w)
    return validas, invalidas
