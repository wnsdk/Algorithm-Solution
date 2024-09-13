str = input()
s = set()
for i in range(len(str) + 1):
    for j in range(i):
        s.add(str[j:i])

print(len(s))