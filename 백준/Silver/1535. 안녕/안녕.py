N = int(input())
effort = list(map(int, input().split()))
happy = list(map(int, input().split()))

# dp[i][j] = x : i번째 사람까지 탐색했고, 그 때의 무게(노력)가 j일 때, 가치(행복) 최댓값은 x다.
dp = [[0] * 100 for _ in range(N + 1)]

for i in range(N):
    e = effort[i]
    h = happy[i]

    for j in range(0, 100):
        if j < e:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - e] + h)

print(dp[N - 1][99])
