# Problem: Bicoloring - https://www.eolymp.com/en/contests/30008/problems/349926

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
    n = ii()
    if n == 0:
        return -1
    adj = defaultdict(list)
    for i in range(ii()):
        a , b = ll()
        adj[a].append(b)
        adj[b].append(a)
        sm =a

    col = [-1] * (n+1)
    qu = deque([a])
    lvl = 0
    while qu:
        lvl += 1
        for _ in range(len(qu)):
            cur = qu.popleft()
            col[cur] = lvl % 2
            for ch in adj[cur]:
                if col[ch] == -1:
                    qu.append(ch)

                if col[ch] == lvl % 2:
                    return "NOT BICOLOURABLE."
                
    
    return "BICOLOURABLE."
                
while True:
    val = solve()
    if val == -1:
        break
    print(val)



 


