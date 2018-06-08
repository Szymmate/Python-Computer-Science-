class Node:
 
    def __init__(self, nazwisko, ocena):
        self.nazwisko = nazwisko
        self.ocena = ocena
        self.next = None
        self.prev = None
 
    def __str__(self):
        return str(self.nazwisko)
        
    def __int__(self):
        return int(self.ocena)
        
class Lista_dwukierunkowa:
 
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
 
    def dodaj_na_koncu(self, nazwisko, ocena):
        n = Node(nazwisko, ocena)
        n.next = None
        n.prev = self.tail
        self.tail = n
        self.size +=1
        if not self.head:
            self.head = n
        else:  
            n.prev.next = n

    def dodaj_na_poczatku(self, nazwisko, ocena):
        n = Node(nazwisko, ocena)
        n.prev = None
        n.next = self.head
        self.head = n
        self.size +=1
        if not self.tail:
            self.tail = n      
        else:  
            n.next.prev = n
            
    def wypisz_od_poczatku(self):
          n=self.head
          while n:
              print (n.nazwisko, n.ocena)
              n=n.next
              
    def wypisz_od_konca(self):
        n = self.tail
        while n:
            print (n.nazwisko, n.ocena)
            n = n.prev
            
    def usun_od_poczatku(self):
        n=self.head.next
        n.prev = None
        self.head.next=None
        self.head=n
        self.size -=1
        
    def usun_na_koncu(self):
        n=self.tail.prev
        n.next = None
        self.tail.prev=None
        self.tail=n
        self.size -=1
    
    def dodaj_na_k(self, nazwisko, ocena):
        k=int(input("Podaj na ktorym miejscu ma byc dodany wyraz\n"))
        c=int(self.size)
        if ((k-1)>c) or k<1:
            print ("Blad wyraz mial byc dodany poza tablica")
            return
        if (k==1):
            Lista_dwukierunkowa.dodaj_na_poczatku(self, nazwisko, ocena)
            return
        if ((k-1)==c):
            Lista_dwukierunkowa.dodaj_na_koncu(self, nazwisko, ocena)
            return
        else:
            p=1
            n=self.head
            while (p<k):
                n=n.next
                p+=1
            c=Node(nazwisko, ocena)
            c.next=n
            c.prev=n.prev
            n.prev.next=c
            n.prev=c
            self.size+=1
    def wyszukaj_najwieksza_ocena(self):
        n=self.head
        b=self.head
        while n:
            if n.ocena>=b.ocena:
                b=n
            n=n.next
        print(b.nazwisko, b.ocena)
        
 
ll = Lista_dwukierunkowa()

ll.dodaj_na_poczatku("Mickiewicz", 10)
ll.dodaj_na_poczatku("Slowacki", 14)
ll.dodaj_na_poczatku("Krasinski", 15)
ll.dodaj_na_poczatku ("Norwid", 11)
ll.dodaj_na_koncu("Herbert", 12)
ll.dodaj_na_koncu("Prus", 10)
ll.dodaj_na_koncu ("Lesmian", 9)
ll.dodaj_na_k("Nalkowska", 16)
ll.usun_na_koncu()
ll.usun_od_poczatku()
ll.wypisz_od_poczatku()
ll.wypisz_od_konca()
ll.wyszukaj_najwieksza_ocena()