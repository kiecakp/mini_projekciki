import random as R

from interfejs_uzytkownika import InterfejsUzytkownika
from pion import Pion
from plansza import Plansza
from ruch import Ruch


class Gracz:
    def __init__(self, pion: Pion, nazwa: str):
        self._pion = pion
        self._nazwa = nazwa

    def pion(self) -> Pion:
        return self._pion
        
    def nazwa(self) -> str:
        return self._nazwa
    
    def podaj_ruch(self, interfejs: InterfejsUzytkownika, plansza: Plansza) -> Ruch:
        raise NotImplementedError

    
class GraczCzlowiek(Gracz):
    
    def podaj_ruch(self, interfejs: InterfejsUzytkownika, plansza: Plansza) -> Ruch:
        return interfejs.pobierz_ruch(self._pion, self._nazwa)


class GraczKomputer(Gracz):
    
    def podaj_ruch(self, interfejs: InterfejsUzytkownika, plansza: Plansza) -> Ruch:
        while True:
            w = R.randint(0, 2)
            k = R.randint(0, 2)
            r = Ruch(w, k, self._pion)
            if plansza.czy_ruch_poprawny(r):
                return r

    
