"""Práctica 3, Ejercicio 1.1: los cinco AFD convertidos a expresión regular en JFLAP 7.1.

Uso (requiere Java y JFLAP 7.1):

    set JFLAP_JAR=C:\\ruta\\JFLAP7.1.jar          (bash: export JFLAP_JAR=/ruta/JFLAP7.1.jar)
    python herramientas/practica3_er.py

Para cada AFD de automatas/practica3/afd-a-er/ ejecuta herramientas/JflapER.java,
que maneja la ventana real de JFLAP (Convert FA to RE → Export → Convert to NFA →
Do All → Export, y FSAEqualityChecker, la clase de Test > Compare Equivalence) y
simula seis cadenas en el AFD y en el AFN de la expresión. Después:

* guarda la expresión en automatas/practica3/afd-a-er/<AFD>-ER.jff (tipo re de JFLAP);
* copia las capturas y los registros a evidencias/practica3/jflap/<AFD>/;
* comprueba, con el núcleo del proyecto, que la expresión de JFLAP y la
  simplificada a mano (SIMPLIFICADAS) son equivalentes al AFD.
"""

from __future__ import annotations

import os
import pathlib
import shutil
import subprocess
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
sys.path[:0] = [str(RAIZ / "src"), str(RAIZ / "herramientas")]

from construir import thompson  # noqa: E402
from formatos import cargar  # noqa: E402

CARPETA = RAIZ / "automatas" / "practica3" / "afd-a-er"
EVIDENCIAS = RAIZ / "evidencias" / "practica3" / "jflap"
AFD = ["L2-130", "L2-138", "L2-141", "L3-257", "L3-258"]

# Expresiones simplificadas a mano en docs/practica3/01-afd-a-er-jflap.md (sintaxis de JFLAP: + es unión, λ la vacía).
SIMPLIFICADAS = {
    "L2-130": "0*1(1+0(0+1))*",
    "L2-138": "a*(ba*ba*ba*)*",
    "L2-141": "(1+01)*",
    "L3-257": "((1+01*0)(0+1))*(01*(λ+0)+1)",
    "L3-258": "((0+1)(01)*(1+00))*(0+1)(01)*",
}


def cadenas_de_prueba(aut, cuantas=3):
    """Las `cuantas` cadenas aceptadas y rechazadas más cortas, en orden canónico."""
    si, no = [], []
    for w in aut.cadenas_aceptadas(8):
        if len(si) < cuantas:
            si.append(w)
    from algoritmos import palabras

    for t in palabras(aut.alfabeto, 8):
        w = "".join(t)
        if not aut.acepta(w) and len(no) < cuantas:
            no.append(w)
        if len(no) >= cuantas:
            break
    return [w or "λ" for w in si + no]


def leer_resultado(carpeta):
    datos = {"cadenas": []}
    for linea in (carpeta / "resultado.tsv").read_text(encoding="utf-8").splitlines():
        p = linea.split("\t")
        if p[0] == "cadena":
            datos["cadenas"].append((p[1], p[2] == "true", p[3] == "true"))
        else:
            datos[p[0]] = p[1]
    return datos


def escribir_er(nombre, expresion):
    (CARPETA / f"{nombre}-ER.jff").write_text(
        '<?xml version="1.0" encoding="UTF-8" standalone="no"?><!--Created with JFLAP 7.1.-->\n'
        f"<structure>\n\t<type>re</type>\n\t<expression>{expresion}</expression>\n</structure>\n",
        encoding="utf-8", newline="\n")


def main():
    jar = os.environ.get("JFLAP_JAR")
    if not jar:
        sys.exit("Defina JFLAP_JAR con la ruta de JFLAP7.1.jar")
    clases = RAIZ / "build" / "clases"
    clases.mkdir(parents=True, exist_ok=True)
    subprocess.run(["javac", "-nowarn", "-encoding", "UTF-8", "-cp", jar, "-d", str(clases),
                    str(RAIZ / "herramientas" / "JflapER.java")], check=True)
    lista = RAIZ / "build" / "practica3-er.tsv"
    salida = RAIZ / "build" / "practica3-er"
    renglones = []
    for n in AFD:
        aut = cargar(CARPETA / f"{n}.jff")
        renglones.append(f"{CARPETA / f'{n}.jff'}\t{salida / n}\t{','.join(cadenas_de_prueba(aut))}")
    lista.write_text("\n".join(renglones) + "\n", encoding="utf-8")
    if salida.exists():
        shutil.rmtree(salida)
    subprocess.run(["java", "-Duser.language=en", "-cp", os.pathsep.join([str(clases), jar]), "JflapER", str(lista)],
                   check=True, cwd=RAIZ, timeout=600)
    for n in AFD:
        aut = cargar(CARPETA / f"{n}.jff")
        datos = leer_resultado(salida / n)
        er = datos["expresion"]
        escribir_er(n, er)
        destino = EVIDENCIAS / n
        if destino.exists():
            shutil.rmtree(destino)
        shutil.copytree(salida / n, destino)
        jflap_ok = thompson(er.replace("!", "λ"), aut.alfabeto).equivalente(aut)
        mano_ok = thompson(SIMPLIFICADAS[n], aut.alfabeto).equivalente(aut)
        cadenas_ok = all(a == b == aut.acepta("" if w == "λ" else w) for w, a, b in datos["cadenas"])
        print(f"{n}: {er}  | Compare Equivalence: {datos['equivalentes']} (sin sumideros "
              f"[{datos.get('sumideros', '')}]: {datos['equivalentes_sin_sumidero']}) | AFN: {datos['estados_afn']} estados | "
              f"núcleo: JFLAP {jflap_ok}, simplificada {mano_ok}, cadenas {cadenas_ok}")


if __name__ == "__main__":
    main()
