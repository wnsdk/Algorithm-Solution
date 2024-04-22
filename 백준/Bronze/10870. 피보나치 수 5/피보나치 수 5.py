def fibonacci(x):
    if x < 2:
        return x
    if dp[x]:
        return dp[x]
    return fibonacci(x - 1) + fibonacci(x - 2)


n = int(input())
dp = [0] * (n + 1)
print(fibonacci(n))
