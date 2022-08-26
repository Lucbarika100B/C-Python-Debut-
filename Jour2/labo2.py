#!/usr/bin/python
# -*- coding: UTF-8 -*-

from ift099 import *
from math import *

# 1. Écrire une fonction qui calcule la moyenne de 3 nombres
def numbersAverage(x, y, z):
    return (x+y+z)/3.0

# 2. Écrire une fonction qui calcule le quotient et le reste d'une division,
#  et retourne le résultat sous forme de liste
def divideNumbers(x, y):
    listeDeRetour = [x/y, x%y]
    return listeDeRetour
    #return ([x/y, x%y])


#2a. Utiliser la fonction précédente pour afficher le quotient de 752 / 95 et le reste de 451 / 333
print divideNumbers(752, 95)
print divideNumbers(451, 333)

# 3. Écrire une fonction qui calcule le quotient et le reste d'une division,
#  et retourne le résultat sous forme de dictionnaire, avec les clés 'quotient' et 'reste'.
def divideNum(a, b):
    return {"quotient":a/b, "reste": a%b}

#3a. Utiliser la fonction précédente pour afficher le quotient de 932 / 101 et le reste de 2349 / 312
print divideNum(932, 101)
print divideNum(2349, 312)

# 4. Définir une fonction qui retourne l'aire d'un cercle à partir de son rayon.
def circleSurface(z):
    return (pi*2*z)


# 5. Écrire une fonction qui dessine un carre avec une taille et une position
# reçus en paramètre.
nouveauCanevas()
ajouterTortue()

def drawSquare(n):
    avancerTortue(n)
    tournerTortue()
    avancerTortue(n)
    tournerTortue()
    avancerTortue(n)
    tournerTortue()
    avancerTortue(n)
    tournerTortue()

print drawSquare(40)


# 6. Écrire une fonction qui place la tortue au centre d'un carré qu'elle a dessiné.
# La taille et la position du carré doivent être reçus en paramètre.
def centerTurtle(n):
    avancerTortue(n)
    tournerTortue()
    avancerTortue(n)
    tournerTortue()
    avancerTortue(n)
    tournerTortue()
    avancerTortue(n/2)
    tournerTortue()
    avancerTortue(n/2)
    tournerTortue()

print centerTurtle(80)


# 7. Définir une fonction qui calcule le polynôme x² + 5x - 4
def findX(x):
    return (x**2 + 5*x - 4)
print findX(3)
# def findValue(a, b, c):
#     return ((-b + sqrt(b**2 - 4*a * c)/2*a), (-b- sqrt(b**2 - 4*a * c)/2*a))
#
# print findValue(1, 5, -4)



# 8. Définir une fonction qui calcul le périmètre d'un rectangle à partir des longueurs de ses côtés.
def rectangleScope(v, u):
    return ((v+u)*2)
print rectangleScope(3, 6)


# 9. Définir une procédure qui fait dessiner la lettre A en majuscule à la tortue, avec un facteur
# d'échelle reçu en paramètre. Pour tourner la tortue d'un angle qui n'est pas multiple de 90 degrés,
# utilisez la procédure tournerTortueDegres(angle).
nouveauCanevas()
ajouterTortue()
def turtleDrawing():
    avancerTortue(40)
    tournerTortue(degrees(90))
    avancerTortue(40)
    tournerTortue(degrees(120))
    avancerTortue(degrees(90))
    tournerTortue(degrees(60))
    avancerTortue(degrees(45))
    tournerTortue()
    avancerTortue(degrees(90))
    tournerTortue()


# 10. Entrez des nombres réels dans l'interpréteur jusqu'à ce que vous découvriez la plus petite fraction
# décimale pouvant être représentée fidèlement dans python (aucun arrondi). Faites de même pour la représentation d'un
# très grand nombre. Définissez une constante pour chacun de ces nombres. Vous pouvez écrire des nombres en notation
# scientifique directement dans l'interpréteur: 5e-3 = 0.005, et 5e+3 = 5000, par exemple.

# 11. Écrivez une fonction qui retourne True si et seulement si une seule des deux valeurs (p ou q) reçue en paramètre
# est elle-même True. Utilisez les opérations logigues or, and et not pour réaliser cette tâche.
def booleanOutput(p, q):
    if p or q:
        return True
    else:
        return False
print booleanOutput(False, False)


# 12. Écrivez une fonction qui produit True si la valeur de son paramètre se trouve entre 100 et 500 et False sinon.
def outputBoolean(x):
    rangeValue = range(100, 500)
    if x < 100 or x > 500:
        return False
    else :
        return True

print outputBoolean(150)

# 13. Écrivez une fonction de x et y qui produit True si la valeur de x est un multiple de la valeur de y.
def boolOutput(x, y):
    if (x%y == 0):
        return True
    else :
        return False
print boolOutput(10, 5)


# 14. Calculez quantité de carburant qu'une fusée idéale a besoin pour envoyer en orbite à une vitesse non-relativiste un cargo.
# Utilisez l'équation de Tsiolkovsky: https://fr.wikipedia.org/wiki/%C3%89quation_de_Tsiolkovski
# Assumez qu'on utilise un moteur Merlin 1-D au sol : https://fr.wikipedia.org/wiki/Merlin_(moteur-fus%C3%A9e)#Merlin_1D
# Assumez que le delta-v désiré est 9700 m/s (nécessaire pour orbite basse).
# Dans l'équation de Tsiolkovsky, on s'intéresse donc à obtenir mi - mf (masse du carburant seulement).
# Placez toutes vos constantes dans un dictionnaire appelé ParametresFusee et utilisez-les dans votre fonction.
# Votre fonction devrait s'appeler ProportionCargo, et prendre en paramètre la masse du cargo (en tonnes).
# Séparez le travail en plusieurs sous-fonctions si possible et évitez complètement de définir des symboles
# pour vos résultats intermédiaires. N'oubliez pas la masse du moteur (470 kg)!


