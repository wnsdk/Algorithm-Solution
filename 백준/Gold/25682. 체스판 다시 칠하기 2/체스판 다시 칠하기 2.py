import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
B = [[0] * m for _ in range(n)]
W = [[0] * m for _ in range(n)]
ans = 1e9

for y in range(n):
    for x, c in enumerate(input().strip()):
        # 누적합 구하기
        if y == 0 and x == 0:
            if (y + x) % 2 and c != 'W' or (y + x) % 2 == 0 and c != 'B':
                B[y][x] += 1
            else:
                W[y][x] += 1
        elif y == 0:
            B[y][x] = B[y][x - 1]
            W[y][x] = W[y][x - 1]
            if (y + x) % 2 and c != 'W' or (y + x) % 2 == 0 and c != 'B':
                B[y][x] += 1
            else:
                W[y][x] += 1
        elif x == 0:
            B[y][x] = B[y - 1][x]
            W[y][x] = W[y - 1][x]
            if (y + x) % 2 and c != 'W' or (y + x) % 2 == 0 and c != 'B':
                B[y][x] += 1
            else:
                W[y][x] += 1
        else:
            B[y][x] = B[y][x - 1] + B[y - 1][x] - B[y - 1][x - 1]
            W[y][x] = W[y][x - 1] + W[y - 1][x] - W[y - 1][x - 1]
            if (y + x) % 2 and c != 'W' or (y + x) % 2 == 0 and c != 'B':
                B[y][x] += 1
            else:
                W[y][x] += 1

        sy = y - k + 1
        sx = x - k + 1

        if sy > -1 and sx > -1:
            if sy == 0 and sx == 0:
                ans = min(ans, B[y][x])
                ans = min(ans, W[y][x])
            elif sy == 0:
                ans = min(ans, B[y][x] - B[y][sx - 1])
                ans = min(ans, W[y][x] - W[y][sx - 1])
            elif sx == 0:
                ans = min(ans, B[y][x] - B[sy - 1][x])
                ans = min(ans, W[y][x] - W[sy - 1][x])
            else:
                ans = min(ans, B[y][x] - B[y][sx - 1] - B[sy - 1][x] + B[sy - 1][sx - 1])
                ans = min(ans, W[y][x] - W[y][sx - 1] - W[sy - 1][x] + W[sy - 1][sx - 1])

print(ans)