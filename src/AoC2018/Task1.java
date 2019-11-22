import java.io.IOException;

public class Task1 {


    public static void main(String[] args) throws IOException {

//        System.out.println(new Solution().trap(new int[]{0,1,0,2,1,0,1,3,2,1,2,1}));
        System.out.println(new Solution().trap(new int[]{2,0,1,0,2}));
    }
//        Scanner scan = new Scanner(System.in).useDelimiter("\n");
//        int i = scan.nextInt();
//        String ds = scan.next();
//
//        String s =  scan.next() + scan.nextLine();
//
//        if (!ds.contains(".")){
//            ds += ".0";
//        }
//
//        System.out.println("String: " + s);
////        System.out.println("Double: " +  new DecimalFormat("0.0#").format(d));
//        System.out.println("Double: " +  ds);
//        System.out.println("Int: " + i);
//        File file = new File("resources/task1.txt");
//        System.out.println(file.getAbsolutePath());
//
//        BufferedReader br = new BufferedReader(new FileReader(file));
//
//        String st;
//        long res = 0;
//
//        while ((st = br.readLine()) != null) {
//            res += Long.valueOf(st);
//        }
//        System.out.println(res);
//    }

    static class Solution {
        public int trap(int[] skyline) {

            int waterAmount = 0;
            if (skyline.length == 0 || skyline.length == 1) {
                return waterAmount;
            }

            int max1Index;
            int max2Index;

            // findNextLocalExtremumIndex will skip the 0 element, so check it manually
            if (skyline[0] > skyline[1]) {
                max1Index = 0;
            } else {
                max1Index = findNextLocalExtremumIndex(skyline, 0, true);
            }
//
//            do {
//                int localMinInBetween = findNextLocalExtremumIndex(skyline, max1Index, false);
//                max2Index = findNextLocalExtremumIndex(skyline, localMinInBetween, true);
//
//                if (max2Index != max1Index) {
//                    int maxWaterLine = Math.min(skyline[max1Index], skyline[max2Index]);
//                    for (int i = max1Index + 1; i < max2Index; i++) {
//                        waterAmount += maxWaterLine - skyline[i];
//                        skyline[i] = maxWaterLine; // drowned!
//                    }
//                    if (skyline[max2Index] > skyline[max1Index]){
//                        max1Index = max2Index;
//                    }
//                } else {
//                    break; // no more maximums - get out of the loop
//                }
//            } while (max2Index != max1Index || max2Index );

            // process new shape of skyline until fully drowned
            if (waterAmount != 0) { // no changes
                waterAmount += trap(skyline);
            }
            return waterAmount;
        }

        private static int findNextLocalExtremumIndex(int[] skyline, int startIndex, boolean max) { // exclusive for startIndex
            int index = startIndex;
            if (startIndex != -1) {
                while (index < skyline.length - 1  &&
                        (max ?  // local max or local min condition to be applied
                                skyline[index] <= skyline[index + 1] : // condition for finding a local max
                                skyline[index] >= skyline[index + 1])) { // condition for finding a local min
                    index++;
                }
            }
            return index;
        }
    }
}

