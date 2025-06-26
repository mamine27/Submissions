# Problem: Minimize XOR - https://leetcode.com/problems/minimize-xor/description/

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        
        fir = num1.bit_count()
        sec = num2.bit_count()

        if fir == sec:
            return num1

        if fir < sec:
            ans = num1
            lft = sec - fir
            for i in range(32):
                if not lft:
                    return ans
                if not ((ans >> i) & 1):
                    lft -= 1
                    ans |= (1 << i)


        else:
            ans = 0
            lft = sec
            for i in range(32,-1,-1):
                if not lft:
                    return ans
                if ((num1 >> i) & 1):
                    lft -= 1
                    ans |= (1 << i)

