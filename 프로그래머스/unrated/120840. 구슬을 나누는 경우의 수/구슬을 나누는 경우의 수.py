dp = [-1] * 31

def factorial(n):
    if dp[n] > 0:
        return dp[n]
    if n < 2:
        dp[n] = 1
    else:
        dp[n] = n * factorial(n - 1)
    
    return dp[n]
            

def solution(balls, share):
    return factorial(balls) // (factorial(balls - share) * factorial(share))