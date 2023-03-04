n = int(input())
# dp[x][y] : x자리의 오르막 수의 제일 마지막 숫자가 y일 수 있는 경우의 수
dp = [[0] * 10 for _ in range(n + 1)]

for i in range(10):
    dp[1][i] = 1

for x in range(2, n + 1):
    for i in range(10):
        for j in range(i, 10):
            dp[x][i] += dp[x - 1][j]
            dp[x][i] %= 10007

print(sum(dp[n]) % 10007)