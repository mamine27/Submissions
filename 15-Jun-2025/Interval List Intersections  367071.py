# Problem: Interval List Intersections  - https://leetcode.com/problems/interval-list-intersections/description/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []

        for x , y in firstList:
            for x2 , y2 in secondList:
                l = max(x,x2)
                r = min(y,y2)
                if r < l:
                    continue

                ans.append([l,r])


        return ans