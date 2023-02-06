from collections import deque

dy = [0, 1]
dx = [1, 0]

def solution(m, n, puddles):
    board = [[0] * m for _ in range(n)]
    
    for x, y in puddles:
        board[y - 1][x - 1] = -1
    
    return bfs(m, n, board)

def bfs(m, n, board):
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    
    q = deque()
    q.append((0, 0))
    
    while q:
        y, x = q.popleft()
        # printBoard(dp)
        
        for k in range(2):
            ny = y + dy[k]
            nx = x + dx[k]
            
            if not isCoord(m, n, ny, nx) or board[ny][nx] == -1:
                continue
            
            if dp[ny][nx] == 0:
                q.append((ny, nx))
            
            dp[ny][nx] = (dp[ny][nx] + dp[y][x]) % 1000000007
    
    return dp[n - 1][m - 1]
            

def isCoord(m, n, y, x):
    return 0 <= x < m and 0 <= y < n

def printBoard(board):
    print('----------------------')
    for row in board:
        for col in row:
            print(col, end=' ')
        print()