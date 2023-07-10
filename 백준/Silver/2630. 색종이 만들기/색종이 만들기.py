N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 1. 현재 탐색 중인 네모는 1 * 1입니까?
# 1-1. 그렇다 -> 탐색 종료
# 2-2. 아니다 -> 2번으로
#
# 2. 현재 탐색 중인 네모는 모두 같은 색입니까?
# 2-1. 그렇다 -> 탐색 종료
# 2-2. 아니다 -> 3번으로
#
# 3. 네모를 4등분하고, 각 네모에 대하여 1번으로

# 시작 좌표가 (y, x)이고 길이가 d인 네모가 모두 같은 색인지 확인
def is_same(y, x, d):
    omit = board[y][x] ^ 1
    for i in range(y, y + d):
        if omit in board[i][x:x + d]:
            return False
    return True

cnt = [0, 0]
def solve(y, x, d):
    if d == 1 or is_same(y, x, d):
        cnt[board[y][x]] += 1
        return

    solve(y, x, d // 2)
    solve(y + d // 2, x, d // 2)
    solve(y, x + d // 2, d // 2)
    solve(y + d // 2, x + d // 2, d // 2)

solve(0, 0, N)
print(cnt[0])
print(cnt[1])