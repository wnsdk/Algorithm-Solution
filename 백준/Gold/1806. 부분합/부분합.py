import sys
input = sys.stdin.readline

n, x = map(int, input().split())

# 누적합
A = [0]
for i, item in enumerate(map(int, input().split())):
    A.append(A[i] + item)

ans = 1e9
s = 0
e = 0

while e <= n and s <= n:
    tot = A[e] - A[s]

    if tot < x:
        e += 1
        continue

    if e - s >= ans:
        s += 1
        continue

    ans = min(ans, e - s)
    s += 1

print(ans if ans < 1e9 else 0)
