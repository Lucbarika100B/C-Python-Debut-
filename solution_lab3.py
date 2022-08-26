#!/usr/bin/python
# -*- coding: UTF-8 -*-

from ift099 import *
from math import *

# 1. définir une fonction qui affiche tous les multiples positifs de 3 inférieurs à une certaine valeur
#    reçue en paramètre
def afficheMultiples3(n):
    for x in range(n):
        if(x%3==0):
            print x


# 2. définissez une fonction qui produit un arrondi d'un nombre décimal reçu en paramètre à l'entier le plus près.
#    Vous pouvez séparer les parties entières et fractionnaire à l'aide de l'opérateur de quotient (//).
#    L'entier le plus près de 1.3 est 1, l'entier le plus près de 1.7 est 2. (séparé à 0.5).
def fraction(x):
    return x-x//1.0
def entier(x):
    return x-fraction(x)

def arrondi(x):
    if(fraction(x)>=0.5):
        return entier(x)+1
    else:
        return entier(x)


# 3. définissez une fonction qui calcule les racines d'un polynôme quadratique de la forme ax**2 + bx + c.
#    Vous devez retourner les racines sous forme de liste. S'il n'y a qu'une racine, retournez seulement
#    la valeur de la racine unique. Si les racines sont imaginaires, retournez None, et affichez un message d'erreur.

def det(a,b,c):
    return b**2 - 4*a*c

def racineQuadPos(a,b,c):
    return (-b + sqrt(det(a,b,c)))/(2*a)

def racineQuadNeg(a,b,c):
    return (-b - sqrt(det(a,b,c)))/(2*a)

def racineQuad(a,b,c):
    if(det(a,b,c)<0):
        print "Erreur: déterminant négatif"

    elif(det(a,b,c)==0):
        return racineQuadPos(a,b,c)

    else:
        return (racineQuadPos(a,b,c),racineQuadNeg(a,b,c))


# 4. definissez une fonction qui permet de tracer un rectangle avec la tortue
#   les coordonnes du coin superieur gauche ainsi que les dimensions doivent etre en parametre
nouveauCanevas()
def tracerRectangle(x, y, tailleX, tailleY):

    ajouterTortue(x,y)
    for i in range(2):
        demiRectangle(tailleX,tailleY)

def demiRectangle(tailleX,tailleY):
    avancerTortue(tailleX)
    tournerTortueDegres(90)
    avancerTortue(tailleY)
    tournerTortueDegres(90)


# 5. definissez une fonction qui trace un triangle équilateral (longueur des cotes en parametre)
#    avec un des sommet sur les coordonnes (x,y)

def triangle(x, y, taille):

    ajouterTortue(x,y)
    for i in range(3):
        avancerTortue(taille)
        tournerTortueDegres(120) # complement de l'angle interieur (60°)



# 6. defninir une fonction qui trace un polygone regulier de N côtés (de longueur paramétrable, avec un sommet a (x,y) )

def polygone(N,taille):
    for i in range(N):
        avancerTortue(taille)
        tournerTortueDegres(360.0/N)

def polygonePositionne(x, y, N, taille):
    nouveauCanevas()
    ajouterTortue(x,y)
    polygone(N,taille)

# 7. definir une fonction qui calcule le rayon d'un polygone regulier (a partir de la longueur d'un cote et du nombre de cotes)
#   reference: http://www.mathopenref.com/polygonradius.html    (leur formule utilise un sin en degres)
#   écrire une fonction qui transforme les degrés en radians est pratique ici.
#       rappel pour la formule: https://en.wikipedia.org/wiki/Radian#Conversions
def rayonPolygone(taille, N):
    return taille / (2. * sin(angleRadian(180)/N))

# 8. definir une fonction qui trace un polygone regulier de N cotes (de longueur parametrable, centre sur (x,y) )

def angleRadian(degres):
    return degres*pi/180.


# 9. Définissez une fonction qui trace un polygone régulier de N côtés, placé au centre du canevas.
def sommeAnglesInterieur(N):
    return N * (180 - 360. / N)


def angleInterieur(N):
    return sommeAnglesInterieur(N) / N


def polygoneCentre(x, y, N, taille):

    rayon = rayonPolygone(taille, N)
    ajouterTortue(x, y - rayon)
    angleInitial = 90 - angleInterieur(N) / 2
    tournerTortueDegres(angleInitial)
    polygone(N,taille)


def polygoneCentreCanevas(N,taille):
    polygoneCentre(400,300,N,taille)

#polygoneCentreCanevas(5,100)

# 10. Définissez une fonction qui fait le même travail qu'en 9, mais vérifie d'abord si votre polygone dépassera
#     le canevas. Si le polygone dépasse le canevas, vous ne devez pas le dessiner, et afficher un message
#     d'erreur à la place.

def polygoneCentreCanevasVerif(N,taille):
    if(rayonPolygone(taille,N)>300):
        print "Le polygone va dépasser"
    else:
        polygoneCentreCanevas(N,taille)

#polygoneCentreCanevasVerif(5, 500)


#11. Définissez une fonction qui calcule le rayon minimal d'un cercle pouvant contenir N cercles de rayon R
#    (ils sont tous identiques).
#    Les ratios optimals connus à dates se trouvent ici:
#    https://en.wikipedia.org/wiki/Circle_packing_in_a_circle
coefficients = (0,1,0.5,0.6466,0.6864,0.6854,0.6667,0.7778,0.7328,0.6895,0.6878,0.7148,0.7392,0.7245,0.7474,0.7339,0.7512,0.7403,0.7611,0.8034,0.7623)
print len(coefficients)
def rayonCercledansCercle(petitRayon,N):
    if(N >0 and N<=20):
        return sqrt((petitRayon**2)*N/coefficients[N])
    else:
        return 0


print rayonCercledansCercle(1,9)

#12. Définissez une fonction qui dessine avec la tortue la lettre A, la lettre O, la lettre L ou la lettre H,
#    selon la lettre que vous avez reçue en paramètre.

#13. Définissez une fonction qui dessine du texte sur le canevas, seulement avec les lettre A,O,L et T.
#    Exemple de texte valide: "aloha"
ajouterTortue(100,100)
def dessinerA():
        tournerTortueDegres(300)
        avancerTortue(50)
        tournerTortueDegres(120)
        avancerTortue(50)
        tournerTortueDegres(180)
        avancerTortue(25, True)
        tournerTortueDegres(-60)
        avancerTortue(25)
        tournerTortueDegres(270)
        avancerTortue(25*sin(60*pi/180),True)
        tournerTortueDegres(270)
        avancerTortue(50,True)


def dessinerL():

    tournerTortueDegres(-90)
    avancerTortue(40)
    tournerTortueDegres(180)
    avancerTortue(40,True)
    tournerTortueDegres(-90)
    avancerTortue(30)

def dessinerO():
    tournerTortueDegres(-90)
    avancerTortue((rayonPolygone(3,50)*2),True)
    tournerTortueDegres(90)
    avancerTortue((rayonPolygone(3,50)),True)
    polygone(50, 3)
    tournerTortueDegres(90)
    avancerTortue((rayonPolygone(3,50)*2),True)
    tournerTortueDegres(-90)
    avancerTortue((rayonPolygone(3, 50)), True)


def dessinerH():
    tournerTortueDegres(-90)
    avancerTortue(40)
    tournerTortueDegres(180)
    avancerTortue(20,True)
    tournerTortueDegres(-90)
    avancerTortue(30)
    tournerTortueDegres(-90)
    avancerTortue(20)
    tournerTortueDegres(180)
    avancerTortue(20,True)
    avancerTortue(20)
    tournerTortueDegres(-90)


def dessinerTexte(texte):
    for lettre in texte:
        if(lettre == 'a'):
            dessinerA()

        elif(lettre == 'l'):
            dessinerL()

        elif(lettre == 'o'):
            dessinerO()

        elif(lettre == 'h'):
            dessinerH()
        else:
            print "Erreur: lettre indessinable:"+lettre

        avancerTortue(5,True)

#dessinerTexte("alolohahaha")

#14. Écrivez une fonction qui utilise la solution du jour 2 pour calculer la quantité de combustible dans une
# fusée pour déterminer la hauteur de la citerne qui contiendrait le combustible.
# Assumez que la densité du combustible est de 1g/ml. Assumez que le diamètre d'un moteur (et donc de la citerne)
# est de 1m.

def calculerHauteurCiterne(rayon,litresCombustible):
    return (litresCombustible/ (rayon**2.0*pi))/1000.0


#15. Écrivez une fonction qui calcule combien de moteurs seraient nécessaires pour lever un certain poids dans le
# champ de gravité de la terre. Un moteur Merlin 1-D a une poussée de 900 kN.
def calculerMoteurs(cargo):
    return cargo*9.8 / 900000

#16. Écrivez une fonction qui dessine une fusée, avec une taille proportionnele au cargo qu'elle transporterait,
#   et au nombre de moteurs nécessaire pour qu'elle décolle.

ParametresFusee = {'Deltav':9700.0, 'VitesseGasMoteur':2766.0, 'MasseMoteur' : 470.0}

def calculerProportionMasse(masseCargo):
    return e**(-ParametresFusee['Deltav'] / ParametresFusee['VitesseGasMoteur'])

def calculerMasseCombustible(masseCargo):
    return (calculerMasseSeche(masseCargo)/calculerProportionMasse(masseCargo))-calculerMasseSeche(masseCargo)

def calculerMasseSeche(masseCargo):
    return ParametresFusee['MasseMoteur']+masseCargo

print calculerMasseCombustible(5000)
print calculerHauteurCiterne(1,calculerMasseCombustible(5000))

def profilMoteurs(n):
    return (int)(ceil(rayonCercledansCercle(1, n)))


def dessinerCargo(largeur):
    tournerTortueDegres(-60)
    polygone(3,largeur*echelle[0])
    tournerTortueDegres(60)

def dessinerCiterne(hauteur,largeur):

    for i in range(2):
        demiRectangle(largeur*echelle[0],hauteur*echelle[1])

    tournerTortueDegres(90)
    avancerTortue(hauteur*echelle[1],True)
    tournerTortueDegres(-90)
    avancerTortue(10,True)



def dessinerMoteur():
    tournerTortueDegres(125)
    avancerTortue(20)
    tournerTortueDegres(180)
    avancerTortue(20,True)
    tournerTortueDegres(55)
    avancerTortue(20)
    tournerTortueDegres(180)
    avancerTortue(20, True)
    tournerTortueDegres(180)
    tournerTortueDegres(60)
    avancerTortue(10)
    tournerTortueDegres(-120)
    avancerTortue(10)
    tournerTortueDegres(120)
    avancerTortue(10)
    tournerTortueDegres(-120)
    avancerTortue(10)
    tournerTortueDegres(115)
    avancerTortue(20)
    tournerTortueDegres(180)
    avancerTortue(20,True)
    tournerTortueDegres(125)
    avancerTortue(22,True)


   # avancerTortue(100,True)

echelle=(52,10)
def dessinerFusee(masseCargo):

    combustible = calculerMasseCombustible(masseCargo)
    moteurs =(int)(calculerMoteurs(masseCargo + combustible))+1
    largeur=rayonCercledansCercle(1, moteurs)
    hauteur = calculerHauteurCiterne(largeur,combustible)
    ajouterTortue(350, 2*rayonPolygone(echelle[0]*largeur,3))
    dessinerCargo(largeur)
    dessinerCiterne(hauteur,largeur)

    for i in range(profilMoteurs(moteurs)):
        dessinerMoteur()


dessinerFusee(10000)