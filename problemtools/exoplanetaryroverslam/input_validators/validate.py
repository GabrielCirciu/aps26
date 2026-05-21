import sys
import re

def validate():
    lines = sys.stdin.readlines()
    if len(lines) < 2:
        sys.exit(43)
    if not re.match(r"^[1-9]\d*\n$", lines[0]):
        sys.exit(43)
    N = int(lines[0])
    if not 1 <= N <= 400:
        sys.exit(43)
    if not re.match(r"^[1-9]\d*\n$", lines[1]):
        sys.exit(43)
    M = int(lines[1])
    if not 1 <= M <= 60:
        sys.exit(43)
    if len(lines) != 2 + M + N:
        sys.exit(43)
    seeds = []
    for i in range(2, 2 + M):
        if not re.match(r"^[1-9]\d*\n$", lines[i]):
            sys.exit(43)
        seed = int(lines[i])
        if not 1 <= seed <= 10**9:
            sys.exit(43)
        seeds.append(seed)
    if len(seeds) != len(set(seeds)):
        sys.exit(43)
    row_pattern = re.compile(rf"^(-?0|-?[1-9]\d*)( (-?0|-?[1-9]\d*)){{{N-1}}}\n$")
    last_row_pattern = re.compile(rf"^(-?0|-?[1-9]\d*)( (-?0|-?[1-9]\d*)){{{N-1}}}\n?$")
    for i in range(2 + M, 2 + M + N):
        pattern = last_row_pattern if i == len(lines) - 1 else row_pattern
        if not pattern.match(lines[i]):
            sys.exit(43)
    sys.exit(42)

if __name__ == '__main__':
    validate()