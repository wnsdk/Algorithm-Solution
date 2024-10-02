# 10000000 이하의 수를 소인수분해
# 10000000 ** 0.5 이하의 소수들을 이용해서 나눌 수 있는데 까지 나누기
# 그러고 나서 남은 수는 자연스럽게 1 아니면 10000000 ** 0.5 이상의 소수가 됨

# 에라토스테네스의 체
N = int(10000000 ** 0.5) + 1
chk = [True] * (N + 1)
for i in range(2, int(N ** 0.5) + 1):
    if chk[i]:
        for j in range(i + i, N, i):
            chk[j] = False

prime = [i for i in range(2, N + 1) if chk[i]]
N = int(input())

if N != 1:
    i = 0
    while i < len(prime) and N >= prime[i] ** 2:
        if not(N % prime[i]):
            N //= prime[i]
            print(prime[i])
        else:
            i += 1
    if N != 1:
        print(N)