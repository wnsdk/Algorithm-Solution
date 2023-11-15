x = input()
ans = 0
if len(x) > 1:
    if x[0] == 'A':
        ans = 4
    elif x[0] == 'B':
        ans = 3
    elif x[0] == 'C':
        ans = 2
    elif x[0] == 'D':
        ans = 1

    if x[1] == '+':
        ans += 0.3
    elif x[1] == '-':
        ans -= 0.3
print(f'{ans:.1f}')