import time
import matplotlib.pyplot as plt

def AlgoSansTableau(x,n):
    y=x
    for i in range(1, n):
        y=y*x
    return y

def AlgoDetC(x,n):
    if n==1:
        return x
    else :
        z=AlgoDetC(x,n//2)
        if(n%2==0): 
            return z*z
        else:
            return x*z*z
    
#Valeurs de n choisies    
abscisses = [n for n in range(1,100)]
#Temps de calcul
tps1 = []
for n in range(1,100):
    t=time.time()
    AlgoSansTableau(2,n)
    tps1.append(time.time()-t)
tps2 = []
for n in range(1,100):
    t=time.time()
    AlgoDetC(2,n)
    tps2.append(time.time()-t)
#Tracé
plt.plot(abscisses, tps1)
plt.plot(abscisses, tps2)
plt.show()