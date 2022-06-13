# importer des modules requis pour la création du jeu 
from turtle import *
import turtle as tur
import time
import random 

# définir le retard, le score et le meilleur score du point initial
delay = 0.1
score = 0
high_score = 0

# construire l'affichage du jeu 
# l'écran (screen) 
screen = tur.Screen()
# titre du jeu 
screen.title('Snake Game') 
# couleur de fond du jeu 
screen.bgcolor('black')

#la taille de l'écran en largeur (width) et en hauteur (height)
screen.setup(width = 600, height = 600)
screen.tracer(0)

