#!/usr/bin/python
# -*- coding: UTF-8 -*-

from ift099 import *
from math import *




# 1. faire la somme des 100 premiers nombres pairs

def sommePairs(listeNbs):
    total=0
    for nb in listeNbs:
        total += pair(nb)
    return total

def pair(n):
    return 2*n

print sommePairs(range(0,100))


# 2. faire la somme des nombres de 0 à -100

def sommeTransfo(listeNbs,transfo):
    total=0
    for nb in listeNbs:
        total+= transfo(nb)
    return total

def negation(n):
    return -n

def carre(n):
    return n*n

print sommeTransfo(range(0,100),negation)
print sommeTransfo(range(0,100),pair)
print sommeTransfo(range(0,100),carre)


# 3. faire une fonction qui retourne la liste des nombres premiers inferieurs a n (exclus)
def estPremier(nombreATester):
    for diviseurPotentiel in range(2,nombreATester):
       if(nombreATester%diviseurPotentiel == 0):
           return False

    return True

def listePremiers(max):
    listeResultante=[]
    for candidat in range(2,max):
        if(estPremier(candidat)):
            listeResultante.append(candidat)
    return listeResultante

print listePremiers(100)


# 4. écrire une fonction qui retourne le plus petit élément d'une liste reçue en paramètre.
def trouvePlusPetit(listeNombres):

    if len(listeNombres)==0:
        print "Erreur, liste vide"
        return

    plusPetitADate = listeNombres[0]

    for nombre in listeNombres:
        if(nombre < plusPetitADate):
            plusPetitADate = nombre

    return plusPetitADate

print trouvePlusPetit([3,7,5,0,7,-4,2,9])
print trouvePlusPetit([])

# 5. écrire un programme qui retourne l'écart-type d'une liste de nombres entrés au clavier. Divisez le programme en
#    3 modules, chacun implanté dans une fonction:
#    a) obtenir la liste de nombres
#    b) calculer la moyenne de la liste
#    c) calculer l'écart-type de la liste.

def lireListeNombres(quantite):

    listeResultante=[]
    for cpt in range(quantite):
        print "Entrez une note:"
        noteCourante = lireEntier()
        while(noteCourante < 0 or noteCourante > 100):
            print "Erreur, entrez des valeurs entre 0 et 100"
            noteCourante = lireEntier()
        listeResultante.append(noteCourante)

    return listeResultante

def calculerMoyenne(listeNotes):
    total=0
    for note in listeNotes:
        total += note

    return (total*1.0)/len(listeNotes)


def calculerEcartType(listeNotes):

    total = 0
    for note in listeNotes:
        total += (calculerMoyenne(listeNotes)-note)**2

    return sqrt(total / (len(listeNotes)*1.0))

def ecartType():

    print "Entrez le nombre de notes:"
    nombreNotes = lireEntier()
    print calculerEcartType(lireListeNombres(nombreNotes))



# 6. écrire un programme qui détermine si un mot est un palindrôme. Le mot en question sera
#    lu au clavier. Le programme affiche "Est un palindrôme" ou "N'est pas un palindrôme" selon
#    le cas.
def verifiePalindrome(mot):

    for position in range(len(mot)):

        if(mot[position] != mot[len(mot)-1-position]):
            print "N'est pas un palindrome"
            return False

    print "Est un palindrome"
    return True

verifiePalindrome("laval")
verifiePalindrome("loozoo")
verifiePalindrome("epique")

# 7. écrire un programme qui classifie un triangle: équilatéral, isocèle, rectangle, scalène.
#     Un triangle peut avoir plusieurs de ces qualités.
#     Votre programme devrait lire au clavier les informations décrivant le triangle.
#     Ces informations peuvent prendre plusieurs formes: coordonnées des sommets? Longueur
#     des côtés et angles? 6 paramètres séparés, ou 3 couples (x,y)? Ou 2 listes (longueurs et angles)?
#     Tout dépend de l'approche que vous prenez pour faire le traitement.
#     Le programme affiche à l'aide de print les qualités du triangle.
