# Problem: Height Checker
(Easy) - https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(1 if fir != sec else 0 for fir , sec in zip(sorted(heights) , heights))