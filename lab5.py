import math
import numpy as np

a = 0
b = 1
n = 4
m = 4
eps = 0.5 * 10**-4

def f(x):
    return math.log(1 + x**2) / (1 + x**2)

def Trump(a, b, n):
    h = (b - a) / n
    arr = np.arange(a, b, h)
    res = 0
    k = 0
    for i in arr:
        k += 1
        res += f(i)
    return h * (res - 0.5 * f(a) + 0.5 * f(b))

def Homer(a, b, c):
    h = (b - a) / c
    arr = np.arange(a, b, h)
    res = 0
    k = 0
    for i in arr:
        if i == a:
            res += f(i)
        elif k%2 == 1:
            res += 4 * f(i)
        elif k%2 == 0:
            res += 2 * f(i)
        k += 1
    return h / 3 * (res + f(b))

int1 = Trump(a, b, n)
int2 = Trump(a, b, 2 * n)
while (math.fabs(int1 - int2) > eps):
    n *= 2
    int1 = int2
    int2 = Trump(a, b, 2 * n)

int3 = Homer(a, b, m)
int4 = Homer(a, b, 2 * m)
while (math.fabs(int1 - int2) > eps):
    m *= 2
    int3 = int4
    int4 = Homer(a, b, 2 * m)

print()
print("Метод трапеций: n =", n, ", интеграл равен: ", "%.6F"%int2)
print()
print("Формула Симпсона: m =", m, ", интеграл равен: ", "%.6F"%int4)
print()