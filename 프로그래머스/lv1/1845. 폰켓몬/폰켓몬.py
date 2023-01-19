def solution(nums):
    ponketmon = dict()
    
    for i in nums:
        if i in ponketmon:
            ponketmon[i] += 1
        else:
            ponketmon[i] = 1
    
    N = len(nums)
    size = len(list(ponketmon.keys()))

    return size if N / 2 > size else N / 2