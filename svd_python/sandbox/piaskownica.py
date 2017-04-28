import ctypes

import numpy
from svd_python.common.wielomiany import *




w1 = wielomian()
w1 = w1 + niewiadoma(1,1)
w1 = w1 + niewiadoma(-3,0)

w2 = wielomian()
w2 = w2 + niewiadoma(1,1)
w2 = w2 + niewiadoma(-1,0)

w3 = wielomian()
w3 = w3 + niewiadoma(1,1)
w3 = w3 + niewiadoma(3,0)

w4 = w1 * w2 * w3
print(w4)
print(w4.daj_wspolczynniki())
print(list(reversed(w4.daj_wspolczynniki())))
coeff = list(reversed(w4.daj_wspolczynniki()))
d = numpy.roots(coeff)
print(d)

coeff = [1,2,2]
d = numpy.roots(coeff)
print(d)

numpy.linalg.cond([[1,2],[1,2]])


a = numpy.repeat(0, 50).reshape((5,10))

print(a)

Me = 2
Ne = 2
wynik = numpy.repeat(0, (Me * Ne)).reshape((Me, Ne))
print(wynik)

p