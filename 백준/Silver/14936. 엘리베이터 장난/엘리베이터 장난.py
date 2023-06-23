# 1 ~ N층, m초 동안 버튼 누르기
N, m = map(int, input().split())

bit1 = 0
bit2 = 0
bit3 = 0
bit4 = 0
time1 = N
time2 = N // 2
time3 = N // 2 + N % 2
time4 = N // 3 if N % 3 == 0 else N // 3 + 1

for i in range(N):
    bit1 |= (1 << i)
    if i % 3 == 0:
        bit4 |= (1 << i)
    if i % 2 == 0:
        bit2 |= (1 << i)
    else:
        bit3 |= (1 << i)

ans = set()


def solve(bit, time):
    global bit1, bit2, bit3, bit4, time1, time2, time3, time4

    ans.add(bit)

    # 모든 버튼 누르기
    if time >= time1:
        solve(bit ^ bit1, time - time1)

    # 짝수 층 누르기
    if N >= 2 and time >= time2:
        solve(bit ^ bit2, time - time2)

    # 홀수 층 누르기
    if N >= 2 and time >= time3:
        solve(bit ^ bit3, time - time3)

    # 3k + 1층 누르기
    if N >= 3 and time >= time4:
        solve(bit ^ bit4, time - time4)


solve(0, m)
print(len(ans))
