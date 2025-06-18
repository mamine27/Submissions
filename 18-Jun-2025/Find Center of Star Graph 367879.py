# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        cnt = Counter()

        for x , y in edges:
            cnt[x] += 1
            cnt[y] += 1

        mx = 0
        ans = 0

        for i in cnt:
            if cnt[i] > mx:
                mx = cnt[i]
                ans = i

        return ans