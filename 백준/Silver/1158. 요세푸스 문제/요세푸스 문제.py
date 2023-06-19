n, k = map(int, input().split())

arr = [i for i in range(1, n + 1)]

print('<', end='')

i = 0
for _ in range(n - 1):
    i = (i + k - 1) % len(arr)
    print(arr.pop(i), end=', ')

print(arr.pop(), end='>')
