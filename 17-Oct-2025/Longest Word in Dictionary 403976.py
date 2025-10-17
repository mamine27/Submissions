# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class Solution:
    def longestWord(self, words: List[str]) -> str:
        class tr:
            def __init__(self):
                self.children = defaultdict(int)
                self.end = False

        class Trie:

            def __init__(self):
                self.root = tr()
                self.root.end = True

            def insert(self , word):
                cur = self.root
                for ch in word:
                    if ch not in cur.children:
                        cur.children[ch] = tr()

                    cur = cur.children[ch]

                cur.end = True

            def solve(self):

                pos = []
                def dfs(tmp = "", cur = self.root):
                    if not cur.end:
                        return
                    for ch in cur.children:
                        dfs( tmp + ch , cur.children[ch])

                    pos.append(tmp)

                dfs()
                mx = sorted(pos , key = lambda x : len(x))[-1]

                for i in pos:
                    if len(i) == len(mx):
                        mx = min(mx ,i)

                return mx
                


        cook = Trie()

        for wrd in words:
            cook.insert(wrd)


        return cook.solve()


        
