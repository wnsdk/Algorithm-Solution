import sys
input = sys.stdin.readline

arr = sorted([tuple(map(int, input().split())) for _ in range(int(input()))], key=lambda x: (x[1], x[0]))
cnt = 0
pre = 0

for s, e in arr:
    if pre <= s:
        cnt += 1
        pre = e

print(cnt)
