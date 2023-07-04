import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

n, m = map(int, input().split())
matrix = [list(map(lambda x: -1 if x == 'H' else int(x), list(input().strip()))) for _ in range(n)]

# dp[y][x] : (y, x) 에서 시작하여, 동전을 움직일 수 있는 최대 횟수
dp = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]


def isCoord(y, x):
    return 0 <= y < n and 0 <= x < m


def dfs(y, x):
    # 방문한 적 있다면 -> 루프
    if visited[y][x]:
        print(-1)
        exit()

    # 방문 체크
    visited[y][x] = True

    # 예전에 찾아놓은 dp 값이 있다면
    if dp[y][x] > 0:
        visited[y][x] = False
        return dp[y][x]

    for k in range(4):
        ny = y + dy[k] * matrix[y][x]
        nx = x + dx[k] * matrix[y][x]

        # 보드의 바깥으로 나가거나 구멍을 만났다면
        if not isCoord(ny, nx) or matrix[ny][nx] == -1:
            continue

        # 재귀
        dp[y][x] = max(dp[y][x], dfs(ny, nx) + 1)

    # 방문 초기화
    visited[y][x] = False

    return dp[y][x]


dfs(0, 0)
print(dp[0][0] + 1)
