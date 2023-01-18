def solution(array):
    nums = [0] * 1000
    for i in array:
        nums[i] += 1
    
    # 최빈값의 개수
    m_cnt = 0
    
    # 최빈값
    m = max(nums)
    
    ans = -1
    cnt = 0
    
    # i라는 숫자는 c번 등장했음
    for i, c in enumerate(nums):
        if c == m:
            cnt += 1
            ans = i
    
    if cnt > 1:
        return -1
    return ans