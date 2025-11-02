# Problem: Selection of Personnel - https://codeforces.com/problemset/problem/630/F

from heapq import heappush, heappop
from collections import defaultdict, deque
from random import randint
from cmath import inf, sqrt
from math import ceil, comb, gcd, isqrt, lcm
from sys import stdin

def ii(): return int(stdin.readline().strip())
def ll(): return list(map(int, stdin.readline().strip().split()))
def ss(): return stdin.readline().strip()
rand = randint(1000, 10000000)

def solve():
    n = ii()
    ans =0 
    ans += comb(n,5)
    ans += comb(n,6)
    ans += comb(n,7)

    return ans

print(solve())

