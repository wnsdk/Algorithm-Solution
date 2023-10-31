import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
adj = [list(map(int, input().split())) for _ in range(n)]
ans = [[0] * n for _ in range(n)]


def chk(start, end):
    visited = [False] * n
    q = deque()
    q.append(start)

    while q:
        now = q.popleft()
        for nxt in range(n):
            if visited[nxt] or not adj[now][nxt]:
                continue
                
            if nxt == end:
                return True
            
            q.append(nxt)
            visited[nxt] = True

    return False


for i in range(n):
    for j in range(n):
        print(1 if chk(i, j) else 0, end=' ')
    print()