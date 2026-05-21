import sys

MOD = 1000000007
A_LCG = 911382323
C_LCG = 972663749

def generate_matrix(n, seed):
    x = seed % MOD
    matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            x = (A_LCG * x + C_LCG) % MOD
            matrix[i][j] = x

    return matrix

def multiply_matrices(A, B, n):
    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            aij = A[i][j]
            if aij == 0:
                continue
            for k in range(n):
                result[i][k] = (result[i][k] + aij * B[j][k]) % MOD

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
            E[i][j] = int(input_data[ptr])
            ptr += 1

    prod = generate_matrix(n, seeds[0])

    for seed in seeds[1:]:
        mat = generate_matrix(n, seed)
        prod = multiply_matrices(prod, mat, n)

    print("YES" if prod == E else "NO")

if __name__ == "__main__":
    solve()