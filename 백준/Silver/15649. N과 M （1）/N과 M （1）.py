from itertools import permutations

n, r = map(int, input().split())
arr = [i for i in range(1, n + 1)]

for ans in permutations(arr, r):
    print(*ans)
