import sys
import heapq
input = sys.stdin.readline
EMPTY = 'EMPTY'

for _ in range(int(input())):
    min_h = []
    max_h = []
    min_d = dict()
    max_d = dict()

    for _ in range(int(input())):
        command, n = input().split()
        n = int(n)

        # 삽입
        if command == 'I':
            heapq.heappush(min_h, n)
            heapq.heappush(max_h, -n)

        # 삭제할 것이 없다면
        elif not max_h or not min_h:
            max_h.clear()
            min_h.clear()
            max_d.clear()
            min_d.clear()

        # 최솟값 삭제
        elif n == -1:
            idx = True
            dn = heapq.heappop(min_h)

            while dn in min_d and min_d[dn]:
                min_d[dn] -= 1
                if not min_h:
                    idx = False
                    break
                dn = heapq.heappop(min_h)

            if idx:
                if dn in max_d:
                    max_d[dn] += 1
                else:
                    max_d[dn] = 1

        # 최댓값 삭제
        else:
            idx = True
            dn = -heapq.heappop(max_h)

            while dn in max_d and max_d[dn]:
                max_d[dn] -= 1
                if not max_h:
                    idx = False
                    break
                dn = -heapq.heappop(max_h)
            
            if idx:
                if dn in min_d:
                    min_d[dn] += 1
                else:
                    min_d[dn] = 1

    ans1 = -heapq.heappop(max_h) if max_h else EMPTY
    while ans1 in max_d and max_d[ans1]:
        max_d[ans1] -= 1
        if not max_h:
            ans1 = EMPTY
            break
        ans1 = -heapq.heappop(max_h)

    ans2 = heapq.heappop(min_h) if min_h else EMPTY
    while ans2 in min_d and min_d[ans2]:
        min_d[ans2] -= 1
        if not min_h:
            ans2 = EMPTY
            break
        ans2 = heapq.heappop(min_h)

    if ans1 == EMPTY or ans2 == EMPTY:
        print(EMPTY)

    else:
        print(ans1, ans2)
