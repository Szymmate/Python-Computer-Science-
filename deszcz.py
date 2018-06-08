import random
import os
import time
x=int(input("podaj wymiary"))
random.seed()
t=[]
for i in range(100000):
	w=random.randrange(x)
	t.append(w)
if(len(t)>x):
	t.pop(0)
for i in range(0,x):
	for j in range(0,x):
		if(i<len(t) and j==t[len(t)-1-i]):
			print('*')
		else:
			print('_')
		print(" ")
time.sleep(0.1)
os.system('clear')
    