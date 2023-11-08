def solution(a, d, included):
    answer = 0
    i = 0
    while i < len(included):
        if included[i]:
            answer += a
        i += 1
        a += d
    return answer