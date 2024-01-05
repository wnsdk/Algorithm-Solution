a, b = map(int, input().split())
nums = []
chk = [False] * (a + 1)


def permutation(n, r):
    if not r:
        print(*nums)

    for i in range(1, n + 1):
        if not chk[i]:
            chk[i] = True
            nums.append(i)
            permutation(n, r - 1)
            nums.pop()
            chk[i] = False


permutation(a, b)
