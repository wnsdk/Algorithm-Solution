def solve(length, k, n):
    # 중심부 moo 길이
    middle = k + 3

    # 좌우 양측 각각의 moo 길이
    side = (length - k - 3) // 2

    if n < side:
        solve(side, k - 1, n)

    elif n < side + middle:
        print('m' if n == side else 'o')
        exit()

    else:
        solve(side, k - 1, n - side - middle)


solve(1073741792, 27, int(input()) - 1)
