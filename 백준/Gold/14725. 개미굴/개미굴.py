import sys
input = sys.stdin.readline

n = int(input())
arr = sorted([input()[2:] for _ in range(n)])
ans = []

for j, items in enumerate(arr):
    items_list = items.split()
    for i, item in enumerate(items_list):
        # 그동안 나왔던 경로들(arr[: j])에서 현재 경로가 등장한 적 있다면, 해당 경로는 print 하지 않음
        idx2 = False
        for items2 in arr[: j]:
            items2_list = items2.split()
            if len(items2_list) < i + 1:
                continue

            idx = True

            for k in range(i + 1):
                if items2_list[k] != items_list[k]:
                    idx = False
                    break

            if idx:
                idx2 = True
                break

        if not idx2:
            s = '--' * i + item
            ans.append(s)

for item in ans:
    print(item)
