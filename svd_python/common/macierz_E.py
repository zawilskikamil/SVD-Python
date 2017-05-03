import math
import numpy as np

def pierwiastek(p):
    return math.sqrt(p)

def stworz_macierz_zer(m, n):
    E = np.zeros((m,n))
    return E

def pierwiastki(wartosci_wlasne):
    pierwiastki = []
    for i in range(len(wartosci_wlasne)):
        pierwiastki.append(pierwiastek(wartosci_wlasne[i]))
    pierwiastki.sort(reverse=True)
    return pierwiastki

def stworz_macierz_E(pierwiastki, numrows, numcols):
    """funkca zwraca macierz E - diagonalną macierz wartosci własnych macierzy wejsicowej
            Args:
              pierwiastki ([num]): lista wartości własnych
              numrows (int): liczba wierszy
              numcols (int): liczba kolum

            Returns:
              [[num]]: diagonalna macierz wartosci własnych
    """
    E = stworz_macierz_zer(numrows,numcols)
    for i in range(len(pierwiastki)):
        E[i,i] = pierwiastki[i]
    return E


