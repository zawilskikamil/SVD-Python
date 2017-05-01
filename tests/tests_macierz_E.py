import unittest
import numpy
from svd_python.common.macierz_E import pierwiastek, stworz_macierz_zer, stworz_macierz_E, pierwiastki


class TestMacierzE(unittest.TestCase):

    def testPierwiastek(self):
        wejsciowa = 81
        wynik =  9
        self.assertEqual(pierwiastek(wejsciowa), wynik, "Źle obliczony pierwiastek!")

    def testMacierzZer(self):
         # Me = 2
         # Ne = 2
         # wynik = [[0,0],[0,0]]
         #self.assertEqual(stworz_macierz_zer(2,2), wynik, "Źle obliczony pierwiastek!")
        pass


    def testPierwiastki(self):
        A =  [2,3,3,2]
        wynik = [1.7320508075688772, 1.7320508075688772, 1.4142135623730951, 1.4142135623730951]
        self.assertEqual(pierwiastki(A), wynik, "Źle obliczone pierwiastki!")

    def testMacierzE(self):
        pass
