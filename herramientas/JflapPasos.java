import java.awt.Color;
import java.awt.Component;
import java.awt.Container;
import java.awt.Font;
import java.awt.Graphics2D;
import java.awt.RenderingHints;
import java.awt.Window;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.Serializable;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import javax.imageio.ImageIO;
import javax.swing.AbstractButton;
import javax.swing.JFrame;
import javax.swing.JMenu;
import javax.swing.JMenuItem;
import javax.swing.JTextField;
import javax.swing.SwingUtilities;

/**
 * Simulación paso a paso en la ventana real de JFLAP 7.1 (Input > Step with Closure).
 *
 * Entrada: TSV con renglones  archivo.jff  cadena  salida.png. Para cada uno abre
 * el autómata, ingresa la cadena, pulsa Step una vez por símbolo y guarda todas
 * las vistas, una debajo de otra, en una sola imagen. Las ventanas se colocan
 * fuera de la pantalla para no interrumpir al usuario.
 */
public class JflapPasos {
    static final int ANCHO = 1000, ALTO = 640;
    static final double ESCALA = 0.5;

    static AbstractButton buscar(Container c, String texto) {
        for (Component h : c.getComponents()) {
            if (h instanceof AbstractButton && texto.equals(((AbstractButton) h).getText())) return (AbstractButton) h;
            if (h instanceof Container) {
                AbstractButton r = buscar((Container) h, texto);
                if (r != null) return r;
            }
        }
        return null;
    }

    static JTextField campo(Container c) {
        for (Component h : c.getComponents()) {
            if (h instanceof JTextField) return (JTextField) h;
            if (h instanceof Container) {
                JTextField r = campo((Container) h);
                if (r != null) return r;
            }
        }
        return null;
    }

    static BufferedImage foto(JFrame f) throws Exception {
        BufferedImage i = new BufferedImage(f.getWidth(), f.getHeight(), BufferedImage.TYPE_INT_RGB);
        SwingUtilities.invokeAndWait(() -> { Graphics2D g = i.createGraphics(); f.printAll(g); g.dispose(); });
        return i;
    }

    static void montaje(List<BufferedImage> fotos, String cadena, File destino) throws Exception {
        int w = (int) (ANCHO * ESCALA), h = (int) (ALTO * ESCALA), banda = 22;
        BufferedImage m = new BufferedImage(w, (h + banda) * fotos.size(), BufferedImage.TYPE_INT_RGB);
        Graphics2D g = m.createGraphics();
        g.setRenderingHint(RenderingHints.KEY_INTERPOLATION, RenderingHints.VALUE_INTERPOLATION_BICUBIC);
        g.setRenderingHint(RenderingHints.KEY_TEXT_ANTIALIASING, RenderingHints.VALUE_TEXT_ANTIALIAS_ON);
        for (int k = 0; k < fotos.size(); k++) {
            int y = k * (h + banda);
            g.setColor(new Color(40, 60, 90));
            g.fillRect(0, y, w, banda);
            g.setColor(Color.WHITE);
            g.setFont(new Font("SansSerif", Font.BOLD, 13));
            String leido = cadena.substring(0, Math.min(k, cadena.length()));
            g.drawString("JFLAP 7.1, Step with Closure. Paso " + k + " de " + (fotos.size() - 1)
                    + ". Leído: " + (leido.isEmpty() ? "λ" : leido) + "   (entrada: " + (cadena.isEmpty() ? "λ" : cadena) + ")",
                    8, y + 16);
            g.drawImage(fotos.get(k), 0, y + banda, w, h, null);
        }
        g.dispose();
        ImageIO.write(m, "png", destino);
    }

    static void uno(String jff, String cadena, File destino) throws Exception {
        Object aut = new file.XMLCodec().decode(new File(jff), null);
        JFrame[] marco = new JFrame[1];
        SwingUtilities.invokeAndWait(() -> marco[0] = gui.environment.FrameFactory.createFrame((Serializable) aut));
        JFrame f = marco[0];
        SwingUtilities.invokeAndWait(() -> { f.setLocation(-4000, -4000); f.setSize(ANCHO, ALTO); });
        Thread.sleep(500);
        JMenuItem opcion = null;
        for (int m = 0; m < f.getJMenuBar().getMenuCount(); m++) {
            JMenu menu = f.getJMenuBar().getMenu(m);
            for (int k = 0; menu != null && k < menu.getItemCount(); k++) {
                JMenuItem it = menu.getItem(k);
                if (it != null && it.getText() != null && it.getText().startsWith("Step with Closure")) opcion = it;
            }
        }
        if (opcion == null) {
            StringBuilder sb = new StringBuilder();
            for (int m = 0; m < f.getJMenuBar().getMenuCount(); m++) {
                JMenu menu = f.getJMenuBar().getMenu(m);
                sb.append(menu == null ? "null" : menu.getText()).append(":");
                for (int k = 0; menu != null && k < menu.getItemCount(); k++)
                    sb.append(menu.getItem(k) == null ? "-" : menu.getItem(k).getText()).append(",");
                sb.append(" | ");
            }
            throw new IllegalStateException("Sin opcion Step with Closure: " + sb);
        }
        final JMenuItem elegido = opcion;
        SwingUtilities.invokeLater(elegido::doClick);
        Thread.sleep(600);
        for (Window w : Window.getWindows()) {
            if (w.isVisible() && w != f && campo((Container) w) != null && buscar((Container) w, "OK") != null) {
                w.setLocation(-4000, -4000);
                JTextField t = campo((Container) w);
                SwingUtilities.invokeAndWait(() -> t.setText(cadena));
                AbstractButton ok = buscar((Container) w, "OK");
                SwingUtilities.invokeAndWait(ok::doClick);
            }
        }
        Thread.sleep(600);
        SwingUtilities.invokeAndWait(() -> { f.setSize(ANCHO, ALTO); f.validate(); });
        Thread.sleep(300);
        List<BufferedImage> fotos = new ArrayList<>();
        fotos.add(foto(f));
        AbstractButton paso = buscar(f.getContentPane(), "Step");
        for (int i = 1; i <= cadena.length(); i++) {
            SwingUtilities.invokeAndWait(paso::doClick);
            Thread.sleep(250);
            fotos.add(foto(f));
        }
        montaje(fotos, cadena, destino);
        SwingUtilities.invokeAndWait(f::dispose);
    }

    public static void main(String[] a) throws Exception {
        // JOptionPane usa el idioma del sistema ("Aceptar"); en inglés el botón es "OK", como en JFLAP.
        java.util.Locale.setDefault(java.util.Locale.ENGLISH);
        javax.swing.JComponent.setDefaultLocale(java.util.Locale.ENGLISH);
        SwingUtilities.invokeAndWait(gui.action.NewAction::showNew);
        for (Window w : Window.getWindows()) w.setVisible(false);
        for (String linea : Files.readAllLines(Paths.get(a[0]), StandardCharsets.UTF_8)) {
            String[] p = linea.split("\t", -1);
            if (p.length < 3) continue;
            try {
                uno(p[0], p[1], new File(p[2]));
                System.out.println("ok\t" + p[2]);
            } catch (Exception e) {
                System.out.println("error\t" + p[2] + "\t" + e);
                e.printStackTrace(System.out);
            }
            for (Window w : Window.getWindows()) if (w.isVisible()) w.dispose();
        }
        System.exit(0);
    }
}
