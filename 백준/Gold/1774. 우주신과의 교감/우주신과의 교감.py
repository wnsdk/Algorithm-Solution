import sys
import heapq
from itertools import product

input = sys.stdin.readline

# 우주신들의 개수 n, 이미 연결된 신들과의 통로 개수 m
n, m = map(int, input().split())

position = [[]] + [list(map(int, input().split())) for _ in range(n)]
adj = [[-1] * (n + 1) for _ in range(n + 1)]


def get_dist(pos1, pos2):
    x1, y1 = position[pos1]
    x2, y2 = position[pos2]
    return ((y1 - y2) ** 2 + (x1 - x2) ** 2) ** 0.5


# 이미 연결된 노드들
for _ in range(m):
    a, b = map(int, input().split())
    adj[a][b] = adj[b][a] = 0

# 아직 연결안 된 노드들
for a, b in product(range(1, n + 1), range(1, n + 1)):
    if a == b or adj[a][b] == 0:
        continue

    adj[a][b] = adj[b][a] = get_dist(a, b)


# 프림 알고리즘
# 최소 신장 트리(MST) 생성 알고리즘 - 모든 정점을 포함하고, 사용된 간선들의 합이 최소인 트리
tot = 0
visited = [False] * (n + 1)
h = []

# 1단계 : 임의 정점 선택 (1번 노드, 거리는 0)
heapq.heappush(h, (0, 1))

while h:
    # 2단계 : 인접 정점들 중 최소 비용 간선 선택
    weight, vertex = heapq.heappop(h)

    if visited[vertex]:
        continue

    tot += weight
    visited[vertex] = True

    # 선택된 정점과 연결된 정점들을 모두 힙에 추가
    for i in range(1, n + 1):
        d = adj[vertex][i]
        if d > -1 and not visited[i]:
            heapq.heappush(h, (d, i))

print(f"{round(tot, 2):.2f}")
