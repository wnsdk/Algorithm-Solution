def f(s):
    # 나쁜 수열인지 확인하기
    l = 1
    while l <= len(s) // 2:
        if s[len(s) - l * 2: len(s) - l] == s[len(s) - l: len(s)]:
            return
        l += 1

    if len(s) == n:
        print(s)
        exit(0)

    f(s + '1')
    f(s + '2')
    f(s + '3')


n = int(input())
f('')
