import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(n)]

for y in range(n):
    for x in range(m):
        print(A[y][x] + B[y][x], end=' ')
    print()