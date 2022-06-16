# importer des modules requis pour la création du jeu 
from turtle import Turtle, Screen
import turtle
import time
import random
from turtle import *

# une position initial (snake)
POSITIONS = [(0, 0)]

# la classe Segment qui hérite de Turtle 
class Segment(Turtle):
    def __init__(self):
        super(). __init__()
        self.shape('square')
        self.color('green')
        self.penup()
        
# la classe Snake 
class Snake:
    def __init__ (self):
        self.parts = []
        self.call()
        self.head = self.parts[0]

    # appeler pour la création du snake                 
    def call(self):
        for x in POSITIONS:
            self.create_snake(x)

     # création du snake    
    def create_snake(self, position):
        snake = Turtle()
        snake.color('green')
        snake.shape('square')
        snake.penup()
        snake.goto(position)
        self.parts.append(snake)

    # définir ses mouvement: en bas, en haut, à droite et à gauche        
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

#         
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

    # fonction qui permet de refaire un nouveau food (avoir un nouveau x et un nouveau y)   
    def refresh(self):
        new_x = random.randint(-280, 280)
        new_y = random.randint(-280, 280)
        self.goto(new_x, new_y)
        
 # la classe Score qui hérite de Turtle        
class Score(Turtle):
    def __init__(self):
        super().__init__()        
        self.color('black')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(-60, 270)
        self.update()

    # mettre à jour le score            
    def update(self):
        self.clear()
        self.write(f"Score:{self.score}", font = ('Arial', 28, 'bold'))

     # game over        
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
        # faire marcher la fonction tick toute de suite dans le jeu 
        ontimer(self.tick)

    # réécire la valuer actuelle (max value qui diminue 1 par 1)     
    def tick(self):
        self.clear()
        self.write(self.value, align='center', font = ('arial', 28, 'normal'))
        self.value -= 1
        #tant que la valeur est supérieur à 0, tick est toujours actif 
        if self.value >= 0: 
            #exécuter la fonction tic après 1 sec 
            ontimer(self.tick, 1000)

    def isFinished(self):
        return self.value < 0

# affichage du jeu (taille et la couleur de l'écran)               
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

# la durée du jeu: 60 secondes 
counter = Chrono(60)

# lancement du jeu (pendant que le jeu est actif)    
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # collision entre le Snake et le Food/ changement du score     
    if snake.head.distance(food) < 20:
        food.refresh()
        score.score += 10
        score.update()
        snake.grow()
            
    snake.move()
                
    if counter.isFinished() or snake.check_collision() or snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        break
score.game_over()
screen.exitonclick() 