from collections import defaultdict
import sys

input = sys.stdin.readline
n = int(input())
d = defaultdict(int)
for _ in range(n):
    d[int(input())] += 1

ans = 2 ** 62
ans_tot = 0

for i in d.keys():
    if d[i] >= ans_tot:
        if d[i] == ans_tot and i >= ans:
            continue
        ans = i
        ans_tot = d[i]

print(ans)