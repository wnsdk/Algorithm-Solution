def solution(before, after):
    
    answer = 1

    d = dict()
    for c in after:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    for c in before:
        if c in d and d[c] > 0:
            d[c] -= 1
        else:
            answer = 0
            break
        
    return answer