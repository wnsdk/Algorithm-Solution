N, M = map(int, input().split())
ans = []


def combinaction_with_replacement(n, m, idx):
    if not m:
        print(*ans)
    else:
        for i in range(idx, n + 1):
            ans.append(i)
            combinaction_with_replacement(n, m - 1, i)
            ans.pop()


combinaction_with_replacement(N, M, 1)