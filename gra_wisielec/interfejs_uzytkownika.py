from haslo import Haslo

class InterfejsUzytkownika:      
    
    def pobierz_litere(self)    -> str:
        self._podana_litera = str(input('Podaj kolejna litere: '))
        return self._podana_litera
    
    def powtorzenia_liter(self):
        self._powtorzenia_litery = 0
        for litera in self._zagadnienie:
            if self._podana_litera == litera:
                self._powtorzenia_litery += 1    
        
    def komunikat_o_powtorzeniu_litery(self):
        self.powtorzenia_liter()
        if self._powtorzenia_litery == 1:
            print('litera ' + self._podana_litera + 
                          ' wystepuje w hasle tylko 1 raz')
        elif self._powtorzenia_litery > 1:
            print('litera ' + self._podana_litera + 
                          ' powtarza sie w hasle ' + 
                          str(self._powtorzenia_litery) + ' razy')
            
            
            

           