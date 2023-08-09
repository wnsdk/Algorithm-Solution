from collections import deque

INF = 1e9
n = int(input())

# dp[x] : n을 x로 만드는 데 드는 최소 연산 횟수
dp = [INF] * (n + 1)
q = deque()

q.append((n, 0, ''))
dp[n] = 0
ans = ''

while q:
    x, dist, path = q.popleft()

    if x == 1:
        ans = path + '1'
        break

    next = []
    if x % 3 == 0:
        next.append(x // 3)
    if x % 2 == 0:
        next.append(x // 2)
    if x > 1:
        next.append(x - 1)

    path += str(x) + ' '

    for nx in next:
        if dp[nx] != INF:
            continue
        q.append((nx, dist + 1, path))
        dp[nx] = dist + 1

print(dp[1])
print(ans)
