n, m = map(int, input().split())
arr = [i + 1 for i in range(n)]

for _ in range(m):
    i, j = map(int, input().split())
    i -= 1
    arr = arr[:i] + (arr[i:j])[::-1] + arr[j:]

print(*arr)