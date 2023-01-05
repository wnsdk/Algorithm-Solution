n = int(input())    # 색종이 수
paper = [[0] * 100 for _ in range(100)]

for _ in range(n):
    left, bottom = map(int, input().split())
    for y in range(10):
        for x in range(10):
            paper[bottom + y][left + x] += 1

ans = 0
for y in range(100):
    for x in range(100):
        if paper[y][x] > 0:
            ans += 1

print(ans)