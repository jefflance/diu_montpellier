#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def html_haut():
    """ Renvoie le haut de la page web.
    """
    # Création de la page web
    # Indique le type de document envoyé au navigateur
    print("Content-type:text/html")
    print("<!doctype html>\n")
    print("<html>")
    print("<head>")
    print("<meta charset='utf8'>")
    print("<title>QCM</title>")
    print("</head>\n")
    print("<body>")
    print("<div class='content'>")


def accueil():
    """ Renvoie la page d'acceuil du QCM.

    Entrée: Rien
    Sortie: Rien
    """
    print("""
    <p>Bonjour !<p/>
    <p>Veuillez entrer votre nom.</p>

    <form action='/cgi-bin/qcm.py' method='post'>
    Prénom: <input type='text' name='prenom' required><br>
    Nom: <input type='text' name='nom' required><br>
    Nombre de questions du QCM:
    <input type='text' name='nombre_questions' value='5'><br>
    <input type='hidden' name='qcm_on' value=1><br><br>

    <input type='submit' value='Démarrer le QCM'>
    </form>
    """)


def html_bas():
    """ Renvoie le bas de la page web.
    """
    # Création de la page web
    # Indique le type de document envoyé au navigateur
    print("</div>")
    print("</body>")
    print("</html>")
