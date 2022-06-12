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

from textwrap import fill
from turtle import *


class Rectangle:
    """Draw a filled rectangle."""
    
    def __init__(self, pos, size, color='gray', outline=True):
        """Initialize the rectangle and draw it."""
        self.pos = pos
        self.size = size
        self.color = color
        self.outline = outline
        self.draw()
    

    def trace(self):
        for x in self.size * 2:
            forward(x)
            left(90)
        

    def draw(self):
        """Draw the outline of the rectangle and fill it a color is defined."""
        goto(self.pos)
        
        if self.color:
            fillcolor(self.color)
            begin_fill()
            self.trace()
            end_fill()
        
        if self.outline:
            pensize(5)
            down()
            self.trace()
            up()

     
    def inside(self, p):
        """Check if the point p is inside the rectangle."""
        x, y = self.pos
        w, h = self.size
        
        return 0 < p[0]-x < w and 0 < p[1]-y < h
        

class Text:
    """Draw a text at a given position."""
    
    def __init__(self, pos, text, size=16, align='center'):
        """Initilizes the text."""
        self.pos = pos
        self.text = text
        self.size = size
        self.align = align
        self.draw()


    def draw(self):
        """Draw the text."""
        goto(self.pos)
        write(self.text, font=('Times', self.size), align=self.align)


class Button:
    """Create a button that the player can interact with."""
    
    def __init__(self, pos, text, size=(80, 30), color='mediumslateblue', displayed=True):
        """Create a new Button instance."""
        self.rect = Rectangle(pos, size, color)
        x, y = pos
        w, h = size
        self.label = Text((x + w//2, y + h//4), text, h//2)
        self.displayed = displayed
    

    def inside(self, p):
        """Check if p = (x, y) is inside the button."""
        return self.rect.inside(p)
    

    def draw(self):
        """Draw the button."""
        self.rect.draw()
        self.label.draw()


class Grid:
    """Define a grid class with the size (n x m).

    n is the number of lignes,
    m the number of columns.
    """

    def __init__(self, n=6, m=7, d=45):
        """Create a new Grid instance."""
        self.n = n        # vertical (y)
        self.m = m        # horizontal (x)
        self.d = d        # distance
        self.x0 = m * d // 2
        self.y0 = n * d // 2

        self.state = []
        for i in range(6):
            self.state.append([0] * 7)
        
        self.draw()

    
    def inside(self, x, y):
        """Check if (x, y) is inside the grid."""
        x0 = self.x0
        y0 = self.y0
        x0 += self.d // 2
        y0 += self.d // 2    
        return -x0 < x < x0 and -y0 < y < y0
    

    def get_cell(self, x, y, pixels=False):
        """Returns the coordinates of center.
        The result will be between 0 and 5 or 6 (for y or x) if pixels=False.
        Otherwise, the result will be in pixel (like “-104.0 -78.0“).
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


class Player:
    """Create a player"""

    def __init__(self, name, col):
        self.name = name
        self.col = col
        self.score = 0


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

        self.grid = Grid()
        self.title = Text((0,  170), 'Puissance 4', 24)
        self.author = Text((285, -190), 'by Emilien Barde', align='right')
        self.bt_undo = Button((200, 100), 'Undo')
        self.bt_new = Button((200, 50), 'New')
        self.player1 = Player('Player 1', 'red')
        self.player2 = Player('Player 2', 'yellow')
        self.status = Text((-285, -190), f'{self.player1.name} ({self.player1.col}) to move', align='left')
        self.status_eraser = Rectangle(self.status.pos, (300, 20), color='deepskyblue', outline=False)
        self.players = (self.player1, self.player2)
        self.current_player = 1
        self.history = []

        self.reset()
        self.board()
        self.draw()

        s = getscreen()

        # when the player uses the keyboard
        s.onclick(self.click)

        # when the player uses the keyboard
        s.onkey(self.key(1), '1')
        

        s.listen()
    
    
    def board(self):
        """Draw the background and the darkblue board."""
        home()
        
        # background
        dot(2000, 'deepskyblue')

        # board, initialization of the turtle
        goto(-self.grid.x0 + self.grid.d // 2, self.grid.y0 + self.grid.d // 2)
        color('black')
        fillcolor('navy')
        pensize(8)
        down()
        begin_fill()

        # Board's drawing
        for i in range(2):
            forward(2 * self.grid.x0 - self.grid.d)
            circle(-self.grid.d, 90)
            forward(2 * self.grid.y0 - self.grid.d)
            circle(-self.grid.d, 90)
        end_fill()
        up()

    
    def key(self, column):
        """Reacts to keyboard."""
        # print('choose the column', column)
        pass


    def click(self, x, y):
        """Reacts to mouse clicks."""

        # the player clicks on the grid
        if self.grid.inside(x, y):
            i = self.grid.get_cell(x, y)[0]
            self.play(i)
            self.draw()
        
        # buttons
        p = x, y

        # the player clicks on the “undo“ button
        if self.bt_undo.inside(p) and len(self.history) > 1:
            self.undo()
            self.draw()

        # if self.bt_clear.inside(p):
        #     clear()
        #     self.bt_new.draw()
        #     self.bt_clear.draw()
        
        # the player clicks on the “new“ button
        if self.bt_new.inside(p):
            self.reset()
            self.draw()
        
        # print the grid's state (debugging)
        for i in range(len(self.history)):
            print(f'step {i + 1} :')
            for j in range(6):
                print('\t\t', self.history[i][j])
        print('\n')


    def reset(self):
        """Reset the game.
        It resets the grid, the history and the current player."""

        # grid initialization
        self.grid.state = []
        for i in range(6):
            self.grid.state.append([0] * 7)
        
        # history initialization
        self.history = []
        history_temp = []
        for i in range(6):
            history_temp.append([0] * 7)
        self.history.append(history_temp)

        # reset the current player
        self.current_player = 1
        self.status.text = f'{self.player1.name} ({self.player1.col}) to move'

        # board and game drawing
        self.board()


    def switch_players(self):
        """Switch the current player and the game's status."""
        self.current_player = self.current_player % 2 + 1
        player = self.players[self.current_player - 1]  # to simplify the next line
        self.status.text = f'{player.name} ({player.col}) to move'


    def play(self, column):
        """Change the state of one grid's column."""
        # from the bottom to the top of the column
        for j in range(5, -1, -1):
            # if the cell is free, we change his value
            if self.grid.state[j][column] == 0:
                self.grid.state[j][column] = self.current_player
                self.save()
                self.switch_players()
                break


    def undo(self):
        """Cancel the last move."""
        print('Undo !')
        
        # when there is only one move played
        if len(self.history) == 2:
            self.reset()            

        else:
            last_state = []

            for line in range(6):
                last_cells = []
                for cell in range(7):
                    # the cells of one column are added to the temporary cells's list
                    last_cells.append(int(self.grid.state[line][cell]))
                
                # the line is added to the temporary state's list
                last_state.append(list(last_cells))
            
            self.grid.state = last_state
            self.history.pop()
        
        self.switch_players()
    

    def save(self):
        """Save the state of the game in the history."""
        current_state = []

        for line in range(6):
            current_cells = []
            for cell in range(7):
                # the cells of one column are added to the temporary cells's list
                current_cells.append(int(self.grid.state[line][cell]))
            
            # the line is added to the temporary state's list
            current_state.append(list(current_cells))
        self.history.append(list(current_state))

        # print for debugging
        for i in range(len(self.history)):
            print(f'step {i + 1} :')
            for j in range(6):
                print('\t\t', self.history[i][j])
    
    
    def draw(self):
        """Draws all the game objects."""
        self.grid.draw()
        self.title.draw()
        self.author.draw()

        self.status_eraser.draw()
        self.status.draw()

        for button in [self.bt_undo, self.bt_new]:
            if button.displayed:
                button.draw()


game = Game()

done()
