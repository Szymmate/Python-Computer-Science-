class Node():
    def __init__(self, nazwa, priorytet):
        self.nazwa = nazwa
        self.priorytet=priorytet
        self.next = None

class Lista():
    def __init__(self):
        self.head = None
        self.rozmiar = 0

    def dodawanie(self, nazwa, priorytet):
        if self.head == None:
            nowy = Node(nazwa, priorytet)
            self.head = nowy
            self.rozmiar += 1
        else:
            nowy = Node(nazwa, priorytet)
            if nowy.priorytet>=self.head.priorytet:
              nowy.next = self.head
              self.head = nowy
              self.rozmiar += 1
            elif self.head.next==None:
              self.head.next=nowy
            else:
              n=self.head
              while n.next:
                if nowy.priorytet>=n.next.priorytet:
                  break
                n=n.next
              tmp=n.next
              n.next=nowy
              nowy.next=tmp
            

    def usuwanie(self):
        self.head = self.head.next
        self.rozmiar -= 1
    def printf(self):
        n=self.head
        while n!=None:
          print(n.nazwa, n.priorytet)
          n=n.next
ll=Lista()
ll.dodawanie ("Pranie", 12)
ll.dodawanie ("Prasowanie", 10)
ll.dodawanie ("Prasowanie", 11)
ll.dodawanie ("Prasowanie", 19)
ll.dodawanie ("Prasowanie", 9)
ll.printf()