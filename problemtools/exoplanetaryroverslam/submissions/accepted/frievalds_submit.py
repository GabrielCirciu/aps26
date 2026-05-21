import sys
import random

A = 911382323
C = 972663749
MOD = 10007

"""JIT optimized
def generate_matrix(n, seed):
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        i_term = i * 7
        row = matrix[i]
        for j in range(n):
            row[j] = (seed * 42 + i_term + j * 3) % 100
    return matrix

def multiply_matrix_vector(matrix, vector, n):
    result = [0] * n
    for i in range(n):
        row = matrix[i]
        s = 0
        for j in range(n):
            s += row[j] * vector[j]
        result[i] = s % MOD
    return result
"""

"""Regular"""
def multiply_matrix_vector(matrix, vector, n):
    result = [0] * n
    for i in range(n):
        row = matrix[i]
        s = 0
        for j in range(n):
            s += row[j] * vector[j]
        result[i] = s % MOD
    return result

def solve():
    # Fast I/O: Read all inputs from stdin at once
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    m = int(input_data[ptr])
    ptr += 1
    
    # Read the m seeds
    seeds = [int(input_data[ptr + i]) for i in range(m)]
    ptr += m
    
    # Read the target matrix E and reduce modulo MOD on read
    E = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            E[i][j] = int(input_data[ptr])
            ptr += 1
    
    # Run Freivalds' Algorithm
    k_rounds = 10
    is_equal = True
    
    for _ in range(k_rounds):
        # Generate a standard random binary vector r in {0, 1}^N
        r = [random.randint(0, 1) for _ in range(n)]
        
        # 1. Compute E * r
        Er = multiply_matrix_vector(E, r, n)
        
        # 2. Compute M_1 * (M_2 * ... * (M_m * r)...) from right to left
        curr = r
        for seed in reversed(seeds):
            x = seed % MOD
            result = [0] * n

            for i in range(n):
                s = 0
                for j in range(n):
                    x = (A * x + C) % MOD
                    s += x * curr[j]
                result[i] = s % MOD

            curr = result
            
        # 3. Compare vectors
        if Er != curr:
            is_equal = False
            break
            
    if is_equal:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    solve()
