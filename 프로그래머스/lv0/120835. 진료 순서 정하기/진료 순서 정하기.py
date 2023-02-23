def solution(emergency):
    answer = []
    tmp = sorted(emergency, reverse=True)
    
    for i1, v1 in enumerate(emergency):
        for i2, v2 in enumerate(tmp):
            if v1 == v2:
                answer.append(i2 + 1)
                break
    
    return answer