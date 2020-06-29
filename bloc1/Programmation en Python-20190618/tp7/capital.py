#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import re

nombre_de_questions = int(input("Combien de questions à poser ? "))
numero_de_question = 1
done = []
score = 0
dict_capitales = {}


def nettoyer_nom(nom):
    """ Renvoie le nome de la capitale sans la partie entre
    parenthèses.

    Entrée: chaîne de caractères
    Sortie: chaîne de caractères
    """
    regexp = "(.+)( \((.{2,3})\))"
    resultat = re.search(regexp, nom)
    if resultat:
        return resultat.group(1)
    return nom


def peupler_dict():
    """ Peuple le dictionnaire des questions et réponses au quizz.

    Entrée: rien
    Sortie: rien
    """
    with open("capitales.csv", "r") as fd:
        for line in fd:
            pays, capitale = line.split(",")
            capitale = capitale.rstrip('\n')   
            dict_capitales[pays] = capitale
    
    return None


def afficher_question():
    """ Renvoie un question du quizz choisie aléatoirement ainsi
    que la réponse associée.

    Entrée: rien
    Sortie: chaîne de caractères, chaîne de caractères
    """
    question = random.choice(list(dict_capitales.keys()))
    while question in done:
        question = random.choice(list(dict_capitales.keys()))

    reponse = input("Quelle est la capitale de {} ? ".format(nettoyer_nom(question)))

    return question, reponse


def valider_question(question, reponse, score):
    """ Renvoie si la réponse à la question est correcte et le score mis à jour.

    Entrée: chaîne de caractères, chaîne de caractères, entier
    Sortie: bool, entier
    """
    result = False
    if reponse.lower() == dict_capitales[question].lower():        
        score += 1
        result = True
    
    return result, score


def afficher_message(question, correct):
    """ En fonction de la question, affiche un message, en cas d'erreur,
    qui mortifie l’utilisateur en affichant la bonne réponse correspondante.

    Entrée: chaîne de caractères, bool
    Sortie: rien
    """
    if not correct:
        print("Mauvaise réponse !")
        print("La bonne réponse est {}".format(dict_capitales[question]))
    return None

# peuplement du quizz
peupler_dict()

# tant que le nombre de questions posées n'est pas arrivé à la quantité voulue
# par l'utilisateur, on pose des questions
while numero_de_question <= nombre_de_questions:
    # on affiche un question et on récupère la réponse
    question, reponse = afficher_question()
    # la réponse est-elle valide et doit-on mettre à jour le score ?
    resultat, score = valider_question(question, reponse, score)
    # on affiche le message de réussite ou non à la question
    afficher_message(question, resultat)
    # on passe à la question suivante
    numero_de_question += 1

# Le quizz est terminé
print("Vous avez gagné {} point(s)".format(score))
