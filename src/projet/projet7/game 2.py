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
        history / board, switch_players, 
        
        check_win,
        
        undo, reset, save, click, play, draw

to add:
- Player.score
- Player.chrono
"""

from http.client import SWITCHING_PROTOCOLS
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
            pencolor('black')
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
    
    def __init__(self, pos, text, size=16, align='center', col='black'):
        """Initilizes the text."""
        self.pos = pos
        self.text = text
        self.size = size
        self.align = align
        self.col = col
        self.draw()


    def draw(self):
        """Draw the text."""
        goto(self.pos)
        color(self.col)
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
        return -x0 < x < x0 - self.d // 2 and -y0 < y < y0 - self.d // 2
    

    def get_cell(self, x, y, pixels=False):
        """Returns the coordinates of center.
        The result will be between 0 and 5 or 6 (for y or x) if pixels=False.
        Otherwise, the result will be in pixel (like “-104.0 -78.0“).
        """
        
        x = (x + self.d // 2) // self.d * self.d
        y = y // self.d * self.d + self.d // 2

        if pixels:
            return x, y
        
        else:
            i = int(x // self.d) + self.m // 2
            j = int(y // self.d) - self.n // 2
            return i, j

    
    def draw(self):
        """Draw the grid."""
        up()
        colors = {0:'deepskyblue', 1:'red', 2:'yellow', 3:'lime', 4:'black'}
        for x in range(self.m):
            for y in range(self.n):
                goto(-self.x0 + x * self.d + self.d // 2, self.y0 - y * self.d - self.d // 2)
                col = colors[self.state[y][x]]
                
                if col != 'lime' and col != 'black':
                    dot(self.d * 25 // 32, 'black')
                    dot(self.d * 3 // 5, col)
                elif col == 'lime':
                    dot(self.d * 2 // 5, col)
                else:
                    dot(self.d // 4, col)


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

        dot(1500, 'deepskyblue')
        write('Please enter the names of\nthe players in the console', font=('Times', 30), align='center')
        
        title = '\n* * * CONNECT 4 * * *\n\n\n'
        rules = 'Goal of the game :\n\n\t-> The goal is to align 4 tokens of your colour vertically, horizontally or diagonally.\n\n\n'
        how_to_play = 'How to play ?\n\n\t'
        using_the_mouse = '- by using the mouse :\n\t\t- play : click on the column you want to play in.\n\t\t- undo (cancel the last move), new (reset the board), reset all (except the names), quit : click on the buttons.\n\n\t'
        using_the_keyboard = '- by using the keyboard :\n\t\t- play : the columns are numbered from 1 to 7.\n\t\t- undo (cancel the last move): use the “delete“ button.\n\t\t- new (reset the board) : Tabulation.\n\t\t- reset all (except the names) : R\n\t\t- quit : Q\n\t\t- close the window : X\n\n\n'
        before_starting = 'Before starting, please enter the names of the players :\n'
        print(title + rules + how_to_play + using_the_mouse + using_the_keyboard + before_starting)

        input_player1 = input('\tName of the first player : ')
        input_player2 = input('\n\tName of the second player : ')

        print('\nNames registered ! You can now play on the game\'s screen.\n\n\nHave a good game :)\n')

        self.grid = Grid()
        self.title = Text((0,  168), 'Connect 4', size=24, col='black')
        # self.title2 = Text((-2,  166), 'Connect 4', size=24, col='grey')
        self.author = Text((285, -190), 'by Emilien Barde', align='right')
        self.column_names = Text((0, -150), ' 1         2         3         4         5         6         7', size='15', col='white')
        
        self.bt_undo = Button((200, 100), 'Undo')
        self.bt_new = Button((200, 50), 'New')
        self.bt_reset_scores = Button((200, 0), 'Reset all')
        self.bt_quit = Button((200, -50), 'QUIT', color='slategrey')
        self.bt_close = Button((-80, -60), 'CLOSE', (160, 60), color='red', displayed=False)
        
        self.player1 = Player(input_player1, 'red')
        self.player2 = Player(input_player2, 'yellow')
        
        self.scores = Text((-280, 50), f'Scores :\n\n{self.player1.name} : {self.player1.score}\n\n{self.player2.name} : {self.player2.score}', align='left')
        self.scores_eraser = Rectangle(self.scores.pos, (80, 110), color='deepskyblue', outline=False)
        self.win_message = Text((-285, -80), 'Nobody win !!!', size=18, align='left')
        self.win_message_eraser = Rectangle(self.win_message.pos, (100, 100), color='deepskyblue', outline=False)
        self.status = Text((-285, -190), f'{self.player1.name} ({self.player1.col}) to move', align='left')
        self.status_eraser = Rectangle(self.status.pos, (300, 20), color='deepskyblue', outline=False)
        
        self.players = (self.player1, self.player2)
        self.current_player = 1
        self.moves = 0
        self.playing = True
        self.no_winner = False
        self.history = []
        self.run = True

        self.reset()


        s = getscreen()

        # when the player uses the keyboard
        s.onclick(self.click)

        # when the player uses the keyboard
        if self.run:
            for num in range(1, 8):
                s.onkey(lambda column=num : self.play(column - 1), num)
            s.onkey(lambda:self.undo(), 'BackSpace')
            s.onkey(lambda:self.reset(), 'Tab')
            s.onkey(lambda:self.reset_scores(), 'r')
            s.onkey(lambda:self.quit(), 'q')
        s.onkey(lambda:quit(), 'x')

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


    def switch_players(self):
        """Switch the current player and the game's status."""
        self.current_player = self.current_player % 2 + 1
        player = self.players[self.current_player - 1]  # to simplify the next line
        self.status.text = f'{player.name} ({player.col}) to move'
    
    
    def check_win(self):
        """Check if a player has won by lining up 4 tokens."""
        
        self.draw()

        # some useful lists
        winning_cells = []
        winning_coordinates = []

        
        # check the columns
        for column in range(7):
            for line in range(6):
                cell_test = self.grid.state[line][column]

                # we add a token (the value of the cell_test) to the list
                if cell_test == 1 or cell_test == 2:
                    winning_cells.append(cell_test)
                    winning_coordinates.append([line, column])

                    # we remove some tokens if they are not all identical
                    while winning_cells.count(winning_cells[0]) != len(winning_cells):
                        winning_cells.pop(0)
                        winning_coordinates.pop(0)
                
                    # we check if there is 4 identical winning cells
                    if len(winning_cells) == 4:
                        # we use the coordinates of the winning cells to change the grid's state
                        for coordinates in winning_coordinates:
                            self.grid.state[coordinates[0]][coordinates[1]] = 3
                        self.playing = False
                        self.draw()
                        break
                    
                if cell_test == 0:
                    winning_cells.clear()
                    winning_coordinates.clear()
    
            if not self.playing:
                break
            
            else:
                winning_cells.clear()
                winning_coordinates.clear()


        # check the lines
        for line in range(6):
            for column in range(7):
                cell_test = self.grid.state[line][column]

                # we add a token (the value of the cell_test) to the list
                if cell_test == 1 or cell_test == 2:
                    winning_cells.append(cell_test)
                    winning_coordinates.append([line, column])

                    # we remove some tokens if they are not all identical
                    while winning_cells.count(winning_cells[0]) != len(winning_cells):
                        winning_cells.pop(0)
                        winning_coordinates.pop(0)
                
                    # we check if there is 4 identical winning cells
                    if len(winning_cells) == 4:
                        # we use the coordinates of the winning cells to change the grid's state
                        for coordinates in winning_coordinates:
                            self.grid.state[coordinates[0]][coordinates[1]] = 3
                        self.playing = False
                        self.draw()
                        break
                
                if cell_test == 0:
                    winning_cells.clear()
                    winning_coordinates.clear()

            if not self.playing:
                break
            
            else:
                winning_cells.clear()
                winning_coordinates.clear()
        

        # check the first diagonals
        for diagonal in range(12):
            col_num = max(0, diagonal - 7) # 0 à 7
            line_num = min(diagonal, 6) # de 0 à 6
            # print(f'diagonal : {diagonal} - col_num : {col_num} - line_num : {line_num}')
            
            for i in range(col_num, line_num):
                # print(i, diagonal - i - 1)
                cell_test = self.grid.state[i][diagonal - i - 1]

                # we add a token (the value of the cell_test) to the list
                if cell_test == 1 or cell_test == 2:
                    winning_cells.append(cell_test)
                    winning_coordinates.append([i, diagonal - i - 1])

                    # we remove some tokens if they are not all identical
                    while winning_cells.count(winning_cells[0]) != len(winning_cells):
                        winning_cells.pop(0)
                        winning_coordinates.pop(0)

                    # we check if there is 4 identical winning cells
                    if len(winning_cells) == 4:
                        # we use the coordinates of the winning cells to change the grid's state
                        for coordinates in winning_coordinates:
                            self.grid.state[coordinates[0]][coordinates[1]] = 3
                        self.playing = False
                        self.draw()
                        break
                
                if cell_test == 0:
                    winning_cells.clear()
                    winning_coordinates.clear()

            if not self.playing:
                break
            
            else:
                winning_cells.clear()
                winning_coordinates.clear()
        

        # check the second diagonals
        for diagonal in range(12):
            col_num = max(0, 5 - diagonal)
            line_num = min(12 - diagonal, 6)
            # print(f'diagonal : {diagonal} - col_num : {col_num} - line_num : {line_num}')
            
            for i in range(col_num, line_num):
                # print(i, i + diagonal - 5)
                cell_test = self.grid.state[i][i + diagonal - 5]

                # we add a token (the value of the cell_test) to the list
                if cell_test == 1 or cell_test == 2:
                    winning_cells.append(cell_test)
                    winning_coordinates.append([i, i + diagonal - 5])

                    # we remove some tokens if they are not all identical
                    while winning_cells.count(winning_cells[0]) != len(winning_cells):
                        winning_cells.pop(0)
                        winning_coordinates.pop(0)

                    # we check if there is 4 identical winning cells
                    if len(winning_cells) == 4:
                        # we use the coordinates of the winning cells to change the grid's state
                        for coordinates in winning_coordinates:
                            self.grid.state[coordinates[0]][coordinates[1]] = 3
                        self.playing = False
                        self.draw()
                        break
                
                if cell_test == 0:
                    winning_cells.clear()
                    winning_coordinates.clear()

            if not self.playing:
                break
            
            else:
                winning_cells.clear()
                winning_coordinates.clear()

        # the board is full
        if self.moves == 6 * 7:
            self.no_winner = True
            for line in range(self.grid.n):
                for cell in range(self.grid.m):
                    self.grid.state[line][cell] = 4
            
            self.win_message_eraser.draw()
            self.win_message.text = f'*  *  *  *  *\nNobody\nWIN !!!\n*  *  *  *  *'
            self.win_message.draw()
            self.status_eraser.draw()
            
            self.playing = False

            self.draw()


    def undo(self):
        """Cancel the last move."""

        self.switch_players()
        if not self.playing:
            if self.no_winner:
                self.no_winner = False
            else:
                self.players[self.current_player - 1].score -= 1
            
            # draw the scores
            self.win_message_eraser.draw()
            self.scores.text = f'Scores :\n\n{self.player1.name} : {self.player1.score}\n\n{self.player2.name} : {self.player2.score}'         
            self.scores_eraser.draw()
            self.scores.draw()
            self.playing = True
        
        # when there is only one move played
        if len(self.history) <= 2:
            self.reset()

        else:
            last_state = []

            for line in range(6):
                last_cells = []
                for cell in range(7):
                    # the cells of one column are added to the temporary cells's list
                    last_cells.append(int(self.history[-2][line][cell]))
                
                # the line is added to the temporary state's list
                last_state.append(list(last_cells))
            
            self.grid.state = last_state
            self.history.pop()
            
            self.moves -= 1

        self.draw()
    

    def reset(self):
        """Reset the game.
        It resets the grid, the history and the current player."""

        self.playing = True

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

        # reset the current player and the numbers of moves
        self.current_player = (self.player1.score + self.player2.score) % 2 + 1
        self.status.text = f'{self.players[self.current_player - 1].name} ({self.players[self.current_player - 1].col}) to move'
        self.moves = 0
        
        # board and game drawing
        self.board()
        self.scores.draw()
        self.draw()
    

    def reset_scores(self):
        for player in self.players:
            player.score = 0
        self.reset()
        self.scores.text = f'Scores :\n\n{self.player1.name} : {self.player1.score}\n\n{self.player2.name} : {self.player2.score}'
        self.scores_eraser.draw()
        self.scores.draw()


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
        # for i in range(len(self.history)):
        #     print(f'step {i + 1} :')
        #     for j in range(6):
        #         print('\t\t', self.history[i][j])


    def play(self, column):
        """Change the state of one grid's column."""
        
        if self.playing:
            # from the bottom to the top of the column
            for j in range(5, -1, -1):
                # if the cell is free, we change his value
                if self.grid.state[j][column] == 0:
                    self.grid.state[j][column] = self.current_player
                    self.moves += 1
                    self.save()
                    self.check_win()

                    
                    if not self.playing and  not self.no_winner:
                        # add a point to the score of the current player
                        self.players[self.current_player - 1].score += 1
                        self.scores.text = f'Scores :\n\n{self.player1.name} : {self.player1.score}\n\n{self.player2.name} : {self.player2.score}'
                        
                        # draw the scores
                        self.scores_eraser.draw()
                        self.scores.draw()
                        
                        self.win_message_eraser.draw()
                        self.win_message.text = f'*  *  *  *  *\n{self.players[self.current_player - 1].name}\nWINS !!!\n*  *  *  *  *'
                        self.win_message.draw()
                        self.switch_players()
                    elif not self.no_winner:
                        self.switch_players()
                        self.status_eraser.draw()
                        self.status.draw()
                    break
    
    
    def quit(self):
        self.run = False
        dot(1500, 'deepskyblue')
        goto(0, 50)
        write('Thanks for playing !', font=('Times', 40), align='center')
        self.author.draw()
        self.bt_close.displayed = True
        self.bt_close.draw()
    

    def click(self, x, y):
        """Reacts to mouse clicks."""

        if self.run:
            # the player clicks on the grid
            if self.grid.inside(x, y) and self.playing:
                i = self.grid.get_cell(x, y)[0]
                self.play(i)
            
            # buttons
            p = x, y

            # the player clicks on the “undo“ button
            if self.bt_undo.inside(p) and len(self.history) > 1:
                self.undo()

            
            # the player clicks on the “new“ button
            if self.bt_new.inside(p):
                self.reset()
                self.draw()

            # the player clicks on the “reset all“ button
            if self.bt_reset_scores.inside(p):
                self.reset_scores()
            

            # the player clicks on the “quit“ button
            if self.bt_quit.inside(p):
                self.quit()
        
        else:
            if self.bt_close.inside((x, y)):
                quit()

        # print the grid's state (debugging)
        # for i in range(len(self.history)):
        #     print(f'step {i + 1} :')
        #     for j in range(6):
        #         print('\t\t', self.history[i][j])
        # print('\n')
        

    def draw(self):
        """Draws all the game objects."""
        self.grid.draw()
        self.title.draw()
        # self.title2.draw()
        self.author.draw()
        self.column_names.draw()

        self.status_eraser.draw()
        if self.playing:
            self.status.draw()
        else:
            self.scores.draw()

        for button in [self.bt_undo, self.bt_new, self.bt_reset_scores, self.bt_quit]:
            if button.displayed:
                button.draw()


game = Game()

done()
