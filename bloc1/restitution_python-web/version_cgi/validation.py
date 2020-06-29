#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import cgitb

from template import *

cgitb.enable()
# cgi.test()


def recuperer_reponse():
    """ Récupère la réponse à la question posée via le formulaire.

    Entrée: rien
    Sortie: entier, chaîne de caractère
    """
    donnees_formulaire = cgi.FieldStorage()

    numero_question = donnees_formulaire.getvalue('numero_question')
    reponse_question = donnees_formulaire.getvalue('reponse_question')

    return int(numero_question), reponse_question


def valider_reponse(numero_question, reponse_question):
    """ Vérifie la réponse donnée à la question du QCM, dont le numéro est
    passé en paramètre.
    Renvoie vrai si la réponse est correcte, faux sinon.

    Entrée: entier, chaîne de caractère
    Sortie: bool
    """
    # on récupère la réponse à la question posée
    # en lisant autant de ligne que le numéro de la question posée
    fd = open("capitales.csv", "r")
    for line in range(numero_question):
        line = fd.readline()
    # attention: readline renvoie une chaîne de caractère correspondant
    # à la ligne lu avec un caractère de nouvelle ligne à la fin
    # il est donc nécessaire de le retirer
    line = line.rstrip('\n')

    _, reponse = line.split(",")

    return reponse_question.lower() == reponse.lower()


html_haut()

n, r = recuperer_reponse()

print(valider_reponse(n, r))

html_bas()
