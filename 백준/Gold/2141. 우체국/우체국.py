import sys
input = sys.stdin.readline

N = int(input())
arr = []

# 전체 인구 수
tot = 0

# 입력 받기
for i in range(N):
    x, a = map(int, input().split())
    arr.append([x, a])
    tot += a

# 위치 순으로 정렬
arr.sort()

for i in range(N):
    if i:
        arr[i][1] += arr[i - 1][1]

    # 전체 인구의 과반수가 처음으로 넘는 지점 찾기
    if arr[i][1] >= tot / 2:
        print(arr[i][0])
        break
