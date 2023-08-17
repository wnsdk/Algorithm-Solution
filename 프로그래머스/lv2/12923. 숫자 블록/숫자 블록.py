def solution(begin, end):
    N = 10000000
    answer = []
    for x in range(begin, end + 1):
        ans = 1 if begin > 1 else 0
        
        for k1 in range(2, int(max(N, x) ** 0.5) + 1):
            if x % k1:
                continue
                
            if k1 < x and k1 <= N:
                ans = max(ans, k1)
            
            k2 = x // k1
                
            if k2 < x and k2 <= N:
                ans = max(ans, k2)
            
        answer.append(ans)
        
    return answer