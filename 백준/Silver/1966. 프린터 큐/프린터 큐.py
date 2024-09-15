import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    q = deque()

    for i, x in enumerate(list(map(int, input().split()))):
        q.append((x, i))

    cnt = 0

    while q:
        now = q.popleft()
        if q and now[0] < max(q)[0]:
            q.append(now)
        else:
            cnt += 1
            if now[1] == m:
                print(cnt)
                continue