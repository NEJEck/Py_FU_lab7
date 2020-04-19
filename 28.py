a = [int(s) for s in input().split()]
b = [i for i in a if i] + [0] * a.count(0)
print(*b)
