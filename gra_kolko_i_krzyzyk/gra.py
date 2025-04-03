from wynik import Wynik
from plansza import Plansza
from pion import Pion
from gracz import Gracz
from interfejs_uzytkownika import InterfejsUzytkownika


class Gra:

    def __init__(self, 
                 gracz1: Gracz,
                 gracz2: Gracz,
                 pion_rozpoczynajacy: Pion,
                 interfejs_uzytkownika: InterfejsUzytkownika):
        if gracz1.pion() == Pion('.'):
            raise ValueError('Gracz 1 nie może mieć pionu pustego.')
        if gracz2.pion() == Pion('.'):
            raise ValueError('Gracz 2 nie może mieć pionu pustego.')
        if gracz1.pion() == gracz2.pion():
            raise ValueError('Gracze muszą mieć różne piony.')
        self._gracze = [gracz1, gracz2]
        if gracz1.pion() == pion_rozpoczynajacy:
            self._aktualny_gracz = gracz1
        else:
            self._aktualny_gracz = gracz2
        self._interfejs = interfejs_uzytkownika

    def _zmien_gracza(self):
        if self._aktualny_gracz == self._gracze[0]:
            self._aktualny_gracz = self._gracze[1]
        else:
            self._aktualny_gracz = self._gracze[0]

    def rozegraj(self) -> Wynik:
        plansza = Plansza()
        self._interfejs.pokaz_plansze(plansza)
        while not plansza.czy_koniec():
            ruch = self._aktualny_gracz.podaj_ruch(self._interfejs, plansza)
            czy_ok = plansza.czy_ruch_poprawny(ruch)
            if czy_ok:
                plansza.wykonaj_ruch(ruch)
                self._interfejs.pokaz_ruch(ruch)
                self._interfejs.pokaz_plansze(plansza)
                self._zmien_gracza()
            else:
                self._interfejs.wyswietl_komunikat_o_blednym_ruchu(ruch)
        wynik = plansza.wynik_partii()
        self._interfejs.pokaz_wynik(wynik)
        return wynik
