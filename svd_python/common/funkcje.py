def transpozycja(macierz):
    transponowana = [list(i) for i in zip(*macierz)]
    return transponowana


def mnozenie(macierz_A, macierz_B):
    wiersz_A = len(macierz_A)
    columna_A = len(macierz_A[0])
    wiersz_B = len(macierz_B)
    columna_B = len(macierz_B[0])

    if columna_A != columna_B:
        print("Nie można mnożyć macierzy, ZŁE WYMIARY")
        return

    wynik = [[0 for row in range(columna_B)] for col in range(wiersz_A)]

    for i in range(wiersz_A):
        for j in range(columna_B):
            for k in range(columna_A):
                wynik[i][j] += macierz_A[i][k] * macierz_B[k][j]
    return wynik


def daj_Minor(m, i, j):
    return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]


def oblicz_wyznacznik(m):
    # base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    wyznacznik = 0
    for c in range(len(m)):
        wyznacznik = wyznacznik + ((-1) ** c) * m[0][c] * oblicz_wyznacznik(daj_Minor(m, 0, c))
    return wyznacznik

def licz_R(wartosci_wlasne):
    r = 0
    for i in range(len(wartosci_wlasne)):
        if wartosci_wlasne[i]!=0:
            r+=1
    return r