from numpy import matrix, linalg
A = matrix([[1,1,1],[1,1,1],[1,1,2]])
print(linalg.matrix_rank(A))