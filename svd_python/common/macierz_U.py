from svd_python.common import funkcje
import math

def stworz_macierz_U(pierwiastki, A, V, r):
    U = []
    print(1/math.sqrt(pierwiastki[0]))
    for j in range(r):
        U = U.append(1 / math.sqrt(pierwiastki[j]) * funkcje.mnozenie(A, V[:, j]))
    return U
