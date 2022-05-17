""""TRON

Deux motos génèrent des traces derrière eux, et qui ne peut pas être franchi 

La trace est représenter

"""


import os
import pygame
pygame.init()
os.chdir('assets')
moto1image = pygame.image.load('Player1.png')
moto2image = pygame.image.load('Player2.png')
clock = pygame.time.Clock()

pygame.display.set_caption("TRON", 'moto.png')
screen = pygame.display.set_mode((500, 500))

class Game:
    def __init__(self):
        
        self.moto1 = Moto(moto1image,50 - moto1image.get_width() / 2,screen.get_height() / 2 - moto1image.get_height() / 2,[pygame.K_d,pygame.K_a,pygame.K_s,pygame.K_w],(255,0,0),180)
        self.moto2 = Moto(moto2image,screen.get_width() - 50 - moto1image.get_width() / 2,screen.get_height() / 2 - moto1image.get_height() / 2,[pygame.K_RIGHT,pygame.K_LEFT,pygame.K_DOWN,pygame.K_UP],(0,0,255),0)

class Moto(pygame.sprite.Sprite):
    def __init__(self,img,posx,posy,touches,couleur,rotation):
        super().__init__()
        self.health = 1
        self.max_health = 1
        self.velocity = 2
        self.base_image = img
        self.image = pygame.transform.rotate(self.base_image,rotation)
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
        self.dir = (0,0)
        if rotation == 0:
            self.dir = (-1,0)
        elif rotation == 180:
            self.dir = (1,0)
        self.line_points = [self.rect.x + self.image.get_width() / 2, self.rect.y + self.image.get_height() / 2]
        self.line_rect = []
        self.touches = touches
        self.color = couleur
    def left(self):
        self.line_points += self.rect.x + self.image.get_width() / 2, self.rect.y + self.image.get_height() / 2
        rect_a = self.image.get_rect()
        self.image = pygame.transform.rotate(self.base_image, 0)
        rect_b = self.image.get_rect()
        
        if rect_a != rect_b:
            pos = pos_apres_rot(self.dir,self.image,(0,1),(0,-1))
            self.rect.x += pos[0]
            self.rect.y += pos[1]
        self.dir = (-1,0)
    def down(self):
        self.line_points += self.rect.x + self.image.get_width() / 2, self.rect.y + self.image.get_height() / 2
        rect_a = self.image.get_rect()
        self.image = pygame.transform.rotate(self.base_image, 90)
        rect_b = self.image.get_rect()

        if rect_a != rect_b:
            pos = pos_apres_rot(self.dir,self.image,(1,0),(-1,0))
            self.rect.x += pos[0]
            self.rect.y += pos[1]
        self.dir = (0,-1)    
    def right(self):
        self.line_points += self.rect.x + self.image.get_width() / 2, self.rect.y + self.image.get_height() / 2
        rect_a = self.image.get_rect()
        self.image = pygame.transform.rotate(self.base_image, 180)
        rect_b = self.image.get_rect()

        if rect_a != rect_b:
            pos = pos_apres_rot(self.dir,self.image,(0,1),(0,-1))
            self.rect.x += pos[0]
            self.rect.y += pos[1]
        self.dir = (1,0)
    def up(self):
        self.line_points += self.rect.x + self.image.get_width() / 2, self.rect.y + self.image.get_height() / 2
        rect_a = self.image.get_rect()
        self.image = pygame.transform.rotate(self.base_image, 270)
        rect_b = self.image.get_rect()

        if rect_a != rect_b:
            pos = pos_apres_rot(self.dir,self.image,(1,0),(-1,0))
            self.rect.x += pos[0]
            self.rect.y += pos[1]
        self.dir = (0,1)

    def moto_controller(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == self.touches[0]:
                self.right()
            elif event.key == self.touches[1]:
                self.left()
            elif event.key == self.touches[2]:
                self.down()
            elif event.key == self.touches[3]:
                self.up()
    def move(self):
        self.rect.x += self.dir[0] * self.velocity
        self.rect.y -= self.dir[1] * self.velocity
        screen.blit(self.image, self.rect)
    
    def draw_trail(self):
        temps_entre_points = 0
        #Creer un points tous les temps_entre_points

        self.line_rect.clear()
        for i in range(int(len(self.line_points) / 2) - 1):
            self.line_rect += pygame.draw.line(screen,self.color,(self.line_points[2*i],self.line_points[2*i+1]),(self.line_points[2*i+2],self.line_points[2*i+3]),8)
        self.line_rect += pygame.draw.line(screen,self.color,(self.line_points[int(len(self.line_points)) - 2],self.line_points[int(len(self.line_points)) - 1]),(self.rect.x + self.image.get_width() / 2, self.rect.y + self.image.get_height() / 2),8)

    def collision_test(self):
        hit_list = []
        for i in range(int(len(self.line_rect) / 4)):
            rect = pygame.Rect(self.line_rect[(i*4):(i*4+4)])
            print(rect)
            if(self.rect.colliderect(rect)):
                hit_list.append(rect)
        print(hit_list)
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

son = pygame.mixer.Sound('music/music_game.wav')
son.play(loops=-1, maxtime=0, fade_ms=0)

bg = pygame.image.load('bg.png')
game = Game()
running = True
while running:
    fond(bg)
    for event in pygame.event.get():
        game.moto1.moto_controller(event)
        game.moto2.moto_controller(event)
        if event.type == pygame.QUIT:
           run = False
           pygame.quit()
    game.moto1.draw_trail()
    game.moto1.move()
    game.moto1.collision_test()
    game.moto2.draw_trail()
    game.moto2.move()
    game.moto2.collision_test()
    pygame.display.update()  
    clock.tick(60)