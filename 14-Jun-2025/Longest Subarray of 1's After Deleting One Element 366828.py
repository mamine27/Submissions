# Problem: Longest Subarray of 1's After Deleting One Element - https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        l = 0
        cnt = 0
        for i in range(len(nums)):
            cnt += nums[i] == 0
            while l < i and cnt >= 2:
                cnt -= nums[l] == 0
                l += 1

            ans = max(ans , (i - l))


        return ans