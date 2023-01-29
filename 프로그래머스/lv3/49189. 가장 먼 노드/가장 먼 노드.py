from collections import deque

def solution(n, edge):
    adj = [[] for _ in range(n)]
    
    for e in edge:
        n1 = e[0] - 1
        n2 = e[1] - 1
        adj[n1].append(n2)
        adj[n2].append(n1)
    
    
    return bfs(n, adj)

def bfs(n, adj):
    q = deque()
    visited = [False] * n
    distance = []
    
    q.append((0, 0))
    visited[0] = True
    distance.append(0)
    
    
    while q:
        x, d = q.popleft()
        distance.append(d)
        
        for y in adj[x]:
            if not visited[y]:
                q.append((y, d + 1))
                visited[y] = True
    
    return distance.count(max(distance))