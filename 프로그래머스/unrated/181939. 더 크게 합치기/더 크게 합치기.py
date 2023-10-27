def solution(a, b):
    x1 = int(str(a) + str(b))
    x2 = int(str(b) + str(a))
    return x1 if x1 > x2 else x2