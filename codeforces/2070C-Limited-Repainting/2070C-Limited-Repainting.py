from heapq import heappush, heappop
from collections import defaultdict, deque , Counter
from random import randint    
from cmath import inf

rand = randint(1000,10000000)    
def ii():
    return int(input())

def ll():
    return list(map(int, input().split()))
 
def ss():
    return input()
 
#^^^^^^^^^^^^^^^^^^^^^^^^^^^
def solve():
    n , m = ll()
    s = ss()
    arr = ll()
    nw = [0] + sorted(arr)

    def chk(mx):
        cnt = 0
        bl = 0
        for i in range(n):
            if s[i] == 'R' and arr[i] > mx and bl:
                cnt += 1
                bl = 0

            if s[i] == 'B' and arr[i] > mx:
                bl = 1

        if bl:
            cnt += 1

        return cnt <= m
    
    l = 0
    r = len(nw)-1
    
    while l <= r:
        md = (l+r) // 2
        if chk(nw[md]):
            r = md - 1
        else:
            l = md + 1


    return nw[l]
                  


    
    
 
 
 
tt = 1
tt = ii()
res = []
for _ in range(tt):
    res.append(solve())
    
for i in res:
    print(i)