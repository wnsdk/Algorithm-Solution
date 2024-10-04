# n개를 s에서 e로 옮긴다.
def hanoi(n, s, e):
    if n == 1:
        return f'{s} {e}\n'

    m = 6 - s - e

    a = hanoi(n - 1, s, m)
    b = f'{s} {e}\n'
    c = hanoi(n - 1, m, e)
    return a + b + c


N = int(input())
print(2 ** N - 1)
print(hanoi(N, 1, 3))