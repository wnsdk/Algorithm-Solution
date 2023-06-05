INF = float('inf')  # 양수 무한대
N = int(input())    # 총 칸 수
A = list(map(int, input().split()))

# cnt[i] : i번째 칸에 오기 위해 필요한 최소 점프 수
cnt = [INF] * N
cnt[0] = 0

for i in range(1, N):
    for j in range(i):
        # j번째 칸에서 i번째 칸으로 점프가 가능하다면
        if A[j] >= i - j:
            cnt[i] = min(cnt[i], cnt[j] + 1)

print(cnt[N - 1] if cnt[N - 1] < INF else -1)