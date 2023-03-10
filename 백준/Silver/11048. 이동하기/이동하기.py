N, M = map(int, input().split())

# dp[y][x] : (y, x) 위치까지 왔을 때 가질 수 있는 최대 사탕 개수
dp = [list(map(int, input().split())) for _ in range(N)]

for y in range(N):
    for x in range(M):
        if not y and not x:
            continue
        elif not y:
            dp[0][x] += dp[0][x - 1]
        elif not x:
            dp[y][0] += dp[y - 1][0]
        else:
            dp[y][x] += max(dp[y - 1][x - 1], dp[y - 1][x], dp[y][x - 1])

print(dp[N - 1][M - 1])
