import numpy as np

def jordan_gauss_m(A, b):
    n = len(A)
    Ab = np.hstack([A.astype(float), b.astype(float).reshape(-1, 1)])
    
    for i in range(n):
        max_row = i + np.argmax(np.abs(Ab[i:, i]))
        Ab[[i, max_row]] = Ab[[max_row, i]]
        Ab[i] = Ab[i] / Ab[i, i]
        
        for k in range(n):
            if k != i:
                Ab[k] = Ab[k] - Ab[k, i] * Ab[i]
    
    return Ab[:, -1]

A = np.array([[4, 2, 3], [-7, -1, 4], [-2, 10, 2]])
b = np.array([8, -11, -3])
print(jordan_gauss_m(A, b))