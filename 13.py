a = [int(i) for i in input().split()]
b = []
for i in a:
    b.append(i)
b.reverse()
print(*b)
