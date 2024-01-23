import math


def is_prime(x):
    if x < 2:
        return False

    for a in range(2, int(math.sqrt(x)) + 1):
        if x % a == 0:
            return False
    return True


input()
ans = 0
for n in map(int, input().split()):
    if is_prime(n):
        ans += 1

print(ans)
