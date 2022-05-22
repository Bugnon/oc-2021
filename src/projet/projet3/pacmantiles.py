"""Pacman 4 - Score

Transformer en programmation orientée objet avec les classe :

- Ghost *
- Pacman *
- World *
- Score *
- Game

"""

from random import choice
from turtle import *
from freegames import floor, vector

path = Turtle(visible=False)


class Ghost:
    """Define a ghost."""
    def __init__(self, pos, aim):
        self.pos = pos
        self.aim = aim
        
    def move(self):
        """Move a ghost."""
        if world.valid(self.pos + self.aim):
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

ghosts = [
    Ghost(vector(-180, 160), vector(5, 0)),
    Ghost(vector(-180, -160), vector(0, 5)),
    Ghost(vector(100, 160), vector(0, -5)),
    Ghost(vector(100, -160), vector(-5, 0)),
]

class Pacman:
    """Define a pacman."""
    def __init__(self, pos, aim):
        self.pos = pos
        self.aim = aim
        
    def move(self):
        """Move a pacman."""
        if world.valid(self.pos + self.aim):
            self.pos.move(self.aim)

        i, j = world.index(self.pos)

        if world.tiles[i][j] == 1:
            world.tiles[i][j] = 2
            score.score += 1
            x = self.pos[0]
            y = self.pos[1]
            square(x, y)

        
    def draw(self):
        """Draw a pacman."""
        goto(self.pos.x + 10, self.pos.y + 10)
        dot(20, 'yellow')
        
    def __str__(self):
        """Represent a pacman with a string."""
        return f'Pacman({self.pos})'
    
pacman = Pacman(vector(-40, -80), vector(5, 0))

tiles = [
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


tiles2 = [
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
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


class World:
    def __init__(self, tiles):
        """Draw world using path."""        
        bgcolor('black')
        path.color('blue')
        self.tiles = tiles
        
    def draw(self):
        """Draw the path."""
        for i in range(20):
            for j in range(20):
                tile = self.tiles[i][j] 
                if  tile > 0:
                    x = -200 + j * 20
                    y =  180 - i * 20
                    square(x, y)

                if tile == 1:
                    path.up()
                    path.goto(x + 10, y + 10)
                    path.dot(2, 'white')
                    
    def load(self, tiles):
        self.tiles = tiles
        path.clear()
        self.draw()
                    
    def index(self, point):
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
        
        return True        
        
    def __str__(self):
        return f'World({len(self.tiles)})'
                    
world = World(tiles)
        
        
class Score:
    """Show the score."""
    def __init__(self):
        self.score = 0
        self.writer = Turtle(visible=False)
        self.writer.goto(160, 160)
        self.writer.color('white')
        self.writer.write(self.score)
    
    def draw(self):
        """Display the score."""
        self.writer.undo()
        self.writer.write(self.score)
    
score = Score()

def square(x, y):
    """Draw square using path at (x, y)."""
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()


def change(x, y):
    """Change pacman aim if valid."""
    if world.valid(pacman.pos + vector(x, y)):
        pacman.aim = vector(x, y)

def f(x, y):
    """Debug the tile index."""
    p = vector(x, y)
    print(p, world.index(p))


class Game:
    """Define the game class."""
    def __init__(self):
        up()
        setup(420, 420, 370, 0)
        hideturtle()
        tracer(False)

        listen()
        onkey(lambda: change(5, 0), 'Right')
        onkey(lambda: change(-5, 0), 'Left')
        onkey(lambda: change(0, 5), 'Up')
        onkey(lambda: change(0, -5), 'Down')
        onkey(lambda: world.load(tiles2), '2')
        onkey(lambda: world.load(tiles), '1')
        onscreenclick(f)
        world.draw()
        self.move()
        done()
        
    def move(self):
        """Move all game objects."""
        pacman.move()
        for ghost in ghosts:
            ghost.move()
            if abs(pacman.pos - ghost.pos) < 20:
                return
        self.draw()
        ontimer(self.move, 200)
        
    def draw(self):
        """Draw all game objects."""
        score.draw()
        clear()
        pacman.draw()
        for ghost in ghosts:
            ghost.draw()

Game()