import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


# 두 노드의 루트 노드를 일치시키기 (둘 중 작은 값으로)
def union(x, y):
    x = find(x)
    y = find(y)
    
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


# 노드 x의 루트 노드 찾기
def find(x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
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