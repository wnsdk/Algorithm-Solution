from itertools import product

n, r = map(int, input().split())
arr = [i for i in range(1, n + 1)]

for ans in product(arr, repeat=r):
    print(*ans)