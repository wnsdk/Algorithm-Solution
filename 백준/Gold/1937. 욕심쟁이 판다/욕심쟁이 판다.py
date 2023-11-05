import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

ans = 0
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

# dp[y][x] : (y, x)에서 출발했을 때 앞으로 이동할 수 있는 거리
dp = [[-1] * n for _ in range(n)]


def solve(y, x):
    alpha = 0

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]

        if 0 <= ny < n and 0 <= nx < n and matrix[y][x] < matrix[ny][nx]:
            # 이미 탐색이 완료된 칸이라면
            if dp[ny][nx] != -1:
                alpha = max(alpha, dp[ny][nx])

            # 아직 탐색이 안 된 칸이라면
            else:
                alpha = max(alpha, solve(ny, nx))

    dp[y][x] = alpha + 1
    return dp[y][x]


for sy in range(n):
    for sx in range(n):
        ans = max(ans, solve(sy, sx))

print(ans)