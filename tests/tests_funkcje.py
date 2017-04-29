import unittest
from svd_python.common.funkcje import transpozycja, mnozenie, oblicz_wyznacznik, daj_Minor, licz_R


class TestFunkcje(unittest.TestCase):
    def test_zmiana(self):
        XX = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        wynik = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        self.assertEqual(transpozycja(XX), wynik, "Źle odwrócona macierz")

    def test_mnozenie(self):
        A1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        A2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        wynik = [[30, 36, 42], [66, 81, 96], [102, 126, 150]]
        self.assertEqual(mnozenie(A1,A2), wynik, "Zły wyznacznik macierzy")

    def test_wyznacznik(self):
        A = [[5, 1, 3, 3], [32, 3, 9, 9], [6, 6, 7, 8], [4, -1, -2, -9]]
        wynik = -1292
        self.assertEqual(oblicz_wyznacznik(A), wynik, "Zły wyznacznik macierzy")

    def test_rzad(self):
        A = [[1, 2, 3], [1,2,3], [1,2,3]]
        wynik = [[1,3],[1,3]]
        self.assertEqual(daj_Minor(A,2,1),wynik,"Źle obliczony rząd macierzy")

    def testLiczR(self):
        A = [1,2,3,3]
        wynik = 4
        self.assertEqual(licz_R(A), wynik, "Źle obliczony R macierzy")



if __name__ == '__main__':
    unittest.main()
