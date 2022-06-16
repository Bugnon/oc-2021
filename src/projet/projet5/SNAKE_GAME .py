# importer des modules requis pour la création du jeu 
from turtle import Turtle, Screen
import turtle
import time
import random
from turtle import *

# position initiale (x, y)
POSITIONS = [(0, 0)]

# une grille de 29 x 29 
state = []

for i in range(29):
    state.append([0] *29)
    
for line in state:
    print(line)
     
# la classe Segment qui hérite de Turtle 
class Segment(Turtle):
    def __init__(self):
        super(). __init__()
        self.shape('square')
        self.color('green')
        self.penup()

# la classe Snake 
class Snake:
    # définir init de la classe Snake 
    def __init__ (self):
        self.parts = []
        self.call()
        self.head = self.parts[0]

    # fonction call pour appeler à créer un snake            
    def call(self):
        for x in POSITIONS:
            self.create_snake(x)
    
    # fonction pour la création du snake (color, shape, position)
    def create_snake(self, position):
        snake = Turtle()
        snake.color('green')
        snake.shape('square')
        snake.penup()
        snake.goto(position)
        self.parts.append(snake)

    # fonction pour faire les mouvement du snake    
    def move(self):
        for i in range(len(self.parts) -1, 0, -1):
            new_x = self.parts[i-1].xcor()
            new_y = self.parts[i-1].ycor()
            self.parts[i].goto(new_x, new_y)
        self.head.forward(20)

    # en haut     
    def up(self):
        self.head.setheading(90)

    # en bas    
    def down(self):
        self.head.setheading(270)

    # à gauche     
    def left(self):
        self.head.setheading(180)

    # à droite     
    def right(self):
        self.head.setheading(0)

    # fonction qui permet de rajouter un segment à chaque fois qu'il mange       
    def grow(self):
        s = Segment()
        self.parts.append(s)

    # vérifier les collisions entre le snake et le corps     
    def check_collision(self):
        if len(self.parts) < 3 :
            return False
        for i in range (2, len(self.parts)):
            if self.head.distance(self.parts[i]) < 20:
                return True
        return False 

# la classe Food qui hérite de Turtle                               
class Food(Turtle):
    def __init__(self):
        super(). __init__()
        self.shape('circle')
        self.color('red')
        self.penup()
    
    # à chaque collision entre Food et Snake, le Food admet une nouvelle position (nouveaux et nouveauy)
    def refresh(self):
        new_x = random.randint(-280, 280)
        new_y = random.randint(-280, 280)
        self.goto(new_x, new_y)
        
# la classe Score qui hérite Turtle        
class Score(Turtle):
    def __init__(self):
        super().__init__()        
        self.color('black')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(-60, 270)
        self.update()

    # fonction pour mettre à jour le score         
    def update(self):
        self.clear()
        self.write(f"Score:{self.score}", font = ('Arial', 28, 'bold'))

    # fonction game over    
    def game_over(self):
        self.clear()
        self.write(f"Game Over", font = ('Arial', 28, 'bold'))

# la classe Chrono qui hérite de Turtle 
class Chrono(Turtle): 
    # 2 variables  
    def __init__(self, max_value): 
        super().__init__()   
        self.value = max_value
        self.speed(0)
        self.penup()
        self.goto(-250, 260)
        # mettre en marche la fonction de manière immédiate dans le jeu 
        ontimer(self.tick)

    # réécrire la valeur actuelle (max value qui diminue de 1 par 1)    
    def tick(self):
        self.clear()
        self.write(self.value, align='center', font = ('arial', 28, 'normal'))
        self.value -= 1
        # vérifier que la valeur est supérieur à 0 et que tick est toujours actif 
        if self.value >= 0: 
            # exécuter la fonction tic après 1 sec 
            ontimer(self.tick, 1000) 

    # focntion qui permet d'arrêter le jeu si la value devient négatif 
    def isFinished(self):
        return self.value < 0
               
# affichage du jeu
# écran (screen)
screen = Screen()
screen.setup(height = 600, width = 600)
screen.bgcolor('white')
screen.tracer(0)

snake = Snake()
score = Score()
food = Food()
food.refresh()

# onkey 
screen.listen()
screen.onkey(key='Up', fun = snake.up)
screen.onkey(key='Down', fun = snake.down)
screen.onkey(key='Left', fun = snake.left)
screen.onkey(key='Right', fun = snake.right)

game_is_on = True

# la durée du jeu est de 60 secondes 
counter = Chrono(60)

# boucle pour le lancement du jeu     
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # collision avec le snake et le food    
    if snake.head.distance(food) < 20:
        food.refresh()
        # ajouter +10 au score 
        score.score += 10
        score.update()
        snake.grow()
            
    snake.move()

    # arrêter le jeu après des conditions             
    if counter.isFinished() or snake.check_collision() or snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        break

# game over 
score.game_over()
screen.exitonclick() 