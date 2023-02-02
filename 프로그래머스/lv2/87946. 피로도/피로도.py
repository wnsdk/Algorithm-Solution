answer = -1

def solution(k, dungeons):
    global answer
    dfs(k, dungeons, 0, [False] * len(dungeons))
    return answer

def dfs(k, dungeons, cnt, visited):
    global answer
    answer = max(answer, cnt)
    
    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            dfs(k - dungeons[i][1], dungeons, cnt + 1, visited)
            visited[i] = False

        