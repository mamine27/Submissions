# Problem: Minimum Path Sum - https://leetcode.com/problems/minimum-path-sum/description/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dp = [[0] * (m) for i in range(n)]

        dp[n-1][m-1] = grid[-1][-1]
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if i == n-1 and j == m-1:
                    continue
                dp[i][j] = grid[i][j] + min(dp[i+1][j] if i + 1 < n else inf , dp[i][j+1] if j + 1 < m else inf)

        return dp[0][0]