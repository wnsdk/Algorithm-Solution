import sys
input = sys.stdin.readline

r, c = map(int, input().split())
l1 = [list(map(int, input().split())) for _ in range(r)]
l2 = [list(map(int, input().split())) for _ in range(r)]

for y in range(r):
    for x in range(c):
        print(l1[y][x] + l2[y][x], end=' ')
    print()