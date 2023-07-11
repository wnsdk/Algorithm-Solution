import sys, re
input = sys.stdin.readline
n = int(input())
p = re.compile(input().replace('*', '.*'))
for _ in range(n):
    print('DA' if p.match(input()) else 'NE')