# d는 number 자릿수
d, number = map(int, input().split())
arr = list(map(int, list(str(number))))

# 이동
moveX, moveY = map(int, input().split())

# 현재 내 위치 좌표
my = mx = 0

# 좌표평면 크기
size = pow(2, d)


# 1단계 : 현재 내 위치를 좌표로 나타내기
def find(i, y, x):
    global d, my, mx
    
    # 재귀 종료 조건
    if i == d - 1:
        my, mx = y, x

        if arr[i] == 1 or arr[i] == 4:
            mx += 1
        if arr[i] == 3 or arr[i] == 4:
            my += 1

    else:
        if arr[i] == 1 or arr[i] == 4:
            x += pow(2, d - i - 1)
        if arr[i] == 3 or arr[i] == 4:
            y += pow(2, d - i - 1)

        find(i + 1, y, x)


find(0, 0, 0)

# 2단계 : 위치 이동하기
my -= moveY
mx += moveX

if my < 0 or my >= size or mx < 0 or mx >= size:
    print(-1)
    exit()


# 3단계 : 이동한 위치 좌표의 사분면 알아내기
ans = ''


def quadrant(i, y, x):
    global d, my, mx, ans
    
    # 재귀 종료 조건
    if i == d:
        print(ans)
        exit()

    unit = pow(2, d - i - 1)

    if my < y + unit and mx >= x + unit:
        ans += '1'
        quadrant(i + 1, y, x + unit)

    elif my < y + unit and mx < x + unit:
        ans += '2'
        quadrant(i + 1, y, x)

    elif my >= y + unit and mx < x + unit:
        ans += '3'
        quadrant(i + 1, y + unit, x)

    elif my >= y + unit and mx >= x + unit:
        ans += '4'
        quadrant(i + 1, y + unit, x + unit)


quadrant(0, 0, 0)
