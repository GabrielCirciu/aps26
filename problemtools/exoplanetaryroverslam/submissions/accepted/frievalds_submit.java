import java.io.InputStream;
import java.io.IOException;
import java.util.Random;

public class frievalds_submit {
    private static final int MOD = 1000000007;

    static class FastReader {
        private static final int BUFFER_SIZE = 1 << 16;
        private final InputStream din;
        private final byte[] buffer;
        private int bufferPointer, bytesRead;

        public FastReader(InputStream in) {
            din = in;
            buffer = new byte[BUFFER_SIZE];
            bufferPointer = bytesRead = 0;
        }

        public int nextInt() throws IOException {
            int ret = 0;
            int c = read();
            while (c <= ' ' && c != -1) {
                c = read();
            }
            if (c == -1) {
                throw new IOException("EOF");
            }
            boolean neg = (c == '-');
            if (neg) {
                c = read();
            }
            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');

            if (neg) {
                return -ret;
            }
            return ret;
        }

        private void fillBuffer() throws IOException {
            bytesRead = din.read(buffer, bufferPointer = 0, BUFFER_SIZE);
        }

        private int read() throws IOException {
            if (bufferPointer == bytesRead) {
                fillBuffer();
            }
            if (bytesRead <= 0) {
                return -1;
            }
            return buffer[bufferPointer++] & 0xff;
        }
    }

    public static int[][] generateMatrix(int n, int seed) {
        int[][] matrix = new int[n][n];
        long seedL = seed;
        for (int i = 0; i < n; i++) {
            long iTerm = i * 7L;
            int[] row = matrix[i];
            for (int j = 0; j < n; j++) {
                row[j] = (int) ((seedL * 42 + iTerm + j * 3L) % 100);
            }
        }
        return matrix;
    }

    public static int[] multiplyMatrixVector(int[][] matrix, int[] vector, int n) {
        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            long s = 0;
            int[] row = matrix[i];
            for (int j = 0; j < n; j++) {
                s += (long) row[j] * vector[j];
                if (s >= 8000000000000000000L) {
                    s %= MOD;
                }
            }
            result[i] = (int) (s % MOD);
        }
        return result;
    }

    public static void main(String[] args) {
        try {
            FastReader reader = new FastReader(System.in);
            int n = reader.nextInt();
            int m = reader.nextInt();

            int[] seeds = new int[m];
            for (int i = 0; i < m; i++) {
                seeds[i] = reader.nextInt();
            }

            int[][] E = new int[n][n];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    long val = reader.nextInt();
                    E[i][j] = (int) ((val % MOD + MOD) % MOD);
                }
            }

            // Generate the chain matrices M_1 to M_m
            int[][][] matrices = new int[m][n][n];
            for (int i = 0; i < m; i++) {
                matrices[i] = generateMatrix(n, seeds[i]);
            }

            // Run Freivalds' Algorithm
            int kRounds = 10;
            boolean isEqual = true;
            Random rand = new Random();

            for (int r = 0; r < kRounds; r++) {
                // Generate a standard random binary vector r in {0, 1}^N
                int[] rv = new int[n];
                for (int i = 0; i < n; i++) {
                    rv[i] = rand.nextInt(2);
                }

                // 1. Compute E * rv
                int[] Er = multiplyMatrixVector(E, rv, n);

                // 2. Compute M_1 * (M_2 * ... * (M_m * rv)...) from right to left
                int[] curr = rv;
                for (int i = m - 1; i >= 0; i--) {
                    curr = multiplyMatrixVector(matrices[i], curr, n);
                }

                // 3. Compare vectors
                boolean match = true;
                for (int i = 0; i < n; i++) {
                    if (Er[i] != curr[i]) {
                        match = false;
                        break;
                    }
                }

                if (!match) {
                    isEqual = false;
                    break;
                }
            }

            if (isEqual) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }

        } catch (Exception e) {
            // Gracefully handle EOF or other exceptions
        }
    }
}
