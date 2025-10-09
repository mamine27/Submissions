# Problem: Complicated GCD - https://codeforces.com/contest/664/problem/A

 
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
    l , r = ll()
    return 1 if l != r else l

print(solve())