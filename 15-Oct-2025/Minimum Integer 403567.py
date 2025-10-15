# Problem: Minimum Integer - https://codeforces.com/problemset/problem/1101/A



from heapq import heappush, heappop
from collections import defaultdict, deque
from random import randint
from cmath import inf, sqrt
from math import ceil, gcd, isqrt, lcm
from sys import stdin

def ii(): return int(stdin.readline().strip())
def ll(): return list(map(int, stdin.readline().strip().split()))
def ss(): return stdin.readline().strip()
rand = randint(1000, 10000000)

def solve():
    l , r , d = ll()
    if d < l or d > r:
        return d
    
    return r+d - (r+d)%d


tt = ii()
res = []
for _ in range(tt):
    res.append(solve())
for ans in res:
    print(ans)