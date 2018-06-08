import random
random.seed()
losowana = random.randrange(50)  
A0=[]
x=0
while x<1000:
    A0.append(random.randrange(1000))
    x=x+1


def babelkowe(tab):
    a=len(tab)
    while a>0:
        for i in range(0,a-1):
            if (tab[i]>tab[i+1]):
                tab[i],tab[i+1]=tab[i+1],tab[i]
        a=a-1
babelkowe(A0)