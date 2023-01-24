answer = 999999

# 알파벳 'A'에서 Z를 만들려면 조이스틱을 몇 번 조작하는지 반환하는 함수
def diff(Z):
    diff1 = ord(Z) - ord('A')
    diff2 = ord('Z') - ord(Z) + 1
    return min(diff1, diff2)

# i번째 글자를 탐색
def dfs(now, name, cnt1, cnt2, i, direction, isPossible):
    global answer
    
    if now == name:
        answer = min(answer, cnt1 + cnt2 - 1)
        return
    
    if cnt1 + cnt2 - 1 >= answer:
        return
    
    # i번째 글자를 맞춰주기
    if now[i] != name[i]:
        cnt2 += diff(name[i])
        now = now[:i] + name[i] + now[i + 1:]
    
    # 다음 인덱스로 이동
    next1 = i + direction
    if next1 == -1:
        next1 = len(name) - 1
    elif next1 == len(name):
        next1 = 0
    
    dfs(now, name, cnt1 + 1, cnt2, next1, direction, True)
    
    # 방향전환을 여태까지 한 번도 안했고, 현재 인덱스가 'A'가 아니고, 절반 이상 이동하지 않았다면, 방향전환 해보기
    if isPossible and now[i] != 'A' and cnt1 <= len(name) // 2:
        direction *= -1
        next2 = i + direction
        if next2 == -1:
            next2 = len(name) - 1
        elif next2 == len(name):
            next2 = 0
        
        dfs(now, name, cnt1 + 1, cnt2, next2, direction, False)
    

def solution(name):
    # 현재 이름
    now = ''
    for _ in range(len(name)):
        now += 'A'
    
    if name == now:
        return 0
    
    # 오른쪽으로 이동
    dfs(now, name, 0, 0, 0, 1, True)
    # 왼쪽으로 이동
    dfs(now, name, 0, 0, 0, -1, True)
    global answer
    return answer