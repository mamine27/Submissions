# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        mx = (n + 1)
        prms = [0] * (mx)
        prms[0] = 1
        if n >= 1:
            prms[1] = 1

        for i in range(2,n+1):
            if not prms[i]:
                for j in range(2*i,n+1,i):
                    prms[j] = 1

        
        cnt = 0

        for nm , st in enumerate(prms):
            if nm == n:
                return cnt
            if st == 0:
                cnt += 1
