max = max_y = max_x = -1

for y in range(9):
    for x, v in enumerate(map(int, input().split())):
        if max < v:
            max = v
            max_y = y
            max_x = x

print(max)
print(max_y + 1, max_x + 1)