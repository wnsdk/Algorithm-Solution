import sys
input = sys.stdin.readline

# 입력 받기
INF = float('inf')
V, E = map(int, input().split())
adj = [[INF] * (V + 1) for _ in range(V + 1)]

# for i in range(1, V + 1):
#     adj[i][i] = 0

for _ in range(E):
    # a에서 b로 가는 거리 c
    a, b, c = map(int, input().split())
    adj[a][b] = c

# 플로이드 워셜
for k in range(1, V + 1):
    for a in range(1, V + 1):
        for b in range(1, V + 1):
            adj[a][b] = min(adj[a][b], adj[a][k] + adj[k][b])

# 정답
ans = INF
for i in range(1, V + 1):
    ans = min(ans, adj[i][i])

print(-1 if ans == INF else ans)