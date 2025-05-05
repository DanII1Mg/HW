import numpy as np

def direct_deployment_method(A):
    a, b = A[0, 0], A[0, 1]
    c, d = A[1, 0], A[1, 1]
    trace = a + d
    det = a * d - b * c
    coeffs = [1, -trace, det]


    D = coeffs[1] ** 2 - 4 * coeffs[0] * coeffs[2]
    if D < 0:
        return
    elif D == 0:
        s_znach = [-coeffs[1] / (2 * coeffs[0])]
    else:
        sqrt_D = D ** 0.5
        s_znach = [(-coeffs[1] + sqrt_D) / (2 * coeffs[0]),
                       (-coeffs[1] - sqrt_D) / (2 * coeffs[0])]

    for i, lambd in enumerate(s_znach):
        I = np.eye(2)
        M = A - lambd * I

        if abs(M[0][0]) > 1e-10 or abs(M[0][1]) > 1e-10:
            row = M[0]
        else:
            row = M[1]

        a_row, b_row = row
        if abs(b_row) > 1e-4:
            x2 = 1.0
            x1 = (-b_row * x2) / a_row if abs(a_row) > 1e-10 else 0.0
        elif abs(a_row) > 1e-4:
            x1 = 1.0
            x2 = (-a_row * x1) / b_row if abs(b_row) > 1e-10 else 0.0
        else:
            x1, x2 = 1, 1

        vect = np.array([x1, x2], dtype=float)
        norm = np.linalg.norm(vect)
        vect = vect / norm if norm != 0 else vect

        print(f"Собственный вектор{i+1}: {vect}")


A = np.array([
    [3, -2],
    [-4, 1]
])

direct_deployment_method(A)
