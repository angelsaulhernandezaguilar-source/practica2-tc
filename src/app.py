"""
Simulador de autómatas finitos con interfaz gráfica (Flet).

Este archivo solo conecta controles con el núcleo:

* automata.py  — la quíntupla, la simulación y las conversiones;
* formatos.py  — la lectura y escritura de .jff, .json y .xml;
* lenguajes.py — las operaciones de la Práctica 1.

Ninguna regla del autómata vive aquí; por eso el núcleo se prueba con pytest
sin abrir la interfaz.
"""

from __future__ import annotations

import math
import os
import pathlib

import flet as ft
import flet.canvas as cv

from automata import (
    LAMBDA,
    Automata,
    AutomataInvalido,
    desde_tabla,
    mostrar_cadena,
    mostrar_conjunto,
)
from formatos import FormatoInvalido, a_texto, desde_texto, posiciones, resumen_quintupla
from lenguajes import (
    cerradura_kleene,
    cerradura_positiva,
    parsear_alfabeto,
    prefijos,
    subcadenas,
    sufijos,
)

RAIZ = pathlib.Path(__file__).resolve().parent.parent
CARPETA_EJEMPLOS = RAIZ / "automatas"
RADIO = 22

# Modos de simulación de un autómata no determinista (ver docs/03-simulador.md).
TODOS_LOS_CAMINOS = "caminos"
CONVERTIR_A_AFD = "afd"


def mostrar(cadenas):
    return ", ".join(c if c else "λ" for c in cadenas) or "∅"


def ejemplos_disponibles() -> list[str]:
    if not CARPETA_EJEMPLOS.is_dir():
        return []
    return sorted(str(p.relative_to(CARPETA_EJEMPLOS)).replace(os.sep, "/")
                  for p in CARPETA_EJEMPLOS.rglob("*.jff"))


# ----------------------------------------------------------------------
# Dibujo del diagrama de transiciones
# ----------------------------------------------------------------------

def diagrama(aut: Automata, activos=frozenset(), recientes=()) -> ft.Control:
    """Diagrama con Canvas: círculos, flechas con etiqueta, inicial con flecha de entrada y
    aceptación con doble círculo. ``activos`` se colorean; ``recientes`` son las transiciones
    (origen, símbolo, destino) que se acaban de tomar."""
    pos = posiciones(aut)
    xs = [x for x, _ in pos.values()] or [0]
    ys = [y for _, y in pos.values()] or [0]
    ancho, alto = max(xs) + 90, max(ys) + 90
    lapiz = ft.Paint(color=ft.Colors.BLUE_GREY_700, stroke_width=1.6, style=ft.PaintingStyle.STROKE)
    resaltado = ft.Paint(color=ft.Colors.ORANGE_800, stroke_width=3, style=ft.PaintingStyle.STROKE)
    figuras = []

    etiquetas: dict[tuple[str, str], list[str]] = {}
    for (q, a), destinos in aut.transiciones.items():
        for p in destinos:
            etiquetas.setdefault((q, p), []).append(a or "λ")
    usados = {(q, p) for q, _, p in recientes}

    def texto(x, y, valor, color=ft.Colors.BLACK, tam=12, negrita=False):
        return cv.Text(x, y, valor, style=ft.TextStyle(size=tam, color=color,
                                                        weight=ft.FontWeight.BOLD if negrita else None),
                       alignment=ft.Alignment.CENTER)

    def punta(x1, y1, x2, y2, pintura):
        ang = math.atan2(y2 - y1, x2 - x1)
        return [cv.Line(x2, y2, x2 - 10 * math.cos(ang - 0.4), y2 - 10 * math.sin(ang - 0.4), pintura),
                cv.Line(x2, y2, x2 - 10 * math.cos(ang + 0.4), y2 - 10 * math.sin(ang + 0.4), pintura)]

    for (q, p), simbolos in etiquetas.items():
        pintura = resaltado if (q, p) in usados else lapiz
        rotulo = ",".join(sorted(simbolos, key=lambda s: (s == "λ", s)))
        x1, y1 = pos[q]
        if q == p:
            figuras.append(cv.Circle(x1, y1 - RADIO - 10, 13, pintura))
            figuras += punta(x1 + 14, y1 - RADIO - 14, x1 + 9, y1 - RADIO + 2, pintura)
            figuras.append(texto(x1, y1 - RADIO - 34, rotulo))
            continue
        x2, y2 = pos[p]
        ang = math.atan2(y2 - y1, x2 - x1)
        # Si también existe la flecha de regreso, ambas se curvan hacia lados opuestos.
        curva = 28 if (p, q) in etiquetas else 0
        mx, my = (x1 + x2) / 2 - curva * math.sin(ang), (y1 + y2) / 2 + curva * math.cos(ang)
        sx, sy = x1 + RADIO * math.cos(ang), y1 + RADIO * math.sin(ang)
        ex, ey = x2 - RADIO * math.cos(ang), y2 - RADIO * math.sin(ang)
        if curva:
            figuras.append(cv.Path([cv.Path.MoveTo(sx, sy), cv.Path.QuadraticTo(mx, my, ex, ey)], paint=pintura))
            figuras += punta(mx, my, ex, ey, pintura)
        else:
            figuras.append(cv.Line(sx, sy, ex, ey, pintura))
            figuras += punta(sx, sy, ex, ey, pintura)
        figuras.append(texto(mx - 8 * math.sin(ang), my + 8 * math.cos(ang) - 6, rotulo))

    for q, (x, y) in pos.items():
        relleno = ft.Colors.AMBER_200 if q in activos else ft.Colors.WHITE
        figuras.append(cv.Circle(x, y, RADIO, ft.Paint(color=relleno, style=ft.PaintingStyle.FILL)))
        figuras.append(cv.Circle(x, y, RADIO, lapiz))
        if q in aut.aceptacion:
            figuras.append(cv.Circle(x, y, RADIO - 4, lapiz))
        if q == aut.inicial:
            figuras.append(cv.Line(x - RADIO - 28, y, x - RADIO, y, lapiz))
            figuras += punta(x - RADIO - 28, y, x - RADIO, y, lapiz)
        figuras.append(texto(x, y - 6, q if len(q) <= 6 else q[:5] + "…", tam=11, negrita=True))

    return ft.Container(cv.Canvas(figuras, width=ancho, height=alto), width=ancho, height=alto,
                        bgcolor=ft.Colors.GREY_50)


def tabla_control(aut: Automata) -> ft.DataTable:
    filas = aut.tabla()
    return ft.DataTable(
        columns=[ft.DataColumn(ft.Text(c, weight=ft.FontWeight.BOLD)) for c in filas[0]],
        rows=[ft.DataRow([ft.DataCell(ft.Text(c, selectable=True)) for c in f]) for f in filas[1:]],
        border=ft.Border.all(1, ft.Colors.GREY_400),
        horizontal_lines=ft.BorderSide(0.5, ft.Colors.GREY_300),
    )


# ----------------------------------------------------------------------
# Aplicación
# ----------------------------------------------------------------------

def main(page: ft.Page):
    page.title = "Práctica 2 — Simulador de autómatas finitos"
    page.padding = 16
    page.scroll = ft.ScrollMode.AUTO

    estado = {"aut": None, "pasos": [], "i": 0, "cadena": "", "simulado": None}
    selector = ft.FilePicker()
    page.services.append(selector)

    def avisar(mensaje, error=False):
        page.show_dialog(ft.SnackBar(ft.Text(mensaje), bgcolor=ft.Colors.RED_700 if error else None))

    # ------------------------------------------------------------------
    # Pestaña 1: definición del autómata
    # ------------------------------------------------------------------
    campo_sigma = ft.TextField(label="Alfabeto Σ (separado por comas)", value="a, b", width=320)
    campo_q = ft.TextField(label="Estados Q (separados por comas)", value="q0, q1", width=320)
    con_lambda = ft.Checkbox(label="Columna λ (AFND-λ)", value=True)
    lista_inicial = ft.Dropdown(label="Estado inicial q0", width=200)
    fila_finales = ft.Row(wrap=True)
    contenedor_tabla = ft.Column()
    celdas: dict[tuple[str, str], ft.TextField] = {}
    mensajes = ft.Text(color=ft.Colors.RED_700, selectable=True)

    def preparar_tabla(e=None, aut: Automata | None = None):
        """Rehace la tabla interactiva para el Σ y la Q escritos (o para ``aut``)."""
        if aut is not None:
            campo_sigma.value = ", ".join(aut.alfabeto)
            campo_q.value = ", ".join(aut.estados)
            con_lambda.value = aut.tiene_lambda
        sigma = [s.strip() for s in (campo_sigma.value or "").split(",") if s.strip()]
        estados = [s.strip() for s in (campo_q.value or "").split(",") if s.strip()]
        anteriores = {k: c.value for k, c in celdas.items()}
        columnas = sigma + ([LAMBDA] if con_lambda.value else [])
        lista_inicial.options = [ft.DropdownOption(q) for q in estados]
        if aut is not None:
            lista_inicial.value = aut.inicial
        elif lista_inicial.value not in estados:
            lista_inicial.value = estados[0] if estados else None
        marcados = {c.label for c in fila_finales.controls if c.value}
        if aut is not None:
            marcados = set(aut.aceptacion)
        fila_finales.controls = [ft.Checkbox(label=q, value=q in marcados) for q in estados]
        celdas.clear()
        renglones = []
        for q in estados:
            fila = [ft.DataCell(ft.Text(q, weight=ft.FontWeight.BOLD))]
            for a in columnas:
                if aut is not None:
                    valor = ", ".join(sorted(aut.destinos(q, a)))
                else:
                    valor = anteriores.get((q, a), "")
                celdas[q, a] = ft.TextField(value=valor, dense=True, width=110, hint_text="∅")
                fila.append(ft.DataCell(celdas[q, a]))
            renglones.append(ft.DataRow(fila))
        contenedor_tabla.controls = [ft.Row([ft.DataTable(
            columns=[ft.DataColumn(ft.Text("δ"))] + [ft.DataColumn(ft.Text(a or "λ")) for a in columnas],
            rows=renglones, border=ft.Border.all(1, ft.Colors.GREY_400))], scroll=ft.ScrollMode.AUTO)]
        page.update()

    def aplicar(e=None):
        try:
            aut = desde_tabla(campo_sigma.value, campo_q.value, lista_inicial.value or "",
                              {c.label for c in fila_finales.controls if c.value},
                              {k: c.value for k, c in celdas.items()},
                              nombre=(estado["aut"].nombre if estado["aut"] else "manual"))
        except AutomataInvalido as err:
            mensajes.value = str(err)
            page.update()
            return
        mensajes.value = ""
        fijar(aut, "Autómata definido manualmente.")

    def fijar(aut: Automata, aviso=None):
        estado["aut"] = aut
        estado["pasos"], estado["i"], estado["simulado"] = [], 0, None
        refrescar_vista()
        refrescar_simulacion()
        if aviso:
            avisar(aviso)
        page.update()

    # Importación y exportación
    lista_ejemplos = ft.Dropdown(label="Autómatas del repositorio", width=420, enable_filter=True,
                                 editable=True, options=[ft.DropdownOption(n) for n in ejemplos_disponibles()])

    def cargar_texto(texto, nombre_archivo):
        try:
            aut = desde_texto(texto, nombre_archivo)
        except (FormatoInvalido, AutomataInvalido, KeyError, TypeError) as err:
            avisar(f"No se pudo leer {nombre_archivo}: {err}", error=True)
            return
        preparar_tabla(aut=aut)
        fijar(aut, f"Cargado {nombre_archivo}: {aut.tipo} con {len(aut.estados)} estados.")
        pestanas.selected_index = 1
        page.update()

    def cargar_ejemplo(e):
        if lista_ejemplos.value:
            ruta = CARPETA_EJEMPLOS / lista_ejemplos.value
            cargar_texto(ruta.read_text(encoding="utf-8"), ruta.name)

    async def abrir_archivo(e):
        archivos = await selector.pick_files(allowed_extensions=["jff", "json", "xml"], with_data=True)
        if not archivos:
            return
        f = archivos[0]
        if f.bytes is not None:
            texto = bytes(f.bytes).decode("utf-8")
        elif f.path:
            texto = pathlib.Path(f.path).read_text(encoding="utf-8")
        else:
            avisar("El archivo no trajo contenido.", error=True)
            return
        cargar_texto(texto, f.name)

    def exportador(ext):
        async def exportar(e):
            aut = estado["aut"]
            if aut is None:
                avisar("Primero defina o cargue un autómata.", error=True)
                return
            nombre = (aut.nombre or "automata") + ext
            datos = a_texto(aut, nombre).encode("utf-8")
            ruta = await selector.save_file(file_name=nombre, src_bytes=datos)
            # En escritorio save_file devuelve la ruta elegida; en web el navegador ya descargó.
            if ruta and not os.path.exists(ruta):
                pathlib.Path(ruta).write_bytes(datos)
            avisar(f"Guardado como {ruta or nombre}.")
        return exportar

    pestana_definir = ft.Column([
        ft.Text("Definición del autómata M = (Q, Σ, δ, q0, F)", size=20, weight=ft.FontWeight.BOLD),
        ft.Row([campo_sigma, campo_q, con_lambda], wrap=True),
        ft.Row([ft.Button("Generar o actualizar la tabla", icon=ft.Icons.TABLE_CHART, on_click=preparar_tabla),
                lista_inicial]),
        ft.Text("Estados de aceptación F:"), fila_finales,
        ft.Text("Función de transición: escriba en cada celda los destinos separados por comas "
                "(vacío = ∅). La columna λ es la de las transiciones λ.", italic=True),
        contenedor_tabla,
        ft.Row([ft.FilledButton("Aplicar definición", icon=ft.Icons.CHECK, on_click=aplicar)]),
        mensajes,
        ft.Divider(),
        ft.Text("Importar y exportar", size=18, weight=ft.FontWeight.BOLD),
        ft.Row([ft.Button("Abrir .jff / .json / .xml", icon=ft.Icons.UPLOAD_FILE, on_click=abrir_archivo),
                lista_ejemplos, ft.Button("Cargar", on_click=cargar_ejemplo)], wrap=True),
        ft.Row([ft.Button("Guardar .jff", icon=ft.Icons.SAVE, on_click=exportador(".jff")),
                ft.Button("Guardar .json", icon=ft.Icons.SAVE, on_click=exportador(".json")),
                ft.Button("Guardar .xml", icon=ft.Icons.SAVE, on_click=exportador(".xml"))], wrap=True),
    ], spacing=10)

    # ------------------------------------------------------------------
    # Pestaña 2: representación visual y conversiones
    # ------------------------------------------------------------------
    vista = ft.Column(spacing=10)

    def convertir(como):
        def accion(e):
            aut = estado["aut"]
            if aut is None:
                return
            try:
                if como == "lambda":
                    nuevo = aut.sin_lambda(nombre=f"{aut.nombre}_sin_lambda")
                elif como == "afd":
                    nuevo = aut.subconjuntos(nombre=f"{aut.nombre}_afd")
                elif como == "min":
                    nuevo = aut.minimizar(nombre=f"{aut.nombre}_min")
                else:
                    nuevo = aut.numerar(nombre=aut.nombre)
            except AutomataInvalido as err:
                avisar(str(err), error=True)
                return
            preparar_tabla(aut=nuevo)
            fijar(nuevo, f"Resultado: {nuevo.tipo} con {len(nuevo.estados)} estados "
                         f"(antes {len(aut.estados)}). Lenguaje {'igual' if nuevo.equivalente(aut) else 'DISTINTO'}.")
        return accion

    def refrescar_vista(activos=frozenset(), recientes=()):
        aut = estado["aut"]
        if aut is None:
            vista.controls = [ft.Text("Defina o cargue un autómata en la primera pestaña.")]
            return
        vista.controls = [
            ft.Text(f"{aut.nombre or 'Autómata'} — {aut.tipo}", size=20, weight=ft.FontWeight.BOLD),
            ft.Row([ft.Button("Quitar λ (AFND-λ → AFND)", on_click=convertir("lambda")),
                    ft.Button("Subconjuntos (→ AFD)", on_click=convertir("afd")),
                    ft.Button("Minimizar (Hopcroft)", on_click=convertir("min")),
                    ft.Button("Renombrar q0, q1, …", on_click=convertir("numerar"))], wrap=True),
            ft.Row([diagrama(aut, activos, recientes)], scroll=ft.ScrollMode.AUTO),
            ft.Row([tabla_control(aut)], scroll=ft.ScrollMode.AUTO),
            ft.Text(resumen_quintupla(aut), selectable=True, font_family="monospace", size=12),
        ]
        if aut.tiene_lambda:
            vista.controls.append(ft.Text(
                "λ-clausuras: " + "; ".join(f"Cl({q}) = {mostrar_conjunto(aut.clausura(q))}" for q in aut.estados),
                selectable=True))

    # ------------------------------------------------------------------
    # Pestaña 3: simulación paso a paso
    # ------------------------------------------------------------------
    campo_cadena = ft.TextField(label="Cadena w (vacía = λ)", width=320)
    modo = ft.RadioGroup(value=TODOS_LOS_CAMINOS, content=ft.Row([
        ft.Radio(value=TODOS_LOS_CAMINOS, label="Seguir todos los caminos (conjuntos de estados)"),
        ft.Radio(value=CONVERTIR_A_AFD, label="Convertir a AFD y simular el AFD"),
    ]))
    veredicto = ft.Text(size=18, weight=ft.FontWeight.BOLD)
    paso_actual = ft.Text(selectable=True, size=14)
    lista_traza = ft.Column(spacing=2)
    lista_caminos = ft.Column(spacing=2)
    diagrama_sim = ft.Row(scroll=ft.ScrollMode.AUTO)

    def automata_a_simular():
        aut = estado["aut"]
        if modo.value == CONVERTIR_A_AFD and not aut.es_determinista:
            return aut.subconjuntos(nombre=f"{aut.nombre}_afd")
        return aut

    def iniciar(e=None):
        aut = estado["aut"]
        if aut is None:
            avisar("Primero defina o cargue un autómata.", error=True)
            return None
        simulado = automata_a_simular()
        w = campo_cadena.value or ""
        fuera = [s for s in simulado.simbolos(w) if s not in simulado.alfabeto]
        if fuera:
            avisar(f"Símbolos fuera de Σ: {', '.join(sorted(set(fuera)))}. La cadena se rechazará.", error=True)
        estado.update(simulado=simulado, cadena=w, pasos=simulado.traza(w), i=0)
        lista_caminos.controls = []
        return simulado

    def validar(e):
        simulado = iniciar()
        if simulado is None:
            return
        estado["i"] = len(estado["pasos"]) - 1
        refrescar_simulacion(mostrar_caminos=True)
        page.update()

    def mover(delta):
        def accion(e):
            if not estado["pasos"] or estado["cadena"] != (campo_cadena.value or ""):
                if iniciar() is None:
                    return
                if delta > 0:
                    estado["i"] = 0
                    refrescar_simulacion()
                    page.update()
                    return
            estado["i"] = max(0, min(len(estado["pasos"]) - 1, estado["i"] + delta))
            refrescar_simulacion(mostrar_caminos=estado["i"] == len(estado["pasos"]) - 1)
            page.update()
        return accion

    def refrescar_simulacion(mostrar_caminos=False):
        simulado, pasos, i = estado["simulado"], estado["pasos"], estado["i"]
        if simulado is None or not pasos:
            veredicto.value = paso_actual.value = ""
            lista_traza.controls, lista_caminos.controls, diagrama_sim.controls = [], [], []
            return
        p = pasos[i]
        total = len(pasos) - 1
        simbolos = simulado.simbolos(estado["cadena"])
        leido, resto = simbolos[:i], simbolos[i:]
        texto = (f"Paso {i} de {total}. Leído: {mostrar_cadena(leido)} · Por leer: {mostrar_cadena(resto)}\n"
                 f"Estado(s) actual(es): {mostrar_conjunto(p.despues)}")
        if i > 0:
            texto += "\nTransición tomada: " + ("; ".join(f"δ({q}, {a}) ∋ {r}" for q, a, r in p.tomadas)
                                                 or f"ninguna: no hay δ(·, {p.simbolo}) desde {mostrar_conjunto(p.antes)}")
        if p.por_lambda:
            texto += "\nTransiciones λ seguidas: " + "; ".join(f"{q} -λ→ {r}" for q, _, r in p.por_lambda)
        paso_actual.value = texto
        if i == total:
            acepta = bool(p.despues & simulado.aceptacion)
            veredicto.value = f"«{mostrar_cadena(estado['cadena'])}» {'ACEPTADA' if acepta else 'RECHAZADA'}"
            veredicto.color = ft.Colors.GREEN_800 if acepta else ft.Colors.RED_800
        else:
            veredicto.value, veredicto.color = "Simulación en curso…", ft.Colors.BLUE_GREY_700
        lista_traza.controls = [ft.Text(
            f"{k}. " + (f"lee {x.simbolo}: " if k else "inicio: ") + f"{mostrar_conjunto(x.antes)} → "
            f"{mostrar_conjunto(x.despues)}", selectable=True,
            weight=ft.FontWeight.BOLD if k == i else None) for k, x in enumerate(pasos[: i + 1])]
        diagrama_sim.controls = [diagrama(simulado, p.despues, p.tomadas + p.por_lambda)]
        if mostrar_caminos and not simulado.es_determinista:
            caminos, truncado = simulado.caminos(estado["cadena"], limite=40)
            lista_caminos.controls = [ft.Text("Árbol de cómputo (todos los caminos):", weight=ft.FontWeight.BOLD)] + [
                ft.Text(("✔ " if c.acepta else ("✘ muere: " if c.leidos < len(simbolos) else "✘ ")) +
                        c.texto(simulado.inicial), selectable=True,
                        color=ft.Colors.GREEN_800 if c.acepta else ft.Colors.GREY_700) for c in caminos]
            if truncado:
                lista_caminos.controls.append(ft.Text("(se muestran solo los primeros 40 caminos)", italic=True))

    pestana_simular = ft.Column([
        ft.Text("Simulación y validación de cadenas", size=20, weight=ft.FontWeight.BOLD),
        ft.Row([campo_cadena, ft.FilledButton("Validar", icon=ft.Icons.PLAY_ARROW, on_click=validar)]),
        ft.Text("Para un autómata no determinista:"), modo,
        ft.Row([ft.Button("Reiniciar", icon=ft.Icons.RESTART_ALT, on_click=mover(-10 ** 6)),
                ft.Button("Paso anterior", icon=ft.Icons.NAVIGATE_BEFORE, on_click=mover(-1)),
                ft.Button("Siguiente paso", icon=ft.Icons.NAVIGATE_NEXT, on_click=mover(1)),
                ft.Button("Hasta el final", icon=ft.Icons.SKIP_NEXT, on_click=mover(10 ** 6))], wrap=True),
        veredicto, paso_actual, diagrama_sim,
        ft.Text("Traza del recorrido:", weight=ft.FontWeight.BOLD), lista_traza, lista_caminos,
    ], spacing=10)

    # ------------------------------------------------------------------
    # Pestaña 4: operaciones de la Práctica 1
    # ------------------------------------------------------------------
    entrada_w = ft.TextField(label="Cadena", width=260)
    salida_w = ft.Text(selectable=True)
    entrada_sigma = ft.TextField(label="Alfabeto (comas)", width=200, value="a, b")
    entrada_n = ft.TextField(label="Longitud máxima", width=150, value="3")
    salida_l = ft.Text(selectable=True)

    def desde_automata(e):
        if estado["aut"] is not None:
            entrada_sigma.value = ", ".join(estado["aut"].alfabeto)
            page.update()

    def operar_cadena(e):
        w = entrada_w.value or ""
        salida_w.value = (f"Prefijos: {mostrar(prefijos(w))}\n\nSufijos: {mostrar(sufijos(w))}\n\n"
                          f"Subcadenas: {mostrar(subcadenas(w))}")
        page.update()

    def operar_lenguaje(e):
        try:
            sigma = parsear_alfabeto(entrada_sigma.value or "")
            n = int(entrada_n.value)
            kleene, positiva = cerradura_kleene(sigma, n), cerradura_positiva(sigma, n)
            texto = f"Σ* hasta longitud {n} ({len(kleene)}): {mostrar(kleene)}\n\nΣ⁺ ({len(positiva)}): {mostrar(positiva)}"
            aut = estado["aut"]
            if aut is not None and set(sigma) == set(aut.alfabeto):
                aceptadas = [w for w in kleene if aut.acepta(w)]
                texto += f"\n\nDe Σ* hasta longitud {n}, L(M) contiene ({len(aceptadas)}): {mostrar(aceptadas)}"
            salida_l.value = texto
        except ValueError as err:
            salida_l.value = f"Error: {err}"
        page.update()

    pestana_lenguajes = ft.Column([
        ft.Text("Operaciones sobre cadenas y lenguajes (Práctica 1)", size=20, weight=ft.FontWeight.BOLD),
        ft.Row([entrada_w, ft.Button("Prefijos, sufijos y subcadenas", on_click=operar_cadena)], wrap=True),
        salida_w, ft.Divider(),
        ft.Row([entrada_sigma, entrada_n, ft.Button("Usar Σ del autómata", on_click=desde_automata),
                ft.Button("Cerraduras de Kleene y positiva", on_click=operar_lenguaje)], wrap=True),
        salida_l,
    ], spacing=10)

    pestanas = ft.Tabs(
        length=4,
        selected_index=0,
        content=ft.Column([
            ft.TabBar(tabs=[ft.Tab(label="1. Definir"), ft.Tab(label="2. Autómata"),
                            ft.Tab(label="3. Simular"), ft.Tab(label="4. Lenguajes")]),
            ft.TabBarView(controls=[
                ft.Container(ft.Column([pestana_definir], scroll=ft.ScrollMode.AUTO), padding=10),
                ft.Container(ft.Column([vista], scroll=ft.ScrollMode.AUTO), padding=10),
                ft.Container(ft.Column([pestana_simular], scroll=ft.ScrollMode.AUTO), padding=10),
                ft.Container(ft.Column([pestana_lenguajes], scroll=ft.ScrollMode.AUTO), padding=10),
            ], expand=True),
        ], expand=True),
        expand=True,
    )
    page.scroll = None
    page.add(pestanas)

    # Autómata inicial: el AFND-λ del Anexo 3.
    inicial = Automata("ab", ["q0", "q1"], "q0", ["q1"], [("q0", "a", "q1"), ("q0", "b", "q0"), ("q0", "", "q1")],
                       nombre="anexo3")
    preparar_tabla(aut=inicial)
    fijar(inicial)


if __name__ == "__main__":
    ft.run(main)
