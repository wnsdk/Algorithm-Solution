import sys
input = sys.stdin.readline


def f(sy, sx, d):
    ch = arr[sy][sx]

    if d == 1:
        return ch

    nd = d // 2

    for y in range(sy, sy + d):
        for x in range(sx, sx + d):
            if ch != arr[y][x]:
                ret = '('
                ret += f(sy, sx, nd)
                ret += f(sy, sx + nd, nd)
                ret += f(sy + nd, sx, nd)
                ret += f(sy + nd, sx + nd, nd)
                ret += ')'
                return ret

    return ch


n = int(input())
arr = [input().strip() for _ in range(n)]

print(f(0, 0, n))
