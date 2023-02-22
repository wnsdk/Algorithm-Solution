def solution(age):
    answer = ''
    for c in str(age):
        answer += chr(ord('a') + int(c))
    return answer