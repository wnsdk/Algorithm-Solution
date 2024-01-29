def f(x, n):
    if n == 1:
        return x

    ret = f(x, n // 2)

    if n % 2:
        return ret * ret * x % c
    else:
        return ret * ret % c


a, b, c = map(int, input().split())
print(f(a, b) % c)
