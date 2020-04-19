a = [int(i) for i in input().split()]
max1 = 0
iv = 0
jv = 0
for i in range(0, 3):
    for j in range(i+1, len(a)):
        if a[i] * a[j] > max1:
            max1 = a[i] * a[j]
            iv = a[i]
            jv = a[j]
print(iv, jv)
