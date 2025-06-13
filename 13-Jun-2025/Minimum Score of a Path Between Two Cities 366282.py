# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        class UnionFind:
            def __init__(self):
                self.size = {}
                self.root = {}

            def find(self, x):
                if x not in self.root:
                    self.root[x] = x
                    self.size[x] = 1
                    return x

                while x != self.root[x]:
                    x = self.root[self.root[x]]

                return x

            def union(self, x, y):
                repx = self.find(x)
                repy = self.find(y)
                if repx == repy:
                    return

                szx = self.size[repx]
                szy = self.size[repy]

                if szx > szy:
                    self.root[repy] = self.root[repx]
                    self.size[repx] += self.size[repy]
                
                else:
                    self.root[repx] = self.root[repy]
                    self.size[repy] += self.size[repx]

        uf = UnionFind()
        roads.sort(key = lambda x : x[2])
        for u , v , w in roads:
            uf.union(u,v)

        tar = inf

        for u , v , w in roads:
            if uf.find(u) == uf.find(1):
                tar = min(tar , w)

        return tar


            
        # dist = [-1] * n
        # adj = defaultdict(list)
        # for u , v , w in roads:
        #     u -= 1
        #     v -= 1
        #     adj[u].append([v,w])
        #     adj[v].append([u,w])

        # qu = deque([(0,0)])

        # while qu:
        #     cost ,cur = qu.popleft()
        #     if dist[cur] != -1:
        #         continue
        #     dist[cur] = cost
        #     for ch ,cst in adj[cur]:
        #         qu.append((cost + cst , ch))

        # print(dist)
        # return dist[-1]


