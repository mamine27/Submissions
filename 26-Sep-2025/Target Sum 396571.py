# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        

        mx = 1001
        dp = [0] * (mx)

        tot = sum(nums)
        tar = (tot + target)//2
        if (tot + target) % 2 == 1 or target > tot or target < -tot:
            return 0


        dp[0] = 1
        for vl in nums:
            for j in range(mx-1,vl-1,-1):
                if j - vl > -1:
                    dp[j] += dp[j-vl]

        


        return dp[tar]