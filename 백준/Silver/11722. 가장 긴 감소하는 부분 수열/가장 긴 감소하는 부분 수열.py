n = int(input())
l = list(map(int, input().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):
        # 감소하는 부분 수열을 만족한다면
        if l[j] > l[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))