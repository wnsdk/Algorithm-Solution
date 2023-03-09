mod = 1000000000

N, K = map(int, input().split())

# dp[a][b][c] : b개의 숫자를 이용해서 숫자 a를 완성하는 경우의 수 (단, 제일 마지막에 쓰인 숫자는 c)
dp = [[0] * (K + 1) for _ in range(N + 1)]

# 사용해야 하는 숫자의 개수가 1개라면, 목표 숫자 a를 딱 1개 사용하는 경우 1가지 밖에 없다.
for a in range(N + 1):
    dp[a][1] = 1

# 숫자 a를 만든다.
for a in range(N + 1):
    # b개의 숫자를 이용한다.
    for b in range(2, K + 1):
        # 제일 마지막에 숫자 c를 사용할 것이다.
        for c in range(a + 1):
            dp[a][b] += dp[a - c][b - 1] % mod

print(dp[N][K] % mod)