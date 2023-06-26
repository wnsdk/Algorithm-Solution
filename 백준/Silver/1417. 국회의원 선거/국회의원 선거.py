import heapq
import sys
input = sys.stdin.readline

# 후보의 수
n = int(input())

# 현재 나의 민심
me = int(input())

h = []
ans = 0

# 각 후보 별 민심
for i in range(1, n):
    heapq.heappush(h, -int(input()))

while h:
    vote = -heapq.heappop(h)

    # 내가 제일 표 수가 많다면
    if me > vote:
        break

    # 매수
    heapq.heappush(h, -(vote - 1))
    me += 1
    ans += 1

print(ans)
