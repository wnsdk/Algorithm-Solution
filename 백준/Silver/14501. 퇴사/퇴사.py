import sys
input = sys.stdin.readline

# 일 할 수 있는 기간
N = int(input())

T = [0]  # 걸리는 기간
P = [0]  # 받을 수 있는 금액

for i in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

dp = [0] * (N + 1)

if 1 + T[1] <= N + 1:
    dp[1] = P[1]

for t in range(2, N + 1):
    if t + T[t] <= N + 1:
        dp[t] = P[t]
    for i in range(1, t):
        # i번째 날 했던 상담이 오늘 전에 끝난다면
        if i + T[i] <= t:
            dp[t] = max(dp[t], dp[i] + P[t] if t + T[t] <= N + 1 else dp[i])

print(max(dp))