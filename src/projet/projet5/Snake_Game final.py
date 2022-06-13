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

# création de la tête du snake (head) avec la forme, la couleur, la position et la vitesse 
head = tur.Turtle()
head.shape('square')
head.color('green')
head.goto(0, 0)
head.penup()
head.speed(0)
head.direction = 'stop'

# création de la nourriture (food) avec forme, couleur
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0, 100)