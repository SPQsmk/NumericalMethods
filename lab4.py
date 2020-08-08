import numpy as np
import math
from numpy.linalg import norm, inv
 
A = np.array([[-2, 3.01, 0.12, -0.11], [2.92, -0.17, 0.11, 0.22], [0.66, 0.52, 3.17, 2.11], [3.01, 0.42, 0.27, -0.15]])
AT = np.array([[-2, 2.92, 0.66, 3.01], [3.01, -0.17, 0.52, 0.42], [0.12, 0.11, 3.17, 0.27], [-0.11, 0.22, 2.11, -0.15]])

b = np.array([0.2, 0.1, 0, -0.1])

AN = AT @ A
bn = AT @ b
 
def fast_descent(A, b, EPS):
    x = np.diag(A)
    WWT = A @ A.T
    WT = A.T 
    it = 1
    r = 10000
    while norm(r) > EPS:
        it += 1
        r = A @ x - b
        WWTR = WWT @ r
        mu = (r @ WWTR) / (WWTR @ WWTR)
        x = x - (mu * WT) @ r
    return x, it
 
def conjugate_gradient(A, b, EPS):
    it = 1
    x = b
    r = b - A @ x
    rho1 = r @ r
    p = r
    q = A @ p
    if (p @ q == 0):
        return x
    else:
        alpha = rho1 / (p @ q)
    x = x + p * alpha
    r = r - q * alpha
    while(norm(r) > EPS):
        it += 1
        rho2, rho1 = rho1, r @ r
        p = r + p * (rho1 / rho2)
        q = A @ p
        alpha = rho1 / (p @ q)
        x = x + p * alpha
        r = r - q * alpha
    return x, it
 
print("Метод сопряженных градиентов")
for i in range(2,8):
    x, it = conjugate_gradient(AN, bn, 10**-i)
    print("eps = ", 10**-i, end="")
    print(", x = [", end="")
    for itx in x : print("%.7F " % itx, end ="")
    print("], iteration = ", it)
 
print("Метод наискорейшего спуска:")
for i in range(2,8):
    x, it = fast_descent(A, b, 10**-i)
    print("eps = ", 10**-i, end="")
    print(", x = [", end="")
    for itx in x : print("%.7F " % itx, end ="")
    print("], iteration = ", it)

def Goose(A, b):
    for i in range(4):
        for c in range(i + 1, 4):
            k = A[c][i] / A[i][i]
            b[c] -= k * b[i]    
            for j in range(4):
                A[c][j] -= k * A[i][j]

Goose(A, b)

x1 = b[3] / A[3][3]
x2 = (b[2] - A[2][3] * x1) / A[2][2]
x3 = (b[1] - A[1][3] * x1 - A[1][2] * x2) / A[1][1]
x4 = (b[0] - A[0][3] * x1 - A[0][2] * x2 - A[0][1] * x3) / A[0][0]

print("Метод Гаусса:")
print("x1 =", "%7F" % x4, "x2 =", "%7F" % x3, "x3 =", "%7F" % x2, "x4 =", "%7F" % x1)

e1 = 0.2 - A[0][3] * x1 - A[0][2] * x2 - A[0][1] * x3 - A[0][0] * x4
e2 = 0.1 - A[1][3] * x1 - A[1][2] * x2 - A[1][1] * x3 - A[1][0] * x4
e3 = 0 - A[2][3] * x1 - A[2][2] * x2 - A[2][1] * x3 - A[2][0] * x4
e4 = -0/1 - A[3][3] * x1 - A[3][2] * x2 - A[3][1] * x3 - A[3][0] * x4

print("Невязки в методе Гаусса:")
print("e1 =", "%7F" % e1, "e2 =", "%7F" % e2, "e3 =", "%7F" % e3, "e4 =", "%7F" % e4)
print()