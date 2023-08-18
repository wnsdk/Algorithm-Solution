import sys
input = sys.stdin.readline

tot = 0
cnt = 0

for _ in range(20):
    subject, score, grade = input().strip().split()
    if grade == 'A+':
        tot += float(score) * 4.5
    elif grade == 'A0':
        tot += float(score) * 4
    elif grade == 'B+':
        tot += float(score) * 3.5
    elif grade == 'B0':
        tot += float(score) * 3
    elif grade == 'C+':
        tot += float(score) * 2.5
    elif grade == 'C0':
        tot += float(score) * 2
    elif grade == 'D+':
        tot += float(score) * 1.5
    elif grade == 'D0':
        tot += float(score) * 1

    if grade != 'P':
        cnt += float(score)

print(tot / cnt)
