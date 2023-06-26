import sys
input = sys.stdin.readline

# n 단어의 개수, k 가르칠 글자 개수
n, k = map(int, input().split())

words = []
for _ in range(n):
    # 단어의 알파벳 구성을 2진수로 표현
    word = 0b0
    for ch in set(list(input().strip())):
        word |= (1 << ord(ch) - ord('a'))

    words.append(word)

if k < 5:
    print(0)
    exit()

ans = 0

# 0부터 25까지의 26개의 숫자 중에서 k개의 숫자를 조합하기
def combination(idx, alpha, depth):
    global k, words, ans, antic

    # k개를 다 뽑았다면
    if depth == k - 5:
        # alpha 를 통해 읽을 수 있는 단어 개수 구하기
        cnt = 0
        for word in words:
            if (alpha & word) == word:
                cnt += 1
        ans = max(ans, cnt)
    else:
        for i in range(idx + 1, 26):
            if i in set([0, 2, 8, 13, 19]):
                continue
            combination(i, alpha | (1 << i), depth + 1)


antic = 0b0
# antic 는 꼭 포함 0, 2, 8, 13, 19
antic |= (1 << 0)
antic |= (1 << 2)
antic |= (1 << 8)
antic |= (1 << 13)
antic |= (1 << 19)

combination(0, antic, 0)
print(ans)
