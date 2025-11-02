# Problem: Make Sum Divisible by P - https://leetcode.com/problems/make-sum-divisible-by-p/

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)

  

        pre = defaultdict(int)
        pre[0] = -1
        tot = sum(nums)
        sm = 0
        ans = inf
        for i in range(n):
            rem = tot - sm
            if (p -(rem % p))%p in pre:
                ans = min(ans , (i -pre[(p -(rem % p))%p])-1)

            sm += nums[i]
            pre[sm%p] = i
            if sm%p == 0:
                ans = min(ans , n-(i+1))




        return ans if ans != inf else -1

      
