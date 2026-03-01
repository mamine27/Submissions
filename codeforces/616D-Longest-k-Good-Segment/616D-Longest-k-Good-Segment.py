from collections import Counter
from random import randint


def iI():
    return int(input())
 
def iT():
    return list(map(int, input().split()))
 
def iL():
    return list(map(int, input().split()))
 
def iS():
    return input()
 
 
def solve():
    n , k = iL()
    arr = iL()

    rand = randint(1000, 10000000)
    cnt = Counter()

    



    l = 0
    mx = 0
    ans = [0,0]
    for i in range(n):
        cnt[arr[i]] += 1
        while len(cnt.keys()) > k:
            cnt[arr[l]] -= 1
            if not cnt[arr[l]]:
                del cnt[arr[l]]
            l += 1

        if mx < i - l + 1:
            mx = i - l + 1
            ans[0] = l+1
            ans[1] = i + 1



    return ans


        


 
 
 
tt = 1
# tt = iI()
res = []
for _ in range(tt):
    res.append(solve())
 
for i in res:
    print(*i)