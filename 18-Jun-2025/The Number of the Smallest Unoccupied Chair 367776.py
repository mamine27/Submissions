# Problem: The Number of the Smallest Unoccupied Chair - https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/description/

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        cnt = 0

        qu = []
        n = len(times)

        inf = []

        for per , ot in enumerate(times):
            st , en = ot
            inf.append([st,1,per])
            inf.append([en,0 , per])


        inf.sort()
        mp = {}
        for time , ask , per in inf:
            if not ask:
                chair = mp[per]
                heappush(qu,chair)

            else:
                if qu:
                    cur = heappop(qu)
                    mp[per] = cur

                else:
                    mp[per] = cnt
                    cnt += 1


        
        return mp[targetFriend]


            