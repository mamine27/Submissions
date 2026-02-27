t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    res=-1
    
    if "aa" in s:
        res=2
    elif "aba" in s or "aca" in s:
        res=3
    elif "abca" in s or "acba" in s:
        res=4
    elif "abbacca" in s or "accabba" in s:
        res=7
    print(res)