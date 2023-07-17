import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
tree = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


def dfs(node):
    for child in tree[node]:
        if parent[child]:
            continue

        parent[child] = node
        dfs(child)


parent[1] = 1
dfs(1)

for ans in parent[2:]:
    print(ans)
