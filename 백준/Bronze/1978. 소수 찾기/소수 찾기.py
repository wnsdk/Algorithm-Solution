def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


cnt = 0
input()
for n in map(int, input().split()):
    if is_prime(n):
        cnt += 1

print(cnt)