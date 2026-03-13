class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        mn = [inf] * (len(nums)+1)
        for i in range(len(nums)-1,-1,-1):
            mn[i] = min(mn[i+1] , nums[i])
    
        ans = 0
        for i in range(len(nums)-2,-1,-1):
            mn[i] = min(mn[i] , mn[i+1])
            if nums[i] > mn[i+1]:
                cn = ceil(nums[i] / mn[i+1])
                mn[i] = min(mn[i] ,nums[i]//cn)
                ans += ceil(nums[i] / mn[i+1])-1

        return ans  


