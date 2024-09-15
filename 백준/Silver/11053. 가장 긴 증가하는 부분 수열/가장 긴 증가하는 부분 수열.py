INF = float('inf')

n = int(input())
arr = list(map(int, input().split()))

# LIS[x] : x번째 숫자를 반드시 LIS에 포함시켰을 때, 그 때의 LIS의 길이 최댓값
LIS = [1] * n


for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            LIS[i] = max(LIS[i], LIS[j] + 1)

print(max(LIS))