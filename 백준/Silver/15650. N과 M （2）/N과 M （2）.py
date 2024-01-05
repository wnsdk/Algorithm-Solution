a, b = map(int, input().split())
nums = []


def combination(n, r, idx):
    if not r:
        print(*nums)
    else:
        for i in range(idx, n):
            nums.append(i + 1)
            combination(n, r - 1, i + 1)
            nums.pop()


combination(a, b, 0)
