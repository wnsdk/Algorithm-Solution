a, b, c, d, e, f = map(int, input().split())
y = (c * d - a * f) // (d * b - a * e)
x = (c * e - b * f) // (e * a - b * d)
print(x, y)