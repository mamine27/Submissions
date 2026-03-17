class Solution:
    def myPow(self, x: float, n: int) -> float:
        @cache
        def pw(nm , px):
            if px == -1:
                return 1 / x
            if px == 1:
                return x
            if px == 0:
                return 1
            

            return pw(nm , px // 2) * pw(nm , ceil(px/2))

        return pw(x , n)
