import numpy as np
A = [[1,2,3],[1,2,3],[1,2,3]]
def do_stuff(matrix):
    # jakaś walidacja czy matrix to macierz
    if not validate(matrix):
        raise Exception

    # 1. transponujemy macierz
    T = np.transpose(A)


    # 2. liczymy AT (AAT) i TA (ATA)
    AT = np.dot(A,T)
    TA = np.dot(T,A)

    # 3. wybieramy macierz
    if (np.linalg.matrix_rank(TA) > np.linalg.matrix_rank(AT)):
        main_matrix = AT
    else:
        main_matrix = TA

    # 4.
    # 5.
    # 6.
    # 7.
    # 8.
    # 9.

def validate(matrix):
    return False
