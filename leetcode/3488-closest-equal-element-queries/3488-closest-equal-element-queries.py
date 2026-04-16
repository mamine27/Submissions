class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        ans = [inf] *(len(nums))

        mp = defaultdict(list)
        n = len(nums)
        for i , nm in enumerate(nums):
            if mp[nm]:
                if ans[mp[nm][-1]] > (i -mp[nm][-1]):
                    ans[mp[nm][-1]] = (i -mp[nm][-1])
                # if ans[mp[nm][-1]] > (mp[nm][0]) + (n - i):
                #     ans[mp[nm][-1]] = (mp[nm][0]) + (n - i)
                ans[i] = min((mp[nm][0]) + (n - i) , (i - mp[nm][-1]))
                if ans[mp[nm][0]] > (mp[nm][0]) + (n - i):
                    ans[mp[nm][0]] = (mp[nm][0]) + (n - i)

            mp[nm].append(i)

        return [(ans[i] if ans[i] != inf else -1) for i in queries]