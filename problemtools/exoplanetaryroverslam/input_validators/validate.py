import sys
import re

MOD = 10007

def validate():
    lines = sys.stdin.readlines()

    if len(lines) < 2:
        sys.exit(43)

    if not re.fullmatch(r"[1-9]\d*\n?", lines[0]):
        sys.exit(43)
    N = int(lines[0])
    if not 1 <= N <= 400:
        sys.exit(43)

    if not re.fullmatch(r"[1-9]\d*\n?", lines[1]):
        sys.exit(43)
    M = int(lines[1])
    if not 1 <= M <= 60:
        sys.exit(43)

    if len(lines) != 2 + M + N:
        sys.exit(43)

    seeds = []
    for i in range(2, 2 + M):
        if not re.fullmatch(r"[1-9]\d*\n?", lines[i]):
            sys.exit(43)

        seed = int(lines[i])
        if not 1 <= seed <= 10**9:
            sys.exit(43)

        seeds.append(seed)

    if len(seeds) != len(set(seeds)):
        sys.exit(43)

    for i in range(2 + M, 2 + M + N):
        parts = lines[i].strip().split()

        if len(parts) != N:
            sys.exit(43)

        for x in parts:
            if not re.fullmatch(r"0|[1-9]\d*", x):
                sys.exit(43)

            val = int(x)
            if not 0 <= val < MOD:
                sys.exit(43)

    sys.exit(42)

if __name__ == "__main__":
    validate()