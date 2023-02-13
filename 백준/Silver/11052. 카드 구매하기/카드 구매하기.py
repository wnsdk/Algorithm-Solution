N = int(input())
P = [0] + list(map(int, input().split()))
# dp[i] : 카드 i개를 갖기 위해 지불하는 돈의 최댓값
dp = [0] * (N + 1)
dp[1] = P[1]

for i in range(2, N + 1):
    dp[i] = P[i]
    for j in range(i // 2 + 1):
        dp[i] = max(dp[i], dp[j] + dp[i - j])

print(dp[N])
