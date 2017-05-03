import copy
"""
Plik zawiera klasy robocze niewiadomej oraz wielomianu,
które pozwalają na tworzenie nieliniowego układu równań.
"""
class niewiadoma():
    def __init__(self, a, n):
        self.a = a
        self.n = n

    def __add__(self, other):
        if (isinstance(other, int)):
            other = niewiadoma(other, 0)

        if (isinstance(other, niewiadoma)):
            if (self.n == other.n):
                return niewiadoma(self.a + other.a, self.n)
            else:
                w = wielomian()
                w = w.dodaj_liczbe(self)
                w = w.dodaj_liczbe(other)
                return w
        elif (isinstance(other, wielomian)):
            return other + self

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if (isinstance(other, int)):
            other = niewiadoma(other, 0)
        kopia = copy.deepcopy(self)
        return kopia + (other * (niewiadoma(-1, 0)))

    def __mul__(self, other):
        if (isinstance(other, int)):
            other = niewiadoma(other, 0)
        if (isinstance(other, niewiadoma)):
            return niewiadoma(self.a * other.a, self.n + other.n)
        elif (isinstance(other, wielomian)):
            return other * self

    def __rmul__(self, other):
        return self * other;

    def __str__(self):
        return str(self.a) + 'x^' + str(self.n)


class wielomian():
    def __init__(self, liczby = []):
        self.liczby = liczby

    def __sub__(self, other):
        kopia = copy.deepcopy(self)
        return kopia + (other * (niewiadoma(-1, 0)))

    def __add__(self, other):
        if (isinstance(other, int)):
            other = niewiadoma(other, 0)

        if (isinstance(other, niewiadoma)):
            return self.dodaj_liczbe(other)
        elif (isinstance(other, wielomian)):
            return self.dodaj_wielomian(other)

    def __radd__(self, other):
        return self + other

    def __rmul__(self, other):
        return self * other

    def __mul__(self, other):
        if (isinstance(other, int)):
            other = niewiadoma(other, 0)

        if (isinstance(other, niewiadoma)):
            return self.pomnoz_przez_liczbe(other)
        elif (isinstance(other, wielomian)):
            return self.pomnoz_przez_wielomian(other)
            pass

    def dodaj_liczbe(self, niewiadoma):
        kopia = copy.deepcopy(self)
        istnieje = None
        for x in kopia.liczby:
            if (x.n == niewiadoma.n):
                istnieje = x
        if (istnieje == None):
            kopia.liczby.append(niewiadoma)
        else:
            kopia.liczby.remove(istnieje)
            kopia.liczby.append(istnieje + niewiadoma)
        return kopia

    def dodaj_wielomian(self, wielomian):
        kopia = copy.deepcopy(self)
        for w in wielomian.liczby:
            kopia = kopia.dodaj_liczbe(w)
        return kopia

    def pomnoz_przez_liczbe(self, niewiadoma):
        kopia = copy.deepcopy(self)
        l = []
        for w in kopia.liczby:
            l.append(w * niewiadoma)
        return wielomian(l)

    def pomnoz_przez_wielomian(self, inny_wielomian):
        kopia = copy.deepcopy(self)
        nowa = wielomian()
        for w in inny_wielomian.liczby:
            nowa = nowa + (kopia.pomnoz_przez_liczbe(w))
        return nowa

    # zwraca liste wspolczynnikow
    # odpowiednio dla ax^0 + bx^1 + cx^2 + ...
    #  [a,b,c]
    def daj_wspolczynniki(self):
        """zwraca liste wspolczynnikow
        odpowiednio dla ax^0 + bx^1 + cx^2 + ...
        [a,b,c]
        :return:
         [int]: lista współczynników
        """
        najwiekszy = 0;
        for w in self.liczby:
            if najwiekszy < w.n:
                najwiekszy = w.n
        wsp = [0] * (najwiekszy + 1)
        for w in  self.liczby:
            wsp[w.n] = w.a
        return wsp

    def __str__(self):
        s = ""
        for w in self.liczby:
            s += " + " + str(w)
        return s
