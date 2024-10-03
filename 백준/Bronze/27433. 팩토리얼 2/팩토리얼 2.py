import sys
sys.setrecursionlimit(10 ** 6)


def factorial(x):
    if x == 0:
        return 1
    return x * factorial(x - 1)


print(factorial(int(input())))