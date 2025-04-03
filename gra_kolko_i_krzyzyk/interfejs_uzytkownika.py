from plansza import Plansza
from ruch import Ruch
from wynik import Wynik
from pion import Pion


class InterfejsUzytkownika:

    def pokaz_plansze(self, plansza: Plansza):
        print(' %s | %s | %s ' % (
                plansza(0, 0), plansza(0, 1), plansza(0, 2)))
        print('---+---+---')
        print(' %s | %s | %s ' % (
                plansza(1, 0), plansza(1, 1), plansza(1, 2)))
        print('---+---+---')
        print(' %s | %s | %s ' % (
                plansza(2, 0), plansza(2, 1), plansza(2, 2)))

    def pokaz_ruch(self, ruch: Ruch):
        print('Postawiono %s na polu (%s, %s).' % (
                ruch.pion(),
                ruch.wiersz(),
                ruch.kolumna()
                ))

    def wyswietl_komunikat_o_blednym_ruchu(self, ruch: Ruch):
        print('Ruch %s na polu(%s, %s) jest niemozliwy!' % (
                ruch.pion(),
                ruch.wiersz(),
                ruch.kolumna()
                ))

    def pokaz_wynik(self, wynik: Wynik):
        if wynik == Wynik('.'):
            print('Remis')
        else:
            print('Wygrana %s!' % (wynik,))

    def pobierz_ruch(self, pion: Pion, opis_gracz: str) -> Ruch:
        print('%s (%s), Twoj ruch!' % (opis_gracz, pion))
        w = int(input('  podaj wiersz [0, 1, 2]: '))
        k = int(input('  podaj kolumne [0, 1, 2]: '))
        return Ruch(w, k, pion)


def test1():
    InterfejsUzytkownika().pokaz_ruch(Ruch(1, 2, Pion('x')))

def test2():
    iu = InterfejsUzytkownika()
    iu.pokaz_wynik(Wynik('.'))
    iu.pokaz_wynik(Wynik('x'))
    iu.pokaz_wynik(Wynik('o'))