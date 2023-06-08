N = int(input())
board = []
for y in range(N):
    board.append(list(map(int, input().split())))

# dp[y][x] : (y, x) 위치까지 올 수 있는 경로의 수
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for y in range(N):
    for x in range(N):
        # (y, x) 위치
        for ny in range(y):
            if board[ny][x] == y - ny:
                dp[y][x] += dp[ny][x]
        
        for nx in range(x):
            if board[y][nx] == x - nx:
                dp[y][x] += dp[y][nx]

print(dp[N - 1][N - 1])