def solution(slice, n):
    answer = n // slice
    return answer if not n % slice else answer + 1