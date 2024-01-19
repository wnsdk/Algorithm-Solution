import sys
input = sys.stdin.readline


def combination(r, idx):
    if not r:
        print(*ans)
        return
    for i in range(idx, n):
        ans.append(arr[i])
        combination(r - 1, i + 1)
        ans.pop()


n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

chk = [False] * 10001
ans = []

combination(m, 0)
