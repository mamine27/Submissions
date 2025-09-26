# Problem: 01 Knapsack - https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

class Solution:
    def knapsack(self, W, val, wt):
        # code here
        mx = W+1
        dp = [-1] * (mx)
        dp[0] = 0
        
        for i in range(len(val)):
            for j in range(mx-1,wt[i]-1,-1):
                dp[j] = max(dp[j],dp[j-wt[i]] + val[i]) 
                
        return max(dp)
        
