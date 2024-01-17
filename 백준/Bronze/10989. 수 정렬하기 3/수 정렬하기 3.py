# 배열을 이용한 풀이
import sys
input = sys.stdin.readline

n = int(input())
arr = [0] * 10001

for _ in range(n):
    arr[int(input())] += 1

for num, cnt in enumerate(arr):
    for _ in range(cnt):
        print(num)