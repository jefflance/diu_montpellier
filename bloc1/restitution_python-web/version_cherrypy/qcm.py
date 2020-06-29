#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""
date: 29/06/19

Portage du qcm python avec interface en ligne de commande
en version web.
"""

import cherrypy


qcm = []

def peupler_qcm():
    """ Rempli la liste de questions-réponses du qcm dont les données sont
    stockées dans un fichier .csv dont la spécification est :
    'question';'reponse 1';'reponse 2';'reponse 3';'reponse 4';numero correct

    Entrée: rien
    Sortie: rien
    """
    fd = open('qcm.csv', 'r')
    for line in fd:
        line = line.rstrip('\n')
        question, *reponses_possibles, reponse_correcte = line.split(';')
        qcm.append((question, reponses_possibles, reponse_correcte))

    return None


def obtenir_question(numero_question):
    """ Renvoie le texte de la question numero_question.

    Entrée: entier
    Sortie: chaîne de caractères
    """
    question = qcm[numero_question-1][0]

    return question


def obtenir_reponse_possibles(numero_question):
    """ Renvoie les réponses possibles de la question numero_question.

    Entrée: entier
    Sortie: liste de chaîne de caractères
    """
    reponses_possibles = qcm[numero_question-1][1]

    return reponses_possibles


def obtenir_reponse_correcte(numero_question):
    """ Renvoie la réponse correcte de la question numero_question.

    Entrée: entier
    Sortie: entier
    """
    reponse_correcte = qcm[numero_question-1][2]

    return reponse_correcte


def valider_reponse(numero_question, reponse):
    """ Vérifie si le numéro de réponse donné à la question numero_question
    du QCM est celui de la bonne réponse.
    Renvoie vrai si la réponse est correcte, faux sinon.

    Entrée: entier, entier
    Sortie: bool
    """
    return reponse == obtenir_reponse_correcte(numero_question)


class QCM(object):
    """
    Déclare l'application QCM.
    """

    @cherrypy.expose
    def index(self):
        """ Affiche la page d'accueil.

        Entrée: instance de QCM
        Sortie: chaîne de caractères
        """
        nombre_questions = len(qcm)

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
                <input type='number' name='nombre_questions' min='5' max={nombre_questions} step='1' value='{nombre_questions}'><br>
                <input type='submit' value='Enregistrement'>
              </form>

            </div>
          </body>
        </html>
        """.format(nombre_questions=nombre_questions)

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
    def question(self, numero_question, reponse=None):
        """ Valide la réponse à la question précédente puis afiche la
        question suivante.
        Si le numéro de question atteint le nombre total de questions à poser,
        on affiche une page de fin contenant les informations utilisateur
        et le score.

        Entrée: instance de QCM, entier, entier par défaut à None
        Sortie: chaîne de caractères
        """
        numero_question = int(numero_question)

        # on vérifie la réponse précédente et on incrémente le score
        # en conséquence
        result = ''
        if numero_question > 0:
            if valider_reponse(numero_question, reponse):
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
            reponses_possibles = obtenir_reponse_possibles(numero_question)

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
                                <p>{question}</p>
                                <input type='radio' name='reponse' value='1' id='1'/><label for='1'>{reponses_possibles[0]}</label>
                                <input type='radio' name='reponse' value='2' id='2'/><label for='2'>{reponses_possibles[1]}</label>
                                <input type='radio' name='reponse' value='3' id='3'/><label for='3'>{reponses_possibles[2]}</label>
                                <input type='radio' name='reponse' value='4' id='4'/><label for='4'>{reponses_possibles[3]}</label>
                                <input type='hidden' name='numero_question' value='{numero_question}'><br>
                                <input type='submit' value='Valider la réponse'>
                            </div>
                        </div>
                    </form>
                </div>
              </body>
            </html>
            """.format(numero_question=numero_question, question=question, reponses_possibles=reponses_possibles)
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
    # au lancement de l'application on peuple le qcm
    peupler_qcm()
    # on lance l'application qui devient accessible à la racine de l'url
    cherrypy.quickstart(QCM(), '/', {'/': {'tools.sessions.on': True}})
