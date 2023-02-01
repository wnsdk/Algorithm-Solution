from collections import deque

def solution(s):
    q = deque()
    
    for c in s:
        if c == '(':
            q.append(c)
        elif not q:
            return False
        else:
            q.pop()
            
    if q:
        return False
    
    return True