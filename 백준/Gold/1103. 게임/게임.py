import sys
from collections import deque

input = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]
ans = 0

n, m = map(int, input().split())
matrix = [list(input()) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]


def is_coord(y, x):
    return 0 <= y < n and 0 <= x < m


def bfs(sy, sx):
    global ans
    q = deque()

    q.append((sy, sx, [(sy, sx)]))
    dp[sy][sx] = 1

    while q:
        y, x, path = q.popleft()

        for k in range(4):
            ny = y + dy[k] * int(matrix[y][x])
            nx = x + dx[k] * int(matrix[y][x])
            new_path = path[:]

            # 현재 탐색 경로에 대해서, 방문한 적 있다면
            if (ny, nx) in new_path:
                ans = -1
                return

            new_path.append((ny, nx))

            # 동전이 보드의 바깥으로 나가거나 구멍에 빠질 경우 게임 종료
            if not is_coord(ny, nx) or matrix[ny][nx] == 'H':
                ans = max(ans, len(path))
                continue

            # (ny, nx) 좌표에 도달할 때 까지 걸린 거리(nd)가 기존에 찾아놓은 값(dp)보다 작다면 더이상 탐색할 필요 없음
            if dp[ny][nx] >= len(new_path):
                continue

            q.append((ny, nx, new_path))
            dp[ny][nx] = len(new_path)


bfs(0, 0)
print(ans)
