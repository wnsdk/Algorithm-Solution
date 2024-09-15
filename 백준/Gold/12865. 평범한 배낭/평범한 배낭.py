import sys
input = sys.stdin.readline

n, k = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(n)]

# dp[x][y] : x번째 물건까지 담았고, 무게가 y일 경우 가치의 최댓값
dp = [[0] * (k + 1) for _ in range(n)]

if items[0][0] <= k:
    dp[0][items[0][0]] = items[0][1]

for i in range(1, n):
    w, v = items[i]

    for j in range(k + 1):
        # i번째 물건을 안 담는다.
        dp[i][j] = dp[i - 1][j]
        
        # i번째 물건을 담는다. (i번째 물건을 담았더니 무게가 j가 되어야 함)
        if j >= w:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - w] + v)        

print(max(dp[n - 1]))