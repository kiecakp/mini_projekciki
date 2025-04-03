from haslo import Haslo
from interfejs_uzytkownika import InterfejsUzytkownika

class Plansza(Haslo, InterfejsUzytkownika):        
            
    def lista_pol(self):
        for litery in self._zagadnienie:
            if len(self._lista_z_pol) < len(self._zagadnienie):
                self._lista_z_pol.append('___')      
        return ' '.join(self._lista_z_pol)   

    def czy_litera_odgadniona(self) -> bool:
        if self._podana_litera in self._zagadnienie:
            print('')
            print('zgadles litere')
            return True
        else:
            pass    
    
        
    def tworzenie_hasla(self)   -> str:
        for litera in self._zagadnienie:
            if self._podana_litera == litera:
                self._ilosc_odgadnionych_liter += 1
                

                
    def wpisz_odgadnione_litery_w_pola(self):
        self.lista_pol()
        if self._podana_litera in self._zagadnienie:
            self.lista_liter_hasla()
            self.powtorzenia_liter()
            if self._powtorzenia_litery > 1:
                lista_miejsc = []
                for litera in self._lista_z_hasla:
                    if self._podana_litera == litera:
                        while self._powtorzenia_litery != 0:
                            odgadnione_miejsce = (self._lista_z_hasla.index
                                                  (self._podana_litera))
                            lista_pomocnicza = self._lista_z_hasla
                            lista_pomocnicza[odgadnione_miejsce] = '.'
                            self._lista_z_pol[odgadnione_miejsce] = (
                                                        self._podana_litera)
                            self._powtorzenia_litery -= 1
            else:
                odgadnione_miejsce = (self._lista_z_hasla.index
                                      (self._podana_litera))
                self._lista_z_pol[odgadnione_miejsce] = self._podana_litera
            print(' '.join(self._lista_z_pol))
        
        
    def czy_koniec(self)    -> bool:
        odgadnione_haslo = ' '.join(self._lista_z_pol)
        if odgadnione_haslo.replace(' ', '') == self._zagadnienie:
            print('KONIEC')
            print('WYGRALES')
            print('Haslo to: ' + odgadnione_haslo.replace(' ', ''))
            return True
        elif self._bledna_odp == 11:
            print('KONIEC')
            print('PRZEGRALES')
            print('Haslo to: ' + self._zagadnienie)
            return True
            
        
        

def test0():
    p1 = Plansza('kot')
    p2 = Plansza('statek')
    p3 = Plansza('czarny kot')
    print(p1.lista_pol())
    print(p2.lista_pol())
    print(p3.lista_pol())   #problem ze spacjami, zobacz pozniej
    
def test1():
    p1 = Plansza('statek')
    while p1.czy_koniec() != True:
        p1.pobierz_litere()
        if p1.czy_litera_odgadniona() == True:
            p1.komunikat_o_powtorzeniu_litery()
            p1.tworzenie_hasla()
      
def test2():
    p1 = Plansza('kot')
    p2 = Plansza('statek')
    print(p1.lista_z_pol())
    print(p2.lista_z_pol())
    
def test3():
    p1 = Plansza('kot')
    while p1.czy_koniec() != True:
        p1.pobierz_litere()
        p1.wpisz_odgadnione_litery_w_pola()
    
def test4():
    p1 = Plansza('statek')
    print(p1.lista_pol())
    while p1.czy_koniec() != True:
        p1.pobierz_litere()
        p1.wpisz_odgadnione_litery_w_pola()
        if p1.czy_litera_odgadniona() == True:
            p1.komunikat_o_powtorzeniu_litery()
            p1.tworzenie_hasla()
            
def test5():
    p1 = Plansza('kot')
    while p1.czy_koniec() != True:
        p1.pobierz_litere()
        p1.bledna_odpowiedz()
        p1.bledne_odpowiedz_rysunek()
    
    
#test0()
#test1()
#test2()
#test3()
#test4()
#test5()