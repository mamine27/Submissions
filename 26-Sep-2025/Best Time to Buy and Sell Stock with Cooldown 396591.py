# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mem = defaultdict(int)
        # def do(indx = 0 , state = 0):
        #     if len(prices) == indx:
        #         return 0

        #     if state == 0:
        #         return max(do(indx+1 , 1) - prices[indx] , do(indx+1,0))
        #     if state == 1:
        #         return max(do(indx+1 , 2) + prices[indx] , do(indx+1,1))
        #     if state == 2:
        #         return do(indx+1 , 0)
        n = len(prices)
        dp = [[0,0,0] for i in range(n+1)]
        for i in range(n-1,-1,-1):
            dp[i][0] = max(dp[i+1][1] - prices[i] , dp[i+1][0])
            dp[i][1] = max(dp[i+1][2] + prices[i] , dp[i+1][1])
            dp[i][2] = dp[i+1][0]

        return dp[0][0]