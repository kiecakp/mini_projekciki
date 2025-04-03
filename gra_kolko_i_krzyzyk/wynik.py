from pion import Pion

class Wynik(Pion):
    pass

def test0():
    print(Wynik('x').wyglad() == 'x')
    print(Wynik('o').wyglad() == 'o')
    print(Wynik('.').wyglad() == '.')

def test1():
    p1 = Wynik('x')
    p2 = Wynik('o')
    p3 = Wynik('x')
    print(p1 != p2)
    print(p2 != p3)
    print(p1 == p3)
    print((p1 != p3) == False)
    
def test2():
    p = Wynik('#')   # spodziewamy sie bledu
