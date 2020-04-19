counter = 0
a = [int(i) for i in input().split()]
for i in range(1, len(a) - 1):
    if a[i] > a[i + 1] and a[i] > a[i - 1]:
        counter += 1
print(counter)
