#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import cgi
# import cgitb

# import Cookie

from template import *

# cgitb.enable()
# cgi.test()


def recuperer_donnees():
    """ Renvoie le numero de la question à afficher.

    Entrée: rien
    Sortie: entier
    """
    donnees_formulaire = cgi.FieldStorage()
    qcm_on = donnees_formulaire.getfirst('qcm_on', 0)
    nombres_questions = donnees_formulaire.getfirst('nombres_questions', 5)
    numero_question = donnees_formulaire.getfirst('numero_question', 0)
    reponse_question = donnees_formulaire.getfirst('reponse_question', '')

    return (int(qcm_on), int(nombres_questions),
           int(numero_question), reponse_question)


def affiche_question(numero):
    """ Affiche la question de numéro donné du QCM.

    Entrée: entier
    Sortie: rien
    """
    fd = open("capitales.csv", "r")
    for line in range(numero):
        line = fd.readline()
    question, _ = line.split(",")

    print("""
    <form action='/cgi-bin/qcm.py' method='post'>
        <div class='qcm-question'>
            <div class='qcm-numero'>
                <span>{numero}</span>
            </div>
            <div class='qcm-txt'>
                <p>
                Quelle est la capitale de {question} ?
                </p>
                Réponse : <input type='text' name='reponse_question'><br>
                <input type='hidden' name='numero_question' value='{numero}'><br>
                <input type='hidden' name='qcm_on' value='{qcm_on}'><br>
                <input type='submit' value='Valider la réponse'>
            </div>
        </div>
    </form>
    """.format(numero=numero, question=question, qcm_on=qcm_on))


def valider_reponse(numero_question, reponse_question):
    """ Vérifie la réponse donnée à la question du QCM, dont le numéro est
    passé en paramètre.
    Renvoie vrai si la réponse est correcte, faux sinon.

    Remarque: ne gère pas les accents.
    En effet, si la bonne réponse comporte un ou des caractères spéciaux
    il faudra les avoir rentré dans la réponse pour se voir valider la réponse.

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


"""
Affichage de la page du QCM
"""
html_haut()


qcm_on, nombres_questions, numero, reponse = recuperer_donnees()

print("qcm_on:", qcm_on, "numero:", numero, "reponse:", reponse)
if qcm_on:
    while numero < nombres_questions:
        affiche_question(numero+1)
        if numero > 0:
            print("Réponse précédente: ", valider_reponse(numero, reponse))
else:
    accueil()

html_bas()
