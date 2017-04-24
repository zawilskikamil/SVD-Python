A = [[1,2,3,4],[1,2,3,4],[1,2,3,4]]

def transpozycja(macierz):
    transponowana = [list(i) for i in zip(*macierz)]
    return transponowana


## działa tylko dla macierzy kwadratowych
def mnozenie(macierz1, macierz2):
    wynik = []
    for i in range(len(macierz1)):
        wiersz = macierz1[i]
        nowyWiersz = []
        for j in range(len(macierz2[0])):
            y = 0
            for x in range(len(wiersz)):
                wierszE = wiersz[x]
                kolumnaE = macierz2[x][j]
                y += wierszE + kolumnaE
            nowyWiersz.append(y)
        wynik.append(nowyWiersz)
    return wynik



