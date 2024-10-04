import heapq
import sys
input = sys.stdin.readline


def union(x, y):
    x = find(x)
    y = find(y)

    # x와 y를 합칠 수 없음 (사이클 발생)
    if x == y:
        return False

    p[x] = y
    return True


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def kruskal():
    ans = 0     # MST의 가중치 합
    cnt = 0     # 선택된 간선의 개수

    while cnt < V - 1:
        # 최소 비용 간선 선택하기
        e, v1, v2 = heapq.heappop(h)

        # 사이클 발생하는지 확인하기
        if union(v1, v2):
            ans += e
            cnt += 1

    return ans


V, E = map(int, input().split())

visited = [False] * (V + 1)
p = [i for i in range(V + 1)]  # 루트 노드
h = []  # 최소 힙

for _ in range(E):
    a, b, c = map(int, input().split())
    heapq.heappush(h, [c, a, b])

print(kruskal())
