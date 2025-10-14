# Problem: Prefix and Suffix Search - https://leetcode.com/problems/prefix-and-suffix-search/

# class TrieNode:
#     def __init__(self,):
#         self.children = [None] * (26)
#         self.lastseen = []

# class Trie:
#     def __init__(self):
#         self.rootpre = TrieNode()
#         self.rootsuf = TrieNode()
        
#     def add(self,word,idx , ty = 0):
#         if ty:
#             cur = self.rootpre
#         else:
#             cur = self.rootsuf

#         for ch in word:
#             vl = ord(ch) - ord('a')
#             if cur.children[vl] == None:
#                 cur.children[vl] = TrieNode()
#             cur = cur.children[vl]
#             cur.lastseen.append(idx)

#     def search(self,word , ty = 0):
#         if ty:
#             cur = self.rootpre
#         else:
#             cur = self.rootsuf

#         for ch in word:
#             vl = ord(ch) - ord('a')
#             if cur.children[vl] == None:
#                 return -1
#             cur = cur.children[vl]
        
#         return cur.lastseen




            





class WordFilter:

    def __init__(self, words: List[str]):
        self.mp = defaultdict(lambda : inf)

        def do(word , idx):
            # print(word)

            n = len(word)
            if n == 1:
                # print(self.mp)
                self.mp[(word,word)] = idx
            tmp = ""
            for i in range(n):                                                            
                tmp += word[i]
                for j in range(n):
                    suf = word[j:]
                    self.mp[(tmp,suf)] = idx


        for i , wrd in enumerate(words):
            do(wrd , i)


        

    def f(self, pref: str, suff: str) -> int:


        fir = self.mp[(pref , suff)]
        return fir if fir != inf else -1



# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)