def solution(numbers, k):
    answer = 0
    k -= 1
    while k:
        answer += 2
        k -= 1
    return numbers[answer % len(numbers)]