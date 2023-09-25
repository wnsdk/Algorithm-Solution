import sys
input = sys.stdin.readline


def merge(p, q, r):
    global k
    i = p
    j = q + 1
    t = 1

    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp[t] = A[i]
            i += 1
        else:
            tmp[t] = A[j]
            j += 1
        t += 1

    while i <= q:
        tmp[t] = A[i]
        t += 1
        i += 1

    while j <= r:
        tmp[t] = A[j]
        t += 1
        j += 1

    i = p
    t = 1

    while i <= r:
        k -= 1
        A[i] = tmp[t]
        if k == 0:
            print(tmp[t])
            exit(0)

        i += 1
        t += 1


# 리스트 A의 p ~ r 범위를 정렬한다.
def merge_sort(p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(p, q)
        merge_sort(q + 1, r)
        merge(p, q, r)


n, k = map(int, input().split())
A = [0] + list(map(int, input().split()))   # 1-based
tmp = [-1] * (n + 1)
merge_sort(1, n)

if k > 0:
    print(-1)
