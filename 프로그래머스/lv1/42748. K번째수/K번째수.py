def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        s = commands[i][0] - 1
        e = commands[i][1]
        k = commands[i][2] - 1
    
        a = array[s:e]
        a.sort()
        
        answer.append(a[k])
    
    return answer