from turtle import Turtle, Screen
import turtle
import time
import random
from turtle import *

POSITIONS = [(0, 0)]

class Segment(Turtle):
    def __init__(self):
        super(). __init__()
        self.shape('square')
        self.color('green')
        self.penup()

class Snake:
    def __init__ (self):
        self.parts = []
        self.call()
        self.head = self.parts[0]
                
    def call(self):
        for x in POSITIONS:
            self.create_snake(x)
    
    def create_snake(self, position):
        snake = Turtle()
        snake.color('green')
        snake.shape('square')
        snake.penup()
        snake.goto(position)
        self.parts.append(snake)
        
    def move(self):
        for i in range(len(self.parts) -1, 0, -1):
            new_x = self.parts[i-1].xcor()
            new_y = self.parts[i-1].ycor()
            self.parts[i].goto(new_x, new_y)
        self.head.forward(20)
        
    def up(self):
        self.head.setheading(90)
        
    def down(self):
        self.head.setheading(270)
        
    def left(self):
        self.head.setheading(180)
        
    def right(self):
        self.head.setheading(0)
        
    def grow(self):
        s = Segment()
        self.parts.append(s)
        
    def check_collision(self):
        if len(self.parts) < 3 :
            return False
        for i in range (2, len(self.parts)):
            if self.head.distance(self.parts[i]) < 20:
                return True
        return False 
                              
class Food(Turtle):
    def __init__(self):
        super(). __init__()
        self.shape('circle')
        self.color('red')
        self.penup()
    
    def refresh(self):
        new_x = random.randint(-280, 280)
        new_y = random.randint(-280, 280)
        self.goto(new_x, new_y)
        
        
class Score(Turtle):
    def __init__(self):
        super().__init__()        
        self.color('black')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(-60, 270)
        self.update()
            
    def update(self):
        self.clear()
        self.write(f"Score:{self.score}", font = ('Arial', 28, 'bold'))
        
    def game_over(self):
        self.clear()
        self.write(f"Game Over", font = ('Arial', 28, 'bold'))

class Chrono(Turtle): #hérite de turtle 
    def __init__(self, max_value): # 2 variables 
        super().__init__()   
        self.value = max_value
        self.speed(0)
        self.penup()
        self.goto(-250, 260)
        ontimer(self.tick)# faire marcher la fonction tick toute de suite dans le jeu 
        
    def tick(self):# réecire la valuer actuelle (msx value qui diminue 1 par 1) 
        self.clear()
        self.write(self.value, align='center', font = ('arial', 28, 'normal'))
        self.value -= 1
        if self.value >= 0: #tant que la valeur est supérieur à 0, tick est toujours actif 
            ontimer(self.tick, 1000) #exécuter la fonction tic après 1 sec 
    def isFinished(self):
        return self.value < 0
               
#vérifie le contexte dans laquel tu exécute le code -> lancement de l'application (risque: code au dessus se répète plusieurs fois, donc refaire ontimer, etc.)
screen = Screen()
screen.setup(height = 600, width = 600)
screen.bgcolor('white')
screen.tracer(0)

snake = Snake()
score = Score()
food = Food()
food.refresh()

screen.listen()
screen.onkey(key='Up', fun = snake.up)
screen.onkey(key='Down', fun = snake.down)
screen.onkey(key='Left', fun = snake.left)
screen.onkey(key='Right', fun = snake.right)

game_is_on = True

counter = Chrono(60)
    
while game_is_on:
    screen.update()
    time.sleep(0.1)
        
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