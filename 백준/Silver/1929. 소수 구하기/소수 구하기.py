m, n = map(int, input().split())

is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False

for a in range(2, int(n ** 0.5) + 1):
    if is_prime[a]:
        for b in range(a + a, n + 1, a):
            is_prime[b] = False


for x in range(m, n + 1):
    if is_prime[x]:
        print(x)
