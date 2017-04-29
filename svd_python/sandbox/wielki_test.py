import numpy

from svd_python import SVD

A = [[1,1], [0,1], [1,0]]
q = numpy.linalg.svd(A)
q2 = SVD.daj_nam_wynik(A)
print("================")
print(q[0])
print(q[1])
print(q[2])

print("================")
print(q2[0])
print(q2[1])
print(q2[2])