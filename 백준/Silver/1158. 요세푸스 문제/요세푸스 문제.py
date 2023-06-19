from collections import deque

n, k = map(int, input().split())
ans = '<'

q = deque([i for i in range(1, n + 1)])

for i in range(n):
    for j in range(k):
        num = q.popleft()
        if j == k - 1:
            ans += str(num)
        else:
            q.append(num)

    if i != n - 1:
        ans += ', '

ans += '>'
print(ans)
