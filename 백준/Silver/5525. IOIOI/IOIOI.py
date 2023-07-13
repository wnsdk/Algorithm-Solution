n = int(input())
input()
s = input().strip('O')


def findI(string, start):
    for j in range(start, len(string)):
        if string[j] == 'I':
            return j
    return len(string)


ans = 0
cnt = 0
i = 1

while i < len(s) - 1:
    if s[i: i + 2] == 'OI':
        cnt += 1

        if cnt >= n:
            ans += 1

        i += 2

    else:
        cnt = 0
        i = findI(s, i) + 1

print(ans)
