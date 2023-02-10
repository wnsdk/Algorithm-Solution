from collections import deque
import math

def solution(jobs):
    dq = deque(sorted(jobs, key = lambda x: x[0]))
    tasks = deque([])   # 대기 중인 작업들
    time = 0
    answer = 0
    
    # 하드디스크가 비었을 때, 하나의 요청이 왔다 -> 바로 실행
    # 하드디스크가 비었을 때, 요청이 여러개다 -> 실행시간이 짧은 것 부터 실행
    
    while dq or tasks:
        # print('시각 : ', time)
        # print('대기중 : ', tasks)
        # print('남은일 : ', dq)
        # 현재 시각(time) 기준, 요청이 들어온 작업을 모두 tasks에 담기
        while dq and dq[0][0] <= time:
            tasks.append(dq.popleft())
            
        # 만약 tasks에 담긴 task가 없다면, 시간을 흘려보내기
        if not tasks:
            time = dq[0][0]
            continue
        
        # tasks 중에서 무슨 task를 먼저 처리할 지 정하기 (실행시간이 짧은거부터)
        tasks = deque(sorted(tasks, key = lambda x: (x[1], x[0])))
        task = tasks.popleft()
        
        time += task[1]
        answer += time - task[0]
    
    return math.floor(answer / len(jobs))