N, R = map(int, input().split())


def comb2(n, r, idx):
    if not r:
        print(*ans)
    else:
        for i in range(idx, n):
            ans.append(i + 1)
            comb2(n, r - 1, i)
            ans.pop()


ans = []
comb2(N, R, 0)
