# importer les différents modules requis pour commencer la réalisation
from turtle import *
import turtle as tur
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
screen = tur.Screen()
screen.title('Snake Game')
screen.bgcolor('black')

#la taille en largeur (width) et hauteur (height)
screen.setup(width = 600, height = 600)
screen.tracer(0)

