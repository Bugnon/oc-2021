import pygame
from pygame.locals import *

class Fond() :
    def __init__(self) :
        self.case_image = pygame.image.load('sol.png')
    def Initialise(self) :
        for x in range(int(SCREEN_WIDTH / CASE)) :
            for y in range(int(SCREEN_HIGH / CASE)) :
                screen.blit(self.case_image, (x * CASE, y * CASE))
                pygame.display.update()


class Perso() :
    def __init__(self) :
        self.perso_image = pygame.image.load("mygale.jfif")
        self.x = (self.perso_image.get_rect()[2] + self.perso_image.get_rect()[0]) / 2
        self.y = (self.perso_image.get_rect()[3] + self.perso_image.get_rect()[1]) / 2
        self.largeur = self.perso_image.get_rect()[2] - self.perso_image.get_rect()[0]
        self.hauteur = self.perso_image.get_rect()[3] - self.perso_image.get_rect()[1]
        self.pos = (self.x, self.y)
    def DisplayCentre(self) :
        screen.blit(self.perso_image, ((SCREEN_WIDTH / 2) - (self.largeur / 2), (SCREEN_HIGH / 2) - (self.hauteur / 2)))
        pygame.display.update()
    def Display(self, nouvX, nouvY) :
        fond.Initialise()
        screen.blit(self.perso_image, (nouvX, nouvY))
        pygame.display.update()
    def Up(self) :
        self.y -= 10
        personnage.Display(self.x, self.y)
        pygame.display.update()
    def Down(self) :
        self.y += 10
        personnage.Display(self.x, self.y)
        pygame.display.update()
    def Left(self) :
        self.x -= 10
        personnage.Display(self.x, self.y)
        pygame.display.update()
    def Right(self) :
        self.x += 10
        personnage.Display(self.x, self.y)
        pygame.display.update()

    def NW(self) :
        self.x -= 15
        self.y -= 15
        personnage.Display(self.x, self.y)
        pygame.display.update()
    def NE(self) :
        self.x += 15
        self.y -= 15
        personnage.Display(self.x, self.y)
        pygame.display.update()
    def SW(self) :
        self.x -= 15
        self.y += 15
        personnage.Display(self.x, self.y)
        pygame.display.update()
    def SE(self) :
        self.x += 15
        self.y += 15
        personnage.Display(self.x, self.y)
        pygame.display.update()
        


#VARIABLES GLOBALES :

GAME = True
SCREEN_HIGH = 700
SCREEN_WIDTH = 1000
CASE = 100
SPEED = 10


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
            personnage.Up()
        elif event.type == pygame.KEYDOWN and event.key == K_DOWN :
            lastEventType["Down"] = 1
            personnage.Down()
        elif event.type == pygame.KEYDOWN and event.key == K_LEFT :
            lastEventType["Left"] = 1
            personnage.Left()
        elif event.type == pygame.KEYDOWN and event.key == K_RIGHT :
            lastEventType["Right"] = 1
            personnage.Right()
        elif event.type == pygame.KEYUP and event.key == K_UP :
            lastEventType["Up"] = 0
        elif event.type == pygame.KEYUP and  event.key == K_DOWN :
            lastEventType["Down"] = 0
        elif event.type == pygame.KEYUP and event.key == K_LEFT :
            lastEventType["Left"] = 0
        elif event.type == pygame.KEYUP and  event.key == K_RIGHT :
            lastEventType["Right"] = 0


        

        
    if lastEventType["Up"] == 1 :
        personnage.Up()
    elif lastEventType["Down"] == 1 :
        personnage.Down()
    elif lastEventType["Left"] == 1 :
        personnage.Left()
    elif lastEventType["Right"] == 1 :
        personnage.Right()
    elif lastEventType["Up"] == 1 and lastEventType["Right"] == 1 :
        personnage.NE()


    print(lastEventType)

        
        #print(lastEventType)

            


