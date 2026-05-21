#include <iostream>
#include <vector>

using namespace std;

const long long MOD = 10007;
const long long A_LCG = 911382323;
const long long C_LCG = 972663749;

vector<vector<long long>> generate_matrix(int n, long long seed) {
    vector<vector<long long>> matrix(n, vector<long long>(n));

    long long x = seed % MOD;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            x = (A_LCG * x + C_LCG) % MOD;
            matrix[i][j] = x;
        }
    }

    return matrix;
}

vector<vector<long long>> multiply_matrices(
    const vector<vector<long long>>& A,
    const vector<vector<long long>>& B,
    int n
) {
    vector<vector<long long>> C(n, vector<long long>(n, 0));

    for (int i = 0; i < n; ++i) {
        for (int k = 0; k < n; ++k) {
            long long aik = A[i][k];
            if (aik == 0) continue;

            for (int j = 0; j < n; ++j) {
                C[i][j] = (C[i][j] + aik * B[k][j]) % MOD;
            }
        }
    }

    return C;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    vector<long long> seeds(M);
    for (int i = 0; i < M; ++i) {
        cin >> seeds[i];
    }

    vector<vector<long long>> E(N, vector<long long>(N));
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> E[i][j];
        }
    }

    vector<vector<long long>> P = generate_matrix(N, seeds[0]);

    for (int i = 1; i < M; ++i) {
        vector<vector<long long>> mat = generate_matrix(N, seeds[i]);
        P = multiply_matrices(P, mat, N);
    }

    cout << (P == E ? "YES\n" : "NO\n");

    return 0;
}