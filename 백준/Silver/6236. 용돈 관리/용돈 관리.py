import sys
input = sys.stdin.readline

# n일 동안, m번만 돈 뺀다
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]


# 인출 금액을 k원 으로 했을 때 인출 횟수를 반환
def count(k):
    # 인출 횟수
    cnt = 0

    # 현재 갖고 있는 돈
    money = 0

    for cost in arr:
        if money < cost:
            cnt += 1
            money = k
        money -= cost

    return cnt


lo = max(arr)
hi = sum(arr)

while lo <= hi:
    mi = (lo + hi) // 2

    # 인출 횟수가 m 이하여야한다.
    if count(mi) <= m:
        hi = mi - 1
    else:
        lo = mi + 1

print(mi)
