m, n = map(int, input().split())

is_prime = [False] * 2 + [True] * (n - 1)

for x in range(2, int(n ** 0.5) + 1):
    if is_prime[x]:
        for y in range(x * 2, n + 1, x):
            is_prime[y] = False

for x in range(m, n + 1):
    if is_prime[x]:
        print(x)