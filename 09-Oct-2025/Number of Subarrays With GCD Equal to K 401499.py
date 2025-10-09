# Problem: Number of Subarrays With GCD Equal to K - https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/description/

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            tmpg = nums[i]
            
            for j in range(i,n):
                if tmpg < k :
                    break
                tmpg = gcd(tmpg,nums[j])

                if tmpg == k:
                    ans += 1


        return ans
