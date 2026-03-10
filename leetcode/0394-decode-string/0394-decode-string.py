class Solution:
    def decodeString(self, arr: str) -> str:
        n = len(arr)
        stk = [[0,""]]
        i = 0
        nms = "0123456789"
        while i < n:

            if arr[i] == "]":
                tm , st = stk.pop()
                tba = tm * st
                stk[-1][1] += tba
            if arr[i] == "[":
                tb = ""
                j = i-1

                while arr[j] in nms:
                    tb += arr[j]
                    j -= 1
                
                stk.append([int(tb[::-1]) , ""])
            elif arr[i] != "]" and arr[i] not in nms:
                stk[-1][1] += arr[i]

            i += 1
        return stk[0][1]



        return ans