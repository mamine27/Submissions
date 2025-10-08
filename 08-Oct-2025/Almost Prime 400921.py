# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A



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
    # nms = [0] * (n+1)
    prms = [0] * (3001)
    prms[1] = 1

    for i in range(2,n+1):
        if not prms[i]:
            for j in range(2*i,n+1,i):
                prms[j] = 1

    

    def do(nm):
        st = set()
        for i in range(1,isqrt(nm)+1):
            if nm % i == 0:
                fir = i
                sec = nm // i
                if not prms[fir]:
                    st.add(fir)
                if not prms[sec]:
                    st.add(sec)

        return len(st) == 2


    
    ans = 0
    for i in range(1,n+1):
        ans += int(do(i))

    return ans
print(solve())