# Problem: E - Knapsack 2 - https://atcoder.jp/contests/dp/tasks/dp_e

from heapq import heappush, heappop
from collections import defaultdict, deque
from random import randint    
from cmath import inf
from math import ceil
rand = randint(1000,10000000)
from sys import stdin
 
def ii(): return int(stdin.readline().strip())
def ll(): return list(map(int, stdin.readline().strip().split()))
def ss() : return stdin.readline().strip()

def Counter(arr , asked = None):
    cnt = defaultdict(int)   
    for i in arr:
        cnt[i^rand] += 1
    if asked:
        return cnt[asked ^ rand]
    
    return cnt

def sieve():
    mx = 10 ** 6 + 2
    prm = [0]*(mx) 
    for i in range(2,mx):
        if prm[i]:
            continue
        for j in range(i,mx,i):
            prm[j] += 1


from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

class UnionFind:
    def __init__(self):
        self.size = {}
        self.root = {}

    def find(self, x):
        if x not in self.root:
            self.root[x] = x
            self.size[x] = 1
            return x

        while x != self.root[x]:
            x = self.root[self.root[x]]

        return x

    def union(self, x, y):
        repx = self.find(x)
        repy = self.find(y)
        if repx == repy:
            return

        szx = self.size[repx]
        szy = self.size[repy]

        if szx > szy:
            self.root[repy] = self.root[repx]
            self.size[repx] += self.size[repy]
           
        else:
            self.root[repx] = self.root[repy]
            self.size[repy] += self.size[repx]
    
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^
# nnnnnnnnnnnnnnnnnnnnnnnnnn
def solve():

    n , w = ll()

    vals = [ll() for i in range(n)]
    dp = [inf] * (10 ** 5 + 1)
    dp[0] = 0
    for tr , vls in vals:
        for j in range(10**5 , vls - 1 , -1):
            dp[j] = min(dp[j] , dp[j-vls] + tr)


    ans = 0
    for i in range(10 ** 5+1):
        if dp[i] <= w:
            ans = max(ans , i)

    # print(dp[:100])
    return ans

 
tt = 1
# tt = ii()
res = []
for _ in range(tt):
    res.append(solve())
    
for i in res:
    print(i)
 

