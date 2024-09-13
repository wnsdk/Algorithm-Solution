import sys
input = sys.stdin.readline


def gcd(x, y):
    n = x % y
    if not n:
        return y
    return gcd(y, n)


for _ in range(int(input())):
    a, b = map(int, input().split())
    a, b = (b, a) if b > a else (a, b)

    print(a * b // gcd(a, b))