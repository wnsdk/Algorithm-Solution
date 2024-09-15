from collections import deque

n, m = map(int, input().split())
d = deque([i for i in range(1, n + 1)])
ans = 0

for x in list(map(int, input().split())):
    index = d.index(x)
    if index:
        if index <= len(d) // 2:
            d.rotate(-index)

            ans += index
        else:
            d.rotate(len(d) - index)
            ans += len(d) - index
    d.popleft()

print(ans)