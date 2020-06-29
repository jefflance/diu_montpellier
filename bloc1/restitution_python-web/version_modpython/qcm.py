# -*- coding: utf8 -*-

from mod_python import apache, util

from template import *


def question(numero):
    """ Affiche la question de numéro donné du QCM.

    Entrée: entier
    Sortie: rien
    """
    fd = open("/var/www/html/test1.mala.fr/capitales.csv", "r")
    for line in range(5):
        line = fd.readline()
    question, _ = line.split(",")

    req.content_type = 'text/html'
    req.send_http_header()

    content = """
    <html>
    <body>
    <form action='qcm.py/{numero}' method='post'>
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
                <input type='submit' value='Valider la réponse'>
            </div>
        </div>
    </form>
    </body>
    </html>
    """.format(numero=numero, question=question)

    return content


def start(req):
    """ Renvoie la page d'acceuil du QCM.

    Entrée: Rien
    Sortie: Rien
    """

    donnees_formulaire = util.FieldStorage(req)
    qcm_on = donnees_formulaire.getfirst('qcm_on', 0)
    nombres_questions = donnees_formulaire.getfirst('nombres_questions', 5)
    numero_question = donnees_formulaire.getfirst('numero_question', 0)
    reponse_question = donnees_formulaire.getfirst('reponse_question', '')

    return (int(qcm_on), int(nombres_questions),
            int(numero_question), reponse_question)
