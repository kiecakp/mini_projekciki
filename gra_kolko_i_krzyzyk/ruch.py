from pion import Pion

class Ruch:

    def __init__(self, wiersz:int, kolumna:int, pion:Pion):
        if pion != Pion('x') and pion != Pion('o'):
            raise ValueError('Niepoprawny pion')
        self._wiersz = wiersz
        self._kolumna = kolumna
        self._pion = pion

    def wiersz(self) -> int:
        return self._wiersz

    def kolumna(self) -> int:
        return self._kolumna

    def pion(self) -> Pion:
        return self._pion


def test0():
    r1 = Ruch(0, 2, Pion('x'))
    r2 = Ruch(1, 2, Pion('o'))

    print(r1.wiersz() == 0)
    print(r2.wiersz() == 1)
    print(r1.kolumna() == 2)
    print(r2.kolumna() == 2)
    print(r1.pion() == Pion('x'))
    print(r2.pion() == Pion('o'))
    
def test1():
    r = Ruch(1, 2, 'Ala ma kota')   # powinno spowodować wyjątek
