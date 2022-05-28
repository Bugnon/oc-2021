import pygame
from pygame.locals import *
import time



class Fond() :
    def __init__(self) :
        self.fond = pygame.image.load('src/projet/projet2/images/salleDongeon.png')
    def Initialise(self) :
        screen.blit(self.fond, (0, 0))


class Perso() :
    def __init__(self) :
        self.perso_image = pygame.image.load("src/projet/projet2/images/perso.png")
        self.x = (self.perso_image.get_rect()[2] + self.perso_image.get_rect()[0]) / 2
        self.y = (self.perso_image.get_rect()[3] + self.perso_image.get_rect()[1]) / 2
        self.largeur = self.perso_image.get_rect()[2] - self.perso_image.get_rect()[0]
        self.hauteur = self.perso_image.get_rect()[3] - self.perso_image.get_rect()[1]
        self.pos = (self.x, self.y)
        self.checkColl = self.CheckCollision() 
    def DisplayCentre(self) :
        screen.blit(self.perso_image, ((1000, 1000)))
        pygame.display.update()
    def Display(self, nouvX, nouvY) :
        fond.Initialise()
        screen.blit(self.perso_image, (nouvX, nouvY))
        pygame.display.update()
    def CheckCollision(self) :
        if self.perso_image.get_rect()[0] <= 60 or self.perso_image.get_rect()[1] <= 360 or self.perso_image.get_rect()[3] >= 1135 or self.perso_image.get_rect()[4] >= 896 :
            return True
        else :
            return False
    def Up(self) :
        if self.checkColl == False :
            self.y -= SPEED
        personnage.Display(self.x, self.y)
        pygame.display.update()
    def Down(self) :
        if self.checkColl == False :
            self.y += SPEED
        personnage.Display(self.x, self.y)
        pygame.display.update()
    def Left(self) :
        if self.checkColl == False :
            self.x -= SPEED
        personnage.Display(self.x, self.y)
        pygame.display.update()
    def Right(self) :
        if self.checkColl == False :
            self.x += SPEED
        personnage.Display(self.x, self.y)
        pygame.display.update()

    def NW(self) :
        if self.checkColl == False :
            self.x -= SPEED / (2 ** 0.5)
            self.y -= SPEED / (2 ** 0.5)
        personnage.Display(self.x, self.y)
        pygame.display.update()
    def NE(self) :
        if self.checkColl == False :
            self.x += SPEED / (2 ** 0.5)
            self.y -= SPEED / (2 ** 0.5)
        personnage.Display(self.x, self.y)
        pygame.display.update()
    def SW(self) :
        if self.checkColl == False :
            self.x -= SPEED / (2 ** 0.5)
            self.y += SPEED / (2 ** 0.5)
        personnage.Display(self.x, self.y)
        pygame.display.update()
    def SE(self) :
        if self.checkColl == False :
            self.x += SPEED / (2 ** 0.5)
            self.y += SPEED / (2 ** 0.5)
        personnage.Display(self.x, self.y)
        pygame.display.update()
        


#VARIABLES GLOBALES :

GAME = True
SCREEN_HIGH = 960
SCREEN_WIDTH = 1200
CASE = 120
SPEED = 15

#Début
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGH))



fond = Fond()
fond.Initialise()

personnage = Perso()
personnage.DisplayCentre()



lastEventType = {"Up" : 0, "Down" : 0, "Left" : 0, "Right" : 0}
listOfKeys = list(lastEventType.keys())
lastPressedKey = []


while GAME == True :
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

    pygame.display.update() 




