#2048
from turtle import *
from random import choice
from time import sleep
from pygame import mixer
setup(920, 850)
case_num = {(-290, 290): 0, (-140, 290) : 0, (10, 290) : 0, (160, 290) : 0, (-290, 140) : 0, (-140, 140) : 0,
            (10, 140) : 0, (160, 140) : 0, (-290, -10) : 0, (-140, -10) : 0, (10, -10) : 0, (160, -10) : 0,
            (-290, -160) : 0, (10, -160) : 0, (160, -160) : 0, (-140, -160) : 0, (310, 290): 'stop', (310, 140): 'stop',
            (310, -10): 'stop', (310, -160): 'stop', (-440, 290): 'stop',(-440, 140): 'stop', (-440, -10): 'stop',
            (-440, -160): 'stop', (-290, 440): 'stop', (-140, 440): 'stop',(10, 440): 'stop', (160, 440): 'stop',
            (-290, -310): 'stop', (-140, -310): 'stop', (10, -310): 'stop', (160, -310): 'stop'}
hist = []
retour_hist = []
pause, modifi , nbr, score, endjeu = 0, 0, 0, 0, 1
color_num = {0 : 'darkgrey', 2 : 'whitesmoke', 4 : 'MistyRose' , 8 : 'plum1', 16 : 'orchid2', 32 : 'magenta',
             64 : 'magenta3', 128 : 'DeepPink', 256 : 'MediumVioletRed', 512 : 'VioletRed1', 1024 : 'LightSeaGreen',
             2048 : 'turquoise1'}
speed(0)
addshape('bois.gif')
shape('bois.gif')
hideturtle()
up()
#show nbrmax


# cette fonction permet de dessiner le cadre du jeu 
def tour():
    color('grey')
    goto(-300, -310)
    begin_fill()
    for pos in (310, -310), (310, 300), (-300, 300):
        goto(pos)
    end_fill()
   

# cette fonction permet de créer les 16 cases vides du début du jeu   
def cases():
    color('darkgrey')
    for y in 290, 140, -10, -160:
        goto(-290, y)
        for i in range(4):
            begin_fill()
            for i in range(4):
                forward(140)
                right(90)
            end_fill()
            forward(150)


# Ce modèle sert à créer les cases qui se calqueront sur les cases, de la fonction cases(), avec leur chiffre et couleur
class Case:
    def __init__(self, pos, text, size=(80, 60)):
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
            forward(140)
            right(90)
        end_fill()
        if self.text != 0:
            goto(x + 70, y - 90)
            w, h = self.size
            color('black')
            write(self.text, font=('Arial', h//2), align='center')
            
    def __str__(self):
        return f'Case({self.pos}, {self.text})'


# Ce modèle crée des boutons
class Button:
    def __init__(self, pos, text, size, color= 'Lightgrey'):
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


# cette fonction sert à écrire un citation lors d'un échec
def citation():
    goto(0, -100)
    write('''“L'échec fait partie intégrante de notre réussite. L'échec, c'est l'envers de la réussite."\nJean-Pierre Chevènement''',
          font=('Didot', 12), align='center')


# cette fonction permet de tout effacer en remettant l'arrière plan et de poser les boutons choisit en fonction des paramètres de la fonction
def reboutons(rage, hist = 1, back = 0):
    goto(0, 0)
    stamp()
    if rage:
        Button_end = Button((350, 100), 'Rage', (80, 30))
    else:
        if hist:
            Button_hist = Button((350, -300), 'hist', (80, 30))
    Button_new = Button((350, -100), 'New', (80, 30))
    if back:
        Button_back = Button((350, 0), 'Back', (80, 30))
    Button_quit = Button((350, -200), 'Quit', (80, 30))


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
    goto(0, 300)
    color('white')
    write('historique:', font=('Arial', 12), align='center')
    if len(hist) != 0:
        partie = []
        writehist = []
        for i in range(len(hist)):
            partie.append(hist[i])
            if i != 0:
                if i % 25 == 0:
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
def résultat():
    global score
    global case_num
    goto(-300, -350)
    width(40)
    down()
    color('white')
    goto(310, -350)
    up()
    width(5)
    color('black')
    goto(0, -363)
    nbrmax1 = []
    for nbr in case_num:
        if case_num[nbr] != 'stop':
            nbrmax1.append(case_num[nbr])
    nbrmax = max(nbrmax1)
    write('score: ' + str(score) + 20 * ' ' + 'max: ' + str(nbrmax), font=('Arial', 25), align='center')
    if nbrmax == 2048:
        sleep(1)
        end('2048 c\'est la win! :)', 1)


# cette fonction remet le jeu comme c'était le tour d'avant et supprime la sauvegarde du dernier coup
def retour():
    global retour_hist
    retour_hist.pop()
    rh = retour_hist[-1]
    n = 0
    global case_num
    for case in case_num:
        if case_num[case] != 'stop':
            case_num[case] = rh[n]
            n += 1
            Caseback = Case(case, case_num[case])
    global hist
    hist.pop()
    global score
    score -= 2
    global nbr
    nbr -= 1
    résultat()
    

# cette fonction permet de mémoriser la position de chaque cases
def retour_calcul():
    global retour_hist
    global case_num
    rappel = []
    for case in case_num:
        if case_num[case] != 'stop':
            rappel.append(case_num[case])
    retour_hist.append(rappel)


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
    sleep(0.2)
    global nbr
    listey = (290, 140, -10, -160)
    listex = (160, 10, -140, -290)
    x = choice(listex)
    y = choice(listey)
    global case_num
    if nbr == 16:
        end('Game Over', 0)
    elif case_num[(x, y)] == 0:
        Case2 = Case((x, y), 2)
        case_num[(x, y)] = 2
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
def changement(pos, suiv):
    global case_num
    if pos != suiv:
        if case_num[suiv] == 0:
            nbrsuiv = case_num[pos]
        else:
            nbrsuiv = case_num[pos] * 2
        Casei = Case(suiv, nbrsuiv)
        case_num[suiv] = nbrsuiv
        Case0 = Case(pos, 0)
        case_num[pos] = 0
        global nbr
        nbr -= 1
        global modifi
        modifi = 1
    

# cette fonction calcule les coordonnées de la case suivante en fonction de la direction 
def opération(x, y, direction):
    if direction == 'h':
        return x, y + 150
    elif direction == 'b':
        return x, y - 150
    elif direction == 'd':
        return x + 150, y
    elif direction == 'g':
        return x - 150, y
    

# cette fonction permet de calculer les coordonnées de la case présedente
# elle est utilisé si la case suivante est une bordure ou une case d'un autre chiffre
def opération_inverse(x, y, direction):
    if direction == 'h':
        return x, y - 150
    elif direction == 'b':
        return x, y + 150
    elif direction == 'd':
        return x - 150, y
    elif direction == 'g':
        return x + 150, y


# cette fonction calcule si un changement peut être effectué même si le chiffre de la case suivante n'est pas le même
def notsame(pos, direction, suiv):
    global case_num
    fusible = 0
    while True:
        if case_num[suiv] == 0:
            x, y = suiv
            suiv = opération(x, y, direction)
            fusible += 1
            if fusible > 5:
                break
#! bloquage du curseur sans raisons -> à résoudre
        elif case_num[suiv] == 'stop':
            x, y = suiv
            suiv = opération_inverse(x, y, direction)
            changement(pos, suiv)
            break
        elif case_num[pos] == case_num[suiv]:
            changement(pos, suiv)
            break
        elif case_num[pos] != case_num[suiv]:
            x, y = suiv
            suiv = opération_inverse(x, y, direction)
            changement(pos, suiv)
    

# cette fonction calcule si le chiffre dans la case est le même que le suivant    
def calcul(pos, direction):
    global case_num
    x, y = pos
    suiv = opération(x, y, direction)
    if suiv in case_num:
        if case_num[suiv] == case_num[pos]:
            changement(pos, suiv)
        else:
            notsame(pos, direction, suiv)
                

# cette fonction, si le jeu n'est pas fini, lance les calculs des changements possible de cases
# Si, après les calculs, il n'y a eu aucune modification dans le jeu, le coup est considéré comme sans intéret et le joueur peut rejouer 
def mouvement(direction):
    global endjeu
    if endjeu:
        global modifi
        modifi = 0
        global case_num
        for i in range(4):
            for pos in case_num:
                if case_num[pos] != 0 and case_num[pos] != 'stop':
                    calcul(pos, direction)
        if modifi == 1:         
            new()
            résultat()
        else:
            global pause
            pause = 1
        historique(direction)
        retour_calcul()
   

# cette fonction, si l'ordinateur n'est pas encore en calcul dù au dernier coup, lance la fonction mouvement() avec comme variable la direction donnée   
def haut():
    global pause
    if pause == 1:
        pause = 0
        mouvement('h')
        

# cette fonction, si l'ordinateur n'est pas encore en calcul dù au dernier coup, lance la fonction mouvement() avec comme variable la direction donnée    
def bas():
    global pause
    if pause == 1:
        pause = 0
        mouvement('b')


# cette fonction, si l'ordinateur n'est pas encore en calcul dù au dernier coup, lance la fonction mouvement() avec comme variable la direction donnée
def gauche():
    global pause
    if pause == 1:
        pause = 0
        mouvement('g')


# cette fonction, si l'ordinateur n'est pas encore en calcul dù au dernier coup, lance la fonction mouvement() avec comme variable la direction donnée
def droite():
    global pause
    if pause == 1:
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
    tour()
    cases()
    new(1)
    son_fond()
    résultat()
    

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
    global case_num
    case_num = {(-290, 290): 0, (-140, 290) : 0, (10, 290) : 0, (160, 290) : 0, (-290, 140) : 0, (-140, 140) : 0,
            (10, 140) : 0, (160, 140) : 0, (-290, -10) : 0, (-140, -10) : 0, (10, -10) : 0, (160, -10) : 0,
            (-290, -160) : 0, (10, -160) : 0, (160, -160) : 0, (-140, -160) : 0, (310, 290): 'stop', (310, 140): 'stop',
            (310, -10): 'stop', (310, -160): 'stop', (-440, 290): 'stop',(-440, 140): 'stop', (-440, -10): 'stop',
            (-440, -160): 'stop', (-290, 440): 'stop', (-140, 440): 'stop',(10, 440): 'stop', (160, 440): 'stop',
            (-290, -310): 'stop', (-140, -310): 'stop', (10, -310): 'stop', (160, -310): 'stop'}
    rezero()
    hist = []
    reboutons(1, 1, 1)
    tour()
    cases()
    new(1)
    résultat()
    son_fond()
    

# cette fonction permet de savoir si le joueur à cliquer dans un boutons et, si oui, lance la fonction de ce dernier    
def f(x, y):
    if pause == 1:
        if Button_end.inside((x, y)):
            end('Tant Pis :(', 0)
        if Button_new.inside((x, y)):
            newgame()
        if Button_back.inside((x, y)):
            global hist
            if len(hist) != 0:
                retour()
    if Button_hist.inside((x, y)):
        reboutons(0, 0)
        end_hist()
    if Button_quit.inside((x, y)):
        bye()


Button_hist = Button((350, -300), 'hist', (80, 30))
main()
Button_end = Button((350, 100), 'Rage', (80, 30))
Button_new = Button((350, -100), 'New', (80, 30))
Button_back = Button((350, 0), 'Back', (80, 30))
Button_quit = Button((350, -200), 'Quit', (80, 30))
s = getscreen()
s.onkey(haut, 'Up')
s.onkey(bas, 'Down')
s.onkey(gauche, 'Left')
s.onkey(droite, 'Right')
s.onclick(f)
s.listen()
done()
# perdre
# new 1x sur 2 un 4
# win trop de reboutons
