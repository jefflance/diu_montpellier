#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Génère les nombres premiers inférieurs à la valeur passée en paramètre.
"""

import sys
from math import sqrt



def is_prime(n):
    """
    Renvoie si une un nombre entier naturel est premier ou non.

    :param: n
        entier naturel
    :type n:
        int
    :return:
        si l'entier est premier ou non
    :rtype:
        bool
    """
    primalite = False

    if ( n == 2 or n == 3 or n == 5 or n%2 != 0 and n%3 != 0 and n%5 != 0):
        primalite = True
        i = 7

        while primalite and i <= sqrt(n):
            if n%i == 0:
                primalite = False
            i = i + 1

    return primalite



if len(sys.argv) != 2:
    print('Ce script prend un unique paramètre')
    exit()

n = int(sys.argv[1])


if n < 2:
    print('Il n\'y a pas de nombre premier inférieur strict à {}'.format(n))
else:
    for i in range(2, n+1):
        if is_prime(i):
            print(i)
