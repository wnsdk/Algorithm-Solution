D, K = map(int, input().split())

dp1 = [0] * D   # 첫쨋 날 준 떡 기준
dp2 = [0] * D   # 둘쨋 날 준 떡 기준

dp1[0] = 1
dp2[1] = 1

for i in range(2, D):
    dp1[i] = dp1[i - 1] + dp1[i - 2]
    dp2[i] = dp2[i - 1] + dp2[i - 2]

# 첫 날 준 떡의 개수
a = 1

# 둘쨋 날 준 떡의 개수
b = 1

while True:
    B = K - a * dp1[D - 1]
    if B % dp2[D - 1] == 0:
        b = B // dp2[D - 1]
        break
    a += 1

print(a)
print(b)