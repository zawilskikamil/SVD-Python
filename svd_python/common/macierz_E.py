def pierwiastek(p):
    import math
    return math.sqrt(p)

def stworz_macierz_zer(m, n):
    import numpy as np
    E = np.zeros((m,n))
    return E

def stworz_macierz_E(wartosci_wlasne, numrows, numcols):
    pierwiastki = []
    for i in range(len(wartosci_wlasne)):
        pierwiastki.append(pierwiastek(wartosci_wlasne[i]))
    E = stworz_macierz_zer(numrows,numcols)
    pierwiastki.sort(reverse=True)
    for i in range(len(pierwiastki)):
        E[i,i] = pierwiastki[i]
    return E


print(stworz_macierz_zer(2,2))