#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""
date: 29/06/19

Portage du qcm python avec interface en ligne de commande
en version avec interface web.
"""

import cherrypy


def obtenir_question(numero_question):
    """ Renvoie la question de numéro numero_question.

    Entrée: entier
    Sortie: chaîne de caractères
    """
    fd = open("capitales.csv", "r")
    for line in range(numero_question):
        line = fd.readline()
    question, _ = line.split(",")

    return question


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


class qcm(object):
    """
    Déclare l'application QCM.
    """

    @cherrypy.expose
    def index(self):
        """ Affiche la page d'accueil.

        Entrée: instance de QCM
        Sortie: chaîne de caractères
        """

        content = """
        <!doctype html>
        <html>
          <head>
            <meta charset='utf8'>
            <title>QCM</title>
          </head>

          <body>
            <div class='content'>

              <p>Bonjour !<p/>
              <p>Veuillez entrer votre nom.</p>

              <form action='start' method='post'>
                Prénom: <input type='text' name='prenom' required><br>
                Nom: <input type='text' name='nom' required><br>
                Nombre de questions du QCM:
                <input type='text' name='nombre_questions' value='5'><br>
                <input type='submit' value='Enregistrement'>
              </form>

            </div>
          </body>
        </html>
        """

        return content


    @cherrypy.expose
    def start(self, prenom, nom, nombre_questions=5):
        """ Affiche la page de démarrage du QCM après avoir enregistré
        les informations utilisateur.

        Entrée: instance de QCM, chaîne de caractères,
                chaîne de caractères, entier
        Sortie: chaîne de caractères
        """
        cherrypy.session['prenom'] = prenom
        cherrypy.session['nom'] = nom
        cherrypy.session['nombre_questions'] = int(nombre_questions)
        cherrypy.session['score'] = 0

        content = """
        <!doctype html>
        <html>
          <head>
            <meta charset='utf8'>
            <title>QCM</title>
          </head>

          <body>
            <div class='content'>

              <p>Vous êtes prêt ?<p/>

              <form action='question' method='post'>
                <input type='submit' value='Démarrer le QCM'>
                <input type='hidden' name='numero_question' value='0'>
              </form>

            </div>
          </body>
        </html>
        """

        return content


    @cherrypy.expose
    def question(self, numero_question, reponse_question=''):
        """ Valide la réponse à la question précédente puis afiche la
        question suivante.
        Si le numéro de question atteint le nombre total de questions à poser,
        on affiche une page de fin contenant les informations utilisateur
        et le score.

        Entrée: instance de QCM, entier, chaîne de caractères
        Sortie: chaîne de caractères
        """
        numero_question = int(numero_question)

        # on vérifie la réponse précédente et on incrémente le score
        # en conséquence
        result = ''
        if numero_question > 0:
            if valider_reponse(numero_question, reponse_question):
                cherrypy.session['score'] += 1

        # on passe à la question suivante
        # en effet, la variable numero_question est initialement fixée à 0
        # et puisque les questions commencent à 1...
        # ce qui fait qu'à chaque appel de cette fonction, on incrémente le
        # compteur des questions
        numero_question += 1

        if numero_question <= cherrypy.session['nombre_questions']:
            # stockage des informations utilisateur dans une session
            cherrypy.session['numero_question'] = numero_question
            question = obtenir_question(numero_question)

            content = """
            <!doctype html>
            <html>
              <head>
                <meta charset='utf8'>
                <title>QCM</title>
              </head>

              <body>
                <div class='content'>
                    <form action='question' method='post'>
                        <div class='qcm-question'>
                            <div class='qcm-numero'>
                                <span>{numero_question}</span>
                            </div>
                            <div class='qcm-txt'>
                                <p>Quelle est la capitale de {question} ?</p>
                                Réponse : <input type='text' name='reponse_question'><br>
                                <input type='hidden' name='numero_question' value='{numero_question}'><br>
                                <input type='submit' value='Valider la réponse'>
                            </div>
                        </div>
                    </form>
                </div>
              </body>
            </html>
            """.format(numero_question=numero_question, question=question)
        else:
            content = """
            <!doctype html>
            <html>
              <head>
                <meta charset='utf8'>
                <title>QCM</title>
              </head>

              <body>
                <div class='content'>
                    <div class='qcm-resultat'>
                        <h2>Bravo {prenom} {nom} !</h2><br>
                        <p>Vous avez terminé.</p><br>
                        <p>Votre score est de {score} bonnes réponses sur
                        un total de {nombre_questions} questions.</p>
                    </div>
                </div>
              </body>
            </html>
            """.format(prenom=cherrypy.session['prenom'],
                       nom=cherrypy.session['nom'],
                       nombre_questions=cherrypy.session['nombre_questions'],
                       score=cherrypy.session['score'])

        return content


if __name__ == '__main__':
    # on lance l'application qui devient accessible à la racine de l'url
    cherrypy.quickstart(qcm(), '/', {'/': {'tools.sessions.on': True}})
