# Метод секущих 

def func(x):
    y = x ** 2 - 5 * x + 6
    return y

def secant_m(x0, x1, e):
    while abs(x1 - x0) >= e:
        x2 = x1 - (func(x1) * (x1 - x0)) / (func(x1) - func(x0))
        x0, x1 = x1, x2
    return x1

x0 = 4
x1 = -4
e = 0.001

print(secant_m(x0, x1, e))