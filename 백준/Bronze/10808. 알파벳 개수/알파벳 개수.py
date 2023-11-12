from collections import defaultdict
d = defaultdict(int)

for c in input().strip():
    d[c] += 1

for i in range(26):
    print(d[chr(ord('a') + i)], end=' ')
