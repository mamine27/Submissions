# Problem: Solving Questions With Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n+1)
        for i in range(n):
            pnt , jmp  = questions[i]
            nxt = i+jmp+1 if i+jmp+1 < n else n
            dp[i] = max(dp[i] , dp[i-1])
            dp[nxt] = max(dp[nxt] , dp[i] + pnt)


        return max(dp)
        