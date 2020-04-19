numbers = [3, 5, 1, 7, 9, 0, 9, -3, 10]
if len(numbers) < 3:
    print('Список должен состоять минимум из 3 чисел')
    exit(0)
nmax1 = numbers[0]
nmin1 = numbers[0]
for n in numbers:
    if n > nmax1:
        nmax1 = n
    if n < nmin1:
        nmin1 = n
numbers.remove(nmax1)
numbers.remove(nmin1)
nmax2 = numbers[0]
nmin2 = numbers[0]
for n in numbers:
    if n > nmax2:
        nmax2 = n
    if n < nmin2:
        nmin2 = n
numbers.remove(nmax2)
nmax3 = numbers[0]
for n in numbers:
    if n > nmax3:
        nmax3 = n
p1 = nmin1 * nmin2 * nmax1
p2 = nmax1 * nmax2 * nmax3
if p1 > p2:
    print(nmin1, nmin2, nmax1)
else:
    print(nmax1, nmax2, nmax3)
