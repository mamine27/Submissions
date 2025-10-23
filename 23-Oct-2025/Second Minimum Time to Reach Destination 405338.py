# Problem: Second Minimum Time to Reach Destination - https://leetcode.com/problems/second-minimum-time-to-reach-destination/

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        
        adj = [[] for i in range(n+1)]

        for u , v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # vis = [0] * (n+1)

        # def dfs(node = 1):
        #     if node == n:
        #         return [0]
        #     hp = []
        #     for ch in adj[node]:
        #         if not vis[ch]:
        #             vis[ch] = 1
        #             ot = dfs(ch)

        #             for vl in ot:
        #                 cr = ceil(vl/change)
        #                 if cr % 2:
        #                     vl = ceil(vl/change)
        #                 heappush(hp , vl+time)
        #                 if len(hp) > 2:
        #                     heappop(hp)

        #             vis[ch] = 0

        #     return hp

        # print(dfs())

        
               

        vis = defaultdict(int)

        heap = [[0,1]]

        ans = [0] * (n+1)
        mp = defaultdict(set)
        vis[1] += 1
        while heap:
            # print(heap,"here")
            cst , cur = heappop(heap)

            cr = ceil(cst // change)+1
            ans[cur]= cst
            if cr % 2 == 0:
                cst = cr * change


            for ch in adj[cur]:
                if vis[ch]< 2 or len(mp[ch])< 2:
                    mp[ch].add(cst + time)

                    heappush(heap , [cst + time , ch])
                    vis[ch] += 1
        # print(mp[n])

        return ans[n]