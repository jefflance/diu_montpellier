Fiche pédagogique
===

## Résumé de l'activité

Mini-projet : Transformer l'application QCM réalisée en Python en serveur de QCM.

## Problématique

Le TP QCM Python permet de créer un QCM s'exécutant par l'utilisateur dans la console. Ainsi, chaque utilisateur lance indépendamment sa propre application QCM avec sa propre banque de questions.

Plusieurs questions en découlent :

- peut-on centraliser les données du QCM (pour faciliter la mise à jour des questions,...) ?
- peut-on faire que plusieurs utilisateurs accèdent au même QCM en même temps ?
- peut-on avoir une interface accessible depuis un poste ne disposant pas de Python ?

## Objectifs

+ À l'aide de Python créer un outil web côté serveur.
  On utilisera pour cela le module **CherryPy**.
+ L'utilisateur après s'être enregistré, sera en mesure de compléter le QCM, le terminer et obtenir son score.
+ Modifier l'aspect des pages web du QCM à l'aide de CSS (et de JavaScript éventuellement).
+ *Aller plus loin, en proposant un stockage des informations utilisateur et du score dans une structure de données.*



## Durée approximative

Ce mini-projet peut être abordé de manière indépendante du TP QCM Python et être lancé après avoir laissé s'écouler quelques séances heures.
S'agissant d'un mini-projet, la durée du déroulement peut donc varier.
Partir sur une base d'une petite dizaine d'heure semble cohérent sur le niveau 1ère.

## Niveau

1ère ou Terminale NSI

## Prérequis

1. Matériels.
   - sujet du mini-projet avec fichier `qcm.csv`
   - poste informatique avec une installation de Python fonctionnnelle et un navigateur web.
   - module CherryPy et ses dépendances installés et accessibles.
   - accès au web pour accéder aux ressources documentaire de HTML, CSS, CherryPy,...

2. Connaissances de bases sur la programmation avec Python.
   - au travers de l'activité QCM Python, l'élève aura déjà abordé :
     + la création de fonction.
     + le traitement des chaînes de caractères.
     + la lecture de fichier dont la spécifiaction est fournie (.csv dont les colonnes contiennent une information précise).

3. Connaissances sur la programmation de page web en HTML.
   - créer une page HTML.
   - savoir créer et traiter un formulaire web.
   - CSS.
   - *JavaScript peut être un plus.*



## Lien programme

*Une des compétence élémentaire mise en œuvre est la division d'un problème en plusieurs sous problème. Celle-ce se retrouve en la création et l'utilisatin de sous fonctions permettant de réaliser des tâches mais répétitives que d'implémenter quelques grosses procédures incluant plusieurs tâches.*

*Les notions du monde de la programmation objet sont abordées implicetement dans la mesure où le module CherryPy instancie un objet "site web" qu'il rend ensuite accessible via sa "partie serveur".*

---

#### En 1ère

##### Représentation des données: types construits (1ere)

- p-uplets.
- Tableau indexé.

##### Traitement de données en table (1ere)

- Indexation de tables.

##### Interactions entre l’homme et la machine sur le Web (1ere)

- Interaction avec l’utilisateur dans une page Web
- Interaction client-serveur.
- Formulaire d’une page Web.

##### Langages et programmation (1ere)

- Constructions élémentaires.
- Spécification.
- Utilisation de bibliothèques.


---
#### En Terminale

Cette activité peut être abordée en Terminale.
Dès lors, il est possible de la modifier afin :

- d'implémenter une base de données pour le stockage des données du QCM, des données utilisateur et des scores.
- de communiquer avec une API Rest afin de récolter le questionnaire du QCM (voir https://openquizzdb.org).

Voici les thèmes abordés :

##### Structures de données (Tale)

##### Bases de données (Tale)

##### Langages et programmation (Tale)

---


Activité
===

### 1. Présentation du mini-projet

Situer le mini-projet par rapport au produit du TP QCM et faire émerger les éléments de la problématique.

### 2. Présentation du fichier de données

Le fichier qcm.csv contient les questions et les réponses du QCM.
Voici la description de ses champs :

| Champ 1              | Champ 2   | Champ 3   | Champ 4   | Champ 5   | Champ 6                    |
|----------------------|-----------|-----------|-----------|-----------|----------------------------|
| Texte de la question | Réponse A | Réponse B | Réponse C | Réponse D | Numéro de la bonne réponse |

### 3. Passons aux choses sérieuses...

#### a) Écrire une fonction qui ouvre et analyse le fichier `qcm.csv` pour créer une liste contenant des tuples dont :
- le 1er élément est la question ;
- le second élément est une liste des réponses possibles ;
- le troisième élément est un entier correspond au numéro de la réponse correcte.