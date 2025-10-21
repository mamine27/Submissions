# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/description/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:


        adj = [[] for i in range(n+1)]

        for u , v , w in times:
            adj[u].append([v,w])
            # adj[v].append([u,w])

        ans = [inf] * (n+1)
        # ans[k] = 0

        qu = [[0,k]]
        vis = set()
        while qu:
            cst , cur = heappop(qu)
            if ans[cur] != inf:
                continue
            ans[cur] = cst
            for ch , w in adj[cur]:
                if ans[ch] == inf:
                    heappush(qu , [cst + w , ch])


        vl = max(ans[1:])
        return vl if vl != inf else -1
