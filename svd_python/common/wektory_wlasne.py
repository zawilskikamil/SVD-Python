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
    wartosci_wlasne.sort()
    macierz_wartosci_wlasnych = []
    for w in wartosci_wlasne:
        macierz_wartosci_wlasnych.append(daj_wektor_wlasny(w, macierz))
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


def daj_wektor_wlasny(lamba, macierz):
    kopia_macierzy = copy.deepcopy(macierz)
    for i in range(len(macierz)):
        kopia_macierzy[i][i] = kopia_macierzy[i][i] - lamba
    x0 = [0]*len(kopia_macierzy[0])
    w = scipy.optimize.root(f, x0=x0, args=kopia_macierzy, method='lm')
    return w.x


def f(x,args):
    out = []
    for j in range(len(args)):
        o = 0
        for i in range(len(args[j])):
            o += (x[i] * args[j][i])
        out.append(o)
    o = -1
    for i in range(len(x)):
        o += (x[i] ** 2)
    out.append(o)
    return out

