n = int(input())
INF = float('inf')

# dp[x] : x원을 만들기 위해 필요한 최소 동전 개수
dp = [INF] * (n + 1)

if n >= 2:
    dp[2] = 1
    if n >= 4:
        dp[4] = 2
        if n >= 5:
            dp[5] = 1

for target in range(6, n + 1):
    # i는 5원의 개수
    for i in range(target // 5, -1, -1):
        rest = target - 5 * i

        if rest % 2 == 0:
            dp[target] = i + rest // 2
            break

print(dp[n] if dp[n] != INF else -1)
