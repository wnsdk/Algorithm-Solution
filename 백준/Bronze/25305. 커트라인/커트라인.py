# N : 응시자 수
# k : 상을 받는 사람의 수
N, k = map(int, input().split())

score = list(map(int, input().split()))
score.sort(reverse=True)

print(score[k - 1])