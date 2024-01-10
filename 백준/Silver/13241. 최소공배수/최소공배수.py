def gcd(x, y):
    if y > x:
        x, y = y, x
    while y > 0:
        x, y = y, x % y
    return x


a, b = map(int, input().split())
print(a * b // gcd(a, b))
