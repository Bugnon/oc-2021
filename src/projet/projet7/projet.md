# Puissance 4

Emilien

## But du jeu

Aligner 4 jetons de la même couleur horizontalement, verticalement ou en diagonale.

## Description du jeu

On joue sur un plateau 6x7, les premiers jetons se déposent sur la ligne du bas, puis les jetons suivants viennent se poser “par-dessus“ (comme si on jouait avec de la gravité)

## Comment jouer

On peut utiliser la souris ou le clavier (touches 1 à 7)pour choisir dans quelle colonne est-ce que l’on désire placer son jeton.

## Options supplémentaires

Il est possible d’annuler les coups joués, de créer une nouvelle partie et de réinitialiser les scores.

## Réprésentation de l'état

L'état du jeu est représenté avec un tableau 2D appelé ``state``

```{codeplay}
state = []

for i in range(6):
    state.append([0] *7)

for line in state:
    print(line)
```

## Codeplay

Voici le jeu final !
(Cliquer sur la flèche bleue pour lancer le jeu, puis retrouver la fenêtre du jeu au bas de la page)

```{codeplay}
"""
Game's name :
    Connect 4
    (“Puissance 4“ in french)

Rules :
    This is a game for two players, playing in a 6x7 board.

    When a piece is placed in a column, it is placed in the lowest
    free cell of the column (as if playing with gravity).

    The goal of the game is to align 4 tokens of the same colour horizontally,
    vertically or diagonally.

My code :
    In my version, the score of the players represents the number of games won, 
    and they can cancel their move, create a new game or reset the scores at any time.

    When you run the code, you will first see some gameplay informations in the
    console, and will have to enter the names of the 2 players.
    You will then can play on the window using the mouse or keyboard.

    Have fun !

Information about the code :
    classes : 6
    lines : 910


Note: if there are any problems when downloading the audios,
      it should be a problem of the path to find the right audio.
      the lines of code concerned are 289-291, 778-780 and 788-190.
      In this website there is no sound, the lines concerned are ignored


Emilien Barde
15.06.2022
"""


from email.mime import audio
from http.client import SWITCHING_PROTOCOLS
from textwrap import fill
from tkinter import filedialog

from turtle import *
import os
from pygame import init
from time import sleep
from pygame.mixer import music


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
        """Runs along the edges of the rectangle."""

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

        """The grid's state is a two-dimensional array.
        By convention :
            player one's token = 1 ; player two's token = 2
            free cell = 0 ; winning cell = 3 ; draw = 4
        """
        
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
    

    def get_column(self, x):
        """Returns the coordinates (between 0 and 6)
        of the column in which the player has played.
        """
        
        x = (x + self.d // 2) // self.d * self.d

        i = int(x // self.d) + self.m // 2

        return i

    
    def draw(self):
        """Draw the grid."""
        
        up()
        colors = {0:'deepskyblue', 1:'red', 2:'yellow', 3:'limegreen', 4:'black'}
        
        # we go through the columns
        for x in range(self.m):

            # we go through the lines
            for y in range(self.n):

                goto(-self.x0 + x * self.d + self.d // 2, self.y0 - y * self.d - self.d // 2)
                col = colors[self.state[y][x]]

                # the cell is free or is fulled by a token
                if col != 'limegreen' and col != 'black':
                    dot(self.d * 25 // 32, 'black')
                    dot(self.d * 3 // 5, col)
                
                # the cell is a winning cell
                elif col == 'limegreen':
                    dot(self.d * 2 // 5, col)
                
                # there is a draw (no one has won)
                else:
                    dot(self.d // 4, col)


class Player:
    """Create a player (with attributes only)."""

    def __init__(self, name, col):
        self.name = name
        self.col = col
        self.score = 0


class Game:
    """This is a general Game class.
    It contains all the game variables, methods and attributes.
    """
    
    def __init__(self):
        """Set up the game window and the turtle attributes.
        Write some informations on the console.
        Start the music.
        Initilize all the attributes.
        Setup the callback functions.
        """
        
        # window and turtle set up
        setup(600, 400)
        hideturtle()
        tracer(0)
        up()

        # first message on the screen
        dot(1500, 'deepskyblue')
        write('Please enter the names of\nthe players in the console', font=('Times', 30), align='center')
        

        # strings to display in the console
        title = '\n\n\n\n\n\n\n\n\n\n\n\n\n* * * CONNECT 4 (Puissance 4) * * *\n\n\n'
        rules = 'Goal of the game :\n\n\t-> The goal is to align 4 tokens of your colour vertically, horizontally or diagonally.\n\n\n'
        how_to_play = 'How to play ?\n\n\t'
        using_the_mouse = '- By using the mouse : click on the column you want to play in.\n\t'
        using_the_keyboard = '- By using the keyboard : use the keys 1 to 7 to play in the respective column.\n\n\n'
        dont_play_fast = '!!! WARNING !!! : don\'t play too fast, or lightning will fall on you\n\n\n'
        buttons_definition = 'Buttons (and keyboard shortcuts) :\n\n\t  Name\t\tAction\t\t\t\t\t\tKeyboard shortcut\n\n\t'
        button_undo_new = '- Undo\t\t-> cancel the last move\t\t\t\tDelete\n\t- New\t\t-> create a new game by clearing the board\tTabulation\n\t'
        button_reset = '- Reset all\t-> reset the scores, clear the board,\t\tR\n\t\t\t   only the names are preserved\n\t'
        button_quit_close = '- QUIT\t\t-> quit the game\t\t\t\tQ\n\t- CLOSE\t\t-> close the window\t\t\t\tX\n\n\n\n'
        before_starting = 'Before starting, please enter the names of the players :\n'
        print(title + rules + how_to_play + using_the_mouse + using_the_keyboard + dont_play_fast +
            buttons_definition + button_undo_new + button_reset + button_quit_close + before_starting)

        # input for the names of the players
        input_player1 = input('\tName of the first player : ')
        input_player2 = input('\n\tName of the second player : ')

        print('\nNames registered ! You can now play on the game\'s screen.\n\n\nHave a good game :)\n\n')


        # load the music
        # init()
        # fileDir = os.path.dirname(os.path.realpath('__file__'))
        # print(fileDir)
        # filename = os.path.join(fileDir, 'src/projet/projet7/connect_4_audio.mp3')       
        # music.load(filename)

        # play the music (-1 <=> infinite loop)
        # music.play(-1)
        

        # initialization of the attributes : creation of objects

        # grid and texts
        self.grid = Grid()
        self.title = Text((0,  168), 'Connect 4', size=24, col='black')
        self.author = Text((285, -190), 'by Emilien Barde', align='right')
        self.columns_name = Text((0, -150), ' 1         2         3         4         5         6         7', size='15', col='white')
        
        # buttons
        self.bt_undo = Button((200, 100), 'Undo')
        self.bt_new = Button((200, 50), 'New')
        self.bt_reset_scores = Button((200, 0), 'Reset all')
        self.bt_quit = Button((200, -50), 'QUIT', color='slategrey')
        self.bt_close = Button((-80, -60), 'CLOSE', (160, 60), color='red', displayed=False)
        
        # players
        self.player1 = Player(input_player1, 'red')
        self.player2 = Player(input_player2, 'yellow')
        
        # erasables text (rectangles are used to erase old text)
        self.scores = Text((-280, 50), f'Scores :\n\n{self.player1.name} : {self.player1.score}\n\n{self.player2.name} : {self.player2.score}', align='left')
        self.scores_eraser = Rectangle((self.scores.pos[0] - 5, self.scores.pos[1] - 10), (100, 100), color='deepskyblue', outline=False)
        self.win_message = Text((-285, -80), 'Nobody win !!!', size=18, align='left')
        self.win_message_eraser = Rectangle(self.win_message.pos, (100, 100), color='deepskyblue', outline=False)
        self.status = Text((-285, -190), f'{self.player1.name} ({self.player1.col}) to move', align='left')
        self.status_eraser = Rectangle((self.status.pos[0] - 5, self.status.pos[1]), (450, 20), color='deepskyblue', outline=False)
        

        # initialization of the attributes : other types of variables
        self.players = (self.player1, self.player2)
        self.current_player = 1
        self.moves = 0
        self.playing = True
        self.no_winner = False
        self.history = []
        self.run = True


        # game initialization
        self.reset()


        # call back functions
        s = getscreen()

        # when the player uses the mouse
        s.onclick(self.click)

        # when the player uses the keyboard
        if self.run:

            # test the keys from 1 to 7
            for num in range(1, 8):
                s.onkey(lambda column=num : self.play(column - 1), num)
            
            # test other specifics keys
            s.onkey(lambda:self.undo(), 'BackSpace')
            s.onkey(lambda:self.reset(), 'Tab')
            s.onkey(lambda:self.reset_scores(), 'r')
            s.onkey(lambda:self.quit(), 'q')
        
        s.onkey(lambda:quit(), 'x')


        s.listen()
    
    
    def board(self):
        """Draw the background, the darkblue board
        and the name of the columns."""
        
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

        # writing of the column's name
        self.columns_name.draw()


    def switch_players(self):
        """Switch the current player and the game's status."""
        
        # switch the current player
        self.current_player = self.current_player % 2 + 1

        # switch the game's status
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
                
                # if the cell is empty (no token), we clear both lists
                if cell_test == 0:
                    winning_cells.clear()
                    winning_coordinates.clear()

            # if someone has won, we stop checking the rest of the board
            if not self.playing:
                break
            
            # before moving on to the next column, we clear both lists
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
                
                # if the cell is empty (no token), we clear both lists
                if cell_test == 0:
                    winning_cells.clear()
                    winning_coordinates.clear()

            # if someone has won, we stop checking the rest of the board
            if not self.playing:
                break
            
            # before moving on to the next line, we clear both lists
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
                
                # if the cell is empty (no token), we clear both lists
                if cell_test == 0:
                    winning_cells.clear()
                    winning_coordinates.clear()

            # if someone has won, we stop checking the rest of the board
            if not self.playing:
                break
            
            # before moving on to the next diagonal, we clear both lists
            else:
                winning_cells.clear()
                winning_coordinates.clear()
        

        # check the second diagonals
        for diagonal in range(12):
            col_num = max(0, 5 - diagonal)
            line_num = min(12 - diagonal, 6)
            
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
                
                # if the cell is empty (no token), we clear both lists
                if cell_test == 0:
                    winning_cells.clear()
                    winning_coordinates.clear()

            # if someone has won, we stop checking the rest of the board
            if not self.playing:
                break
            
            # before moving on to the next diagonal, we clear both lists
            else:
                winning_cells.clear()
                winning_coordinates.clear()


        # the board is full
        if self.moves == 6 * 7:
            self.no_winner = True

            # all cells take the value of 4 (which means there is no winner)
            for line in range(self.grid.n):
                for cell in range(self.grid.m):
                    self.grid.state[line][cell] = 4
            
            # we erase the old win message, update it and display it
            self.win_message_eraser.draw()
            self.win_message.text = f'*  *  *  *  *\nNobody\nWIN !!!\n*  *  *  *  *'
            self.win_message.draw()

            # we erase the game's status (no one is playing)
            self.status_eraser.draw()
            
            self.playing = False

            self.draw()


    def undo(self):
        """Cancel the last move."""

        self.switch_players()

        # when someone has won (or there was a draw)
        if not self.playing:

            # if there was a draw
            if self.no_winner:
                self.no_winner = False
            
            # if someone has won
            else:
                self.players[self.current_player - 1].score -= 1
            

            # we erase the win message
            self.win_message_eraser.draw()

            # we erase the old scores, update it and display it
            self.scores_eraser.draw()
            self.scores.text = f'Scores :\n\n{self.player1.name} : {self.player1.score}\n\n{self.player2.name} : {self.player2.score}'
            self.scores.draw()

            self.playing = True
        
        # when there is only one move played
        if len(self.history) <= 2:
            # we reset the game
            self.reset()

        # when there was more than one move played
        else:
            last_state = []

            # we go through lines and columns
            for line in range(6):
                last_cells = []

                for cell in range(7):
                    # the cells of one column are added to the temporary cells's list
                    last_cells.append(int(self.history[-2][line][cell]))
                
                # the line is added to the temporary state's list
                last_state.append(list(last_cells))
            
            # we update the grid's state and change the history
            self.grid.state = last_state
            self.history.pop()
            
            self.moves -= 1

        self.draw()
    

    def reset(self):
        """Reset the game.
        It resets the grid, the history, the current player,
        the numbers of moves played and finally draw the board and the game."""

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
        """Reset the score of both players and display it."""

        # reset the players's score
        for player in self.players:
            player.score = 0
        
        # reset the game
        self.reset()

        # update the text's score, erase the old scores and display the new one
        self.scores.text = f'Scores :\n\n{self.player1.name} : {self.player1.score}\n\n{self.player2.name} : {self.player2.score}'
        self.scores_eraser.draw()
        self.scores.draw()


    def save(self):
        """Save the state of the game in the history."""

        current_state = []

        # we go through lines and columns
        for line in range(6):
            current_cells = []

            for cell in range(7):
                # the cells of one column are added to the temporary cells's list
                current_cells.append(int(self.grid.state[line][cell]))
            
            # the line is added to the temporary state's list
            current_state.append(list(current_cells))
        
        # we add the current state to the history
        self.history.append(list(current_state))


    def play(self, column):
        """Change the state of one grid's column."""
        
        # no one must have won
        if self.playing:

            # from the bottom to the top of the column
            for j in range(5, -1, -1):

                # if the cell is free
                if self.grid.state[j][column] == 0:
                    
                    # we change the cell's value (depending of the current player)
                    self.grid.state[j][column] = self.current_player

                    self.moves += 1
                    self.save()
                    self.check_win()

                    # after the check_win function, someone has maybe won
                    # if someone has won (not a draw)
                    if not self.playing and  not self.no_winner:

                        # add a point to the score of the current player
                        self.players[self.current_player - 1].score += 1

                        # update the text's scores
                        self.scores.text = f'Scores :\n\n{self.player1.name} : {self.player1.score}\n\n{self.player2.name} : {self.player2.score}'
                        
                        # erase the old scores and display the new one
                        self.scores_eraser.draw()
                        self.scores.draw()
                        
                        # update the text of the win message
                        self.win_message.text = f'*  *  *  *  *\n{self.players[self.current_player - 1].name}\nWINS !!!\n*  *  *  *  *'
                        
                        # erase the old win message and draw the new one
                        self.win_message_eraser.draw()
                        self.win_message.draw()


                        self.switch_players()


                        # victory music

                        # fast fadeout of the current game's music
                        # music.fadeout(100)

                        # loading of the victory music
                        # fileDir = os.path.dirname(os.path.realpath('__file__'))
                        # print(fileDir)
                        # filename = os.path.join(fileDir, 'src/projet/projet7/win.wav')       
                        # music.load(filename)
                        
                        # start the victory music
                        # music.play()
                        # sleep(3)

                        # loading of the game's music
                        # fileDir = os.path.dirname(os.path.realpath('__file__'))
                        # print(fileDir)
                        # filename = os.path.join(fileDir, 'src/projet/projet7/connect_4_audio.mp3')       
                        # music.load(filename)
                        
                        # start the game's music (-1 <=> infinite loop)
                        # music.play(-1)


                    # if the players are playing
                    elif not self.no_winner:

                        # we switch the players
                        self.switch_players()

                        # we erase the old status and draw the new one
                        self.status_eraser.draw()
                        self.status.draw()
                    
                    break
    
    
    def quit(self):
        """Quit the game, draw the final screen."""

        self.run = False
        
        # draw the background (it erases all the element displayed)
        dot(1500, 'deepskyblue')

        # end of the music, with a fadeout effect
        music.fadeout(2000)

        # write a last message
        goto(0, 50)
        write('Thanks for playing !', font=('Times', 40), align='center')
        
        # draw the name of the author
        self.author.draw()

        # display the final “CLOSE“ button
        self.bt_close.displayed = True
        self.bt_close.draw()
    

    def click(self, x, y):
        """Reacts to mouse clicks."""

        # if the players are playing
        if self.run:

            # the player clicks on the grid
            if self.grid.inside(x, y) and self.playing:
                i = self.grid.get_column(x, y)
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
        

        # players no longer play => we are at the final screen
        else:

            # the player clicks on the “CLOSE“ button
            if self.bt_close.inside((x, y)):
                quit()
        

    def draw(self):
        """Draws all the game objects."""

        # draw the grid, the title, the author's name and the column's name
        self.grid.draw()
        self.title.draw()
        self.author.draw()

        # we erase the current status
        self.status_eraser.draw()


        # if the players are playing
        if self.playing:

            # writing of the game's status
            self.status.draw()
        

        # players no longer play => we are at the final screen
        else:

            # writing of the player's scores
            self.scores.draw()

        # runs through all the buttons
        for button in [self.bt_undo, self.bt_new, self.bt_reset_scores, self.bt_quit]:
            
            # if the button have to be displayed
            if button.displayed:

                # drawing of the button
                button.draw()


game = Game()

done()

```
