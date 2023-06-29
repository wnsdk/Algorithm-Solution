import sys
from itertools import product
from collections import deque

input = sys.stdin.readline
ans1 = ans2 = ans3 = 0

dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]

N, M = map(int, input().split())

# 벽 정보
matrix = [list(map(int, input().split())) for _ in range(M)]

# visited[y][x] : (y, x) 좌표의 방 번호 (값이 0이면 방문한 적 없음)
visited = [[0] * N for _ in range(M)]

# area[x] : x번째 방의 넓이 (1-based)
area = [0]

# adj[x] : x번째 방과 인접해 있는 방들의 번호 리스트
adj = [[]]


def bfs(sy, sx, num):
    global ans2
    adj.append([])
    q = deque()
    d = 0

    q.append((sy, sx))
    visited[sy][sx] = num

    while q:
        y, x = q.popleft()
        d += 1

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if not (0 <= ny < M and 0 <= nx < N):
                continue

            if visited[ny][nx]:
                # 인접한 방 정보 추가
                if visited[ny][nx] != num and visited[ny][nx] not in adj[num]:
                    adj[num].append(visited[ny][nx])
                continue

            if matrix[y][x] & (1 << k):
                continue

            q.append((ny, nx))
            visited[ny][nx] = num

    area.append(d)


for r, c in product(range(M), range(N)):
    if not visited[r][c]:
        ans1 += 1
        bfs(r, c, ans1)

ans2 = max(area)

for i in range(1, ans1 + 1):
    for j in adj[i]:
        ans3 = max(ans3, area[i] + area[j])

print(ans1)
print(ans2)
print(ans3)
