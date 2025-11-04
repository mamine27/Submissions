# Problem: Number of Laser Beams in a Bank - https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        sm = 0
        n = len(bank)
        m = len(bank[0])
        ans = 0
        for i in range(n):
            sm2 = 0 
            for j in range(m):
                sm2 += bank[i][j] == "1"
                if bank[i][j] == "1":
                    ans += sm
            if sm2:
                sm = sm2

        return ans
