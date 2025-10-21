# Problem: Find the City With the Smallest Number of Neighbors at a Threshold Distance - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], dt: int) -> int:
        

        dp = [ [inf ] * n for j in range(n)]

        for i in range(n):
            dp[i][i] = 0

        for u , v , w in edges:
            dp[u][v] = dp[v][u] = w


        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = min(dp[i][j] , dp[i][k] + dp[k][j])


        ans = inf
        cnt = inf
        for i in range(n):
            tmp = 0
            for j in range(n):
                if 1 <= dp[i][j] <= dt and j != i:
                    tmp += 1
            if cnt >= tmp:
                cnt = tmp
                ans = i
 

            
                    


        return ans


        
















        # n = len(edges)
        # dp = [[0,0] for i in range(n+1)]
        # dp2 = deepcopy(dp)

        # adj = [[] for i in range(n)]
        # dp[0][1] = 0
        # for u , v , w in edges:
        #     adj[u].append([v,w])
        #     adj[v].append([u,w])
        # # print(adj)
        # for i in range(len(edges)-1):
        #     print(dp2,"--------------->")
        #     for node in range(n):
        #         for ch , w in adj[node]:
    
        #             if dp[ch][1] + w > dt:
        #                 # print(ch,"chec")
        #                 continue
        #             if dp[ch][0] + 1 > dp2[node][0]:
        #                 # print("here")
        #                 dp2[node][0] = dp[ch][0] + 1
        #                 dp2[node][1] = dp[ch][1] + w
        #             elif dp[ch][0] + 1 == dp2[node][0]:
        #                 dp2[node][1] = min(dp2[node][1] , dp[ch][1] + w)

        #     dp = deepcopy(dp2)

        # ans = inf
        # print(dp2)
        # print(dp)
        # for i in dp:
        #     ans = min(ans , i[0])

        # return ans

        


