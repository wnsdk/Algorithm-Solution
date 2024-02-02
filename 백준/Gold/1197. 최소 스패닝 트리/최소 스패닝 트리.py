import heapq
import sys
input = sys.stdin.readline


def prim():
    ans = 0

    # 임의의 정점을 선택한다.
    h = [(0, 1)]

    # 모든 정점이 선택될 때까지 반복한다.
    while h:
        # 인접 정점들 중 간선의 가중치가 제일 작은 정점을 선택한다.
        e, v = heapq.heappop(h)

        if visited[v]:
            continue

        visited[v] = True
        ans += e

        for nv, ne in adj[v]:
            if not visited[nv]:
                heapq.heappush(h, (ne, nv))

    return ans


V, E = map(int, input().split())

adj = [[] for _ in range(V + 1)]
visited = [False] * (V + 1)

for _ in range(E):
    a, b, c = map(int, input().split())
    adj[a].append([b, c])
    adj[b].append([a, c])

print(prim())
