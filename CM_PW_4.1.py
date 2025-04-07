import numpy as np

def gauss_m(A, b):
    n = len(A)
    Ab = np.hstack([A.astype(float), b.astype(float).reshape(-1, 1)])
    
    # 1) Прямой ход
    for i in range(n):
        Ab[i] = Ab[i] / Ab[i, i]
        
        for k in range(i + 1, n):
            Ab[k] -= Ab[k, i] * Ab[i]
    
    # 2) Обратный ход
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = Ab[i, -1] - np.dot(Ab[i, i+1:n], x[i+1:n])
    
    return x


A = np.array([[4, 2, 3], [-7, -1, 4], [-2, 10, 2]])
b = np.array([8, -11, -3])
print(gauss_m(A, b))