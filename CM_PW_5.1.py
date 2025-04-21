import numpy as np

#Метод простой итерации

def func(A, b):    
    n = A.shape[0]
    alpha = np.zeros((n, n))
    beta = np.zeros(n)
    
    for i in range(n):
        beta[i] = b[i] / A[i, i]
        for j in range(n):
            if i != j:
                alpha[i, j] = -A[i, j] / A[i, i]
    
    x = beta.copy()
    e = 0.001
    for k in range(100):
        x_n = alpha @ x + beta
        if np.linalg.norm(x_n - x) < e:
            return x_n 
        x = x_n
    else:
        raise ValueError("Метод не сошелся за 100 итераций")
    
    
    
A = np.array([[10, 1, 1], [2, 10, 1], [2, 2, 10]])
b = np.array([12, 13, 14]) 

print(func(A,b))