# Problem: Number of Parallelograms - https://codeforces.com/contest/660/problem/D



# from heapq import heappush, heappop
from collections import defaultdict
# import math
# from random import randint
# from cmath import inf, sqrt
from math import ceil, comb, gcd, isqrt, lcm, perm
from sys import stdin

def ii(): return int(stdin.readline().strip())
def ll(): return list(map(int, stdin.readline().strip().split()))
def ss(): return stdin.readline().strip()
# rand = randint(1000, 10000000)

def solve():
    n = ii()
    pnts = [ll() for i in range(n)]
    ans = 0
    cntx = defaultdict(int)
    # for i in range(n):
    #     x1 , y1 = pnts[i]
    #     for j in range(i+1,n):
    #         x2 , y2 = pnts[j]
    #         dis1 = x2 - x1
    #         dis2 = y2 - y1
    #         tmp = abs(dis1)** 2  + abs(dis2) ** 2 
    #         if not dis1:
    #             key = inf , tmp
    #             ans += cntx[key] 
    #             cntx[key] += 1
    #             continue
       

    #         gd = gcd(dis2 , dis1)
    #         slope = dis2//gd , dis1//gd , tmp
    #         ans += cntx[slope]
    #         cntx[slope] += 1

    ans = 0
    for i in range(n):
        x1 , y1 = pnts[i]
        for j in range(i+1 , n):
            x2 , y2 = pnts[j]
            cntx[((x1+x2) ,(y1+y2))] += 1

    
    for vls in cntx:
        ans += comb(cntx[vls] , 2)




    return ans


    

# tt = ii()
res = []

for _ in range(1):
    res.append(solve())
for ans in res:
    print(ans)