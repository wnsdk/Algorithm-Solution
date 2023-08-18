from collections import deque

ret_intensity = 1e9
ret_goal = 1e9
dp = []


def solution(n, paths, gates, summits):
    global dp
    
    adj = [[] for _ in range(n + 1)]
    dp = [1e9] * (n + 1)    # dp[x] : x노드에 도달할 때 까지 필요한 최대 intensity
    
    for path in paths:
        i, j, w = path[0], path[1], path[2]
        adj[i].append((j, w))
        adj[j].append((i, w))
    
    # 등산로 정렬
    for i in range(1, n + 1):
        adj[i].sort(key=lambda x: x[1])
    
    visited = 0b0
    for gate in gates:
        visited |= (1 << gate)
    
    is_summit = 0b0
    for summit in summits:
        is_summit |= (1 << summit)
    
    for gate in gates:
        dp[gate] = 0
        bfs(gate, n, adj, visited, is_summit)
    
    return [ret_goal, ret_intensity]


def bfs(gate, n, adj, visited, is_summit):
    global ret_intensity, ret_goal
        
    q = deque()
    q.append((gate, 0, visited))
    
    while q:
        node, intensity, visited = q.popleft()
        
        for tmp in adj[node]:
            n_node = tmp[0]
            weight = tmp[1]
            
            # 백트래킹
            if weight > ret_intensity:
                break
            
            # 방문한 적 있거나 출입구일 경우
            if visited & (1 << n_node):
                continue
            
            n_intensity = max(intensity, weight)
            
            if n_intensity >= dp[n_node]:
                break
            
            # 산의 정상일 경우
            if is_summit & (1 << n_node):
                if ret_intensity == n_intensity and ret_goal > n_node or ret_intensity > n_intensity:
                    ret_intensity = n_intensity
                    ret_goal = n_node
                continue
            
            n_visited = visited | (1 << n_node)
            
            dp[n_node] = n_intensity
            q.append((n_node, n_intensity, n_visited))