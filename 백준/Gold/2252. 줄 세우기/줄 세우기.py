import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
adj = [set() for _ in range(n + 1)]
in_cnt = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].add(b)
    in_cnt[b] += 1

q = deque()
ans = []

for i in range(1, n + 1):
    if not in_cnt[i]:
        q.append(i)

while q:
    s = q.popleft()
    ans.append(s)

    for j in adj[s]:
        in_cnt[j] -= 1
        if not in_cnt[j]:
            q.append(j)

print(*ans)