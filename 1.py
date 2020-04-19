stroka = str(input())
b = stroka.split()
a = list(map(int, b))
for dig in (a[::2]):
    print(dig, '', end='')
