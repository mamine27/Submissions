# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # n = len(nums)

        # ans = 1
        # def dfs(i , cur , co = 1):
        #     nonlocal ans
        #     co += 1
        #     for j in range(i+1,n):
        #         if nums[j] > cur:
        #             dfs(j,nums[j],co)

        #     ans = max (ans , co)
        # for i in range(n):
        #     dfs(i,nums[i],0)

        # return ans 










        n = len(nums)


        dp = [1] * n 
        ans = 1
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if nums[j] > nums[i] :
                    dp[i] = max(dp[i] , 1 + dp[j])

        

        print(dp)
        return max(dp)
