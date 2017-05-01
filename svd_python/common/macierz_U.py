from svd_python.common import funkcje
import math

def mnozenie_wek(wektor1,wektor2):
    w = 0
    for i in range(len(wektor1)):
        w += wektor1[i][0]*wektor2[0][i]
    return w

def wektor_razy_liczba(wektor, liczba):
    w = []
    for y in range(len(wektor)):
        w.append(wektor[y] * liczba)
    return w

def dlugosc_wektora(u):
    ut = funkcje.transpozycja(u)
    wektor = mnozenie_wek(ut,u)
    return math.sqrt(wektor)

def oblicz_e(u):
    dl_wektora = 1/dlugosc_wektora([u])
    e = wektor_razy_liczba(u,dl_wektora)
    return e
  
def stworz_macierz_U(pierwiastki, A, V, r):
    U = []
    # print(1/math.sqrt(pierwiastki[0]))
    # Vt = funkcje.transpozycja(V)
    for it in range(r):
        d1 = 1 / pierwiastki[it]
        a = A
        b = V[it]
        c = [0]*len(a)

        for i in range(len(a)):
            for j in range(len(a[i])):
                c[i] = c[i] + (a[i][j] * b[j])
        d2 = c
        for x in range(len(d2)):
            d2[x] = d2[x] * d1
        U.append(d2)
    if (r<len(a[0])):
        pozostale = len(a[0]) - r

    return U

def oblicz_pozostale_u(U,pozostale, r):
     Ut = funkcje.transpozycja(U)
     U1 = Ut[0]
     e = oblicz_e(U1)
     et = funkcje.transpozycja([e])
     odj = wektor_razy_liczba(U1,(mnozenie_wek(et,[U1])))
     uj = funkcje.odejmij_wektory(e, odj)
     if r == 1 & pozostale == 1:
         U.append(uj)
     else:
         for i in range(1, (pozostale - r)):
             uj = uj - e - wektor_razy_liczba(Ut[i], (mnozenie_wek(Ut[i], e)))
             if i>=r:
                U.append(uj)
     return U


