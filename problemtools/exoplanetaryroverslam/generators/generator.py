import random
import sys
import os
import numpy as np

A_LCG = 911382323
C_LCG = 972663749
MOD = 10007

def generate_matrix(n, seed):
    x = seed % MOD
    values = np.empty(n * n, dtype=np.int64)

    for idx in range(n * n):
        x = (A_LCG * x + C_LCG) % MOD
        values[idx] = x

    return values.reshape((n, n))

def multiply_matrices(A, B):
    return (A @ B) % MOD

def generate_test(n, m, correct):
    seeds = random.sample(range(1, 10**9 + 1), m)

    E = generate_matrix(n, seeds[0])

    for seed in seeds[1:]:
        M = generate_matrix(n, seed)
        E = multiply_matrices(E, M)

    if not correct:
        ri = random.randint(0, n - 1)
        rj = random.randint(0, n - 1)
        E[ri, rj] = (int(E[ri, rj]) + random.randint(1, 100)) % MOD

    input_lines = [str(n), str(m)]
    input_lines.extend(map(str, seeds))

    for i in range(n):
        input_lines.append(" ".join(map(str, E[i])))

    answer = "YES" if correct else "NO"
    return "\n".join(input_lines), answer

# run_ python3 generators/generator.py NAME N M yes OUTPUT_PATH SEED
# example: python3 generators/generator.py no2 200 30 no data/secret/group2 2
if __name__ == "__main__":
    name = sys.argv[1]
    n = int(sys.argv[2])
    m = int(sys.argv[3])
    correct = sys.argv[4].lower() == "yes"
    path = sys.argv[5]

    if len(sys.argv) > 6:
        random.seed(int(sys.argv[6]))

    os.makedirs(path, exist_ok=True)

    input_data, answer = generate_test(n, m, correct)

    with open(f"{path}/{name}.in", "w", newline="\n") as f:
        f.write(input_data + "\n")

    with open(f"{path}/{name}.ans", "w", newline="\n") as f:
        f.write(answer + "\n")