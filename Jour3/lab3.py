#!/usr/bin/python
# -*- coding: UTF-8 -*-

#from ift099 import *
from math import *
from ift099 import *





# 1. définir une fonction qui affiche tous les multiples positifs de 3 inférieurs à une certaine valeur
#    reçue en paramètre

def multipleOfThree(limitValue):

  x = range(limitValue)
  for i in x:
    if i % 3 == 0:
      print i
  else:
      pass
print multipleOfThree(15)
# 2. définissez une fonction qui produit un arrondi d'un nombre décimal reçu en paramètre à l'entier le plus près.
#    Vous pouvez séparer les parties entières et fractionnaire d'un nombre réal à l'aide de l'opérateur de quotient (//).
#    L'entier le plus près de 1.3 est 1, l'entier le plus près de 1.7 est 2. (séparé à 0.5).
def roundValue(value):
  return round(value)

print roundValue(13.7)


# 3. définissez une fonction qui calcule les racines d'un polynôme quadratique de la forme ax**2 + bx + c.
#    Vous devez retourner les racines sous forme de liste. S'il n'y a qu'une racine, retournez seulement
#    la valeur de la racine unique. Si les racines sont imaginaires, retournez None, et affichez un message d'erreur.
def findRacineValue(a, b, c):
    computeDelta = b**2 - 4*a*c

    if (computeDelta) == 0:
     return -b/2*a
    elif computeDelta < 0:
      return "l'equation n'admet pas de solution dans R"
    elif (computeDelta) > 0:
      return [(-b + sqrt(b**2 - 4*a * c)/2*a), (-b- sqrt(b**2 - 4*a * c)/2*a)]

print findRacineValue(3, 5, 7)

# 4. definissez une fonction qui permet de tracer un rectangle avec la tortue
#   les coordonnes du coin superieur gauche ainsi que les dimensions doivent etre recues en parametre
nouveauCanevas()
ajouterTortue()

def drawRectangle(long, lat):
    avancerTortue(long)
    tournerTortue()
    avancerTortue(lat)
    tournerTortue()
    avancerTortue(long)
    tournerTortue()
    avancerTortue(lat)
    tournerTortue()
    avancerTortue(long)

drawRectangle(120, 60)


# 5. definissez une fonction qui trace un triangle équilateral (longueur des cotes en parametre)
#    avec un des sommet sur les coordonnes (x,y)

def drawTriEqui(x):
  avancerTortue(x)
  tournerTortueDegres(120)
  avancerTortue(x)
  tournerTortueDegres(120)
  avancerTortue(x)
print drawTriEqui(50)
# 6. definissez une fonction qui trace un polygone regulier de N côtés (de longueur paramétrable, avec un sommet a (x,y))
def drawPolygone(x, y):


# 7. definir une fonction qui calcule le rayon d'un polygone regulier (a partir de la longueur d'un cote et du nombre de cotes)
#   reference: http://www.mathopenref.com/polygonradius.html    (leur formule utilise un sin en degres)
#   écrire une fonction qui transforme les degrés en radians est pratique ici.
#       rappel pour la formule: https://en.wikipedia.org/wiki/Radian#Conversions
#   Les fonctions trigonométrique de python s'attendent à recevoir des radians en entrée.

# 8. definir une fonction qui trace un polygone regulier de N cotes (de longueur parametrable, centre sur (x,y) )

# 9. Définissez une fonction qui trace un polygone régulier de N côtés, placé au centre du canevas.

# 10. Définissez une fonction qui fait le même travail qu'en 9, mais vérifie d'abord si votre polygone dépassera
#     le canevas. Si le polygone dépasse le canevas, vous ne devez pas le dessiner, et afficher un message
#     d'erreur à la place.

#11. Définissez une fonction qui calcule le rayon minimal d'un cercle pouvant contenir N cercles de rayon R
#    (ils sont tous identiques).
#    Les ratios optimals connus à dates se trouvent ici:
#    https://en.wikipedia.org/wiki/Circle_packing_in_a_circle

#12. Définissez une fonction qui dessine avec la tortue la lettre A, la lettre O, la lettre L ou la lettre H,
#    selon la lettre que vous avez reçue en paramètre.

#13. Définissez une fonction qui dessine du texte sur le canevas, seulement avec les lettres A,O,L et T.
#    Exemple de texte valide: "aloha"


#14. Écrivez une fonction qui utilise la solution du jour 2 pour calculer la quantité de combustible dans une
# fusée pour déterminer la hauteur de la citerne qui contiendrait le combustible.
# Assumez que la densité du combustible est de 1g/ml. Assumez que le diamètre d'un moteur (et donc de la citerne)
# est de 1m.

#15. Écrivez une fonction qui calcule combien de moteurs seraient nécessaires pour lever un certain poids dans le
# champ de gravité de la terre. Un moteur Merlin 1-D a une poussée de 470 kN.

#16. Écrivez une fonction qui dessine une fusée, avec une taille proportionnelle au cargo qu'elle transporterait,
#   et au nombre de moteurs nécessaire pour qu'elle décolle.
# Le rayon de la citerne est déterminé par le nombre de moteurs nécessaires à lever la fusée au complet.
# Le nombre de moteurs visibles de profil devrait être déterminé ainsi que le rayon de la citerne sont déterminés
# par votre fonction qui calcule le nombre de cercles qu'on peut mettre dans un cercle.


