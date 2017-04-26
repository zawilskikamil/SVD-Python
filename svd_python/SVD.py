import numpy as np
from svd_python.common import funkcje

A = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]


def validate(matrix):
    return False


def do_stuff(matrix):
    # jakaś walidacja czy matrix to macierz
    if not validate(matrix):
        pass
        # dodamy potem
        # raise Exception

    # 1. transponujemy macierz
    T = funkcje.transpozycja(A)

    # 2. liczymy AT (AAT) i TA (ATA)
    AT = funkcje.mnozenie(A, T)
    TA = funkcje.mnozenie(T, A)

    # 3. wybieramy macierz
    # if (np.linalg.matrix_rank(TA) > np.linalg.matrix_rank(AT)):
    #    main_matrix = AT
    # else:
    #    main_matrix = TA

    # 4.
    # 5.
    # 6.
    # 7.
    # 8.
    # 9.


do_stuff(A)
