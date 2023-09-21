import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == -1:
        break

    arr = []
    for i in range(1, n):
        if n % i == 0:
            arr.append(i)

    if sum(arr) != n:
        print(n, 'is NOT perfect.')
    else:
        print(f'{n} = ', end='')
        print(' + '.join(map(str, arr)))