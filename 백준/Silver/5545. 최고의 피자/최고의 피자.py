import math

# 토핑의 종류 수
N = int(input())

# A 도우의 가격, B 토핑의 가격
A, B = map(int, input().split())

# 도우의 열량
C = int(input())

toppings = []
for _ in range(N):
    # 각 토핑별 열량
    toppings.append(int(input()))

toppings.sort(reverse=True)

price = A
kcal = C

for topping in toppings:
    if kcal / price < (kcal + topping) / (price + B):
        kcal += topping
        price += B
    else:
        break

print(math.floor(kcal / price))