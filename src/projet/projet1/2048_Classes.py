# 2048
from turtle import *
from random import choice
from time import sleep
from pygame import mixer


# Ce modèle sert à créer les cases qui se calqueront sur les cases, de la fonction cases(), avec leur chiffre et couleur
class Case:
    def __init__(self, pos, text, size=77.5):
        self.pos = pos
        self.size = size
        self.text = text
        self.draw()

    # cette fonction permet de déssiner la case avec sa couleur et son chiffre
    def draw(self):
        up()
        x, y = self.pos
        goto(x, y)
        color_num = {-1: 'grey', 0: 'darkgrey', 2: 'whitesmoke', 4: 'MistyRose', 8: 'plum1', 16: 'orchid2', 32: 'magenta',
             64: 'magenta3', 128: 'DeepPink', 256: 'MediumVioletRed', 512: 'VioletRed1', 1024: 'LightSeaGreen',
              2048: 'turquoise1'}
        couleur = color_num[self.text]
        color(couleur)
        begin_fill()
        for i in range(4):
            forward(self.size)
            right(90)
        end_fill()
        if self.text != 0 and self.text != -1:
            goto(x + self.size / 2, y - self.size / 2 - 10)
            color('black')
            write(self.text, font=('Arial', 20), align='center')

    def __str__(self):
        return f'Case({self.pos}, {self.text})'

    def cases():
        tour = Case((-180, 200), -1, 360)
        for y in 190, 102.5, 15, -72.5:
            for x in -170, -82.5, 5, 92.5:
                case_begin = Case((x, y), 0)


class Rectangle:
    """Draw a filled rectangle."""

    def __init__(self, pos, size, color='Lightgrey'):
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


# Ce modèle crée des boutons
class Button:
    def __init__(self, pos, text, size=(60, 30), color='Lightgrey'):
        # hello
        self.rect = Rectangle(pos, size, color)
        x, y = pos
        w, h = size
        self.color = color
        self.label = Text((x+w/2, y+h/4 - 1), text, h//2, 'center')
#         self.draw()

#     # cette fonction permet de dessiner le bouton
    def draw(self):
        self.rect.draw()
        self.label.draw()
#         goto(self.pos)
# #         fillcolor(self.color)
# #         begin_fill()
# #         for x in self.size * 2:
# #             forward(x)
# #             left(90)
# #         end_fill()
# #         x, y = self.pos
# #         w, h = self.size
#         goto(x+w/2, y+h/4 - 1)
#         color('black')
#         write(self.text, font=('Arial', h//2), align='center')
#
#     def __str__(self):
#         return f'Button({self.pos}, {self.text})'

    # cette fonction permet de calculer si la position donnée est à l'intérieur du bouton
    def inside(self, p):
        return self.rect.inside(p)


class Text:
    """Draw a text at a given position."""

    def __init__(self, pos, text, size, align, color='black', typeface='Arial'):
        """Initilizes the text"""
        self.pos = pos
        self.text = text
        self.size = size
        self.align = align
        self.color = color
        self.typeface = typeface
        self.draw()

    def draw(self):
        """Draw the text."""
        goto(self.pos)
        color(self.color)
        write(self.text, font=(self.typeface, self.size), align=self.align)


class Game:

    def __init__(self):
        setup(600, 400)
        hideturtle()
        tracer(0)
        up()
        self.button_hist = Button((210, -135), 'hist')
        goto(0, 0)
        addshape("src/projet/projet1/bois.gif")
        shape("src/projet/projet1/bois.gif")
        stamp()
        self.state = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        ]

        self.correspondance = {
        (0, 0): (-170.0, 190.0), (0, 1): (-82.5, 190.0), (0, 2): (5.0, 190.0), (0, 3): (92.5, 190.0),
        (1, 0): (-170.0, 102.5), (1, 1): (-82.5, 102.5), (1, 2): (5.0, 102.5), (1, 3): (92.5, 102.5),
        (2, 0): (-170.0, 15.0), (2, 1): (-82.5, 15.0), (2, 2): (5.0, 15.0), (2, 3): (92.5, 15.0),
        (3, 0): (-170.0, -72.5), (3, 1): (-82.5, -72.5), (3, 2): (5.0, -72.5), (3, 3): (92.5, -72.5)
        }

        self.correspondance_inverse = {value: key for key, value in self.correspondance.items()}
        self.hist = []
        self.retour_hist = []

        self.score = 0
        self.historique = []
        self.cases = Case.cases()
        self.pause = 0
        self.modifi = 0
        self.nbr = 0
        self.score = 0
        self.endjeu = 1
        self.not_op = 0

        self.button_end = Button((210, 125), 'Rage')
        self.button_new = Button((210, -5), 'New')
        self.button_back = Button((210, 60), 'Back')
        self.button_quit = Button((210, -70), 'Quit')
        self.title()
        self.son_fond()

        self.new(1)
        self.resultat()

        s = getscreen()
        s.onkey(lambda: self.haut(), 'Up')
        s.onkey(lambda: self.bas(), 'Down')
        s.onkey(lambda: self.gauche(), 'Left')
        s.onkey(lambda: self.droite(), 'Right')
        s.onkey(lambda: self.retour(), 'BackSpace')
        s.onclick(self.click)
        s.listen()

    def title(self):
        x, y = -240, 80
        mot = ('2', '0', '4', '8')
        for l in mot:
            Text((x, y), l, 45, 'center', 'white')
            y -= 60

    def reboutons(self, rage, hist=1, back=0):
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
    def song(self, win):
        mixer.music.stop()
        if win:
            mixer.music.load("src/projet/projet1/win.mp3")
            mixer.music.play()
            sleep(6)
        else:
            mixer.music.load("src/projet/projet1/cri.wav")
            mixer.music.play()
            sleep(1)
        mixer.music.load("src/projet/projet1/Sojiada-Lanmou.mp3")
        mixer.music.play(-1)

    # cette fonction sert à écrire l'historique sous formes de flèches
    def end_hist(self):
        clear()
        goto(0, 0)
        addshape("src/projet/projet1/bois.gif")
        shape("src/projet/projet1/bois.gif")
        stamp()
        self.reboutons(0, 0, 0)
        goto(0, 180)
        color('white')
        write('historique:', font=('Arial', 12), align='center')
        if len(self.hist) != 0:
            partie = []
            writehist = []
            for i in range(len(self.hist)):
                partie.append(self.hist[i])
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

    # cette fonction prend les coordonnées de la case et retourn la valeur de celle-ci
    def coord_to_res(self, xcoord, ycoord):
#         global correspondance_inverse
        yres, xres = self.correspondance_inverse[(xcoord, ycoord)]
#         global state
        return self.state[yres][xres]

    # cette fonction remet le jeu comme c'était le tour d'avant et supprime la sauvegarde du dernier coup
    def retour(self):
        print(self.retour_hist)
        self.retour_hist.pop(-1)
        print(self.retour_hist)
        self.state = self.retour_hist[-1]
        for c in self.correspondance_inverse:
            y, x = self.correspondance_inverse[c]
            text = self.state[y][x]
            case_back = Case(c, text)
        self.hist.pop()
        self.score -= 2
        self.nbr -= 1
        self.resultat()


#     # cette fonction permet de mémoriser la position de chaque case
#     def retour_calcul(self):
# #         global retour_hist
# #         global state
#         self.retour_hist.append(self.state)

    # cette fonction permet de mémoriser les coups à l'aide d'une flèche ajoutée à l'historique
    def historiquef(self, direction):
#         global hist
        if direction == 'h':
            self.hist.append('↑')
        elif direction == 'b':
            self.hist.append('↓')
        elif direction == 'd':
            self.hist.append('→')
        elif direction == 'g':
            self.hist.append('←')

    #  cette fonction permet de créer une nouvelle case après un coup
    def new(self, newretour=0):
#         global nbr
        listexy = (0, 1, 2, 3)
        xres = choice(listexy)
        yres = choice(listexy)
#         global state
#         global correspondance
        if self.nbr == 16:
            self.end('Game Over', 0)
        elif self.state[yres][xres] == 0:
            case2 = Case(self.correspondance[(yres, xres)], 2)
            self.state[yres][xres] = 2
            self.nbr += 1
            self.pause = 1
            self.score += 2
            if newretour:
                self.retour_hist.append(self.state)
        else:
            self.new()

    # cette fonction fait le changement de case
    def changement(self, xpos, ypos, xsuiv, ysuiv):
        if (xpos, ypos) != (xsuiv, ysuiv):
            if self.coord_to_res(xsuiv, ysuiv) == 0:
                nbrsuiv = self.coord_to_res(xpos, ypos)
            else:
                nbrsuiv = self.coord_to_res(xpos, ypos) * 2
#             global correspondance_inverse
#             global state
            casei = Case((xsuiv, ysuiv), nbrsuiv)
            ysuivres, xsuivres = self.correspondance_inverse[(xsuiv, ysuiv)]
            self.state[ysuivres][xsuivres] = nbrsuiv
            case0 = Case((xpos, ypos), 0)
            yposres, xposres = self.correspondance_inverse[(xpos, ypos)]
            self.state[yposres][xposres] = 0
#             global nbr
            self.nbr -= 1
#             global modifi
            self.modifi = 1

    # cette fonction calcule les coordonnées de la case suivante en fonction de la direction
    def operation(self, coord, direction):
#         global correspondance_inverse
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
        if (xcoord, ycoord) not in self.correspondance_inverse:
            self.not_op = 1
            xcoord, ycoord = coord_memoire
        return xcoord, ycoord

    # cette fonction permet de calculer les coordonnées de la case présedente
    # elle est utilisé si la case suivante est une bordure ou une case d'un autre chiffre
    def operation_inverse(self, coord, direction):
        self.correspondance_inverse
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
    def notsame(self, xpos, ypos, xsuiv, ysuiv, direction):
        while True:
            if self.coord_to_res(xsuiv, ysuiv) == 0:
                xsuiv, ysuiv = self.operation((xsuiv, ysuiv), direction)
                if self.not_op:
                    self.not_op = 0
                    self.changement(xpos, ypos, xsuiv, ysuiv)
                    break
            elif self.coord_to_res(xpos, ypos) == self.coord_to_res(xsuiv, ysuiv):
                self.changement(xpos, ypos, xsuiv, ysuiv)
                break
            elif self.coord_to_res(xpos, ypos) != self.coord_to_res(xsuiv, ysuiv):
                xsuiv, ysuiv = self.operation_inverse((xsuiv, ysuiv), direction)
                self.changement(xpos, ypos, xsuiv, ysuiv)
                break

    # cette fonction calcule si le chiffre dans la case est le même que le suivant
    def calcul(self, pos, direction):
        xsuiv, ysuiv = self.operation(pos, direction)
        if not self.not_op:
            xpos, ypos = pos
            if self.coord_to_res(xpos, ypos) == self.coord_to_res(xsuiv, ysuiv):
                self.changement(xpos, ypos, xsuiv, ysuiv)
            else:
                self.notsame(xpos, ypos, xsuiv, ysuiv, direction)
        else:
            self.not_op = 0

    # cette fonction, si le jeu n'est pas fini, lance les calculs des changements possible de cases
    # Si, après les calculs, il n'y a eu aucune modification dans le jeu, le coup est considéré comme sans intéret et le joueur peut rejouer
    def mouvement(self, direction):
        if self.endjeu == 1:
            self.modifi = 0
#             global state
#             global correspondance_inverse
            for i in range(4):
                for coord in self.correspondance_inverse:
                    xcoord, ycoord = coord
                    if self.coord_to_res(xcoord, ycoord) != 0:
                        self.calcul(coord, direction)
            if self.modifi == 1:
                self.new()
                self.resultat()
            else:
                self.pause = 1
            self.historiquef(direction)
            self.retour_hist.append(self.state)

    # cette fonction, si l'ordinateur n'est pas encore en calcul dù au dernier coup, lance la fonction mouvement() avec comme variable la direction donnée
    def haut(self):
        if self.pause:
            self.pause = 0
            self.mouvement('h')

    # cette fonction, si l'ordinateur n'est pas encore en calcul dù au dernier coup, lance la fonction mouvement() avec comme variable la direction donnée
    def bas(self):
        if self.pause:
            self.pause = 0
            self.mouvement('b')

    # cette fonction, si l'ordinateur n'est pas encore en calcul dù au dernier coup, lance la fonction mouvement() avec comme variable la direction donnée
    def gauche(self):
        if self.pause:
            self.pause = 0
            self.mouvement('g')

    # cette fonction, si l'ordinateur n'est pas encore en calcul dù au dernier coup, lance la fonction mouvement() avec comme variable la direction donnée
    def droite(self):
        if self.pause:
            self.pause = 0
            self.mouvement('d')

    # cette fonction lance le son de fond
    def son_fond(self):
        mixer.init()
        mixer.music.load("src/projet/projet1/Meydn-SynthwaveVibe.mp3")
        mixer.music.play(-1)

    # cette fonction rement des variables comment ils étaient au début
#     def rezero(self):  # supprimer car que à 1 endroit? (newgame())
#         global pause
#         global modifi
#         global nbr
#         global score
#         global endjeu
#         self.pause, self.modifi , self.nbr, self.score, self.endjeu = 0, 0, 0, 0, 1

    def click(self, x, y):
        p = x, y
        if self.button_quit.inside(p):
            mixer.quit()
            bye()

        if self.button_end.inside(p):
            self.end('Tant Pis :(', 0)

        if self.button_new.inside(p):
            self.newgame()

        if self.button_back.inside(p):
            if len(self.hist) != 0:
                self.retour()

        if self.button_hist.inside(p):
            self.end_hist()


#     def reboutons():

    # cette fonction calcul le nombre maximum sur le plateau et le score. Il les écrit au bas du plateau
    def resultat(self):
        goto(-170, -175)
        width(20)
        down()
        color('white')
        goto(170, -175)
        width(1)
        up()
        nbrmax = 0
        for y in self.state:
            if max(y) > nbrmax:
                nbrmax = max(y)
        txt_score = 'score: ' + str(self.score) + 20 * ' ' + 'max: ' + str(nbrmax)
        Text((0, -185), txt_score, 13, 'center')
        if nbrmax == 2048:
            sleep(1)
            self.end('2048 c\'est la win!', 1)

    def end(self, text, win):
        clear()
        goto(0, 0)
        addshape("src/projet/projet1/bois.gif")
        shape("src/projet/projet1/bois.gif")
        stamp()

        self.text = text
        citation = '''“L'échec fait partie intégrante de notre réussite. L'échec, c'est l'envers de la réussite."\nJean-Pierre Chevènement'''
#         global endjeu
        self.endjeu = 1
        self.reboutons(0)
        Text((0, 0), self.text, 40, 'center', 'white')
        if not win:
            Text((0, -110), citation, 12, 'center', 'white', 'Didot')
        else:
            goto(0, -100)
            write('👍     ╰*°▽°*╯     👍', font=('Arial', 30), align='center')
        color('black')
        self.song(win)

    def newgame(self):
        # cette fonction remet les variables comment elles étaient au début et redessine le jeu
        clear()

        goto(0, 0)
        stamp()

        self.draw()
#         global hist
#         global state
        self.state = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        ]
        self.pause, self.modifi, self.nbr, self.score, self.endjeu = 0, 0, 0, 0, 1
        self.hist = []
#         reboutons(1, 1, 1)
# #         Case.cases()
        self.new(1)
        self.resultat()
#         self.resultat()
#     #     son_fond()

    def draw(self):
        """Draws all the game objects."""
#         self.cases.draw()
        Case.cases()
#         self.title.draw()
#         self.status.draw()
#         self.button_hist.draw()
        self.title()
        self.resultat()
        self.button_end.draw()
        self.button_new.draw()
        self.button_back.draw()
        self.button_quit.draw()


game = Game()
done()
