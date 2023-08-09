import sys
import bisect
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())
ans = 0

for p1 in range(n):
    if arr[p1] > x:
        break

    left = bisect.bisect_left(arr, x - arr[p1], p1 + 1, n)
    right = bisect.bisect_right(arr, x - arr[p1], p1 + 1, n)

    ans += right - left

print(ans)
