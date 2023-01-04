N = int(input())
l = map(int, input().split())
v = int(input())
ans = 0

for i in l:
    if v == i:
        ans += 1

print(ans)