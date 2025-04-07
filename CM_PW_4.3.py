import numpy as np

def gauss_m2(A, b):
    n = len(A)
    Ab = np.hstack([A.astype(float), b.reshape(-1, 1).astype(float)])
    
    # 1) Правило прямоугольника
    for i in range(n):
        for k in range(i + 1, n):
            el = Ab[k, i] / Ab[i, i]
            Ab[k, i+1:] -= el * Ab[i, i+1:]
            Ab[k, i] = 0
    
    # 2) Обратный ход
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i+1:n], x[i+1:n])) / Ab[i, i]
    
    return x

A = np.array([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]])
b = np.array([8, -11, -3])
print(gauss_m2(A, b))  # [ 2.  3. -1.]