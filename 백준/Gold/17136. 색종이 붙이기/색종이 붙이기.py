import sys
from itertools import product

input = sys.stdin.readline
INF = float('inf')

matrix = [list(map(int, input().split())) for _ in range(10)]

# 각 색종이의 남아있는 개수
cnt = [0] + [5] * 5

# 정답 (최소로 사용한 종이 개수)
ans = INF

# 덮어야하는 구역 개수
rest = 0
for r in range(10):
    rest += matrix[r].count(1)

if not rest:
    print(0)
    exit()


def is_coord(y, x):
    return 0 <= y < 10 and 0 <= x < 10


def dfs(y, x, paper):
    global ans, rest

    # 모든 구역을 다 덮었다면
    if rest < 1:
        return

    # 이미 찾아놓은 정답보다 더 비효율적이라면
    if ans <= paper + 1:
        return

    # 큰 색종이로 덮을 수 있었던 적이 있으면, 그보다 작은 색종이는 무조건 덮을 수 있음
    idx2 = False

    for size in range(5, 0, -1):
        # size 크기의 색종이가 한 장도 남아있지 않다면
        if not cnt[size]:
            continue

        idx = True
        if not idx2:
            for dy, dx in product(range(size), range(size)):
                ny = y + dy
                nx = x + dx
                if not is_coord(ny, nx) or not matrix[ny][nx]:
                    idx = False
                    break

        idx2 = idx

        # size 크기의 색종이로 덮을 수 있다면
        if idx2:
            # 색종이 덮기
            cnt[size] -= 1
            rest -= size ** 2
            for dy, dx in product(range(size), range(size)):
                matrix[y + dy][x + dx] = 0

            # 정답 갱신
            if not rest:
                ans = min(ans, paper + 1)

            # 재귀
            for next_y, next_x in product(range(y, 10), range(10)):
                if matrix[next_y][next_x]:
                    dfs(next_y, next_x, paper + 1)
                    break

            # 색종이 제거하기
            cnt[size] += 1
            rest += size ** 2
            for dy, dx in product(range(size), range(size)):
                matrix[y + dy][x + dx] = 1


for r, c in product(range(10), range(10)):
    if matrix[r][c] == 1:
        dfs(r, c, 0)
        break

print(ans if ans < INF else -1)
