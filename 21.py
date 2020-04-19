a = [int(i) for i in input().split()]
max1 = a.index(max(a))
min1 = a.index(min(a))
if len(a) > 0:
    a[max1], a[min1] = a[min1], a[max1]
print(' '.join([str(i) for i in a]))
