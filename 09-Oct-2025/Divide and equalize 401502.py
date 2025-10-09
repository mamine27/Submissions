# Problem: Divide and equalize - https://codeforces.com/problemset/problem/1881/D

import sys
import heapq
import math
def input():
    return sys.stdin.readline().strip()
from collections import defaultdict, Counter, deque
from random import randint
def intlist(): return list(map(int, (x for x in input().split())))
def strarr(): return list(int(x) for x in input())
def yn(val): print("YES" if val else "NO")

def solve():
    n = int(input())
    arr = intlist()

    cnt = defaultdict(int)
    def factors(num):
        d = 2
        while d * d <= num:
            while num % d == 0:
                cnt[d] += 1
                num //= d
            d += 1
    
        if num > 1:
           cnt[num] += 1

    for i in range(n):
       factors(arr[i])

    tmp = set()
    for ke in cnt:
       if cnt[ke] % n:
           print("NO")
           return 
    print("YES")

    return

t = lambda inp = 0: int(input()) if not inp else inp 
for _ in range(t()):
    solve()