from random import *
import operator

def CoursAuHasard(T,n):
    for i in range(0,n):
        x=randint(1,90)
        T.append([x,x+randint(1,10)])

T=[]
CoursAuHasard(T,12)
print("Cours générés au hasard: \n",T)
T=sorted(T, key=operator.itemgetter(1))
print("Cours triés par dates de fin croissantes: \n",T)