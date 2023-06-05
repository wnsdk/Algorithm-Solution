import math

# N 트랙 길이, M 심판 수, K 심판이 있을 수 있는 위치 수
N, M, K = map(int, input().split())

# 심판이 있을 수 있는 위치
spot = list(map(int, input().split()))

ans = [0] * K

l = 1
h = spot[K - 1] - spot[0]
m = math.ceil((l + h) / 2)

# 심판 간 거리 최솟값을 dist
def chk(dist):
    # print('거리 :', dist)
    global M, K, spot, ans
    judgement = [0] * K

    # 맨 첫 번째 위치에 심판 1명 두고 시작하기
    cnt = 1
    prev = spot[0]
    judgement[0] = 1

    for i, now in enumerate(spot):
        if cnt == M:
            break

        if not i or now - prev < dist:
            continue

        # i번째 자리에 심판 배치하기
        judgement[i] = 1
        prev = now
        cnt += 1

    # 심판 M명을 모두 배치했다면, dist 값을 좀 더 늘려봐도 됨.
    if cnt == M:
        ans = judgement[::]
        return 1

    # 심판을 모두 배치하지 못했다면, dist 값은 더 작아야 함.
    return -1

while l <= h:
    # 심판 사이 거리 최솟값이 m이라고 할 때, 심판을 모두 세우는 것이 가능한지 확인하기
    if chk(m) < 0:
        h = m - 1
    else:
        l = m + 1

    m = math.ceil((l + h) / 2)

# print(m)
for i in ans:
    print(i, end='')