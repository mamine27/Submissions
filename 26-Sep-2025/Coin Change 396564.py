# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [inf] * (10 ** 4 + 1)
        dp[0] = 0
        for i in coins:
            if i < 10** 4 + 1:
                dp[i] = 1

        coins.sort()
        for i in range(amount+1):
            mn = inf
            for j in coins:
                if i - j > 0:
                    mn = min(dp[i-j] , mn)

            dp[i] = min(dp[i] ,(mn + (1 if mn != inf else 0)))

        return dp[amount] if dp[amount] != inf else -1

