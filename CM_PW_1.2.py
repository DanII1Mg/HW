import numpy as np

def func(x):
    y = x**2 - 5*x +6
    return y
    
def d_func(x):
    y = 2*x - 5
    return y
   
def bisection_m(x0, x1, e):     
    if func(x0) * func(x1) >= 0:
        print("Функция не меняет знак")
    else:
        while abs(x1 - x0) > e:
            x2 = (x0 + x1) / 2
            if func(x2) == 0:
                break
            elif func(x0) * func(x2) < 0:
                x1 = x2 
            else:
                x0 = x2

    return(x2)

def newton_m(x0, e):
    while True:
        if d_func(x0) == 0:
            print("d_func = 0")
            return None
        x1 = x0 - func(x0) / d_func(x0)
        
        if abs(x1 - x0) < e:
            return x1
        x0 = x1
        
    
x0 = 2.5
x1 = 4  
e = 10**-6 
method_1 = bisection_m(x0, x1, e)
print(newton_m(method_1, e))