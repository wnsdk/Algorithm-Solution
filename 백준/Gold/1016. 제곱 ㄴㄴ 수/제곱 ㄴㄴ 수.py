m, M = map(int, input().split())

# 소수 구하기
size = int(M ** 0.5) + 1
isPrime = [False, False] + [True] * size

for i in range(2, int(size ** 0.5) + 1):
    if isPrime[i]:
        for j in range(i * 2, size, i):
            isPrime[j] = False

primes = [i ** 2 for i in range(2, size) if isPrime[i]]

# 정답 개수 세기
cnt = 0
chk = [True] * (M - m + 1)

for prime in primes:
    start = prime * (m // prime + 1) - m if m % prime else prime * (m // prime) - m
    end = prime * (M // prime) - m + 1
    
    for i in range(start, end, prime):
        chk[i] = False

for i in range(0, M - m + 1):
    if chk[i]:
        cnt += 1

print(cnt)
