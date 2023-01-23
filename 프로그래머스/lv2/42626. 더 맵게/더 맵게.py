import heapq

def solution(scoville, K):
    size = len(scoville)
    heapq.heapify(scoville)
    
    for i in range(size - 1):
        # 제일 안 매운 음식
        n1 = heapq.heappop(scoville)
        
        if n1 >= K:
            return i
        
        # 두 번째로 안 매운 음식
        n2 = heapq.heappop(scoville)
        
        # 두 음식을 합한 스코빌 지수
        n = n1 + n2 * 2
        
        heapq.heappush(scoville, n)
    
    if scoville[0] >= K:
        return size - 1
    
    return -1