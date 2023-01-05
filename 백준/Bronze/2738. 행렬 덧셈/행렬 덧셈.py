# N : 행 수
# M : 열 수
N, M = map(int, input().split())

matrix = [[0] * M for _ in range(N)]

for _ in range(2):
    for y in range(N):
        row = list(map(int, input().split()))
        for x in range(M):
            matrix[y][x] += row[x]

for y in range(N):
    print(*matrix[y])