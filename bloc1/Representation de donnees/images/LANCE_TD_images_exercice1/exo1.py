#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""
TD Images - Exercice 1

date: 27/06/19
auteur: Jean-François LANCE

Manipulation des images en Python, dans les formats PBM, PGM et PPM.
Ces formats sont des formats bitmap (on code la couleur de chaque pixel),
écrits en ASCII pour être lisibles et modifiables facilement par un humain.

Question 1. voir les fichiers image1.pbm, image2.pgm et image3.ppm
"""


from es import *
from random import randint


def hauteur_image(image):
    """ Renvoie la hauteur de l'image passée
    en paramètre.

    Entrée: liste de liste
    Sortie: entier
    """
    # la hauteur de l'image est la longueur de
    # la liste principale
    return len(image)


def largeur_image(image):
    """ Renvoie la hauteur de l'image passée
    en paramètre.

    Entrée: liste de liste
    Sortie: entier
    """
    # la largeur de l'image est la longueur de chaque
    # sous liste
    # on renvoie la longueur de la 1ère
    return len(image[0])


def affiche_image(image):
    """ Affiche "proprement" la liste de liste
    correspondant à l'image passée en paramètre.

    Entrée: liste de liste
    Sortie: None
    """
    for i in range(hauteur_image(image)):
        print(image[i])
    print("\n")


def initialise(largeur, hauteur, couleur):
    """ Renvoie la matrice de dimensions largeur et hauteur
    dont le contenu est initialisé à la lavaleur couleur.

    Entrées: entier, entier, entier ou liste de 3 entiers
    Sortie: liste de liste
    """
    image = [[couleur for i in range(largeur)] for j in range(hauteur)]
    return image


def couleur_pixel(image, i, j):
    """ Renvoie la couleur du pixel de coordonnées (i, j)
    de l'image passée en paramètre.

    Entrées: liste de liste, entier, entier
    Sortie: entier
    """
    return image[j][i]


def change_pixel(image, i, j, couleur):
    """ Met le pixel de coordonnées (i, j) de l'image
    à la couleur passée en paramètre.

    Entrées: liste de liste, entier, entier, entier
    Sortie: Rien
    """
    image[j][i] = couleur
    return None


def rectangle(image, x0, y0, largeur, hauteur, couleur):
    """ Ajoute à l'image passée en paramètre un rectangle de la couleur fournie,
    de dimensions largeur x hauteur et dont le coin en haut à gauche
    est aux coordonnées (x0, y0).

    Modifie l'image passée en paramètre, ne fait pas de copie.

    Entrées: liste de liste, entier, entier, entier, entier, entier
    Sortie: Rien
    """
    # coordonnées du coin inférieur droit de l'image
    coin_image_x = largeur_image(image)
    coin_image_y = hauteur_image(image)

    # coordonnées du coin inférieur droit du rectangle
    coin_rect_x = x0 + largeur
    coin_rect_y = y0 + hauteur

    # le rectangle peut avoir des dimensions plus grandes
    # que celles de l'image originale
    # on prend le minimum des coordonnées
    coin_rect_x = min(coin_rect_x, coin_image_x)
    coin_rect_y = min(coin_rect_y, coin_image_y)

    # traitement des pixels
    for j in range(y0, coin_rect_y):
        for i in range(x0, coin_rect_x):
            change_pixel(image, i, j, couleur)

    return None


def rectangle_degrade(image, x0, y0, largeur, hauteur, couleur_bas, couleur_haut):
    """ Ajoute à l'image passée en paramètre un rectangle en dégradé de
    couleurs entre couleur_bas et couleur_haut, de dimensions largeur x hauteur
    et dont le coin en haut à gauche est aux coordonnées (x0, y0).

    Modifie l'image passée en paramètre, ne fait pas de copie.

    Entrées: liste de liste, entier, entier, entier, entier,
             liste d'entier, liste d'entier
    Sortie: Rien
    """
    # coordonnées du coin inférieur droit de l'image
    coin_image_x = largeur_image(image)
    coin_image_y = hauteur_image(image)

    # coordonnées du coin inférieur droit du rectangle
    coin_rect_x = x0 + largeur
    coin_rect_y = y0 + hauteur

    # le rectangle peut avoir des dimensions plus grandes
    # que celles de l'image originale
    # on prend le minimum des coordonnées
    coin_rect_x = min(coin_rect_x, coin_image_x)
    coin_rect_y = min(coin_rect_y, coin_image_y)

    # pas du dégradé de couleur:
    # il est fonction du nombre de couleurs utilisées et de la hauteur
    # rectangle
    pas_degrade = [(couleur_haut[i] - couleur_bas[i]+1)/(coin_rect_y+1)
                   for i in range(3)]

    # initialisation de la couleur de départ du dégradé
    # attention: on crée ici un nouvel objet liste car une simple
    # affectation (=) adresse le nouvel objet vers l'original
    couleur_en_cours = [couleur_bas[i] for i in range(3)]

    # traitement des pixels
    for j in range(y0, coin_rect_y):
        for i in range(x0, coin_rect_x):
            # on change la couleur du pixel en cours
            # attention: on arrondi les valeurs à l'unité
            # rmq: usage d'une compréhension de liste pour éviter l'usage
            #      d'une variable temporaire pour la couleur à attribuer
            change_pixel(image, i, j,
                         [round(couleur_en_cours[i]) for i in range(3)])

        # on passe au gradient de couleur suivant
        couleur_en_cours[0] += pas_degrade[0]
        couleur_en_cours[1] += pas_degrade[1]
        couleur_en_cours[2] += pas_degrade[2]

    return None


def disque(image, x0, y0, rayon, couleur):
    """ Ajoute à l'image passée en paramètre un disque centré au point de
    coordonnées (x0, y0), du rayon passé en paramètre et de la couleur fournie.

    Entrées: liste de liste, entier, entier, entier, liste d'entiers
    Sortie: Rien
    """
    # on liste les points se situant dans le cercle de centre (x0, y0)
    # et de rayon rayon
    points_du_disque = [(i, j) for i in range(largeur_image(image))
                               for j in range(hauteur_image(image))
                               if ((i-x0)**2 + (j-y0)**2) <= rayon**2]

    # on dessine les points
    for point in points_du_disque:
        change_pixel(image, point[0], point[1], couleur)

    return None


def cercle(image, x0, y0, rayon, couleur):
    """ Ajoute à l'image passée en paramètre un cercle centré au point de
    coordonnées (x0, y0), du rayon passé en paramètre et de la couleur fournie.

    Entrées: liste de liste, entier, entier, entier, liste d'entiers
    Sortie: Rien
    """
    # on liste les points se situant sur le cercle de centre (x0, y0)
    # et de rayon rayon
    # procédé insuffisant pour avoir un tracé du cercle plein donc
    # nécessité de prendre les points se situant entre deux cercles de rayons
    # sqrt(r^2 - r) et sqrt(r^2 + r)
    points_du_disque = [(i, j) for i in range(largeur_image(image))
                               for j in range(hauteur_image(image))
                               if (rayon**2-rayon < ((i-x0)**2 + (j-y0)**2) < rayon**2+rayon) ]

    # on dessine les points
    for point in points_du_disque:
        change_pixel(image, point[0], point[1], couleur)

    return None


def tableau_aleatoire(largeur, hauteur, max_elements):
    """ Renvoie un tableau de dimensions largeur x hauteur et contenant
    au maximum max_elements choisis aléatoirement parmi le rectangle,
    le rectangle_degrade, le disque et le cercle.

    Entrées: entier, entier, entier
    Sortie: liste de liste
    """
    # liste des fonctions de traçage
    fonctions_disponibles = ['rectangle', 'rectangle_degrade', 'disque', 'cercle']

    # initialise l'image de fond noir
    image = initialise(largeur, hauteur, [0, 0, 0])

    # quantité d'éléments à tracer
    nb_elements = randint(1, max_elements)

    for i in range(1, nb_elements+1):
        # choisissons une fonction
        # non utilisation de random.choice car usage de randint
        # explicitement demandé
        i_fn = randint(0, len(fonctions_disponibles)-1)

        if fonctions_disponibles[i_fn] == 'rectangle':
            x0, y0 = randint(0, largeur), randint(0, hauteur)

            # façon rapide et simple d'éciter d'avoir des figures
            # couvrant tout le tableau
            l, h = randint(0, (largeur)//4), randint(0, (hauteur)//4)

            couleur = [randint(1, 256), randint(1, 256), randint(1, 256)]

            rectangle(image, x0, y0, l, h, couleur)

        elif fonctions_disponibles[i_fn] == 'rectangle_degrade':
            x0, y0 = randint(0, largeur), randint(0, hauteur)

            # façon rapide et simple d'éciter d'avoir des figures
            # couvrant tout le tableau
            l, h = randint(0, (largeur)//4), randint(0, (hauteur)//4)

            couleur_bas = [randint(1, 256), randint(1, 256), randint(1, 256)]
            couleur_haut = [randint(1, 256), randint(1, 256), randint(1, 256)]

            rectangle_degrade(image, x0, y0, l, h, couleur_bas, couleur_haut)

        elif fonctions_disponibles[i_fn] == 'disque':
            x0, y0 = randint(0, largeur), randint(0, hauteur)

            # façon rapide et simple d'éciter d'avoir des figures
            # couvrant tout le tableau
            rayon = randint(0, min(largeur, hauteur)//4)

            couleur = [randint(1, 256), randint(1, 256), randint(1, 256)]

            disque(image, x0, y0, rayon, couleur)

        elif fonctions_disponibles[i_fn] == 'cercle':
            x0, y0 = randint(0, largeur), randint(0, hauteur)

            # façon rapide et simple d'éciter d'avoir des figures
            # couvrant tout le tableau
            rayon = randint(0, min(largeur, hauteur)//4)

            couleur = [randint(1, 256), randint(1, 256), randint(1, 256)]

            cercle(image, x0, y0, rayon, couleur)

    return image


#==========================================================
# TESTS
#==========================================================

print("test1: Initialise une image")
c0 = 4
c1 = [0,0,0]
test1 = initialise(1000, 1000, c1)
# affiche_image(test1)

print("test1: Modifie la couleur d'un pixel")
c2 = [7, 7, 7]
change_pixel(test1, 40, 40, c2)
# affiche_image(test1)

print("test1: Ajoute un rectangle")
c3 = [5, 5, 2]
rectangle(test1, 500, 500, 200, 450, c3)
# affiche_image(test1)

print("test1: Ajoute un rectangle dégradé")
couleur_bas = [1, 0, 3]
couleur_haut = [5, 7, 9]
rectangle_degrade(test1, 200, 600, 150, 300, couleur_bas, couleur_haut)
# affiche_image(test1)

print("test1: Ajoute un disque")
c4 = [7, 5, 1]
disque(test1, 100, 100, 200, c4)
# affiche_image(test1)

print("test1: Ajoute un cercle")
c4 = [9, 2, 9]
cercle(test1, 500, 30, 100, c4)
# affiche_image(test1)

print("Sauvegarde de l'image test1\n")
sauver_image(test1, 'PPM', 'test1', 9)

print("test2: Créé un tableau")
test2 = tableau_aleatoire(1280, 720, 100)
print("Sauvegarde de l'image test2")
sauver_image(test2, 'PPM', 'test2')
