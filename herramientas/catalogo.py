"""Catálogo de la Práctica 2: todos los ejercicios de la Lista 2 (94-150) y de la Lista 3 (151-263).

Cada ``Ejercicio`` lleva su clasificación (AFD, AFND, AFND-λ o ninguna), la
justificación de una línea que pide el apartado 2.1, el enunciado y sus
``Pieza``s: los autómatas que lo resuelven. Cada pieza tiene un oráculo, una
definición del lenguaje escrita a partir del enunciado e independiente del
autómata, contra la que se verifica el archivo (herramientas/generar.py).

Los ejercicios con asterisco ya se entregaron en la Práctica 1; sus .jff se
conservan (se copiaron con importar_p1.py) y aquí se reutilizan su diseño y
su oráculo, que vienen de herramientas/practica1.py.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

import practica1 as p1
from automata import Automata
from construir import afd, busqueda, regex, tabla, thompson

AFD_, AFND_, LAMBDA_, NINGUNA = "AFD", "AFND", "AFND-λ", "Ninguna"
CARPETA = {AFD_: "lista2-afd", AFND_: "lista3-afnd", LAMBDA_: "lista3-afnd-lambda"}

S1, S2, S3 = "012", "abc01", "ab"


@dataclass
class Pieza:
    archivo: str
    titulo: str
    diseno: str
    automata: Automata | None = None  # None: el .jff ya existe (Práctica 1)
    oraculo: object = None  # función w -> bool, o el nombre de otra pieza
    significado: dict = field(default_factory=dict)
    lambda_razon: str = ""  # para AFND-λ: por qué y dónde van las transiciones λ
    convertir: bool = True  # si se convierte a AFD en automatas/conversiones
    origen: str = ""  # archivo de la Práctica 1 del que se copió el .jff


@dataclass
class Ejercicio:
    num: str
    lista: int
    seccion: str
    justificacion: str
    enunciado: str
    piezas: list = field(default_factory=list)
    notas: str = ""
    practica1: bool = False

    @property
    def carpeta(self):
        return CARPETA.get(self.seccion)

    @property
    def orden(self):
        m = re.search(r"\d+", self.num)
        return (int(m.group()), self.num)


EJERCICIOS: list[Ejercicio] = []


def ej(*args, **kw):
    e = Ejercicio(*args, **kw)
    EJERCICIOS.append(e)
    return e


# ======================================================================
# Utilidades de oráculos
# ======================================================================

def traslapadas(w, p):
    return sum(w.startswith(p, i) for i in range(len(w)))


def disjuntas(w, p, q):
    """Hay una ocurrencia de p y una de q que no comparten posiciones."""
    ip = [i for i in range(len(w)) if w.startswith(p, i)]
    iq = [i for i in range(len(w)) if w.startswith(q, i)]
    return any(i + len(p) <= j or j + len(q) <= i for i in ip for j in iq)


def entero(w, con_signo=False):
    if con_signo and w[:1] in ("+", "-"):
        w = w[1:]
    return re.fullmatch(r"0|[1-9][0-9]*", w) is not None


# ======================================================================
# LISTA 2 — problemas 94-150
# ======================================================================

def _l2_p1(num):
    return [e for e in p1.L2 if e[0] == num]


def p1_afd(num, sufijo="", seccion=AFD_, justificacion=None):
    """Ejercicio de la Lista 2 ya resuelto en la Práctica 1."""
    entradas = _l2_p1(num)
    piezas = []
    for problema, archivo, enunciado, diseno, oraculo in entradas:
        numero = int(re.match(r"\d+", problema).group())
        extra = archivo.replace(f"ejercicio_{numero:03d}", "")
        nombre = f"L2-{numero:03d}{extra.replace('_', '-')}"
        piezas.append(Pieza(nombre, enunciado, diseno, None, oraculo, origen=f"lista2-afd/{archivo}"))
    return piezas


ESTRELLA_AFD = "El enunciado pide un AFD: δ total, un único estado activo y sin transiciones λ."

def nueva(archivo, titulo, diseno, resultado, oraculo, **kw):
    """Pieza construida con afd()/busqueda(): resultado = (autómata, significados)."""
    aut, signif = resultado if isinstance(resultado, tuple) else (resultado, {})
    aut.nombre = archivo
    return Pieza(archivo, titulo, diseno, aut, oraculo, signif, **kw)


ej("94", 2, AFD_, ESTRELLA_AFD + " Basta recordar si el primer símbolo fue 1 y si el último es 2.",
   "Las palabras de Σ₁ = {0,1,2} que comienzan con 1 y terminan con 2.",
   [nueva(
    "L2-094", "AFD",
    "El estado guarda si el prefijo leído es válido (empezó con 1) y si el último símbolo es 2. "
    "Si el primer símbolo no es 1, el rechazo es definitivo.",
    afd(S1, "inicio", lambda s, a: (None if a != "1" else "ok-no2") if s == "inicio" else ("ok-2" if a == "2" else "ok-no2"),
        lambda s: s == "ok-2",
        {"inicio": "no se ha leído nada", "ok-no2": "empezó con 1 y el último símbolo no es 2",
         "ok-2": "empezó con 1 y el último símbolo es 2"}.get),
    lambda w: w[:1] == "1" and w[-1:] == "2")])

ej("95", 2, AFD_, ESTRELLA_AFD + " Solo se cuenta la longitud hasta 5.",
   "Las palabras de Σ₁ que tienen longitud 4.",
   [nueva("L2-095", "AFD", "Contador de longitud saturado: qᵢ = se han leído i símbolos (i ≤ 4); a partir del quinto "
          "símbolo el estado de rechazo es absorbente. Solo q4 acepta.",
          afd(S1, 0, lambda i, a: i + 1 if i < 4 else None, lambda i: i == 4, lambda i: f"se han leído {i} símbolos"),
          lambda w: len(w) == 4)])

ej("96", 2, AFD_, ESTRELLA_AFD + " Combina la verificación del prefijo con un contador de longitud.",
   "Las palabras de Σ₁ con prefijo 20 y longitud 4.",
   [nueva("L2-096", "AFD", "Las dos primeras posiciones exigen 2 y luego 0 (cualquier otro símbolo lleva al rechazo); "
          "las posiciones 3 y 4 aceptan cualquier símbolo. Solo acepta el estado de longitud exacta 4.",
          afd(S1, 0, lambda i, a: (1 if a == "2" else None) if i == 0 else (2 if a == "0" else None) if i == 1
              else (i + 1 if i < 4 else None), lambda i: i == 4,
              lambda i: ["inicio", "se leyó 2", "se leyó el prefijo 20", "20 y un símbolo más", "20 y dos símbolos más: longitud 4"][i]),
          lambda w: len(w) == 4 and w.startswith("20"))])

ej("97", 2, AFD_, ESTRELLA_AFD + " Contador módulo 3 de la longitud.", "Palabras de Σ₁ cuya longitud es múltiplo de 3.",
   p1_afd("97"), practica1=True)

ej("98", 2, AFD_, ESTRELLA_AFD + " Búsqueda de sufijo con función de fallo.",
   "Las palabras de Σ₁ que terminan con la cadena 00102.",
   [nueva("L2-098", "AFD", "Autómata de búsqueda del sufijo 00102 (función de fallo, como en el algoritmo KMP): el estado qⱼ "
          "indica que los últimos j símbolos son el prefijo más largo de 00102 que es sufijo de lo leído. q5 acepta, pero "
          "no es absorbente: si llegan más símbolos se retrocede según la función de fallo.",
          busqueda("00102", S1, "termina"), lambda w: w.endswith("00102"))])

ej("99", 2, AFD_, ESTRELLA_AFD + " Búsqueda de sufijo con función de fallo.", "Palabras de Σ₁ que terminan con 001001.",
   p1_afd("99"), practica1=True)

ej("100", 2, AFD_, ESTRELLA_AFD + " Solo se revisan las dos primeras posiciones.",
   "Las palabras de Σ₂ = {a,b,c,0,1} tales que el primer símbolo es una letra y el segundo es un dígito.",
   [nueva("L2-100", "AFD", "q0 espera una letra; q1, un dígito; q2 confirma el prefijo y acepta todo lo que siga "
          "(absorbente). Un símbolo del tipo equivocado lleva al rechazo absorbente. Se exige longitud ≥ 2, porque "
          "una palabra de longitud 1 no tiene segundo símbolo.",
          afd(S2, 0, lambda i, a: (1 if a in "abc" else None) if i == 0 else (2 if a in "01" else None) if i == 1 else 2,
              lambda i: i == 2, lambda i: ["inicio", "primer símbolo: letra", "letra seguida de dígito"][i]),
          lambda w: len(w) >= 2 and w[0] in "abc" and w[1] in "01")])

ej("101", 2, AFD_, ESTRELLA_AFD + " Búsqueda de subcadena con estado final absorbente.",
   "Las palabras de Σ₃ = {a,b} que contienen la cadena aba.",
   [nueva("L2-101", "AFD", "Búsqueda de aba: qⱼ = j símbolos del patrón ya coinciden. Tras una a con ab (q2 → q3) se "
          "acepta y q3 es absorbente. En q2, una b regresa a q0 porque abb no tiene sufijo que sea prefijo de aba.",
          busqueda("aba", S3), lambda w: "aba" in w)])

ej("102", 2, AFD_, ESTRELLA_AFD + " Búsqueda de subcadena.", "Palabras de Σ₃ que contienen abbbab.", p1_afd("102"), practica1=True)
ej("103", 2, AFD_, ESTRELLA_AFD + " Búsqueda de subcadena.", "Palabras de Σ₃ que contienen aabbba.", p1_afd("103"), practica1=True)

ej("104", 2, AFD_, ESTRELLA_AFD + " Verificación de prefijo.",
   "Las palabras de Σ₃ que inician con la cadena abbab.",
   [nueva("L2-104", "AFD", "Cadena lineal que compara el prefijo símbolo por símbolo; el primer desacuerdo lleva al "
          "rechazo absorbente. Al completar abbab, el estado de aceptación es absorbente.",
          busqueda("abbab", S3, "empieza"), lambda w: w.startswith("abbab"))])

ej("105", 2, AFD_, ESTRELLA_AFD + " Búsqueda de sufijo con función de fallo.",
   "Las palabras de Σ₃ que terminan con la cadena abaa.",
   [nueva("L2-105", "AFD", "Búsqueda del sufijo abaa con función de fallo; q4 acepta y, si llega otro símbolo, se "
          "retrocede (con a a q1, porque solo la última a sirve como inicio; con b a q2, porque ab es prefijo).",
          busqueda("abaa", S3, "termina"), lambda w: w.endswith("abaa"))])

ej("106", 2, AFD_, ESTRELLA_AFD + " Búsqueda de subcadena.", "Palabras de Σ₁ que incluyen 1101001.", p1_afd("106"), practica1=True)
ej("107", 2, AFD_, ESTRELLA_AFD + " Producto de dos búsquedas.", "Palabras de Σ₁ con 0101 y con 021.", p1_afd("107"), practica1=True)


def _afd_desde(er, alfabeto):
    """AFD mínimo de una expresión regular: Thompson → subconjuntos → Hopcroft."""
    return thompson(er, alfabeto).subconjuntos().minimizar().numerar()


_S2_ = "(a+b+c+0+1)*"
ej("108", 2, AFD_, ESTRELLA_AFD + " Producto de búsquedas que exige ocurrencias disjuntas.",
   "Las palabras de Σ₂ que incluyen al menos una vez abbcb y al menos una vez cbaabb, sin traslape "
   "(abbcbaabb no pertenece).",
   [nueva("L2-108", "AFD", "El lenguaje es la unión de Σ*·abbcb·Σ*·cbaabb·Σ* y Σ*·cbaabb·Σ*·abbcb·Σ*: una ocurrencia completa "
          "de un patrón seguida, sin compartir símbolos, de una del otro. Se construyó el AFND-λ de esa unión (el del "
          "problema 162-188 correspondiente), se determinizó por subconjuntos y se minimizó con Hopcroft. A diferencia "
          "del 109, al completar un patrón la búsqueda del otro recomienza desde cero en lugar de reutilizar el traslape.",
          _afd_desde(f"{_S2_}abbcb{_S2_}cbaabb{_S2_}+{_S2_}cbaabb{_S2_}abbcb{_S2_}", S2),
          lambda w: disjuntas(w, "abbcb", "cbaabb"))])

ej("109", 2, AFD_, ESTRELLA_AFD + " Producto de búsquedas con traslape.", "Σ₂: abbcb y cbaabb, con traslape.", p1_afd("109"), practica1=True)


def _cuenta_01(s, a):
    ultimo0, n = s
    if ultimo0 and a == "1":
        n = min(n + 1, 4)
    return (a == "0", n)


ej("110", 2, AFD_, ESTRELLA_AFD + " Contador saturado de ocurrencias de 01.",
   "Las palabras de Σ₁ que contienen exactamente tres veces la subcadena 01.",
   [nueva("L2-110", "AFD", "El estado es el par (¿el último símbolo fue 0?, ocurrencias de 01 vistas, saturadas en 4). 01 no "
          "puede traslaparse consigo mismo, así que cada 1 precedido de 0 cuenta una ocurrencia nueva. Acepta con "
          "contador 3; el contador 4 representa «más de tres» y es de rechazo.",
          afd(S1, (False, 0), _cuenta_01, lambda s: s[1] == 3,
              lambda s: f"{min(s[1], 4) if s[1] < 4 else 'más de 3'} ocurrencias; último símbolo {'0' if s[0] else 'distinto de 0'}"),
          lambda w: traslapadas(w, "01") == 3)])

ej("111", 2, AFD_, ESTRELLA_AFD + " Contador de ocurrencias.", "Exactamente tres veces 01002.", p1_afd("111"), practica1=True)
ej("112", 2, AFD_, ESTRELLA_AFD + " Contador sin traslape.", "Dos veces 010 sin traslape.", p1_afd("112"), practica1=True)
ej("113", 2, AFD_, ESTRELLA_AFD + " Contador con traslape.", "Dos veces 010 con traslape.", p1_afd("113"), practica1=True)

NAT = ("Se toma ℕ = {1, 2, …}, la convención de la Tarea 2 y de la Práctica 1 (problema 121); con ℕ = {0, 1, …} "
       "bastaría con volver de aceptación los estados de los bloques que pueden ser vacíos.")

ej("114", 2, AFD_, ESTRELLA_AFD + " Dos fases consecutivas: primero a, después b.",
   "L = {w ∈ Σ₃* : w = aⁿbᵐ, m, n ∈ ℕ}.",
   [nueva("L2-114", "AFD", "q0: inicio; q1: se han leído a; q2: se leyó al menos una b después de las a (acepta). Una a "
          "después de una b, o una b al inicio, llevan al rechazo absorbente. " + NAT,
          afd(S3, 0, lambda i, a: {(0, "a"): 1, (1, "a"): 1, (1, "b"): 2, (2, "b"): 2}.get((i, a)), lambda i: i == 2,
              lambda i: ["inicio", "bloque de a", "bloque de b tras las a"][i]),
          regex("a(a)*b(b)*"))])

ej("115", 2, AFD_, ESTRELLA_AFD + " Ciclo de longitud 3 que reconoce abc.",
   "L = {w ∈ Σ₂* : w = (abc)ⁿ, n ∈ ℕ}.",
   [nueva("L2-115", "AFD", "Ciclo q0 -a→ q1 -b→ q2 -c→ q3 -a→ q1: q3 indica que se cerró un bloque abc y es de "
          "aceptación. Cualquier otro símbolo lleva al rechazo absorbente. " + NAT,
          afd(S2, 0, lambda i, a: {(0, "a"): 1, (1, "b"): 2, (2, "c"): 3, (3, "a"): 1}.get((i, a)), lambda i: i == 3,
              lambda i: ["inicio", "se leyó a", "se leyó ab", "se cerró un bloque abc"][i]),
          regex("abc(abc)*"))])

ej("116", 2, NINGUNA,
   "Ningún autómata finito lo reconoce: L no es regular (lema de bombeo), así que no cabe en ninguna de las tres secciones.",
   "L = {w ∈ Σ₂* : w = aⁿbᵐcⁿ⁺¹, m, n ∈ ℕ}.",
   notas="""**L no es regular.** Supóngase que lo es y sea p la constante del lema de bombeo. La palabra
z = aᵖ b cᵖ⁺¹ pertenece a L y |z| ≥ p. Toda descomposición z = uvw con |uv| ≤ p y |v| ≥ 1 tiene
v = aᵏ con k ≥ 1, porque los primeros p símbolos son a. Entonces uv⁰w = aᵖ⁻ᵏ b cᵖ⁺¹ tiene p − k a
y p + 1 c, y p + 1 ≠ (p − k) + 1; luego uv⁰w ∉ L, lo que contradice el lema. Por lo tanto ningún
AFD, AFND ni AFND-λ reconoce L (los tres reconocen exactamente los lenguajes regulares).

La misma conclusión sale del teorema de Myhill-Nerode: las palabras a, a², a³, … son distinguibles
dos a dos (aⁱ b cⁱ⁺¹ ∈ L pero aʲ b cⁱ⁺¹ ∉ L si i ≠ j), así que la relación tiene índice infinito.
Reconocer L exige contar las a sin cota, lo que hace un autómata de pila (Unidad II): apila una
marca por cada a, ignora las b y desapila una por cada c, aceptando cuando sobra exactamente una c.""")

ej("117", 2, AFD_, ESTRELLA_AFD + " Cuatro fases consecutivas a, b, a, b.",
   "L = {w ∈ Σ₃* : w = aⁿbᵐaᵖbᵠ, m, n, p, q ∈ ℕ}.",
   [nueva("L2-117", "AFD", "Una fase por bloque: q1 (a⁺), q2 (a⁺b⁺), q3 (a⁺b⁺a⁺), q4 (a⁺b⁺a⁺b⁺, acepta). Cada estado "
          "tiene un lazo con el símbolo de su bloque y pasa al siguiente con el otro símbolo; una quinta alternancia "
          "lleva al rechazo absorbente. " + NAT,
          afd(S3, 0, lambda i, a: ({(0, "a"): 1, (1, "a"): 1, (1, "b"): 2, (2, "b"): 2, (2, "a"): 3, (3, "a"): 3,
                                     (3, "b"): 4, (4, "b"): 4}.get((i, a))), lambda i: i == 4,
              lambda i: ["inicio", "bloque a⁺", "a⁺b⁺", "a⁺b⁺a⁺", "a⁺b⁺a⁺b⁺"][i]),
          regex("aa*bb*aa*bb*"))])

ej("118", 2, AFD_, ESTRELLA_AFD, "L = {w ∈ Σ₃ : w = a x ab y a}.", p1_afd("118"), practica1=True)


def _tras_aa(s, a):
    if s == 2:
        return 0 if a == "b" else None
    return (s + 1) if a == "a" else 0


ej("119", 2, AFD_, ESTRELLA_AFD + " Se recuerda la racha final de a (0, 1 o 2).",
   "Las palabras de Σ₃ tales que después de cada subcadena aa aparece una b.",
   [nueva("L2-119", "AFD", "Se interpreta que el símbolo inmediato a cada aa debe ser b; así, aaa no pertenece (su primer "
          "aa va seguido de a) y una palabra no puede terminar en aa. q0: el último símbolo no es a; q1: una a "
          "suelta; q2: aa pendiente, que exige b. Leer a en q2 lleva al rechazo absorbente.",
          afd(S3, 0, _tras_aa, lambda s: s in (0, 1),
              lambda s: ["sin a pendientes", "una a al final", "aa al final: falta la b"][s]),
          lambda w: all(w[i + 2:i + 3] == "b" for i in range(len(w) - 1) if w[i:i + 2] == "aa"))])

for n in ("120", "121", "122", "123", "124"):
    ej(n, 2, AFD_, ESTRELLA_AFD, _l2_p1(n)[0][2], p1_afd(n), practica1=True)

# 125-127: preguntas teóricas, con un ejemplo construido sobre el AFD del problema 139.
_PAR = Automata("01", ["q0", "q1"], "q0", ["q0"],
                [("q0", "0", "q1"), ("q0", "1", "q0"), ("q1", "0", "q0"), ("q1", "1", "q1")])


def _variante(nombre, finales):
    m = _PAR.copia(nombre)
    m.aceptacion = set(finales)
    return m


_SIG_PAR = {"q0": "número par de ceros", "q1": "número impar de ceros"}

ej("125", 2, AFD_, "Pregunta sobre un AFD (δ total); se ilustra con el AFD del 139 y su complemento.",
   "Sea A = (Q, Σ, δ, A₀, F) un AFD. ¿Cuál es el lenguaje de A' = (Q, Σ, δ, A₀, Q \\ F)?",
   [Pieza("L2-125-A", "AFD A del ejemplo (problema 139: par de ceros)", "Ejemplo: el AFD del problema 139.",
          _variante("L2-125-A", ["q0"]), lambda w: w.count("0") % 2 == 0, _SIG_PAR),
    Pieza("L2-125-complemento", "A' = (Q, Σ, δ, A₀, Q \\ F)", "Mismos estados y transiciones; se intercambian los estados de "
          "aceptación y de no aceptación.", _variante("L2-125-complemento", ["q1"]), lambda w: w.count("0") % 2 == 1, _SIG_PAR)],
   notas="""**Respuesta.** L(A') = Σ* \\ L(A), el complemento de L(A). Como δ es total, para cada w existe
exactamente un estado δ̂(A₀, w); w ∈ L(A') ⇔ δ̂(A₀, w) ∈ Q \\ F ⇔ δ̂(A₀, w) ∉ F ⇔ w ∉ L(A).
La hipótesis de que δ sea total es indispensable: en un AFND (o en un autómata con δ parcial)
intercambiar F y Q \\ F no da el complemento, porque una palabra puede tener caminos que terminan
dentro y fuera de F, o no tener ninguno. Por eso el ejemplo usa el AFD completo del problema 139:
el complemento de «número par de ceros» es «número impar de ceros».""")

ej("126", 2, AFD_, "Pregunta sobre un AFD; con F = ∅ ninguna palabra llega a un estado de aceptación.",
   "Sea A = (Q, Σ, δ, A₀, F) un AFD. ¿Cuál es el lenguaje del autómata si F = ∅?",
   [Pieza("L2-126", "AFD del 139 con F = ∅", "Mismo δ que el 139, sin estados de aceptación.",
          _variante("L2-126", []), lambda w: False, _SIG_PAR)],
   notas="**Respuesta.** L(A) = ∅: w ∈ L(A) exige δ̂(A₀, w) ∈ F, y F no tiene elementos. No es lo mismo que "
         "{λ}: el lenguaje vacío no contiene ni siquiera la cadena vacía. Por eso este autómata no tiene casos "
         "válidos: no existe ninguna cadena que acepte.")

ej("127", 2, AFD_, "Pregunta sobre un AFD; con F = Q y δ total toda palabra termina en un estado de aceptación.",
   "Sea A = (Q, Σ, δ, q₀, F) un AFD. ¿Cuál es el lenguaje del autómata si F = Q?",
   [Pieza("L2-127", "AFD del 139 con F = Q", "Mismo δ que el 139; los dos estados son de aceptación.",
          _variante("L2-127", ["q0", "q1"]), lambda w: all(c in "01" for c in w), _SIG_PAR)],
   notas="**Respuesta.** L(A) = Σ*: como δ es total, δ̂(q₀, w) existe para toda w ∈ Σ* y pertenece a Q = F. "
         "Si δ fuera parcial, L(A) sería el conjunto de palabras que no «se atoran», que puede ser menor que Σ*. "
         "Como el lenguaje es Σ*, las únicas cadenas inválidas posibles contienen símbolos fuera de Σ.")

ej("128", 2, AFD_, ESTRELLA_AFD + " Se cambia F de un AFD dado.", _l2_p1("128")[0][2] + " Se pide un AFD para L₂.",
   p1_afd("128"), practica1=True)

ej("129", 2, AFD_, "El enunciado da el AFD completo (δ total, un destino por par); solo se transcribe y se verifica.",
   "AFD M que acepta LM = {w ∈ {a,b}* : w no contiene tres b consecutivas}, dado por su tabla.",
   [Pieza("L2-129", "AFD dado en el enunciado",
          "Transcripción de la tabla. qᵢ = la racha actual de b tiene longitud i; q3 = ya hubo bbb (rechazo absorbente).",
          tabla("A", "ABC", "ab", "A: A B; B: A C; C: A D; D: D D")
          .renombrar({"A": "q0", "B": "q1", "C": "q2", "D": "q3"}, "L2-129"), lambda w: "bbb" not in w,
          {"q0": "racha de b de longitud 0", "q1": "racha de longitud 1", "q2": "racha de longitud 2", "q3": "ya apareció bbb"})])

ej("130", 2, AFD_, "El enunciado da el AFD completo; se transcribe y se corrige la descripción de su lenguaje.",
   "AFD M = ({q1,q2,q3}, {0,1}, δ, q1, {q2}) dado por su tabla; describir el lenguaje.",
   [Pieza("L2-130", "AFD dado en el enunciado",
          "Transcripción de la tabla. La descripción del enunciado («alternan entre estados hasta llegar a q2») es "
          "imprecisa; el lenguaje exacto es: w tiene al menos un 1 y después del último 1 hay un número par de 0. "
          "q1: aún no hay 1; q2: después del último 1 hay un número par de 0; q3: hay un número impar.",
          tabla("1", ["2"], "01", "1: 1 2; 2: 3 2; 3: 2 2").renombrar({"1": "q1", "2": "q2", "3": "q3"}, "L2-130"),
          lambda w: "1" in w and len(w) - 1 - w.rindex("1") >= 0 and (len(w) - 1 - w.rindex("1")) % 2 == 0,
          {"q1": "todavía no aparece un 1", "q2": "tras el último 1, número par de 0",
           "q3": "tras el último 1, número impar de 0"})],
   notas="Comprobación: 100 ∈ L (dos 0 tras el último 1) y 10 ∉ L (uno); 1001 ∈ L porque cuenta el último 1, y 0110 ∉ L.")

for n in ("131",):
    ej(n, 2, AFD_, ESTRELLA_AFD, _l2_p1(n)[0][2], p1_afd(n), practica1=True)

ej("132", 2, AFD_, ESTRELLA_AFD + " Un bloque de a y una sola b final.",
   "Diseñar un AFD para L = {aⁿb : n ≥ 0}.",
   [nueva("L2-132", "AFD", "q0 tiene un lazo con a (n ≥ 0 permite cero a); la b lleva a q1, el único de aceptación. "
          "Cualquier símbolo después de la b lleva al rechazo absorbente.",
          afd(S3, 0, lambda i, a: {(0, "a"): 0, (0, "b"): 1}.get((i, a)), lambda i: i == 1,
              lambda i: ["bloque de a (posiblemente vacío)", "se leyó la b final"][i]),
          regex("a*b"))])

ej("133", 2, AFD_, ESTRELLA_AFD, _l2_p1("133")[0][2], p1_afd("133"), practica1=True)

ej("134", 2, AFD_, ESTRELLA_AFD + " Búsqueda de subcadena (aplicación a búsqueda de texto).",
   "L(M) = {w | w ∈ {a,b,c}* y w contiene el patrón abac}.",
   [nueva("L2-134", "AFD", "Búsqueda de abac con función de fallo: en q3 (aba) una b regresa a q2 porque ab es prefijo "
          "del patrón; una a regresa a q1. q4 es de aceptación y absorbente.",
          busqueda("abac", "abc"), lambda w: "abac" in w)])

ej("135", 2, AFD_, ESTRELLA_AFD, _l2_p1("135")[0][2], p1_afd("135"), practica1=True)

ej("136", 2, AFD_, ESTRELLA_AFD + " Dos fases, cada una con al menos un símbolo.",
   "Dado Σ = {a,b}, construir un AFD para L = {aᵐbⁿ : m, n > 0}.",
   [nueva("L2-136", "AFD", "Igual que el 114 (allí ℕ empieza en 1): q1 = al menos una a; q2 = al menos una b tras ellas "
          "(acepta); el orden inverso lleva al rechazo absorbente.",
          afd(S3, 0, lambda i, a: {(0, "a"): 1, (1, "a"): 1, (1, "b"): 2, (2, "b"): 2}.get((i, a)), lambda i: i == 2,
              lambda i: ["inicio", "bloque de a", "bloque de b tras las a"][i]),
          regex("aa*bb*"))])

ej("137", 2, AFD_, ESTRELLA_AFD, _l2_p1("137")[0][2], p1_afd("137"), practica1=True)

ej("138", 2, AFD_, ESTRELLA_AFD + " Contador módulo 3 de las b.",
   "AFD sobre {a,b} que acepta las palabras cuyo número de b es divisible entre tres.",
   [nueva("L2-138", "AFD", "qᵢ = el número de b leídas es ≡ i (mód 3). La a no cambia el estado (lazo) y la b avanza el "
          "contador. q0 es inicial y de aceptación porque 0 es divisible entre 3.",
          afd(S3, 0, lambda i, a: (i + (a == "b")) % 3, lambda i: i == 0, lambda i: f"#b ≡ {i} (mód 3)"),
          lambda w: w.count("b") % 3 == 0)])

ej("139", 2, AFD_, ESTRELLA_AFD, _l2_p1("139")[0][2], p1_afd("139"), practica1=True)

ej("140", 2, AFD_, ESTRELLA_AFD + " Contadores de paridad (uno para a; un par para b).",
   "Autómata finito sobre {0,1} para: a) un número impar de ceros; b) un número par de ceros y un número par de unos.",
   [nueva("L2-140a", "a) Número impar de ceros", "q0 = par de ceros, q1 = impar (acepta); el 0 cambia de estado y el 1 no.",
          afd("01", 0, lambda i, a: (i + (a == "0")) % 2, lambda i: i == 1, lambda i: ["par de ceros", "impar de ceros"][i]),
          lambda w: w.count("0") % 2 == 1),
    nueva("L2-140b", "b) Par de ceros y par de unos", "El estado es el par (paridad de ceros, paridad de unos); el 0 cambia "
          "la primera componente y el 1 la segunda. Solo (par, par) acepta. Es el mismo autómata del problema 133.",
          afd("01", (0, 0), lambda s, a: ((s[0] + (a == "0")) % 2, (s[1] + (a == "1")) % 2), lambda s: s == (0, 0),
              lambda s: f"{'par' if s[0] == 0 else 'impar'} de ceros, {'par' if s[1] == 0 else 'impar'} de unos"),
          lambda w: w.count("0") % 2 == 0 and w.count("1") % 2 == 0)])

ej("141", 2, AFD_, ESTRELLA_AFD, _l2_p1("141")[0][2], p1_afd("141"), practica1=True)

ej("142", 2, AFD_, ESTRELLA_AFD + " Ciclo de longitud 2 que reconoce ab.",
   "Autómata finito sobre {a,b} para: a) LA = (ab)* = {(ab)ⁿ : n ≥ 0}; b) LB = {(ab)ⁿ : n ≥ 1}.",
   [nueva("L2-142a", "a) (ab)*", "El enunciado añade «la cadena vacía no es aceptada», lo que contradice n ≥ 0: (ab)⁰ = λ. "
          "Se sigue la definición formal, así que λ se acepta: q0 es inicial y de aceptación; q0 -a→ q1 -b→ q0.",
          afd(S3, 0, lambda i, a: {(0, "a"): 1, (1, "b"): 0}.get((i, a)), lambda i: i == 0,
              lambda i: ["se han cerrado bloques ab completos", "falta la b del bloque"][i]),
          regex("(ab)*")),
    nueva("L2-142b", "b) (ab)⁺", "Con n ≥ 1, λ queda fuera: q0 inicial no acepta; q2 = se cerró al menos un bloque ab.",
          afd(S3, 0, lambda i, a: {(0, "a"): 1, (1, "b"): 2, (2, "a"): 1}.get((i, a)), lambda i: i == 2,
              lambda i: ["inicio", "falta la b del bloque", "se cerró al menos un bloque ab"][i]),
          regex("ab(ab)*"))])

ej("143", 2, AFD_, "La figura (a) es un AFD; la (b) es un AFND (dos destinos con b en q1) y se clasifica en esa sección.",
   _l2_p1("143a")[0][2] + " / " + _l2_p1("143b")[0][2], p1_afd("143a"), practica1=True)
ej("143b", 2, AFND_, "La figura (b) tiene dos transiciones con b desde q1 y ninguna con b desde q0: es no determinista.",
   _l2_p1("143b")[0][2], p1_afd("143b"), practica1=True)

ej("144", 2, AFD_, ESTRELLA_AFD + " Cinco lenguajes de prefijo, sufijo, subcadena y formato numérico.",
   "Autómata finito para: a) cadenas que comienzan con a; b) comienzan con a y terminan con b; c) contienen aaa; "
   "d) el conjunto de números enteros; e) el conjunto de números enteros con signo.",
   [nueva("L2-144a", "a) Comienzan con a", "El primer símbolo decide: a lleva a un estado de aceptación absorbente y b al "
          "rechazo absorbente.", busqueda("a", S3, "empieza"), lambda w: w.startswith("a")),
    nueva("L2-144b", "b) Comienzan con a y terminan con b", "Tras una a inicial, el estado recuerda el último símbolo; acepta "
          "si es b. Una b inicial lleva al rechazo absorbente.",
          afd(S3, "inicio", lambda s, a: (("ult-a" if a == "a" else None) if s == "inicio" else ("ult-" + a)),
              lambda s: s == "ult-b", {"inicio": "inicio", "ult-a": "empezó con a; último símbolo a",
                                        "ult-b": "empezó con a; último símbolo b"}.get),
          lambda w: w.startswith("a") and w.endswith("b")),
    nueva("L2-144c", "c) Contienen aaa", "Búsqueda de aaa: qᵢ = racha actual de a (i < 3); q3 absorbente de aceptación.",
          busqueda("aaa", S3), lambda w: "aaa" in w),
    nueva("L2-144d", "d) Números enteros (Σ = {0,…,9})", "Se toma la representación decimal sin ceros a la izquierda: 0, o "
          "un dígito de 1 a 9 seguido de cualquier cantidad de dígitos. q1 = se leyó «0» (otro dígito lo invalida); "
          "q2 = número que empieza con 1-9 (absorbe dígitos). λ no es un número.",
          afd("0123456789", "inicio", lambda s, a: ("cero" if a == "0" else "num") if s == "inicio" else
              (None if s == "cero" else "num"), lambda s: s in ("cero", "num"),
              {"inicio": "nada leído", "cero": "se leyó el número 0", "num": "número sin ceros a la izquierda"}.get),
          entero),
    nueva("L2-144e", "e) Enteros con signo (Σ = {0,…,9,+,−})", "Como d), con un signo opcional al principio: q1 = se leyó "
          "el signo y falta al menos un dígito. Un signo en otra posición lleva al rechazo absorbente.",
          afd("0123456789+-", "inicio", lambda s, a: (("signo" if a in "+-" else ("cero" if a == "0" else "num"))
                                                         if s == "inicio" else
                                                         (None if a in "+-" else ("cero" if a == "0" else "num"))
                                                         if s == "signo" else
                                                         (None if s == "cero" or a in "+-" else "num")),
              lambda s: s in ("cero", "num"),
              {"inicio": "nada leído", "signo": "se leyó el signo", "cero": "el número 0 (con o sin signo)",
               "num": "número sin ceros a la izquierda"}.get),
          lambda w: entero(w, True))])

ej("145", 2, AFD_, ESTRELLA_AFD, _l2_p1("145")[0][2], p1_afd("145"), practica1=True)

ej("146", 2, AFD_, ESTRELLA_AFD + " El estado guarda el residuo módulo 5 del valor leído.",
   "AFD que lee un número binario de izquierda a derecha e identifica los múltiplos de 5.",
   [nueva("L2-146", "AFD", "Al leer el bit b el valor pasa de v a 2v + b, así que basta el residuo: r' = (2r + b) mod 5. "
          "q0 (residuo 0) es inicial y de aceptación; λ representa el 0, igual que en el problema 145 de la Práctica 1.",
          afd("01", 0, lambda r, a: (2 * r + int(a)) % 5, lambda r: r == 0, lambda r: f"valor ≡ {r} (mód 5)"),
          lambda w: p1.binario_msb(w, 5))])

for n in ("147", "148", "149", "150"):
    ej(n, 2, AFD_, ESTRELLA_AFD, _l2_p1(n)[0][2], p1_afd(n), practica1=True)


# ======================================================================
# LISTA 3 — problemas 151-263
# ======================================================================

def p1_l3(entradas, nombres):
    """Piezas de la Lista 3 ya resueltas en la Práctica 1; ``nombres`` traduce el archivo viejo al nuevo."""
    return [Pieza(nombres[archivo], enunciado, diseno, None, oraculo, origen=f"lista3-afn/{archivo}")
            for _, archivo, enunciado, diseno, oraculo in entradas if archivo in nombres]


def _l3(num):
    return [e for e in p1.L3 if e[0] == num]


SIMPLIFICACION = "AFD dado por tabla (δ total) que se simplifica; la sección AFD es la que corresponde."
for n in ("151", "152", "153", "154", "155", "156", "157"):
    nombres = {e[1]: "L3-" + e[1].replace("ej", "").replace("_", "-").replace("-sin-inaccesibles", "-accesibles")
               for e in _l3(n)}
    piezas = p1_l3(_l3(n), nombres)
    for pz in piezas:
        if isinstance(pz.oraculo, str):
            pz.oraculo = nombres[pz.oraculo]
    ej(n, 3, AFD_, SIMPLIFICACION, _l3(n)[0][2], piezas, practica1=True)

for n in ("158", "159", "160", "161"):
    ej(n, 3, AFND_, "Los diagramas dejan transiciones indefinidas (δ(q, a) = ∅); la lista los presenta como AFN.",
       _l3(n)[0][2], p1_l3(_l3(n), {f"ej{n}": f"L3-{n}"}), practica1=True)

# 162-188: un AFN para cada problema 94-123 de la Lista 2.
_P1_AFN = {e[0]: e for e in p1.L3_AFN}
AFN_JUST = "El ejercicio pide un AFN; el no determinismo (o δ parcial) simplifica el diagrama del AFD."


def afn(estados, inicial, finales, trans, alfabeto):
    t = []
    for tr in trans.split(";"):
        q, simbolos, p = tr.split()
        for a in ("" if simbolos == "λ" else simbolos.replace("Σ", alfabeto)) or [""]:
            t.append((q, a, p))
    return Automata(alfabeto, estados.split(), inicial, finales.split(), t).validar()


NUEVOS_AFN = {
    "94": (AFND_, "q0 lee el 1 inicial; q1 consume cualquier símbolo y adivina cuál es el 2 final, que lleva a q2 sin salidas.",
           afn("q0 q1 q2", "q0", "q2", "q0 1 q1; q1 Σ q1; q1 2 q2", S1), lambda w: w[:1] == "1" and w[-1:] == "2"),
    "95": (AFND_, "Cadena de cuatro transiciones con cualquier símbolo; sin estado de rechazo (δ parcial): una quinta letra "
                  "no tiene transición y el cómputo muere.",
           afn("q0 q1 q2 q3 q4", "q0", "q4", "q0 Σ q1; q1 Σ q2; q2 Σ q3; q3 Σ q4", S1), lambda w: len(w) == 4),
    "96": (AFND_, "Cadena 2, 0, Σ, Σ sin estado de rechazo; δ parcial.",
           afn("q0 q1 q2 q3 q4", "q0", "q4", "q0 2 q1; q1 0 q2; q2 Σ q3; q3 Σ q4", S1), lambda w: len(w) == 4 and w.startswith("20")),
    "98": (AFND_, "q0 con lazo adivina dónde empieza el sufijo 00102; el resto es una cadena lineal sin salidas al final. "
                  "Sustituye la función de fallo del AFD por la adivinanza.",
           afn("q0 q1 q2 q3 q4 q5", "q0", "q5", "q0 Σ q0; q0 0 q1; q1 0 q2; q2 1 q3; q3 0 q4; q4 2 q5", S1),
           lambda w: w.endswith("00102")),
    "100": (AFND_, "Letra, dígito y un lazo final con todo Σ₂; sin estado de rechazo.",
            afn("q0 q1 q2", "q0", "q2", "q0 abc q1; q1 01 q2; q2 Σ q2", S2),
            lambda w: len(w) >= 2 and w[0] in "abc" and w[1] in "01"),
    "101": (AFND_, "q0 con lazo adivina el inicio de aba; q3 absorbente.",
            afn("q0 q1 q2 q3", "q0", "q3", "q0 Σ q0; q0 a q1; q1 b q2; q2 a q3; q3 Σ q3", S3), lambda w: "aba" in w),
    "104": (AFND_, "Cadena lineal abbab con lazo final; sin estado de rechazo.",
            afn("q0 q1 q2 q3 q4 q5", "q0", "q5", "q0 a q1; q1 b q2; q2 b q3; q3 a q4; q4 b q5; q5 Σ q5", S3),
            lambda w: w.startswith("abbab")),
    "105": (AFND_, "q0 con lazo adivina dónde empieza el sufijo abaa.",
            afn("q0 q1 q2 q3 q4", "q0", "q4", "q0 Σ q0; q0 a q1; q1 b q2; q2 a q3; q3 a q4", S3), lambda w: w.endswith("abaa")),
    "110": (AFND_, "Se conserva el AFD (como en los problemas 111-113 de la Práctica 1): un AFND acepta si algún camino acepta, "
                   "así que adivinar tres ocurrencias no impide que haya una cuarta. Contar «exactamente» exige "
                   "descartar todas las demás, y eso lo hace el AFD.", None, lambda w: traslapadas(w, "01") == 3),
    "114": (AFND_, "Lazo de a y lazo de b sin estado de rechazo: δ parcial.",
            afn("q0 q1 q2", "q0", "q2", "q0 a q1; q1 a q1; q1 b q2; q2 b q2", S3), regex("aa*bb*")),
    "115": (AFND_, "Ciclo abc sin estado de rechazo; δ parcial.",
            afn("q0 q1 q2 q3", "q0", "q3", "q0 a q1; q1 b q2; q2 c q3; q3 a q1", S2), regex("abc(abc)*")),
    "119": (AFND_, "Los tres estados útiles del AFD; leer a con aa pendiente no tiene transición (δ parcial).",
            afn("q0 q1 q2", "q0", "q0 q1", "q0 b q0; q0 a q1; q1 b q0; q1 a q2; q2 b q0", S3),
            lambda w: all(w[i + 2:i + 3] == "b" for i in range(len(w) - 1) if w[i:i + 2] == "aa")),
}

_LAMBDA_108 = afn(
    "i x0 x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 y0 y1 y2 y3 y4 y5 y6 y7 y8 y9 y10 y11 f", "i", "f",
    "i λ x0; i λ y0; x0 Σ x0; x0 a x1; x1 b x2; x2 b x3; x3 c x4; x4 b x5; x5 Σ x5; x5 c x6; x6 b x7; x7 a x8; "
    "x8 a x9; x9 b x10; x10 b x11; x11 Σ x11; x11 λ f; "
    "y0 Σ y0; y0 c y1; y1 b y2; y2 a y3; y3 a y4; y4 b y5; y5 b y6; y6 Σ y6; y6 a y7; y7 b y8; y8 b y9; y9 c y10; "
    "y10 b y11; y11 Σ y11; y11 λ f", S2)
_LAMBDA_117 = afn("q0 q1 q2 q3 q4 q5 q6 q7", "q0", "q7",
                  "q0 a q1; q1 a q1; q1 λ q2; q2 b q3; q3 b q3; q3 λ q4; q4 a q5; q5 a q5; q5 λ q6; q6 b q7; q7 b q7", S3)
NUEVOS_AFN_LAMBDA = {
    "108": ("Unión de dos órdenes: desde i, una transición λ elige la rama x (primero abbcb, luego cbaabb) y otra la rama y "
            "(al revés). En cada rama, los lazos con Σ₂ adivinan dónde empieza cada patrón; los patrones son cadenas "
            "lineales separadas, así que no pueden traslaparse. Las ramas se reúnen en f con otra λ.",
            _LAMBDA_108, lambda w: disjuntas(w, "abbcb", "cbaabb"),
            "Las dos λ de salida de i implementan la unión (el autómata «elige» el orden sin consumir símbolos) y las "
            "dos λ de llegada a f la cierran en un único estado de aceptación. Sin ellas habría que duplicar el lazo de "
            "q0 en cada rama o tener dos estados iniciales, que la definición no permite."),
    "117": ("Concatenación de cuatro bloques x⁺: cada bloque es un estado de entrada y un estado con lazo; una transición λ "
            "pasa al bloque siguiente cuando el autómata adivina que el bloque terminó.",
            _LAMBDA_117, regex("aa*bb*aa*bb*"),
            "Las λ (q1→q2, q3→q4, q5→q6) unen los bloques a⁺, b⁺, a⁺, b⁺ sin consumir símbolos: así cada bloque se "
            "diseña por separado y se concatena, que es como se construye el autómata de una concatenación de "
            "expresiones. No son indispensables (el AFD del 117 tiene 5 estados más el de rechazo), pero hacen "
            "visible la estructura aⁿ·bᵐ·aᵖ·bᵠ del enunciado."),
}

for n in ["94", "95", "96", "97", "98", "99", "100", "101", "102", "103", "104", "105", "106", "107", "108", "109",
          "110", "111", "112", "113", "114", "115", "116", "117", "118", "119", "120", "121", "122", "123"]:
    etiqueta = f"162-188 (p. {n})"
    archivo = f"L3-AFND-p{int(n):03d}"
    enunciado_l2 = next(e for e in EJERCICIOS if e.num == n and e.lista == 2).enunciado
    if n in _P1_AFN:
        _, viejo, enun, diseno, oraculo = _P1_AFN[n]
        ej(etiqueta, 3, AFND_, AFN_JUST, "AFN para el problema " + n + " de la Lista 2: " + enunciado_l2,
           [Pieza(archivo, "AFND", diseno, None, oraculo, origen=f"lista3-afn/{viejo}")], practica1=True)
    elif n in NUEVOS_AFN:
        sec, diseno, m, oraculo = NUEVOS_AFN[n]
        if m is None:  # se conserva el AFD
            base = next(e for e in EJERCICIOS if e.num == n and e.lista == 2).piezas[0]
            m = base.automata.copia()
        m.nombre = archivo
        ej(etiqueta, 3, AFND_, AFN_JUST, "AFN para el problema " + n + " de la Lista 2: " + enunciado_l2,
           [Pieza(archivo, "AFND", diseno, m, oraculo, convertir=not m.es_completo)])
    elif n in NUEVOS_AFN_LAMBDA:
        diseno, m, oraculo, razon = NUEVOS_AFN_LAMBDA[n]
        archivo = f"L3-AFNDL-p{int(n):03d}"
        m.nombre = archivo
        ej(etiqueta, 3, LAMBDA_, "Se resolvió con transiciones λ: componen el autómata a partir de piezas (unión o "
                                 "concatenación) sin consumir símbolos.",
           "AFN para el problema " + n + " de la Lista 2: " + enunciado_l2,
           [Pieza(archivo, "AFND-λ", diseno, m, oraculo, lambda_razon=razon)])
    elif n == "116":
        ej(etiqueta, 3, NINGUNA, "El lenguaje del 116 no es regular: tampoco existe un AFN (ver el problema 116).",
           "AFN para el problema 116 de la Lista 2.", notas="Ver la demostración en el problema 116: L no es regular.")

for n, archivo in (("189", "ej189_AFN"), ("190", "ej190_AFN")):
    ej(n, 3, AFND_, "Se pide un AFN: un lazo inicial adivina dónde empieza cada patrón.", _l3(n)[0][2],
       p1_l3(_l3(n), {archivo: f"L3-{n}"}), practica1=True)

ej("191", 3, AFND_, "Es el planteamiento común de los problemas 192-194: dado un AFN, hallar el AFD por subconjuntos.",
   "En los problemas 191-194, considere el AFN A = (Q, Σ, δ, A₀, F) definido en cada tabla. Encuentre un AFD "
   "equivalente y calcule δ̂(Z, ω) y δ̂_D(Z, ω).",
   notas="El método común es la construcción de subconjuntos: el AFD tiene por estados los subconjuntos de Q "
         "alcanzables desde {A₀}; δ_D(S, a) = ⋃_{q ∈ S} δ(q, a) y S es de aceptación si S ∩ F ≠ ∅. Como el AFD "
         "simula todos los caminos a la vez, δ̂_D({…}, ω) = δ̂(Z, ω) para todo Z y toda ω: los incisos a) y b) dan "
         "el mismo conjunto, uno visto como conjunto de estados del AFN y el otro como un solo estado del AFD. Los "
         "valores numéricos se calculan en cada problema.")

for n in ("192", "193", "194", "195"):
    nombres = {f"ej{n}_AFN": f"L3-{n}-AFND", f"ej{n}_AFD": f"L3-{n}-AFD"}
    piezas = p1_l3(_l3(n), nombres)
    piezas[1].convertir = False
    ej(n, 3, AFND_, "El autómata dado tiene celdas con dos o más estados y celdas ∅: es un AFN; el AFD es su conversión.",
       _l3(n)[0][2], piezas, practica1=True)

# 196-200: AFND-λ dados por tabla (columnas λ, 0, 1).
TABLAS_LAMBDA = {
    "196": ("A", "C", "A: B A -; B: - AB C; C: - - -"),
    "197": ("A", "D", "A: C BD -; B: D AC D; C: B - AC; D: - - D"),
    "198": ("A", "D", "A: C B -; B: - C -; C: B - CD; D: - - B"),
    "199": ("A", "DE", "A: BC E -; B: - E B; C: E - AC; D: - - D; E: - - D"),
    "200": ("A", "DE", "A: B F ACF; B: - CD BE; C: E - AC; D: EF AC BE; E: - - D; F: E BE -"),
}
INCISOS_LAMBDA = {
    "196": [("dg", "A", "110"), ("cl", "A"), ("cl", "B"), ("cl", "AB"), ("d", "A", "0")],
    "197": [("cl", "A"), ("cl", "BD"), ("cl", "ABC"), ("d", "A", "0"), ("dg", "A", "010")],
    "198": [("cl", "A"), ("cl", "CD"), ("cl", "ACD"), ("dg", "B", "0111")],
    "199": [("cl", "A"), ("cl", "C"), ("dg", "A", "011")],
    "200": [("cl", "A"), ("cl", "CD"), ("dg", "C", "1011")],
}
for n, (inicial, finales, renglones) in TABLAS_LAMBDA.items():
    m = tabla(inicial, finales, "01", renglones, lambda_primero=True, nombre=f"L3-{n}")
    ej(n, 3, LAMBDA_, "La tabla tiene una columna λ con entradas no vacías: es un AFND con transiciones λ.",
       f"Dibujar el AFND-λ de la tabla {n}, hallar un AFD equivalente y calcular los incisos.",
       [Pieza(f"L3-{n}", "AFND-λ dado en la tabla", "Transcripción de la tabla (columnas λ, 0, 1).", m,
              None, lambda_razon="Las transiciones λ vienen dadas por la tabla; su papel se lee en las λ-clausuras.")],
       notas=INCISOS_LAMBDA[n])

# 201-235: verdadero o falso. Cada expresión distinta se resuelve con su AFND-λ de Thompson.
VF = list(p1.VF) + [(235, None, "∅", "∅ no es una cadena: es el conjunto vacío. L(∅) = ∅ no tiene elementos, y aun si "
                                     "se leyera como «λ ∈ L(∅)», L(∅) no contiene ninguna cadena. Es falso.")]
_vistas = {}
for num, cadena, expresion, razon in VF:
    if expresion not in _vistas:
        _vistas[expresion] = f"L3-VF-{num}"
_POR_EXPRESION = {}
for num, cadena, expresion, razon in VF:
    _POR_EXPRESION.setdefault(expresion, []).append((num, cadena, razon))
for expresion, casos in _POR_EXPRESION.items():
    archivo = _vistas[expresion]
    m = thompson(expresion, "abc", archivo)
    nums = ", ".join(str(c[0]) for c in casos)
    ej(nums, 3, LAMBDA_,
       "Se decide la pertenencia construyendo el AFND-λ de Thompson de la expresión y simulando la cadena.",
       f"¿Es verdadera la afirmación «w ∈ L({expresion})»? Afirmaciones {nums}.",
       [Pieza(archivo, f"AFND-λ de Thompson de {expresion}",
              "Construcción de Thompson sobre Σ = {a, b, c}: cada símbolo es un fragmento i -a→ f; la unión y la "
              "estrella agregan un estado inicial y uno final unidos con λ, y la concatenación une fragmentos con λ.",
              m, regex(expresion),
              lambda_razon="Las λ son las de la construcción de Thompson: en la unión eligen una alternativa, en la "
                           "estrella permiten repetir o saltar el fragmento y en la concatenación enlazan fragmentos.",
              convertir=True)],
       notas=[("vf", c[0], c[1], expresion, c[2]) for c in casos], practica1=all(c[0] <= 234 for c in casos))

# 236-240: expresiones regulares (Práctica 1) y su AFND-λ de Thompson.
RAIZ_AUTOMATAS = __import__("pathlib").Path(__file__).resolve().parent.parent / "automatas"


def expresion_de(archivo_er):
    """Lee la expresión de un .jff de tipo re (sintaxis de JFLAP: + unión, ! λ)."""
    import xml.etree.ElementTree as ET

    for carpeta in CARPETA.values():
        ruta = RAIZ_AUTOMATAS / carpeta / f"{archivo_er}.jff"
        if ruta.exists():
            return ET.parse(ruta).getroot().findtext("expression").replace("!", "λ")
    raise FileNotFoundError(archivo_er + ".jff (ejecute primero herramientas/importar_p1.py)")


def thompson_de_archivo(archivo_er, nombre):
    return thompson(expresion_de(archivo_er), "01", nombre)

for num, archivo, enunciado, razon, oraculo in p1.ER:
    if int(num) > 240:
        continue
    ruta_p1 = f"L3-{num}-ER"
    ej(num, 3, LAMBDA_, "La respuesta es una expresión regular; su AFND-λ de Thompson es la forma de simularla.",
       enunciado + " Encontrar una expresión regular.",
       [Pieza(f"L3-{num}", "AFND-λ de Thompson de la expresión", razon, thompson_de_archivo(ruta_p1, f"L3-{num}"),
              oraculo, lambda_razon="Las λ son las de la construcción de Thompson (unión, estrella y concatenación).")],
       notas=[("er", ruta_p1)], practica1=True)

# 241-253: de expresión regular a AFND-λ.
ER_241 = {"241": "0+1", "242": "0*+1", "243": "(0+1)*", "244": "0(0+1)", "245": "0(0+1)*", "246": "0*(0+1)",
          "247": "(01)*+1*", "248": "(0*+1)0", "249": "(0*+1)0*", "250": "0*1*+1*0", "251": "(0+1*)0+1*1",
          "252": "(0+1)*(00+11)+(00+11)(0+1)*", "253": "(0+(11+00)*)(11+10+01)*(λ+110)"}
for num, er in ER_241.items():
    ej(num, 3, LAMBDA_, "Se pide explícitamente un AFND-λ equivalente a la expresión regular.",
       f"Encontrar un AFND-λ equivalente a la expresión regular {er}.",
       [Pieza(f"L3-{num}", f"AFND-λ de Thompson de {er}",
              "Construcción de Thompson: el árbol de la expresión se recorre de abajo hacia arriba y cada operador "
              "combina los fragmentos de sus operandos (ver la tabla de reglas en este documento).",
              thompson(er, "01", f"L3-{num}"), regex(er),
              lambda_razon="Thompson usa λ en tres lugares: dos de salida en cada unión (elegir alternativa), cuatro en "
                           "cada estrella (entrar, repetir, salir, saltar) y una entre los fragmentos de cada "
                           "concatenación. Ninguna consume símbolos, por eso la construcción es composicional.")],
       notas=[("thompson", er)])

# 254-258: de AFD a expresión regular (Práctica 1).
for n in ("254", "255", "256", "257", "258"):
    e = [x for x in p1.L3 if x[0] == n][0]
    er = [x for x in p1.ER if x[0] == n][0]
    ej(n, 3, AFD_, "El autómata dado es un AFD (δ total); la expresión se obtiene con el lema de Arden.",
       e[2] + " Encontrar una expresión regular.",
       [Pieza(f"L3-{n}", "AFD dado en la tabla", e[3], None, e[4], origen=f"lista3-afn/ej{n}")],
       notas=[("er", f"L3-{n}-ER"), ("texto", er[3])], practica1=True)

ej("259", 3, AFD_, "El autómata dado es un AFD (δ total); se aplica el algoritmo Rᵢⱼ⁽ᵏ⁾ de Kleene.",
   "Para el autómata de la tabla, ¿qué valores Rᵢⱼ⁽ᵏ⁾ (k = 0,…,4) son necesarios para encontrar R₁₄⁽⁴⁾? "
   "Encontrar una expresión regular equivalente.",
   [Pieza("L3-259", "AFD dado en la tabla", "Transcripción: 1 -a→ 3, 1 -b→ 2; 2 -a→ 1, 2 -b→ 3; 3 -a→ 2, 3 -b→ 3; "
          "4 -a→ 1, 4 -b→ 4. El estado de aceptación 4 no tiene transiciones de entrada desde 1, 2 o 3.",
          tabla("1", "4", "ab", "1: 3 2; 2: 1 3; 3: 2 3; 4: 1 4", nombre="L3-259"), lambda w: False)],
   notas=[("kleene",)])

for n in ("260", "261", "262", "263"):
    nombres = {f"ej{n}_AFN": f"L3-{n}-AFND", f"ej{n}_AFD": f"L3-{n}-AFD", f"ej{n}_AFD_min": f"L3-{n}-AFD-min"}
    piezas = p1_l3(_l3(n), nombres)
    for pz in piezas[1:]:
        pz.convertir = False
    ej(n, 3, AFND_, "El autómata de partida es un AFN (varios destinos por símbolo); el AFD es su conversión.",
       _l3(n)[0][2], piezas, practica1=True)

EJERCICIOS.sort(key=lambda e: (e.lista, e.orden))


def piezas():
    for e in EJERCICIOS:
        for p in e.piezas:
            yield e, p
