import sys
input = sys.stdin.readline

size = -1
arr = []
selected = [-1] * 6


def solve(idx, cnt):
    if cnt == 6:
        print(*selected)
        return

    for i in range(idx, size):
        selected[cnt] = arr[i]
        solve(i + 1, cnt + 1)


while True:
    l = list(map(int, input().split()))
    if not l[0]:
        break
    size = l[0]
    arr = l[1:]
    solve(0, 0)
    print()