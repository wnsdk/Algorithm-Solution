import heapq
import sys

input = sys.stdin.readline
h1 = [] # 양수
h2 = [] # 음수

for _ in range(int(input())):
    x = int(input())

    # 삽입 연산
    if x:
        if x > 0:
            heapq.heappush(h1, x)
        else:
            heapq.heappush(h2, -x)
            
    # 삭제 연산
    else:
        if not h1 and not h2:
            print(0)
        elif not h1:
            print(-heapq.heappop(h2))
        elif not h2:
            print(heapq.heappop(h1))
        else:
            print(heapq.heappop(h1) if h1[0] < h2[0] else -heapq.heappop(h2))
