from math import exp
def f(x):
    return x * exp(-x)

integral = 0.0
x = 0
xmax = 50
dx = 0.1
while x < xmax:
    integral = integral + (dx * f(x))
    x = x + dx
print("Integral =", integral, "error =", abs(1- integral))
