from svd_python.common import funkcje, wektory_wlasne, macierz_E, macierz_U

A = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
B = [[2,1,0], [-6,1,-6], [-3,1,-1]]


def validate(matrix):
    return False


def daj_nam_wynik(matrix):
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
    if (funkcje.oblicz_wyznacznik(TA) > funkcje.oblicz_wyznacznik(AT)):
       main_matrix = AT
    else:
       main_matrix = TA

    wartosci_wlasne, V = wektory_wlasne.daj(main_matrix)
    print(wartosci_wlasne)
    print(V)

    # =========== do zrobienia ===========
    # 7. Stworzyć macierz ∑ € Rmxn i umieścić na diagonalnej pierwiastki kwadratowe z wartości własnych macierzy Aw (main_matrix).
    numrows = len(A)
    numcols = len(A[0])
    pierwiastki = macierz_E.pierwiastki(wartosci_wlasne)
    E = macierz_E.stworz_macierz_E(pierwiastki, numrows, numcols)
    print(E)

    # 8. Znaleźć r pierwszych wektorów kolumnowych macierzy U € Rmxm
    #    z równań Uj= 1/sqrt(Vj) * A * Vj, gdzie j = 1,2…r.
    r = funkcje.licz_R(wartosci_wlasne)
    print(r)
    U = macierz_U.stworz_macierz_U(pierwiastki, A, V, r)
    print(U)


    # 9. Dodać do macierzy U pozostałe m-r
    #    wektorów wykorzystując proces ortogonalizacji
    #    Grama-Schmidta (i unormować wektory?).
    #

daj_nam_wynik(A)
