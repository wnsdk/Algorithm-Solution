from collections import deque

for _ in range(int(input())):
    ans_l = deque()
    ans_r = deque()
    for cmd in input():
        if cmd == '-':
            if len(ans_l):
                ans_l.pop()
        elif cmd == '<':
            if len(ans_l):
                ans_r.appendleft(ans_l.pop())
        elif cmd == '>':
            if len(ans_r):
                ans_l.append(ans_r.popleft())
        else:
            ans_l.append(cmd)
    print(''.join(ans_l) + ''.join(ans_r))