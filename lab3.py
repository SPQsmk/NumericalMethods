import math
eps = 10**-5

def f1(x, y):
    return (x**2) * (y**2) - 3 * (x**3) - 6 * (y**3) + 8

def f2(x, y):
    return x**4 - 9 * y + 2

def fp11(x, y):
    return 2 * x * y * y - 9 * x * x

def fp12(x, y):
    return 2 * y * x * x - 18 * y * y

def fp21(x, y):
    return 4 * x**3

def fp22(x, y):
    return -9

def Newtone(x, y):
    iter = 0
    while True:
        iter+=1
        x1, y1 = x, y
        a11 = fp11(x1, y1)
        a12 = fp12(x1, y1)
        a21 = fp21(x1, y1)
        a22 = fp22(x1, y1)
        f11 = f1(x1, y1)
        f22 = f2(x1, y1)
        determ = a11 * a22 - a21 * a12
        x = x1 - (a22 * f11 - a12 * f22) / determ
        y = y1 - (-a21 * f11 + a11 * f22) / determ
        if (abs(f1(x, y) - f2(x, y)) < eps):
            return x, y, iter

print()
print("Частные производные находятся численно:")
x, y, it = Newtone(1.5, 1)
print("x1 =","%.6F"%x,", y1 =","%.6F"%y,". Количество итераций:",it)
x, y, it = Newtone(-2.5, 3)
print("x2 =","%.6F"%x,", y2 =","%.6F"%y,". Количество итераций:",it)

def count_f_x(f, x, y):
    h = 10**-2
    return (f(x + h, y) - f(x, y)) / h

def count_f_y(f, x, y):
    h = 10**-2
    return (f(x, y + h) - f(x, y)) / h
 
def Newtone_c(x, y):
    it = 0
    while True:
        it += 1
        x1, y1 = x, y
        a11 = count_f_x(f1, x, y)
        a12 = count_f_y(f1, x, y)
        a21 = count_f_x(f2, x, y)
        a22 = count_f_y(f2, x, y)
        f11 = f1(x1, y1)
        f22 = f2(x1, y1)
        determ = a11 * a22 - a21 * a12
        x = x1 - (a22 * f11 - a12 * f22) / determ
        y = y1 - (-a21 * f11 + a11 * f22) / determ
        if (abs(f1(x, y) - f2(x, y)) < eps):
            return x, y, it

print()
print("Частные производные находятся аналитически:")
x, y, it = Newtone_c(1.2, 1.5)
print("x1 =","%.6F"%x,", y1 =","%.6F"%y,". Количество итераций:",it)
x, y, it = Newtone_c(-4, 4)
print("x2 =","%.6F"%x,", y2 =","%.6F"%y,". Количество итераций:",it)
print()