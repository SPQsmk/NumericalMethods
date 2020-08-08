import math
a = 0.5; n = 0
eps = 10**-10
x = 0
y = math.log(((0.5 * math.pi * a)**-1) * math.tan(0.5 * a * math.pi))
while math.fabs(x - y) > eps:
    n += 1
    m = -n
    if (n % 2 == 1):
        x = x - math.log(1 - (a / n)**2)
    if (n % 2 == 0):
        x = x + math.log(1 - (a / n)**2)   

print()
print("Левая часть:", "%.11F" % x)
print("Правая часть:", "%.11F" % y)
print("n =", n)
print()