#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        a.sort()
        b.sort()
        i = 0 
        j = 0 
        while i < len(a):
            if a[i] == b[j]:
                j += 1
                if j == len(b):
                    return True
            i += 1
        return False