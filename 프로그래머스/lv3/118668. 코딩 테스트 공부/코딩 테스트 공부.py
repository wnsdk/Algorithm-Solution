import sys

dp = []
INF = 1e9
max_alp_req, max_cop_req = 0, 0
arr = []

def dfs(alp, cop, cost):
    alp = min(alp, max_alp_req)
    cop = min(cop, max_cop_req)
    
    if dp[alp][cop] <= cost:
        return dp[alp][cop]
    
    dp[alp][cop] = cost
    
    if alp == max_alp_req and cop == max_cop_req:
        return dp[alp][cop]
    
    cost_list = [cost]
    
    for problem in arr:
        # 풀기 위해 필요한 능력
        alp_req = problem[0]
        cop_req = problem[1]
        # 풀었을 때 증가하는 능력
        alp_rwd = problem[2]
        cop_rwd = problem[3]
        # 푸는데 드는 시간
        time = problem[4]
        
        if alp < alp_req or cop < cop_req:
            continue
        
        cost_list.append(dfs(alp + alp_rwd, cop + cop_rwd, cost + time))
    
    if alp < max_alp_req:
        cost_list.append(dfs(alp + 1, cop, cost + 1))
    
    if cop < max_cop_req:
        cost_list.append(dfs(alp, cop + 1, cost + 1))
    
    dp[alp][cop] = min(cost_list)
    
    return dp[alp][cop]


def solution(alp, cop, problems):
    global dp, max_alp_req, max_cop_req, arr
    arr = sorted(problems, key=lambda x: -(x[2] + x[3]) // x[4])
    
    for problem in problems:
        max_alp_req = max(max_alp_req, problem[0])
        max_cop_req = max(max_cop_req, problem[1])
    
    # dp[x][y] : 알고력 x, 코딩력 y를 만드는 데 필요한 비용의 최솟값
    dp = [[INF] * (max_cop_req + 1) for _ in range(max_alp_req + 1)]
    
    dfs(alp, cop, 0)
    
    return dp[max_alp_req][max_cop_req]