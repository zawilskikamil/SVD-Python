import unittest
from svd_python.common.funkcje import transpozycja, mnozenie, getMatrixDeternminant


class TestTranspozycja(unittest.TestCase):
    def test_zmiana(self):
        XX = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        wynik = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        self.assertEqual(transpozycja(XX), wynik, "Źle odwrócona macierz")

    def test_mnozenie(self):
        A1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        A2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        wynik = [[30, 36, 42], [66, 81, 96], [102, 126, 150]]
        self.assertSequenceEqual(mnozenie(A1, A2), wynik, "Zły wynik mnożenia macierzy")

    def test_wyznacznik(self):
        A = [[5, 1, 3, 3], [32, 3, 9, 9], [6, 6, 7, 8], [4, -1, -2, -9]]
        wynik = -1292
        self.assertEqual(getMatrixDeternminant(A), wynik, "Zły wyznacznik macierzy")


if __name__ == '__main__':
    unittest.main()
