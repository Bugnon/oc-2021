# Othello

Arthur

## Description

Othello est un jeu de plateau à deux joueurs noir et blanc, se jouant sur une grille de 8x8 avec 4 pions blanc et noir placer au centre au début de la partie. 

A son tour de jeu, le joueur doit poser un pion de sa couleur sur une case vide de l’othellier, adjacente à un pion adverse. Il doit également, en posant son pion, encadrer un ou plusieurs pions adverses entre le pion qu’il pose et un pion à sa couleur, déjà placé sur l’othellier. Cette prise en sandwich peut se faire aussi bien horizontalement ou verticalement, qu’en diagnonale. Le joueur retourne le ou les pions qu’il vient d’encadrer, qui devient ainsi de sa couleur. Les pions ne sont ni retirés de l’othellier, ni déplacés d’une case à l’autre.

Si le joueur ne peut pas prendre de pièce adverse, il passe son tour.

Le but du jeu est d’avoir plus de pièce que l’adversaire à la fin de la partie.


## Représentation

Le jeu est représenté avec une liste 2D par une variable ``state``.


```{codeplay}
state = []

for i in range(8):
    state.append([0] *8)

for line in state:
    print(line)
```

La signification 

- 0 : case vide
- 1 : case rempli par joueur 1 (noir)
- 2 : case rempli par joueur 2 (gris)

## Evolution

Le joueur peut cliquer dans une cellule.
Supposons qu'il clique dans la cellue de la ligne 2, colonne 3, ce qui correspond à ``state[2][3]``.

```{codeplay}
state = []

for i in range(8):
    state.append([0] *8)

state[2][3] = 1

for line in state:
    print(line)
```

## Conclusion

Le jeu a été implémenté. Vous pouvez y jouer ci-dessous.

## Le jeu
Cliquez sur Play pour tester

```{codeplay}
from enum import Enum
from tkinter.messagebox import askyesno
from turtle import *
from random import *

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

COLOR_BOARD = 'ForestGreen'
COLOR_BLACK_PIECES = 'Black'
COLOR_WHITE_PIECES = 'White'
COLOR_LAST_MOVE = 'Red'
COLOR_POSSIBLE_MOVES = 'lightgreen'


def ligne(p, q, color='black'):
    """Draws a ligne from point p to point q."""
    up()
    old = pencolor()
    pencolor(color)
    goto(p)
    down()
    goto(q)
    up()
    pencolor(old)


class Rectangle:
    """Draw a filled rectangle."""

    def __init__(self, pos, size, fillcolor='white', color='black'):
        """Initialize the rectangle and draw it."""
        self.pos = pos
        self.size = size
        self.color = color
        self.fillcolor = fillcolor
        self.draw()

    def outline(self):
        """Draw just the outline of the rectangle."""
        goto(self.pos)
        down()
        if (self.color):
            old_color = getturtle().pencolor()
            getturtle().pencolor(self.color)
        for x in self.size * 2:
            forward(x)
            left(90)
        if old_color:
            getturtle().pencolor(old_color)
        up()

    def draw(self):
        """Draw the outline of the rectangle and fill it a color is defined."""
        if self.fillcolor:
            fillcolor(self.fillcolor)
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
        self.writer = getturtle()
        self.draw()

    def draw(self):
        """Draw the text."""
        goto(self.pos)
        self.writer.write(self.text, font=(
            "Arial", self.size), align=self.align)


class Button:
    """Draws a button"""

    def __init__(self, pos, text, size=(80, 30), color='lightgray', align='center'):
        self.rect = Rectangle(pos, size, color)
        x, y = pos
        w, h = size
        self.label = Text((x + w//2, y + h//4), text, h//2, align)

    def draw(self):
        self.rect.draw()
        self.label.draw()

    def inside(self, p):
        return self.rect.inside(p)


class Score:
    """Draws the score"""

    def __init__(self, pos, size=(150, 80), fillcolor='white', color='white', align='center'):
        self.rect = Rectangle(pos, size, fillcolor=fillcolor, color=color)
        x, y = pos
        w, h = size
        self.label_white = Text((x + w//2, y + 3*h//4 - 15),
                                self.get_text_for_white(0), 16, align)
        self.label_black = Text((x + w//2, y + h//4 - 15),
                                self.get_text_for_black(0), 16, align)

    def get_text_for_white(self, score):
        return "WHITE: {0}".format(score)

    def get_text_for_black(self, score):
        return "BLACK: {0}".format(score)

    def set_score(self, score_white, score_black):
        self.label_white.text = self.get_text_for_white(score_white)
        self.label_black.text = self.get_text_for_black(score_black)
        self.draw()

    def draw(self):
        self.rect.draw()
        self.label_white.draw()
        self.label_black.draw()


class Status:
    """Draws the status"""

    def __init__(self, pos, size=(300, 40), fillcolor='white', color='white', align='center'):
        self.rect = Rectangle(pos, size, fillcolor=fillcolor, color=color)
        x, y = pos
        w, h = size
        self.label = Text((x + w//2, y + 3*h//4 - 15), '', 16, align)

    def set_status(self, text):
        self.label.text = text
        self.draw()

    def draw(self):
        self.rect.draw()
        self.label.draw()


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


class PieceColor(Enum):
    """Possible colors for a cell: empty (no piece), black or white"""
    EMPTY = 0
    BLACK = 1
    WHITE = 2


class Grid:
    """Define a grid class with the size (n x m).

    n is the number of lines,
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

    def draw(self):
        """Draw the grid."""
        Rectangle((-self.x0, -self.y0), (2*self.x0, 2*self.y0),
                  fillcolor=COLOR_BOARD, color="white")
        for x in range(-self.x0, self.x0+1, self.d):
            ligne((x, -self.y0), (x, self.y0), "white")

        for y in range(-self.y0, self.y0+1, self.d):
            ligne((-self.x0, y), (self.x0, y), "white")

    def inside(self, x, y):
        """Check if (x, y) is inside the grid."""
        x0 = self.x0
        y0 = self.y0
        if self.ongrid:
            x0 += self.d // 2
            y0 += self.d // 2
        return -x0 < x < x0 and -y0 < y < y0

    def get_cell(self, x, y):
        """Returns the cell at pixel coordinates [x, y].
        The cell returned is in the form [row, column] where 1 <= row <= 8 and 1 <= col <= 8 """

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
        """Returns a string representation of the Grid, used for instance when we call print(grid)"""
        return f'Grid({self.n}, {self.m})'


class Game:
    """This is a general Game class.
    It contains all the game variables and attributes.
    """

    def __init__(self):
        """Set up the game window and the turtle attributes.
        Initilize all the attributes.
        Setup the callback functions.
        """
        # Call turtle reset: force to reset turtle and release resources in case of new game
        reset()
        setup(700, 500)
        hideturtle()
        tracer(0)
        up()

        self.init_board()
        s = getscreen()
        s.onclick(self.click)
        s.onkey(self.print, 'p')
        s.onkey(self.reset, 'BackSpace')
        s.onkey(self.draw, ' ')
        s.listen()

        self.draw()
        done()

    def init_board(self):
        """Init board values"""
        self.score_white = 2
        self.score_black = 2
        self.grid = Grid()
        self.title = Text((0,  200), 'Othello', 24, 'center')
        self.status = Status((-150, -220))
        self.score = Score((-350, 80), fillcolor='white')
        self.headers = CellHeaders()
        self.bt_new = Button((200, 50), 'New')
        self.currentPlayer = PieceColor.BLACK
        self.state = []
        self.last_move = []
        self.possible_moves = []
        for i in range(8):
            self.state.append([PieceColor.EMPTY] * 8)
        # start pieces
        self.set_cell_value(4, 4, PieceColor.WHITE)
        self.set_cell_value(4, 5, PieceColor.BLACK)
        self.set_cell_value(5, 4, PieceColor.BLACK)
        self.set_cell_value(5, 5, PieceColor.WHITE)
        self.set_possible_moves(self.get_possible_moves(self.currentPlayer))
        # if a player cannot play, it is incremented. If it reaches 2, the game is over
        self.try_count = 0

    def set_possible_moves(self, moves):
        """Set the possible_moves variable"""
        self.possible_moves = moves

    def announce_end_of_game(self, text):
        """Announce the end of the game to the user displaying the result and proposing to restart"""
        response = askyesno("La partie est finie", text + "\nOn recommence ?")
        if response:
            self.new_game()

    def increment_try_count(self):
        """Increments the number of tries when a user must pass its turn"""
        self.try_count = self.try_count + 1
        self.check_winner()

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

    def has_possible_moves(self):
        """Return true if the current user has possible moves to play"""
        if len(self.possible_moves) > 0:
            return True
        else:
            return False

    def click(self, x, y):
        """Reacts to mouse clicks."""
        if self.grid.inside(x, y):
            # we have clicked in the grid
            x = x//self.grid.d * self.grid.d + self.grid.d//2
            y = y//self.grid.d * self.grid.d + self.grid.d//2
            goto(x, y)
            if (self.put_new_piece_on_board(x, y, self.currentPlayer)):
                self.try_count = 0
                self.check_winner()
                # the move was valid and we have put a piece on board
                self.toggle_player()
                self.set_possible_moves(
                    self.get_possible_moves(self.currentPlayer))
                self.check_winner()
                self.bot_plays()
                self.draw_board()
                # we cannot play
                if (not self.has_possible_moves()):
                    self.pass_your_turn()
        p = x, y

        if self.bt_new.inside(p):
            self.new_game()

    def pass_your_turn(self):
        """The human user passes its turn and let the bot play"""
        self.increment_try_count()
        self.toggle_player()
        self.set_possible_moves(self.get_possible_moves(self.currentPlayer))
        self.check_winner()
        self.bot_plays()

    def new_game(self):
        """Create a new game: initialize variables and draw a fresh board"""
        game = Game()

    def reset(self):
        """Reset the game. Used for instance with backspace"""
        self.new_game()

    def bot_plays(self):
        """The bot will play if there is a possible move"""
        if (self.has_possible_moves()):
            # bot can play
            # take a random move among all possible moves
            index = randint(0, len(self.possible_moves)-1)
            cell = self.possible_moves[index]
            # save the move the bot is playinf, in order to display it
            self.last_move = cell
            coords = self.grid.get_cell_coords(cell[0], cell[1])
            if (self.put_new_piece_on_board(coords[0], coords[1], self.currentPlayer)):
                print("Bot played: {0}".format(
                    self.get_cell_name(cell[0], cell[1])))
                self.try_count = 0
                self.toggle_player()
                self.set_possible_moves(
                    self.get_possible_moves(self.currentPlayer))
                self.check_winner()
        else:
            # bot cannot play
            self.increment_try_count()
            self.toggle_player()
            self.set_possible_moves(
                self.get_possible_moves(self.currentPlayer))
            self.check_winner()

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
                row = cell[0]
                col = cell[1]
                self.set_cell_value(row, col, color or self.currentPlayer)
                self.eat_pieces(row, col, color)
                self.calculate_score()
                return True
            else:
                return False

    def calculate_score(self):
        """Calculate the current score for white and black and display it"""
        self.score_black = 0
        self.score_white = 0
        for i in range(8):
            for j in range(8):
                value = self.get_cell_value(i+1, j+1)
                if (value == PieceColor.BLACK):
                    self.score_black += 1
                elif (value == PieceColor.WHITE):
                    self.score_white += 1
        self.draw_score()

    def get_pieces_in_line(self, row, col, row_inc, col_inc, opposing_color):
        """Returns a list of pieces of the passed color in the direction
        given by row_inc and col_inc, starting at row, col"""
        r = row+row_inc
        c = col+col_inc
        line_candidates = []
        while r <= 8 and r >= 1 and c <= 8 and c >= 1:
            value = self.get_cell_value(r, c)
            # as long as we have opposing colors, they are candidates
            if value == opposing_color:
                line_candidates.append([r, c])
            # an empty cell means that we cannot eat any piece
            elif value == PieceColor.EMPTY:
                line_candidates = []
                break
            # we have reached a piece of the same color
            else:
                break
            r += row_inc
            c += col_inc
        # we are out of the grid ==> they are not candidates anymore
        if (r < 1 or r > 8 or c < 1 or c > 8):
            line_candidates = []
        return line_candidates

    def eat_pieces(self, row, col, color):
        """"We have put a piece on cell [row, col]. Eat pieces"""
        opposing_color = self.get_opposing_color(color)
        candidates = []
        # we get the pieces of the opposing color that are in a line in each direction
        # and that and with a piece of my color: they are candidates for being eaten
        candidates.extend(self.get_pieces_in_line(
            row, col, -1, 0, opposing_color))
        candidates.extend(self.get_pieces_in_line(
            row, col, 1, 0, opposing_color))
        candidates.extend(self.get_pieces_in_line(
            row, col, 0, -1, opposing_color))
        candidates.extend(self.get_pieces_in_line(
            row, col, 0, 1, opposing_color))
        candidates.extend(self.get_pieces_in_line(
            row, col, 1, 1, opposing_color))
        candidates.extend(self.get_pieces_in_line(
            row, col, -1, -1, opposing_color))
        candidates.extend(self.get_pieces_in_line(
            row, col, -1, 1, opposing_color))
        candidates.extend(self.get_pieces_in_line(
            row, col, 1, -1, opposing_color))
        for candidate in candidates:
            # eating a piece simply means changing its color
            self.set_cell_value(candidate[0], candidate[1], color)

    def draw_board(self):
        """Draw board (i.e. representation of the current state)"""
        self.grid.draw()
        for i in range(8):
            for j in range(8):
                value = self.get_cell_value(i + 1, j + 1)
                coords = self.grid.get_cell_coords(i + 1, j + 1)
                if ([i+1, j+1] in self.possible_moves):
                    # draw possible moves (green background)
                    offset = self.grid.d // 2
                    Rectangle((coords[0] - offset, coords[1]-offset), (self.grid.d,
                                                                       self.grid.d), fillcolor=COLOR_POSSIBLE_MOVES, color='white')
                if (value != PieceColor.EMPTY):
                    # draw pieces
                    goto(coords[0], coords[1])
                    cell = [i+1, j+1]
                    piece_color = self.get_piece_color(value)
                    dot(self.grid.d-4, piece_color)
                    if (cell == self.last_move):
                        dot(10, COLOR_LAST_MOVE)

    def draw(self):
        """Draws all the game objects."""
        self.title.draw()
        self.status.draw()
        self.headers.draw()
        self.bt_new.draw()
        self.draw_board()
        self.draw_score()
        self.draw_current_player()

    def draw_current_player(self):
        """Draws the current player"""
        self.status.set_status(
            "Current player: {0}".format(self.currentPlayer.name))

    def draw_score(self):
        """Draws the score"""
        self.score.set_score(self.score_white, self.score_black)

    def get_cell_value(self, row, col):
        """Get value stored in cell. The value is eithjer BLACK, WHITE or EMPTY. Row and Col between 1 and 8"""
        return self.state[row-1][col-1]

    def set_cell_value(self, row, col, piece: PieceColor):
        """Set value stored in cell into the state. Row and Col between 1 and 8"""
        self.state[row-1][col-1] = piece
        self.draw_board()

    def is_empty(self, row, col):
        """Returns True if the cell at [row, col] is empty"""
        value = self.get_cell_value(row, col)
        return value == PieceColor.EMPTY

    def has_opposing_pawn(self, piece_to_kill, cell_candidate):
        """Return True if we find a cell of the same color as cell_candidate
        piece_to_kill is the cell that we try to trap between two cells of our cell_candidate color.
        The first piece is cell_candidate. We are looking for a second one in a line between cell_candidate and piece_to_kill"""
        # determine the direction where we try to find a pawn of the same color as cell_candidate
        row_inc = piece_to_kill[0]-cell_candidate[0]
        col_inc = piece_to_kill[1]-cell_candidate[1]
        target_color = self.currentPlayer
        row = piece_to_kill[0] + row_inc
        col = piece_to_kill[1] + col_inc
        while row <= 8 and row >= 1 and col <= 8 and col >= 1:
            value = self.get_cell_value(row, col)
            if value == target_color:
                # we have found a piece of the same color as current player, located after piece_to_kill on the same line
                # In other words:
                # candidate -> [row, col] cell -> pawn_1 -> ... -> pawn_n -> last_cell, and last_cell color = candidate color and pawn_1 to pawn_n are of the opposite color
                # print("For player {0}, cell {1} is a valid move because it has an opposing cell {2} to win {3}".format(
                #     target_color, self.get_cell_name(cell_candidate[0], cell_candidate[1]), self.get_cell_name(row, col), self.get_cell_name(piece_to_kill[0], piece_to_kill[1])))
                return True
            elif value == PieceColor.EMPTY:
                # we have an empty cell on this line, before having found a cell of the same color as the current player
                # cell_candidate is thus not a candidate to put a piece
                return False
            row += row_inc
            col += col_inc
        # we have reached the grid border without having found a pawn of the same color as the current player
        return False

    def get_candidates_among_neighbours(self, row, col):
        """Among neighbours of the passed cell, what are the cells where we could put our piece ?"""
        # candidates are the 8 cells around the [row, col] cell
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
            # if the cell is outside the grid, then pass to the next one (it is not a candidate)
            if candidate[0] < 1 or candidate[0] > 8 or candidate[1] < 1 or candidate[1] > 8:
                continue
            # if the cell is not empty, then pass to the next one (we will not be able to put a piece there)
            if not self.is_empty(candidate[0], candidate[1]):
                continue
            # if we have in line candidate -> [row, col] cell -> pawn_1 -> ... -> pawn_n -> last_cell
            # and last_cell color == candidate color and pawn_1 to pawn_n color == opposite color
            if self.has_opposing_pawn([row, col], candidate):
                # then it means that we can put a piece there
                result.append(candidate)
        return result

    def get_opposing_color(self, color):
        """Returns the color of the other user"""
        if color == PieceColor.BLACK:
            return PieceColor.WHITE
        else:
            return PieceColor.BLACK

    def get_possible_moves(self, player):
        """Returns a list of cells [row, col] where we can put a piece to eat adversary pieces"""
        # A possible move is a cell that
        # 1. must be empty
        # 2. must be adjacent to an opposing pawn (i.e. black if current player is white)
        # 3. must have a pawn of the same color as the current player after the opposing pawns on the same line
        # iterate over all empty cells that are close to an opposing pawn
        possible_moves = []
        opposing_color = self.get_opposing_color(player)
        for i in range(8):
            for j in range(8):
                value = self.get_cell_value(i + 1, j + 1)
                # we are looking for cells that contain pieces of the opposing color (e.g. white cells if current player is black)
                if value != opposing_color:
                    continue
                # for these cells, we are looking for cells that have empty neighbours
                moves = self.get_candidates_among_neighbours(i + 1, j + 1)

                for move in moves:
                    possible_moves.append(move)
        return possible_moves
        # find all empty cells that have at least one opposing color among the 8 neighbouring cells
        # amongs those cells, find cells that frame opposing pawns

    def get_cell_name(self, row, col):
        """Returns the name of the cell (e.g. A4, F2)"""
        cols = ["A", "B", "C", "D", "E", "F", "G", "H"]
        rows = ["1", "2", "3", "4", "5", "6", "7", "8"]
        return cols[col - 1] + rows[row - 1]

    def toggle_player(self):
        """Changes the current player"""
        self.currentPlayer = PieceColor.BLACK if self.currentPlayer == PieceColor.WHITE else PieceColor.WHITE
        self.draw_current_player()

    def get_piece_color(self, piece_color: PieceColor, cell=[0, 0]):
        """Returns the color to use to draw a pawn"""
        # if cell == self.last_move:
        #     # that's the last move of the bot
        #     return COLOR_LAST_MOVE
        if piece_color == PieceColor.BLACK:
            return COLOR_BLACK_PIECES
        elif piece_color == piece_color.WHITE:
            return COLOR_WHITE_PIECES
        else:
            # empty
            return "#FF000000"

    def check_winner(self):
        """Check if someone has won the game and announce it"""
        moves1 = self.get_possible_moves(PieceColor.BLACK)
        moves2 = self.get_possible_moves(PieceColor.WHITE)
        if len(moves1) != 0 and len(moves2) != 0:
            # we have possible moves
            print("We can still play...")
            return

        if self.try_count < 2:
            # we can still do sth: pass your turn, but not more than once
            print("Try count: {0}".format(self.try_count))
            return
        # we cannot play anymore. So who won ?
        if self.score_white > self.score_black:
            self.announce_end_of_game("WHITE WON !!")
        elif self.score_white < self.score_black:
            self.announce_end_of_game("BLACK WON !!")


game = Game()
```