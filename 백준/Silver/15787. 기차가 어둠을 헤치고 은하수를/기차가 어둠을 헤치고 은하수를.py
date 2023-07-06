import sys

input = sys.stdin.readline

# 기차의 수 n, 명령의 수 m
n, m = map(int, input().split())
trains = [0b0] * (n + 1)

for _ in range(m):
    command = list(map(int, input().split()))

    # 태운다.
    if command[0] == 1:
        seat = command[2] - 1
        trains[command[1]] |= (1 << seat)

    # 하차시킨다.
    elif command[0] == 2:
        seat = command[2] - 1
        trains[command[1]] &= ~(1 << seat)

    # 한칸씩 뒤로 간다. 20번째 좌석은 하차한다.
    elif command[0] == 3:
        trains[command[1]] &= ~(1 << 19)
        trains[command[1]] <<= 1

    # 한칸씩 앞으로 간다. 1번째 좌석은 하차한다.
    elif command[0] == 4:
        trains[command[1]] &= ~(1 << 0)
        trains[command[1]] >>= 1

print(len(set(trains[1:])))
