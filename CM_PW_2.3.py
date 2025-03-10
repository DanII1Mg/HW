# 

def func(x):
    return x ** 2 - 5 * x + 6  

def g(x):
    return (5 * x - 6) / x 

def simple_iteration_m(x0, e):
    x1 = g(x0)
    while abs(x1 - x0) > e:
        x0, x1 = x1, g(x1)
    return x1

x0 = 4
e = 0.001

print(simple_iteration_m(x0, e))