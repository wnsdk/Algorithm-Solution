N, R = map(int, input().split())
ans = []


def permutation2(n, r):
    if not r:
        print(*ans)
    else:
        for i in range(n):
            ans.append(i + 1)
            permutation2(n, r - 1)
            ans.pop()


permutation2(N, R)
