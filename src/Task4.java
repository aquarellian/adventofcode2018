import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Task4 {
    public static void main(String[] args) throws IOException {
        File file = new File("resources/task4.txt");
        int doubles = 0;
        int triples = 0;
        BufferedReader br = new BufferedReader(new FileReader(file));
        List<String> strings = new ArrayList<String>();
        String st;

        while ((st = br.readLine()) != null) {
            strings.add(st);
        }
        for (String s : strings) {
            for (int i = strings.indexOf(s)+1; i < strings.size(); i++) {
                String s2 = strings.get(i);
                if (s.length() == s2.length()) {
                    boolean disc1 = false;
                    boolean disc2 = false;
                    for (int j = 0; j < s2.length(); j++) {
                        boolean match = s.charAt(j) == s2.charAt(j);
                        if (!match) {
                            if (disc1) {
                                disc2 = true;
                                break;
                            } else {
                                disc1 = true;
                            }
                        }

                    }
                    if (!disc2) {
                        System.out.println("Found a pair:");
                        System.out.println(s);
                        System.out.println(s2);
                    }

                }
            }
        }

        System.out.println(doubles * triples);

    }
}
