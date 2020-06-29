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


def affiche_question(numero):
    """ Affiche la question de numéro donné du QCM.

    Entrée: entier
    Sortie: Rien
    """
    print('\
        ')
