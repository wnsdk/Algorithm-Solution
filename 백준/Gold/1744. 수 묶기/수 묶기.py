import sys
import heapq
input = sys.stdin.readline

n = int(input())
ans = 0
hasZero = False
max_h = []
min_h = []

for _ in range(n):
    num = int(input())
    if num > 0:
        heapq.heappush(max_h, -num)
    elif num < 0:
        heapq.heappush(min_h, num)
    else:
        hasZero = True

while len(max_h) > 1:
    a = -heapq.heappop(max_h)
    b = -heapq.heappop(max_h)

    if a == 1 or b == 1:
        heapq.heappush(max_h, -a)
        heapq.heappush(max_h, -b)
        break

    ans += a * b

while len(min_h) > 1:
    a = heapq.heappop(min_h)
    b = heapq.heappop(min_h)
    ans += a * b

while max_h:
    ans -= heapq.heappop(max_h)

if not hasZero and min_h:
    ans += heapq.heappop(min_h)

print(ans)
