# Problem: Number of Ways to Reach a Position After Exactly k Steps - https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        

        dis = abs(startPos - endPos)
        
        if (dis % 2 )!=( k % 2) or dis > k:
            return 0

        ops = abs(dis - k)
        main = (dis) + ceil(ops/2)
        ops //= 2
        md = 10 ** 9 + 7
    
        return (perm(k) * pow((perm(ops) * perm(main)) % md, md - 2, md)) % md



        # return dp()

