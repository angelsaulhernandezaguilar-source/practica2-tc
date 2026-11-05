"""Genera los archivos de la Práctica 4 en automatas/practica4/ y las tablas de resultados.

    python herramientas/practica4_generar.py

* casos-de-prueba/er/: para cada expresión de prueba (Lista 3, 241-253; Lista 4, 272 y 278) la expresión
  en .jff de JFLAP y los cuatro autómatas (AFN-λ, AFN, AFD, AFD mínimo) que produce el software.
* casos-de-prueba/afd/: para cada AFD de prueba (Lista 3, 254-258; Lista 4, 276 y 277; los cinco de la
  Práctica 3) la expresión obtenida por eliminación de estados y el AFD mínimo de esa expresión.
* validadores/: el AFN-λ, el AFD mínimo y la expresión de cada validador del Ejercicio 4.
* resultados.md: las tablas que se citan en docs/practica4/.
"""

import pathlib
import shutil
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "src"))

from algoritmos import equivalentes_por_minimizacion  # noqa: E402
from expresiones import (  # noqa: E402
    a_python,
    analizar,
    comparar_expresiones,
    de_expresion_a_minimo,
    eliminar_estados,
    equivalente_al_automata,
    escribir_expresion_jff,
    leer_expresion_jff,
)
from formatos import cargar, guardar  # noqa: E402
from validadores import VALIDADORES  # noqa: E402

P4 = RAIZ / "automatas" / "practica4"

ER_241_253 = {
    "241": "0+1", "242": "0*+1", "243": "(0+1)*", "244": "0(0+1)", "245": "0(0+1)*", "246": "0*(0+1)",
    "247": "(01)*+1*", "248": "(0*+1)0", "249": "(0*+1)0*", "250": "0*1*+1*0", "251": "(0+1*)0+1*1",
    "252": "(0+1)*(00+11)+(00+11)(0+1)*", "253": "(0+(11+00)*)(11+10+01)*(λ+110)",
}
ER_L4 = {"272a": "a+b*", "272b": "(ab)*a", "272c": "(a+b)*abb", "272d": "a(ba)*+b", "272e": "(a+λ)(b+∅)",
         "278": "(a+b)*b"}

AFD_CASOS = {
    # nombre: (archivo de entrada, expresión de referencia, origen de la referencia)
    "L3-254": ("lista2-afd/L3-254.jff", "lista2-afd/L3-254-ER.jff", "Arden, Práctica 1"),
    "L3-255": ("lista2-afd/L3-255.jff", "lista2-afd/L3-255-ER.jff", "Arden, Práctica 1"),
    "L3-256": ("lista2-afd/L3-256.jff", "lista2-afd/L3-256-ER.jff", "Arden, Práctica 1"),
    "L3-257": ("lista2-afd/L3-257.jff", "lista2-afd/L3-257-ER.jff", "Arden, Práctica 1"),
    "L3-258": ("lista2-afd/L3-258.jff", "lista2-afd/L3-258-ER.jff", "Arden, Práctica 1"),
    "L4-276": ("practica4/casos-de-prueba/afd/L4-276.jff", "(b+ab*ab*a)*", "Arden, Lista 4"),
    "L4-277": ("practica4/casos-de-prueba/afd/L4-277.jff", "(0+11*0)*11*", "Arden, Lista 4 (Rᵢⱼᵏ: 0*1(0*1)*)"),
    "P3-L2-130": ("practica3/afd-a-er/L2-130.jff", "practica3/afd-a-er/L2-130-ER.jff", "JFLAP, Práctica 3"),
    "P3-L2-138": ("practica3/afd-a-er/L2-138.jff", "practica3/afd-a-er/L2-138-ER.jff", "JFLAP, Práctica 3"),
    "P3-L2-141": ("practica3/afd-a-er/L2-141.jff", "practica3/afd-a-er/L2-141-ER.jff", "JFLAP, Práctica 3"),
    "P3-L3-257": ("practica3/afd-a-er/L3-257.jff", "practica3/afd-a-er/L3-257-ER.jff", "JFLAP, Práctica 3"),
    "P3-L3-258": ("practica3/afd-a-er/L3-258.jff", "practica3/afd-a-er/L3-258-ER.jff", "JFLAP, Práctica 3"),
}


def escribir(ruta: pathlib.Path, texto: str):
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(texto, encoding="utf-8", newline="\n")


def expresiones():
    carpeta = P4 / "casos-de-prueba" / "er"
    filas = ["| Caso | Expresión | AFN-λ | AFN | AFD | AFD mínimo | Patrón de `re` |", "|---|---|---|---|---|---|---|"]
    for numero, er in {**ER_241_253, **ER_L4}.items():
        prefijo = f"L3-{numero}" if numero in ER_241_253 else f"L4-{numero}"
        c = de_expresion_a_minimo(er, nombre=prefijo)
        escribir(carpeta / f"{prefijo}-ER.jff", escribir_expresion_jff(c.expresion))
        for etapa, m in (("afn-lambda", c.afn_lambda), ("afn", c.cadena.sin_lambda.automata),
                         ("afd", c.cadena.subconjuntos.automata), ("min", c.minimo)):
            guardar(m.copia(f"{prefijo}-{etapa}"), carpeta / f"{prefijo}-{etapa}.jff")
        t = c.tamanos()
        filas.append(f"| {prefijo} | `{er}` | {t['AFN-λ']} | {t['AFN']} | {t['AFD']} | {t['AFD mínimo']} | "
                     f"`{a_python(c.expresion)}` |")
        print(prefijo, er, t)
    return filas


def automatas():
    carpeta = P4 / "casos-de-prueba" / "afd"
    filas = ["| Caso | Estados | Orden de eliminación | Expresión obtenida | Referencia | Equivalentes | "
             "Estados del AFD mínimo |", "|---|---|---|---|---|---|---|"]
    for nombre, (entrada, referencia, origen) in AFD_CASOS.items():
        afd = cargar(RAIZ / "automatas" / entrada)
        if not nombre.startswith("L4"):
            guardar(afd, carpeta / f"{nombre}.jff")
        r = eliminar_estados(afd)
        escribir(carpeta / f"{nombre}-ER.jff", escribir_expresion_jff(r.expresion))
        ref = referencia if not referencia.endswith(".jff") else leer_expresion_jff(
            (RAIZ / "automatas" / referencia).read_text(encoding="utf-8"))
        cmp = comparar_expresiones(str(r.expresion), ref)
        contra_afd = equivalente_al_automata(str(r.expresion), afd)
        guardar(cmp.primera.minimo.copia(f"{nombre}-ER-min"), carpeta / f"{nombre}-ER-min.jff")
        assert cmp.equivalentes and contra_afd.equivalentes, nombre
        filas.append(f"| {nombre} | {len(afd.estados)} | {', '.join(r.orden) or '(ninguno)'} | `{r.expresion}` | "
                     f"`{ref}` ({origen}) | sí | {len(cmp.primera.minimo.estados)} |")
        print(nombre, "→", r.expresion, "| ref:", ref, "| equivalentes")
    return filas


def validadores():
    carpeta = P4 / "validadores"
    filas = ["| Validador | Σ | AFN-λ | AFN | AFD | AFD mínimo |", "|---|---|---|---|---|---|"]
    for clave, v in VALIDADORES.items():
        c = v.cadena()
        escribir(carpeta / f"{clave}-ER.jff", escribir_expresion_jff(analizar(v.expresion, v.clases)))
        guardar(c.afn_lambda.copia(f"{clave}-afn-lambda"), carpeta / f"{clave}-afn-lambda.jff")
        guardar(c.minimo.copia(f"{clave}-min"), carpeta / f"{clave}-min.jff")
        escribir(carpeta / f"{clave}-re.txt", v.patron + "\n")
        t = c.tamanos()
        filas.append(f"| {v.nombre} | {len(v.alfabeto())} símbolos | {t['AFN-λ']} | {t['AFN']} | {t['AFD']} | "
                     f"{t['AFD mínimo']} |")
        print(clave, t)
    return filas


def main():
    partes = ["# Resultados generados por herramientas/practica4_generar.py", "",
              "## Ejercicio 2: de la expresión al AFD mínimo", ""] + expresiones()
    partes += ["", "## Ejercicio 3: del AFD a la expresión por eliminación de estados", ""] + automatas()
    partes += ["", "## Ejercicio 4: validadores", ""] + validadores()
    escribir(P4 / "resultados.md", "\n".join(partes) + "\n")


if __name__ == "__main__":
    main()
