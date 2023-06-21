N = int(input())
A = []
ans = [-1] * N

for i, item in enumerate(map(int, input().split())):
    while A and A[-1][0] < item:
        j = A.pop()[1]
        ans[j] = item

    A.append((item, i))

print(*ans)
