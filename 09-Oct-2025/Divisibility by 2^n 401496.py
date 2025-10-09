# Problem: Divisibility by 2^n - https://codeforces.com/contest/1744/problem/D



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
    cnt = 0

    def calc(nm):
        nonlocal cnt
        tmp = 0
        while nm % 2 == 0:
            nm //= 2
            cnt += 1
            tmp += 1

        return tmp

    for nm in arr:
        calc(nm)
    mst = n - cnt
    ans = 0
    # print(cnt)

    vals = []
    for i in range(1,n,2):
        vals.append(calc(i+1))

    vals.sort()

    for pnt in vals[::-1]:
        if mst < 1:
            break
        mst -= pnt
        ans += 1


    return ans if mst < 1 else -1
        


tt = ii()
res = []
for _ in range(tt):
    res.append(solve())
for ans in res:
    print(ans)