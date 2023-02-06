from collections import deque

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def solution(maps):    
    return bfs(maps)

def bfs(maps):
    q = deque()
    q.append((0, 0, 1))
    
    while q:
        y, x, d = q.popleft()
        
        if y == len(maps) - 1 and x == len(maps[0]) - 1:
            return d
        
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            nd = d + 1
            
            # 방문한 적 있거나, 길이 막혀있다면
            if not isCoord(ny, nx, len(maps), len(maps[0])) or maps[ny][nx] != 1:
                continue
            
            maps[ny][nx] = 2
            q.append((ny, nx, nd))
            
    return -1

def isCoord(y, x, Y, X):
    return 0 <= y < Y and 0 <= x < X
    
            
        