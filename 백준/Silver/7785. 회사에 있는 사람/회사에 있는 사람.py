import sys

input = sys.stdin.readline
names = set()
for _ in range(int(input())):
    name, state = input().split()
    if state == 'enter':
        names.add(name)
    else:
        names.remove(name)
print('\n'.join(sorted(list(names), reverse=True)))