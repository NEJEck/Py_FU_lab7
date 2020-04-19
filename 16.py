N = int(input())
a = [int(s) for s in input().split()]
x = int(input())
print(min(a, key=lambda n: abs(n-x)))
