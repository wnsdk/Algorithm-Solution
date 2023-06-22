import sys
input = sys.stdin.readline

for _ in range(int(input())):
    sizeA, sizeB = map(int, input().split())
    A = list(map(int, input().split()))
    B = sorted(list(map(int, input().split())))
    cnt = 0

    for target in A:
        l = 0
        h = sizeB - 1
        m = (l + h) // 2

        while l <= h:
            if B[m] < target:
                l = m + 1
            else:
                h = m - 1

            m = (l + h) // 2

        if B[m] < target:
            cnt += m + 1

    print(cnt)
    