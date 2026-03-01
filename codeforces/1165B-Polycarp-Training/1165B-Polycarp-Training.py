n = int(input())
a = sorted(list(map(int,input().split())))
i = 0
day = 1
done = False
while i < len(a) and not done:
    if day <= a[i]:
        day += 1
        i += 1
    else:
        i += 1
        if i >= len(a):
            done = True
print(day -1)