# Problem: Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        chk = [[-1 for i in range(27)] for j in range(len(s2)+1) ]
        for i in range(len(s2)-1,-1,-1):
            for j in range(27):
                if s2[i] == chr(ord('a')+j):
                    chk[i][j] = i
                else:
                     chk[i][j] = chk[i+1][j]

        dp = [[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]


        x = len(s1)
        y = len(s2)
        for i in range(x-1,-1,-1):
            for j in range(y-1,-1,-1):
                nxt = chk[j][ord(s1[i]) - ord('a')]
                ad = int(nxt > -1)
                lft =  nxt+1 if nxt != - 1 else len(s2)
                vl1 = ad + dp[i+1][lft]
                vl2 = dp[i+1][j]
                if vl1 > vl2:
                    dp[i][j] =  vl1 
                    # dp[i][j][1] = lft
                    # dp[i][j][2] = 1 
                else:
                    dp[i][j] =  vl2
        return dp[0][0]