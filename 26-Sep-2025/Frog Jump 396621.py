# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
            

        # def help(nm):
        #     l = 0
        #     r = n-1
        #     while l <= r:
        #         md = (l+r) // 2
        #         if stones[md] < nm:
        #             l = md + 1
        #         else:
        #             r = md - 1
        #     return l if l < n and stones[l] == nm else n

        # def do(indx,lst):
        #     if indx >= len(stones)-1:
        #         return indx == len(stones)-1

        #     return do(help(stones[indx]+lst) , lst) or do(help(stones[indx]+lst+1) , lst+1) or (do(help(stones[indx]+lst-1),lst-1) if lst-1 > 0 else False)

        n = len(stones)
        help = defaultdict(lambda : n)

        for i , nm in enumerate(stones):
            help[nm] = i

        dp =[[0 for i in range(n+2)] for i in range(n-1)]
        dp += [[1 for i in range(n+2)]]
        dp += [[0 for i in range(n +2)]]
    
        for i in range(n-2,-1,-1):
            for j in range(i+1,-1,-1):
                dp[i][j] = dp[help[stones[i]+j]][j] + (dp[help[stones[i]+j+1]][j+1] if j + 1 < n+1 else 0) + (dp[help[stones[i]+j-1]][j-1] if j-1 > 0 else 0)
                



        return dp[0][0] > 0 and stones[1] - stones[0] == 1