# 바구니 개수 N개 (1 ~ N)
# M번 공을 넣는다
N, M = map(int, input().split())

arr = [0] * N

# 공을 넣는 방법
for _ in range(M):
    # i번 바구니부터 j번 바구니까지 k번 번호가 적혀 있는 공을 넣는다.
    i, j, k = map(int, input().split())

    for idx in range(i - 1, j):
        arr[idx] = k

print(*arr)