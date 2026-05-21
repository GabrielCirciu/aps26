def rec(j, i):
    if j == 0:
        return 0
    if i == 0:
        return float("-inf")

    best = rec(j, i - 1)

    for s in range(1, i + 1):
        best = max(best, rec(j - 1, s - 1) + prefix[i] - prefix[s - 1])

    return best

n, k = map(int, input().split())
numbers = list(map(int, input().split()))

prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + numbers[i - 1]

print(rec(k, n))


