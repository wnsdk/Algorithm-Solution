a, b = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = []


def permutation(n, m, l, visited):
    if m == 0:
        print(*l)
        return
    for i in range(n):
        if visited[i]:
            continue
        # i번째를 뽑았다.
        visited[i] = True
        l.append(arr[i])
        permutation(n, m - 1, l, visited)
        l.pop()
        visited[i] = False


permutation(a, b, [], [False] * a)
