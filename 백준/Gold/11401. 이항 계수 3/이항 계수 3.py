import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, K = map(int, input().split())
p = 1000000007
A = B = 1

def power(x, y):
    if y == 0: return 1
    if y % 2 == 1: return x * power(x, y - 1) % p
    return power(x, y // 2) ** 2 % p



# A = N * (N - 1) * ... * (N - K + 1)
for i in range(N, N - K, -1):
    A = (A * i) % p;

#B = K!
for i in range(1, K + 1):
    B = (B * i) % p

# B = (K!)^(p-2)
B = power(B, p - 2)

print(A * B % p)