#!/usr/bin/python
# -*- coding: UTF-8 -*-


from ift099 import *
from math import *


# 1. Écrire une fonction qui calcule la moyenne de 3 nombres
def moyenne3(a,b,c):
    return (a+b+c)/3

print moyenne3(19,25,67)


# 2. Écrire une fonction qui calcule le quotient et le reste d'une division,
#  et retourne le résultat sous forme de liste
def quotientReste(a,b):
    return (a//b, a%b)

print quotientReste(25,3)

#2a. Utiliser la fonction précédente pour afficher le quotient de 752 / 95 et le reste de 451 / 333
print quotientReste(752,95)[0]
print quotientReste(451,333)[1]

# 3. Écrire une fonction qui calcule le quotient et le reste d'une division,
#  et retourne le résultat sous forme de dictionnaire, avec les clés 'quotient' et 'reste'.
def quotientResteDic(a,b):
    return {'quotient':a//b,'reste':a%b}

print quotientResteDic(546,7)

#3a. Utiliser la fonction précédente pour afficher le quotient de 932 / 101 et le reste de 2349 / 312
print quotientResteDic(932,101)['quotient']
print quotientResteDic(2349,312)['reste']

# 4. Écrire une fonction qui calcule le nombre d'or

# 5. Écrire une fonction qui dessine un carre avec une taille et une position
# reçus en paramètre.
def dessineCarre(taille,x,y):
    nouveauCanevas()
    ajouterTortue(x,y)
    avancerTortue(taille)
    tournerTortue()
    avancerTortue(taille)
    tournerTortue()
    avancerTortue(taille)
    tournerTortue()
    avancerTortue(taille)

dessineCarre(200,300,300)


# 6. Écrire une fonction qui place la tortue au centre d'un carré qu'elle a dessiné.
# La taille et la position du carré doivent être reçus en paramètre.
def centreCarre(taille,x,y):
    dessineCarre(taille,x,y)
    tournerTortue()
    tournerTortue()
    avancerTortue(taille/2,True)
    tournerTortue(False)
    avancerTortue(taille/2,True)

centreCarre(200,300,300)


# 7. Définir une fonction qui retourne le n_ième terme ( en math on lirait f (n) ),
#  de la fonction f(x) = x² + 5x - 4

def nieme(x):
    return x**2+5*x -4


print nieme(70)

# 8. Définir une fonction qui retourne l'aire d'un cercle à partir de son rayon.
def aireCercle(r):
    return pi*(r**2)

print aireCercle(100)

# 9. Définir une procédure qui fait dessiner la lettre A en majuscule à la tortue, avec un facteur
# d'échelle reçu en paramètre. Pour tourner la tortue d'un angle qui n'est pas multiple de 90 degrés,
# utilisez la procédure tournerTortueDegres(angle).

def dessinerLettreA(taille):
    ajouterTortue(200,200)
    tournerTortueDegres(300)
    avancerTortue(2*taille)
    tournerTortueDegres(120)
    avancerTortue(2*taille)
    tournerTortueDegres(180)
    avancerTortue(taille,True)
    tournerTortueDegres(-60)
    avancerTortue(taille)


dessinerLettreA(50)



# 10. Entrez des nombres réels dans l'interpréteur jusqu'à ce que vous découvriez la plus petite fraction
# décimale pouvant être représentée fidèlement dans python (aucun arrondi). Faites de même pour la représentation d'un
# très grand nombre. Définissez une constante pour chacun de ces nombres. Vous pouvez écrire des nombres en notation
# scientifique directement dans l'interpréteur: 5e-3 = 0.005, et 5e+3 = 5000, par exemple.

minimum = 1e-323
maximum=1.7976931348623157e+308

# 11. Écrivez une fonction qui calcule l'expression logique suivante:
# (p ou-exclusif q)

def xor(p,q):
    return (p and (not q)) or ((not p) and q)


# 12. Écrivez une fonction qui produit True si la valeur de son paramètre se trouve entre 100 et 500 et False sinon.

def entre100et500(n):
    return n<500 and n>100


# 13. Écrivez une fonction de x et y qui produit True si la valeur de x est un multiple de la valeur de y.

def estMultiple(x,y):
    return x%y == 0

# 14. Calculez quantité de carburant qu'une fusée idéale a besoin pour envoyer en orbite à une vitesse non-relativiste un cargo.
# Utilisez l'équation de Tsiolkovsky: https://fr.wikipedia.org/wiki/%C3%89quation_de_Tsiolkovski
# Assumez qu'on utilise un moteur Merlin 1-D au sol : https://fr.wikipedia.org/wiki/Merlin_(moteur-fus%C3%A9e)#Merlin_1D
# Assumez que le delta-v désiré est 9700 m/s (nécessaire pour orbite basse).
# Dans l'équation de Tsiolkovsky, on s'intéresse donc à obtenir mi - mf (masse du carburant seulement).
# Placez toutes vos constantes dans un dictionnaire appelé ParametresFusee et utilisez-les dans votre fonction.
# Votre fonction devrait s'appeler ProportionCargo, et prendre en paramètre la masse du cargo (en tonnes).
# Séparez le travail en plusieurs sous-fonctions si possible et évitez complètement de définir des symboles
# pour vos résultats intermédiaires. N'oubliez pas la masse du moteur (470 kg)!

ParametresFusee = {'Deltav':9700.0, 'VitesseGasMoteur':2766.0, 'MasseMoteur' : 470.0}

def calculerProportionMasse(masseCargo):
    return e**(-ParametresFusee['Deltav'] / ParametresFusee['VitesseGasMoteur'])

def calculerMasseCombustible(masseCargo):
    return (calculerMasseSeche(masseCargo)/calculerProportionMasse(masseCargo))-calculerMasseSeche(masseCargo)

def calculerMasseSeche(masseCargo):
    return ParametresFusee['MasseMoteur']+masseCargo

print calculerMasseCombustible(5000)

