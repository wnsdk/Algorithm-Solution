import sys
input = sys.stdin.readline

n = int(input())

# 돈 제일 많이 주는 것부터 정렬
lecture = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: (-x[0], x[1]))

# day[x] : x번째 날에 버는 돈
day = [0] * 10001

for p, d in lecture:
    # 최대한 마지막 날에 강연하기
    while day[d] != 0 and d > 0:
        d -= 1

    if d > 0:
        day[d] = p

print(sum(day))
