from difflib import restore
from platform import win32_is_iot
from turtle import *


'''
Summary :
    - some variables :          line ...
    - drawing functions :       line ...
    - some useful functions :   line ...
    - check win functions :     line ...
    - history functions :       line ...
    - time functions :          line ...
    - interactive functions :   line ...
    - classes :                 line ...
    - game code :               line ...
'''


# ================================================== #
''' some variables '''
# ================================================== #

# sizes
screen_size = 804
step = screen_size // 12   # distance between 2 cells
board_width = 6 * step
board_height = 5 * step

# colors
bg_color = 'deepskyblue'
board_color = 'navy'
player_1_color = 'red'
player_2_color = 'yellow'
selecting_color = 'lime'
winning_color = 'lime'
button_selecting_color = 'lime'
button_color = 'mediumslateblue'
playing_color = 'fuchsia'

# others variables
text_font = 'Times'

# history list
history = []

# dictionary for conversion from a number to a color
cell_state = {0:bg_color, 1:player_1_color, 2:player_2_color,3:selecting_color}


# ================================================== #
''' drawing functions '''
# ================================================== #

def initialization():
    # initialization of the window and  the turtle
    setup(screen_size, screen_size)
    hideturtle()
    penup()
    tracer(0)
    dot(100000, bg_color)

    goto(convert(3, 5.5))
    write('Puissance 4', align='center', font=(text_font, 100, 'italic'))
    goto(convert(3, 4))
    write('by Emilien Barde', align='center', font=(text_font, 50, 'italic'))


def board_initialization():
    # this function initializes the turtle state, draw the background,
    # write some text on the screen and draw the dark blue part of the board

    # a dot is used to make the background
    dot(5000, bg_color)

    # some texts are written
    goto(convert(3, 7.6))
    write('Puissance 4', align='center', font=(text_font, 50, 'italic'))
    goto(convert(3, 7.2))
    write('Emilien Barde', align='center', font=(text_font, 20, 'italic'))

    # initialization of the turtle
    goto(convert(0, 7))
    pencolor('black')
    fillcolor(board_color)
    pensize(5)
    pendown()
    begin_fill()

    # drawing of the dark blue part of the board
    for distance in [board_width, board_height] * 2:
        forward(distance)
        circle(-step, 90)
    end_fill()
    penup()


def draw_cell(cell_type, size = screen_size // 14):
    # this function draw the cells
    # they can be free cells, selected cells, or cell fulled by a token
    dot(size, 'black')

    # the color depend on the cell type
    # the conversion (from a number to a color) is done using a dictionary 
    dot(size * 4 // 5, cell_state[cell_type])

    # only for the selected cells (we can see the background in the middle)
    if cell_type == 3:
        dot(size // 2, bg_color)


def draw_win(winning_list, winning_player, size = screen_size // 13):
    for cell in range(4):
        dot_color = cell_state[winning_player]
        goto(convert(*winning_list[cell]))
        dot(size, winning_color)
        dot(size * 4 // 5, dot_color)

# ================================================== #
''' some useful functions '''
# ================================================== #

def action(self, selecting=False, confirmation=False):
    # this very important function will select a cell, un-select a cell,
    # or replace a cell with a token of the current player

    # the player has selected a non-full column
    if selecting and not self.full:
        # the lowest free cell will be selected
        for index in range(6):
            if self.cells[index] == 0:
                self.cells[index] = 3
                break
        self.selected = True

    # the player has selected a full column (he can't play here)
    elif selecting and self.full:
        self.selected = False
    
    # the player didn't select the column
    else:
        # the player want to confirm his last selection
        if confirmation:
            # the selected cell will be replace by a token
            for index in range(6):
                if self.cells[index] == 3:
                    # the token's color depend on the current player
                    game.current_player = 1 + (game.current_player % 2)
                    self.cells[index] = game.current_player
                    break
            # after the change, we check if the column is full or not
            # if there no more free cells (no more 0 in the cells), the column is full
            if 0 not in self.cells:
                self.full = True
        
        # the player has NOT clicked on the column
        else:
            # all the selected cells (there should be only one)
            # become an un-selected cell
            for index in range(6):
                if self.cells[index] == 3:
                    self.cells[index] = 0
        self.selected = False


def convert(x, y):
    # the input is the coordinate of a point on the board (not in pixels)
    # x should be between 0 and 6 ; y should be between 0 and 5
    reel_x = -screen_size // 4 + x * step
    reel_y = -screen_size // 4 + y * step

    # the output is the coordinate of a point in pixels
    return (reel_x, reel_y)


# ================================================== #
''' check win functions '''
# ================================================== #

def four_token(token_list):
    """test if there is at least 4 token
    test if the number of times the first element of the list appears is equal to the size of the list
    (the second test check if all elements of the list are equal to the first element of the list)
    """
    return len(token_list) >= 4 and token_list.count(token_list[0]) == len(token_list)


def check_win():
    win, winning_list, winning_player = check_columns()
    if not win:
        win, winning_list, winning_player = check_lines()
    if not win:
        win, winning_list, winning_player = check_diagonal_1()
    if not win:

        win, winning_list, winning_player = check_diagonal_2()

    return win, winning_list, winning_player


def check_columns():


    win = False



    print('check columns')
    # list of the winning's cells coordinate (between 0 and 6)
    winning_list = []

    # list of the winning's cells values (1 or 2)
    winning_cells = []

    # loop for the columns
    for column in range(7):
        # loop fot the column's cells
        print(f'\ttest column {column}')

        for cell in range(6):
            win, winning_list, winning_cells = test(column, cell, winning_list, winning_cells)
            if win:
                break
        if win:
            break
        else:
            winning_cells.clear()
            winning_list.clear()
    if len(winning_cells) == 0:
        winning_cells.append(0)
    return win, winning_list, winning_cells[0]


def check_lines():
    win = False

    print('check lines')
    # list of the winning's cells coordinate (between 0 and 6)
    winning_list = []

    # list of the winning's cells values (1 or 2)
    winning_cells = []

    # loop for the lines
    for line in range(6):
        print(f'\ttest line {line}')
        # loop fot the columns
        for column in range(7):
            win, winning_list, winning_cells = test(column, line, winning_list, winning_cells)
            if win:
                break
        if win:
            break
        else:
            winning_cells.clear()
            winning_list.clear()
    if len(winning_cells) == 0:
        winning_cells.append(0)
    return win, winning_list, winning_cells[0]


def check_diagonal_1():
    win = False

    print('check lines')
    # list of the winning's cells coordinate (between 0 and 6)
    winning_list = []

    # list of the winning's cells values (1 or 2)
    winning_cells = []

    # loop for the diagonal
    for diagonal in range(12):
        col_num = max(0, diagonal - 5)
        line_no = min(diagonal + 1, 7)
        print(f'\t\t\t\ton check :')
        for i in range(col_num, line_no):
            print(f'\t\t\t\t\t{i}, {diagonal - i}')
            # coordinate = convert(i, diagonal - i + 1)
            win, winning_list, winning_cells = test(i, diagonal - i, winning_list, winning_cells)
            if win:
                break
        if win:
            break
        else:
            winning_cells.clear()
            winning_list.clear()
    if len(winning_cells) == 0:
        winning_cells.append(0)
    return win, winning_list, winning_cells[0]


def check_diagonal_2():
    win = False

    print('check lines')
    # list of the winning's cells coordinate (between 0 and 6)
    winning_list = []

    # list of the winning's cells values (1 or 2)
    winning_cells = []

    # loop for the diagonal
    for diagonal in range(12):
        col_num = max(0, 6 - diagonal)
        line_no = min(12 - diagonal, 7)
        print(f'\t\t\t\ton check :')
        for i in range(col_num, line_no):
            print(f'\t\t\t\t\t{i}, {diagonal + i - 6}')
            # coordinate = convert(i, diagonal - i + 1)
            win, winning_list, winning_cells = test(i, diagonal + i - 6, winning_list, winning_cells)
            if win:
                break
        if win:
            break
        else:
            winning_cells.clear()
            winning_list.clear()
    if len(winning_cells) == 0:
        winning_cells.append(0)
    return win, winning_list, winning_cells[0]


def test(cell_column, cell_line, winning_list, winning_cells):
    win = False

    # new variable to simplify the comprehension
    cell_test = columns[cell_column].cells[cell_line]
    
    # check if the cell_test is fulled with a token (the cell_test should NOT be equal to 0 or 3)
    if cell_test != 0 and cell_test != 3:

        # the coordinate of the cell is added to the winning list
        winning_list.append((cell_column, cell_line + 1))

        # the value (1 or 2) of the cell is added to the winning cells's list
        winning_cells.append(cell_test)
        
        print('\t\t\t', winning_cells)

        # this loop remove the first element of the list,
        # only if all the elements on the list are not equals
        while winning_cells.count(cell_test) != len(winning_cells):
            winning_cells.pop(0)
            winning_list.pop(0)
        
        # check if there is four equal token on the list
        win = four_token(winning_cells)

    return win, winning_list, winning_cells




# ================================================== #
''' history functions '''
# ================================================== #

def save_game():
    
    # for move in range(len(history)):
    #     print(f'\tmove {move} :')
    #     for column in range(len(history[move])):
    #         print(f'\t\tcolumn {column} : {history[move][column]}')
    
    current_columns = []
    for column in columns:
        current_columns.append(list(column.cells))
    history.append(current_columns)
    print('game saved !')


def restore_last_move():

    last_columns = history[-2]
    history.pop()
    
    # change the values of the columns's cells
    for one_column in range(7):
        columns[one_column].cells = list(last_columns[one_column])
        columns[one_column].draw()
    
    game.current_player = 1 + (game.current_player % 2)

    for player in (player_1, player_2):
        player.is_playing = not player.is_playing
        player.draw_name()


# ================================================== #
''' time functions '''
# ================================================== #


# ================================================== #
''' interactive functions '''
# ================================================== #

def f(x, y):
    # this function is called when the player click on the screen
    if game.playing:
        if undo_button.inside(x, y) and undo_button.displayed == True:
            print('Undo !')
            restore_last_move()
            print(len(history))
            if len(history) < 2:
                undo_button.delete_button()
                undo_button.displayed = False
        else:
            # every column check if there is some changes to make
            for column_number in range(7):
                # the column make the necessary changes
                columns[column_number].click(x, y)

                # the column is drawn
                columns[column_number].draw()
        

def confirmation():
    # this function is called when the player press the space bar

    # every column check if ther is some changes to make
    for column_number in range(7):
        # the column make the necessary changes
        columns[column_number].confirmation()

        # the column is drawn
        columns[column_number].draw()
    
    win, winning_list, winning_player = check_win()
    print(f'winning list : {winning_list}')
    if win:
        undo_button.delete_button()
        undo_button.displayed = False
        
        draw_win(winning_list, winning_player)
        game.playing = False
        game.winning = True
        game.draw_win()
    else:
        for player in (player_1, player_2):
            player.is_playing = not player.is_playing
            player.draw_name()
    save_game()

    if len(history) > 1 and game.playing:
        undo_button.displayed = True
        undo_button.draw()
    
    
# ================================================== #
''' Classes '''
# ================================================== #

class Column:
    def __init__(self, column_num):
        # values in pixels
        self.x0 = (column_num - 3) * step - step // 2
        self.x1 = (column_num - 3) * step + step // 2
        self.y0 = -2 * step - step // 2
        self.y1 = 3 * step + step // 2

        self.num = column_num   # value between 0 and 6
        self.free_cell = 0   # index of the lowest free cell
        self.selected = False
        self.full = False

        self.cells = [0 for i in range(6)]   # list of all the cell's state
    

    def click(self, x, y):
        # the player has clicked on the column
        if self.x0 < x < self.x1 and self.y0 < y < self.y1:
            self.selected = not self.selected
        
        # the player has NOT clicked on the column
        else:
            self.selected = False
        
        # this function will select (or un-select) the lowest free cell of the column
        action(self, selecting=self.selected)


    def draw(self):
        if game.playing:
            # this function draw the cells of the column one by one
            # from the lowest cell to the highest
            goto(convert(self.num, 1))
            for cell_index in range(6):
                draw_cell(self.cells[cell_index])
                goto(xcor(), ycor() + step)
    

    def confirmation(self):
        # this function call an other function if the column is selected
        if self.selected:
            # this action will repace the selected cell with a token
            action(self, confirmation=True)


class Button:
    def __init__(self, text, pos=(0, 0), size=(100, 60), displayed=False, selectable=True, 
    col=button_color, selecting_col=button_selecting_color):
        self.text = text
        self.pos = pos   # the center of the button
        self.size = size
        self.col = col
        self.selecting_col = selecting_col
        
        # boolean variables
        self.selected = False
        self.selectable = selectable
        self.displayed = displayed

        self.draw()
    

    def draw(self, deleting_button=False):
        # if the button should be displayed
        if self.displayed:
            # 1) button (without text)
            # initialization of the turtle
            goto(self.pos[0] - self.size[0] // 2, self.pos[1] - self.size[1] // 2)
            if deleting_button:
                color(bg_color)
            else:
                fillcolor(self.col)
                pencolor(self.selecting_color if self.selected else 'black')
            pensize(5)
            down()
            begin_fill()

            # drawing of the button (without text)
            for a in self.size * 2:
                forward(a)
                left(90)
            
            end_fill()
            up()

            # 2) text
            goto(self.pos[0], self.pos[1] - self.size[1] // 4)
            write(self.text, font=('Times', self.size[1] // 2, 'normal'), align='center')
    

    def inside(self, x, y):
        a = self.pos[0] - self.size[0] // 2 < x < self.pos[0] + self.size[0] // 2
        b = self.pos[1] - self.size[1] // 2 < y < self.pos[1] + self.size[1] // 2
        return a and b
    
    def delete_button(self):
        self.draw(deleting_button=True)


class Game:
    def __init__(self):
        self.starting = True
        self.choosing_parameters = False
        self.playing = False
        self.winning = False
        self.end = False
        self.current_player = 0
        self.players_names = ['Emilien', 'Bot']
    
    def click(self, x, y):
        if self.starting == True:
            if start_button.inside(x, y):
                # first drawing of the game (without the free cells)
                board_initialization()
                self.starting = False
                self.playing = True
                save_game()
                undo_button.displayed = True

                for i in range(7):
                    columns[i].draw()
                
                player_1.is_playing = True
                for player in (player_1, player_2):
                    player.draw_name()
            
        elif self.playing == True:
            f(x, y)
        
        elif self.winning == True:
            self.draw_win()

    def draw_win(self):
        print('write on the screen !!')
        goto(convert(3, -2))
        color('black')
        write(f'WIN !!!', font=(text_font, 60, 'normal'), align='center')


class Player():
    def __init__(self, num, name='no name', is_playing=False):
        self.num = num
        self.name = name
        self.color = player_1_color if num == 1 else player_2_color
        self.time = 0
        self.is_playing = is_playing
    
    def draw_name(self):
        goto(convert(-1, -1) if self.num == 1 else convert(7, -1))
        color(playing_color if self.is_playing else 'black')
        write(self.name, align='center', font=(text_font, 40, 'normal'))

# ================================================== #
''' game code '''
# ================================================== #

initialization()

game = Game()

player_1 = Player(1)
player_2 = Player(2)

start_button = Button('Start', pos=(0, -100), size=(200, 80) , displayed=True)
undo_button = Button('Undo', pos=(0, -250))

# creation of a list containing the 7 columns of the board
columns = [Column(i) for i in range(7)]

s = getscreen()


s.onclick(game.click)
s.onkey(confirmation, 'space')
s.listen()

done()