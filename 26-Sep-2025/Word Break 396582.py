# Problem: Word Break - https://leetcode.com/problems/word-break/description/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wrds = set([wrd for wrd in wordDict])
        dp = [0] * (len(s)+1)
        dp[-1] = 1
        for i in range(len(s)):
            tmp = []
            if dp[i-1]:
                for j in range(i,len(s)):
                    tmp.append(s[j])
                    if "".join(tmp) in wrds:
                        dp[j] = 1

        return dp[-2] == 1

                        
