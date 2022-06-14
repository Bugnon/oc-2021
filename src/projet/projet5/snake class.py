# importer des modules requis pour la création du jeu 
import turtle
import time
import random

# définir le retard, le score et le meilleur score du point initial
delay = 0.1
score = 0
high_score = 0

# Construire l'affichage du jeu
# l'écran (screen)
screen = turtle.Screen()
screen.title('Snake Game')
screen.bgcolor('black')

#la taille en largeur (width) et hauteur (height)
screen.setup(width = 600, height = 600)
screen.tracer(0)

class Snake:
    
    # création du snake (tête) avec forme, couleur, position et vitesse 
    def __init__(self, pos=(0,0), shape = 'square', color = 'green'):
        self.shape = shape
        self.color = color
        self.goto = pos
        self.draw()
        
        
    def draw(self):
        shape(self.shape)
        color(self.color)
        pos(self.pos.x + 20, self.pos.y + 20)
        spped(self.speed)
        write(self. __str__())
        
    def __str__(self):
        return f'Snake({self.pos.x}, {self.pos.y }, {self.shape})'
    
    
Snake()    
        
        
    

