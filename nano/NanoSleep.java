public class NanoSleep {
    public static void main(String[] args) {
        int threads = 60;
        final int nanoSleep = 1; // 1 ns
        final int count = 100000; // 1000 executions per thread


        for (int i = 0; i < threads; i++) {
            new Thread(new Runnable() {
                @Override
                public void run() {
                    int counter = count;
                    while (counter > 0) {
                        long started = System.nanoTime();
                        try {
                            Thread.sleep(0, nanoSleep);
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                        System.out.println(System.nanoTime() - started);
                        counter--;
                    }
                }
            }).start();
        }
    }


}
