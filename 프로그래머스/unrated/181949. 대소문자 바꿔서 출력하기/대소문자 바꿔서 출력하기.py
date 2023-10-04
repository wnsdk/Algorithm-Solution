str = input()
for c in str:
    if c.islower():
        print(c.upper(), end='')
    else:
        print(c.lower(), end='')