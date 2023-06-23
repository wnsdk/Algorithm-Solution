import sys
import heapq

input = sys.stdin.readline
INF = float('inf')
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

# 가로 M, 세로 N
M, N = map(int, input().split())

miro = [list(map(int, list(input().strip()))) for _ in range(N)]


def isCoord(y, x):
    global N, M
    return 0 <= y < N and 0 <= x < M


# dp[y][x] : (y, x) 까지 오기 위해 벽을 부순 횟수의 최솟값
dp = [[INF] * M for _ in range(N)]

dp[0][0] = 0

h = []
heapq.heappush(h, (0, 0, 0))

while h:
    cnt, y, x = heapq.heappop(h)

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        ncnt = cnt

        if isCoord(ny, nx):
            # 벽이라면 벽 부순 횟수가 1 증가
            if miro[ny][nx] == 1:
                ncnt += 1

            if dp[ny][nx] > ncnt:
                dp[ny][nx] = ncnt
                heapq.heappush(h, (ncnt, ny, nx))

print(dp[N - 1][M - 1])