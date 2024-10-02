n = int(input())
m = int(n ** 0.5) + 1

is_prime = [True] * (m + 1)

for x in range(2, int(m ** 0.5) + 1):
    if is_prime[x]:
        for y in range(x * 2, m + 1, x):
            is_prime[y] = False

prime = [x for x in range(2, m + 1) if is_prime[x]]

for p in prime:
    while n % p == 0:
        n //= p
        print(p)

if n > 1:
    print(n)
