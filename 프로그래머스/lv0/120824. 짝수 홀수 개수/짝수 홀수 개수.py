def solution(num_list):
    ans1 = 0
    ans2 = 0
    for i in num_list:
        if i % 2:
            ans1 += 1
        else:
            ans2 += 1
    return [ans2, ans1]