class Znak():
    def __init__(self, rodzaj):
        self.rodzaj = rodzaj
        self.next = None

class ONP():
    def __init__(self):
        self.head = None
        self.rozmiar = 0

    def dodawanie(self, rodzaj):
        if self.head == None:
            nowy = Znak(rodzaj)
            self.head = nowy
            self.rozmiar += 1
        else:
            nowy = Znak(rodzaj)
            nowy.next = self.head
            self.head = nowy
            self.rozmiar += 1

    def usuwanie(self):
        self.head = self.head.next
        self.rozmiar -= 1

wyrazenie= [3,3,'+']
lista = ONP()

for i in wyrazenie:
    if type(i)==int:
        lista.dodawanie(int(i))
    elif i == '*':
        n=lista.head.next
        n.rodzaj=n.rodzaj*lista.head.rodzaj
        lista.usuwanie()
    elif i == '+':
        n=lista.head.next
        n.rodzaj=n.rodzaj+lista.head.rodzaj
        lista.usuwanie()
    elif i == '-':
        n=lista.head.next
        n.rodzaj=n.rodzaj-lista.head.rodzaj
        lista.usuwanie()
    elif i == '/':
        n=lista.head.next
        n.rodzaj=n.rodzaj/lista.head.rodzaj
        lista.usuwanie()
print(lista.head.rodzaj)