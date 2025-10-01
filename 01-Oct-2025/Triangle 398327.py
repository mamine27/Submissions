# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        n = len(triangle)
        dp = [[0 for j in range(i+1)] for i in range(n) ]
        dp[0][0] = triangle[0][0]
        for i in range(1,n):
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            for j in range(1,i+1):
                dp[i][j] = min(dp[i-1][j] if j < i else inf , dp[i-1][j-1]) + triangle[i][j]


        return min(dp[-1])