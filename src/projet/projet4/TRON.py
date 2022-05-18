from dis import dis
import os
import pygame
import math
pygame.init()
os.chdir('assets')
moto1image = pygame.image.load('Player1.png')
moto2image = pygame.image.load('Player2.png')
clock = pygame.time.Clock()

pygame.display.set_caption("TRON", 'moto.png')
screen = pygame.display.set_mode((500, 500))


class game:
    def __init__(self):
        
        self.moto1 = moto(moto1image,50 - moto1image.get_width() / 2,screen.get_height() / 2 - moto1image.get_height() / 2,[pygame.K_d,pygame.K_a,pygame.K_s,pygame.K_w],(255,0,0),180,"red")
        self.moto2 = moto(moto2image,screen.get_width() - 50 - moto1image.get_width() / 2,screen.get_height() / 2 - moto1image.get_height() / 2,[pygame.K_RIGHT,pygame.K_LEFT,pygame.K_DOWN,pygame.K_UP],(0,0,255),0,"blue")

def dist(xa,ya,xb,yb):
    return math.sqrt((xb - xa)**2 + (yb - ya)**2)

class moto(pygame.sprite.Sprite):
    def __init__(self,img,posx,posy,touches,couleur,rotation,name):
        super().__init__()
        self.name = name
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

        self.points = [self.rect.x + self.image.get_width() / 2, self.rect.y + self.image.get_height() / 2]
        self.maxpoints = 25
        self.d_entre_pts = 1
        self.points_distance = 1
        self.point_connecte = []
    def left(self):
        if self.dir == (-1,0):
            return
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
        if self.dir == (0,-1):
            return
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
        if self.dir == (1,0):
            return
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
        if self.dir == (0,1):
            return
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
        self.line_rect.clear()
        if dist(self.points[-2],self.points[-1],self.rect.x + self.image.get_width() / 2,self.rect.y + self.image.get_height() / 2) > self.d_entre_pts:
            if int(len(self.points) / 2) >= self.maxpoints:
                del self.points[0]
                del self.points[0]
            self.points.append(self.rect.x + self.image.get_width() / 2)
            self.points.append(self.rect.y + self.image.get_height() / 2)
        if int(len(self.points)) > 4:
            for i in range(0,int(len(self.points)) - 4,2):
                pygame.draw.line(screen,self.color,(self.points[i],self.points[i+1]),(self.points[i+2],self.points[i+3]),5)
        for i in range(0,int(len(self.line_points)),2):
                pygame.draw.circle(screen,self.color,(self.line_points[i],self.line_points[i+1]),2)
        
        coins_possibles = []
        for i in range(0,int(len(self.line_points)),2):
            if self.check_coin(self.line_points[i],self.line_points[i+1]) == True or self.point_connecte.count(i) > 0:
                coins_possibles.append(self.line_points[i])
                coins_possibles.append(self.line_points[i+1])
        for i in range(0,int(len(coins_possibles)) - 3,2):
            self.line_rect += pygame.draw.line(screen,self.color,(coins_possibles[i],coins_possibles[i+1]),(coins_possibles[i+2],coins_possibles[i+3]),5)
            if(self.point_connecte.count(i) == 0):
                self.point_connecte.append(i)

        if(len(coins_possibles)) > 1:
            self.line_rect += pygame.draw.line(screen,self.color,(coins_possibles[-2],coins_possibles[-1]),(self.points[0],self.points[1]),5)

    def check_coin(self,posx,posy):
        for i in range(0,int(len(self.points)),2):
            if not dist(posx,posy,self.points[i],self.points[i+1]) > self.points_distance:
                return False
        return True
    
    def get_collision(self):
        collisions.extend(self.line_rect)
    
    def apply_collision(self):
        hit_list = []
        for i in range(0,int(len(collisions)),4):
            rect = pygame.Rect(collisions[(i):(i+4)])
            if(self.rect.colliderect(rect)):
                hit_list.append(rect)
        if len(hit_list) != 0:
            print(self.name,"COLLISION")
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

son = pygame.mixer.Sound('music/music_TRON.wav')
son.set_volume(0.1)
son.play(loops=-1, maxtime=0, fade_ms=0)

bg = pygame.image.load('bg.png')
game = game()
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
    game.moto2.draw_trail()
    game.moto1.move()
    game.moto2.move()
    collisions = []
    game.moto1.get_collision()
    game.moto2.get_collision()
    game.moto1.apply_collision()
    game.moto2.apply_collision()
    pygame.display.update()  
    clock.tick(60)