# 놓여진 돌 개수 (마지막 돌을 가져가면 승리)
N = int(input())

# dp[x] : 남은 돌의 개수가 x개일 때, 첫 번째 턴인 사람이 승리하면 1, 그렇지 않으면 -1
dp = [0] * (N + 1)

dp[1] = 1
if N > 1:
    dp[2] = -1
if N > 2:
    dp[3] = 1

def dfs(x):
    if not dp[x]:
        dp[x] = dfs(x - 3) * -1
    return dp[x]

print('SK' if dfs(N) > 0 else 'CY')