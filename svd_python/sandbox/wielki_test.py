import numpy

from svd_python import SVD
from svd_python.common import funkcje

A = [[1, 3, 1, 12], [4, 11, 22, 9],[5, 11, 7, 9],[5, 13, 22, 4]]
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
print(numpy.dot(numpy.dot(q2[0], q2[1]), q2[2]))