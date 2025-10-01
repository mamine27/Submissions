# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target+1)
        dp[0] = 1

        for i in range(target+1):
            for nm in nums:
                if i + nm <= target:
                    dp[i+nm] += dp[i]

        return dp[target]