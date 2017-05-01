import numpy

from svd_python import SVD
from svd_python.common import funkcje

A = [[1,2,3], [7,3,3],[4,5,6]]
q = numpy.linalg.svd(A)
q2 = SVD.daj_nam_wynik(A)
print("================")
print(q[0])
print(q[1])
print(q[2])
# print(numpy.dot(numpy.transpose(q[2]),q[2]))
print("================")
print(q2[0])
print(q2[1])
print(q2[2])
print("================")
print(funkcje.mnozenie(q2[2],funkcje.transpozycja(q2[2])))