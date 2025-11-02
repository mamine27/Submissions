# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        eve = (n+1)//2
        od = n//2
        fir = sec = 1
        if eve:
            fir = pow(5 , eve ,(10 ** 9 + 7))
        if od:
            sec = pow(4 , od , 10 ** 9 + 7)

        return (fir * sec)  % (10 ** 9 + 7)