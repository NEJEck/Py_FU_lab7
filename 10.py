a = [int(i) for i in input().split()]
minA = 1000
for dig in range(0, len(a)):
    if minA > a[dig] > 0:
        minA = a[dig]
print(minA)
