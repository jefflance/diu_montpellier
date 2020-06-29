#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

nombre_de_questions = int(input("Combien de questions à poser ? "))
done = []
points = 0
dict_capitales = {}


fd = open("capitales.csv", "r")
for line in fd:
    pays, capitale = line.split(",")
    dict_capitales[pays] = capitale

print(dict_capitales)

numero_de_question = 1

while numero_de_question <= nombre_de_questions:
    choice = random.choice(list(dict_capitales.keys()))
    if choice not in done:
        answer = input("Quelle est la capitale de {} ? ".format(choice))

    if answer.lower() == dict_capitales[choice].lower():
        # print(answer.lower(), "-", dict_capitales[choice].lower())
        points += 1
    else:
        print("Mauvaise réponse !")
        print("La bonne réponse est {}".format(dict_capitales[choice]))

    numero_de_question += 1

print("Vous avez gagné {} point(s)".format(points))
