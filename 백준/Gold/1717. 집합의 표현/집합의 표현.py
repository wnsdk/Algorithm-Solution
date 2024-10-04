import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


# 두 노드의 루트 노드를 일치시키기 (둘 중 작은 값으로)
def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        p[y] = x
    else:
        p[x] = y


def find(x):
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]


n, m = map(int, input().split())
p = [i for i in range(n + 1)]

for _ in range(m):
    cmd, a, b = map(int, input().split())

    # union
    if cmd == 0:
        union(a, b)
    # find
    else:
        print('yes' if find(a) == find(b) else 'no')