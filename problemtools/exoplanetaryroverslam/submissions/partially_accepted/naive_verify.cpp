#include <iostream>
#include <vector>

using namespace std;

const long long MOD = 1000000007;

vector<vector<long long>> generate_matrix(int n, long long seed) {
    vector<vector<long long>> matrix(n, vector<long long>(n));
    for (int i = 0; i < n; ++i) {
        long long i_term = i * 7;
        for (int j = 0; j < n; ++j) {
            matrix[i][j] = (seed * 42 + i_term + j * 3) % 100;
        }
    }
    return matrix;
}

vector<vector<long long>> multiply_matrices(const vector<vector<long long>>& m1, const vector<vector<long long>>& m2, int n) {
    vector<vector<long long>> res(n, vector<long long>(n, 0));
    for (int i = 0; i < n; ++i) {
        for (int k = 0; k < n; ++k) {
            long long m1_ik = m1[i][k];
            for (int j = 0; j < n; ++j) {
                res[i][j] = (res[i][j] + m1_ik * m2[k][j]) % MOD;
            }
        }
    }
    return res;
}

int main() {
    // Faster standard C++ I/O
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    // 1. Read seeds
    vector<long long> seeds(M);
    for (int i = 0; i < M; ++i) {
        cin >> seeds[i];
    }

    // 2. Read matrix E
    vector<vector<long long>> E(N, vector<long long>(N));
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> E[i][j];
            E[i][j] %= MOD;
        }
    }

    // 3. Generate the M matrices
    vector<vector<vector<long long>>> matrices;
    matrices.reserve(M);
    for (int i = 0; i < M; ++i) {
        matrices.push_back(generate_matrix(N, seeds[i]));
    }

    // 4. Naive matrix chain multiplication
    vector<vector<long long>> P = matrices[0];
    for (int i = 1; i < M; ++i) {
        P = multiply_matrices(P, matrices[i], N);
    }

    // 5. Compare P and E
    bool ok = true;
    for (int i = 0; i < N && ok; ++i) {
        for (int j = 0; j < N && ok; ++j) {
            if (P[i][j] != E[i][j]) {
                ok = false;
            }
        }
    }

    if (ok) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }

    return 0;
}
