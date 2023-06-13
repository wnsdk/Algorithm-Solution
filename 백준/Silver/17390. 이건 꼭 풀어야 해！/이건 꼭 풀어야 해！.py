import sys
input = sys.stdin.readline

# N 수열의 길이, Q 질문의 개수
N, Q = map(int, input().split())
A = [0] + sorted(list(map(int, input().split())))

# 누적 합
for i in range(1, N + 1):
    A[i] += A[i - 1]

for _ in range(Q):
    L, R = map(int, input().split())
    print(A[R] - A[L - 1])