"""Template for a game

This script implements general classes for your game.
Put your description of the game as a doc-string at the beginning.
A doc-string is a mult-line string enclosed with three double-quotes.

Your game must define at a minimum these 5 classes :

- Rectangle
- Text
- Button (composed of class Rectangle and Button)
- Grid
- Game (composed of class Grid, Text and Button)

You can modify these classes.
You can add more classes (ex. Player, Enemy, Score, Room, Level, etc.)
The last command to be called must be Game()

"""

"""
Classes : (name / attributes / methods)
- Rectangle / pos, size, color / outline, draw, inside
- Text / pos, text, size / draw
- Button / rect, pos, size, label, displayed / draw, inside
- Grid / n, m, d, x0, y0, state / draw, inside, get_cell
- Player / name, col / X
- Game / grid, title, status, buttons, players, current_player,
        history / move, click, save, undo, draw

to add:
- Player.score
- Player.chrono
"""

from turtle import *


def ligne(p, q):
    """Draws a ligne from point p to point q."""

    goto(p)
    down()
    goto(q)
    up()


class Rectangle:
    """Draw a filled rectangle."""
    
    def __init__(self, pos, size, color='gray'):
        """Initialize the rectangle and draw it."""
        self.pos = pos
        self.size = size
        self.color = color
        self.draw()
    

    def outline(self):
        """Draw just the outline of the rectangle."""
        goto(self.pos)
        pensize(5)
        down()
        for x in self.size * 2:
            forward(x)
            left(90)
        up()


    def draw(self):
        """Draw the outline of the rectangle and fill it a color is defined."""
        if self.color:
            fillcolor(self.color)
            begin_fill()
            self.outline()
            end_fill()
        else:
            self.outline()

     
    def inside(self, p):
        """Check if the point p is inside the rectangle."""
        x, y = self.pos
        w, h = self.size
        
        return 0 < p[0]-x < w and 0 < p[1]-y < h
        

class Text:
    """Draw a text at a given position."""
    
    def __init__(self, pos, text, size=16, align='center'):
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
    def __init__(self, pos, text, size=(80, 30), color='mediumslateblue', displayed=True):
        self.rect = Rectangle(pos, size, color)
        x, y = pos
        w, h = size
        self.label = Text((x + w//2, y + h//4), text, h//2)
        self.displayed = displayed


    def draw(self):
        self.rect.draw()
        self.label.draw()
    

    def inside(self, p):
        return self.rect.inside(p)


class Grid:
    """Define a grid class with the size (n x m).

    n is the number of lignes,
    m the number of columns.
    """

    # d = 52
    def __init__(self, n=6, m=7, d=45):
        """Create a new Grid instance"""
        self.n = n        # vertical (y)
        self.m = m        # horizontal (x)
        self.d = d        # distance
        self.x0 = m * d // 2
        self.y0 = n * d // 2
        # self.state = [[0] * 7] * 6
        self.state = []
        for i in range(6):
            self.state.append([0] * 7)
        
        self.draw()
    

    def draw(self):
        """Draw the grid."""
        up()
        colors = {0:'deepskyblue', 1:'red', 2:'yellow'}
        for x in range(self.m):
            for y in range(self.n):
                goto(-self.x0 + x * self.d + self.d // 2, self.y0 - y * self.d - self.d // 2)
                dot(self.d * 25 // 32, 'black')
                col = colors[self.state[y][x]]
                dot(self.d * 3 // 5, col)

    
    def inside(self, x, y):
        """Check if (x, y) is inside the grid."""
        x0 = self.x0
        y0 = self.y0
        x0 += self.d // 2
        y0 += self.d // 2    
        return -x0 < x < x0 and -y0 < y < y0
    

    def get_cell(self, x, y, pixels=False):
        """Returns the coordinates of center or intersection.
        The result will be between 0 and 5 or 6 (for y or x) if pixels=False
        Else, the result will be in pixel (like “-104.0 -78.0“)
        """
        
        x = (x + self.d // 2) // self.d * self.d
        y = y // self.d * self.d + self.d // 2

        if pixels:
            print(x, y)
            return x, y
        
        else:
            i = int(x // self.d) + self.m // 2
            j = int(y // self.d) - self.n // 2
            return i, j

    
    def __str__(self):
        return f'Grid({self.n}, {self.m})'


class Player:
    '''This is blablabla
    '''

    def __init__(self, name, col):
        '''Add explanations
        '''
        self.name = name
        self.col = col


class Game:
    """This is a general Game class.
    It contains all the game variables and attributes.
    """
    
    def __init__(self):
        """Set up the game window and the turtle attributes.
        Initilize all the attributes.
        Setup the callback functions.
        """
        
        setup(600, 400)
        hideturtle()
        tracer(0)
        up()
   
        # self.score = 0
        self.grid = Grid()
        self.title = Text((0,  170), 'Puissance 4', 24)
        self.status = Text((-280, -190), 'status line', align='left')
        self.bt_undo = Button((200, 100), 'Undo')
        # self.bt_new = Button((200, 50), 'New')
        self.player1 = Player('Player 1', 'red')
        self.player2 = Player('Player 2', 'yellow')
        self.current_player = 1
        self.history = [[[0] * 7] * 6]
        self.board()
        self.draw()

        ''' TEST '''
        # affichage du “state“ actuel dans la console
        print('TEST\n\nbefore change :')
        for y in range(6):
            # affiche une ligne après l'autre
            # en commançant par celle du haut
            print(self.grid.state[y])
        
        # changement de l'état
        # j'essaie de changer une case au milieu du plateau
        self.grid.state[3][3] = 2

        # ré-affichage du “state“ actuel dans la console
        print('\nafter change :')
        for y in range(6):
            print(self.grid.state[y])
        print('FIN DU TEST\n\n')
        ''' FIN DU TEST - même problème dans game.click() '''

        self.save()
        self.grid.draw()
        s = getscreen()

        s.onclick(self.click)

        s.onkey(self.move(1), '1')
        # s.onkey(self.move(2), '2')
        # s.onkey(self.move(3), '3')
        # s.onkey(self.move(4), '4')
        # s.onkey(self.move(5), '5')
        # s.onkey(self.move(6), '6')
        # s.onkey(self.move(7), '7')
        
        # s.onkey(clear, 'enter')
        s.onkey(self.draw, ' ')

        s.listen()
    
    
    def board(self):
        home()
        dot(2000, 'deepskyblue')
        goto(-self.grid.x0 + self.grid.d // 2, self.grid.y0 + self.grid.d // 2)
        color('black')
        fillcolor('navy')
        pensize(8)
        down()
        begin_fill()
        for i in range(2):
            forward(2 * self.grid.x0 - self.grid.d)
            circle(-self.grid.d, 90)
            forward(2 * self.grid.y0 - self.grid.d)
            circle(-self.grid.d, 90)
        end_fill()
        up()

    
    def move(self, column):
        # print('choose the column', column)
        pass


    def click(self, x, y):
        """Reacts to mouse clicks."""
        if self.grid.inside(x, y):
            i = self.grid.get_cell(x, y)[0]
            for j in range(5, 0, -1):
                if self.grid.state[j][i] == 0:
                    # print(f'i = {i}; j = {j} =>', self.grid.state[j][i])

                    # print('grid state before click :\n\t\t', (self.grid.state[k] for k in range(6)))
                    self.grid.state[j][i] = self.current_player
                    # print('grid state after click :\n\t\t', (self.grid.state[k] for k in range(6)))

                    self.save()
                    self.current_player = self.current_player % 2 + 1
                    break
            
            self.draw()
        
        p = x, y
        if self.bt_undo.inside(p) and len(self.history) > 1:
            self.undo()
            self.current_player = self.current_player % 2 + 1
        # if self.bt_clear.inside(p):
        #     clear()
        #     self.bt_new.draw()
        #     self.bt_clear.draw()
        
        # if self.bt_new.inside(p):
        #     self.draw()
        for i in range(len(self.history)):
            print(f'step {i + 1} :')
            for j in range(6):
                print('\t\t', self.history[i][j])
        print('\n')


    def save(self):
        current_state = []

        for line in range(6):
            current_cells = []
            for cell in range(7):
                current_cells.append(int(self.grid.state[line][cell]))
            
            current_state.append(list(current_cells))
        self.history.append(list(current_state))

        for i in range(len(self.history)):
            print(f'step {i + 1} :')
            for j in range(6):
                print('\t\t', self.history[i][j])


    def undo(self):
        print('Undo !')
        if len(self.history) == 2:
            # self.grid.state = [[0] * 7] * 6
            self.grid.state = []
            for i in range(6):
                self.grid.state.append([0] * 7)

            self.history.clear()
            self.history = [[[0] * 7] * 6]
        else:
            self.grid.state = list(self.history[-2])
            self.history.pop()
        self.draw()
    

    def draw(self):
        """Draws all the game objects."""
        self.grid.draw()
        self.title.draw()
        self.status.draw()
        for button in [self.bt_undo]:
            if button.displayed:
                button.draw()
        down()


game = Game()

done()