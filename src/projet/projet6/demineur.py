# Malik et Enrico
# Projet Demineur

from curses.textpad import rectangle
from logging import root
from random import *
from turtle import *
from time import *
from tkinter import *
import pygame 
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

         global state

         state = [[0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0]]
         self.print_state()
         
         self.highscore = []
         self.title = Text((0,165), 'Welcome to the best game ever: The Demineur', 20, 'center')
         self.bt_highscore = Button((200, 100), 'Highscores')
         self.bt_new = Button((200, 50), 'New')
         self.bt_difficulty = Button((200, 0), 'Diffuculty')

         self.title = Text((0,650), 'Welcome to the best game ever: The Demineur', 20, align='center')
         self.grid = Grid()
         self.generate()
         s = getscreen()
         s.onclick(self.click)
         s.listen()
         done()

    def generate(self):
         for i in range(9):
            state[randint(0, 7)][randint(0, 7)] = 6
         self.print_state()
         self.check()
         self.print_state()

    def check(self):
         for i in range(8):
             for n in range(8):
                 if state[i][n] >= 6:
                     if i == 0:
                         if n == 0:
                             state[0][1] += 1
                             state[1][1] += 1
                             state[1][0] += 1
                         if n == 7:
                             state[0][6] += 1
                             state[1][7] += 1
                             state[1][6] += 1
                         if n == 1 or n == 2 or n == 3 or n == 4 or n == 5 or n == 6:
                             state[0][n-1] += 1
                             state[0][n+1] += 1
                             state[1][n+1] += 1
                             state[1][n-1] += 1
                             state[1][n] += 1
                     if i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 5 or i == 6:
                         if n == 0:
                             state[i][1] += 1
                             state[i+1][1] += 1
                             state[i+1][0] += 1
                             state[i-1][1] += 1
                             state[i-1][0] += 1
                         if n == 7:
                             state[i-1][7] += 1
                             state[i-1][6] += 1
                             state[i][6] += 1
                             state[i+1][6] += 1
                             state[i+1][7] += 1
                         if n == 1 or n == 2 or n == 3 or n == 4 or n == 5 or n == 6:
                             state[i][n-1] += 1
                             state[i+1][n-1] += 1
                             state[i+1][n] += 1
                             state[i-1][n+1] += 1
                             state[i-1][n] += 1
                             state[i][n+1] += 1
                             state[i-1][n-1] += 1
                             state[i+1][n+1] += 1
                     if i == 7:
                         if n == 0:
                             state[7][1] += 1
                             state[6][0] += 1
                             state[6][1] += 1
                         if n == 7:
                             state[7][6] += 1
                             state[6][7] += 1
                             state[6][6] += 1
                         if n == 1 or n == 2 or n == 3 or n == 4 or n == 5 or n == 6:
                             state[7][n-1] += 1
                             state[7][n+1] += 1
                             state[6][n+1] += 1
                             state[6][n-1] += 1
                             state[6][n] += 1

    def click(self, x, y):
         if self.grid.inside(x, y):
             global i 
             global j
             j = int((x + 160) // 40)
             i = int((159 - y) // 40)

             if 0 <= i <=7 and 0 <= j <=7:
                 self.load(i,j)
             """"" i ligne
                   j colonne"""
            
         p = x,y 

         if self.bt_new.inside(p):
             clear()
             game = Game()

         if self.bt_highscore.inside(p):
             clear()
             self.Highscores = Highscores()
        
         if self.bt_difficulty.inside(p):
            clear()
            self.difficulty = Difficulty()

    def load(self, ligne, colonne):
         x = -180 + ((colonne + 1) * 40)
         y = (130 - (ligne * 20) * 2)

         if state[ligne][colonne] < 10:
             if state[ligne][colonne] >= 6:
                 """ inserer l'image d'une bombe """
                 pygame.blit('mine123.gif', (0,0))
                 pygame.display.flip()
             if state[ligne][colonne] < 6:
                 """ montrer le chiffre """
                 self.num = Text((x,y),state[ligne][colonne])
                 if state[ligne][colonne] == 0:
                     self.holes(ligne, colonne)

    def draw_cell_text(self, ligne, colonne, texte):
        x = -180 + ((colonne + 2) * 40)
        y = (130 - (ligne * 20) * 2)
        Text((x, y),'0')

    def print_state(self):
        for ligne in state:
            print(ligne)
        print()

    def holes(self, l, c):
         """Affiche tous les 0 (cellules vides), quand le joueur clique dans la cellule state[l][c]."""
         for i in range(3):
             for n in range(3):
                 ligne = l + n
                 colonne = c + i
                 if colonne != 7:
                    if state[ligne][colonne + 1] == 0:
                        # x = -180 + ((colonne + 2) * 40)
                        # y = (130 - (ligne * 20) * 2)
                        # self.num = Text((x,y),'0')
                        self.draw_cell_text(ligne, colonne, '0')

                 if colonne != 0:
                    if state[ligne][colonne - 1] == 0:
                        x = -180 + ((colonne) * 40)
                        y = (130 - (ligne * 20) * 2)
                        self.num = Text((x,y),'0')


                 if ligne != 7 and colonne != 7:
                    if state[ligne + 1][colonne + 1] == 0:
                        x = -180 + ((colonne + 2) * 40)
                        y = (130 - (ligne * 20) * 2) - 40
                        self.num = Text((x,y),'0')

                 if ligne != 0 and colonne != 0: 
                    if state[ligne + 1][colonne - 1] == 0:
                        x = -180 + ((colonne) * 40)
                        y = (130 - (ligne * 20) * 2) - 40
                        self.num = Text((x,y),'0')

                 if ligne != 0 and colonne != 7:
                    if state[ligne - 1][colonne + 1] == 0:
                        x = -180 + ((colonne + 2) * 40)
                        y = (130 - (ligne * 20) * 2) + 40
                        self.num = Text((x,y),'0')
                    
                 if ligne != 0 and colonne != 0:
                    if state[ligne - 1][colonne - 1] == 0:
                        x = -180 + ((colonne) * 40) 
                        y = (130 - (ligne * 20) * 2) + 40
                        self.num = Text((x,y),'0')
                        
                 if ligne != 7:
                    if state[ligne + 1][colonne] == 0:
                        x = -180 + ((colonne + 1) * 40)
                        y = (130 - (ligne * 20) * 2) - 40
                        self.num = Text((x,y),'0')
                    
                 if ligne != 0:
                    if state[ligne - 1][colonne] == 0:
                        x = -180 + ((colonne + 1) * 40)
                        y = (130 - (ligne * 20) * 2) + 40
                        self.num = Text((x,y),'0')
                
    def loose(self):
         clear()

    def win(self):
         ...

class Highscores:
    def __init__(self):
         ...

class Difficulty:
    def __init__(self):
         ...
        
    
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

game = Game()
