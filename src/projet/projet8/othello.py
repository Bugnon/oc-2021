from enum import Enum
from re import T
from telnetlib import DO
from turtle import *
from abc import get_cache_token

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

Author: Raphael Holzer
Date: 11 May 2022
"""


def ligne(p, q):
    """Draws a ligne from point p to point q."""

    goto(p)
    down()
    goto(q)
    up()


class PieceColor(Enum):
    EMPTY = 0
    BLACK = 1
    WHITE = 2


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

    def __init__(self, pos, text, size=16, align='left', erasable=False):
        """Initilizes the text"""
        self.pos = pos
        self.text = text
        self.size = size
        self.align = align
        self.erasable = erasable
        self.writer = self.erasableWriter() if erasable else getturtle()
        # self.erasableWriter = self.erasableWriter()
        self.draw()

    def erasableWriter(self):
        """Get a specific turtle to write and clear  text independently from the rest"""
        t = Turtle()
        t.hideturtle()
        t.up()
        t.setposition(self.pos)
        return t

    def draw(self):
        """Draw the text."""
        goto(self.pos)
        if self.erasable:
            self.writer.clear()
        # self.erasableWriter.write(self.text, font=("Arial", self.size), align=self.align)
        self.writer.write(self.text, font=(
            "Arial", self.size), align=self.align)


class Button:
    def __init__(self, pos, text, size=(80, 30), color='lightgray', align='center'):
        self.rect = Rectangle(pos, size, color)
        x, y = pos
        w, h = size
        self.label = Text((x + w//2, y + h//4), text, h//2, 'center')

    def draw(self):
        self.rect.draw()
        self.label.draw()

    def inside(self, p):
        return self.rect.inside(p)


class CellHeaders:
    """Define a class to draw column names"""

    def __init__(self, n=8, m=8, d=40, ongrid=True):
        """Create a new Grid instance"""
        self.n = n        # vertical (y)
        self.m = m        # horizontal (x)
        self.d = d        # distance
        self.x0 = m * d // 2
        self.y0 = n * d // 2

    def get_col_name(self, col):
        cols = ["A", "B", "C", "D", "E", "F", "G", "H"]
        return cols[col - 1]

    def get_row_name(self, row):
        rows = ["1", "2", "3", "4", "5", "6", "7", "8"]
        return rows[row - 1]

    def draw(self):
        i = 0
        j = 0
        for x in range(-self.x0 + self.d // 2, self.x0, self.d):
            i += 1
            text = self.get_col_name(i)
            Text((x, self.y0 + 10), text=text, size=10)

        for y in range(self.y0 - self.d // 2, -self.y0, -self.d):
            j += 1
            text = self.get_row_name(j)
            Text((-self.x0 - 20, y - self.d // 4), text=text, size=10)


class Grid:
    """Define a grid class with the size (n x m).

    n is the number of lignes,
    m the number of columns.
    """

    def __init__(self, n=8, m=8, d=40, ongrid=True):
        """Create a new Grid instance"""
        self.n = n        # vertical (y)
        self.m = m        # horizontal (x)
        self.d = d        # distance
        self.ongrid = ongrid
        self.x0 = m * d // 2
        self.y0 = n * d // 2

        self.draw()
        # print(self)

    def draw(self):
        """Draw the grid."""
        Rectangle((-self.x0, -self.y0), (2*self.x0, 2*self.y0), color="white")
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

        # X0 = grid size in pixels. x is in number of pixels, from the left
        x += self.x0
        y += self.y0
        if self.ongrid:
            x += self.d // 2
            y += self.d // 2

        i = 9 - int(y // self.d)
        j = int(x // self.d)

        return [i, j]

    def get_cell_coords(self, row, col):
        """Coords in pixels as [x, y]"""
        return [-self.x0 + (col - 1) * self.d + self.d // 2, self.y0 - (row - 1) * self.d - self.d // 2]

    def __str__(self):
        return f'Grid({self.n}, {self.m})'


def position(event):
    a, b = event.x, event.y
    print('{}, {}'.format(a, b))


class Game:
    """This is a general Game class.
    It contains all the game variables and attributes.
    """

    def __init__(self):
        """Set up the game window and the turtle attributes.
        Initilize all the attributes.
        Setup the callback functions.
        """

        setup(600, 500)
        hideturtle()
        tracer(0)
        up()

        self.init_board()

        s = getscreen()
        s.onclick(self.click)
        s.onkey(self.print, 'p')
        s.onkey(clear, 'BackSpace')
        s.onkey(self.draw, ' ')
        s.listen()

        ws = getcanvas()
        ws.bind('<Motion>', self.mouse_pos)
        self.draw()
        done()

    def init_board(self):
        """Init board values"""
        self.score = 0
        self.history = []
        self.grid = Grid()
        self.title = Text((0,  200), 'Othello', 24, 'center')
        self.status = Text((-280, -200), '', erasable=True)
        self.headers = CellHeaders()
        self.bt_clear = Button((200, 100), 'Clear')
        self.bt_new = Button((200, 50), 'New')
        self.currentPlayer = PieceColor.BLACK
        self.possible_moves = []
        self.state = []
        for i in range(8):
            self.state.append([PieceColor.EMPTY] * 8)
        # start pieces
        self.set_cell_value(4, 4, PieceColor.WHITE)
        self.set_cell_value(4, 5, PieceColor.BLACK)
        self.set_cell_value(5, 4, PieceColor.BLACK)
        self.set_cell_value(5, 5, PieceColor.WHITE)
        self.possible_moves = []
        self.calculate_possible_moves()

    def set_status(self, text):
        """Display status"""
        self.status.text = text
        self.status.draw()

    def mouse_pos(self, event):
        """Display current cell in status"""
        # a, b = event.x, event.y
        # # text = '{}, {}'.format(a, b)
        # cell = self.grid.get_cell(event.x, event. y)
        # self.set_status(cell)

    def print(self):
        """Print state"""
        for line in self.state:
            val = ", ".join(str(v.value) for v in line)
            print(val)
        text = []
        for move in self.possible_moves:
            text.append(self.get_cell_name(move[0], move[1]))
        print("Possible moves: {0}".format(text))
        print("Current player: {0}".format(self.currentPlayer))

    def click(self, x, y):
        """Reacts to mouse clicks."""
        if self.grid.inside(x, y):
            x = x//self.grid.d * self.grid.d + self.grid.d//2
            y = y//self.grid.d * self.grid.d + self.grid.d//2
            goto(x, y)
            if (self.put_new_piece_on_board(x, y, self.currentPlayer)):
                self.toggle_player()

        p = x, y
        if self.bt_clear.inside(p):
            clear()
            self.bt_new.draw()
            self.bt_clear.draw()
            self.reset()

        if self.bt_new.inside(p):
            self.init_board()
            self.draw_board()

        self.calculate_possible_moves()

    def put_new_piece_on_board(self, x, y, color: PieceColor):
        """Record a new piece on the board"""
        value = -1
        if self.grid.inside(x, y):
            # cell : [1-8, 1-8]
            cell = self.grid.get_cell(x, y)
            if not cell in self.possible_moves:
                return False
            value = self.get_cell_value(cell[0], cell[1])
            if value == PieceColor.EMPTY:
                print('Putting {0} piece on cell {1}'.format(color, cell))
                self.set_cell_value(
                    cell[0], cell[1], color or self.currentPlayer)
                return True
            else:
                return False

    def draw_possible_moves(self):
        # display possible moves
        for i in range(8):
            for j in range(8):
                if ([i+1, j+1] in self.possible_moves):
                    coords = self.grid.get_cell_coords(i + 1, j + 1)
                    offset = self.grid.d // 2
                    Rectangle((coords[0] - offset, coords[1]-offset), (self.grid.d - 2,
                                                                       self.grid.d - 2), color="lightgreen")

    def draw_board(self):
        """Draw board (i.e. representation of the current state)"""
        self.draw_possible_moves()
        for i in range(8):
            for j in range(8):
                value = self.get_cell_value(i + 1, j + 1)
                coords = self.grid.get_cell_coords(i + 1, j + 1)
                if (value != PieceColor.EMPTY):
                    print("Cell {0}, Coords {1}, Value {2}". format(
                        [i, j], coords, value.value))
                    goto(coords[0], coords[1])
                    dot(self.grid.d, self.get_color(value))

    def draw(self):
        """Draws all the game objects."""
        self.grid.draw()
        self.title.draw()
        self.status.draw()
        self.headers.draw()
        self.bt_clear.draw()
        self.bt_new.draw()
        self.draw_board()
        # down()

    def get_cell_value(self, row, col):
        """Get value stored in cell. Row and Col between 1 and 8"""
        return self.state[row-1][col-1]

    def set_cell_value(self, row, col, piece: PieceColor):
        """Set value stored in cell. Row and Col between 1 and 8"""
        self.state[row-1][col-1] = piece
        self.draw_board()

    def is_empty(self, row, col):
        """Returns True if the cell at [row, col] is empty"""
        value = self.get_cell_value(row, col)
        return value == PieceColor.EMPTY

    def has_opposing_pawn(self, piece_to_kill, cell_candidate):
        # determine the direction where we try to find a pawn of the same color
        row_inc = piece_to_kill[0]-cell_candidate[0]
        col_inc = piece_to_kill[1]-cell_candidate[1]
        # my color
        # self.get_opposing_color(piece_to_kill)
        target_color = self.currentPlayer

        # print("has_opposing_pawn for cell candidate {0}".format(
        #     cell_candidate))
        row = piece_to_kill[0] + row_inc
        col = piece_to_kill[1] + col_inc
        while row <= 8 and row >= 1 and col <= 8 and col >= 1:
            value = self.get_cell_value(row, col)
            if value == target_color:
                print("For player {0}, cell {1} is a valid move because it has an opposing cell {2} to win {3}".format(
                    target_color, self.get_cell_name(cell_candidate[0], cell_candidate[1]), self.get_cell_name(row, col), self.get_cell_name(piece_to_kill[0], piece_to_kill[1])))
                return True
            elif value == PieceColor.EMPTY:
                return False
            row += row_inc
            col += col_inc

        return False

    def get_empty_neighbours(self, row, col):
        candidates = []
        candidates.append([row - 1, col - 1])
        candidates.append([row - 1, col])
        candidates.append([row - 1, col + 1])
        candidates.append([row, col - 1])
        # candidates.append([row, col])
        candidates.append([row, col + 1])
        candidates.append([row + 1, col - 1])
        candidates.append([row + 1, col])
        candidates.append([row + 1, col + 1])
        result = []
        for candidate in candidates:
            if candidate[0] < 1 or candidate[0] > 8 or candidate[1] < 1 or candidate[1] > 8:
                continue
            if not self.is_empty(candidate[0], candidate[1]):
                continue
            if self.has_opposing_pawn([row, col], candidate):
                result.append(candidate)
        return result

    def get_opposing_color(self, color):
        if color == PieceColor.BLACK:
            return PieceColor.WHITE
        else:
            return PieceColor.BLACK

    def calculate_possible_moves(self):
        # Must be empty and adjacent to an opposing pawn and must frame opposing pawns with one pawn of its own color
        # iterate over all empty cells that are close to an opposing pawn
        possible_moves = []
        for i in range(8):
            for j in range(8):
                value = self.get_cell_value(i + 1, j + 1)
                # consider only opposing pawns
                if not value == self.get_opposing_color(self.currentPlayer):
                    continue
                # find opposing pawns neighbours that are empty
                moves = self.get_empty_neighbours(i + 1, j + 1)

                for move in moves:
                    possible_moves.append(move)
        self.possible_moves = possible_moves
        self.draw()
        # find all empty cells that have at least one opposing color among the 8 neighbouring cells
        # amongs those cells, find cells that frame opposing pawns

    def get_cell_name(self, row, col):
        cols = ["A", "B", "C", "D", "E", "F", "G", "H"]
        rows = ["1", "2", "3", "4", "5", "6", "7", "8"]
        return cols[col - 1] + rows[row - 1]

    def toggle_player(self):
        self.currentPlayer = PieceColor.BLACK if self.currentPlayer == PieceColor.WHITE else PieceColor.WHITE
        self.set_status("{0} playing".format(self.currentPlayer))

    def get_current_color(self):
        return "black" if self.currentPlayer == PieceColor.BLACK else "lightgrey"

    def get_color(self, piece_color: PieceColor):

        if piece_color == PieceColor.BLACK:
            return "black"
        elif piece_color == piece_color.WHITE:
            return "lightgrey"
        else:
            return "#FF000000"


game = Game()
