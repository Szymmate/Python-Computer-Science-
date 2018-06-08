import random
random.seed()
losowana = random.randrange(50)  

A0=[]
x=0
while x<1000:
    A0.append(random.randrange(1000))
    x=x+1
def quicksort(tab, poczatek, koniec):
    if poczatek<koniec:
   
        punkt=podzial(tab,poczatek,koniec)
       
        quicksort(tab,poczatek,punkt-1)
        quicksort(tab,punkt+1,koniec)
    return tab
    
def podzial(tab, poczatek, koniec):
    punkt=tab[poczatek]
    lewy=poczatek+1
    prawy=koniec
    done=False
    while not done:
        while lewy<=prawy and tab[lewy]<=punkt:
            lewy=lewy+1
        while tab[prawy]>=punkt and prawy>=lewy:
            prawy=prawy-1
        if prawy<lewy:
            done=True
        else:
            tab[lewy],tab[prawy]=tab[prawy],tab[lewy]

    tab[poczatek],tab[prawy]=tab[prawy],tab[poczatek]
    return prawy

quicksort (A0,0,len(A0)-1)
print(A0)