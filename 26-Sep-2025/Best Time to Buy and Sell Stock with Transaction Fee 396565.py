# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        
        @cache
        def do(indx , state):
            if indx == len(prices):
                return 0

            if state:
                return max(prices[indx] + do(indx+1 , 1-state) , do(indx+1 , state))
            if not state:
                return max(-(prices[indx]+fee) + do(indx+1 , 1-state) , do(indx+1 , state))    

        return do(0,0)
        # fin = 0
        # mem = defaultdict(int)
        # def do(prv = 0 , cur = 0 , indx = 0 , ans = 0):
        #     if (prv , cur , indx , ans) in mem:
        #         return mem[(prv , cur , indx , ans)]
        #     nonlocal fin
        #     if indx == len(prices):
        #         return ans
        #     lft = ans
        #     lprv = prv
        #     lcur = int(not cur)
        #     if cur:
        #         lft += prices[indx] - (prv + fee)
        #     else:
        #         lprv = prices[indx]

        #     vl1 = do(lprv , lcur , indx+1 , lft)
        #     vl2 = do(prv , cur , indx+1 , ans)
        #     mem[(lprv , lcur , indx+1 , lft)] =  vl1
        #     mem[(prv , cur , indx+1 , ans)] = vl2
        #     return max(vl1,vl2)
        

        # return do()