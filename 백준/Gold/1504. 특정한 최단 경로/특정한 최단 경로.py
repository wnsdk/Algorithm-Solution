import sys
import heapq

INF = sys.maxsize / 10

input = sys.stdin.readline

# 정점 개수 N, 간선 개수 E (출발 노드는 1, 도착 노드는 N)
N, E = map(int, input().split())

adj = [[] for _ in range(N + 1)]

for _ in range(E):
    # a -> b 양방향 길 존재, 거리는 c
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))

# 반드시 거쳐야 하는 정점 2개
v1, v2 = map(int, input().split())

def dijstra(N, start, adj):
    distance = [INF] * (N + 1)
    distance[start] = 0

    h = []
    heapq.heappush(h, (0, start))

    while h:
        # 현재까지 밝혀진 경로 중, 가장 이동 거리가 짧은 노드
        dist1, now = heapq.heappop(h)

        # now 노드와 연결된 노드들 중에서
        for next, dist2 in adj[now]:
            cost = dist1 + dist2

            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(h, (cost, next))

    return distance

node1 = dijstra(N, 1, adj) # 노드 1에서 시작할 경우
nodeV1 = dijstra(N, v1, adj) # 노드 v1에서 시작할 경우
nodeV2 = dijstra(N, v2, adj) # 노드 v2에서 시작할 경우

ans1 = node1[v1] + nodeV1[v2] + nodeV2[N] # 1 -> v1 -> v2 -> N
ans2 = node1[v2] + nodeV2[v1] + nodeV1[N] # 1 -> v2 -> v1 -> N

ans = min(ans1, ans2)

print(ans if ans < INF else -1)
