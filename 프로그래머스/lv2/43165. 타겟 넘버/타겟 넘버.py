answer = 0

def solution(numbers, target):
    global answer
    dfs(0, 0, numbers, target)
    return answer

def dfs(i, tot, numbers, target):
    global answer
    
    if i == len(numbers):
        if target == tot:
            answer += 1
        return
    
    dfs(i + 1, tot + numbers[i], numbers, target)
    dfs(i + 1, tot - numbers[i], numbers, target)
    