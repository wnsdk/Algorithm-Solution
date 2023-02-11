def solution(genres, plays):
    answer = []
    size = len(genres)
    
    d1 = dict() # 장르별로 수록곡을 저장 (재생 횟수를 기준으로 정렬)
    d2 = dict() # 장르별 총 재생 횟수를 저장
    
    for i in range(size):
        if genres[i] not in d1:
            d1[genres[i]] = []
            d2[genres[i]] = 0
        
        d1[genres[i]].append((plays[i], i))
        d2[genres[i]] += plays[i]
    
    # 장르별 총 재생 횟수를 총 재생 횟수를 기준으로 정렬하기
    rank = sorted(list(d2.items()), key = lambda x: -x[1])
    
    for genre, cnt in rank:
        l = sorted(d1.get(genre), key = lambda x: (-x[0], x[1]))

        answer.append(l[0][1])
        if len(l) > 1:
            answer.append(l[1][1])
            
    return answer