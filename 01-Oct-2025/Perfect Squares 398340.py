# Problem: Perfect Squares - https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        nums = []

        sp = 1
        for i in range(1,n+1):
            if i * i > n:
                break
            nums.append(i*i)

        dp = [inf] * (n+1)
        dp[0] = 0
        for i in range(n+1):
            if dp[i] != inf:
                for nm in nums:
                    if i + nm <= n:
                        dp[i+nm] = min(dp[i] + 1 , dp[i+nm])

        return dp[-1]