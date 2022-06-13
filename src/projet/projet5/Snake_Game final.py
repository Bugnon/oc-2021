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
screen = tur.Screen()
screen.title('Snake Game')
screen.bgcolor('black')