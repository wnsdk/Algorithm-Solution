from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))
F = defaultdict(int)
stk = []
ans = [-1] * n

for x in A:
    F[x] += 1

for i, x in enumerate(A):
    while stk and F[stk[-1][1]] < F[x]:
        ans[stk[-1][0]] = x
        stk.pop()
    stk.append((i, x))

print(*ans)
