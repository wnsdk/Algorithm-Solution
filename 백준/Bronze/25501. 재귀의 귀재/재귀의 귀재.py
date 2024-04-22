import sys
input = sys.stdin.readline


def isPalindrome(str, l, r):
    global cnt
    cnt += 1
    if l >= r:
        return 1
    if str[l] != str[r]:
        return 0
    return isPalindrome(str, l + 1, r - 1)


for _ in range(int(input())):
    cnt = 0
    s = input().strip()
    print(isPalindrome(s, 0, len(s) - 1), cnt)
    