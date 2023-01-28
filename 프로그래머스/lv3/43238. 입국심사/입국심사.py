import heapq

def solution(n, times):
    times.sort()
    
    l = 0
    r = times[-1] * n
    
    while l != r:
        m = (l + r) // 2
        
        # m시간동안 심사가 가능한 최대 인원 구하기
        possible_cnt = 0
        for t in times:
            possible_cnt += m // t
        
        if n <= possible_cnt:
            r = m
        else:
            l = m + 1
    
    return l