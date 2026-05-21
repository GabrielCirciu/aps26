import java.io.InputStream;
import java.io.IOException;

public class naive_verify {
    private static final int P = 10007;

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

    public static int[][] generateMatrix(int n, long seed) {
        int[][] matrix = new int[n][n];
        long x = seed;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                x = (911382323L * x + 972663749L) % P;
                matrix[i][j] = (int) x;
            }
        }
        return matrix;
    }

    public static int[][] multiplyMatrices(int[][] A, int[][] B, int n) {
        int[][] result = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (A[i][j] == 0) {
                    continue;
                }
                long aVal = A[i][j];
                int[] rowB = B[j];
                int[] rowRes = result[i];
                for (int k = 0; k < n; k++) {
                    rowRes[k] = (int) ((rowRes[k] + aVal * rowB[k]) % P);
                }
            }
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
                    E[i][j] = (int) ((val % P + P) % P);
                }
            }

            // Generate the chain matrices M_1 to M_m
            int[][][] matrices = new int[m][n][n];
            for (int i = 0; i < m; i++) {
                matrices[i] = generateMatrix(n, seeds[i]);
            }

            // Naively multiply them all sequentially
            int[][] prod = matrices[0];
            for (int i = 1; i < m; i++) {
                prod = multiplyMatrices(prod, matrices[i], n);
            }

            // Check if prod == E
            boolean isEqual = true;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (prod[i][j] != E[i][j]) {
                        isEqual = false;
                        break;
                    }
                }
                if (!isEqual) {
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
