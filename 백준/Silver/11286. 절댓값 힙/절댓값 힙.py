import sys, heapq
input = sys.stdin.readline
h1 = [] # 양수만 저장(최솟값 힙)
h2 = [] # 음수만 저장(최댓값 힙)

for _ in range(int(input())):
    cmd = int(input())
    if cmd > 0:
        heapq.heappush(h1, cmd)
    elif cmd < 0:
        heapq.heappush(h2, -cmd)
    else:
        if not h1 and not h2:
            print(0)
        elif not h1 and h2:
            print(-heapq.heappop(h2))
        elif h1 and not h2:
            print(heapq.heappop(h1))
        else:
            if h1[0] >= h2[0]:
                print(-heapq.heappop(h2))
            else:
                print(heapq.heappop(h1))