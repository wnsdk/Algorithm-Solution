import sys
input = sys.stdin.readline

n = int(input())
board = [input().strip() for _ in range(n)]


def f(y, x, m):
    idx = True
    for i in range(m):
        for j in range(m):
            if board[y + i][x + j] != board[y][x]:
                idx = False
                break
        if not idx:
            break
    
    if idx:
        return board[y][x]

    m //= 2

    return '(' + f(y, x, m) + f(y, x + m, m) + f(y + m, x, m) + f(y + m, x + m, m) + ')'


print(f(0, 0, n))
