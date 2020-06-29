#!/usr/bin/env python3
# -*- coding: utf8 -*-

from random import randint
from time import time

def generate_random_tab(taille, max):
    """ Retrourne un tableau de taille taille
    et dont l'intervalle des valeurs est [0, max]
    """
    # version comprehension de liste
    result = [randint(0, max) for i in range(taille)]

    # version iterative
    # for i in range(taille):
    #     result.append(randint(0, max))

    return result


def algo1(element, tableau):
    """ Recherche l'élément element dans le
    tableau trié tableau.

    Entrées: element, tableau
    Sortie: indice de l'élément, s'il y est
            ou -1, si non
    """
    for i in range(len(tableau)-1):
        if element == tableau[i]:
            return i
    return -1


def algo2(element, tableau):
    """ Recherche par dichotomie l'élément element
    dans le tableau trié tableau.

    Entrées: element, tableau
    Sortie: True si l'élément est présent, False sinon
    """
    # le tableau ne contient qu'un élément
    if len(tableau) == 1:
        return element == tableau[0]
    
    # le tableau contient plus d'un élement, on le divise
    tableau1 = tableau[:(len(tableau)//2)]
    tableau2 = tableau[(len(tableau)//2):]

    # appels récursifs
    if element < tableau[(len(tableau)//2)]:
        # print("Recherche 1ère moitié: ", tableau1)
        return algo2(element, tableau1)
    else:
        # print("Recherche 2ème moitié: ", tableau2)
        return algo2(element, tableau2)


def algo3(element, tableau, a, b):
    """ Recherche par dichotomie l'élément element
    dans le tableau trié tableau.

    Entrées: element, tableau, borne inf, borne sup
    Sortie: indice de l'élément
    """
    # si les bornes inf et sup sont égales
    # le tableau ne contient qu'une valeur
    if a == b:
        # si l'élément cherché vaut la valeur dans le tableau
        if element == tableau[a]:
            # on retourne l'indice
            return a
        else:
            # sinon -1
            return -1
    # sinon a < b
    else:
        # on prend l'indice central
        m = (a+b)//2
        # l'élément est-il dans la 1ère moitié du tableau ?
        if element == tableau[m]:
            return m
        if element < tableau[m]:
            # print("Recherche: {} dans {} entre {} et {}". format(element, tableau, a, m))
            return algo3(element, tableau, a, m)
        else:
            # print("Recherche: {} dans {} entre {} et {}". format(element, tableau, m+1, b))
            return algo3(element, tableau, m+1, b)
    


# generation d'un tableau d'entiers aleatoires
taille = 1000
max = 1000
test_tab = generate_random_tab(taille, max)
# print("Tableau de taille {} et de max {}: {}\n". format(taille, max, test_tab))

# trie du tableau
test_tab.sort()
print("Tableau trié: {}\n".format(test_tab))

# appel de l'algo1
t0=time()
print("Appel de algo1: {}\n".format(algo1(11, test_tab)))
t1=time()

print("Algo1 - Tps: ", t1-t0)

# appel de l'algo2
t0=time()
print("Appel de algo2: {}\n".format(algo2(11, test_tab)))
t1=time()

print("Algo2 - Tps: ", t1-t0)

# appel de l'algo3
t0=time()
print("Appel de algo3: {}\n".format(algo3(11, test_tab, 0, len(test_tab)-1)))
t1=time()

print("Algo3 - Tps: ", t1-t0)