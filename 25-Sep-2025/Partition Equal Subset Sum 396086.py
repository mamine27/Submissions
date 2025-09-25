# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        dp = [0] * (sum(nums) // 2 + 1)
        dp[0] = 1

        for nm in nums:
            for j in range(len(dp)-1,nm-1,-1):
                dp[j] += dp[j-nm]
        
        return dp[sum(nums) // 2] > 0
