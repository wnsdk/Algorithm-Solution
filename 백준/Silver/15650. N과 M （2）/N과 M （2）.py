from itertools import combinations

n, r = map(int, input().split())
arr = [i for i in range(1, n + 1)]

for ans in combinations(arr, r):
    print(*ans)