def fibonacci(x):
    if dp[x]:
        return dp[x]
    if x < 2:
        return x
    dp[x] = fibonacci(x - 1) + fibonacci(x - 2)
    return dp[x]


n = int(input())
dp = [0] * (n + 1)
print(fibonacci(n))
