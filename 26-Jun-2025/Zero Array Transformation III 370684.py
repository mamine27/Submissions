# Problem: Zero Array Transformation III - https://leetcode.com/problems/zero-array-transformation-iii/description/

class Solution:
    def maxRemoval(self, nums: List[int], qu: List[List[int]]) -> int:
        n = len(qu)
        nw = sorted(qu , key = lambda x : (x[0],-x[1]))

        hp = []

        mark = [0] * (len(nums)+1)
        und = 0
        l = 0
        ans = 0
        j = 0
        for i ,nm  in enumerate(nums):
            und += mark[i]
            mark[i] = 0
            while j < n and nw[j][0] <= i <= nw[j][1]:
                heappush(hp,[-nw[j][1] , nw[j][0]])
                j += 1

            if hp and -hp[0][0] < i:
                hp = []

            now = max(nm - und , 0)
            if not now:
                continue
            while now and hp:
                if hp and -hp[0][0] < i:
                    hp = []
                    break
                ans += 1 
                r , _ = heappop(hp)
                r *= -1
                mark[i] += 1
                mark[r+1] -= 1
                now -= 1


            if now > 0:
                return -1
                
            und += mark[i]

        return len(qu) - ans






        


            

