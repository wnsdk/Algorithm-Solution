N, M = map(int, input().split())
ans = []


def combination(n, m, idx):
    if not m:
        print(*ans)
    else:
        for i in range(idx, n + 1):
            ans.append(i)
            combination(n, m - 1, i + 1)
            ans.pop()


combination(N, M, 1)