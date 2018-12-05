import java.io.*;

public class Task1 {
    public static void main(String[] args) throws IOException {
        File file = new File("resources/task1.txt");
        System.out.println(file.getAbsolutePath());

        BufferedReader br = new BufferedReader(new FileReader(file));

        String st;
        long res = 0;

        while ((st = br.readLine()) != null) {
            res += Long.valueOf(st);
        }
        System.out.println(res);
    }
}

