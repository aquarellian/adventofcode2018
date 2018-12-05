import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Task5 {
    public static void main(String[] args) throws IOException {
        File file = new File("resources/task5.txt");
        List<List<Integer>> claims = new ArrayList<List<Integer>>(1000);
        int count = 0;
        BufferedReader br = new BufferedReader(new FileReader(file));

        String claim;

        while ((claim = br.readLine()) != null) {
            String[] strs = claim.split(" ");
            String[] coords = strs[2].replace(":", "").split(",");
            int y = Integer.valueOf(coords[0]);
            int x = Integer.valueOf(coords[1]);
            String[] dims = strs[3].split("x");
            int w = Integer.valueOf(dims[0]);
            int h = Integer.valueOf(dims[1]);
            if (x+w > 1000){
                System.out.println("x:" + x+w);
            }
            if (y+h > 1000){
                System.out.println("y:" + y+h);
            }
            for (int i = x; i < x+w; i++){
                for (int j = y; j < y+h; j++){

                    claims[i][j] ++;
                    if (claims[i][j] == 2){
                        count++;
                    }
                }
            }
        }

        System.out.println(count);
    }
}
