import sys
input = sys.stdin.readline

N = int(input())    # 기둥 개수
M = 0   # 제일 높은 기둥의 높이
pillars = []

for _ in range(N):
    # l 기둥 위치, h 기둥 높이
    l, h = map(int, input().split())
    pillars.append([l, h])
    M = max(M, h)

ans = 0 # 지붕 면적
first_M = -1    # 처음으로 등장한 최고 높이 기둥 위치
last_M = -1     # 마지막으로 등장한 최고 높이 기둥 위치

# 1. 앞에서 부터 최고 높이 기둥 나오기 전까지 계산
height = 0
pillars.sort()

for i, [l, h] in enumerate(pillars):
    ans += (l - pillars[i - 1][0]) * height

    # 더 높은 기둥이 나왔다면
    if height < h:
        height = h

    # 현재 기둥이 제일 높은 기둥이라면
    if h == M:
        first_M = l
        break

# 2. 뒤에서 부터 최고 높이 기둥 나오기 전까지 계산
height = 0
pillars.sort(reverse=True)

for i, [l, h] in enumerate(pillars):
    ans += (pillars[i - 1][0] - l) * height

    # 더 높은 기둥이 나왔다면
    if height < h:
        height = h

    # 현재 기둥이 제일 높은 기둥이라면
    if h == M:
        last_M = l
        break

# 3. 첫 최고 기둥과 마지막 최고 기둥 사이 면적 계산
ans += (last_M - first_M + 1) * M

# 답
print(ans)
