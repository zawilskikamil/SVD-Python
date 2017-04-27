import unittest
from svd_python.common.funkcje import transpozycja, mnozenie


# class TestStringMethods(unittest.TestCase):
#
#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')



class TestTranspozycja(unittest.TestCase):

    def test_zmiana(self):
        XX = [[1,2,3],[4,5,6],[7,8,9]]
        wynik = [[1,4,7],[2,5,8],[3,6,9]]
        self.assertEqual(transpozycja(XX), wynik, "Źle odwrócona macierz" )


#class TestMnozenie(unittest.TestCase):

    def test_mnozenie(self):
        A1 = [[1,2,3],[4,5,6],[7,8,9]]
        A2 = [[1,2,3],[4,5,6],[7,8,9]]
        wynik = [[30, 36, 42], [66, 81, 96], [102,126, 150]]
        self.assertEquals(mnozenie(A1,A2),wynik, "Zły wynik mnożenia macierzy" )

if __name__ == '__main__':
    unittest.main()