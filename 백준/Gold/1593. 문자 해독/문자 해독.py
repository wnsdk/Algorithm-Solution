import sys
input = sys.stdin.readline

sizeW, sizeS = map(int, input().split())
W = input().strip()
S = input().strip()

wd = dict()
sd = dict()

for ch in W:
    if ch in wd:
        wd[ch] += 1
    else:
        wd[ch] = 1
        sd[ch] = 0

ans = 0

for e in range(sizeS):
    # 끝 문자 추가
    if S[e] in sd:
        sd[S[e]] += 1

    if e >= sizeW - 1:
        if wd == sd:
            ans += 1

        # 앞 문자 제거
        s = e - sizeW + 1
        if S[s] in sd:
            sd[S[s]] -= 1

print(ans)
