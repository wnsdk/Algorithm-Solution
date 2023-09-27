import sys
input = sys.stdin.readline

n = int(input())
stk = []
l = 0
ans = 0

for r in range(n):
    l = r
    x = int(input())

    while stk and stk[-1][1] > x:
        l, y = stk.pop()
        ans = max(ans, y * (r - l))
    stk.append((l, x))

while stk:
    l, y = stk.pop()
    ans = max(ans, y * (n - l))

print(ans)
