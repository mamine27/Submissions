# Problem: Distribute Candies Among Children II - https://leetcode.com/problems/distribute-candies-among-children-ii/

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        
        ans = 0
        for i in range(min(n,limit)+1):
            ot = n-i
            sec = min(limit , ot)
            thr = ot - sec
            
            if max(thr,sec) <= limit:
                ans += max(0,abs(sec - thr)+1)

   

        return ans
