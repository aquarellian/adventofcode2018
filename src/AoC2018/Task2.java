import java.io.*;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Task2 {
    public static void main(String[] args) throws IOException {

        File file = new File("resources/task2.txt");

        BufferedReader br = new BufferedReader(new FileReader(file));

        String st;
        long res = 0;
        Set<Long> freq = new HashSet<Long>();
        List<Long> seq = new ArrayList<>();
        freq.add(res);

        while ((st = br.readLine()) != null) {
            Long val = Long.valueOf(st);
            seq.add(val);
            res += val;

            if (freq.contains(res)) {
                System.out.println("found it");
                System.out.println(res);
                break;
            } else {
                freq.add(res);
            }
        }
        int i = 0;
        while(true){
            Long val = seq.get(i % seq.size());
            i++;
            res +=val;
            if (freq.contains(res)) {
                System.out.println("found it");
                System.out.println(res);
                break;
            } else {
                freq.add(res);
            }

        }

    }
}