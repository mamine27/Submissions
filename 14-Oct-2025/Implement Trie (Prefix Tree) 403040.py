# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:

    def __init__(self):
        self.childs = {}
        self.end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:

        tmp = self.root
        for cur in word:
            Node = TrieNode()
            if cur not in tmp.childs:
                tmp.childs[cur] = Node
                tmp = Node

            else:
                tmp = tmp.childs[cur]

        tmp.end = True

        

    def search(self, word: str) -> bool:
        tmp = self.root

        for cur in word:
            if cur not in tmp.childs:
                return False

            tmp = tmp.childs[cur]

        return tmp.end


        

    def startsWith(self, prefix: str) -> bool:
        tmp = self.root

        for cur in prefix:
            if cur not in tmp.childs:
                return False

            tmp = tmp.childs[cur]

        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)