def dp(numbers, n, k):
    M_INF = -float('inf')

    pref = [0] * (n + 1)
    for i in range(1, n + 1):
        pref[i] = pref[i - 1] + numbers[i - 1]

    dp = [[M_INF for _ in range(n + 1)] for _ in range(k + 1)]

    for i in range(n + 1):
        dp[0][i] = 0

    for j in range(1, k + 1):
        best = M_INF
        for i in range(j, n + 1):
            best = max(best, dp[j - 1][i - 1] - pref[i - 1])
            dp[j][i] = max(dp[j][i - 1], pref[i] + best)

    return dp[k][n]

n, k = map(int, input().split())
numbers = list(map(int, input().split()))