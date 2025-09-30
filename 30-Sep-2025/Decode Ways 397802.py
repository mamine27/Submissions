# Problem: Decode Ways - https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        for i in range(1,n):
            if s[i] == "0" and (int (s[i-1]) > 2 or int(s[i-1]) == 0):
                return 0

        if s[0] == "0":
            return 0

        dp = [0] * (101)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,100):
            dp[i] = dp[i-1] + dp[i-2]

        cnt = []
        used = set()
        for i in range(n):
            if i not in used:
                tmp = 0
                fg = 0
                for j in range(i,n):
                    used.add(j)
                    if s[j] != "1" and s[j] != "2":
                        tmp += 1
                        if s[j] == "0":
                            tmp -= 2
                        elif int(s[j]) > 6 and j-1 >= 0 and s[j-1] != "1":
                            tmp -= 1

                        tmp = max(0 , tmp)

                        break

                    tmp += 1
                cnt.append([tmp , fg])

        ans = 1 
        for nm , cs in cnt:
            ans *= max(1,dp[nm] - cs)

        # print(cnt)
        return ans 
        # print(dp)
        # return 0
