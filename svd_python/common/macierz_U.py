from svd_python.common import funkcje
import math

u = [[1],[1],[0]]

def mnozenie_wek(wektor1,wektor2):
    w = 0
    for i in range(len(wektor1)):
        w += wektor1[0][i]*wektor2[i][0]
    return w

def wektor_razy_liczba(wektor, liczba):
    w = []
    for y in range(len(wektor)):
        w.append(w[y][0] * liczba)
    return w

def dlugosc_wektora(u):
    ut = funkcje.transpozycja(u)
    wektor = mnozenie_wek(ut,u)
    return math.sqrt(wektor)

def oblicz_e(u):
    dl_wektora = 1/dlugosc_wektora(u)
    e = wektor_razy_liczba(u,dl_wektora)
    return e
  
def stworz_macierz_U(pierwiastki, A, V, r):
    U = []
    print(1/math.sqrt(pierwiastki[0]))
    Vt = funkcje.transpozycja(V)
    for j in range(r):
        d1 = 1 / math.sqrt(pierwiastki[j])
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
        U.append(d2)
    if (r<len(a[0])):
        pozostale = len(a[0]) - r

    return U

def oblicz_pozostale_u(U,pozostale):
    Ut = funkcje.transpozycja(U)
    U1 = Ut[0]
    e = oblicz_e(U1)
    uj = e - wektor_razy_liczba(U1,(mnozenie_wek(U1,e)))
    if r==1
    for i in range()

    return U1

U = [[1,2,3],[4,5,6]]

print(oblicz_pozostale_u(U))







