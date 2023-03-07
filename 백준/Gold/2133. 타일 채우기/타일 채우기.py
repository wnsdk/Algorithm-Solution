n = int(input())

# dp[x][0] : x번째 칸에 타일을 가로로 3개 둠
# dp[x][1] : x번째 칸에 타일을 세로로 둠 (시작)
# dp[x][2] : x번째 칸에 타일을 세로로 둠 (끝)
dp = [[0] * 3 for _ in range(n + 1)]

dp[1][0] = 1
dp[1][1] = 2
dp[1][2] = 0

for i in range(3, n + 1, 2):
    dp[i][0] = sum(dp[i - 2])
    dp[i][1] = sum(dp[i - 2]) * 2
    for j in range(1, i, 2):
        dp[i][2] += dp[j][1]

# print(*dp)
print(sum(dp[n - 1]))