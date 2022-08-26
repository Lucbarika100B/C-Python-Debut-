#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Jour 4,

from ift099 import *
from math import *


#Exemple #1, heures, minutes, secondes... appliquer la langue


#constantes
nbsecmin=60
nbminheure=60
nbsecheure=nbsecmin*nbminheure

#fonctions pour chaque partie
def calculerHeures(tempsEntre):
    print "test"
    return tempsEntre//nbsecheure


print "Tests pour calculerHeures"
print "3600s ->",calculerHeures(3600),'h'
print "7862s ->",calculerHeures(7862),'h'
print "1000s ->",calculerHeures(1000),'h'

def calculerMinutes(tempsEntre):
    return (tempsEntre%nbsecheure)//nbsecmin

print "Tests pour calculerMinutes"
print "3600s ->",calculerMinutes(3600),'m'
print "7862s ->",calculerMinutes(7862),'m'
print "1000s ->",calculerMinutes(1000),'m'


def calculerSecondes(tempsEntre):
    return tempsEntre % nbsecmin

print "Tests pour calculerMinutes"
print "3600s ->",calculerSecondes(3600),'s'
print "7862s ->",calculerSecondes(7862),'s'
print "1000s ->",calculerSecondes(1000),'s'

def afficherHMS(h, m, s):
    print h, 'h:',m , 'm:',s,'s'

print "3600s ->"
afficherHMS(1,0,0)
print "7862s ->"
afficherHMS(2,11,2)
print "1000s ->"
afficherHMS(0,16,40)

#message + conversion
def conversionHMS():
    conversionPourVrai(lireEntier())



#conversion+affichage
def conversionPourVrai(tempsEntre):
    afficherHMS(calculerHeures(tempsEntre), calculerMinutes(tempsEntre), calculerSecondes(tempsEntre))


#Exemple #2, liste de 100 premiers nombres impairs au carré
#Solution 1: afficher manuellement chaque nombre
listeNb = range(1,101)

def impair(n):
    return 2*n-1

def carre(n):
    return n*n


def appliquer(liste,fonction):

    listeResultante=[]
    for elem in liste:
        listeResultante.append(fonction(elem))

    return listeResultante



def sommation(liste):

    total=0
    for elem in liste:
        total = total+elem

    return total

def impairscarres(liste):
    return sommation(appliquer(appliquer(liste,impair),carre))

print impairscarres(listeNb)
#Exemple #3: faire la sommation des membres d'une liste de nombres


#Exemple #4: programme qui calcule la moyenne de notes lues au clavier
#Discuter des entrées erronnées qu'on peut faire et comment les prévenir
#Dériver l'algorithme suivant:

def moyenne():
    print "Veuillez entrer le nombre de notes"
    nbNotes = lireEntier()
    total=0
    for i in range(0,nbNotes):
        noteCourante=lireNote(i)
        total=ajouterTotal(noteCourante,total)

    moyenne=calculerMoyenne(total,nbNotes)
    print "La moyenne est: ", moyenne

def lireNote(no):

    print "Entrez la ",no+1,"ème note"
    return lireReel()




def ajouterTotal(note,total):
    return 50

def calculerMoyenne(total,quantite):
   return 60






#algorithme:
#lire le nombre de notes
#pour chaque note
    #lire la note (fonction lireNote)
    #ajouter la note au total
#calculer la moyenne (fonction calculer moyenne)

#fonction lireNote (numéro de note)
    #lire un nombre
    #tant que le nombre est < 0 ou > 100
        #message d'erreur
        #lire un nombre


#fonction calculer moyenne (total, quantité)
    #si la quantité est <= 0
        #afficher un message d'erreur
    #sinon
        #calculer la moyenne (total / quantité)