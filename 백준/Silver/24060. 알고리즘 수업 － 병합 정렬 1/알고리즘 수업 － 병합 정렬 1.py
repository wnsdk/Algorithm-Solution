ans = -1
cnt = 0


def chk_ans(x):
    global cnt, ans
    cnt += 1
    if cnt == k:
        ans = x


def merge_sort(A, l, r):
    if l < r:
        m = (l + r) // 2
        merge_sort(A, l, m)     # 전반부 정렬
        merge_sort(A, m + 1, r) # 후반부 정렬
        merge(A, l, m, r)       # 병합


def merge(A, l, m, r):
    global ans, cnt

    i = l
    j = m + 1
    t = 0
    tmp = [0] * (r - l + 1)
    while i <= m and j <= r:
        if A[i] <= A[j]:
            chk_ans(A[i])
            tmp[t] = A[i]
            t += 1
            i += 1
        else:
            chk_ans(A[j])
            tmp[t] = A[j]
            t += 1
            j += 1

    # 왼쪽 배열이 남았다면
    while i <= m:
        chk_ans(A[i])
        tmp[t] = A[i]
        t += 1
        i += 1

    # 오른쪽 배열이 남았다면
    while j <= r:
        chk_ans(A[j])
        tmp[t] = A[j]
        t += 1
        j += 1

    i = l
    t = 0
    while i <= r:
        A[i] = tmp[t]
        i += 1
        t += 1


n, k = map(int, input().split())
a = list(map(int, input().split()))

merge_sort(a, 0, len(a) - 1)
print(ans)