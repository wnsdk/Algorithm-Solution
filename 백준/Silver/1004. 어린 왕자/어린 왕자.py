def d(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    s = []
    for i in range(n):
        cx, cy, r = map(int, input().split())
        d1 = d(cx, cy, x1, y1)
        d2 = d(cx, cy, x2, y2)
        if d1 < r and d2 < r:
            continue
        if d1 < r or d2 < r:
            s.append(i)
    print(len(s))