# importer les différents modules pour commencer la réalisation
from turtle import *
import time
import random

# définir le retard, le score et le meilleur score au point initial
delay = 0.1
score = 0
high_score = 0

# définir le retard, le score et le meilleur score au point initial
delay = 0.1
score = 0
high_score = 0

# construire l'affichage du jeu: 
# l'écran 
screen = turtle.Screen()
screen.title('Snake Game')
screen.color('white')

#la taille en largeur (width) et hauteur (height)
screen.setup(width = 600, height = 600)
screen.tracer(0)

