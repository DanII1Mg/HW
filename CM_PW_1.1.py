import numpy as np

def func(x):
    y = x**2 - 5*x +6
    return y
    
x0 = 2.5
x1 = 4
e = 10**-6
   
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
        
print(bisection_m(x0, x1, e))
    