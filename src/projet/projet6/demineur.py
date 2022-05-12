# Malik et Enrico
# Projet Demineur

from logging import root
from random import *
from turtle import *
from time import *
from tkinter import *

highscores = {'1.': ' Pas encore de temps', '2.': ' Pas encore de temps', '3.': ' Pas encore de temps', '4.': ' Pas encore de temps', '5.': ' Pas encore de temps', '6.': ' Pas encore de temps', '7.': ' Pas encore de temps', '8.': ' Pas encore de temps', '9.': ' Pas encore de temps', '9.': ' Pas encore de temps', '10.': ' Pas encore de temps'}

class Rectangle: 
    def __init__(self, pos, size, color='green'):
        self.pos = pos
        self.size = size
        self.color = color
        self.draw()
    def outline(self):
        goto(self.pos)
        down()
        for x in self.size * 2:
            forward(x)
            left(90)
        up()
    def draw(self):
        if self.color:
            fillcolor(self.color)
            begin_fill()
            self.outline()
            end_fill()
        else:
            self.outline()
    def inside(self, p):
        x, y = self.pos
        w, h = self.size

        return 0 < p[0]-x < w and 0 < p[1]-y < h

class Text:
    """Draw a text at a given position."""
    
    def __init__(self, pos, text, size=16, align='left'):
        """Initilizes the text"""
        self.pos = pos
        self.text = text
        self.size = size
        self.align = align
        self.draw()
        
    def draw(self):
        """Draw the text."""
        goto(self.pos)
        write(self.text, font=('Arial', self.size), align=self.align)

class Button:
    def __init__(self, pos, text, size=(80, 30), color='lightgray'):
        self.rect = Rectangle(pos, size, color)
        x, y = pos
        w, h = size
        self.label = Text((x + w//2, y + h//4), text, h//2, 'center')

        
    def draw(self):
        self.rect.draw()
        self.label.draw()
    
    def inside(self, p):
        return self.rect.inside(p)

    def __str__(self):
        return f'bouton({self.pos}, {self.text})'

    def inside(self, p):
        return self.rect.inside(p)
         
    
def UI():
    goto(0,115)
    write('Welcome to the best game ever', font=('Arial',60//2), align='center')
    goto(0,80)
    write('The Demineur', font=('Arial', 60//2), align='center')
    bouton_start = bouton((-70, 30), 'Select Difficulty', (150,40), 'lightblue')
    bouton_highscore = bouton((-70, -20), 'Highscores', (150,40), 'lightblue')
    bouton_settings = bouton((-70, -70), 'Settings', (150,40), 'lightblue')
    def f(x,y):
        if bouton_start.inside((x,y)):
            clear()
            diff()
        if bouton_highscore.inside((x,y)):
            clear()
            highscore()
        if bouton_settings.inside((x,y)):
            clear()
            settings()
    s.onclick(f)

def settings():
    ...

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
    global b
    b = o 
    if b == 1:
        clear()
        partieencour = True
        grille(1)
    if b == 2:
        clear()
        partieencour = True
        grille(2)
    if b == 3:
        clear()
        partieencour = True
        grille(3)

def grille(p):
    if p == 1:
        x  = 240, 180, 120, 60, 0, -60, -120, -180, -240
        z = 8
        u = 240
    if p == 2:
        setup(700,700)
        x = 290, 230, 170, 110, 50, -10, -70, -130, -190, -250
        z = 10
        u = 310
    if p == 3:
        setup(800,800)
        x = 360, 300, 240, 180, 120, 60, 0, -60, -120, -180, -240, -300
        z = 13
        u = 390
    color('green')
    for y in x:
        goto(-u,y)
        for i in range(z):
            begin_fill()
            for i in range(4):
                fd(50)
                rt(90)
            end_fill()
            fd(60)            

def ligne(p, q):
    goto(p)
    down()
    goto(q)
    up()

class Game:
     def __init__(self):


        setup(600,400)
        hideturtle()
        tracer(0)
        up()
        
        self.highscore = []
        self.title = Text((0,650), 'Welcome to the best game ever: The Demineur', 20, 'center')
        self.bt_clear = Button((200, 100), 'Clear')
        self.bt_new = Button((200, 50), 'New')
        self.bt_difficulty = Button((200, 0), 'Diffuculty')

        self.title = Text((0,650), 'Welcome to the best game ever: The Demineur', 20, align='center')
        self.grid = Grid()
        s = getscreen()
        s.listen()
        done()

    
    
class Grid:
     def __init__(self, n=8, m=8, d=40, ongrid=True):
        """Create a new Grid instance"""
        self.n = n        # vertical (y)
        self.m = m        # horizontal (x)
        self.d = d        # distance
        self.ongrid = ongrid
        self.x0 = m * d // 2
        self.y0 = n * d // 2
        
        self.draw()
        print(self)

     
     def draw(self):
        """Draw the grid."""
        for x in range(-self.x0, self.x0+1, self.d):
            ligne((x, -self.y0), (x, self.y0))

        for y in range(-self.y0, self.y0+1, self.d):
            ligne((-self.x0, y), (self.x0, y))

     def inside(self, x, y):
        """Check if (x, y) is inside the grid."""
        x0 = self.x0
        y0 = self.y0
        if self.ongrid:
            x0 += self.d // 2
            y0 += self.d // 2    
        return -x0 < x < x0 and -y0 < y < y0
            
     def get_cell(self, x, y):
        """Returns the coordinates of center or intersection."""
        
        x += self.x0
        y += self.y0
        if self.ongrid:
            x += self.d // 2
            y += self.d // 2
            
        i = int(y // self.d)
        j = int(x // self.d)
        
        print(i, j)
               
     def __str__(self):
        return f'Grid({self.n}, {self.m})'

'6 = bombe '

'7 = drapeau'

game = Game()
