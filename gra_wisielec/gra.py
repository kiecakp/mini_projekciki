from plansza import Plansza
from haslo import Haslo
from interfejs_uzytkownika import InterfejsUzytkownika

class Gra:
    
    def rozegraj(self):
        pobrane_haslo = input('Podaj zagadnienie: ')
        kategoria = input('Podaj kategorie zagadnienia: ')
        rozgrywka = Plansza(pobrane_haslo)
        print(rozgrywka.lista_pol())
        print('')
        while rozgrywka.czy_koniec() != True:
            print('kategoria: ' + kategoria)
            rozgrywka.pobierz_litere()
            rozgrywka.bledna_odpowiedz()
            rozgrywka.bledne_odpowiedz_rysunek()
            print('')
            rozgrywka.wpisz_odgadnione_litery_w_pola()
            if rozgrywka.czy_litera_odgadniona() == True:
                rozgrywka.komunikat_o_powtorzeniu_litery()
                rozgrywka.tworzenie_hasla() 