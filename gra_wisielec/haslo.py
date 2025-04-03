class Haslo:
    
    def __init__(self, zagadnienie: str):
        self._zagadnienie = zagadnienie
        self._ilosc_odgadnionych_liter = 0
        self._lista_z_pol = []
        self._bledna_odp = 0
        
    def ilosc_liter(self):
        return len(self._zagadnienie)
    
    def lista_liter_hasla(self):
        self._lista_z_hasla = list(self._zagadnienie)
        return self._lista_z_hasla
    
    def bledna_odpowiedz(self):
        if self._podana_litera not in self._zagadnienie:
            self._bledna_odp += 1
        return self._bledna_odp
        
    def wyswietl_aktualne_odgadnienia(self):
        print('')
        print(' '.join(self._lista_z_pol))
        
    def bledne_odpowiedz_rysunek(self):
        if self._bledna_odp == 1:
            print('\n' * 5)
            print('___________')
            self.wyswietl_aktualne_odgadnienia()
        elif self._bledna_odp == 2:
            print('')
            for i in range(4):
                print('     |')
            print('_____|_____')
            self.wyswietl_aktualne_odgadnienia()
        elif self._bledna_odp == 3:
            print('      _______')
            for i in range(4):
                print('     |')
            print('_____|_____')
            self.wyswietl_aktualne_odgadnienia()
        elif self._bledna_odp == 4:
            print('      _______')
            print('     |/')
            for i in range(3):
                print('     |')
            print('_____|_____')
            self.wyswietl_aktualne_odgadnienia()
        elif self._bledna_odp == 5:
            print('      _______')
            print('     |/     | ')
            print('     |')
            print('     |')
            print('     |')
            print('_____|_____')
            self.wyswietl_aktualne_odgadnienia()
        elif self._bledna_odp == 6:
            print('      _______')
            print('     |/     | ')
            print('     |      O')
            print('     |')
            print('     |')
            print('_____|_____')
            self.wyswietl_aktualne_odgadnienia()
        elif self._bledna_odp == 7:
            print('      _______')
            print('     |/     | ')
            print('     |      O')
            print('     |      |')
            print('     |')
            print('_____|_____')
            self.wyswietl_aktualne_odgadnienia()
        elif self._bledna_odp == 8:
            print('      _______')
            print('     |/     | ')
            print('     |      O')
            print('     |      |')
            print('     |     /')
            print('_____|_____')
            self.wyswietl_aktualne_odgadnienia()
        elif self._bledna_odp == 9:
            print('      _______')
            print('     |/     | ')
            print('     |      O')
            print('     |      |')
            print('     |     / )')
            print('_____|_____')
            self.wyswietl_aktualne_odgadnienia()
        elif self._bledna_odp == 10:
            print('      _______')
            print('     |/     | ')
            print('     |      O')
            print('     |     /|')
            print('     |     / )')
            print('_____|_____')
            self.wyswietl_aktualne_odgadnienia()
        elif self._bledna_odp == 11:
            print('      _______')
            print('     |/     | ')
            print('     |      O')
            print('     |     /|)')
            print('     |     / )')
            print('_____|_____')
        
    def projekt_wisielca(self):
        print('      _______')
        print('     |/     | ')
        print('     |      O')
        print('     |     /|)')
        print('     |     / )')
        print('_____|_____')

    
def test0():
    z1 = Haslo('kot')
    z2 = Haslo('dziewczyna')
    z3 = Haslo('statek')
    print(z1.ilosc_liter() == 3)
    print(z2.ilosc_liter() == 10)
    print(z3.ilosc_liter() == 6)
    
def test1():
    z1 = Haslo('kot')
    z2 = Haslo('dziewczyna')
    z3 = Haslo('statek')
    print(z1.lista_liter_hasla())
    print(z2.lista_liter_hasla())
    print(z3.lista_liter_hasla())
def test2():
    z1 = Haslo('kot')
    z1.projekt_wisielca()


#test0()
#test1() 
#test2()
