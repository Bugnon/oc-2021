from turtle import Turtle, Screen
import time
import random 

POSITIONS = [(0, 0)]



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
        for y in range(len(self.parts) -1, 0, -1):
            new_x = self.parts[x-1].xcor()
            new_y = self.parts[x-1].ycor()
            self.parts[x].goto(new_x, new_y)
        self.head.forward(20)
        
    def up(self):
        self.head.setheading(90)
        
    def down(self):
        self.head.setheading(270)
        
    def left(self):
        self.head.setheading(180)
        
    def right(self):
        self.head.setheading(0)
            

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

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    if snake.head.distance(food) < 20:
        food.refresh()
        score.score += 10
        score.update()
        
    elif snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        score.game_over()
        game_is_on = False
        
        
    

screen.exitonclick() 