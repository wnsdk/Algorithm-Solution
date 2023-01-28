from bisect import bisect_left
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
tree = [int(i) for i in input().split()]
tree.sort(key=lambda x : -x)

idx = 1
L = []
sum = []
for i in range(N-1):
    tmp = tree[i] - tree[i+1]
    if tmp:
        L.append((tmp, idx))
        sum.append(tmp * idx)
    idx += 1
L.append((tree[N-1], N))
sum.append(tree[N-1] * N)

for i in range(1, len(sum)):
    sum[i] += sum[i - 1]

idx = bisect_left(sum, M)

if idx:
    M -= sum[idx - 1]

ans = 0
for i in range(idx):
    ans += L[i][0]

if M % L[idx][1]:
    ans += M // L[idx][1] + 1
else:
    ans += M // L[idx][1]

print(tree[0] - ans)