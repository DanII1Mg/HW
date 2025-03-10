# Метод Ньютона-Бройдена (проверить со вторым уравнением)

import numpy as np

def func(x):
    y = x ** 2 - 5 * x + 6
    y2 = (e ** x / e ** x + 1) - 0,7
    return y
    
def d_func(x):
    y = 2*x - 5
    return y

def newton_m(x0, e, c):
    while True:
        if d_func(x0) == 0:
            print("d_func = 0")
            return None
        x1 = x0 - c * (func(x0) / d_func(x0))
        
        if abs(x1 - x0) < e:
            return x1
        x0 = x1
        print(x0)
        
x0 = 4
e = 10**-6 
c = 0.5

print(newton_m(x0, e, c))