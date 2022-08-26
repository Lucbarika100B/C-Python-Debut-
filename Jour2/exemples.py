#!/usr/bin/python
# -*- coding: UTF-8 -*-
from ift099 import *
from math import *

#imbrication, f rond g
def f(x):
    return x + 2
def g(x):
    return 3*f(x)-f(x)

print f(g(5))

#À compléter en démo: def moyenne(a,b) ...
def moyenne(a,b):
    return (a+b)/2

print moyenne(10,2)

#Exemple de dessin d'un carre
nouveauCanevas()
ajouterTortue()

def carre(n):
    avancerTortue(n)
    tournerTortue()
    avancerTortue(n)
    tournerTortue()
    avancerTortue(n)
    tournerTortue()
    avancerTortue(n)
    tournerTortue()

carre(100)



maliste =[3,7,2.3,"fleur"]

mondicto = {'prenom': maliste, 'nom': "AuTibet", 'pages': 54}

