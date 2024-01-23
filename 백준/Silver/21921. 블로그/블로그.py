n, x = map(int, input().split())
arr = list(map(int, input().split()))

window = 0
for i in range(x):
    window += arr[i]

ans = window
cnt = 1

p1 = 0
p2 = x

while p2 < n:
    window -= arr[p1]
    window += arr[p2]

    if window > ans:
        ans = window
        cnt = 1
    elif window == ans:
        cnt += 1

    p1 += 1
    p2 += 1

if ans:
    print(ans)
    print(cnt)
else:
    print('SAD')
