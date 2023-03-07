dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

M, N = map(int, input().split())
H = [list(map(int, input().split())) for _ in range(M)]

dp = [[-1] * N for _ in range(M)]
dp[M - 1][N - 1] = 1

def isCoord(y, x):
    global M, N
    return 0 <= y < M and 0 <= x < N

def dfs(y, x):
    if dp[y][x] > 0:
        return dp[y][x]

    if dp[y][x] == -1:
        dp[y][x] = 0
    else:
        return 0

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]

        if isCoord(ny, nx) and H[ny][nx] < H[y][x]:
            dp[y][x] += dfs(ny, nx)

    return dp[y][x]

print(dfs(0, 0))