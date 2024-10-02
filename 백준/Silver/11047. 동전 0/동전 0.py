import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []

for _ in range(n):
    coins.append(int(input()))

cnt = 0

for coin in coins[::-1]:
    if coin <= k:
        cnt += k // coin
        k %= coin

print(cnt)