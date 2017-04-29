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
    a = numpy.array(kopia_macierzy)
    b = numpy.array([0] * len(kopia_macierzy))
    # TODO treba dodać warunek x^2 + y^2 = 1
    # http://stackoverflow.com/questions/8739227/how-to-solve-a-pair-of-nonlinear-equations-using-python
    # from scipy.optimize import fsolve
    # import math
    #
    # def equations(p):
    #     x, y = p
    #     return (x + y ** 2 - 4, math.exp(x) + x * y - 3)
    #
    # x, y = fsolve(equations, (1, 1))
    #
    # print equations((x, y))
    if funkcje.oblicz_wyznacznik(kopia_macierzy) > 0:
        return numpy.linalg.solve(a, b)
    else:
        b = (funkcje.transpozycja(a)[0])
        for i in range(len(b)):
            b[i] = - b[i]
        a = (funkcje.transpozycja(funkcje.transpozycja(a)[1:]))
        narray = (numpy.linalg.lstsq(a, b, 0)[0])
        wektor = narray.tolist()
        # for i in range(len(wektor)):
        #     if isinstance(wektor[i],numpy.complex):
        #         pass
        #     else:
        #         wektor[i] = float(wektor[i])
        wektor.insert(0, 1)
        return wektor


# print(daj([[2,1],[1,2]]))


def f(x, args):
    out = []
    for j in range(len(args)):
        o = 0
        for i in range(len(args[j])):
            o += (x[i] * args[j][i])
        out.append(o)
    o = 0
    for i in range(len(x)):
        o += (x[i] ** 2)
    out.append(o)
    return out

w = scipy.optimize.root(fun=f, x0=[1, 1], args=[[1, 2],[2,1]], method='excitingmixing', jac=False)
print(w)
# w = scipy.optimize.root(f, [0, 0], [[1, 2]])
# print(w)