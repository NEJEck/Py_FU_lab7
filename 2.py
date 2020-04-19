stroka = str(input())
b = stroka.split()
a = list(map(int, b))
for dig in a:
    if dig % 2 == 0:
        print(dig, '', end='')
