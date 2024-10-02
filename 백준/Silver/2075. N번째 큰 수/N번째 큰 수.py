import sys, heapq
input = sys.stdin.readline
h = []

n = int(input())
for _ in range(n):
    for x in map(int, input().split()):
        if len(h) >= n:
            heapq.heappushpop(h, x)
        else:
            heapq.heappush(h, x)

print(h[0])