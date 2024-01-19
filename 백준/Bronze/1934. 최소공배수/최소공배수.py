import sys
input = sys.stdin.readline


def gcd(x, y):
    if x < y:
        x, y = y, x

    while x and y:
        x, y = y, x % y

    return x


for _ in range(int(input())):
    a, b = map(int, input().split())
    print(a * b // gcd(a, b))
    