n, m = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
tot = 0

p1 = 0
p2 = 0

while p2 < n:
    while tot <= m and p2 < n:
        tot += arr[p2]
        p2 += 1

        if tot == m:
            cnt += 1

    while tot > m and p1 <= p2:
        tot -= arr[p1]
        p1 += 1

        if tot == m:
            cnt += 1

print(cnt)