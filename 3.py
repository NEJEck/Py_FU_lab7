stroka = str(input())
sum1 = 0
b = stroka.split()
a = list(map(int, b))
for dig in a:
    if dig > 0:
        sum1 += 1
print(sum1)
