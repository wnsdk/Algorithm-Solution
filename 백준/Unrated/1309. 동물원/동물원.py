N = int(input())

dp = [[0] * 3 for _ in range(N + 1)]


dp[1][0] = 1    # 1번째 칸의 왼쪽에 사자를 두는 경우
dp[1][1] = 1    # 1번째 칸의 오른쪽에 사자를 두는 경우
dp[1][2] = 1    # 1번째 칸에 사자를 안 두는 경우

for i in range(2, N + 1):
    dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % 9901
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % 9901
    dp[i][2] = sum(dp[i - 1]) % 9901

print(sum(dp[N]) % 9901)