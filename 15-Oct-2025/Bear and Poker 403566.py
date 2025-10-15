# Problem: Bear and Poker - https://codeforces.com/problemset/problem/574/C



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
    n = ii()

    arr = ll()
    # lc = arr[0]
    # for nm in arr:
    #     lc = lcm(nm , lc)

    def ch(nm):

        while nm % 3 == 0:
            nm //= 3
        while nm % 2 == 0:
            nm //= 2
    
        return nm 
            
    st = set([ch(nm)^rand for nm in arr])
    return "Yes" if len(st) == 1 else "No"

# tt = ii()
res = []
for _ in range(1):
    res.append(solve())
for ans in res:
    print(ans)