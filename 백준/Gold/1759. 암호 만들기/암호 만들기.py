l, c = map(int, input().split())
characters = sorted(input().split())
s = {'a', 'e', 'i', 'o', 'u'}


def combination(idx, password):
    if len(password) == l:
        # 모음의 개수
        cnt = len(set(password).intersection(s))
        
        if 0 < cnt <= l - 2:
            print(''.join(password))

    else:
        for i in range(idx, c):
            password.append(characters[i])
            combination(i + 1, password)
            password.pop()


combination(0, [])
