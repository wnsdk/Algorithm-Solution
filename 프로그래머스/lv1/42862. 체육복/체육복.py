def solution(n, lost, reserve):
    answer = 0
    list = [1] * n
    
    for i in lost:
        list[i - 1] -= 1
    
    for i in reserve:
        list[i - 1] += 1
    
    for i in range(n):
        if list[i] == 2:
            if i > 0 and list[i - 1] == 0:
                list[i - 1] += 1
                list[i] -= 1
                continue
            if i < n - 1 and list[i + 1] == 0:
                list[i + 1] += 1
                list[i] -= 1
                continue
    
    for i in list:
        if i > 0:
            answer += 1
            
    return answer