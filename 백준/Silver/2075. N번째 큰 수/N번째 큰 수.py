import sys, heapq
input = sys.stdin.readline

N = int(input())
h = []
for _ in range(N):
    for i in map(int, input().split()):
        if len(h) >= N:
            heapq.heappushpop(h, i)
        else:
            heapq.heappush(h, i)

print(h[0])