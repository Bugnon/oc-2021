from random import choice
from turtle import *
from freegames import vector
import time
import os
import sys
import subprocess


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
    """Create a clickable rectangle"""
    def __init__(self, pos, text, size, color='lightgray', align='center'):
        self.rect = Rectangle(pos, size, color)
        x, y = pos
        w, h = size
        self.label = Text((x + w//2, y + h//4), text, h//2, 'center')

    def draw(self):
        """draw the button"""
        self.rect.draw()
        self.label.draw()

    def inside(self, p):
        """Check if the point p is inside the button"""
        return self.rect.inside(p)


class Ghost:
    """Define a ghost."""
    def __init__(self, game, pos, aim):
        self.game = game
        self.pos = pos
        self.aim = aim

    def move(self):
        """Move a ghost."""
        if self.game.pacman.pos[1] == self.pos[1]:
            if self.game.world.valid(self.pos + vector(5, 0)) and self.game.pacman.pos[0] > self.pos[0]:
                self.aim = vector(5, 0)
                self.pos.move(self.aim)
            elif self.game.world.valid(self.pos + vector(-5, 0)) and self.game.pacman.pos[0] < self.pos[0]:
                self.aim = vector(-5, 0)
                self.pos.move(self.aim)
            elif self.game.world.valid(self.pos + self.aim):
                self.pos.move(self.aim)
            else:
                self.aim = choice([vector(0, 5), vector(0, -5)])
                if self.game.world.valid(self.pos + self.aim):
                    self.pos.move(self.aim)
        elif self.game.pacman.pos[0] == self.pos[0]:
                if self.game.world.valid(self.pos + vector(0, 5)) and self.game.pacman.pos[1] > self.pos[1]:
                    self.aim = vector(0, 5)
                    self.pos.move(self.aim)
                elif self.game.world.valid(self.pos + vector(0, -5)) and self.game.pacman.pos[1] < self.pos[1]:
                    self.aim = vector(0, -5)
                    self.pos.move(self.aim)
                else:
                    self.aim = choice([vector(5, 0), vector(-5, 0)])
                    if self.game.world.valid(self.pos + self.aim):
                        self.pos.move(self.aim)
        else:
            if self.game.world.valid(self.pos + self.aim):
                self.pos.move(self.aim)
            else:
                self.aim = choice([vector(5, 0), vector(-5, 0), vector(0, 5), vector(0, -5)])

    def draw(self):
        """Draw a ghost."""
        goto(self.pos.x + 10, self.pos.y + 10)
        dot(20, 'red')

    def __str__(self):
        """Represent a ghost with a string."""
        return f'Ghost({self.pos})'


class Pacman:
    """Define a pacman.
    With the argument game, Pacman can access its game environment."""
    def __init__(self, game, pos, aim, direction, isdead):
        """aim is where he's going, direction is where he wants to go"""
        self.game = game
        self.pos = pos
        self.aim = aim
        self.direction = direction
        self.isdead = isdead

    def move(self):
        """Move a pacman. If direction is not valid,
        it keeps its aim until direction is valid"""
        if self.game.world.valid(self.pos + self.direction):
            self.aim = self.direction
        if self.game.world.valid(self.pos + self.aim):
            self.pos.move(self.aim)

        i, j = self.game.world.index(self.pos + vector(10, 10))

        if self.game.world.tiles[i][j] == 1:
            """Check if the point is in Pacman"""
            if abs(vector(-200 + j * 20, 180 - i * 20) - self.pos) <= 5:
                self.game.world.tiles[i][j] = 2
                self.game.score.value += 1
                self.game.world.path.up()
                self.game.world.path.goto(self.pos + vector(10, 10))
                self.game.world.path.dot(20)
                if self.game.score.value == 160 * self.game.level:
                    self.game.level += 1
                    if self.game.level % 2 == 0:
                        self.game.world.load(self.game.world.tiles2)
                    else:
                        self.game.world.load(self.game.world.tiles1)


    def change(self, x, y):
        """Change pacman aim if valid."""
        self.direction = vector(x, y)

    def draw(self):
        """Draw a pacman."""
        goto(self.pos.x + 10, self.pos.y + 10)
        dot(20, 'yellow')

    def __str__(self):
        """Represent a pacman with a string."""
        return f'Pacman({self.pos})'


class World:
    """Define the world"""
    def __init__(self, game):
        """Draw world using path."""
        bgcolor('black')
        self.path = Turtle(visible=False)
        self.path.color('blue')
        self.game = game
        self.tiles1 = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0],
                [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ]
        self.tiles2 = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
                [0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
                [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                [0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0],
                [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                [0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                [0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ]
        self.tiles = self.tiles1

    def draw(self):
        """Draw the path."""
        for i in range(20):
            for j in range(20):
                tile = self.tiles[i][j]
                if tile > 0:
                    x = -200 + j * 20
                    y = 180 - i * 20
                    self.square(x, y)

                if tile == 1:
                    self.path.up()
                    self.path.goto(x + 10, y + 10)
                    self.path.dot(2, 'white')

    def load(self, tiles):
        """load a level"""
        self.tiles = tiles
        for i in range(20):
            for j in range(20):
                tile = tiles[i][j]
                if tile == 2:
                    tiles[i][j] = 1
        self.path.clear()
        self.draw()
        self.game.pacman = Pacman(self.game, vector(-40, -80), vector(5, 0), vector(5, 0), False)
        self.game.ghost = [
            Ghost(self.game, vector(-180, 160), vector(5, 0)),
            Ghost(self.game, vector(-180, -160), vector(0, 5)),
            Ghost(self.game, vector(100, 160), vector(0, -5)),
            Ghost(self.game, vector(100, -160), vector(-5, 0)),
        ]

    def index(self, point):
        """Return the index of the point in the tiles,
        return i vertically and j horizontally"""
        x, y = point
        j = int((x + 200) // 20)
        i = int((199 - y) // 20)
        return i, j

    def valid(self, point):
        """Tell if the point is valid (part of the blue path)."""

        i, j = self.index(point)
        if self.tiles[i][j] == 0:
            return False

        i, j = self.index(point + vector(15, 15))
        if self.tiles[i][j] == 0:
            return False

        i, j = self.index(point + vector(15, 0))
        if self.tiles[i][j] == 0:
            return False

        i, j = self.index(point + vector(0, 15))
        if self.tiles[i][j] == 0:
            return False

        return True

    def square(self, x, y):
        """Draw square using path at (x, y)."""
        self.path.up()
        self.path.goto(x, y)
        self.path.down()
        self.path.begin_fill()

        for count in range(4):
            self.path.forward(20)
            self.path.left(90)

        self.path.end_fill()

    def __str__(self):
        "Debug"
        return f'World({len(self.tiles)})'


class Score:
    """Show the score."""
    def __init__(self):
        self.value = 0
        self.writer = Turtle(visible=False)
        self.writer.goto(160, 160)
        self.writer.color('white')
        self.writer.write(self.value, font=(None, 24))

    def draw(self):
        """Display the score."""
        self.writer.undo()
        self.writer.write(self.value, font=(None, 24))


class Game:
    """Define the game class."""
    def __init__(self):
        up()
        setup(600, 400)
        hideturtle()
        tracer(False)
        self.bt_quit = Button((150, 50), 'Quit', (100, 50))
        self.bt_retry = Button((-125, -25), "Retry", (200, 100))

        # The first argument of Pacman and the ghosts is the game (self)
        self.pacman = Pacman(self, vector(-40, -80), vector(5, 0), vector(5, 0), False)
        self.ghost = [
            Ghost(self, vector(-180, 160), vector(5, 0)),
            Ghost(self, vector(-180, -160), vector(0, 5)),
            Ghost(self, vector(100, 160), vector(0, -5)),
            Ghost(self, vector(100, -160), vector(-5, 0)),
        ]
        self.score = Score()
        self.world = World(self)
        self.level = 1

        listen()
        onkey(lambda: self.pacman.change(5, 0), 'Right')
        onkey(lambda: self.pacman.change(-5, 0), 'Left')
        onkey(lambda: self.pacman.change(0, 5), 'Up')
        onkey(lambda: self.pacman.change(0, -5), 'Down')
        onkey(lambda: self.world.load(self.world.tiles2), '2')
        onkey(lambda: self.world.load(self.world.tiles1), '1')
        onscreenclick(self.click)
        self.world.draw()
        self.move()
        done()

    def click(self, x, y):
        """Verify if the click is in a button"""

        if self.bt_quit.inside((x, y)):
            quit()

        if self.bt_retry.inside((x, y)) and self.pacman.isdead:
            self.restart()

    def move(self):
        """Move all game objects."""
        if self.pacman.isdead is False:
            self.pacman.move()
            for ghost in self.ghost:
                ghost.move()
                if abs(self.pacman.pos - ghost.pos) < 19:
                    self.pacman.isdead = True
            if self.pacman.isdead:
                self.bt_retry.draw()
            else:
                self.draw()
                ontimer(self.move, 100)

    def draw(self):
        """Draw all game objects."""
        self.score.draw()
        clear()
        self.pacman.draw()
        self.bt_quit.draw()
        for ghost in self.ghost:
            ghost.draw()

    def restart(self):
        """Restart the game"""
        os.execl(sys.executable, sys.executable, *sys.argv)

Game()
