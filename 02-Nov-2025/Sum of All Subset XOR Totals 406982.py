# Problem: Sum of All Subset XOR Totals - https://leetcode.com/problems/sum-of-all-subset-xor-totals/

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        mem = defaultdict(int)
        def do(indx = 0 , tot = 0):
            nonlocal ans
            if (indx , tot) in mem:
                return mem[(indx , tot)]
            if indx == len(nums):
                return tot
            
            fir = do(indx+1 , tot ^nums[indx])
            sec = do(indx+1 , tot)
            mem[(indx , tot)] = fir + sec

            return fir + sec
        
        return do()
                