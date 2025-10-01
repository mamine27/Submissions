# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # n = len(arr)
        # @cache
        # def do(lft=0 , rt = 0):

        #     if lft == n or rt == n :
        #         return 0

        #     if arr[rt] - arr[lft] == difference:
        #         print(lft , rt)
        #         return max(do(rt , rt)+1 , do(lft , rt+1) , do(lft+1 , lft+1))
            
        #     return max(do(lft         , rt+1) , do(lft+1 , lft+1))

        # return do() + 1


        # for i in range(n-1,-1,-1):
        #     for j in range(n-1,i-1,-1):
        #         if arr[j] - arr[i] == difference:
        #             dp[i][j] = max(dp[j][j]+1 , dp[i][j+1] , dp[i+1][i+1])
        #         else:
        #             dp[i][j] = max( dp[i][j+1] , dp[i+1][i+1])

        # if difference == 0:
        #     return max(Counter(arr).values())
        dp = defaultdict(int)
        ans = 0
        for nm in arr:
            dp[nm] = max(dp[nm] ,dp[nm - difference] + 1 )
            ans = max(ans , dp[nm])

        return ans 
            