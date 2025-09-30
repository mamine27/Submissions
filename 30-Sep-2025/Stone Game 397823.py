# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:


        n = len(piles)
        dp = [[0 for i in range(n+2)] for j in range(n+2)]
        for i in range(n):
            dp[i][i] = piles[i] if n % 2  else -piles[i]
        for d in range(1,n):
            for l in range(n-d):
                r = l + d
                dp[l][r] = (max(dp[l+1][r] + piles[l] , dp[l][r-1] + piles[r]) if d % 2 else min(dp[l+1][r] - piles[l] , dp[l][r-1] - piles[r]))


        return dp[0][n-1] > 0

        

            