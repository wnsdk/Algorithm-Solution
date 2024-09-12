N, M = map(int, input().split())
ans = []


def product(n, m):
    if not m:
        print(*ans)
    else:
        for i in range(1, n + 1):
            ans.append(i)
            product(n, m - 1)
            ans.pop()


product(N, M)