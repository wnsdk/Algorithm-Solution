import sys
from collections import deque

input = sys.stdin.readline
n, m, v = map(int, input().split())


def dfs(x):
    chk[x] = True
    print(x, end=' ')

    for nx in adj[x]:
        if not chk[nx]:
            dfs(nx)


def bfs(s):
    q = deque()
    q.append(s)
    chk[s] = True

    while q:
        x = q.popleft()
        print(x, end= ' ')

        for nx in adj[x]:
            if not chk[nx]:
                q.append(nx)
                chk[nx] = True


adj = [[] for _ in range(n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    adj[i].append(j)
    adj[j].append(i)

for i in range(1, n + 1):
    adj[i].sort()

chk = [False] * (n + 1)
dfs(v)
print()

chk = [False] * (n + 1)
bfs(v)