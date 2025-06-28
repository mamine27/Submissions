# Problem: Number of Wonderful Substrings - https://leetcode.com/problems/number-of-wonderful-substrings/

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        

        n = len(word)
        pre = defaultdict(int)
        cnt = 0
        ans = 0
        get = []
        pre[0] = 1
        for let in word:
            cnt ^= (1 << (ord(let ) - ord('a')))
            for i in range(10):
                cur = cnt ^ (1 << i)
                ans += pre[cur]

            ans += pre[cnt]
            pre[cnt] += 1





        return ans
            




