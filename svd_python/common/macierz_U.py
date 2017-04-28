from svd_python.common import funkcje
import math

def stworz_macierz_U(pierwiastki, A, V, r):
    U = []
    print(1/math.sqrt(pierwiastki[0]))
    Vt = funkcje.transpozycja(V)
    for j in range(r):
        d1 = 1 / math.sqrt(pierwiastki[j])
        #d2 = funkcje.mnozenie(A, [Vt[j]])
        a = A
        b = [Vt[j]]
        c = [[0 for row in range(1)] for col in range(len(a))]

        for i in range(len(a)):
            for j in range(len(a[i])):
                c[i][0] = c[i][0] + (a[i][j] * b[0][j])
        d2 = c
        for x in range(len(d2)):
            for y in range(len(d2[x])):
                d2[x][y] = d2[x][y] * d1
        U.append( d2 )
    return U
