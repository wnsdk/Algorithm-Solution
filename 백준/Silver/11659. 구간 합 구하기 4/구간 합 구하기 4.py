import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
prefix_sum = [0]

for i in range(1, n + 1):
    prefix_sum.append(arr[i] + prefix_sum[i - 1])

for _ in range(m):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i - 1])
