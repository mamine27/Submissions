# Problem: The Two Routes - https://codeforces.com/problemset/problem/601/A



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
    mst = defaultdict(set)

    for i in range(1,n+1):
        for j in range(i+1,n+1):
            mst[i].add(j)
            mst[j].add(i)


    ot = defaultdict(set)

    for i in range(m):
        a , b = ll()
        mst[a].remove(b)
        mst[b].remove(a)
        ot[b].add(a)
        ot[a].add(b)


    def bfs(gr):
        st = 1
        qu = deque([1])
        vis = set([1])
        lvl = -1
        while qu:
            lvl += 1
            for _ in range(len(qu)):
                cr = qu.popleft()
                if cr == n:
                    return lvl if lvl != 0 else inf
                for ch in gr[cr]:
                    if ch not in vis:
                        vis.add(ch)
                        qu.append(ch)


        return inf
    
    ans = max(bfs(mst) , bfs(ot))
    return ans if ans != inf else -1

print(solve())