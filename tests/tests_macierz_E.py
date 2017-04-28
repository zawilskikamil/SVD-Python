import unittest
import numpy
from svd_python.common.macierz_E import pierwiastek, stworz_macierz_zer, stworz_macierz_E


class TestMacierzE(unittest.TestCase):

    def testPierwiastek(self):
        wejsciowa = 81
        wynik =  9
        self.assertEqual(pierwiastek(wejsciowa), wynik, "Źle obliczony pierwiastek!")

    def testMacierzZer(self):
         Me = 2
         Ne = 2
         wynik = numpy.repeat(0, (Me*Ne)).reshape((Me, Ne))
         self.assertEqual(stworz_macierz_zer(2,2), wynik, "Źle obliczony pierwiastek!")


