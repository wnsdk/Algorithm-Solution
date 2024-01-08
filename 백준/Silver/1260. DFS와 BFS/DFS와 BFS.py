from collections import deque


def dfs(x):
    print(x, end=' ')
    visited[x] = True

    for y in range(1, n + 1):
        if not visited[y] and adj[x][y]:
            dfs(y)


def bfs(s):
    visited[s] = True

    q = deque()
    q.append(s)

    while q:
        x = q.popleft()
        print(x, end=' ')

        for y in range(1, n + 1):
            if not visited[y] and adj[x][y]:
                visited[y] = True
                q.append(y)


n, m, v = map(int, input().split())
adj = [[False] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    adj[a][b] = adj[b][a] = True

visited = [False] * (n + 1)
dfs(v)

print()
visited = [False] * (n + 1)
bfs(v)
