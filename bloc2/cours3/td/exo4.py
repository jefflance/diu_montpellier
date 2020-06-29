n = int(input("Entrer n: "))

def affiche(n):
    if n > 1:
        print("Toujours pas fini...")
        affiche(n/2)
        affiche(n/2)

affiche(n)