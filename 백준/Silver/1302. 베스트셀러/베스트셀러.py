import sys
input = sys.stdin.readline

d = dict()
for _ in range(int(input())):
    book = input()
    if book not in d:
        d[book] = 1
    else:
        d[book] += 1

print(sorted(list(d.items()), key=lambda x: (-x[1], x[0]))[0][0])
