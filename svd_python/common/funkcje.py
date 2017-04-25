A = [[1,2,3,4],[1,2,3,4],[1,2,3,4]]

def transpozycja(macierz):
    transponowana = [list(i) for i in zip(*macierz)]
    return transponowana


## działa tylko dla macierzy kwadratowych
def mnozenie(macierz_A, macierz_B):
    wiersz_A = len(macierz_A)
    columna_A = len(macierz_A[0])
    wiersz_B = len(macierz_B)
    columna_B = len(macierz_B[0])

    if columna_A != columna_B:
      print "Nie można mnożyć macierzy, ZŁE WYMIARY"
      return

    # Create the result matrix
    # Dimensions would be rows_A x cols_B
    wynik = [[0 for row in range(columna_B)] for col in range(wiersz_A)]
    print wynik

    for i in range(wiersz_A):
        for j in range(columna_B):
            for k in range(columna_A):
                wynik[i][j] += macierz_A[i][k] * macierz_B[k][j]
    return wynik
    



