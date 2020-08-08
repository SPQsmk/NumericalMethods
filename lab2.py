import math
eps = 10**-5
 
def f(x):
    return 0.25 * x - math.sin(x) - 0.25

def fp(x):
    return 0.25 - math.cos(x)

def iteration(a, b, eps):
    iter = 0
    x1 = (a + b) / 2
    c = -2 / (fp(a) + fp(b))
    while True:
        x0 = x1
        x1 = x0 + c * f(x0)
        iter += 1
        if abs(x0 - x1) < eps:
            return x1, iter
 
def dihotomiya(a, b, eps):
    iter = 0
    while abs(b - a) > eps:
        iter += 1
        x = 0.5 * (a + b)
        fx = f(x)
        fa = f(a)
        if (fx * fa > 0):
            a = x
        else:
            b = x
    if (abs(f(x)) <= eps):
        return x, iter

print()
print('Решение методом дихотомии:')
x, it = dihotomiya(-4, -2, eps)
print('x1 =', "%.6F" % x, ',количество итераций:', it)
x, it = dihotomiya(-2, 0, eps)
print('x2 =', "%.6F" % x, ',количество итераций:', it)
x, it = dihotomiya(2, 4, eps)
print('x3 =', "%.6F" % x, ',количество итераций:', it)

print()
print('Решение методом простых итераций:')
x, it = iteration(-3, -2, eps)
print('x1 =', "%.6F" % x, ',количество итераций:', it)
x, it = iteration(-1, 0, eps)
print('x2 =', "%.6F" % x, ',количество итераций:', it)
x, it = iteration(2, 3, eps)
print('x3 =', "%.6F" % x, ',количество итераций:', it)
print()