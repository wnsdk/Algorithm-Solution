N = int(input())
question = []

for _ in range(N):
    q, s, b = input().split()
    question.append(([int(q[0]), int(q[1]), int(q[2])], int(s), int(b)))

cnt = 0
for n0 in range(1, 10):
    for n1 in range(1, 10):
        if n0 == n1:
            continue

        for n2 in range(1, 10):
            if n0 == n2 or n1 == n2:
                continue

            # ans가 정답이 될 수 있는지 확인
            ans = [n0, n1, n2]
            idx = True

            for q, s, b in question:
                S = B = 0
                for i in range(3):
                    if q[i] == ans[i]:
                        S += 1
                    elif q[i] in ans:
                        B += 1

                if S != s or B != b:
                    idx = False
                    break

            if idx:
                cnt += 1

print(cnt)