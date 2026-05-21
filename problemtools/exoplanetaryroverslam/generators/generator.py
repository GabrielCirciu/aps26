import random
import sys

A_LCG = 911382323
C_LCG = 972663749
MOD = 1000000007

def generate_matrix(n, seed):
    x = seed % MOD
    matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            x = (A_LCG * x + C_LCG) % MOD
            matrix[i][j] = x

    return matrix

def multiply_matrices(A, B, n):
    C = [[0] * n for _ in range(n)]

    for i in range(n):
        for k in range(n):
            aik = A[i][k]
            if aik == 0:
                continue
            for j in range(n):
                C[i][j] = (C[i][j] + aik * B[k][j]) % MOD

    return C

def generate_test(n, m, correct):
    seeds = random.sample(range(1, 10**9 + 1), m)
    matrices = [generate_matrix(n, s) for s in seeds]

    E = matrices[0]
    for i in range(1, m):
        E = multiply_matrices(E, matrices[i], n)

    if not correct:
        ri, rj = random.randint(0, n - 1), random.randint(0, n - 1)
        E[ri][rj] = (E[ri][rj] + random.randint(1, 100)) % MOD

    input_lines = []
    input_lines.append(str(n))
    input_lines.append(str(m))

    for s in seeds:
        input_lines.append(str(s))

    for row in E:
        input_lines.append(" ".join(map(str, row)))

    answer = "YES" if correct else "NO"
    return "\n".join(input_lines), answer


# run_ python3 generators/generator.py NAME N M yes OUTPUT_PATH SEED
# example: python3 generators/generator.py 1 4 2 yes data/sample 2
if __name__ == "__main__":
    name = sys.argv[1]
    n = int(sys.argv[2])
    m = int(sys.argv[3])
    correct = sys.argv[4].lower() == "yes"
    path = sys.argv[5]

    if len(sys.argv) > 6:
        random.seed(int(sys.argv[6]))

    input_data, answer = generate_test(n, m, correct)

    with open(f"{path}/{name}.in", "w") as f:
        f.write(input_data + "\n")

    with open(f"{path}/{name}.ans", "w") as f:
        f.write(answer + "\n")