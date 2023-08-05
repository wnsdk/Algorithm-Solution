import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.children = {}
        self.idx = False


class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, word):
        node = self.head

        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]

        node.idx = True

    def search(self, word):
        node = self.head
        cnt = 0

        for i, ch in enumerate(word):
            if node.idx or len(node.children.values()) > 1 or not i:
                cnt += 1
            node = node.children[ch]

        return cnt


while True:
    try:
        n = int(input())
        words = []
        trie = Trie()
        tot = 0

        for _ in range(n):
            words.append(input().strip())
            trie.insert(words[-1])

        for word in words:
            tot += trie.search(word)

        print(f'{round(tot / n, 2):0.2f}')

    except:
        break