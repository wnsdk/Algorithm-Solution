import sys, heapq
input = sys.stdin.readline

INF = float('inf')

# n 도시 개수, m 도로 수, k번째 최단 경로
n, m, k = map(int, input().split())

adj = [[] for _ in range(n + 1)]

for _ in range(m):
    # a 도시에서 b 도시로 c 시간 걸린다.
    a, b, c = map(int, input().split())
    adj[a].append((b, c))

distance = [[INF] * k for _ in range(n + 1)]
distance[1][0] = 0

h = []
heapq.heappush(h, (0, 1))

while h:
    # 최단 거리가 가장 짧은 노드 찾기
    dist1, now = heapq.heappop(h)

    # now 노드와 연결된 다른 인접한 노드들을 확인
    for next, dist2 in adj[now]:
        cost = dist1 + dist2

        # now 노드를 거쳐서 next 노드로 가는 경로를 추가하기
        if cost < distance[next][k - 1]:
            distance[next][k - 1] = cost
            distance[next].sort()
            heapq.heappush(h, (cost, next))

for i in range(1, n + 1):
    if distance[i][k - 1] == INF:
        print(-1)
    else:
        print(distance[i][k - 1])
