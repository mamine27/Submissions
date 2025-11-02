# Problem: k-Factorization - https://codeforces.com/problemset/problem/797/A

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
    n , k = ll()
    d = 2
    ft = []
    while n != 1:
        while n % d == 0:
            n //= d
            ft.append(d)
        d += 1

    if len(ft) < k:
        return [-1]
    
    while len(ft) > k:
        nm = ft.pop()
        ft[-1] *= nm

    return ft



print(*solve())

