s = input()
ans = set()
for i in range(1, len(s) + 1):
    for j in range(i):
        ans.add(s[j:i])
print(len(ans))