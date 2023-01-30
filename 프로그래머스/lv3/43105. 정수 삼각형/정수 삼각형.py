def solution(triangle):
    size = len(triangle)
    
    # dp[y][x] : y번째 행 x번째 열까지 탐색했을 때, 거쳐간 숫자의 최댓값
    dp = [[0] * i for i in range(1, size + 1)]
    dp[0][0] = triangle[0][0]
    
    # y번째 행을 탐색 중
    for y in range(1, size):
        # 첫 번째 열은 바로 윗 칸에서만 도달 가능
        dp[y][0] = dp[y - 1][0] + triangle[y][0]
        # 마지막 열은 바로 왼쪽 윗 칸에서만 도달 가능
        dp[y][y] = dp[y - 1][y - 1] + triangle[y][y]
            
        # 첫 번째, 마지막 열을 제외한 나머지 모든 열 탐색하기
        for x in range(1, y):
            dp[y][x] = max(dp[y - 1][x - 1], dp[y - 1][x]) + triangle[y][x]
    
    return max(dp[size - 1])