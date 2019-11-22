import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class Task3 {

    public static void main(String[] args) throws IOException {
        File file = new File("resources/task3.txt");
        int doubles = 0;
        int triples = 0;
        BufferedReader br = new BufferedReader(new FileReader(file));

        String st;

        while ((st = br.readLine()) != null) {
            Map<Character, Integer> char2count = new HashMap<Character, Integer>();
            for (int i = 0; i < st.length(); i++) {
                Character ch = st.charAt(i);
                char2count.put(ch, char2count.containsKey(ch)? char2count.get(ch) + 1 : 1);
            }
            boolean skipDoubles=false;
            boolean skipTriples=false;
            for (Character ch : char2count.keySet()){
                if (!skipDoubles&& char2count.get(ch) == 2){
                    doubles++;
                    skipDoubles = true;
                } else if (!skipTriples && char2count.get(ch) == 3){
                    triples++;
                    skipTriples = true;
                }
            }
        }
        System.out.println(doubles*triples);

    }
}
