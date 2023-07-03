n, k = map(int, input().split())
arr = list(map(int, input().split()))

lions = []

for i in range(n):
    if arr[i] == 1:
        lions.append(i)

size = len(lions)

if size < k:
    print(-1)
    exit()

s = 0
e = k
ans = float('inf')

while s < size and e <= size:
    ans = min(ans, lions[e - 1] - lions[s] + 1)
    s += 1
    e += 1

print(ans)