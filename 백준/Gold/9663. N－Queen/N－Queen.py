N = int(input())
ans = 0
chk_col = [False] * N
chk_d1 = [False] * 2 * N  # 대각선 \, 우상단부터 0
chk_d2 = [False] * 2 * N  # 대각선 /, 좌상단부터 0


def bt(row):
    global ans
    if row == N:
        ans += 1
        return

    for col in range(N if row else N // 2):
        if not chk_col[col] and not chk_d1[row - col] and not chk_d2[row + col]:
            chk_col[col] = True
            chk_d1[row - col] = True
            chk_d2[row + col] = True

            bt(row + 1)

            chk_d2[row + col] = False
            chk_d1[row - col] = False
            chk_col[col] = False


if N % 2:
    bt(0)
    ans *= 2

    j = N // 2
    chk_col[j] = chk_d1[-j] = chk_d2[j] = True
    bt(1)

    print(ans)

else:
    bt(0)
    print(ans * 2)