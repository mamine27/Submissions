# Problem: Dreamoon and Stairs - https://codeforces.com/problemset/problem/476/A

from heapq import heappush, heappop
from collections import defaultdict, deque , Counter
from math import ceil
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
    a, b = ll()
    
    mx = ceil(a/2)
    res = ceil(mx/b) * b

    return res if a >= b else -1
    
    
 
 
 
tt = 1
# tt = ii()
res = []
for _ in range(tt):
    res.append(solve())
    
for i in res:
    print(i)
 
 