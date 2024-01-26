import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def union(x, y):
    px = find(x)
    py = find(y)
    if px != py:
        parent[px] = py


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

for _ in range(m):
    cmd, a, b = map(int, input().split())

    # Find
    if cmd:
        print('YES' if find(a) == find(b) else 'NO')

    # Union
    else:
        union(a, b)