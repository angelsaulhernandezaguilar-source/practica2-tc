"""Copia los .jff de la Práctica 1 a la estructura de esta práctica, con sus nombres nuevos.

Uso (una sola vez, con el repositorio de la Práctica 1 clonado junto a este):

    python herramientas/importar_p1.py ../practica1-tc

Los archivos se copian sin modificar su contenido: son los mismos que se
verificaron en JFLAP en la Práctica 1. Después, generar.py les agrega su
versión .json y .xml.
"""

import pathlib
import shutil
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
ER = {"236": "lista3-afnd-lambda", "237": "lista3-afnd-lambda", "238": "lista3-afnd-lambda",
      "239": "lista3-afnd-lambda", "240": "lista3-afnd-lambda",
      "254": "lista2-afd", "255": "lista2-afd", "256": "lista2-afd", "257": "lista2-afd", "258": "lista2-afd"}


def destinos_de_er():
    for num, carpeta in ER.items():
        yield f"lista3-afn/ej{num}_ER", carpeta, f"L3-{num}-ER"


def main(p1):
    p1 = pathlib.Path(p1) / "automatas"
    copiados = 0
    # Primero las expresiones regulares: el catálogo las lee al importarse.
    for origen, carpeta, nuevo in destinos_de_er():
        destino = RAIZ / "automatas" / carpeta / f"{nuevo}.jff"
        destino.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(p1 / f"{origen}.jff", destino)
        copiados += 1
    sys.path[:0] = [str(RAIZ / "src"), str(RAIZ / "herramientas")]
    from catalogo import piezas

    for ejercicio, pieza in piezas():
        if pieza.origen:
            destino = RAIZ / "automatas" / ejercicio.carpeta / f"{pieza.archivo}.jff"
            destino.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(p1 / f"{pieza.origen}.jff", destino)
            copiados += 1
    print(f"{copiados} archivos copiados de {p1}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else RAIZ.parent / "practica1-tc")
