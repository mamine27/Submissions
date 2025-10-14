# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class Node:
    def __init__(self):
        self.childs = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word):
        tmp = self.root

        for let in word:
            if let not in tmp.childs:
                tmp.childs[let] = Node()

            tmp = tmp.childs[let]

        tmp.end = True

    def search(self,word):
        tmp = self.root
        ans = []
        for let in word:
            if tmp.end:
                return "".join(ans)
            ans.append(let)
            if let not in tmp.childs:
                return False
            tmp = tmp.childs[let]
    
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        tr = Trie()

        for roots in dictionary:
            tr.add(roots)

        res = []

        for words in sentence.split():
            val = tr.search(words)
            res.append(val if val else words)

        return " ".join(res)

        