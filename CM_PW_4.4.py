import numpy as np

# LU-разложние
def LU(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    
    for i in range(n):
        for k in range(i, n):
            U[i, k] = A[i, k] - sum(L[i, j] * U[j, k] for j in range(i))
        
        for k in range(i, n):
            if i == k:
                L[i, i] = 1 
            else:
                L[k, i] = (A[k, i] - sum(L[k, j] * U[j, i] for j in range(i))) / U[i, i]
    
    return L, U

A = np.array([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]])
L, U = LU(A)
print("L матрица\n", L)
print("U матрица\n", U)