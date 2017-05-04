import numpy

from svd_python import SVD
from svd_python.common import funkcje

A = [[4,12,3],[-11,3,32],[-3,-33,2]]
nU, nE, nVt = numpy.linalg.svd(A)
U, E, Vt = SVD.daj_nam_wynik(A)
print("================")
print(nU)
print(nE)
print(nVt)
print("================")
print(U)
print(E)
print(Vt)
print("================")
print(numpy.dot(numpy.dot(U,E), Vt))