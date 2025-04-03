from pion import Pion
from wynik import Wynik
from ruch import Ruch

class Plansza:
    def __init__(self):
        self._zawartosc = [
                [Pion('.'), Pion('.'), Pion('.')],
                [Pion('.'), Pion('.'), Pion('.')],
                [Pion('.'), Pion('.'), Pion('.')],
            ]

    def __call__(self, wiersz:int, kolumna:int) -> Pion:
        return self._zawartosc[wiersz][kolumna]

    def wykonaj_ruch(self, ruch:Ruch):
        self._zawartosc[ruch.wiersz()][ruch.kolumna()] = ruch.pion()

    def czy_ruch_poprawny(self, ruch:Ruch) -> bool:
        if ruch.wiersz() not in [0, 1, 2] or ruch.kolumna() not in [0, 1, 2]:
            return False
        return self._zawartosc[ruch.wiersz()][ruch.kolumna()] == Pion('.')

    def czy_koniec(self) -> bool:
        if self.wynik_partii() != Wynik('.'):
            return True
        for wiersz in [0, 1, 2]:
            for kolumna in [0, 1, 2]:
                if self._zawartosc[wiersz][kolumna] == Pion('.'):
                    return False
        return True

    def wynik_partii(self) -> Wynik:
        #przekatna \
        if self._zawartosc[0][0] == self._zawartosc[1][1] == self._zawartosc[2][2] != Pion('.'):
            return Wynik(self._zawartosc[0][0].wyglad())
        #przekatna /
        if self._zawartosc[0][2] == self._zawartosc[1][1] == self._zawartosc[2][0] != Pion('.'):
            return Wynik(self._zawartosc[0][2].wyglad())
        #wiersze
        for wiersz in [0, 1, 2]:
            if (self._zawartosc[wiersz][0]
                    == self._zawartosc[wiersz][1]
                    == self._zawartosc[wiersz][2] != Pion('.')):
                return Wynik(self._zawartosc[wiersz][2].wyglad())
        #kolumny
        for kolumna in [0, 1, 2]:
            if (self._zawartosc[0][kolumna]
                    == self._zawartosc[1][kolumna]
                    == self._zawartosc[2][kolumna] != Pion('.')):
                return Wynik(self._zawartosc[2][kolumna].wyglad())
        return Wynik('.')
    
def test0():
    p = Plansza()
    print(p._zawartosc == [
                [Pion('.'), Pion('.'), Pion('.')],
                [Pion('.'), Pion('.'), Pion('.')],
                [Pion('.'), Pion('.'), Pion('.')],
            ])


def test1():
    p = Plansza()
    print(p(1, 2) == Pion('.'))


def test2():
    p = Plansza()
    p.wykonaj_ruch(Ruch(1, 2, Pion('x')))
    print(p(1, 2) == Pion('x'))


def test3():
    p = Plansza()
    p.wykonaj_ruch(Ruch(1, 2, Pion('x')))
    print(p.czy_ruch_poprawny(Ruch(1, 2, Pion('o'))) == False)
    print(p.czy_ruch_poprawny(Ruch(2, 2, Pion('o'))))


def test4():
    p = Plansza()
    print(p.czy_koniec() == False)


def test5():
    p = Plansza()
    print(p.wynik_partii() == Wynik('.'))


def test6():
    p = Plansza()
    p.wykonaj_ruch(Ruch(1, 1, Pion('x')))
    print(p.czy_koniec() == False)
    print(p.wynik_partii() == Wynik('.'))
    p.wykonaj_ruch(Ruch(1, 0, Pion('o')))
    print(p.czy_koniec() == False)
    print(p.wynik_partii() == Wynik('.'))
    p.wykonaj_ruch(Ruch(0, 0, Pion('x')))
    print(p.czy_koniec() == False)
    print(p.wynik_partii() == Wynik('.'))
    p.wykonaj_ruch(Ruch(2, 1, Pion('o')))
    print(p.czy_koniec() == False)
    print(p.wynik_partii() == Wynik('.'))
    p.wykonaj_ruch(Ruch(2, 2, Pion('x')))
    print(p.czy_koniec())
    print(p.wynik_partii() == Wynik('x'))


def all_tests():
    test0()
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
