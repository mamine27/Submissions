# Problem: Find the Power of K-Size Subarrays II - https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        l = r = 0
        n = len(nums)
        nums.append(inf)
        ans = [0] * ((n-k)+1)
        for i in range(n):
            if l > n-k:
                break
            if nums[i] != nums[i+1]-1:
                if (i - l) + 1 == k:
                        ans[l] = nums[i]
                        l += 1
                for j in range(l,i+1):
                    if j > n-k:
                        break
                    ans[j] = -1
                l = i+1
            else:
                if (i - l) + 1 == k:
                    ans[l] = nums[i]
                    l += 1
    

        return ans
                

