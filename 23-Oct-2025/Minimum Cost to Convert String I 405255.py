# Problem: Minimum Cost to Convert String I - https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        dp = [[inf for i in range(26)] for i in range(26)]

        for i in range(26):
            dp[i][i] = 0 

        n = len(original)
        for i in range(n):
            u , v , w = original[i] , changed[i] , cost[i]
            ou = ord(u) - ord('a')
            ov = ord(v) - ord('a')
            dp[ou][ov] = min(w , dp[ou][ov])


        for k in range(26):
            for i in range(26):
                for j in range(26):
                    dp[i][j] = min(dp[i][j] ,dp[i][k] + dp[k][j])



        ans = 0

        for x , y in zip(source,target):
            ox , oy = ord(x)- ord('a') , ord(y)- ord('a')
            vl = dp[ox][oy]
            if vl == inf:
                return -1

            ans += vl


        return ans
