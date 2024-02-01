st = input()
size = len(st)

ans = set()

for s in range(size):
    for e in range(s + 1, size + 1):
        ans.add(st[s: e])

print(len(ans))
