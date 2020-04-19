stroka = str(input())
b = stroka.split()
a = list(map(int, b))
mv = a[0]
mi = 0
for i, v in enumerate(a):
    if v >= mv:
        mi = i
        mv = v
print(mv, mi)
