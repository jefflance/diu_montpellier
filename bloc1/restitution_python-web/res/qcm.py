#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import cgitb


def accueil():
    """ Affiche la page d'accueil du QCM.

    Entrée: Rien
    Sortie: Rien
    """
    print('\
           <p>Bonjour !<p/>\r\n\
           <p>Veuillez entrer votre nom.</p>\r\n\
           \
           <form action="/cgi-bin/hello_get.py" method="post">\r\n\
           Prénom: <input type="text" name="prenom"><br/>\r\n\
           Nom: <input type="text" name="nom" /><br/><br/>\r\n\
           \
           <input type="submit" value="Démarrer le QCM" />\r\n\
           </form>\
          ')


def affiche_question():
    """ Affiche une question du QCM.

    Entrée: Rien
    Sortie: Rien
    """
    pass

# Création de la page web
# Indique le type de document envoyé au navigateur
print("Content-type:text/html\r\n")

# Début de la page web
print('\
       <html>\r\n\
       <head>\r\n\
       <meta charset="utf8">\r\n\
       <title>QCM</title>\r\n\
       </head>\r\n\
      ')

# Corps de la page
print('\
       <body>\r\n\r\n\
       <div class="content">\r\n\
      ')

accueil()

print('\
       </div>\r\n\
       </body>\r\n\
      ')

# Fin de la page
print('</html>')

# On créé une instance de FieldStorage afin de stocker les données
# du formulaire
formulaire = cgi.FieldStorage()
