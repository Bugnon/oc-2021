
from cmath import e
from re import S, X
from tkinter import CENTER
import pygame
from pygame.locals import *
import time
from random import randint

#Affiche le score :
def Score() :
    font = pygame.font.SysFont('franklingothicmedium', 56)
    score = font.render(str(objet.nbObjets), True, "white")
    screen.blit(score, (15, 15))

def CheckVictory() :
    global GAME, MENU
    if objet.nbObjets == nbPieces :
        victoire = pygame.image.load("images/victoire.png")
        screen = pygame.display.set_mode((victoire.get_width(), victoire.get_height()))
        screen.blit(victoire, (0, 0))
        pygame.display.update()
        click = False
        while click == False :
            for event in pygame.event.get() :
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                    click = True
        GAME = False
        MENU = True

#3 2 1 goo :
def Depart() :
    nb = 3
    font = pygame.font.SysFont('franklingothicmedium', 256)
    while nb >= 1 :
        fond.Initialise()
        for missile in listeMissiles :
            missile.Display()
        personnage.Display()
        text = font.render(str(nb), True, "red")
        text_rect = text.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        screen.blit(text, text_rect)
        pygame.display.update()

        time.sleep(1)
        nb -= 1
    firstTime = False

#Initialise le jeu lorsque l'on veut recommencer :
def InitJeu() :
    global missileH1, missileH2, missileH3, missileH4, missileD1, missileD2, missileB1, missileB2, missileB3, missileG1, missileG2, missileG3, CoordExplosion, lastPressedKey, lastEventType
    missileH1.x, missileH1.y = 115, 210
    missileH2.x, missileH2.y = 360, 210
    missileH3.x, missileH3.y = 835, 210
    missileH4.x, missileH4.y = 1075, 210
    missileD1.x, missileD1.y = 1130, 480
    missileD2.x, missileD2.y = 1130, 720
    missileB1.x, missileB1.y = 960, 900
    missileB2.x, missileB2.y = 600, 900
    missileB3.x, missileB3.y = 235, 900 
    missileG1.x, missileG1.y = 70, 360
    missileG2.x, missileG2.y = 70, 595 
    missileG3.x, missileG3.y = 70, 835 
    personnage.x, personnage.y = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
    CoordExplosion = []
    lastPressedKey = []
    lastEventType = {"Up" : 0, "Down" : 0, "Left" : 0, "Right" : 0}

#Check les collisions entre tous les missiles (collision avec rectangles) :

def MissileCollisionMissile() :
    for missile1 in listeMissiles :
        for missile2 in listeMissiles :
            if missile1 != missile2 :
                if missile1.direction == "N" or missile1.direction == "S" :
                    if missile2.direction == "N" or missile2.direction == "S" :
                        rect1 = pygame.Rect(missile1.x - (missile1.imgLargeur / 2), missile1.y - (missile1.imgLongueur / 2), missile1.imgLargeur, missile1.imgLongueur)
                        rect2 = pygame.Rect(missile2.x - (missile2.imgLargeur / 2), missile2.y - (missile2.imgLongueur / 2), missile2.imgLargeur, missile2.imgLongueur)
                        if pygame.Rect.colliderect(rect1, rect2) :
                            r = randint(0, 1)
                            if r == 0 :
                                missile1.touche = True
                                CoordExplosion.append([(missile1.x + missile2.x) / 2, (missile1.y + missile2.y) / 2, 0])
                            elif r == 1 :
                                missile2.touche = True
                                CoordExplosion.append([(missile1.x + missile2.x) / 2, (missile1.y + missile2.y) / 2, 0])
                            missile1.Display()
                            missile2.Display()
                    elif missile2.direction == "E" or missile2.direction == "W" :
                        rect1 = pygame.Rect(missile1.x - (missile1.imgLargeur / 2), missile1.y - (missile1.imgLongueur / 2), missile1.imgLargeur, missile1.imgLongueur)
                        rect2 = pygame.Rect(missile2.x - (missile2.imgLongueur / 2), missile2.y - (missile2.imgLargeur / 2), missile2.imgLongueur, missile2.imgLargeur)
                        if pygame.Rect.colliderect(rect1, rect2) :
                            r = randint(0, 1)
                            if r == 0 :
                                missile1.touche = True
                                CoordExplosion.append([(missile1.x + missile2.x) / 2, (missile1.y + missile2.y) / 2, 0])
                            elif r == 1 :
                                missile2.touche = True
                                CoordExplosion.append([(missile1.x + missile2.x) / 2, (missile1.y + missile2.y) / 2, 0])
                            missile1.Display()
                            missile2.Display()
                elif missile1.direction == "E" or missile1.direction == "W" :
                    if missile2.direction == "N" or missile2.direction == "S" :
                        rect1 = pygame.Rect(missile1.x - (missile1.imgLongueur / 2), missile1.y - (missile1.imgLargeur / 2), missile1.imgLongueur, missile1.imgLargeur)
                        rect2 = pygame.Rect(missile2.x - (missile2.imgLargeur / 2), missile2.y - (missile2.imgLongueur / 2), missile2.imgLargeur, missile2.imgLongueur)
                        if pygame.Rect.colliderect(rect1, rect2) :
                            r = randint(0, 1)
                            if r == 0 :
                                missile1.touche = True
                                CoordExplosion.append([(missile1.x + missile2.x) / 2, (missile1.y + missile2.y) / 2, 0])
                            elif r == 1 :
                                missile2.touche = True
                                CoordExplosion.append([(missile1.x + missile2.x) / 2, (missile1.y + missile2.y) / 2, 0])
                            missile1.Display()
                            missile2.Display()
                    elif missile2.direction == "E" or missile2.direction == "W" :
                        rect1 = pygame.Rect(missile1.x - (missile1.imgLongueur / 2), missile1.y - (missile1.imgLargeur / 2), missile1.imgLongueur, missile1.imgLargeur)
                        rect2 = pygame.Rect(missile2.x - (missile2.imgLongueur / 2), missile2.y - (missile2.imgLargeur / 2), missile2.imgLongueur, missile2.imgLargeur)
                        if pygame.Rect.colliderect(rect1, rect2) :
                            r = randint(0, 1)
                            if r == 0 :
                                missile1.touche = True
                                CoordExplosion.append([(missile1.x + missile2.x) / 2, (missile1.y + missile2.y) / 2, 0])
                            elif r == 1 :
                                missile2.touche = True
                                CoordExplosion.append([(missile1.x + missile2.x) / 2, (missile1.y + missile2.y) / 2, 0])
                            missile1.Display()
                            missile2.Display()


#regarde si les missiles touchent le joueur :   
def MissileActualisation() :
    global GAME, MORT
    MissileCollisionMissile()
    for missile in listeMissiles :
        if missile.CheckCollision() == True :
            personnage.Mort()
            MORT = True
            GAME = False
        missile.Display()

    #gestion des explosions :
    if CoordExplosion != [] :
        num = 0
        for x, y, frame in CoordExplosion :
            if frame <= 7 :
                imgExp = pygame.image.load(explosions[frame])
                screen.blit(imgExp, (x - (imgExp.get_width() / 2), y - (imgExp.get_height() / 2)))
                CoordExplosion[num][2] += 1
            else :
                del CoordExplosion[num]
            num += 1

      


class Missile() :
    def __init__(self, x, y, direction, vitesse) :
        self.imgMissileBas = pygame.image.load("images/MissileBas.png")
        self.imgMissileHaut = pygame.image.load("images/MissileHaut.png")
        self.imgMissileDroite = pygame.image.load("images/MissileDroite.png")
        self.imgMissileGauche = pygame.image.load("images/MissileGauche.png")
        self.imgLongueur = self.imgMissileBas.get_height()
        self.imgLargeur = self.imgMissileBas.get_width()
        self.x = x
        self.y = y
        self.touche = False
        self.direction = direction
        self.vitesse = vitesse
    def Display(self) :
        if self.direction == "S" :
            if self.y > SCREEN_HEIGHT or self.touche == True : 
                self.y = 210
                self.vitesse = randint(MINMISSILE, MAXMISSILE)
                self.touche = False
            screen.blit(self.imgMissileBas, (self.x - (0.5 * self.imgLargeur), self.y - (0.5 * self.imgLongueur)))
            if firstTime != True :
                self.y += self.vitesse
        elif self.direction == "N" :
            if self.y < 0 or self.touche == True :
                self.y = 900
                self.vitesse = randint(MINMISSILE, MAXMISSILE)
                self.touche = False
            screen.blit(self.imgMissileHaut, (self.x - (0.5 * self.imgLargeur), self.y - (0.5 * self.imgLongueur)))
            if firstTime != True :
                self.y -= self.vitesse
        elif self.direction == "E" :
            if self.x > SCREEN_WIDTH or self.touche == True :
                self.x = 70
                self.vitesse = randint(MINMISSILE, MAXMISSILE)
                self.touche = False
            screen.blit(self.imgMissileDroite, (self.x - (0.5 * self.imgLongueur), self.y - (0.5 * self.imgLargeur)))
            if firstTime != True :
                self.x += self.vitesse
        elif self.direction == "W" :
            if self.x < 0 or self.touche == True :
                self.x = 1130
                self.vitesse = randint(MINMISSILE, MAXMISSILE)
                self.touche = False
            screen.blit(self.imgMissileGauche, (self.x - (0.5 * self.imgLongueur), self.y - (0.5 * self.imgLargeur)))
            if firstTime != True :
                self.x -= self.vitesse

    def CheckCollision(self) :

        #PerfectCollision entre missile et personnage :

        if self.direction == "N" :
            missileMask = pygame.mask.from_surface(self.imgMissileHaut)
            offset = (int((self.x - (self.imgLargeur / 2)) - (personnage.x - (personnage.imageActuelle().get_width() / 2)))), int((self.y - (self.imgLongueur / 2) - (personnage.y - (personnage.imageActuelle().get_height() / 2))))
        elif self.direction == "S" :
            missileMask = pygame.mask.from_surface(self.imgMissileBas)
            offset = (int((self.x - (self.imgLargeur / 2)) - (personnage.x - (personnage.imageActuelle().get_width() / 2)))), int((self.y - (self.imgLongueur / 2) - (personnage.y - (personnage.imageActuelle().get_height() / 2))))
        elif self.direction == "E" :
            missileMask = pygame.mask.from_surface(self.imgMissileDroite)
            offset = (int((self.x - (self.imgLongueur / 2)) - (personnage.x - (personnage.imageActuelle().get_width() / 2)))), int((self.y - (self.imgLargeur / 2) - (personnage.y - (personnage.imageActuelle().get_height() / 2))))
        elif self.direction == "W" :
            missileMask = pygame.mask.from_surface(self.imgMissileGauche)
            offset = (int((self.x - (self.imgLongueur / 2)) - (personnage.x - (personnage.imageActuelle().get_width() / 2)))), int((self.y - (self.imgLargeur / 2) - (personnage.y - (personnage.imageActuelle().get_height() / 2))))
        persoMask = pygame.mask.from_surface(personnage.imageActuelle())
        if persoMask.overlap(missileMask, offset) :
            return True


class Objets() :
    def __init__(self) :
        self.nbObjets = 0
        self.frame = 0
        self.ActuelleImage = pygame.image.load(coins[self.frame])
        self.x = randint(int(59 + (self.ActuelleImage.get_width() / 2)), int(1135 - (self.ActuelleImage.get_width() / 2)))
        self.y = randint(int(300 + (self.ActuelleImage.get_height() / 2)), int(895 - (self.ActuelleImage.get_height() / 2)))

    def Display(self) :
        if self.frame > 5 :
            self.frame = 0
        elif self.frame <= 5 :
            self.ActuelleImage = pygame.image.load(coins[self.frame])
            screen.blit(self.ActuelleImage, (self.x - (self.ActuelleImage.get_width() / 2), self.y - (self.ActuelleImage.get_height() / 2)))
            objet.checkCollisionPerso()
            self.frame += 1

    def checkCollisionPerso(self) :
        maskObjet = pygame.mask.from_surface(self.ActuelleImage)
        maskPerso = pygame.mask.from_surface(personnage.imageActuelle())
        offset = (int((self.x - (self.ActuelleImage.get_width() / 2)) - (personnage.x - (personnage.imageActuelle().get_width() / 2))), int((self.y - (self.ActuelleImage.get_height() / 2)) - (personnage.y - (personnage.imageActuelle().get_height() / 2))))
        if maskPerso.overlap(maskObjet, offset) :
            self.x = randint(int(59 + (self.ActuelleImage.get_width() / 2)), int(1135 - (self.ActuelleImage.get_width() / 2)))
            self.y = randint(int(300 + (self.ActuelleImage.get_height() / 2)), int(895 - (self.ActuelleImage.get_height() / 2)))
            self.nbObjets += 1



class Fond() :
    def __init__(self) :
        self.fond = pygame.image.load('images/salleDongeon.png')
    def Initialise(self) :
        screen.blit(self.fond, (0, 0))


class Perso() :
    def __init__(self, x, y) :
        self.perso_image_Droite = pygame.image.load("images/PR1.png")
        self.perso_image_Gauche = pygame.image.load("images/PL1.png")
        self.perso_image_Haut = pygame.image.load("images/PU1.png")
        self.perso_image_Bas = pygame.image.load("images/PD1.png")
        self.actualDirection = "D"
        self.x = x
        self.y = y
        self.lastimg = []
        self.pos = (self.x, self.y)
    def DisplayCentre(self) :
        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT / 2
        self.actualDirection = "D"
        personnage.Display()
    def Display(self) :
        if self.actualDirection == "D" :
            screen.blit(self.perso_image_Bas, (self.x - (self.perso_image_Bas.get_width() / 2), self.y - (self.perso_image_Bas.get_height() / 2)))
            if self.lastimg != [] :
                del self.lastimg[0]
            self.lastimg.append(self.perso_image_Bas)
        elif self.actualDirection == "U" :
            screen.blit(self.perso_image_Haut, (self.x - (self.perso_image_Haut.get_width() / 2), self.y - (self.perso_image_Haut.get_height() / 2)))
            if self.lastimg != [] :
                del self.lastimg[0]
            self.lastimg.append(self.perso_image_Haut)
        elif self.actualDirection == "L" :
            screen.blit(self.perso_image_Gauche, (self.x - (self.perso_image_Gauche.get_width() / 2), self.y - (self.perso_image_Gauche.get_height() / 2)))
            if self.lastimg != [] :
                del self.lastimg[0]
            self.lastimg.append(self.perso_image_Gauche)
        elif self.actualDirection == "R" :
            screen.blit(self.perso_image_Droite, (self.x - (self.perso_image_Droite.get_width() / 2), self.y - (self.perso_image_Droite.get_height() / 2)))
            if self.lastimg != [] :
                del self.lastimg[0]
            self.lastimg.append(self.perso_image_Droite)
        


    def Mort(self) :
        fond.Initialise()
        for missile in listeMissiles :
            missile.Display()
        persoMort = pygame.image.load("images/PM.png")
        screen.blit(persoMort, (self.x, self.y))


    def Rect(self) :
        if self.actualDirection == "D" :
            return pygame.Rect(self.x - (self.perso_image_Bas.get_width() / 2), self.y - (self.perso_image_Bas.get_height() / 2), self.perso_image_Bas.get_width(), self.perso_image_Bas.get_height())
        elif self.actualDirection == "U" :
            return pygame.Rect(self.x - (self.perso_image_Haut.get_width() / 2), self.y - (self.perso_image_Haut.get_height() / 2), self.perso_image_Haut.get_width(), self.perso_image_Haut.get_height())
        elif self.actualDirection == "L" :
            return pygame.Rect(self.x - (self.perso_image_Gauche.get_width() / 2), self.y - (self.perso_image_Gauche.get_height() / 2), self.perso_image_Gauche.get_width(), self.perso_image_Gauche.get_height())
        elif self.actualDirection == "R" :
            return pygame.Rect(self.x - (self.perso_image_Droite.get_width() / 2), self.y - (self.perso_image_Droite.get_height() / 2), self.perso_image_Droite.get_width(), self.perso_image_Droite.get_height())

    def imageActuelle(self) :
        if self.lastimg != [] :
            return self.lastimg[0]

    def imgLargeur(self) :
        if self.actualDirection == "D" :
            return self.perso_image_Bas.get_width()
        elif self.actualDirection == "U" :
            return self.perso_image_Haut.get_width()
        elif self.actualDirection == "L" :
            return self.perso_image_Gauche.get_width()
        elif self.actualDirection == "R" :
            return self.perso_image_Droite.get_width()
    def imgHauteur(self) :
        if self.actualDirection == "D" :
            return self.perso_image_Bas.get_height()
        elif self.actualDirection == "U" :
            return self.perso_image_Haut.get_height()
        elif self.actualDirection == "L" :
            return self.perso_image_Gauche.get_height()
        elif self.actualDirection == "R" :
            return self.perso_image_Droite.get_height()
    def Up(self) :
        if self.y - SPEED < 300 :
            self.y -= self.y - 300
        else :
            self.y -= SPEED
        self.actualDirection = "U"
        personnage.Display()
    def Down(self) :
        if self.y + SPEED > 835 :
            self.y += 835 - self.y
        else :
            self.y += SPEED
        self.actualDirection = "D"
        personnage.Display()
    def Left(self) :
        if self.x - SPEED < 95 :
            self.x -= self.x - 95
        else :
            self.x -= SPEED
        self.actualDirection = "L"
        personnage.Display()
    def Right(self) :
        if self.x + SPEED > 1105 :
            self.x += 1105 - self.x
        else :
            self.x += SPEED
        self.actualDirection = "R"
        personnage.Display()


    def NW(self) :
        if self.x - SPEED < 95 and self.y - SPEED < 300 :
            self.x = 95
            self.y = 300
        elif self.x - SPEED < 95 :
            self.x -= self.x - 95
            self.y -= SPEED / (2 ** 0.5)
        elif self.y - SPEED < 300 :
            self.y -= self.y - 300
            self.x -= SPEED / (2 ** 0.5)
        else :
            self.x -= SPEED / (2 ** 0.5)
            self.y -= SPEED / (2 ** 0.5)
        personnage.Display()
    def NE(self) :
        if self.y - SPEED < 300 and self.x + SPEED > 1105 :
            self.x = 1105
            self.y = 300
        elif self.y - SPEED < 300 :
            self.y -= self.y - 300
            self.x += SPEED / (2 ** 0.5)
        elif self.x + SPEED > 1105 :
            self.x += 1105 - self.x
            self.y -= SPEED / (2 ** 0.5)
        else :
            self.x += SPEED / (2 ** 0.5)
            self.y -= SPEED / (2 ** 0.5)
        personnage.Display()
    def SW(self) :
        if self.x - SPEED < 95 and self.y + SPEED > 835 :
            self.x = 95
            self.y = 835
        elif self.x - SPEED < 95 :
            self.x -= self.x - 95
            self.y += SPEED / (2 ** 0.5)
        elif self.y + SPEED > 835 :
            self.y += 835 - self.y
            self.x -= SPEED / (2 ** 0.5)
        else :
            self.x -= SPEED / (2 ** 0.5)
            self.y += SPEED / (2 ** 0.5)
        personnage.Display()
    def SE(self) :
        if self.y + SPEED > 835  and self.x + SPEED > 1105 :
            self.x = 1105
            self.y = 835
        elif self.y + SPEED > 835 :
            self.y += 835 - self.y
            self.x += SPEED / (2 ** 0.5)
        elif self.x + SPEED > 1105 :
            self.x += 1105 - self.x
            self.y += SPEED / (2 ** 0.5)
        else :
            self.x += SPEED / (2 ** 0.5)
            self.y += SPEED / (2 ** 0.5)
        personnage.Display()


#VARIABLES GLOBALES :

SCREEN_HEIGHT = 960
SCREEN_WIDTH = 1200
CASE = 120
SPEED = 10
MINMISSILE = 5
MAXMISSILE = 10

#variables booléennes :
GAME = False
MAIN = True
MORT = False
MENU = True


#Début
pygame.init()

missileH1 = Missile(115, 210, 'S', randint(MINMISSILE, MAXMISSILE))
missileH2 = Missile(360, 210, 'S', randint(MINMISSILE, MAXMISSILE))
missileH3 = Missile(835, 210, 'S', randint(MINMISSILE, MAXMISSILE))
missileH4 = Missile(1075, 210, 'S', randint(MINMISSILE, MAXMISSILE))
missileD1 = Missile(1130, 480, 'W', randint(MINMISSILE, MAXMISSILE))
missileD2 = Missile(1130, 720, 'W', randint(MINMISSILE, MAXMISSILE))
missileB1 = Missile(960, 900, 'N', randint(MINMISSILE, MAXMISSILE))
missileB2 = Missile(600, 900, 'N', randint(MINMISSILE, MAXMISSILE))
missileB3 = Missile(235, 900, 'N', randint(MINMISSILE, MAXMISSILE))
missileG1 = Missile(70, 360, 'E', randint(MINMISSILE, MAXMISSILE))
missileG2 = Missile(70, 595, 'E', randint(MINMISSILE, MAXMISSILE))
missileG3 = Missile(70, 835, 'E', randint(MINMISSILE, MAXMISSILE))

#images d'animation pièce / explosions :
coins = ["images/coin.0.png", "images/coin.1.png", "images/coin.2.png", "images/coin.3.png", "images/coin.4.png", "images/coin.5.png"]
explosions = ["images/explosion.0.png", "images/explosion.1.png", "images/explosion.2.png", "images/explosion.3.png", "images/explosion.4.png",
              "images/explosion.5.png", "images/explosion.6.png", "images/explosion.7.png"]

CoordExplosion = []

listeMissiles = [missileH1, missileH2, missileH3, missileH4, missileD1, missileD2, missileB1, missileB2, missileB3, missileG1, missileG2, missileG3]

clock = pygame.time.Clock()

fond = Fond()

objet = Objets()
nbPieces = 5

personnage = Perso(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

lastEventType = {"Up" : 0, "Down" : 0, "Left" : 0, "Right" : 0}
listOfKeys = list(lastEventType.keys())
lastPressedKey = []

difficulte = 1
menu = pygame.image.load("images/menu.png")

while MAIN == True :
    #si le perso est mort :
    while MORT == True :        
        gameOver = pygame.image.load("images/gameOver.png")
        screen = pygame.display.set_mode((gameOver.get_width(), gameOver.get_height()))
        screen.blit(gameOver, (0, 0))
        mouseX, mouseY = pygame.mouse.get_pos()
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
            #Si on appuie sur exit :
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                if 685 < mouseX < 707 and 310 < mouseY < 330 :
                    MORT = False
                    MENU = True
        pygame.display.update()


    while MENU == True :
        mouseX, mouseY = pygame.mouse.get_pos()
        MENUWIDTH = menu.get_width()
        MENUHEIGHT = menu.get_height()
        screen = pygame.display.set_mode((MENUWIDTH, MENUHEIGHT))
        mouseX, mouseY = pygame.mouse.get_pos()

        #si on passe la souris sur les boutons :
        if 867 < mouseX < 890 and 315 < mouseY < 355 :
            menu = pygame.image.load("images/menu1.png")
        elif 935 < mouseX < 955 and 315 < mouseY < 355 :
            menu = pygame.image.load("images/menu2.png")
        elif 980 < mouseX < 1007 and 315 < mouseY < 355 :
            menu = pygame.image.load("images/menu3.png")
        elif 555 < mouseX < 1090 and 222 < mouseY < 282 :
            menu = pygame.image.load("images/menuStart.png")
        else :
            menu = pygame.image.load("images/menu.png")

        screen.blit(menu, (0, 0))
        pygame.display.update()

        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
            #Si on appuie sur ces boutons :
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if 867 < mouseX < 890 and 315 < mouseY < 355 :
                    difficulte = 1
                    MAXMISSILE = 10
                    MINMINSSILE = 5
                    SPEED = 10
                    nbPieces = 5
                elif 935 < mouseX < 955 and 315 < mouseY < 355 :
                    difficulte = 2
                    MAXSPEED = 15
                    MINMISSILE = 10
                    SPEED = 15
                    nbPieces = 10
                elif 980 < mouseX < 1007 and 315 < mouseY < 355 :
                    difficulte = 3
                    MAXMISSILE = 20
                    MINMISSILE = 15
                    SPEED = 20
                    nbPieces = 15
                elif 555 < mouseX < 1090 and 222 < mouseY < 282 :
                    GAME = True
                    MENU = False
                    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                    InitJeu()
                    objet.nbObjets = 0

                
    #Pour le compteur au début de partie :
    firstTime = True

    while GAME == True :

        #3 2 1 pour le start :
        if firstTime == True :
            Depart()
        firstTime = False
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
            
            elif event.type == pygame.KEYDOWN and event.key ==  K_UP :
                lastEventType["Up"] = 1
            elif event.type == pygame.KEYDOWN and event.key == K_DOWN :
                lastEventType["Down"] = 1
            elif event.type == pygame.KEYDOWN and event.key == K_LEFT :
                lastEventType["Left"] = 1
            elif event.type == pygame.KEYDOWN and event.key == K_RIGHT :
                lastEventType["Right"] = 1
            elif event.type == pygame.KEYUP and event.key == K_UP :
                lastEventType["Up"] = 0
            elif event.type == pygame.KEYUP and  event.key == K_DOWN :
                lastEventType["Down"] = 0
            elif event.type == pygame.KEYUP and event.key == K_LEFT :
                lastEventType["Left"] = 0
            elif event.type == pygame.KEYUP and  event.key == K_RIGHT :
                lastEventType["Right"] = 0

        #Lorsque rien ne se passe :
        if pygame.event.get() == [] :
            fond.Initialise()
            personnage.Display()
        
        #Lorsqu'une seule touche est appuyée :

        if lastEventType["Up"] == 1 and lastEventType["Down"] == 0 and lastEventType["Left"] == 0 and lastEventType["Right"] == 0:
            fond.Initialise()
            personnage.Up()
        elif lastEventType["Down"] == 1 and lastEventType["Up"] == 0 and lastEventType["Left"] == 0 and lastEventType["Right"] == 0:
            fond.Initialise()
            personnage.Down()
        elif lastEventType["Left"] == 1 and lastEventType["Right"] == 0 and lastEventType["Up"] == 0 and lastEventType["Down"] == 0:
            fond.Initialise()
            personnage.Left()
        elif lastEventType["Right"] == 1 and lastEventType["Left"] == 0 and lastEventType["Up"] == 0 and lastEventType["Down"] == 0:
            fond.Initialise()
            personnage.Right()

        #déplacements lorsque deux touches sont appuyés :
        
        elif lastEventType["Up"] == 1 and lastEventType["Right"] == 1 and lastEventType["Left"] == 0 and lastEventType["Down"] == 0 :
            fond.Initialise()
            personnage.NE()
        elif lastEventType["Up"] == 1 and lastEventType["Left"] == 1 and lastEventType["Right"] == 0 and lastEventType["Down"] == 0 :
            fond.Initialise()
            personnage.NW()
        elif lastEventType["Down"] == 1 and lastEventType["Right"] == 1 and lastEventType["Left"] == 0 and lastEventType["Up"] == 0 :
            fond.Initialise()
            personnage.SE()
        elif lastEventType["Down"] == 1 and lastEventType["Left"] == 1 and lastEventType["Right"] == 0 and lastEventType["Up"] == 0 :
            fond.Initialise()
            personnage.SW() 
    
        objet.Display()
        MissileActualisation()
        CheckVictory()
        Score()

        pygame.display.update()
        clock.tick(30)

time.sleep(2)