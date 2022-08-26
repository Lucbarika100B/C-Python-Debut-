#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: Alexandre Huppe
# Description: Library created for Universite de Sherbrooke's IFT099 class
#
# Copyright (c) 2015 Alexandre Huppe <Alexandre.Huppe@USherbrooke.ca>
# All rights reserved. No warranty, explicit or implicit, provided.

# explicitely defines what can be imported via "from ift099 import *"
__all__ = ['lireEntier','lireReel','lireTexte','apply','tournerTortueDegres','nouveauCanevas', 'fermerCanevas', 'tracer', 'ajouterTortue', 'avancerTortue', 'tournerTortue', 'infoTortue','readInteger','readDecimal','readText','generateList']

import Tkinter
from threading import Thread
from math import cos, sin, pi



# created with imageToText function (see below)... to be used by Tkinter.PhotoImage()
# from http://www.iconarchive.com/tag/mouse, more precisely: http://icons.iconarchive.com/icons/martin-berube/flat-animal/128/mouse-icon.png
# (since we aren't using object oriented programming... let's use functions only...)
# ... and we'll still need to store some info... we'll be using this class to store them

TURTLE_ICON= '''R0lGODlhIAAgAPcAAAAAAAEBAQICAgMDAwQEBAUFBQYGBgcHBwgICAkJCQoKCgwMDA0NDRAQEBERERISEhMTExUVFRYWFhoaGhwcHB0dHR4eHh8fHyEhISIiIiMjIyYmJicnJykpKSoqKisrKy0tLS4uLi8vLzAwMDExMTU1NTY2Njg4ODw8PD09PUBAQEFBQUJCQkVFRUZGRkdHR0lJSUpKSktLS01NTVBQUFNTU1RUVFZWVldXV1lZWVpaWl5eXl9fX2BgYGFhYWNjY2ZmZmhoaGlpaWpqamtra25ubm9vb3BwcHFxcXh4eHl5eXx8fH19fX9/f4CAgIGBgYKCgoSEhIaGhoqKiouLi4yMjI2NjY+Pj5GRkZOTk5SUlJWVlZaWlpeXl5iYmJmZmZqampubm5ycnJ6enp+fn6CgoKKioqOjo6SkpKampqenp6urq62trbCwsLGxsbW1tba2trm5ubq6uru7u729vb+/v8HBwcLCwsXFxcfHx8nJyczMzM3NzdDQ0NHR0dLS0tPT09TU1NbW1tjY2NnZ2dra2tvb29/f3+Dg4OHh4eLi4uPj4+Tk5Obm5ufn5+jo6Onp6erq6uvr6+zs7O3t7e7u7vDw8PHx8fLy8vPz8/T09PX19ff39/j4+Pn5+fr6+vv7+/z8/P7+/v///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACwAAAAAIAAgAAAI/wBHCRxIsKDBgwgTKlzIsKHDhxAjSnTICU+eTxMR1pEAAECEMBkLImIgoxAgIAGcKBzERQgNGkHMZDLow8KmgVUC5DEY6ssHAAlK2MBhgkCDLwQnHcgycE8bEjYKDhpBQMccTwQfEQmQZKCXA5YGeuDagOAfByH8JNwCAAyoUSxmEISTZQ2AgZowlJip8AYAEYEEpDH4JMJAKAsWMex0B0CDDJxGUSHBaFQeB0UGWjDiEJBHQKOuAIBgYAKAFHwXAZDTUI6EDYZGyRnAJFMZKXFEDewDQNBCSD8CzKg0alOFGAkPAaCTMFKSBRHIDJySQDHCRgSGGBRlhweCBk4uEbrUEEQhkwiKBkpiE8S0hyuYChICUEehlQI3dry4ACAAiCR7IOQGAPEh1MUCELjQQg5NtPHIQmfchZARHcGAxU0O0QFAIgh1sAIPMBSghECaaGKQI2a0IVAlA6CxECADnDEKJx0IYMEJK6hQQgQdPYDVKCjUoFAoIYgQyihDKCBGFEP00EMRVLzBBwFTCLTFAZQkJAgAFIzw0xgJLRFACCNwAIAeCmlxxBFIuLGQGkiwKWNIdNZp550ZBQQAOw=='''

class CanevasVars():
    '''this class is only a container, in C++ it would be a struct)'''
    turtleDirections = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    turtleDirectionText = ['droite', 'bas', 'gauche', 'haut']
    def __init__(self):
        self._clear()
        
    def _clear(self):
        self.canvas = None
        self.tortue = None
        
    
myCanevas = CanevasVars()   # this is the only instance of CanevasVars...since this lib only support one canvas at a time

def angleRadian(degres):
    return degres*pi/180.

def nouveauCanevas(largeur=800, hauteur=600, couleurFond='white'):
    '''cree un nouveau canevas avec les dimension et couleur d'arriere plan passes en parametre
    
    Note: un seul canevas ne peut etre actif a la fois'''
    if myCanevas.canvas:    # si un canevas existe deja, le fermer pour en ouvrir un autre
        fermerCanevas()
    myCanevas.root = Tkinter.Tk()
    # http://stackoverflow.com/questions/4643007/intercept-tkinter-exit-command
    myCanevas.root.wm_protocol ("WM_DELETE_WINDOW", fermerCanevas)
    # http://www.tutorialspoint.com/python/tk_canvas.htm
    myCanevas.canvas = Tkinter.Canvas(myCanevas.root, bg=couleurFond, height=hauteur, width=largeur)
    myCanevas.canvas.pack(expand=1, fill=Tkinter.BOTH)  # make it expandable
    myCanevas.thread = Thread(target=myCanevas.root.mainloop)
    myCanevas.thread.start()
    
def fermerCanevas():
    '''ferme le canevas actif'''
    if myCanevas.canvas:
        try:
            myCanevas.root.destroy()        # stop the mainloop and close the window
            myCanevas.thread.join()         # make sure the thread is done
        except Tkinter.TclError:
            pass    # can appear if the windows was closed via the x button
        except RuntimeError:
            pass    # can appear if the windows was closed via the x button
        myCanevas._clear()
    else:
        raise Exception('Pas de canevas ouvert')
        
def tracer(x1, y1, x2, y2):
    '''permet de tracer une ligne de (x1,y1) vers (x2,y2) sur le canevas actif'''
    if myCanevas.canvas:
        myCanevas.canvas.create_line(x1, y1, x2, y2)
    else:
        raise Exception('Pas de canevas ouvert')
    
def ajouterTortue(x=49, y=51):
    '''ajoute une tortue sur le canevas, centree sur la position (x,y)'''

    if myCanevas.canvas:

        myCanevas.tortue = {'x': x,
                          'y': y,
                          'icon': Tkinter.PhotoImage(data=TURTLE_ICON),  # http://effbot.org/tkinterbook/photoimage.htm
                          #'icon': Tkinter.PhotoImage(file="Turtle-icon.gif"),
                          'direction': (1,0),  # (x multiplier, y multiplier) for the move call (see below)
                            }
        myCanevas.tortue['reference'] = myCanevas.canvas.create_image(x, y, image=myCanevas.tortue['icon'])
        myCanevas.tortue['angle'] = 0
    else:
        raise Exception('Pas de canevas ouvert')
        
def avancerTortue(distance, saut=False):
    '''avance la tortue sur le canevas de 'distance' pixels

    Cree aussi une ligne, sauf si le parametre 'saut' est evalue a vrai'''
    if myCanevas.tortue:
        # http://stackoverflow.com/questions/23275445/move-an-image-in-python-using-tkinter
        directionMultiplier = myCanevas.tortue['direction']
        x, y = distance*directionMultiplier[0], distance*directionMultiplier[1] # get x and y values, according to current direction
        myCanevas.canvas.move(myCanevas.tortue['reference'], x, y)
        newX, newY = myCanevas.tortue['x'] + x, myCanevas.tortue['y'] + y
        if not saut:
            tracer(myCanevas.tortue['x'], myCanevas.tortue['y'], newX, newY)
        myCanevas.tortue['x'], myCanevas.tortue['y'] = newX, newY
    else:
        raise Exception('Pas de tortue')
    
def tournerTortue(horaire=True):
    '''Tourne la tortue en prevision du prochain mouvement
    
    Tourne en sens horaire, sauf si 'horaire' est evalue a faux'''
    if myCanevas.tortue:
        index = CanevasVars.turtleDirections.index(myCanevas.tortue['direction'])
        if horaire:
            myCanevas.tortue['direction'] = CanevasVars.turtleDirections[(index + 1) % len(CanevasVars.turtleDirections)]
        else:
            myCanevas.tortue['direction'] = CanevasVars.turtleDirections[(index - 1) % len(CanevasVars.turtleDirections)]
    else:
        raise Exception('Pas de tortue')

def ajouterTortue2(x=49, y=51): # a utiliser avant d'utiliser tournerTortue2 (initialise l'angle)
    ajouterTortue(x, y)
    myCanevas.tortue['angle'] = 0
    
def tournerTortueDegres(angle=90):   # avec valeur par default, correspondant a tournerTortue
    
    myCanevas.tortue['angle'] = (myCanevas.tortue['angle'] + angle) % 360
    # rappel pour les cos et sin: https://en.wikipedia.org/wiki/Trigonometry#Overview
    composantX = cos(angleRadian(myCanevas.tortue['angle']))
    composantY = sin(angleRadian(myCanevas.tortue['angle']))
    
    myCanevas.tortue['direction'] = (composantX, composantY)
        
def infoTortue2():
    '''retourne des informations sur la tortue:
    - position
    - direction du prochain mouvement'''
    
    if myCanevas.tortue:
        return {'position':(myCanevas.tortue['x'], myCanevas.tortue['y']),
                'direction':CanevasVars.turtleDirectionText[CanevasVars.turtleDirections.index(myCanevas.tortue['direction'])],
                'angle': myCanevas.tortue['angle']}
    else:
        raise Exception('Pas de tortue')
        
def infoTortue():
    '''retourne des informations sur la tortue:
    - position
    - direction du prochain mouvement'''
    
    if myCanevas.tortue:
        return {'position':(myCanevas.tortue['x'], myCanevas.tortue['y']),
                'angle':myCanevas.tortue['angle']}
    else:
        raise Exception('Pas de tortue')
        
    
# Utility function (to get the long string representing the mouse icon (on top of this file)
def imageToText(file):

    # http://effbot.org/librarybook/base64.htm
    import base64
    
    return base64.encodestring(open(file, 'rb').read())
    
def valideArbre(arbre):
    '''fonction pour vous permettre de valider et visualiser vos arbres de tests'''
    taille = len(arbre)
    
    if taille == 1:
        return True
    elif taille == 3:
        return valideArbre(arbre[1]) and valideArbre(arbre[2])
    else:
        return False

def readInteger(phrase=''):
    return int(raw_input(phrase))

def lireEntier(phrase=''):
    return int(raw_input(phrase))


def readDecimal(phrase=''):
    return float(raw_input(phrase))

def lireReel(phrase=''):
    return float(raw_input(phrase))

def readText(phrase=''):
    return raw_input(phrase)

def lireTexte(phrase=''):
    return raw_input(phrase)

def generateList(n):
    return [x for x in range(n)]

def apply(function, list):
    result = []
    for i in range(0,len(list)):
        result.append(function(list[i]))
    return result