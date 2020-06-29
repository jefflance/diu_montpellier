def AfficheGraphe(n,CoordSommet,Aretes,nomfich):
    with open(nomfich+".ps",'w') as f:
        f.write("%!PS-Adobe-3.0\n")
        f.write("%%BoundingBox: 0 0 612 792\n")
        f.write("\n") 
        for i in range(0,n):
            f.write(str(CoordSommet[i][0]))
            f.write(" ") 
            f.write(str(CoordSommet[i][1])) 
            f.write(" 3 0 360 arc\n")
            f.write("0 setgray\n")
            f.write("fill\n")
            f.write("stroke\n")
            f.write("\n")    
        for i in range(len(Aretes)):
            f.write(str(CoordSommet[Aretes[i][0]][0]))
            f.write(" ")
            f.write(str(CoordSommet[Aretes[i][0]][1]))
            f.write(" moveto\n")
            f.write(str(CoordSommet[Aretes[i][1]][0]))
            f.write(" ")
            f.write(str(CoordSommet[Aretes[i][1]][1]))
            f.write(" lineto\n")
            f.write("stroke\n")

#Graphe modélisant le problème du village embourbé
G=[[0,1,4],[0,2,4],[1,3,3],[1,5,2],
   [0,3,2],[0,4,3],[4,2,3],[2,7,2],
   [3,5,4],[3,4,4],[2,9,4],[9,7,3],
   [4,9,2],[3,6,4],[4,6,3],[5,6,5],
   [5,8,4],[8,6,3],[6,9,3],[8,9,5]
]

Coordonnees=[[250,700],[150,680],[350,680],[200,600],[300,570],[120,570],[220,500],[400,500],[160,400],[300,400]]

AfficheGraphe(10,Coordonnees,G,"graphe_initial")
