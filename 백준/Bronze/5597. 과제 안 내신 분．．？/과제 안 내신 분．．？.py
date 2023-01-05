s = set([i for i in range(1, 31)])

for _ in range(28):
    n = int(input())
    if n in s:
        s.remove(n)

ans1 = s.pop()
ans2 = s.pop()
if ans1 > ans2:
    ans1, ans2 = ans2, ans1
print(ans1, ans2, sep='\n')