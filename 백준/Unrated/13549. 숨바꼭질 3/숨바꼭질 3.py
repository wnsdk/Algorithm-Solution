import heapq
import sys

INF = sys.maxsize

# 수빈이가 있는 위치 N, 동생이 있는 위치 K
N, K = map(int, input().split())

SIZE = max(N, K) + 2

adj = [[] for _ in range(SIZE)]

for i in range(SIZE):
    if i - 1 >= 0:
        adj[i].append((1, i - 1))
    if i + 1 < SIZE:
        adj[i].append((1, i + 1))
    if i * 2 < SIZE:
        adj[i].append((0, i * 2))

def dijstra(start, V, adj):
    h = []
    heapq.heappush(h, (0, start))

    # dist[x] : start에서 x로 가는 거리
    dist = [INF] * SIZE
    dist[start] = 0

    while h:
        dist1, now = heapq.heappop(h)

        for dist2, next in adj[now]:
            cost = dist1 + dist2

            if cost < dist[next]:
                heapq.heappush(h, (cost, next))
                dist[next] = cost

    return dist

dist = dijstra(N, SIZE, adj)
print(dist[K])
