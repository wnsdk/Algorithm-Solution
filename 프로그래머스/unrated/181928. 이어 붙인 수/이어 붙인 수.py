def solution(num_list):
    a = ''
    b = ''
    for n in num_list:
        if n % 2:
            a += str(n)
        else:
            b += str(n)

    return int(a) + int(b)