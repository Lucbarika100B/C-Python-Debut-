#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import division
from ift099 import *


# 1. definir la fonction factorielle de facon recursive
def factorial(n):
    if (n == 0):
        return 1
    elif (n < 0):
        return "FACTORIAL DOES NOT APPLY TO NEGATIVE NUMBERS !"
    else:
        return n * factorial(n - 1)


# 2. definir une fonction qui retourne le n_ieme terme de la suite de fibonnaci
#       rappel: fib(0) == fib(1) == 1, fib(n) = fib(n-1) + fib(n-2)
def fiboSeq(f):
    if (f == 0 or f == 1):
        return 1
    else:
        return fiboSeq(f - 1) + fiboSeq(f - 2)


print fiboSeq(0)
print fiboSeq(1)
print fiboSeq(2)
print fiboSeq(3)
print fiboSeq(4)

# 3. definir une fonction racine carree recursive qui calcule une approximation rationnelle
#	 de la racine carree de N avec la methode babylonienne
print "***********************************************************"


def racineBaby(z, p):
    if float(z / p == p):
        return float(p)
    else:
        return float(((z + p) / p) / 2)


print racineBaby(100, 50)

print " Recursive of  RacineBaby ************************************************************"


def recursiveRacine(d, q):
    if float(abs(d / q) == d):
        return d
    else:
        return d, recursiveRacine(d, (((d + q) / q) / 2))


# 4. Fractals: faire un flocon de Koch

nouveauCanevas(1000, 1000)
ajouterTortue(100, 100)


def tortueKoch(ordre=3, niveau=0, taille=100):
    if niveau == 0:
        tortueKoch(niveau=1, ordre=ordre, taille=taille)
        tournerTortueDegres(120)
        tortueKoch(niveau=1, ordre=ordre, taille=taille)
        tournerTortueDegres(120)
        tortueKoch(niveau=1, ordre=ordre, taille=taille)
    elif niveau <= ordre:
        tortueKoch(niveau=niveau + 1, ordre=ordre, taille=taille)
        tournerTortueDegres(-60)
        tortueKoch(niveau=niveau + 1, ordre=ordre, taille=taille)
        tournerTortueDegres(120)
        tortueKoch(niveau=niveau + 1, ordre=ordre, taille=taille)
        tournerTortueDegres(-60)
        tortueKoch(niveau=niveau + 1, ordre=ordre, taille=taille)
    else:
        avancerTortue(taille / (3 ** (ordre + 1)))


tortueKoch(6, 0, 1200)

# 5. fractal: triangle de Sierpinski
