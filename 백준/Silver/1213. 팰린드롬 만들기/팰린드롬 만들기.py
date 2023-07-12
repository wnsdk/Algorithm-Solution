string = input()
n = len(string)

ans = [''] * n
s = 0

for i in range(26):
    c = chr(ord('A') + i)

    cnt = string.count(c)

    # c 문자가 존재하지 않으면
    if not cnt:
        continue

    for j in range(cnt // 2):
        ans[s + j] = ans[n - 1 - s - j] = c
    s += cnt // 2

    # c 문자가 홀수 개 이면
    if cnt % 2:
        if not n % 2 or ans[n // 2] != '':
            print("I'm Sorry Hansoo")
            exit()

        ans[n // 2] = c

print(''.join(ans))
