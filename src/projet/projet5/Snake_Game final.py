# importer des modules requis pour la création du jeu 
import turtle
import time
import random 

# définir le retard, le score et le meilleur score du point initial
delay = 0.1
score = 0
high_score = 0

# construire l'affichage du jeu 
# l'écran (screen) 
screen = turtle.Screen()
# titre du jeu 
screen.title('Snake Game') 
# couleur de fond du jeu 
screen.bgcolor('black')

#la taille de l'écran en largeur (width) et en hauteur (height)
screen.setup(width = 600, height = 600)
screen.tracer(0)

# création de la tête du snake (head) avec la forme, la couleur, la position et la vitesse 
head = turtle.Turtle()
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

# score et high score 
pen = turtle.Turtle()
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
# Ecrire Score et High Score et définir la police d'écriture, la taille et en gras
pen.write("Score : 0   High Score : 0", align ="center", font = ("Arial", 28, "bold"))

# directions pour le snake (en haut, en bas, à droite et à gauche)
def go_up():
    head.direction = 'up'
    
def go_down():
    head.direction = 'down'
    
def go_left():
    head.direction = 'left'
    
def go_right():
    head.direction = 'right'

# bouger le serpent par rapport à sa position 
def move():
    if head.direction == 'up':
       y = head.ycor()
       head.sety(y + 20)
    
    if head.direction == 'down':
       y = head.ycor()
       head.sety(y - 20)
       
    if head.direction == 'left':
       x = head.xcor()
       head.setx(x - 20)
       
    if head.direction == 'right':
       x = head.xcor()
       head.setx(x + 20)

<<<<<<< HEAD
print(head.direction, head.pos())

screen.update()
screen.ontimer(move, 100)
=======
    # Holzer : for debugging only
    print(head.direction, head.pos())   

    # Holzer : setup a callback function some time in the future
    screen.update()
    screen.ontimer(move, 500)
>>>>>>> 9800e09df5fd3d5eb949de285e834582345684c9

# onkeypress 
screen.listen()
screen.onkeypress(go_up, 'Up')
screen.onkeypress(go_down, 'Down')
screen.onkeypress(go_left, 'Left')
screen.onkeypress(go_right, 'Right')

<<<<<<< HEAD

=======
# Holzer : call the function move once, afterwards it is called via ontimer()
move()
turtle.done()   

# Holzer : Use a timer callback function to call move()
# while True:
#     screen.update()
    
# fonctions     
# move()
# go_up()
# go_down()
# go_right()
# go_left()
>>>>>>> 9800e09df5fd3d5eb949de285e834582345684c9
       

