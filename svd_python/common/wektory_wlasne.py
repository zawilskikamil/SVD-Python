import numpy
import copy

import scipy.optimize

from svd_python.common import funkcje
from svd_python.common import wielomiany


def daj(macierz):
    m = stworz_macierz_wielomianow(macierz)
    m = odejmij_i_lambda(m)
    w = funkcje.oblicz_wyznacznik(m)
    coeff = list(reversed(w.daj_wspolczynniki()))
    wartosci_wlasne = numpy.roots(coeff)
    macierz_wartosci_wlasnych = []

    macierz_wartosci_wlasnych = daj_wektor_wlasny(wartosci_wlasne, macierz)
    wartosci_wlasne.sort()
    return wartosci_wlasne, macierz_wartosci_wlasnych


def stworz_macierz_wielomianow(macierz):
    macierz_wielomianow = []
    for a in macierz:
        wiersz = []
        for b in a:
            wiersz.append(wielomiany.niewiadoma(b, 0))
        macierz_wielomianow.append(wiersz)
    return macierz_wielomianow


def odejmij_i_lambda(macierz):
    for i in range(len(macierz)):
        q = macierz[i][i]
        sdf = q - wielomiany.niewiadoma(1, 1)
        macierz[i][i] = sdf
    return macierz


def daj_wektor_wlasny(lamby, macierz):
    kopia_macierzy = copy.deepcopy(macierz)
    args = []
    for l in lamby:
        k = copy.deepcopy(kopia_macierzy)
        for i in range(len(macierz)):
            k[i][i] = k[i][i] - l
        args.append(k)
    x0 = [0]*(len(kopia_macierzy[0])*len(lamby))
    w = scipy.optimize.root(f, x0=x0, args=args, method='lm')
    return numpy.array_split(w.x, len(lamby))


def f(x,args):
    out = []
    for alen in range(len(args)):
        a = args[alen]
        for j in range(len(a)):
            o = 0
            for i in range(len(a[j])):
                o += (x[i + alen * len(a[0])] * a[j][i])
            out.append(o)
        o = -1
        for i in range(alen * (len(a[0])), alen * len(a[0]) + len(a[0])):
            o += (x[i] ** 2)
        out.append(o)
    for k in range(len(args)):
        for i in range(k+1,len(args)):
            o = 0
            for j in range(len(args[0])):
                x1 = j + k * len(args[0])
                x2 = j + i*len(args[0])
                o += x[x1]*x[x2]
            out.append(o)
    return out

a = daj([[1,2,3],[3,2,3],[1,2,31]])
print(a)