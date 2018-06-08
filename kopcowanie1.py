import random
random.seed()
losowana = random.randrange(50)  

A0=[]
x=0
while x<1000:
    A0.append(random.randrange(1000))
    x=x+1
def kopcowanie(tab):
    def kopiec(tab):
        start=(len(tab)-2)//2
        while start>=0:
            funkcja(tab, start, len(tab) - 1)
            start=start-1

    def funkcja(tab, start, koniec):
        rodzic=start
        while (rodzic*2+1<=koniec):
            potomek=rodzic*2+1
            if potomek+1<=koniec and tab[potomek]<tab[potomek+1]:
                potomek=potomek+1
            if potomek<=koniec and tab[rodzic]<tab[potomek]:
                tab[rodzic],tab[potomek]=tab[potomek],tab[rodzic]
                rodzic=potomek
            else:
                return

    kopiec(tab)
    koniec=len(tab)-1
    while koniec>0:
        tab[koniec],tab[0]=tab[0],tab[koniec]
        funkcja(tab,0,koniec-1)
        koniec=koniec-1

    

kopcowanie(A0)
