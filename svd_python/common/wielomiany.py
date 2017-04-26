import copy
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

    def __mul__(self, other):
        return niewiadoma(self.a * other.a, self.n + other.n)

    def __str__(self):
        return str(self.a) + 'x^' + str(self.n)


class wielomian():
    def __init__(self):
        self.liczby = []

    def __add__(self, other):
        if (isinstance(other, niewiadoma)):
            return self.dodaj_liczbe(other)
        elif (isinstance(other, wielomian)):
            return self.dodaj_wielomian(other)


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

    def __str__(self):
        s = ""
        for w in self.liczby:
            s += " + " + str(w)
        return s

n = niewiadoma(2, 0)
print(n)
w = wielomian()
w = w + n
n2 = niewiadoma(2, 1)
n3 = niewiadoma(1, 2)
w = w + n2
w = w + n3
print(w)
w = w + w
print(w)