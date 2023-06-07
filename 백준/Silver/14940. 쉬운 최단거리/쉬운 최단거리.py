from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

# n 세로 크기, m 가로 크기
n, m = map(int, input().split())

# '2'의 좌표
sy, sx = -1, -1

# 지형 입력 받기
board = []
for y in range(n):
    l = list(map(int, input().split()))
    if 2 in l:
        sx = l.index(2)
        sy = y

    board.append(l)


def isCoord(y, x):
    global n, m
    return 0 <= y < n and 0 <= x < m

def bfs(sy, sx):
    global board

    q = deque()
    q.append((sy, sx, 0))

    dist = [[-1] * m for _ in range(n)]
    dist[sy][sx] = 0

    while q:
        y, x, d = q.popleft()

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            nd = d + 1

            # board를 벗어나거나, 방문한 적이 있다면
            if not isCoord(ny, nx) or dist[ny][nx] != -1:
                continue

            # 이동할 수 있는 위치라면
            if board[ny][nx]:
                dist[ny][nx] = nd
                q.append((ny, nx, nd))

            # 이동할 수 없는 위치라면
            if not board[ny][nx]:
                dist[ny][nx] = 0

    return dist

ans = bfs(sy, sx)

for y in range(n):
    for x in range(m):
        print(ans[y][x] if board[y][x] else 0, end=' ')
    print()
