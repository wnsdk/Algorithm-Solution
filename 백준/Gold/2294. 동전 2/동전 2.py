import sys

INF = sys.maxsize
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort()

# dp[x] : 동전들로 x원을 만들 때, 가능한 가장 적은 동전 개수 (만들 수 없으면 -1)
dp = [INF] * (k + 1)

# coin들을 이용해서 i원을 만드려고 함
for i in range(1, k + 1):
    # 코인 1개 만으로 i원을 만들 수 있는 경우
    if i in set(coins):
        dp[i] = 1
        continue

    for coin in coins:
        if coin > i:
            break
        dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[k] if dp[k] < INF else -1)