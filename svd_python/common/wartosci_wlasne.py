from svd_python.common import funkcje
from svd_python.common import wielomiany

A = [[1,2,3],[4,1,4],[3,2,3]]

def daj(macierz):
    m = stworz_macierz_wielomianow(macierz)
    print(funkcje.getMatrixDeternminant(m))
    m = odejmij_i_lambda(m)
    w = funkcje.getMatrixDeternminant(m)
    print(w)
    print(w.daj_wspolczynniki())

def stworz_macierz_wielomianow(macierz):
    macierz_wielomianow = []
    for a in macierz:
        wiersz = []
        for b in a:
            wiersz.append(wielomiany.niewiadoma(b,0))
        macierz_wielomianow.append(wiersz)
    return macierz_wielomianow

def odejmij_i_lambda(macierz):
    for i in range(len(macierz)):
        q = macierz[i][i]
        sdf = q - wielomiany.niewiadoma(1,1)
        macierz[i][i] = sdf
    return macierz

daj(A)
