cnt = 0


def merge_sort(A, l, r):
    if l < r:
        m = (l + r) // 2
        merge_sort(A, l, m)     # 전반부 정렬
        merge_sort(A, m + 1, r) # 후반부 정렬
        merge(A, l, m, r)       # 병합


def merge(A, l, m, r):
    global cnt

    i = l
    j = m + 1
    t = 0
    tmp = [0] * (r - l + 1)
    while i <= m and j <= r:
        if A[i] <= A[j]:
            tmp[t] = A[i]
            t += 1
            i += 1
        else:
            tmp[t] = A[j]
            t += 1
            j += 1

    # 왼쪽 배열이 남았다면
    while i <= m:
        tmp[t] = A[i]
        t += 1
        i += 1

    # 오른쪽 배열이 남았다면
    while j <= r:
        tmp[t] = A[j]
        t += 1
        j += 1

    i = l
    t = 0
    while i <= r:
        cnt += 1
        if cnt == k:
            print(tmp[t])
            exit(0)
        A[i] = tmp[t]
        i += 1
        t += 1


n, k = map(int, input().split())
a = list(map(int, input().split()))

merge_sort(a, 0, len(a) - 1)
print(-1)