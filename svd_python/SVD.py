from svd_python.common import funkcje, wektory_wlasne

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
    #    czyli:
    #   [ sqrt(V1)  0         0        ]
    #   [ 0         sqrt(V2)  0        ]
    #   [ 0         0         sqrt(V3) ]
    #   tak??
    #
    #
    # 8. Znaleźć r pierwszych wektorów kolumnowych macierzy U € Rmxm
    #    z równań Uj= 1/sqrt(Vj) * A * Vj, gdzie j = 1,2…r.
    #
    #
    # 9. Dodać do macierzy U pozostałe m-r
    #    wektorów wykorzystując proces ortogonalizacji
    #    Grama-Schmidta (i unormować wektory?).
    #

daj_nam_wynik(A)
