import numpy

from svd_python import SVD
from svd_python.common import funkcje

A = [[1,2], [2,1]]
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
qw = q2[0]
print(numpy.dot(numpy.dot(q[0], q2[1]), numpy.transpose(q2[2])))