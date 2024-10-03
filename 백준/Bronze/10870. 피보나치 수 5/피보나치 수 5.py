def fibonacci(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    if cache[x] > -1:
        return cache[x]
    cache[x] = fibonacci(x - 1) + fibonacci(x - 2)
    return cache[x]


n = int(input())
cache = [-1] * (n + 1)
print(fibonacci(n))