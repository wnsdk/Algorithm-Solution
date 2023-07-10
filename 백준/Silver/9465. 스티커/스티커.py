import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    
    dp = [[0] * n for _ in range(3)]
    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]

    # i번째 열
    for i in range(1, n):
        # 윗 스티커를 뗀다
        dp[0][i] += stickers[0][i] + max(dp[1][i - 1], dp[2][i - 1])

        # 아래 스티커를 뗀다
        dp[1][i] += stickers[1][i] + max(dp[0][i - 1], dp[2][i - 1])

        # 스티커를 떼지 않는다.
        dp[2][i] += max(dp[0][i - 1], dp[1][i - 1])

    print(max(dp[0][n - 1], dp[1][n - 1], dp[2][n - 1]))
