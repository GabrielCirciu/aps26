import sys

MOD = 1000000007

def generate_matrix(n, seed):
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = (seed * 42 + i * 7 + j * 3) % 100
    return matrix

def multiply_matrices(A, B, n):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if A[i][j] == 0:
                continue
            for k in range(n):
                result[i][k] = (result[i][k] + A[i][j] * B[j][k]) % MOD
    return result

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    m = int(input_data[ptr])
    ptr += 1

    seeds = [int(input_data[ptr + i]) for i in range(m)]
    ptr += m

    E = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            E[i][j] = int(input_data[ptr]) % MOD
            ptr += 1

    matrices = [generate_matrix(n, s) for s in seeds]

    prod = matrices[0]
    for mat in matrices[1:]:
        prod = multiply_matrices(prod, mat, n)

    if prod == E:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    solve()