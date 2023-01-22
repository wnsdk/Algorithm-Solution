def solution(N, number):
    if N == number:
        return 1
    
    dp = [[] for _ in range(9)]
    dp[0] = [0]
    dp[1] = [N]
    
    for n in range(2, 9):
        
        if dp[n - 1][0] * 10 + N == number:
            return n
        dp[n].append(dp[n - 1][0] * 10 + N)
        
        for x in range(1, n // 2 + 1):
            y = n - x
            
            for i in dp[x]:
                for j in dp[y]:
                    if i + j not in dp[n]:
                        if i + j == number:
                            return n
                        dp[n].append(i + j)
                        
                    if abs(i - j) not in dp[n]:
                        if abs(i - j) == number:
                            return n
                        dp[n].append(abs(i - j))
                        
                    # if j - i not in dp[n]:
                    #     if j - i == number:
                    #         return n
                    #     dp[n].append(j - i)
                        
                    if j != 0 and i // j not in dp[n]:
                        if i // j == number:
                            return n
                        dp[n].append(i // j)
                        
                    if i != 0 and j // i not in dp[n]:
                        if j // i == number:
                            return n
                        dp[n].append(j // i)
                        
                    if i * j not in dp[n]:
                        if i * j == number:
                            return n
                        dp[n].append(i * j)

    return -1