import numpy

from svd_python.common import funkcje, wektory_wlasne, macierz_E, macierz_U

def daj_nam_wynik(matrix):
    """algorytm SVD

    funkcja dokonuje rozkładu macierzy wejściowej według algorytmu SVD

    Args:
        matrix ([[float]]): macierz - lista dwuwymiarowa

    Returns:
        ([[float]],[[float]],[[float]]): ortonormalna macierz U, macierz diagonalna, macierz Vt - transponowana ortonormalna macierz V
    -------
    """

    T = funkcje.transpozycja(matrix)

    AT = funkcje.mnozenie(matrix, T)
    TA = funkcje.mnozenie(T, matrix)

    if (numpy.linalg.matrix_rank(TA) > numpy.linalg.matrix_rank(AT)):
       main_matrix = AT
    else:
       main_matrix = TA

    wartosci_wlasne, V = wektory_wlasne.daj(main_matrix)

    numrows = len(main_matrix)
    numcols = len(main_matrix[0])

    pierwiastki = macierz_E.pierwiastki(wartosci_wlasne)
    E = macierz_E.stworz_macierz_E(pierwiastki, numrows, numcols)

    r = funkcje.licz_R(wartosci_wlasne)

    U = macierz_U.stworz_macierz_U(pierwiastki, matrix, V, r)
    U = funkcje.transpozycja(U)
    return U, E, V



