def factorial(x):
    if not x:
        return 1
    return x * factorial(x - 1)


n = int(input())
print(factorial(n))
