s = input()

# 팰린드롬인지 체크하기
def chk(word):
    return word == word[::-1]

for i in range(len(s)):
    # i번째부터 팰린드롬이라면
    if chk(s[i:]):
        print(i + len(s))
        break