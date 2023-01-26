from collections import deque

visited = []

def solution(n, computers):
    global visited
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            bfs(n, computers, i)
            answer += 1
            
    return answer

def bfs(n, computers, start):
    q = deque()
    global visited
    
    q.append(start)
    visited[start] = True
    
    while q:
        x = q.popleft()
        
        for i in range(n):
            if not visited[i] and computers[x][i] == 1:
                q.append(i)
                visited[i] = True