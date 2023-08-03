from collections import defaultdict

class Node(object):
    def __init__(self, key, d=0, data=False):
        self.key = key  # 값으로 입력될 문자
        self.data = data    # 문자열의 종료를 알리는 flag (전체 문자열을 저장)
        self.children = {}  # 자식 노드를 저장
        self.d = d


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        node = self.head

        for ch in string:
            if ch not in node.children:
                node.children[ch] = Node(ch)
            
            node = node.children[ch]
            node.d += 1

        node.data = True

    def start_with(self, prefix):
        cur = self.head
        cnt = 0

        for ch in prefix:
            if ch == '?':
                return cnt
            
            if ch not in cur.children:
                return 0
            
            cur = cur.children[ch]
            cnt = cur.d
            
        return cnt
            


def solution(words, queries):
    answer = []
    length = [0] * 10001
    
    trie = defaultdict(Trie)
    trie_reverse = defaultdict(Trie)
    
    for word in words:
        trie[len(word)].insert(word)
        trie_reverse[len(word)].insert(word[::-1])
        length[len(word)] += 1
    
    for query in queries:
        if query[0] == '?' and query[-1] == '?':
            answer.append(length[len(query)])
        elif query[0] != '?':
            answer.append(trie[len(query)].start_with(query))
        else:
            answer.append(trie_reverse[len(query)].start_with(query[::-1]))
        
    return answer
