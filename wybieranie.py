import random
random.seed()
losowana = random.randrange(50)  
A0=[]
x=0
while x<1000:
    A0.append(random.randrange(1000))
    x=x+1

def wybieranie(tab):
    i=0
    while (i <len(tab)):
        a=i
        j=i+1
        while (j<len(tab)):
            if tab[j]<=tab[a]:
                a=j
            j=j+1
        tab[a],tab[i]=tab[i],tab[a]
        i=i+1

wybieranie (A0)