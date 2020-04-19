a = [int(i) for i in input().split()]
for i in range(1):
    a.insert(0, a.pop())
print(*a)
