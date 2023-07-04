import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    front = deque()
    back = deque()

    for command in list(input().strip()):
        # 지우기
        if command == '-':
            if front:
                front.pop()

        # 커서 왼쪽 이동
        elif command == '<':
            if front:
                back.appendleft(front.pop())

        # 커서 오른쪽 이동
        elif command == '>':
            if back:
                front.append((back.popleft()))

        # 글자 입력
        else:
            front.append(command)

    print(''.join(front) + ''.join(back))
