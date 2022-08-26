#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Jour 3, retour sur dessinerCarre (Jour 3)
# ==============================================================================
from ift099 import *
from math import *

def dessinerCarre1(x, y, taille):
    nouveauCanevas()
    ajouterTortue(x,y)
    avancerTortue(taille)
    for i in range(3):
        tournerTortue()
        avancerTortue(taille)
    
    print infoTortue()

def dessinerCarre2(x, y, taille):
    nouveauCanevas()
    ajouterTortue(x,y)
    for i in range(4):
        avancerTortue(taille)
        tournerTortue()
        
    print infoTortue()
    
def dessinerCarre3(x, y, taille):
    nouveauCanevas()
    ajouterTortue(x,y)
    i = 0
    while i < 4:
        avancerTortue(taille)
        tournerTortue()
        i = i+1
        
    print infoTortue()
    
def dessinerCarre4(x, y, taille):
    nouveauCanevas()
    ajouterTortue(x,y)
    i = 4
    while i > 0:
        avancerTortue(taille)
        tournerTortue()
        i -= 1
        
    print infoTortue()
    
def dessinerCarre5(x, y, taille):
    nouveauCanevas()
    ajouterTortue(x,y)
    i = 3
    while i >= 0:
        avancerTortue(taille)
        tournerTortue()
        i -= 1
        
    print infoTortue()
# ==============================================================================
#lireEntier() : attention! Ne peut pas être appelé avant que la console soit active. Doit découler d'un appel
#dans l'interpréteur.
#Exemple heures minutes secondes, live

nbSecondesParHeure=3600
nbSecondesParMinute=60

def calculerHeures(tempsEntre):
   return tempsEntre / nbSecondesParHeure

def calculerMinutes(tempsEntre):
   return (tempsEntre % nbSecondesParHeure) / nbSecondesParMinute

def calculerSecondes(tempsEntre):
   return tempsEntre % nbSecondesParMinute

def afficherHMS(h,m,s):
    print h,
    print "Heures, ",
    print m,
    print "Minutes, ",
    print s,
    print "Secondes."


def conversionHMS():
    print "Entrez le temps en secondes (entier positif SVP ok merci)"
    conversionPourVrai(lireEntier())

def conversionPourVrai(tempsEntre):
    afficherHMS(calculerHeures(tempsEntre),calculerMinutes(tempsEntre),calculerSecondes(tempsEntre))

#Exemple valeur absolue

def valeurAbsolue(x):
    if (x>0):
        if(x==3):
            print "Numéro gagnant de la tombola"

        return x
    elif (x==0):
        return 0
    else:
        return -x



#Exemple déplacer la tortue (utiliser infoTortue).
def retourAZero():
    nouveauCanevas()
    ajouterTortue(300,300)
    tournerTortueDegres(180)

    while ((infoTortue()['position'][0])>0):
        avancerTortue(10)

#Exemples de boucles dans des listes et dictionnaires
liste=[4,5]
for elem in liste:
    print elem+5

for position in range(2):
    print liste[position]

dict={'a':6,'b':7}
for sdfkjg in dict:
    print sdfkjg

for clef in dict:
    print dict[clef]

texte = "asdf"
for lettre in texte:
    print lettre

for valeur in range(100):
    if(valeur %7 ==0):
        print valeur

#Catégoriser un nombre en ordre de grandeur (<100,<1000...)
#
def evaluerCompteBanque(montant):
    if(montant < 100):
        print "Étudiant"
    elif (montant <-1000):
        print "Étudiant gradué"
    elif (montant > 1000):
        print "Jeune professionnel"
    elif (montant > 10000):
        print "Plein à craquer!!!"


#devine a quoi je pense

def devine():

    print "Devine à quel valeur entière positive je pense!"
    if(lireEntier()==5):
        print "Oui, c'est bien ça!"
    else:
        print "c'est pas ce que je cherche"


