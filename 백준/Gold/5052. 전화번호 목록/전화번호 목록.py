import sys
input = sys.stdin.readline

# 테스트 케이스 수
t = int(input())
ans = ''

for _ in range(t):
    # 전화번호 수
    n = int(input())
    phone = []
    NO = False

    # 전화번호 입력받기
    for _ in range(n):
        phone.append(input().rstrip())

    # 전화번호 정렬하기 -> 내 다음 번 전화번호랑만 비교하면 됨
    phone.sort()

    for i in range(0, n - 1):
        length = len(phone[i])

        # next가 now로 시작하는지 확인하기
        if phone[i + 1][:length] == phone[i]:
            ans += 'NO\n'
            NO = True
            break

    if not NO:
        ans += 'YES\n'

print(ans)