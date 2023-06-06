import math

# X 게임 횟수, Y 이긴 게임 수
X, Y = map(int, input().split())

Z = math.floor(Y * 100 / X)

if Z >= 99:
    print(-1)
else:
    Z += 1
    print(math.ceil((Z * X - 100 * Y) / (100 - Z)))