# importer des modules requises pour la création du jeu 
from turtle import *
import turtle as tur
import time
import random
 
delay = 0.1
score = 0
high_score = 0
 
  
# Creating a window screen
ws = tur.Screen()
ws.title("Pythontpoint")
ws.bgcolor("cyan")
ws.setup(width=700, height=600)
ws.tracer(0)
 
# head of the snake
hd = tur.Turtle()
hd.shape("circle")
hd.color("black")
hd.penup()
hd.goto(0, 0)
hd.direction = "Stop"
 
# food in the game
foodsh = tur.Turtle()
colrs = random.choice(['red', 'orange', 'yellow'])
shpes = random.choice(['square', 'triangle', 'circle'])
foodsh.speed(0)
foodsh.shape(shpes)
foodsh.color(colrs)
foodsh.penup()
foodsh.goto(0, 100)
 
pen = tur.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0  High Score : 0", align="center",
          font=("Times New Roman", 24, "bold"))
 
 
 
# assigning key directions
def gp():
    if hd.direction != "down":
        hd.direction = "up"
 
 
def movedown():
    if hd.direction != "up":
        hd.direction = "down"
 
 
def moveleft():
    if hd.direction != "right":
        hd.direction = "left"
 
 
def moveright():
    if hd.direction != "left":
        hd.direction = "right"
 
 
def move():
    if hd.direction == "up":
        y = hd.ycor()
        hd.sety(y+20)
    if hd.direction == "down":
        y = hd.ycor()
        hd.sety(y-20)
    if hd.direction == "left":
        x = hd.xcor()
        hd.setx(x-20)
    if hd.direction == "right":
        x = hd.xcor()
        hd.setx(x+20)
 
 
         
ws.listen()
ws.onkeypress(gp, "w")
ws.onkeypress(movedown, "s")
ws.onkeypress(moveleft, "a")
ws.onkeypress(moveright, "d")
 
segments = []
 
 
 
# Main Gameplay
while True:
    ws.update()
    if hd.xcor() > 290 or hd.xcor() < -290 or hd.ycor() > 290 or hd.ycor() < -290:
        time.sleep(1)
        hd.goto(0, 0)
        hd.direction = "Stop"
        colors = random.choice(['red', 'blue', 'green'])
        shapes = random.choice(['square', 'circle'])
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
    if hd.distance(foodsh) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        foodsh.goto(x, y)
 
        # Adding segment
        newsegmnt = tur.Turtle()
        newsegmnt.speed(0)
        newsegmnt.shape("circle")
        newsegmnt.color("orange")  # tail colour
        newsegmnt.penup()
        segments.append(newsegmnt)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
    # Checking for hd collisions with body segments
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = hd.xcor()
        y = hd.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(hd) < 20:
            time.sleep(1)
            hd.goto(0, 0)
            hd.direction = "stop"
            colors = random.choice(['red', 'orange', 'yellow'])
            shapes = random.choice(['square', 'circle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segment.clear()
 
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("candara", 24, "bold"))
    time.sleep(delay)
 
ws.mainloop()