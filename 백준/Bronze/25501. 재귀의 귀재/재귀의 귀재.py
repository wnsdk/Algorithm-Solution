import sys
input = sys.stdin.readline

cnt = 0


def recursion(s, l, r):
    global cnt
    cnt += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    return recursion(s, l + 1, r - 1)


def is_palindrome(s):
    return recursion(s, 0, len(s) - 1)


for _ in range(int(input())):
    cnt = 0
    S = input().strip()
    print(is_palindrome(S), cnt)