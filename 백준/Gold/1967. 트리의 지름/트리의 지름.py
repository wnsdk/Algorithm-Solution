import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
adj = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    parent, child, weight = map(int, input().split())
    adj[parent].append([child, weight])

ans = 0


def dfs(p, d):
    global ans
    # tmp1 : p 노드에서부터 자식 노드들로 뻗어나가는 경로들 중, 제일 긴 경로
    # tmp2 : 두 번째로 긴 경로
    tmp1 = tmp2 = 0

    # 자식 노드가 있다면
    if adj[p]:
        for c, w in adj[p]:
            distance = dfs(c, d + w)

            if distance > tmp1:
                tmp2 = tmp1
                tmp1 = distance

            elif tmp1 >= distance > tmp2:
                tmp2 = distance

    # 자식 노드가 없다면
    else:
        return d

    ans = max(ans, tmp1 + tmp2 - d * 2)

    # 제일 긴 경로만 반환
    return tmp1


dfs(1, 0)
print(ans)
