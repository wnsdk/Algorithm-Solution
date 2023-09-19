import sys
from collections import deque

input = sys.stdin.readline
dq = deque()

for _ in range(int(input())):
    commands = list(map(int, input().split()))
    comm = commands[0]
    if len(commands) == 2:
        if comm == 1:
            dq.appendleft(commands[1])
        elif comm == 2:
            dq.append(commands[1])
    else:
        if comm == 3:
            print(dq.popleft() if len(dq) else -1)
        elif comm == 4:
            print(dq.pop() if len(dq) else -1)
        elif comm == 5:
            print(len(dq))
        elif comm == 6:
            print(0 if len(dq) else 1)
        elif comm == 7:
            print(dq[0] if len(dq) else -1)
        elif comm == 8:
            print(dq[-1] if len(dq) else -1)
