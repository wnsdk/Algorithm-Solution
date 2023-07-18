import sys
from collections import deque

input = sys.stdin.readline

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

n, m = map(int, input().split())

campus = []
ans = 0
sy = sx = -1

for i in range(n):
    arr = list(input())
    campus.append(arr)
    if 'I' in arr:
        sy = i
        sx = arr.index('I')

q = deque()
visited = [[False] * m for _ in range(n)]

q.append([sy, sx])
visited[sy][sx] = True

while q:
    y, x = q.popleft()

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]

        if 0 <= ny < n and 0 <= nx < m and campus[ny][nx] != 'X' and not visited[ny][nx]:
            if campus[ny][nx] == 'P':
                ans += 1
            q.append([ny, nx])
            visited[ny][nx] = True

print(ans if ans else 'TT')
