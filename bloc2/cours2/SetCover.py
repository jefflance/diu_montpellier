from random import *

def AfficheMaisons(Maison,n):
    with open("Maison.ps", 'w') as f:
        f.write("%!PS-Adobe-3.0\n")
        f.write("%%BoundingBox: 0 0 612 792\n")
        f.write("\n") 
        for i in range(0,n):
            f.write(str(Maison[i][0]))
            f.write(" ") 
            f.write(str(Maison[i][1])) 
            f.write(" 3 0 360 arc\n")
            f.write("0 setgray\n")
            f.write("fill\n")
            f.write("stroke\n")
            f.write("\n")    

def AfficheEmetteurs(Maison,Emetteur,n):
    with open("Emetteur.ps", 'w') as f:
        f.write("%!PS-Adobe-3.0\n")
        f.write("%%BoundingBox: 0 0 612 792\n")
        f.write("\n") 

        for i in range(0,n):#affichage des disques couvrants
            if Emetteur[i]==1: 
                f.write(str(Maison[i][0]))
                f.write(" ")
                f.write(str(Maison[i][1]))
                f.write(" 100 0 360 arc\n")
                f.write("0.8 setgray\n")
                f.write("fill\n")
                f.write("stroke\n")
                f.write("\n")


        for i in range(0,n): #Affichage des maisons
             f.write(str(Maison[i][0]))
             f.write(" ") 
             f.write(str(Maison[i][1])) 
             f.write(" 3 0 360 arc\n")
             if Emetteur[i]==1:
                f.write("1 0 0 setrgbcolor\n")
             else:
                f.write(" 0 setgray\n")
             f.write("fill\n")
             f.write("stroke\n")
             f.write("\n")


def GenererMaisons(Maison,n):
    for i in range(0,n):
        Maison.append([10+randint(0,592),10+randint(0,772)])


n=50 #nombre de maisons
Maison=[] #contient les coordonnees cartesiennes des maisons dans [0,612]x[0,792]
GenererMaisons(Maison,n)
print(Maison)
AfficheMaisons(Maison,n)
Emetteur=[0]*n #Emetteur[i]=1 ssi on place un émetteur sur la maison i
Emetteur[3]=1 #on choisit quelques émetteurs aléatoirement...
Emetteur[14]=1
Emetteur[22]=1
Emetteur[43]=1
AfficheEmetteurs(Maison,Emetteur,n)
