# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class Node:
    def __init__(self):
        self.childs = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        tmp = self.root
        for let in word:
            if let not in tmp.childs:
                tmp.childs[let] = Node()

            tmp = tmp.childs[let]

        tmp.end = True
        

    def search(self, word: str) -> bool:
        

        def dfs(cur = 0 ,  tmp = self.root):
            if cur == len(word) and tmp.end:
                return True

            if cur == len(word) or (word[cur] != '.' and word[cur] not in tmp.childs):
                return False

            if word[cur] == '.':
                for nodes in tmp.childs:
                    if dfs(cur+1 , tmp.childs[nodes]):
                        return True

            if word[cur] in tmp.childs and dfs(cur+1 , tmp.childs[word[cur]]):
                return True

            return False


        return dfs()
                
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)