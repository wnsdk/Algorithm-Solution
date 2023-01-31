from collections import Counter

def solution(number, k):
    answer = ''
    # 총 size개 만큼 선택해야 됨
    size = len(number) - k
    
    # 
    start = 0
    
    for i in range(1, size + 1):
        # i번째 수를 선택할 것임
        # 뒤에 선택할 size - i개의 수를 남겨놓은 상태에서 최댓값 구하면 됨
        m = '0'
        for j in range(start, len(number) - size + i):
            if m < number[j]:
                m = number[j]
                start = j + 1
            if m == '9':
                break
                
        answer += m
            
    

    return answer