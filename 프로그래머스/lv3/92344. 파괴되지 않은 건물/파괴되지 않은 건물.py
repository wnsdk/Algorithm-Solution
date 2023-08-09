def solution(board, skill):
    Y = len(board)
    X = len(board[0])
    answer = 0
    
    matrix = [[0] * X for _ in range(Y)]
    
    for s in skill:
        r1, c1 = s[1], s[2]
        r2, c2 = s[3], s[4]
        degree = s[5]
        
        if s[0] == 1:
            degree *= -1
        
        matrix[r1][c1] += degree
        
        if r2 + 1 < Y and c2 + 1 < X:
            matrix[r2 + 1][c2 + 1] += degree
        
        if c2 + 1 < X:
            matrix[r1][c2 + 1] -= degree
        
        if r2 + 1 < Y:
            matrix[r2 + 1][c1] -= degree
            
        # for y in range(Y):
        #     for x in range(X):
        #         print(matrix[y][x], end=' ')
        #     print()
        # print()
        
    for y in range(Y):
        for x in range(X):
            if x > 0:
                matrix[y][x] += matrix[y][x - 1]
            if y > 0:
                matrix[y][x] += matrix[y - 1][x]
            if x > 0 and y > 0:
                matrix[y][x] -= matrix[y - 1][x - 1]
            
            board[y][x] += matrix[y][x]
            
            if board[y][x] > 0:
                answer += 1
        #     print(board[y][x], end=' ')
        # print()
                
    return answer