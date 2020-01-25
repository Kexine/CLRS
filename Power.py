#python3
import random

def MyPow(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    if n == 2:
        return x * x
    if n % 2 == 0:
        return MyPow(MyPow(x, n / 2), 2)
    if n % 2 == 1:
        return MyPow(MyPow(x, n // 2), 2) * x

x = random.randint(4, 99)
n = random.randint(3, 40)
print(MyPow(x, n))
print(pow(x, n))