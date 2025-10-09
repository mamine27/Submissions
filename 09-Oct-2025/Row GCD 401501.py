# Problem: Row GCD - https://codeforces.com/problemset/problem/1458/a

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
    n , m = ll()
    arr1 = ll()
    arr2 = ll()

    # cnt = defaultdict(int)
    # def do(num):
    #     d = 2
    #     while d * d <= nm:
    #         while num % d == 0:
    #             num //= d
    #             cnt[d] += 1
            
    #         d += 1

    # def do2(num):
    #     d = 2
    #     while d * d <= nm:
    #         while num % d == 0:
    #             num //= d
    #             cnt[d] += 1
            
    #         d += 1
    mx = max(arr1)
    gd = mx - arr1[0]
    for nm in arr1:
        gd = gcd(gd,mx - nm)


    ans = [0] * (m)
    mn = min(arr1)
    for i in range(m):
        nm = mn + arr2[i]
        ans[i] =gcd(nm,gd)

    return ans




print(*solve())