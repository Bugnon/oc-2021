import math
import pygame
pygame.init()

moto1image = pygame.image.load('assets/Player1.png')

clock = pygame.time.Clock()

class game:
    def __init__(self):
        self.moto1 = moto1()

class moto1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 1
        self.max_health = 1
        self.velocity = 2
        self.image = moto1image
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 238
        self.dir = (-1,0)

    def left(self):
        rect_a = self.image.get_rect()
        self.image = pygame.transform.rotate(moto1image, 0)
        rect_b = self.image.get_rect()
        
        if rect_a != rect_b:
            pos = pos_apres_rot(self.dir,self.image,(0,1),(0,-1))
            self.rect.x += pos[0]
            self.rect.y += pos[1]
        self.dir = (-1,0)
    def down(self):
        rect_a = self.image.get_rect()
        self.image = pygame.transform.rotate(moto1image, 90)
        rect_b = self.image.get_rect()

        if rect_a != rect_b:
            pos = pos_apres_rot(self.dir,self.image,(1,0),(-1,0))
            self.rect.x += pos[0]
            self.rect.y += pos[1]
        self.dir = (0,-1)     
    def right(self):

        rect_a = self.image.get_rect()
        self.image = pygame.transform.rotate(moto1image, 180)
        rect_b = self.image.get_rect()

        if rect_a != rect_b:
            pos = pos_apres_rot(self.dir,self.image,(0,1),(0,-1))
            self.rect.x += pos[0]
            self.rect.y += pos[1]
        self.dir = (1,0)
    def up(self):

        rect_a = self.image.get_rect()
        self.image = pygame.transform.rotate(moto1image, 270)
        rect_b = self.image.get_rect()

        if rect_a != rect_b:
            pos = pos_apres_rot(self.dir,self.image,(1,0),(-1,0))
            self.rect.x += pos[0]
            self.rect.y += pos[1]
        self.dir = (0,1)

    def move(self):
        self.rect.x += self.dir[0] * self.velocity
        self.rect.y -= self.dir[1] * self.velocity
        screen.blit(game.moto1.image, game.moto1.rect)
    
    def trail(self,screen,img):
        if self.dir[0] != 0: #si on est horizontal
            if self.dir[0] == -1:
                screen.blit(img, (self.rect.x + self.image.get_width(),self.rect.y + self.image.get_height() / 2 - img.get_height() / 2))
            elif self.dir[0] == 1:
                screen.blit(img, (self.rect.x - img.get_width(),self.rect.y + self.image.get_height() / 2 - img.get_height() / 2))
        elif self.dir[1] != 0: #si on est vertical
            if self.dir[1] == -1:
                screen.blit(img, (self.rect.x + self.image.get_width() / 2 - img.get_width() / 2,self.rect.y - img.get_height()))
            elif self.dir[1] == 1:
                screen.blit(img, (self.rect.x + self.image.get_width() / 2 - img.get_width() / 2,self.rect.y + self.image.get_height()))

def pos_apres_rot(dirbase,image,dir1,dir2):
    pos = [0,0]
    if(dirbase == dir1 or dirbase == dir2):
        pos[0] -= image.get_width() / 2 - image.get_height() / 2
        pos[1] += image.get_width() / 2 - image.get_height() / 2
    return pos

def fond(image):
    # /!\ il faut que la largeur et longueur de la fenetre soit un multiple de 100 car le fond fait 100x100 px
    nb_x = int(screen.get_width() / 100)
    nb_y = int(screen.get_height() / 100)

    for x in range(nb_x):
        for y in range(nb_y):
            screen.blit(image, (x * 100, y * 100))


pygame.display.set_caption("TRON", 'assets/moto.png')
screen = pygame.display.set_mode((500, 500))



bg = pygame.image.load('assets/bg.png')
def moto1_controller(event, moto):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_d:
            moto.right()
        elif event.key == pygame.K_a:
            moto.left()
        elif event.key == pygame.K_s:
            moto.down()
        elif event.key == pygame.K_w:
            moto.up()
game = game()
running = True
while running:
    fond(bg)
    for event in pygame.event.get():
        moto1_controller(event,game.moto1)
        if event.type == pygame.QUIT:
           run = False
           pygame.quit()
    game.moto1.move()
    game.moto1.trail(screen,bg)
    pygame.display.update()  
    clock.tick(60)