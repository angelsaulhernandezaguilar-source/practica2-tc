import automata.Automaton;
import automata.AutomatonSimulator;
import automata.SimulatorFactory;
import automata.State;
import automata.Transition;
import automata.fsa.FSATransition;
import automata.fsa.FiniteStateAutomaton;
import automata.graph.FSAEqualityChecker;
import java.awt.Component;
import java.awt.Container;
import java.awt.Graphics2D;
import java.awt.Window;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.PrintWriter;
import java.io.Serializable;
import java.lang.reflect.Field;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.TreeSet;
import javax.imageio.ImageIO;
import javax.swing.AbstractButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JMenu;
import javax.swing.JMenuItem;
import javax.swing.SwingUtilities;

/**
 * Ejercicio 1 de la Práctica 3 en la ventana real de JFLAP 7.1.
 *
 * Entrada: TSV con renglones  archivo.jff  carpeta-de-salida  cadena1,cadena2,...
 * Para cada AFD:
 *   1. Abre el autómata y elige Convert > Convert FA to RE.
 *   2. Pulsa "Do It" hasta terminar (estado final único, transiciones combinadas,
 *      transiciones ∅ y eliminación de estados) y guarda una captura por paso, con
 *      el texto de JFLAP y la lista de transiciones del grafo generalizado.
 *   3. Pulsa "Export": JFLAP abre la expresión regular en una ventana nueva.
 *   4. En esa ventana elige Convert > Convert to NFA, pulsa "Do All" y "Export".
 *   5. Compara el AFN obtenido con el AFD original con FSAEqualityChecker, la
 *      clase que usa Test > Compare Equivalence, y simula las cadenas en ambos.
 * Salida en la carpeta: pasos.tsv, resultado.tsv y paso-NN.png, re-a-afn.png.
 */
public class JflapER {
    static final int ANCHO = 900, ALTO = 620;

    static AbstractButton boton(Container c, String texto) {
        for (Component h : c.getComponents()) {
            if (h instanceof AbstractButton && texto.equals(((AbstractButton) h).getText())) return (AbstractButton) h;
            if (h instanceof Container) {
                AbstractButton r = boton((Container) h, texto);
                if (r != null) return r;
            }
        }
        return null;
    }

    static void etiquetas(Container c, List<String> salida) {
        for (Component h : c.getComponents()) {
            if (h instanceof JLabel && ((JLabel) h).getText() != null && !((JLabel) h).getText().isBlank())
                salida.add(((JLabel) h).getText());
            if (h instanceof Container) etiquetas((Container) h, salida);
        }
    }

    static JMenuItem opcion(JFrame f, String inicio) {
        for (int m = 0; m < f.getJMenuBar().getMenuCount(); m++) {
            JMenu menu = f.getJMenuBar().getMenu(m);
            for (int k = 0; menu != null && k < menu.getItemCount(); k++) {
                JMenuItem it = menu.getItem(k);
                if (it != null && it.getText() != null && it.getText().startsWith(inicio)) return it;
            }
        }
        throw new IllegalStateException("No está la opción " + inicio);
    }

    static Object campo(Object o, String nombre) throws Exception {
        for (Class<?> c = o.getClass(); c != null; c = c.getSuperclass()) {
            try {
                Field f = c.getDeclaredField(nombre);
                f.setAccessible(true);
                return f.get(o);
            } catch (NoSuchFieldException e) { /* sigue con la superclase */ }
        }
        throw new NoSuchFieldException(nombre);
    }

    static void foto(JFrame f, File destino) throws Exception {
        BufferedImage i = new BufferedImage(f.getWidth(), f.getHeight(), BufferedImage.TYPE_INT_RGB);
        SwingUtilities.invokeAndWait(() -> { Graphics2D g = i.createGraphics(); f.printAll(g); g.dispose(); });
        ImageIO.write(i, "png", destino);
    }

    static JFrame nuevaVentana(List<Window> antes) throws Exception {
        for (int intento = 0; intento < 30; intento++) {
            for (Window w : Window.getWindows())
                if (w instanceof gui.environment.EnvironmentFrame && w.isVisible() && !antes.contains(w)) return (JFrame) w;
            Thread.sleep(200);
        }
        throw new IllegalStateException("JFLAP no abrió la ventana esperada");
    }

    static void colocar(JFrame f) throws Exception {
        SwingUtilities.invokeAndWait(() -> { f.setLocation(-4000, -4000); f.setSize(ANCHO, ALTO); f.validate(); });
        Thread.sleep(400);
    }

    static String nombre(State s) {
        return s.getName() == null ? "q" + s.getID() : s.getName();
    }

    static String grafo(Automaton a) {
        List<String> t = new ArrayList<>();
        for (Transition x : a.getTransitions()) {
            String l = ((FSATransition) x).getLabel();
            t.add(nombre(x.getFromState()) + " -[" + (l.isEmpty() ? "λ" : l) + "]→ " + nombre(x.getToState()));
        }
        java.util.Collections.sort(t);
        return String.join("; ", t);
    }

    static TreeSet<String> estados(Automaton a) {
        TreeSet<String> r = new TreeSet<>();
        for (State s : a.getStates()) r.add(nombre(s));
        return r;
    }

    static void uno(String jff, File carpeta, String[] cadenas) throws Exception {
        carpeta.mkdirs();
        FiniteStateAutomaton original = (FiniteStateAutomaton) new file.XMLCodec().decode(new File(jff), null);
        FiniteStateAutomaton copia = (FiniteStateAutomaton) new file.XMLCodec().decode(new File(jff), null);
        JFrame[] marco = new JFrame[1];
        SwingUtilities.invokeAndWait(() -> marco[0] = gui.environment.FrameFactory.createFrame((Serializable) copia));
        JFrame f = marco[0];
        colocar(f);
        JMenuItem convertir = opcion(f, "Convert FA to RE");
        SwingUtilities.invokeAndWait(convertir::doClick);
        Thread.sleep(800);
        colocar(f);
        AbstractButton hazlo = boton(f.getContentPane(), "Do It");
        AbstractButton exportar = boton(f.getContentPane(), "Export");
        Object controlador = campo(hazlo.getAction(), "val$controller");
        Automaton gtg = (Automaton) campo(controlador, "automaton");

        try (PrintWriter pasos = new PrintWriter(new java.io.OutputStreamWriter(
                new java.io.FileOutputStream(new File(carpeta, "pasos.tsv")), StandardCharsets.UTF_8), true)) {
            pasos.println("paso\tetapa\tdetalle\taccion\testados\ttransiciones");
            int k = 0;
            List<String> textos = new ArrayList<>();
            etiquetas(f.getContentPane(), textos);
            pasos.println(k + "\t" + textos.get(0) + "\t" + (textos.size() > 1 ? textos.get(1) : "") + "\tinicio\t"
                    + estados(gtg) + "\t" + grafo(gtg));
            foto(f, new File(carpeta, String.format("paso-%02d.png", k)));
            State nuevoFinal = null;
            List<State> viejosFinales = new ArrayList<>(Arrays.asList(gtg.getFinalStates()));
            while (!"Generalized Transition Graph Finished!".equals(textos.get(0)) && k < 80) {
                String detalle = textos.size() > 1 ? textos.get(1) : "";
                String accion;
                if (detalle.startsWith("Create a new state")) {
                    viejosFinales = new ArrayList<>(Arrays.asList(gtg.getFinalStates()));
                    nuevoFinal = (State) llamar(controlador, "stateCreate", new Class<?>[]{java.awt.Point.class},
                            new java.awt.Point(600, 400));
                    accion = "Se crea el estado final único " + nombre(nuevoFinal);
                } else if (detalle.contains("transitions from old final states")) {
                    State v = null;
                    for (State s : viejosFinales)
                        if (gtg.getTransitionsFromStateToState(s, nuevoFinal).length == 0) { v = s; break; }
                    llamar(controlador, "transitionCreate", new Class<?>[]{State.class, State.class}, v, nuevoFinal);
                    accion = "Transición λ de " + nombre(v) + " al nuevo final " + nombre(nuevoFinal);
                } else if (detalle.startsWith("Use the collapse tool")) {
                    State[] par = parRepetido(gtg);
                    llamar(controlador, "transitionCollapse", new Class<?>[]{State.class, State.class}, par[0], par[1]);
                    accion = "Se combinan las transiciones de " + nombre(par[0]) + " a " + nombre(par[1]);
                } else if (detalle.startsWith("Put empty transitions")) {
                    State[] par = parVacio(gtg);
                    llamar(controlador, "transitionCreate", new Class<?>[]{State.class, State.class}, par[0], par[1]);
                    accion = "Transición ∅ de " + nombre(par[0]) + " a " + nombre(par[1]);
                } else if (detalle.startsWith("Use the collapse state tool")) {
                    State s = removible(gtg);
                    llamar(controlador, "stateCollapse", new Class<?>[]{State.class}, s);
                    Thread.sleep(300);
                    List<String> nuevas = new ArrayList<>();
                    for (Window w : Window.getWindows()) {
                        if (w instanceof gui.regular.TransitionWindow && w.isVisible()) {
                            w.setLocation(-4000, -4000);
                            for (Transition t : ((gui.regular.TransitionWindow) w).getTransitions())
                                nuevas.add(nombre(t.getFromState()) + " -[" + (((FSATransition) t).getLabel().isEmpty() ? "λ" : ((FSATransition) t).getLabel()) + "]→ "
                                        + nombre(t.getToState()));
                        }
                    }
                    llamar(controlador, "finalizeStateRemove", new Class<?>[]{});
                    for (Window w : Window.getWindows()) if (w instanceof gui.regular.TransitionWindow) w.dispose();
                    accion = "Se elimina " + nombre(s) + "; nuevas etiquetas: " + String.join("; ", nuevas);
                } else {
                    throw new IllegalStateException("Etapa desconocida: " + textos);
                }
                Thread.sleep(250);
                cerrarAvisos();
                k++;
                textos.clear();
                etiquetas(f.getContentPane(), textos);
                pasos.println(k + "\t" + textos.get(0) + "\t" + (textos.size() > 1 ? textos.get(1) : "") + "\t" + accion
                        + "\t" + estados(gtg) + "\t" + grafo(gtg));
                foto(f, new File(carpeta, String.format("paso-%02d.png", k)));
            }
        }
        String er = (String) campo(controlador, "computedRE");

        // Export: la expresión en una ventana nueva; ahí Convert to NFA, Do All y Export.
        List<Window> ventanas = new ArrayList<>(Arrays.asList(Window.getWindows()));
        SwingUtilities.invokeAndWait(exportar::doClick);
        JFrame fre = nuevaVentana(ventanas);
        colocar(fre);
        foto(fre, new File(carpeta, "expresion.png"));
        SwingUtilities.invokeAndWait(opcion(fre, "Convert to NFA")::doClick);
        Thread.sleep(800);
        colocar(fre);
        SwingUtilities.invokeAndWait(boton(fre.getContentPane(), "Do All")::doClick);
        Thread.sleep(500);
        foto(fre, new File(carpeta, "re-a-afn.png"));
        ventanas = new ArrayList<>(Arrays.asList(Window.getWindows()));
        SwingUtilities.invokeAndWait(boton(fre.getContentPane(), "Export")::doClick);
        JFrame fafn = nuevaVentana(ventanas);
        colocar(fafn);
        foto(fafn, new File(carpeta, "afn.png"));
        FiniteStateAutomaton afn = (FiniteStateAutomaton) ((gui.environment.EnvironmentFrame) fafn).getEnvironment().getObject();
        boolean iguales = new FSAEqualityChecker().equals(original, afn);
        // Segunda comparación: el mismo AFD sin los estados desde los que no se llega a F (sumideros).
        FiniteStateAutomaton sinSumidero = (FiniteStateAutomaton) new file.XMLCodec().decode(new File(jff), null);
        List<State> sumideros = new ArrayList<>();
        for (State s : sinSumidero.getStates()) if (!llegaAFinal(sinSumidero, s)) sumideros.add(s);
        List<String> nombresSumideros = new ArrayList<>();
        for (State s : sumideros) { nombresSumideros.add(nombre(s)); sinSumidero.removeState(s); }
        boolean igualesSinSumidero = new FSAEqualityChecker().equals(sinSumidero, afn);

        try (PrintWriter r = new PrintWriter(new File(carpeta, "resultado.tsv"), "UTF-8")) {
            r.println("expresion\t" + er);
            r.println("equivalentes\t" + iguales);
            r.println("estados_afn\t" + afn.getStates().length);
            r.println("sumideros\t" + String.join(",", nombresSumideros));
            r.println("equivalentes_sin_sumidero\t" + igualesSinSumidero);
            AutomatonSimulator s1 = SimulatorFactory.getSimulator(original);
            AutomatonSimulator s2 = SimulatorFactory.getSimulator(afn);
            for (String w : cadenas) {
                String x = w.equals("λ") ? "" : w;
                r.println("cadena\t" + w + "\t" + s1.simulateInput(x) + "\t" + s2.simulateInput(x));
            }
        }
        for (Window w : Window.getWindows()) if (w.isVisible()) w.dispose();
    }

    static boolean llegaAFinal(Automaton a, State inicio) {
        List<State> pila = new ArrayList<>(List.of(inicio));
        java.util.Set<State> vistos = new java.util.HashSet<>(pila);
        while (!pila.isEmpty()) {
            State q = pila.remove(pila.size() - 1);
            if (a.isFinalState(q)) return true;
            for (Transition t : a.getTransitionsFromState(q))
                if (vistos.add(t.getToState())) pila.add(t.getToState());
        }
        return false;
    }

    /** Cierra los JOptionPane que abra JFLAP y escribe su texto (no debería haber ninguno). */
    static void cerrarAvisos() throws Exception {
        for (Window w : Window.getWindows()) {
            if (w instanceof javax.swing.JDialog && w.isVisible()) {
                List<String> t = new ArrayList<>();
                etiquetas((Container) w, t);
                System.out.println("aviso\t" + t);
                AbstractButton ok = boton((Container) w, "OK");
                if (ok != null) SwingUtilities.invokeAndWait(ok::doClick);
                else SwingUtilities.invokeAndWait(w::dispose);
            }
        }
    }

    static Object llamar(Object o, String metodo, Class<?>[] tipos, Object... args) throws Exception {
        Object[] r = new Object[1];
        Exception[] error = new Exception[1];
        SwingUtilities.invokeAndWait(() -> {
            try {
                r[0] = o.getClass().getMethod(metodo, tipos).invoke(o, args);
            } catch (Exception e) { error[0] = e; }
        });
        if (error[0] != null) throw error[0];
        return r[0];
    }

    static State[] parRepetido(Automaton a) {
        for (State p : a.getStates())
            for (State q : a.getStates())
                if (a.getTransitionsFromStateToState(p, q).length > 1) return new State[]{p, q};
        throw new IllegalStateException("No hay transiciones repetidas");
    }

    static State[] parVacio(Automaton a) {
        for (State p : a.getStates())
            for (State q : a.getStates())
                if (a.getTransitionsFromStateToState(p, q).length == 0) return new State[]{p, q};
        throw new IllegalStateException("No faltan transiciones");
    }

    /** El estado que se elimina: el primero (por nombre) que no es inicial ni final. */
    static State removible(Automaton a) {
        State elegido = null;
        for (State s : a.getStates())
            if (s != a.getInitialState() && !a.isFinalState(s) && (elegido == null || nombre(s).compareTo(nombre(elegido)) < 0))
                elegido = s;
        return elegido;
    }

    static void invocar(Object o, String metodo) {
        try {
            java.lang.reflect.Method m = o.getClass().getMethod(metodo);
            m.invoke(o);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public static void main(String[] a) throws Exception {
        java.util.Locale.setDefault(java.util.Locale.ENGLISH);
        javax.swing.JComponent.setDefaultLocale(java.util.Locale.ENGLISH);
        SwingUtilities.invokeAndWait(gui.action.NewAction::showNew);
        for (Window w : Window.getWindows()) w.setVisible(false);
        for (String linea : Files.readAllLines(Paths.get(a[0]), StandardCharsets.UTF_8)) {
            String[] p = linea.split("\t", -1);
            if (p.length < 3) continue;
            try {
                uno(p[0], new File(p[1]), p[2].split(","));
                System.out.println("ok\t" + p[0]);
            } catch (Exception e) {
                System.out.println("error\t" + p[0] + "\t" + e);
                e.printStackTrace(System.out);
            }
        }
        System.exit(0);
    }
}
