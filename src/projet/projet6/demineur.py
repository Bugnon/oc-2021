# Malik et Enrico
# Projet Demineur

from logging import root
from random import *
from turtle import *
from time import *
from tkinter import *

highscores = {'1.': ' Pas encore de temps', '2.': ' Pas encore de temps', '3.': ' Pas encore de temps', '4.': ' Pas encore de temps', '5.': ' Pas encore de temps', '6.': ' Pas encore de temps', '7.': ' Pas encore de temps', '8.': ' Pas encore de temps', '9.': ' Pas encore de temps', '9.': ' Pas encore de temps', '10.': ' Pas encore de temps'}

state = [[0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0]]
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
         

def ligne(p, q):
    goto(p)
    down()
    goto(q)
    up()

class Game:
     def __init__(self, pos):

        setup(600,400)
        hideturtle()
        tracer(0)
        n = 0
        up()

        self.pos = pos
        
        self.highscore = []
        self.title = Text((0,165), 'Welcome to the best game ever: The Demineur', 20, 'center')
        self.bt_highscore = Button((200, 100), 'Highscores')
        self.bt_new = Button((200, 50), 'New')
        self.bt_difficulty = Button((200, 0), 'Diffuculty')

        self.title = Text((0,650), 'Welcome to the best game ever: The Demineur', 20, align='center')
        self.grid = Grid()
        s = getscreen()
        s.listen()
        done()

     def click(self, x, y):
         if self.grid.inside(x, y):
            goto(x, y)
            dot()
            write(x, y)

     def f(self,x,y):
         if bt_new.inside((x,y)):
             clear()
             self.generate()

         if bt.highscores.inside((x,y)):
             clear()
             self.Highscores = Highscores()
        
         if bt_difficulty.inside((x,y)):
            clear()
            self.difficulty = difficulty()

     def inside(self, p):
        x, y = self.pos
        w, h = self.size
        return 0 < p[0]-x < w and 0 < p[1]-y < h

     def generate(self):
         if n < 10:
            state[randint(0, 8)][randint(0, 8)] = 6
            n += 1
            print(state)
         if n == 10:
             self.play = Play()

            
 class Play:
     def __init__(self, pos):
         self.pos = pos

      def inside(self. pos):
          x,y = self.pos
          if pos = 

        
    
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
