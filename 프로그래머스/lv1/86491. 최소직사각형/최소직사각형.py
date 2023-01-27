def solution(sizes):
    answer = 0
    
    h = 0
    w = 0
    
    for y, x in sizes:
        if y > x:
            y, x = x, y
            
        h = max(h, y)
        w = max(w, x)
        
    return h * w