n = int(input())

nums = ['1', '2', '3']


# 나쁜 수열이면 True
def is_bad(s):
    size = len(s)
    if size < 2:
        return False

    for chunk in range(1, size // 2 + 1):
        if s[size - chunk * 2: size - chunk] == s[size - chunk: size]:
            return True
    return False


def f(ans):
    if len(ans) == n:
        print(ans)
        exit(0)
    else:
        for num in nums:
            if not is_bad(ans + num) and f(ans + num):
                return True
        return False

f('')