from collections import deque

def solution(info, edges):
    answer = 0
    size = len(info)
    adj = [[] for _ in range(size)]
    
    for edge in edges:
        parent = edge[0]
        child = edge[1]    
        adj[parent].append(child)
    
    q = deque()
    q.append((1, 0, set([0])))
    
    while q:
        sheep, wolf, path = q.popleft()
        answer = max(answer, sheep)
        
        # node : 여태까지 방문한 적 있는 노드들
        for node in path:
            
            # child : 앞으로 방문 가능한 노드들
            for child in adj[node]:
                
                if child in path:
                    continue
                
                n_sheep = sheep + 1 if info[child] == 0 else sheep
                n_wolf = wolf + 1 if info[child] == 1 else wolf

                if n_sheep <= n_wolf:
                    continue

                q.append((n_sheep, n_wolf, path.union(set([child]))))
            
    return answer