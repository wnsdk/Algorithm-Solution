def solution(n, m, x, y, r, c, k):
    if (k - abs(r - x) - abs(c - y)) % 2:
        return 'impossible'
    
    if abs(r - x) + abs(c - y) > k:
        return 'impossible'
    
    n, m = m, n
    r, c = c - 1, r - 1
    y, x = x - 1, y - 1
    
    answer = ''
    
    # 밑으로 최대한 이동
    while True:
        if y == m - 1:
            break
        if abs(y + 1 - c) + abs(x - r) > k - len(answer) - 1:
            break
            
        answer += 'd'
        y += 1
    
    # 왼쪽으로 최대한 이동
    while True:
        if x == 0:
            break
        if abs(y - c) + abs(x - 1 - r) > k - len(answer) - 1:
            break
            
        answer += 'l'
        x -= 1
    
    # 오른쪽 - 왼쪽 진동
    while True:
        if x == n - 1:
            break
        if abs(y - c) + abs(x - r) > k - len(answer) - 2:
            break
            
        answer += 'rl'
    
    # 오른쪽으로 이동
    answer += 'r' * abs(x - r)
    
    # 위로 이동
    answer += 'u' * abs(y - c)
        
    return answer