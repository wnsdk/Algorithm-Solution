def solution(participant, completion):
    d = dict()
    
    for i in participant:
        if (i not in d):
            d[i] = 1
        else:
            d[i] += 1
    
    for i in completion:
        d[i] -= 1
        if d[i] == 0:
            del d[i]
        
    
    answer = list(d.keys())[0]
    return answer