sys1=int(input("Podaj system z "))
sys2=int(input("Podaj system na "))
x=str(input("Podaj liczbe w systemie" + str(sys1)))
y=[]
z=''
suma=0
i=0
c=0
while i <len(x):
    suma=suma*sys1+int(x[i])
    i+=1
print("Liczba w systemie 10 wynosi\n"+str(suma))

while suma//sys2>0:
  y.append(suma%sys2)
  suma=suma//sys2
y.append(suma%sys2)
y.reverse()

while c<len(y):
  z+=str(y[c])
  c+=1
print("Liczba wynosi\n" +z)