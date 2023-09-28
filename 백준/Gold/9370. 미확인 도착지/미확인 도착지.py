import heapq
import sys

input = sys.stdin.readline
INF = 1e9

for _ in range(int(input())):
    # n 교차로 개수 / m 도로 개수 / t 목적지 후보 개수
    n, m, t = map(int, input().split())

    # s 출발지 / g와 h 교차로 사이에 있는 도로를 지나감
    s, g, h = map(int, input().split())

    adj = [[] for _ in range(n + 1)]

    for _ in range(m):
        # a와 b 사이에 길이 d인 양방향 도로
        a, b, d = map(int, input().split())
        if (a, b) == (g, h) or (a, b) == (h, g):
            d -= 0.01
        adj[a].append((d, b))
        adj[b].append((d, a))

    goals = set()

    for _ in range(t):
        # 목적지 후보
        goals.add(int(input()))

    ans = set()
    dp = [INF] * (n + 1)
    heap = []

    dp[s] = 0
    heapq.heappush(heap, (0, s))

    while heap:
        dist, now = heapq.heappop(heap)

        # float 이라면 지나야할 곳을 지난 것
        if isinstance(dp[now], float) and now in goals:
            ans.add(now)

        for d, x in adj[now]:
            cost = d + dist
            if cost < dp[x]:
                heapq.heappush(heap, (cost, x))
                dp[x] = cost

    print(*sorted(list(ans)))
