from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]

# 각 vertex의 진입 차수
in_cnt = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    in_cnt[b] += 1

# 진입 차수가 0인 vertex만을 담을 q
q = deque()

for i, cnt in enumerate(in_cnt):
    if i and not cnt:
        q.append(i)

while q:
    now = q.popleft()
    print(now, end=' ')

    for nxt in adj[now]:
        in_cnt[nxt] -= 1
        if not in_cnt[nxt]:
            q.append(nxt)
