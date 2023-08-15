import bisect
from collections import defaultdict
from itertools import product

def solution(info, query):
    
    infos = [i.split() for i in info]
    queries = [[i for i in q.split() if i != 'and'] for q in query]
    
    scores = defaultdict(list)
    
    for info in infos:
        for record in product(*[('-', e) for e in info[:-1]]):
            scores[record].append(int(info[-1]))
    
    for s in scores:
        scores[s].sort()
    
    answer = []
    for query in queries:
        score = int(query[-1])
        record = tuple(query[:-1])
        answer.append(len(scores[record]) - bisect.bisect_left(scores[record], score))
    return answer
