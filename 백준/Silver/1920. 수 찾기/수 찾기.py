N = int(input())
arr = set(map(int, input().split()))
M = int(input())
find = list(map(int, input().split()))
for i in find:
    if i in arr:
        print(1)
    else:
        print(0)