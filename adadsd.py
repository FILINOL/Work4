def max_berry_collection(berries):
    n = len(berries)
    if n == 0:
        return 0
    elif n == 1:
        return berries[0]
    dp = [0] * n
    dp[0] = berries[0]
    dp[1] = max(berries[0], berries[1])
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + berries[i])
    return dp[n-1]
berries = [1, 2, 3, 4, 5]
max_berries_collected = max_berry_collection(berries)
print("Максимальное количество собранных ягод:", max_berries_collected)
