S = input()
bomb = input()

arr = []

for i, ch in enumerate(S):
    arr.append(ch)

    if len(arr) < len(bomb):
        continue
    
    # arr의 제일 끝 문자열이 폭탄 문자열인지 확인
    isSame = True
    for j in range(len(bomb)):
        if arr[len(arr) - len(bomb) + j] != bomb[j]:
            isSame = False
            break

    # 폭탄 문자열이라면 pop
    if isSame:
        for _ in range(len(bomb)):
            arr.pop()

if not len(arr):
    print('FRULA')
else:
    for item in arr:
        print(item, end='')