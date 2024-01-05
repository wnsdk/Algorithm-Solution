from itertools import combinations_with_replacement

n, r = map(int, input().split())
arr = [i for i in range(1, n + 1)]

for ans in combinations_with_replacement(arr, r):
    print(*ans)