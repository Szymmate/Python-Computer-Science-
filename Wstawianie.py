import random
random.seed()
losowana = random.randrange(50)  

A0=[]
x=0
while x<1000:
    A0.append(random.randrange(1000))
    x=x+1


def wstawianie(tab):
    for i in range(1,len(tab)):
        klucz=tab[i]
        j=i-1
        while j>=0 and tab[j]>klucz:
            tab[j+1]= tab[j]
            j=j-1
            tab[j+1]=klucz
wstawianie(A0)
