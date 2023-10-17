def solution(str1, str2):
    answer = ''
    for i in range(max(len(str1), len(str2))):
        if i < len(str1):
            answer += str1[i]
        if i < len(str2):
            answer += str2[i]
    return answer