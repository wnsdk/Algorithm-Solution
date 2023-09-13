import sys
input = sys.stdin.readline

n = int(input())
x1 = 1e9    # 제일 작은 x값
x2 = -1e9   # 제일 큰 x값
y1 = 1e9
y2 = -1e9

for i in range(n):
    x, y = map(int, input().split())
    x1 = min(x1, x)
    x2 = max(x2, x)
    y1 = min(y1, y)
    y2 = max(y2, y)

print((x2 - x1) * (y2 - y1))