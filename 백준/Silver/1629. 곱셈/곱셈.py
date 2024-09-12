def f(A, B, C):
    if B < 2:
        return A % C
    x = f(A, B // 2, C) % C
    return (x * x * (A if B % 2 else 1)) % C


a, b, c = map(int, input().split())
print(f(a, b, c))