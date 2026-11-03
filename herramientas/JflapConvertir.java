import automata.Automaton;
import automata.State;
import automata.Transition;
import automata.fsa.FSATransition;
import automata.fsa.FiniteStateAutomaton;
import automata.fsa.NFAToDFA;
import java.io.File;
import java.io.PrintWriter;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;

/**
 * Convierte cada AFN a AFD con la clase NFAToDFA de JFLAP 7.1, la misma que usa
 * el menú Convert > Convert to DFA. Entrada: un archivo con una ruta .jff por
 * renglón. Salida: un TSV con los estados (S) y transiciones (T) de cada AFD.
 * La etiqueta (label) de cada estado del AFD es el conjunto de estados del AFN.
 */
public class JflapConvertir {
    public static void main(String[] args) throws Exception {
        try (PrintWriter salida = new PrintWriter(args[1], "UTF-8")) {
            for (String ruta : Files.readAllLines(Paths.get(args[0]), StandardCharsets.UTF_8)) {
                if (ruta.isBlank()) continue;
                Automaton afn = (Automaton) new file.XMLCodec().decode(new File(ruta), null);
                FiniteStateAutomaton afd = new NFAToDFA().convertToDFA(afn);
                for (State s : afd.getStates()) {
                    salida.println(ruta + "\tS\t" + s.getName() + "\t" + (s.getLabel() == null ? "" : s.getLabel())
                            + "\t" + (s == afd.getInitialState()) + "\t" + afd.isFinalState(s));
                }
                for (Transition t : afd.getTransitions()) {
                    salida.println(ruta + "\tT\t" + t.getFromState().getName() + "\t" + t.getToState().getName()
                            + "\t" + ((FSATransition) t).getLabel());
                }
            }
        }
        System.exit(0);
    }
}
