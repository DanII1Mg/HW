import numpy as np

def seidel(A, b):
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
    max_iter = 100  
    
    for k in range(max_iter):
        x_new = np.copy(x)
        for i in range(n):
            x_new[i] = np.dot(alpha[i, :], x_new) + beta[i]
        
        if np.linalg.norm(x_new - x) < e:
            return x_new  
        x = x_new
    
A = np.array([[10, 1, 1], [2, 10, 1], [2, 2, 10]])
b = np.array([12, 13, 14])
print(seidel(A,b))