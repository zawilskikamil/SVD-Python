import numpy

from svd_python.common import funkcje, wektory_wlasne, macierz_E, macierz_U

def validate(matrix):
    return False



def daj_nam_wynik(matrix):
    """algorytm SVD

    funkcja dokonuje rozkładu macierzy wejściowej według algorytmu SVD

    Parameters
    ----------
    matrix : {(M, N)} array_like
        macierz - lista dwuwymiarowa

    Returns
    U : { (M,M) } array
        ortonormalna macierz U
    E : { (M,M) }  array
        macierz diagonalna
    Vt : { (N,N) }  array
        transponowana ortonormalna macierz V

    -------


    """
    # jakaś walidacja czy matrix to macierz
    if not validate(matrix):
        pass
        # dodamy potem
        # raise Exception

    # 1. transponujemy macierz
    T = funkcje.transpozycja(matrix)

    # 2. liczymy AT (AAT) i TA (ATA)
    AT = funkcje.mnozenie(matrix, T)
    TA = funkcje.mnozenie(T, matrix)

    #3. wybieramy macierz
    if (numpy.linalg.matrix_rank(TA) > numpy.linalg.matrix_rank(AT)):
       main_matrix = AT
    else:
       main_matrix = TA

    wartosci_wlasne, V = wektory_wlasne.daj(main_matrix)

    # print(wartosci_wlasne)
    # print(V)

    # =========== do zrobienia ===========
    # 7. Stworzyć macierz ∑ € Rmxn i umieścić na diagonalnej pierwiastki kwadratowe z wartości własnych macierzy Aw (main_matrix).
    numrows = len(main_matrix)
    numcols = len(main_matrix[0])

    pierwiastki = macierz_E.pierwiastki(wartosci_wlasne)
    E = macierz_E.stworz_macierz_E(pierwiastki, numrows, numcols)
    # print(E)

    # 8. Znaleźć r pierwszych wektorów kolumnowych macierzy U € Rmxm
    #    z równań Uj= 1/sqrt(Vj) * A * Vj, gdzie j = 1,2…r.
    r = funkcje.licz_R(wartosci_wlasne)
    # print(r)
    # Vt = funkcje.transpozycja(V)
    U = macierz_U.stworz_macierz_U(pierwiastki, matrix, V, r)
    # print(U)
    U = numpy.transpose(U)
    return U, E, V
    # 9. Dodać do macierzy U pozostałe m-r
    #    wektorów wykorzystując proces ortogonalizacji
    #    Grama-Schmidta (i unormować wektory?).
    #


