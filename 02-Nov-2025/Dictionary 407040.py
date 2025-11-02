# Problem: Dictionary - https://codeforces.com/problemset/problem/1674/B

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
    s = ss()
    ans = 0
    ans += (ord(s[0]) - (ord('a'))) * 26
    ask = s[0] < s[1]
    ans += (ord(s[1]) - (ord('a'))+1) - int(ask) - ((ord(s[0]) - (ord('a'))))
    return ans

tt = ii()
res = []
for _ in range(tt):
    res.append(solve())
for ans in res:
    print(ans)

