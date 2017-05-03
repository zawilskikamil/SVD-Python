from svd_python.common import funkcje
import math

def mnozenie_wek(wektor1,wektor2):
    w = 0
    try:
        if wektor1[0][0] or wektor2[0][0]:
            w = 0
    except TypeError:
        for i in range(len(wektor1)):
            w += wektor1[i]*wektor2[i][0]
    else:
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
    """funkca zwraca macierz U
            Args:
              pierwiastki ([num]): pierwiastki wartości własnych
              A ([[num]]): macierz
              V ([[num]]): macierz
              r (num): liczba niezerowych wartości własnych

            Returns:
              [[num]]: macierz U
    """
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
        U = oblicz_pozostale_u(U,pozostale,r)
    return U

def oblicz_pozostale_u(U,pozostale, r):
     Ut = funkcje.transpozycja(U)
     U1 = Ut[0]
     e = oblicz_e(U1)
     et = funkcje.transpozycja([e])
     odj = wektor_razy_liczba(U1,(mnozenie_wek(et,[U1])))
     uj = funkcje.odejmij_wektory(e, odj)
     for i in range(1, pozostale+r-1):
        uj = funkcje.odejmij_wektory(uj, wektor_razy_liczba(Ut[i], (mnozenie_wek(Ut[i], et))))
        if i>=r-1:
            Ut.append(uj)
     return Ut


# U = [[1,0,1],[0, 0.6, -0.8],[0, 0.8, 0.6]]
# print(oblicz_pozostale_u(U,2,3))
