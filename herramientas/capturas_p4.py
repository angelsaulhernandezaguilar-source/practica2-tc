"""Capturas de la interfaz para docs/practica4/ (pestañas 6, 7 y 8).

Requiere la aplicación en modo web y Playwright (no forma parte de requirements.txt):

    FLET_FORCE_WEB_SERVER=true FLET_SERVER_PORT=8551 python src/app.py
    pip install playwright && python -m playwright install chromium
    python herramientas/capturas_p4.py [http://127.0.0.1:8551/]

Hace los mismos clics que un usuario (a través del árbol de accesibilidad de
Flutter) y guarda las imágenes en evidencias/practica4/app/.
"""

import pathlib
import sys
import time

from playwright.sync_api import sync_playwright

RAIZ = pathlib.Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "evidencias" / "practica4" / "app"
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

        def escribir(etiqueta, valor):
            """Teclea el valor con eventos de teclado reales, que Flet recibe como cambios del campo."""
            campo = pg.get_by_role("textbox", name=etiqueta)
            campo.scroll_into_view_if_needed()
            campo.click()
            pg.keyboard.press("End")
            for _ in range(60):  # vacía el campo (Ctrl+A no selecciona en Flutter web)
                pg.keyboard.press("Backspace")
            pg.keyboard.type(valor, delay=15)
            pausa(0.8)

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

        def elegir_en_lista(posicion, opcion):
            """Abre la lista desplegable número ``posicion`` de la pestaña (los desplegables son botones sin nombre)."""
            pg.get_by_role("tabpanel").get_by_role("button").nth(posicion).click()
            pausa(0.8)
            pg.get_by_text(opcion, exact=True).last.click()
            pausa(2)  # la ficha del validador se rellena al cambiar la lista

        def foto(nombre, desplazar=0):
            if desplazar:
                pg.mouse.wheel(0, desplazar)
                pausa(0.8)
            pg.screenshot(path=str(SALIDA / f"{nombre}.png"))
            print("captura", nombre)

        # Ejercicio 2: (ab)*a (Lista 4, 272 b) paso a paso.
        pestana("6. ER → autómata")
        escribir("Expresión regular (notación del curso)", "(ab)*a")
        boton("Analizar y construir")
        pausa(1.5)
        boton("Siguiente paso")
        boton("Siguiente paso")
        boton("Siguiente paso")
        foto("er-construccion-paso")
        boton("Hasta el final")
        foto("er-construccion-final")
        pg.mouse.wheel(0, 900)
        pausa()
        foto("er-afd-minimo")
        escribir("Cadena a validar (vacía = λ)", "aba")
        escribir("Varias cadenas, una por línea", "aba\nab\nbabb\nabab")
        boton("Validar")
        pg.mouse.wheel(0, 2500)
        pausa()
        foto("er-validacion")

        # Expresión mal formada: posición del error.
        pg.mouse.wheel(0, -5000)
        pausa()
        escribir("Expresión regular (notación del curso)", "(a+b)*(ab")
        boton("Analizar y construir")
        foto("er-error")

        # Ejercicio 2: el 253 con la etapa AFD por subconjuntos.
        escribir("Expresión regular (notación del curso)", "(0+(11+00)*)(11+10+01)*(λ+110)")
        boton("Analizar y construir")
        pausa(1.5)
        boton("Hasta el final")
        pg.mouse.wheel(0, 1400)
        pausa()
        foto("er-253-minimo")

        # Ejercicio 3: AFD 257 de la Práctica 3 → expresión, paso a paso y comparación con JFLAP.
        cargar("practica3/afd-a-er/L3-257.jff")
        pestana("7. Autómata → ER")
        boton("Verificar y calcular")
        pausa(1.5)
        boton("Siguiente paso")
        foto("afd-eliminacion-paso")
        boton("Hasta el final")
        foto("afd-eliminacion-final")
        pg.mouse.wheel(0, 2500)  # el campo de comparación está al final de la pestaña
        pausa()
        escribir("Expresión con la que comparar (p. ej. la de JFLAP)", "((1+01*0)(0+1))*(01*(λ+0)+1)")
        boton("Comparar")
        pg.mouse.wheel(0, 2500)
        pausa()
        foto("afd-comparacion")

        # Ejercicio 3: un AFN no pasa la verificación.
        cargar("practica3/casos-de-prueba/L3-192-AFND.jff")
        pestana("7. Autómata → ER")
        boton("Verificar y calcular")
        foto("afd-no-determinista")

        # Ejercicio 4: validadores.
        pestana("8. Validadores")
        boton("Validar")
        foto("validador-correo")
        elegir_en_lista(0, "Teléfono nacional (México, 10 dígitos)")
        escribir("Texto a validar", "(55) 1234 5678")
        boton("Validar")
        boton("Ver el AFD mínimo")
        foto("validador-telefono")
        elegir_en_lista(0, "Fecha (DD/MM/AAAA, DD-MM-AAAA o AAAA-MM-DD)")
        escribir("Texto a validar", "31/02/2026")
        boton("Validar")
        foto("validador-fecha")
        elegir_en_lista(0, "URL (http o https)")
        escribir("Texto a validar", "https://x.mx:8080/a/b.html?q=1&r=2#top")
        boton("Validar")
        foto("validador-url")
        navegador.close()


if __name__ == "__main__":
    main()
