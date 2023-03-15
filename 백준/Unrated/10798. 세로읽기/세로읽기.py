words = [''] * 15

for _ in range(5):
    for i, c in enumerate(input()):
        words[i] += c

ans = ''
for word in words:
    ans += word
print(ans)