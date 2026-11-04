"""Capturas de la interfaz para docs/practica3/02-software.md.

Requiere la aplicación en modo web y Playwright (no forma parte de requirements.txt):

    FLET_FORCE_WEB_SERVER=true FLET_SERVER_PORT=8551 python src/app.py
    pip install playwright && python -m playwright install chromium
    python herramientas/capturas_p3.py [http://127.0.0.1:8551/]

Recorre las funciones de la Práctica 3 con los mismos clics que haría un
usuario (a través del árbol de accesibilidad de Flutter) y guarda las imágenes
en evidencias/practica3/app/.
"""

import pathlib
import sys
import time

from playwright.sync_api import sync_playwright

RAIZ = pathlib.Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "evidencias" / "practica3" / "app"
URL = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8551/"


def main():
    SALIDA.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        navegador = p.chromium.launch()
        pg = navegador.new_page(viewport={"width": 1500, "height": 1150})
        pg.goto(URL)
        time.sleep(8)
        pg.locator("flt-semantics-placeholder").dispatch_event("click")
        time.sleep(2)

        def pausa(s=1.2):
            time.sleep(s)

        def pestana(nombre):
            pg.get_by_role("tab", name=nombre).click()
            pausa()

        def boton(nombre, n=0):
            pg.get_by_role("button", name=nombre, exact=True).nth(n).click()
            pausa()

        def cargar(ruta):
            pestana("1. Definir")
            campo = pg.get_by_role("textbox", name="Autómatas del repositorio")
            campo.click()
            campo.fill(ruta)
            pausa()
            pg.get_by_text(ruta, exact=True).last.click()
            pausa()
            boton("Cargar")
            pausa(1.5)

        def elegir(posicion, opcion):
            """Abre la lista desplegable número ``posicion`` de la pestaña (0 = Algoritmo, 1 = Estado)."""
            pg.get_by_role("tabpanel").get_by_role("button").nth(posicion).click()
            pausa(0.8)
            pg.get_by_text(opcion, exact=True).last.click()
            pausa()

        def foto(nombre):
            pg.screenshot(path=str(SALIDA / f"{nombre}.png"))
            print("captura", nombre)

        # 2.1 Cerradura λ del estado A en el 197 (estado elegido por el usuario).
        cargar("practica3/casos-de-prueba/L3-197.jff")
        pestana("5. Paso a paso")
        elegir(0, "2.1 Cerradura λ")
        elegir(1, "A")
        boton("Calcular")
        boton("Siguiente paso")
        boton("Siguiente paso")
        foto("cerradura-paso")
        boton("Hasta el final")
        foto("cerradura-final")

        # 2.1 Simulación directa del 197 con 010: activos antes y después de la cerradura.
        pestana("3. Simular")
        pg.get_by_role("textbox", name="Cadena w (vacía = λ)").fill("010")
        boton("Siguiente paso")
        boton("Siguiente paso")
        boton("Siguiente paso")
        foto("simulacion-directa-paso")
        boton("Validar")
        foto("simulacion-directa-final")

        # 2.2 Eliminación de λ en el 199.
        cargar("practica3/casos-de-prueba/L3-199.jff")
        pestana("5. Paso a paso")
        elegir(0, "2.2 Eliminación de transiciones λ")
        boton("Calcular")
        for _ in range(3):
            boton("Siguiente paso")
        foto("eliminar-lambda-paso")
        boton("Hasta el final")
        foto("eliminar-lambda-final")

        # 2.3 Subconjuntos del 193: la tabla crece renglón por renglón.
        cargar("practica3/casos-de-prueba/L3-193-AFND.jff")
        pestana("5. Paso a paso")
        elegir(0, "2.3 Construcción de subconjuntos")
        boton("Calcular")
        for _ in range(3):
            boton("Siguiente paso")
        foto("subconjuntos-paso")
        boton("Hasta el final")
        foto("subconjuntos-final")

        # 2.4 Minimización del 155 (con estados inaccesibles).
        cargar("practica3/casos-de-prueba/L3-155-original.jff")
        pestana("5. Paso a paso")
        elegir(0, "2.4 Minimización de AFD")
        boton("Calcular")
        boton("Siguiente paso")
        boton("Siguiente paso")
        foto("minimizar-paso")
        boton("Hasta el final")
        foto("minimizar-final")

        # 2.4 Equivalencia: el AFN del 192 contra el AFD que dio JFLAP en la Práctica 2.
        cargar("practica3/casos-de-prueba/L3-192-AFND.jff")
        pestana("5. Paso a paso")
        elegir(0, "2.4 Equivalencia de dos autómatas")
        campo = pg.get_by_role("textbox", name="Segundo autómata (equivalencia)")
        campo.click()
        campo.fill("lista3-afnd/L3-192-AFD.jff")
        pausa()
        pg.get_by_text("lista3-afnd/L3-192-AFD.jff", exact=True).last.click()
        pausa()
        boton("Calcular")
        boton("Hasta el final")
        foto("equivalencia")

        # 2.5 Validación de varias cadenas con el archivo de ejemplo.
        cargar("practica3/casos-de-prueba/L3-196.jff")
        pestana("3. Simular")
        boton("Usar cadenas-ejemplo.txt")
        pg.mouse.wheel(0, 2500)
        pausa()
        foto("validacion-lote")
        navegador.close()


if __name__ == "__main__":
    main()
