x=int(input("Ile w dzien"))
y=int(input("Ile w nocy"))
z=int(input("Co Ile"))
h=int(input("wysokosc"))
d=0
z_i=1
dzien=0
while d<h:
  d=d+x
  z_i=d//z
  if (d>=z_i*z) and (d-y<z*z_i):
    d=z_i*z
    z_i+=1
  else:
    d=d-y
  dzien+=1
print(dzien)