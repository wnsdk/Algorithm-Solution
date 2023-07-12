import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

n, m, x = map(int, input().split())

adj1 = [[] for _ in range(n + 1)]    # 정방향
adj2 = [[] for _ in range(n + 1)]   # 역방향

for _ in range(m):
    s, e, t = map(int, input().split())
    adj1[s].append([t, e])
    adj2[e].append([t, s])


def dijkstra(adj):
    # dp[x] : 시작 노드 ~ x 노드 거리
    dp = [INF] * (n + 1)
    h = []

    dp[x] = 0
    heapq.heappush(h, (0, x))

    while h:
        time, node = heapq.heappop(h)

        for ntime, nnode in adj[node]:
            tot = time + ntime
            if tot < dp[nnode]:
                dp[nnode] = tot
                heapq.heappush(h, (tot, nnode))

    return dp


dist1 = dijkstra(adj1)
dist2 = dijkstra(adj2)
ans = 0

for i in range(1, n + 1):
    ans = max(ans, dist1[i] + dist2[i])

print(ans)
