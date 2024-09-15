import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    stk = deque()
    for ch in input().strip():
        if stk and ch == ')' and stk[-1] == '(':
            stk.pop()
        else:
            stk.append(ch)

    print('NO' if stk else 'YES')