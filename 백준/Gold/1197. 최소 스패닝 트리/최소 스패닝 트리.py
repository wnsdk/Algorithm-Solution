import heapq, sys
input = sys.stdin.readline


def union(x, y):
    x = find(p[x])
    y = find(p[y])

    if y < x:
        p[x] = y
    else:
        p[y] = x


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def kruskal():
    ans = 0
    cnt = V - 1

    # 2단계 : 최소 비용인 간선을 선택해나간다. (단 사이클 발생x)
    while cnt:
        w, v1, v2 = heapq.heappop(edges)

        if find(v1) == find(v2):
            continue

        union(v1, v2)
        cnt -= 1
        ans += w

    return ans


V, E = map(int, input().split())
p = [i for i in range(V + 1)]
edges = []

for _ in range(E):
    a, b, c = map(int, input().split())
    # 1단계 : 모든 간선을 오름차순 정렬한다.
    heapq.heappush(edges, [c, a, b])

print(kruskal())
