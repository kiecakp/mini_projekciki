class Pion:
    def __init__(self, wyglad:str):  #wyglad: 'x', 'o', '.'
        if wyglad not in {'x', 'o', '.'}:
            raise ValueError('Podany wyglad nie jest poprawny')
        self._wyglad = wyglad

    def wyglad(self) -> str:  # 'x', 'o', '.'
        return self._wyglad

    def __eq__(self, other) -> bool:
        return self._wyglad == other._wyglad

    def __str__(self) -> str:
        if self._wyglad == '.':
            return ' '
        return self._wyglad


def test0():
    print(Pion('x').wyglad() == 'x')
    print(Pion('o').wyglad() == 'o')
    print(Pion('.').wyglad() == '.')

def test1():
    p1 = Pion('x')
    p2 = Pion('o')
    p3 = Pion('x')
    print(p1 != p2)
    print(p2 != p3)
    print(p1 == p3)
    print((p1 != p3) == False)
    
def test2():
    p = Pion('#')   # spodziewamy sie bledu
