#2048
from turtle import *
from random import choice
from time import sleep
from pygame import mixer
setup(600, 400)
hideturtle()
tracer(0)
up()

state = [
[0, 0, 0, 0],
[0, 0, 0, 0],
[0, 0, 0, 0],
[0, 0, 0, 0],
]

correspondance = {
(0, 0): (-170.0, 190.0), (0, 1): (-82.5, 190.0), (0, 2): (5.0, 190.0), (0, 3): (92.5, 190.0),
(1, 0): (-170.0, 102.5), (1, 1): (-82.5, 102.5), (1, 2): (5.0, 102.5), (1, 3): (92.5, 102.5),
(2, 0): (-170.0, 15.0), (2, 1): (-82.5, 15.0), (2, 2): (5.0, 15.0), (2, 3): (92.5, 15.0),
(3, 0): (-170.0, -72.5), (3, 1): (-82.5, -72.5), (3, 2): (5.0, -72.5), (3, 3): (92.5, -72.5)
}

correspondance_inverse = {value: key for key, value in correspondance.items()}
hist = []
retour_hist = []
pause, modifi , nbr, score, endjeu, not_op = 0, 0, 0, 0, 1, 0
color_num = {-1 : 'grey', 0 : 'darkgrey', 2 : 'whitesmoke', 4 : 'MistyRose' , 8 : 'plum1', 16 : 'orchid2', 32 : 'magenta',
             64 : 'magenta3', 128 : 'DeepPink', 256 : 'MediumVioletRed', 512 : 'VioletRed1', 1024 : 'LightSeaGreen',
             2048 : 'turquoise1'}

addshape('bois.gif')
shape('bois.gif')


# Ce modèle sert à créer les cases qui se calqueront sur les cases, de la fonction cases(), avec leur chiffre et couleur
class Case:
    def __init__(self, pos, text, size = 77.5):
        self.pos = pos
        self.size = size
        self.text = text
        self.draw()
       
    # cette fonction permet de déssiner la case avec sa couleur et son chiffre   
    def draw(self):
        up()
        x, y = self.pos
        goto(x, y)
        global color_num
        couleur = color_num[self.text]
        color(couleur)
        begin_fill()
        for i in range(4):
            forward(self.size)
            right(90)
        end_fill()
        if self.text != 0 and self.text != -1:
            goto(x + self.size /2, y - self.size /2 - 10)
            color('black')
            write(self.text, font=('Arial', 20), align='center')
            
    def __str__(self):
        return f'Case({self.pos}, {self.text})'


# Ce modèle crée des boutons
class Button:
    def __init__(self, pos, text, size, color= 'Lightgrey'):
        # hello
        self.pos = pos
        self.size = size
        self.text = text
        self.color = color
        self.draw()
    
    # cette fonction permet de dessiner le bouton
    def draw(self):
        goto(self.pos)
        fillcolor(self.color)
        begin_fill()
        for x in self.size * 2:
            forward(x)
            left(90)
        end_fill()
        x, y = self.pos
        w, h = self.size
        goto(x+w/2, y+h/4 - 1)
        color('black')
        write(self.text, font=('Arial', h//2), align='center')

    def __str__(self):
        return f'Button({self.pos}, {self.text})'

    # cette fonction permet de calculer si la position donnée est à l'intérieur du bouton
    def inside(self, p):
        x, y = self.pos
        w, h = self.size
        return 0 < p[0]-x < w and 0 < p[1]-y < h
   

# cette fonction permet de créer le tour et les 16 cases vides du début du jeu 
def cases():
    tour = Case((-180, 200), -1, 360)
    for y in 190, 102.5, 15, -72.5:
        for x in -170, -82.5, 5, 92.5:
            case_begin = Case((x, y), 0)


# cette fonction sert à écrire un citation lors d'un échec
def citation():
    goto(0, -110)
    write('''“L'échec fait partie intégrante de notre réussite. L'échec, c'est l'envers de la réussite."\nJean-Pierre Chevènement''',
          font=('Didot', 10), align='center')


# cette fonction permet de tout effacer en remettant l'arrière plan et de poser les boutons choisit en fonction des paramètres de la fonction
def reboutons(rage, hist = 1, back = 0):
    goto(0, 0)
    stamp()
    if rage:
        button_end = Button((210, 125), 'Rage', (60, 30))
    else:
        if hist:
            button_hist = Button((210, -135), 'hist', (60, 30))
    button_new = Button((210, -5), 'New', (60, 30))
    if back:
        button_back = Button((210, 60), 'Back', (60, 30))
    button_quit = Button((210, -70), 'Quit', (60, 30))


# cette fonction permet de lancer le son de fin. "win.wav" si c'est une réussite sinon "cri.wav"
def song(win):
    mixer.music.stop()
    if win:
        mixer.music.load('win.mp3')
        mixer.music.play()
        sleep(6)
    else:
        mixer.music.load('cri.wav')
        mixer.music.play()
        sleep(1)
    mixer.music.load('Sojiada-Lanmou.mp3')
    mixer.music.play(-1)

# cette fonction sert à écrire l'historique sous formes de flèches
def end_hist():
    global hist
    goto(0, 180)
    color('white')
    write('historique:', font=('Arial', 12), align='center')
    if len(hist) != 0:
        partie = []
        writehist = []
        for i in range(len(hist)):
            partie.append(hist[i])
            if i != 0:
                if i % 20 == 0:
                    writehist.append(partie)
                    partie = []
        if len(partie) != 0:
            writehist.append(partie)
        for part in writehist:
            part_str = ' | '.join(part)
            goto(0, ycor() - 25)
            write(part_str, font=('Arial', 12), align='center')
    color('black')


# cette fonction permet de créer la page de fin
def end(text, win):
    global endjeu
    endjeu = 1
    reboutons(0)
    color('white')
    goto(0, 0)
    write(text, font=('Arial', 40), align='center')
    if not win: 
        citation()
    else:
        goto(0, 200)
        write('👍     ╰*°▽°*╯     👍', font=('Arial', 50), align='center')
    color('black')
    song(win)
        

# cette fonction calcul le nombre maximum sur le plateau et le score. Il les écrit au bas du plateau
def resultat():
    global score
    global state
    goto(-170, -175)
    width(20)
    down()
    color('white')
    goto(170, -175)
    up()
    width(5)
    color('black')
    goto(0, -185)
    nbrmax = 0
    for y in state:
        if max(y) > nbrmax:
            nbrmax = max(y)
    write('score: ' + str(score) + 20 * ' ' + 'max: ' + str(nbrmax), font=('Arial', 13), align='center')
    if nbrmax == 2048:
        sleep(1)
        end('2048 c\'est la win! :)', 1)



# cette fonction prend les coordonnées de la case et retourn la valeur de celle-ci
def coord_to_res(xcoord, ycoord):
    global correspondance_inverse
    yres, xres = correspondance_inverse[(xcoord, ycoord)]
    global state
    return state[yres][xres]     


# cette fonction remet le jeu comme c'était le tour d'avant et supprime la sauvegarde du dernier coup
def retour():
    global retour_hist
    retour_hist.pop()
    global state
    global correspondance
    for res in correspondance:
        yres, xres = res
        xcoord, ycoord = correspondance[res]
        state[yres][xres] = retour_hist[-1][yres][xres]
        caseback = Case((xcoord, ycoord), state[yres][xres])
    global hist
    hist.pop()
    global score
    score -= 2
    global nbr
    nbr -= 1
    resultat()
    

# cette fonction permet de mémoriser la position de chaque case
def retour_calcul():
    global retour_hist
    global state
    retour_hist.append(state)


# cette fonction permet de mémoriser les coups à l'aide d'une flèche ajoutée à l'historique
def historique(direction):
    global hist
    if direction == 'h':
        hist.append('↑')
    elif direction == 'b':
        hist.append('↓')
    elif direction == 'd':
        hist.append('→')
    elif direction == 'g':
        hist.append('←')
 

#  cette fonction permet de créer une nouvelle case après un coup
def new(newretour = 0):
    global nbr
    listexy = (0, 1, 2, 3)
    xres = choice(listexy)
    yres = choice(listexy)
    global state
    global correspondance
    if nbr == 16:
        end('Game Over', 0)
    elif state[yres][xres] == 0:
        case2 = Case(correspondance[(yres, xres)], 2)
        state[yres][xres] = 2
        nbr += 1
        global pause
        pause = 1
        global score
        score += 2
        if newretour:
            retour_calcul()
    else:
        new()


# cette fonction fait le changement de case     
def changement(xpos, ypos, xsuiv, ysuiv):
    if (xpos, ypos) != (xsuiv, ysuiv):
        if coord_to_res(xsuiv, ysuiv) == 0:
            nbrsuiv = coord_to_res(xpos, ypos)
        else:
            nbrsuiv = coord_to_res(xpos, ypos) * 2
        global correspondance_inverse
        global state
        casei = Case((xsuiv, ysuiv), nbrsuiv)
        ysuivres, xsuivres = correspondance_inverse[(xsuiv, ysuiv)]
        state[ysuivres][xsuivres] = nbrsuiv
        case0 = Case((xpos, ypos), 0)
        yposres, xposres = correspondance_inverse[(xpos, ypos)]
        state[yposres][xposres] = 0
        global nbr
        nbr -= 1
        global modifi
        modifi = 1
    

# cette fonction calcule les coordonnées de la case suivante en fonction de la direction 
def operation(coord, direction):
    global correspondance_inverse
    xcoord, ycoord = coord
    coord_memoire = coord
    if direction == 'h':
        ycoord += 87.5
    elif direction == 'b':
        ycoord -= 87.5
    elif direction == 'd':
        xcoord += 87.5
    elif direction == 'g':
        xcoord -= 87.5
    if (xcoord, ycoord) not in correspondance_inverse:
        global not_op
        not_op = 1
        xcoord, ycoord = coord_memoire
    return xcoord, ycoord
        
# cette fonction permet de calculer les coordonnées de la case présedente
# elle est utilisé si la case suivante est une bordure ou une case d'un autre chiffre
def operation_inverse(coord, direction):
    global correspondance_inverse
    xcoord, ycoord = coord
    if direction == 'h':
        ycoord -= 87.5
    elif direction == 'b':
        ycoord += 87.5
    elif direction == 'd':
        xcoord -= 87.5
    elif direction == 'g':
        xcoord += 87.5
    return xcoord, ycoord


# cette fonction calcule si un changement peut être effectué même si le chiffre de la case suivante n'est pas le même
def notsame(xpos, ypos, xsuiv, ysuiv, direction):
    global not_op
    while True:
        if coord_to_res(xsuiv, ysuiv) == 0:
            xsuiv, ysuiv = operation((xsuiv, ysuiv), direction)
            if not_op:
                not_op = 0
                changement(xpos, ypos, xsuiv, ysuiv)
                break
        elif coord_to_res(xpos, ypos) == coord_to_res(xsuiv, ysuiv):
            changement(xpos, ypos, xsuiv, ysuiv)
            break
        elif coord_to_res(xpos, ypos) != coord_to_res(xsuiv, ysuiv):
            xsuiv, ysuiv = operation_inverse((xsuiv, ysuiv), direction)
            changement(xpos, ypos, xsuiv, ysuiv)
            break
    

# cette fonction calcule si le chiffre dans la case est le même que le suivant    
def calcul(pos, direction):
    global not_op
    xsuiv, ysuiv = operation(pos, direction)
    if not not_op:
        xpos, ypos = pos
        if coord_to_res(xpos, ypos) == coord_to_res(xsuiv, ysuiv):
            changement(xpos, ypos, xsuiv, ysuiv)
        else:
            notsame(xpos, ypos, xsuiv, ysuiv, direction)
    else:
        not_op = 0
                

# cette fonction, si le jeu n'est pas fini, lance les calculs des changements possible de cases
# Si, après les calculs, il n'y a eu aucune modification dans le jeu, le coup est considéré comme sans intéret et le joueur peut rejouer 
def mouvement(direction):
    global endjeu
    if endjeu:
        global modifi
        modifi = 0
        global state
        global correspondance_inverse
        for i in range(4):
            for coord in correspondance_inverse:
                xcoord, ycoord = coord
                if coord_to_res(xcoord, ycoord) != 0:
                    calcul(coord, direction)
        if modifi == 1:         
            new()
            resultat()
        else:
            global pause
            pause = 1
        historique(direction)
        retour_calcul()


# cette fonction, si l'ordinateur n'est pas encore en calcul dù au dernier coup, lance la fonction mouvement() avec comme variable la direction donnée   
def haut():
    global pause
    if pause:
        pause = 0
        mouvement('h')
        

# cette fonction, si l'ordinateur n'est pas encore en calcul dù au dernier coup, lance la fonction mouvement() avec comme variable la direction donnée    
def bas():
    global pause
    if pause:
        pause = 0
        mouvement('b')


# cette fonction, si l'ordinateur n'est pas encore en calcul dù au dernier coup, lance la fonction mouvement() avec comme variable la direction donnée
def gauche():
    global pause
    if pause:
        pause = 0
        mouvement('g')


# cette fonction, si l'ordinateur n'est pas encore en calcul dù au dernier coup, lance la fonction mouvement() avec comme variable la direction donnée
def droite():
    global pause
    if pause:
        pause = 0
        mouvement('d')
        

# cette fonction lance le son de fond
def son_fond():
    mixer.init()
    mixer.music.load('Meydn-SynthwaveVibe.mp3')
    mixer.music.play(-1)


# cette fonction déssine le cadre du jeu et lance le son de fond
def main():
    goto(0, 0)
    stamp()
    cases()
    new(1)
    son_fond()
    resultat()
    

# cette fonction rement des variables comment ils étaient au début
def rezero():
    global pause
    global modifi
    global nbr
    global score
    global endjeu
    pause, modifi , nbr, score, endjeu = 0, 0, 0, 0, 1
    

# cette fonction remet les variables comment ils étaient au début et redessine le jeu   
def newgame():
    global hist
    global state
    state = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    ]
    rezero()
    hist = []
    reboutons(1, 1, 1)
    cases()
    new(1)
    resultat()
    son_fond()
    

# cette fonction permet de savoir si le joueur à cliquer dans un boutons et, si oui, lance la fonction de ce dernier    
def f(x, y):
    if pause == 1:
        if button_end.inside((x, y)):
            end('Tant Pis :(', 0)
        if button_new.inside((x, y)):
            newgame()
        if button_back.inside((x, y)):
            global hist
            if len(hist) != 0:
                retour()
    if button_hist.inside((x, y)):
        reboutons(0, 0)
        end_hist()
    if button_quit.inside((x, y)):
        mixer.quit()
        bye()


button_hist = Button((210, -135), 'hist', (60, 30))
main()
button_end = Button((210, 125), 'Rage', (60, 30))
button_new = Button((210, -5), 'New', (60, 30))
button_back = Button((210, 60), 'Back', (60, 30))
button_quit = Button((210, -70), 'Quit', (60, 30))
s = getscreen()
s.onkey(haut, 'Up')
s.onkey(bas, 'Down')
s.onkey(gauche, 'Left')
s.onkey(droite, 'Right')
s.onkey(retour,'BackSpace')
s.onclick(f)
s.listen()
done()

#class Game:


# perdre
# new 1x sur 2 un 4
# win trop de reboutons
# show nbrmax
# quit when win?????
# sup nbr avec retour_hist
# back
# 2 + 2 + 4 = 4 + 4
#score
