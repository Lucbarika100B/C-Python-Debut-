#!/usr/bin/python
# -*- coding: UTF-8 -*-


from ift099 import *
from math import *
from statistics import *

# 1. faire la somme des 100 premiers nombres pairs
def sumPairNumbers(n):
    total = 0
    for i in range(n):
        total = 2 * i + total
    return total
print sumPairNumbers(100)

# 2. faire la somme des nombres de 0 à -100
def sumFromZero():
    listeTotal = 0
    for i in range(0, -100, -1):
        listeTotal = listeTotal + i
    return listeTotal
print sumFromZero()

# 3. faire une fonction qui retourne la liste des nombres premiers inferieurs a n (exclus).


# 4. écrire une fonction qui retourne le plus petit élément d'une liste reçue en paramètre.
def minOfList(n):
    return min(n)
print minOfList([3, 5, 1, 0, -1])

# 5. écrire un programme qui retourne l'écart-type d'une liste de nombres entrés au clavier. Divisez le programme en
#    3 modules, chacun implanté dans une fonction:
#    a) obtenir la liste de nombres
#    b) calculer la moyenne de la liste
#    c) calculer l'écart-type de la liste.
def findEcartType(l):
    return statistics.pstdev(l)
print findEcartType([1, 2, 3, 5, 8, 7])


# 6. écrire un programme qui détermine si un mot est un palindrôme. Le mot en question sera
#    lu au clavier. Le programme affiche "Est un palindrôme" ou "N'est pas un palindrôme" selon
#    le cas.

# 7. Écrire une fonction filtrer(liste, predicat) qui produit une liste des valeurs pour lesquelles le prédicat est
#    vrai. Par exemple, si le prédicat est x%2==1, et la liste est [1,2,3,4,5] alors les nombres qui seront dans la
#    liste résultante seront: 1,3,5. Inspirez-vous de la fonction appliquer dans les exemples pour le faire.

# 7a.Utilisez la fonction filtrer pour produire la liste des nombres premiers inférieurs à 100.


# 8. écrire un programme qui classifie un triangle: équilatéral, isocèle, rectangle, scalène.
#     Un triangle peut avoir plusieurs de ces qualités.
#     Votre programme devrait lire au clavier les informations décrivant le triangle.
#     Ces informations peuvent prendre plusieurs formes: coordonnées des sommets? Longueur
#     des côtés et angles? 6 paramètres séparés, ou 3 couples (x,y)? Ou 2 listes (longueurs et angles)?
#     Tout dépend de l'approche que vous prenez pour faire le traitement.
#     Le programme affiche à l'aide de print les qualités du triangle.
