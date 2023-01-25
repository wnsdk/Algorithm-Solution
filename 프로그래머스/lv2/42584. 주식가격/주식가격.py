from collections import deque 

def solution(prices):
    answer = [0] * len(prices)
    l = []
    
    for i, p in enumerate(prices):
        # 리스트가 비어있다면
        if not l:
            l.append((p, i))
            continue
        
        cnt = 0
        while l:
            cnt += 1
            
            # 주식 가격이 떨어지지 않았다면
            if l[-1][0] <= p:
                l.append((p, i))
                break

            # 주식 가격이 떨어졌다면
            top = l.pop()
            answer[top[1]] = i - top[1]
            
        if not l :
            l.append((p, i))
            
    for p, i in l:
        answer[i] = len(prices) - i - 1
        
    return answer