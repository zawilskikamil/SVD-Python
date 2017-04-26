<<<<<<< Updated upstream
A = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]

=======
A = [[1,2,3],[1,2,3],[1,2,3]]
>>>>>>> Stashed changes

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

<<<<<<< Updated upstream
    wynik = [[0 for row in range(columna_B)] for col in range(wiersz_A)]

    for i in range(wiersz_A):
        for j in range(columna_B):
            for k in range(columna_A):
                wynik[i][j] += macierz_A[i][k] * macierz_B[k][j]
    return wynik
=======
print(mnozenie(A, A))
>>>>>>> Stashed changes

=====

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant
