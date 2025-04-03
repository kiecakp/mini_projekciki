from gracz import GraczCzlowiek, GraczKomputer
from interfejs_uzytkownika import InterfejsUzytkownika
from pion import Pion
from gra import Gra


def main():
    gracz1 = GraczCzlowiek(Pion('x'), input('Kto gra krzyzykiem? '))
    #gracz2 = GraczCzlowiek(Pion('o'), input('Kto gra kolkiem? '))
    gracz2 = GraczKomputer(Pion('o'), print('ROBOT!'))
    interfejs = InterfejsUzytkownika()
    gra = Gra(gracz1, gracz2, Pion('x'), interfejs)
    gra.rozegraj()


main()
