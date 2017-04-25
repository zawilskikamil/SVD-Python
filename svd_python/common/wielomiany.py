# liczba ax^n
class niewiadoma():
    def __init__(self, a, n):
        self.a = a
        self.n = n

    def __add__(self, other):
        if (isinstance(other, niewiadoma)):
            if (self.n == other.n):
                return niewiadoma(self.a + other.a, self.n)
            else:
                w = wielomian()
                w.dodaj_liczbe(self)
                w.dodaj_liczbe(other)
                return w


    def __str__(self):
        return str(self.a) + 'x^' + str(self.n)


class wielomian():
    def __init__(self):
        self.liczby = []

    def dodaj_liczbe(self, niewiadoma):
        istnieje = None
        for x in self.liczby:
            if (x.n == niewiadoma.n):
                istnieje = x
        if (istnieje == None):
            self.liczby.append(niewiadoma)
        else:
            self.liczby.remove(istnieje)
            self.liczby.append(istnieje + niewiadoma)

    def dodaj_wielomian(self, wielomian):
        for w in wielomian.liczby:
            self.dodaj_liczbe(w)

    def __str__(self):
        s = ""
        for w in self.liczby:
            s += " + " + str(w)
        return s

n = niewiadoma(2, 0)
print(n)
w = wielomian()
w.dodaj_liczbe(n)
n2 = niewiadoma(2, 1)
n3 = niewiadoma(1, 2)
w.dodaj_liczbe(n2)
w.dodaj_liczbe(n2)
w.dodaj_liczbe(n3)
print(w)