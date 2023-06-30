n, k = map(int, input().split())
stk = []

for num in str(input()):
    # 현재 탐색 중인 num 보다 작은 애들 꺼내기 (최대 k번만)
    while k and stk and stk[-1] < num:
        k -= 1
        stk.pop()
    stk.append(num)

while k:
    k -= 1
    stk.pop()

if not stk:
    print(0)
else:
    for item in stk:
        print(item, end='')
