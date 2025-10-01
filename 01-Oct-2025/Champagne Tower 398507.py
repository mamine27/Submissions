# Problem: Champagne Tower - https://leetcode.com/problems/champagne-tower/

class Solution:
    def champagneTower(self, poured: int, qr: int, ql: int) -> float:

        mp = defaultdict(float)
        mp[(0,0)] = poured
        ans = 0

        n = qr+3
        dp = [[0 for j in range(i+1)] for i in range(n) ]
        dp[0][0] = poured
        for i in range(1,n):
            dp[i][0] = max(0,(dp[i-1][0] - 1)) / 2
            for j in range(1,i+1):
                dp[i][j] += (max(0,(dp[i-1][j]-1))/2 if j < i else 0) + max(0,(dp[i-1][j-1]-1))/2


        return min(1,dp[qr][ql])
            

            