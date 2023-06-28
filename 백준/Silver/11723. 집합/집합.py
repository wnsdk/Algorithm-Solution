import sys
input = sys.stdin.readline

s = set()

for _ in range(int(input())):
    command = input().split()

    if command[0] == 'add':
        n = int(command[1])
        s.add(n)

    elif command[0] == 'remove':
        n = int(command[1])
        if n in s:
            s.remove(n)

    elif command[0] == 'check':
        n = int(command[1])
        print(1 if n in s else 0)

    elif command[0] == 'toggle':
        n = int(command[1])
        if n in s:
            s.remove(n)
        else:
            s.add(n)

    elif command[0] == 'all':
        s = set([i for i in range(1, 21)])

    elif command[0] == 'empty':
        s.clear()
