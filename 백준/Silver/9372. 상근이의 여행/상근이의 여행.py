import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    # 국가의 수 N, 비행기 종류 M
    N, M = map(int, input().split())

    adj = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    ans = 0

    for _ in range(M):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    q = deque()
    q.append(1)
    visited[1] = True

    while q:
        now = q.popleft()

        for nxt in adj[now]:
            if not visited[nxt]:
                ans += 1
                visited[nxt] = True
                q.append(nxt)

    print(ans)
