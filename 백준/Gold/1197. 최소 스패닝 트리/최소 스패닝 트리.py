import heapq
import sys
input = sys.stdin.readline


def union(x, y):
    x = p[x]
    y = p[y]
    if x > y:
        p[x] = y
    else:
        p[y] = x


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def kruskal():
    ans = 0     # MST의 가중치 합
    cnt = 0     # 선택된 간선의 개수

    while cnt < V and h:
        # 최소 비용 간선 선택하기
        e, v1, v2 = heapq.heappop(h)

        # 사이클 발생하는지 확인하기
        if find(v1) == find(v2):
            continue

        union(v1, v2)
        ans += e
        cnt += 1

    return ans


V, E = map(int, input().split())

p = [i for i in range(V + 1)]  # 루트 노드
h = []  # 최소 힙
visited = [False] * (V + 1)

for _ in range(E):
    a, b, c = map(int, input().split())
    heapq.heappush(h, (c, a, b))

print(kruskal())
