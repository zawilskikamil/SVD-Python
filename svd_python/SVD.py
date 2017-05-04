import numpy

from svd_python.common import funkcje, macierz_Vt, macierz_E, macierz_U

def daj_nam_wynik(matrix):
    """algorytm SVD

    funkcja dokonuje rozkładu macierzy wejściowej według algorytmu SVD

    Args:
        matrix ([[float]]): macierz - lista dwuwymiarowa

    Returns:
        ([[float]],[[float]],[[float]]): ortonormalna macierz U, macierz diagonalna, macierz Vt - transponowana ortonormalna macierz V
    -------
    """
    #1. Dokonana zostaje transpozycja macierzy wejściowej.
    T = funkcje.transpozycja(matrix)

    #2. Następnie wyliczone zostają macierze ATA i AAT.
    AT = funkcje.mnozenie(matrix, T)
    TA = funkcje.mnozenie(T, matrix)

    #3. W kolejnym etapie zostaje wyliczony rząd dla każdej z utworzonych w poprzednim etapie macierzy.
    #   Następnie zostają one porównane w celu wybrania macierzy z mniejszym rzędem w celu wybrania właściwej macierzy.
    #   Zostają również obliczone jej wartości własne i utworzona zostaje macierz V.
    if (numpy.linalg.matrix_rank(TA) > numpy.linalg.matrix_rank(AT)):
       main_matrix = AT
    else:
       main_matrix = TA

    wartosci_wlasne, V = macierz_Vt.stworz_macierz_Vt(main_matrix)

    #4. Następnym krokiem jest stworzenie macierzy ∑ i obliczenie pierwiastków kwadratowych
    #   z wartości własnych macierzy Aw (czyli macierzy właściwej (ATA lub AAT).
    numrows = len(main_matrix)
    numcols = len(main_matrix[0])

    pierwiastki = macierz_E.pierwiastki(wartosci_wlasne)
    E = macierz_E.stworz_macierz_E(pierwiastki, numrows, numcols)

    #5. Ostatnia funkcja składa się z 2 połączonych ze sobą etapów i jest odpowiedzialna
    #   za stworzenie macierzy U i uzupełnienie jej wartości w zależności od rozmiarów macierzy A.
    r = funkcje.licz_R(wartosci_wlasne)

    U = macierz_U.stworz_macierz_U(pierwiastki, matrix, V, r)
    U = funkcje.transpozycja(U)
    return U, E, V



