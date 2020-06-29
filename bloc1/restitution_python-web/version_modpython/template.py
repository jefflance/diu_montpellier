# -*- coding: utf8 -*-

def html_haut():
    """ Renvoie le haut de la page web.
    """
    # Création de la page web
    # Indique le type de document envoyé au navigateur
    content = """
    <!doctype html>
    <html>
    <head>
    <meta charset='utf8'>
    <title>QCM</title>
    </head>
    <body>
    <div class='content'>
    """

    return content


def html_bas():
    """ Renvoie le haut de la page web.
    """
    # Création de la page web
    # Indique le type de document envoyé au navigateur
    content = """
    </div>
    </body>
    </html>
    """

    return content
