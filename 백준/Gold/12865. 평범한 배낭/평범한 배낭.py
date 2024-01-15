N, K = map(int, input().split())
item = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]

# dp[i][j] : i번째 물건까지 탐색했을 때 가방의 무게가 j라면, 그때의 가치 총합
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

# 냅색 문제 풀이
for i in range(1, N + 1):
    for j in range(1, K + 1):
        # i번째 물건 탐색 중
        w, v = item[i]

        # 목표로 하는 가방의 무게(j)보다 무거운 물건은 가방에 담지 않는다
        if j < w:
            dp[i][j] = dp[i - 1][j]
        # 목표로 하는 가방의 무게(j)보다 가벼운 물건이라면, 가치 비교 후 담을지 결정한다
        else:
            dp[i][j] = max(v + dp[i - 1][j - w], dp[i - 1][j])

print(dp[N][K])