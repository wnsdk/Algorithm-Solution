N = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = float('inf')
ans = ''

for i in range(N):
    # 이분 탐색으로 찾고자 하는 수
    target = -arr[i]

    l = i + 1
    r = N - 1
    m = (l + r) // 2

    while l <= r:
        # 정답 갱신
        tot = abs(arr[i] + arr[m])
        if result > tot:
            result = tot
            ans = str(arr[i]) + ' ' + str(arr[m])

        # 이분 탐색
        if arr[m] < target:
            l = m + 1
        elif arr[m] > target:
            r = m - 1
        else:
            break

        m = (l + r) // 2

print(ans)