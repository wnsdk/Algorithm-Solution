N = int(input())
ans = [0] * N
ans[0] = 1

# i번째 자리에 숫자를 넣겠다.
def dfs(i):
    global N

    if i == N:
        for num in ans:
            print(num, end='')
        exit()

    for n in range(1, 4):
        ans[i] = n

        # 나쁜 수열인지 체크하기
        isBad = False
        for j in range((i + 1) // 2):
            if ans[i - 2 * j - 1:i - j] == ans[i - j:i + 1]:
                isBad = True
                break

        if isBad and n == 3:
            return False

        if isBad:
            continue

        if not dfs(i + 1):
            continue

    return True

dfs(0)

