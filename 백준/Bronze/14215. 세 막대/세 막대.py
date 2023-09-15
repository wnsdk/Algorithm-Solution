a, b, c = map(int, input().split())

M = max(a, b, c)
m = a + b + c - M

if m <= M:
    print(2 * m - 1)
else:
    print(a + b + c)
