import sys

input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break

    # 가장 긴 변의 길이
    M = max(a, b, c)

    # 나머지 두 변의 길이 합
    m = a + b + c - M

    if m <= M:
        print('Invalid')
    elif a == b == c:
        print('Equilateral')
    elif a != b and b != c and c != a:
        print('Scalene')
    else:
        print('Isosceles')