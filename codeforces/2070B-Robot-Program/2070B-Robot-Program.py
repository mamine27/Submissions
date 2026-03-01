# from heapq import heappush, heappop
# from collections import defaultdict, deque , Counter
# from random import randint    
# from cmath import inf

# rand = randint(1000,10000000)
# def bps(matrix):
#     rows = len(matrix)
#     cols = len(matrix[0]) if rows > 0 else 0

#     prefix = [[0] * (cols + 1) for _ in range(rows + 1)]


#     for i in range(1, rows + 1):
#         for j in range(1, cols + 1):
#             prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + matrix[i - 1][j - 1]

#     return prefix
    
# def iI():
#     return int(input())

# def iL():
#     return list(map(int, input().split()))
 
# def iS():
#     return input()
 
# #^^^^^^^^^^^^^^^^^^^^^^^^^^^
# def solve():
#     n , x , k = iL()
#     s = iS()

#     cnt = x
#     stp = 0
#     for i in s:

#         if cnt == 0:
#             break

#         if i == 'L':
#             cnt -=1
#         else:
#             cnt += 1

#         stp += 1

#     if k < stp:
#         return 0
    
   

#     md = 0
#     st = 0
#     a = 0
#     for i in s:
#         st += 1
#         if i == 'L':
#             md += 1
#         else:
#             md -= 1
        
#         if md == 0:
#             a = st
#             break


#     print(stp ,a)
#     ans = k // (stp+a)

#     return ans + 1

    
    

    
 
 
 
# tt = 1
# tt = iI()
# res = []
# for _ in range(tt):
#     res.append(solve())
    
# for i in res:
#     print(i)

from collections import defaultdict, Counter
from random import randint
def intlist(): return list(map(int, (x for x in input().split())))
def strarr(): return list(int(x) for x in input())
for _ in range(int(input())):
    n, p, s = intlist()
    moves = input()
    c = 0
    val = {"L" : -1,
           "R" : 1 }
    
    tmp = p
    for i in range(n):
        if tmp == 0:
            break
        tmp += val[moves[i]]
        c += 1
    if (tmp != 0) or (s < c):
        print(0)
        continue

    c2 = 0
    ini = 0
    for i in range(n):
        if i >=1 and ini == 0:
            break
        ini += val[moves[i]]
        c2 += 1
    if ini != 0:
        print(1)
        continue
    # print(f"---> {c2} {c}")
    print(1 + ((s-c) // c2))