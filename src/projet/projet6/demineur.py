# Malik et Enrico
# Projet Demineur

from random import *
from tkinter import *
from turtle import *
from time import *

s = getscreen()
setup(500,500)
hideturtle()
up()
speed(0)
highscores = {'1.': ' Pas encore de temps', '2.': ' Pas encore de temps', '3.': ' Pas encore de temps', '4.': ' Pas encore de temps', '5.': ' Pas encore de temps', '6.': ' Pas encore de temps', '7.': ' Pas encore de temps', '8.': ' Pas encore de temps', '9.': ' Pas encore de temps', '9.': ' Pas encore de temps', '10.': ' Pas encore de temps'}
partiecontinue = True

class bouton:
    def __init__(self, pos, text, size=(80, 30), color='lightgray'):
        self.pos = pos
        self.size = size
        self.text = text
        self.color = color
        self.draw()
        
    def draw(self):
        goto(self.pos)
        fillcolor(self.color)
        begin_fill()
        down()
        for x in self.size * 2:     # parcourir 2 fois longeur et hauteur
            forward(x)
            left(90)
        up()
        end_fill()
        x, y = self.pos
        w, h = self.size
        goto(x+w/2, y+h/4)
        color('black')
        write(self.text, font=('Arial', h//2), align='center')

    def __str__(self):
        return f'bouton({self.pos}, {self.text})'

    def inside(self, p):
        x, y = self.pos
        w, h = self.size
        
        return 0 < p[0]-x < w and 0 < p[1]-y < h    
def UI():
    goto(0,115)
    write('Welcome to the best game ever', font=('Arial',60//2), align='center')
    goto(0,80)
    write('The Demineur', font=('Arial', 60//2), align='center')
    bouton_start = bouton((-70, 30), 'Select Difficulty', (150,40), 'lightblue')
    bouton_highscore = bouton((-70, -20), 'Highscores', (150,40), 'lightblue')
    def f(x,y):
        if bouton_start.inside((x,y)):
            clear()
            diff()
        if bouton_highscore.inside((x,y)):
            clear()
            highscore()
    s.onclick(f)



def diff():
    goto(10,100)
    write('Choose the difficulty', font=('Arial',40//2), align='center')
    bouton_hard = bouton((-70,-50), 'Hard', (150,40), 'lightblue')
    bouton_medium = bouton((-70,0), 'Medium', (150,40), 'lightblue')
    bouton_easy = bouton((-70,50), 'Easy', (150,40), 'lightblue')
    def c(x,y):
        if bouton_easy.inside((x,y)):
            clear()
            initialisation(1)
        if bouton_medium.inside((x,y)):
            clear()
            initialisation(2)
        if bouton_hard.inside((x,y)):
            clear()
            initialisation(3)
    s.onclick(c)

def highscore():
    goto(0,160)
    write('High scores', font=('Arial', 50//2), align='center')
    goto(-120,125)
    write('1 : ' + highscores['1.'], font=('Arial', 40//2), align='center')
    goto(-120,100)
    write('2 : ' + highscores['2.'], font=('Arial', 40//2), align='center')
    goto(-120,75)
    write('3 : ' + highscores['3.'], font=('Arial', 40//2), align='center')
    goto(-120,50)
    write('4 : ' + highscores['4.'], font=('Arial', 40//2), align='center')
    goto(-120,25)
    write('5 : ' + highscores['5.'], font=('Arial', 40//2), align='center')
    goto(-120,0)
    write('6 : ' + highscores['6.'], font=('Arial', 40//2), align='center')
    goto(-120,-25)
    write('7 : ' + highscores['7.'], font=('Arial', 40//2), align='center')
    goto(-120,-50)
    write('8 : ' + highscores['8.'], font=('Arial', 40//2), align='center')
    goto(-120,-75)
    write('9 : ' + highscores['9.'], font=('Arial', 40//2), align='center')
    goto(-120,-100)
    write('10 : ' + highscores['10.'], font=('Arial', 40//2), align='center')
    bouton_UI = bouton((-130,-160), "Revenir a l'écran principal", (250,40))
    def f(x,y):
        if bouton_UI.inside((x,y)):
            clear()
            UI()
    s.onclick(f)
    
def initialisation(o):
    if o == 1:
        goto(155,200)
        grille(10,10,20,400)
    if o == 2:
        setup(600,600)
        goto(0,0)
        grille(20,20,20,400)
    if o == 3:
        setup(600,700)
        goto(290,300)
        grille(30,30,20,600)
#     if o == 4:
        
            
# def joueraujeu():
    
# def regledujeu():
    
def grille(g,l,z,p):
    for i in range(g):
        x0 = xcor()
        y0 = ycor()
        up()
        setx(x0-p)
        sety(y0-20)
        down()
        for i in range(l):
            up()
            fd(20)
            down()
            for i in range(4):
                fd(z)
                rt(90)
            
UI()
s.listen()
done()