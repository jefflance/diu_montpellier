#!/usr/bin/env python3

"""
Exercice 5

Date: 20/08/19
Auteur: Jeff LANCE <jeff.lance@mala.fr>
"""


import unittest
import random


def randintlist(n):
    """
    Renvoie une liste aléatoire de n entiers avec répétition possible.
    """
    list = []
    
    for i in range(n):
        list.append(random.randint(0, n//6))
    
    return list


def occurences(x, T):
    """
    Renvoie le nombre d'occurences de x dans le tableau d'entiers T.
    
    Entrées:
        - x: entier à comptabiliser
        - T: tableau d'entiers
    Sortie:
        nombre entier d'occurences de x dans T
    """
    c = 0
    n = len(T)
    
    for i in range(n):
        if T[i] == x:
            c += 1
    
    return c
    

def majoritaireDC(T):
    n = len(T)
    if n == 1:
        return (T[0], 1)
    else:
        T1 = [T[i] for i in range(0, n//2)]
        T2 = [T[i] for i in range(n//2, n)]
        (p1, c1) = majoritaireDC(T1)
        (p2, c2) = majoritaireDC(T2)
    
        if c1 != 0:
            c1 += occurences(p1, T2)
        if c2 != 0:
            c2 += occurences(p2, T1)
        if c1 > n//2:
            return (p1, c1)
        elif c2 > n//2:
            return (p2, c2)
        else:
            return (-1, 0)
            

"""
TESTS
"""

class TestExercice5(unittest.TestCase):
    """
    Tests des fonctions du module 'Exercice5'.
    """
    
    def test_occurences(self):
        """
        Test de la fonction occurences.
        """
        for i in range(10):
            tableau = randintlist(20)
            int = random.randint(0,3)
            
            c1 = occurences(1, tableau)
            c2 = occurences(int, tableau)
            
            self.assertEqual(c1, tableau.count(1))
            self.assertEqual(c2, tableau.count(int))


if __name__ == '__main__':
    unittest.main()